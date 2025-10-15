
"""
md_directives.py
================

提供从 LLM 产出的 JSON → Markdown，再到按 Markdown 中“文件指令”落盘（新建/替换/删除）的全流程工具。

包含函数：
1) application_to_md(json_file, md_file)
   - 从 JSON 中提取 outputs.text（支持根层或嵌套 data.outputs），生成 Markdown。
2) parse_md_directives(md_text) -> list[Directive]
   - 解析 MD 中的“文件指令”，支持三种语法（详见下方），自动关联紧随其后的代码块。
3) apply_file_directives(directives, project_root, dry_run=False, backup=True) -> list[dict]
   - 在 project_root 下安全执行 create/replace/delete（目录越权防护、备份、删除进 .trash）。
4) process_md_file(md_path, project_root, dry_run=False) -> dict
   - 读取 MD → 解析 → 执行，返回报告。

支持的指令写法（任选其一）：

A) HTML 注释头（顺序不限，冒号或等号均可）：
   <!-- action:create; path: src/app.py; encoding:utf-8 -->
   ```python
   print("hello")
   ```

B) 标签/粗体头：
   **[FILE action=create path=src/app.py encoding=utf-8]**
   ```python
   print("hello")
   ```

C) 自然语言行（中英兼容）：
   新规文件: src/app.py
   替换文件: src/app.py
   删除文件: src/app.py
   Create file: src/app.py
   Replace file: src/app.py
   Delete file: src/app.py
   （需要内容时，下一段使用代码块）

约定：
- delete 不需要代码块；create/replace 必须紧随一个完整的代码块（``` 或 ~~~）。
- 所有相对路径均解析到 project_root 下；绝对路径会被相对化映射到 project_root 以避免越权。
"""

from __future__ import annotations

import os
import re
import json
import shutil
import datetime as _dt
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List, Dict

# -------------------------
# JSON → Markdown
# -------------------------

def _find_outputs(obj: dict) -> dict:
    """在根或 data 里查找 outputs；如失败则尝试浅层遍历。"""
    if isinstance(obj, dict):
        if 'outputs' in obj and isinstance(obj['outputs'], dict):
            return obj['outputs']
        if 'data' in obj and isinstance(obj['data'], dict) and 'outputs' in obj['data'] and isinstance(obj['data']['outputs'], dict):
            return obj['data']['outputs']
        # 宽松：在一层内递归找 'outputs'
        for v in obj.values():
            if isinstance(v, dict) and 'outputs' in v and isinstance(v['outputs'], dict):
                return v['outputs']
    raise ValueError("JSON结构中未找到 outputs 字段（或 outputs 非对象）。")

def application_to_md(json_file: str, md_file: str) -> None:
    """
    读取 JSON 文件，提取 outputs.text 字段内容，格式化为 Markdown 保存。
    - 保留用户换行，不做额外段落重写。
    - 对部分英文标题做轻量替换（可按需扩展）。
    """
    obj = json.loads(Path(json_file).read_text(encoding='utf-8'))
    outputs = _find_outputs(obj)
    text = outputs.get('text', '')
    if isinstance(text, list):
        text = "\n\n".join(str(x) for x in text)
    else:
        text = str(text or '')
    md_text = text.strip()

    # 轻量 heading 标记（按需可扩展）
    replacements = {
        'Proposal Title:': '## Proposal Title\n',
        'Executive Summary:': '## Executive Summary\n',
    }
    for k, v in replacements.items():
        md_text = md_text.replace(k, v)

    Path(md_file).parent.mkdir(parents=True, exist_ok=True)
    Path(md_file).write_text(md_text, encoding='utf-8')


# -------------------------
# Markdown 指令解析
# -------------------------

# 动作别名
_ACTION_ALIASES = {
    'create':'create','new':'create','新增':'create','新规':'create','新建':'create',
    'replace':'replace','overwrite':'replace','覆盖':'replace','替换':'replace','替換':'replace',
    'delete':'delete','remove':'delete','删除':'delete','刪除':'delete','移除':'delete',
}

def _norm_action(raw: str) -> Optional[str]:
    if not raw: return None
    return _ACTION_ALIASES.get(raw.strip().lower())

# 兼容的多种语法
# A) HTML 注释：允许 'key:value' 或 'key=value'，顺序任意；至少包含 action/path
_RE_HTML = re.compile(
    r'<!--\s*(?P<body>[^>]*?)\s*-->',
    re.IGNORECASE
)
def _parse_html_kvs(body: str) -> Dict[str,str]:
    kvs = {}
    # 分割 ; 或 , 为项
    for part in re.split(r'[;,]\s*', body.strip()):
        if not part: continue
        m = re.match(r'(file|path|action|操作|encoding)\s*[:=]\s*(.+)$', part.strip(), re.IGNORECASE)
        if not m: continue
        key = m.group(1).lower()
        val = m.group(2).strip()
        key = 'path' if key in ('file','path') else ('action' if key in ('action','操作') else key)
        kvs[key] = val
    return kvs

# B) 标签/粗体头
_RE_LABEL = re.compile(
    r'^\s*(\*\*)?\[?FILE\s+action=(?P<action>\w+)\s+path=(?P<path>\S+)(?:\s+encoding=(?P<encoding>[-\w]+))?\]?(?:\*\*)?\s*$',
    re.IGNORECASE
)

# C) 自然语言行
_RE_NATURE = re.compile(
    r'^\s*(?P<prefix>(新规|新建|新增|替换|覆盖|删除|刪除|移除|create|replace|overwrite|delete)\s*文件?)\s*[:：]\s*(?P<path>\S+)\s*$',
    re.IGNORECASE
)

# 简单标签（备选）： [FILE create] path/to/file
_RE_SIMPLE = re.compile(
    r'^\s*\[FILE\s+(?P<action>\w+)\]\s*(?P<path>\S+)\s*$',
    re.IGNORECASE
)

# 代码块（``` 或 ~~~）
_RE_FENCE_START = re.compile(r'^\s*(```|~~~)(?P<lang>[\w#+-]*)\s*$')
_RE_FENCE_END   = re.compile(r'^\s*(```|~~~)\s*$')

@dataclass
class Directive:
    action: str
    path: str
    encoding: str = 'utf-8'
    lang: Optional[str] = None
    content: Optional[str] = None
    origin: str = ''  # 调试用原始行
    # 解析后路径
    abs_path: Optional[Path] = None
    rel_path: Optional[Path] = None

def parse_md_directives(md_text: str) -> List[Directive]:
    """
    从 Markdown 文本中提取“文件指令”列表；
    - delete：不要求代码块
    - create/replace：必须紧随（允许空行/注释）一个完整代码块
    """
    lines = md_text.splitlines()
    directives: List[Directive] = []

    pending: Optional[Directive] = None
    waiting_code = False
    in_code = False
    buf: List[str] = []
    lang: Optional[str] = None

    def flush_if_ready():
        nonlocal pending, waiting_code, in_code, buf, lang
        if not pending: return
        if pending.action == 'delete':
            directives.append(pending)
            pending = None; waiting_code=False; buf.clear(); lang=None
        else:
            if not buf:
                raise ValueError(f"缺少代码块内容：{pending.origin}")
            pending.content = "\n".join(buf)
            pending.lang = lang
            directives.append(pending)
            pending = None; waiting_code=False; buf.clear(); lang=None

    i = 0
    while i < len(lines):
        line = lines[i]

        # 若等待代码块，跳过空白/注释直到遇到 fenced start
        if waiting_code and not in_code:
            mfs = _RE_FENCE_START.match(line)
            if mfs:
                in_code = True
                lang = (mfs.group('lang') or '').strip() or None
                i += 1
                continue
            # 允许 HTML 注释/空行
            if _RE_HTML.match(line) or not line.strip():
                i += 1
                continue
            # 其它文本遇到则判为异常：指令后不跟代码块
            raise ValueError(f"期望出现代码块：{pending.origin}，但遇到：{line[:80]}")

        # 采集代码块内容
        if in_code:
            if _RE_FENCE_END.match(line):
                in_code = False
                flush_if_ready()
                i += 1
                continue
            buf.append(line)
            i += 1
            continue

        # 尝试解析 4 种指令样式
        hit = None
        # A) HTML 注释
        mh = _RE_HTML.search(line)
        if mh:
            kvs = _parse_html_kvs(mh.group('body') or '')
            if 'action' in kvs and 'path' in kvs:
                act = _norm_action(kvs.get('action'))
                if not act:
                    raise ValueError(f"无法识别的 action：{kvs.get('action')} @ {line}")
                pending = Directive(action=act, path=kvs['path'], encoding=kvs.get('encoding','utf-8'), origin=line.strip())
                waiting_code = (act != 'delete')
                i += 1
                continue

        # B) 标签/粗体头
        ml = _RE_LABEL.match(line)
        if ml:
            act = _norm_action(ml.group('action'))
            if not act: raise ValueError(f"无法识别的 action：{ml.group('action')} @ {line}")
            pending = Directive(action=act, path=ml.group('path'), encoding=(ml.group('encoding') or 'utf-8'), origin=line.strip())
            waiting_code = (act != 'delete')
            i += 1
            continue

        # C) 自然语言行
        mn = _RE_NATURE.match(line)
        if mn:
            prefix = mn.group('prefix')
            # 仅取“新规/替换/删除/create/replace/delete”部分
            raw = re.split(r'\s*文件?$', prefix.strip(), maxsplit=1)[0]
            act = _norm_action(raw)
            if not act: raise ValueError(f"无法识别的 action：{raw} @ {line}")
            pending = Directive(action=act, path=mn.group('path'), origin=line.strip())
            waiting_code = (act != 'delete')
            i += 1
            continue

        # 简单标签
        ms = _RE_SIMPLE.match(line)
        if ms:
            act = _norm_action(ms.group('action'))
            if not act: raise ValueError(f"无法识别的 action：{ms.group('action')} @ {line}")
            pending = Directive(action=act, path=ms.group('path'), origin=line.strip())
            waiting_code = (act != 'delete')
            i += 1
            continue

        i += 1

    if in_code:
        raise ValueError("Markdown 代码块未闭合（```/~~~ 缺失结束标记）。")
    if pending is not None:
        # 如果是 delete，没有代码块也可以直接落
        if pending.action == 'delete':
            directives.append(pending)
        else:
            raise ValueError(f"指令未跟随代码块：{pending.origin}")

    return directives


# -------------------------
# 指令执行（写盘）
# -------------------------

def _ensure_within(base: Path, target: Path) -> None:
    """确保 target 在 base 目录树下，防目录穿越。"""
    base_r = base.resolve()
    tgt_r  = target.resolve()
    if os.name == 'nt':
        ok = str(tgt_r).lower().startswith((str(base_r).lower() + os.sep))
    else:
        ok = str(tgt_r).startswith((str(base_r) + os.sep))
    if ok or base_r == tgt_r:
        return
    raise ValueError(f"阻止越权写入：{tgt_r} 不在 {base_r} 下")

def _backup_file(path: Path) -> Path:
    """生成 .bak 时间戳备份并返回备份路径。"""
    ts = _dt.datetime.now().strftime('%Y%m%d-%H%M%S')
    bak = path.with_suffix(path.suffix + f'.bak.{ts}')
    path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(str(path), str(bak))
    return bak

def _move_to_trash(path: Path, project_root: Path) -> Path:
    """将文件移动到 .trash/{ts}/ 原目录结构下。"""
    ts = _dt.datetime.now().strftime('%Y%m%d-%H%M%S')
    rel = path.relative_to(project_root)
    trash = project_root / '.trash' / ts / rel
    trash.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(path), str(trash))
    return trash

def apply_file_directives(directives: List[Directive], project_root: str | Path,
                          dry_run: bool = False, backup: bool = True) -> List[Dict]:
    """
    将 directives 应用到 project_root 下，返回每条操作的报告：
    {action, path, abs_path, status, detail}
    """
    project_root = Path(project_root).resolve()
    out: List[Dict] = []

    for d in directives:
        # 规范化目标路径：把绝对路径相对化到 project_root；相对路径直接拼接
        raw = Path(d.path)
        rel = raw if not raw.is_absolute() else Path(*raw.parts[1:])  # 去掉根/盘符部分
        abs_path = (project_root / rel).resolve()

        # 防越权
        _ensure_within(project_root, abs_path)

        d.rel_path = rel
        d.abs_path = abs_path

        rec = {"action": d.action, "path": str(rel).replace('\\','/'), "abs_path": str(abs_path)}
        try:
            if d.action == 'create':
                if abs_path.exists() and backup:
                    _backup_file(abs_path)
                if not dry_run:
                    abs_path.parent.mkdir(parents=True, exist_ok=True)
                    with open(abs_path, 'w', encoding=d.encoding) as f:
                        f.write(d.content or '')
                rec["status"] = "applied" if not dry_run else "dry-run"
                rec["detail"] = "created (overwritten if existed)"
            elif d.action == 'replace':
                if not abs_path.exists():
                    rec["status"] = "error"
                    rec["detail"] = "target not exists for replace"
                else:
                    if backup:
                        _backup_file(abs_path)
                    if not dry_run:
                        with open(abs_path, 'w', encoding=d.encoding) as f:
                            f.write(d.content or '')
                    rec["status"] = "applied" if not dry_run else "dry-run"
                    rec["detail"] = "replaced"
            elif d.action == 'delete':
                if not abs_path.exists():
                    rec["status"] = "skipped"
                    rec["detail"] = "file not exists"
                else:
                    if not dry_run:
                        _move_to_trash(abs_path, project_root)
                    rec["status"] = "applied" if not dry_run else "dry-run"
                    rec["detail"] = "moved to .trash"
            else:
                rec["status"] = "error"
                rec["detail"] = f"unknown action: {d.action}"
        except Exception as e:
            rec["status"] = "error"
            rec["detail"] = str(e)

        out.append(rec)

    return out


# -------------------------
# 综合处理（读取 MD → 执行）
# -------------------------

def process_md_file(md_path: str | Path, project_root: str | Path, dry_run: bool = False) -> Dict:
    md_path = Path(md_path)
    project_root = Path(project_root).resolve()
    text = md_path.read_text(encoding='utf-8')
    directives = parse_md_directives(text)
    report = apply_file_directives(directives, project_root, dry_run=dry_run, backup=True)
    return {"count": len(directives), "report": report}


# -------------------------
# CLI
# -------------------------

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Parse & apply file directives in a Markdown produced from JSON.")
    ap.add_argument("--json", help="input json file (with outputs.text)", required=True)
    ap.add_argument("--md-out", help="output markdown file path", required=True)
    ap.add_argument("--project-root", help="base project root to apply directives", required=True)
    ap.add_argument("--apply", action="store_true", help="apply directives (default: dry-run)")
    args = ap.parse_args()

    application_to_md(args.json, args.md_out)
    res = process_md_file(args.md_out, args.project_root, dry_run=not args.apply)
    print(json.dumps(res, ensure_ascii=False, indent=2))
