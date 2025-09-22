#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
将目录下实际为 JSON/JSON5 的 .yml/.yaml 文件转为 YAML（块风格）。
- 识别严格 JSON、带尾随逗号/注释的 JSON5（如已安装 json5）
- 未安装 json5 时，做保守预处理：仅去除结构性尾随逗号
"""

import argparse
import json
import re
import sys
from pathlib import Path

# 依赖：PyYAML 必需；json5 可选（pip install json5）
try:
    import yaml
except ImportError:
    print("缺少依赖：请先安装 PyYAML：pip install pyyaml", file=sys.stderr)
    sys.exit(1)

try:
    import json5  # 可解析尾随逗号、注释等
    HAS_JSON5 = True
except Exception:
    HAS_JSON5 = False


# ========= 改进部分：更鲁棒的 JSON/JSON5 判定 =========

_TRAILING_COMMA_PATTERN = re.compile(
    r"""
    (                               # 1: 结构体起始到逗号的主体（非贪婪）
      \{[^{}]*                      #   简单块，或…
      |
      \[[^\[\]]*                    #   简单数组
    )
    ,                               # 尾随逗号
    (\s*[\}\]])                     # 2: 紧接右花括号/右中括号
    """,
    re.VERBOSE,
)

def _strip_trailing_commas(text: str, max_iters: int = 50) -> str:
    """
    保守去除**结构结尾处**的尾随逗号，不试图解析字符串/转义（因此设定为多轮微调）。
    - 只消除形如  {...,} 或 [...,] 的逗号
    - 多轮直到稳定或达迭代上限
    """
    s = text
    for _ in range(max_iters):
        new = _TRAILING_COMMA_PATTERN.sub(r"\1\2", s)
        if new == s:
            break
        s = new
    return s

def load_json_like(text: str):
    """
    尝试按严格 JSON → JSON5（可选）→ 去逗号后 JSON 的顺序解析。
    成功返回 (True, obj)；失败返回 (False, None)。
    """
    s = text.strip()
    if not s:
        return False, None
    # 只对明显以 { 或 [ 开头的文本尝试（减少误判 YAML）
    if not (s.startswith("{") or s.startswith("[")):
        return False, None

    # 1) 严格 JSON
    try:
        return True, json.loads(s)
    except Exception:
        pass

    # 2) JSON5（若可用：可处理尾随逗号、注释、单引号等）
    if HAS_JSON5:
        try:
            return True, json5.loads(s)
        except Exception:
            pass

    # 3) 保守去掉结构尾逗号后再试 JSON
    s2 = _strip_trailing_commas(s)
    if s2 != s:
        try:
            return True, json.loads(s2)
        except Exception:
            pass

    return False, None

# ========= 其余逻辑与原脚本保持一致 =========

def to_yaml_str(obj) -> str:
    return yaml.safe_dump(
        obj,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    )

def process_file(path: Path, dry_run: bool = False, backup: bool = False) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            text = path.read_text(encoding="utf-8-sig")
        except Exception as e:
            print(f"[跳过] 读取失败：{path} - {e}")
            return False
    except Exception as e:
        print(f"[跳过] 读取失败：{path} - {e}")
        return False

    ok, obj = load_json_like(text)
    if not ok:
        return False

    yaml_text = to_yaml_str(obj)

    if dry_run:
        print(f"[将转换] {path}")
        return True

    try:
        if backup:
            bak = path.with_suffix(path.suffix + ".bak")
            if not bak.exists():
                bak.write_text(text, encoding="utf-8")
        path.write_text(yaml_text, encoding="utf-8")
        print(f"[已转换] {path}")
        return True
    except Exception as e:
        print(f"[失败] 写入失败：{path} - {e}")
        return False

def walk_and_convert(root: Path, dry_run: bool = False, backup: bool = False) -> dict:
    total = 0
    converted = 0
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix.lower() in (".yml", ".yaml"):
            total += 1
            if process_file(p, dry_run=dry_run, backup=backup):
                converted += 1
    return {"total_yaml_files": total, "converted": converted}

def main():
    parser = argparse.ArgumentParser(description="将目录下实际为 JSON/JSON5 的 .yml/.yaml 文件转为 YAML。")
    parser.add_argument("directory", help="待检查的根目录路径")
    parser.add_argument("--dry-run", action="store_true", help="试运行：仅打印将被转换的文件，不做任何写入")
    parser.add_argument("--backup", action="store_true", help="转换前为目标文件创建 .bak 备份")
    args = parser.parse_args()

    root = Path(args.directory).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        print(f"路径无效或不是目录：{root}", file=sys.stderr)
        sys.exit(2)

    stats = walk_and_convert(root, dry_run=args.dry_run, backup=args.backup)
    print(
        f"\n扫描完成：共发现 YAML 文件 {stats['total_yaml_files']} 个，"
        f"其中转换 {stats['converted']} 个（{'dry-run' if args.dry_run else '实际写入'}）。"
    )

if __name__ == "__main__":
    main()
