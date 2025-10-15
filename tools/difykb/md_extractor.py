
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
from render_mermaid import render_mermaid_ink, render_kroki
import pathlib

SKIP_LANGS = {"mermaid", "plaintext", "text"}

def extract_mermaid_blocks(md: str) -> List[str]:
    pattern = re.compile(
        r"```[ \t]*mermaid[^\n]*\n(.*?)\n```",
        re.IGNORECASE | re.DOTALL
    )
    blocks = pattern.findall(md)
    return [b.strip("\n") for b in blocks]


def extract_source_tree(md: str) -> Dict[str, Any]:
    code_blocks = re.findall(r"```[a-zA-Z0-9_-]*\n(.*?)\n```", md, flags=re.DOTALL)
    ascii_tree_block = None
    for block in code_blocks:
        if ("├──" in block) or ("└──" in block) or ("│" in block and ("├" in block or "└" in block)):
            ascii_tree_block = block.strip("\n")
            break
    if not ascii_tree_block:
        return {"raw": "", "paths": [], "tree": {}}

    lines = [ln.rstrip() for ln in ascii_tree_block.splitlines() if ln.strip()]
    root_name = None
    tree: Dict[str, Any] = {}
    stack: List[Dict[str, Any]] = []
    path_stack: List[str] = []
    paths: List[str] = []

    def clean_name(name: str):
        name = name.split("#", 1)[0].rstrip()
        is_dir = name.endswith("/")
        if is_dir:
            name = name[:-1]
        return name, is_dir

    def compute_level(prefix: str) -> int:
        return len(re.findall(r"(?:│\s{3}|\s{4})", prefix))

    i = 0
    if lines and ("├" not in lines[0] and "└" not in lines[0]):
        root_name, is_dir = clean_name(lines[0].strip())
        if not root_name:
            root_name = "root"
            is_dir = True
        tree[root_name] = {}
        stack = [tree[root_name]]
        path_stack = [root_name]
        i = 1
    else:
        root_name = "root"
        tree[root_name] = {}
        stack = [tree[root_name]]
        path_stack = [root_name]

    branch_re = re.compile(r"^(?P<prefix>[ \t│]*)(?:├──|└──)\s(?P<name>.+)$")
    for ln in lines[i:]:
        m = branch_re.match(ln)
        if not m:
            continue
        prefix = m.group("prefix")
        name_raw = m.group("name")
        name, is_dir = clean_name(name_raw)
        if not name:
            continue

        level = compute_level(prefix) + 1
        while len(stack) > level:
            stack.pop()
            path_stack.pop()
        while len(stack) < level:
            placeholder = {}
            parent = stack[-1]
            auto_name = f"__auto_dir_{len(parent)}"
            parent[auto_name] = placeholder
            stack.append(placeholder)
            path_stack.append(auto_name)

        parent = stack[-1]
        if is_dir:
            parent[name] = {}
            stack.append(parent[name])
            path_stack.append(name)
        else:
            parent[name] = None
            paths.append("/".join(path_stack + [name]))

        if is_dir:
            paths.append("/".join(path_stack))
            stack.pop()
            path_stack.pop()

    root_path = root_name
    if root_path not in paths:
        paths.insert(0, root_path)

    return {"raw": ascii_tree_block, "paths": paths, "tree": tree}


def _detect_path_from_first_line(code_text: str, lang: str) -> Tuple[str, str]:
    lines = code_text.splitlines()
    idx = 0
    while idx < len(lines) and lines[idx].strip() == "":
        idx += 1
    if idx >= len(lines):
        return "", code_text
    first = lines[idx].strip()

    m = re.match(r"^//\s*(?P<path>[^\\:*?\"<>|]+)$", first)
    if not m:
        m = re.match(r"^#\s*(?P<path>[^\\:*?\"<>|]+)$", first)
    if not m:
        m = re.match(r"^/\*\s*(?P<path>[^*]+?)\s*\*/$", first)
    if not m:
        m = re.match(r"^<!--\s*(?P<path>[^>]+)\s*-->$", first)
    if m:
        path = m.group("path").strip()
        rest = "\n".join(lines[:idx] + lines[idx+1:])
        return path, rest
    return "", code_text


def _detect_path_from_info_string(info: str) -> str:
    """
    支持类似：```ts title=src/app.ts 或 ```python file=src/main.py 或 ```tsx src/components/Button.tsx
    """
    if not info:
        return ""
    # split tokens; allow `key=value` or bare path as first non-lang token
    toks = info.split()
    if not toks:
        return ""
    # Drop first token if it's language
    lang = toks[0].lower()
    rest = toks[1:] if len(toks) > 1 else []

    # key=value
    for t in rest:
        m = re.match(r"(?:file|filename|path|title)\s*=\s*(?P<p>[^\\:*?\"<>|]+)$", t, flags=re.IGNORECASE)
        if m:
            return m.group("p").strip()

    # bare path token
    for t in rest:
        if "/" in t and not any(x in t for x in [":", "*", "?", "\"", "<", ">", "|"]):
            return t.strip()
    return ""


def extract_code_files(md: str, out_root: "Path", fallback: Optional[str] = None) -> list:
    """
    从 Markdown 中抽出代码块：
    1) 优先从首行注释读取路径；
    2) 再尝试从 fence info-string (```lang file=...) 读取路径；
    3) 若上述都失败：
       - fallback=None   -> 跳过
       - fallback='numbered' -> 输出到 code/<lang or txt>/<NNNN>.<ext>
    跳过语言：mermaid、plaintext、text
    """
    out_root = Path(out_root)
    out_root.mkdir(parents=True, exist_ok=True)

    fence_re = re.compile(r"```(?P<info>[^\n]*)\n(?P<body>.*?)(?:\n)```", re.DOTALL)
    written = []
    counter = 0

    for m in fence_re.finditer(md):
        info = (m.group("info") or "").strip()
        body = m.group("body")
        lang = (info.split()[0].strip() if info else "").lower()

        if lang in SKIP_LANGS:
            continue

        # 1) 首行注释
        path, content = _detect_path_from_first_line(body, lang)
        # 2) info-string
        if not path:
            p2 = _detect_path_from_info_string(info)
            if p2:
                path = p2
                content = body

        if path:
            path = path.lstrip("./").strip()
            if path.startswith("/") or ".." in path.split("/"):
                continue
            file_path = out_root / path
        else:
            # fallback
            if fallback != "numbered":
                continue
            counter += 1
            # ext 猜测
            ext = {
                "python": "py", "py": "py",
                "ts": "ts", "tsx": "tsx", "js": "js", "jsx": "jsx",
                "css": "css", "html": "html", "sh": "sh", "bash": "sh",
                "yaml": "yaml", "yml": "yml", "json": "json", "go": "go", "java": "java",
            }.get(lang, "txt")
            subdir = lang if lang else "txt"
            file_path = out_root / "code" / subdir / f"{counter:04d}.{ext}"
            content = body

        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content.rstrip() + "\n", encoding="utf-8")
        written.append(str(file_path.relative_to(out_root)))
    return written

def create_fs_from_tree(tree: Dict[str, Any], dst_root: Path) -> Dict[str, int]:
    """
    使用 os 函数按照 extract_source_tree 产生的嵌套字典，创建真实的目录与空文件。
    规则：
      - 字典节点 -> 目录（os.makedirs）
      - None     -> 文件（os.open 创建空文件）
    返回：{"dirs": 目录数, "files": 文件数}
    """
    import os
    from pathlib import Path

    dst_root = Path(dst_root)
    dst_root.mkdir(parents=True, exist_ok=True)

    stats = {"dirs": 0, "files": 0}

    def _walk(node: Dict[str, Any], base: Path):
        for name, child in node.items():
            safe_name = str(name).strip()
            target = base / safe_name
            if isinstance(child, dict):
                os.makedirs(target, exist_ok=True)
                stats["dirs"] += 1
                _walk(child, target)
            else:
                os.makedirs(target.parent, exist_ok=True)
                fd = os.open(str(target), os.O_CREAT | os.O_WRONLY, 0o644)
                os.close(fd)
                stats["files"] += 1

    # 顶级通常是 {"<root>": {...}}
    for top, sub in tree.items():
        base = dst_root / str(top)
        if isinstance(sub, dict):
            os.makedirs(base, exist_ok=True)
            stats["dirs"] += 1
            _walk(sub, base)
        else:
            os.makedirs(base.parent, exist_ok=True)
            fd = os.open(str(base), os.O_CREAT | os.O_WRONLY, 0o644)
            os.close(fd)
            stats["files"] += 1
    return stats

def main():
    p = argparse.ArgumentParser(description="从 Markdown 中提取 mermaid 图、目录结构与代码文件")
    p.add_argument("input", help="输入的 .md 文件路径")
    p.add_argument("-o", "--outdir", default=".", help="输出目录（默认当前目录）")
    p.add_argument("--prefix", default="mermaid_", help="导出 .mmd 文件名前缀（默认 mermaid_）")
    p.add_argument("--paths-out", default="paths.txt", help="导出路径列表文件名（默认 paths.txt）")
    p.add_argument("--tree-json-out", default="tree.json", help="导出嵌套目录 JSON 文件名（默认 tree.json）")
    p.add_argument("--raw-tree-out", default="tree_raw.txt", help="导出原始目录块文件名（默认 tree_raw.txt）")
    p.add_argument("--code-out-root", default=None, help="将代码块写入此目录（根）")
    p.add_argument("--code-fallback", choices=["none","numbered"], default="none", help="当无法解析路径时的处理策略")

    args = p.parse_args()
    in_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    md = in_path.read_text(encoding="utf-8")

    # 1) Mermaid 提取
    mermaids = extract_mermaid_blocks(md)
    mermaid_files = []
    for i, m in enumerate(mermaids, start=1):
        fn = outdir / f"{args.prefix}{i}.mmd"
        fn.write_text(m + "\n", encoding="utf-8")
        mermaid_files.append(str(fn))
        diagram = pathlib.Path(str(fn)).read_text(encoding="utf-8")
        output_file_png = fn.with_suffix(".png")
        render_kroki(diagram, output_file_png)
        
    # 2) 目录结构提取
    st = extract_source_tree(md)

    raw_tree_path = outdir / args.raw_tree_out
    paths_path = outdir / args.paths_out
    tree_json_path = outdir / args.tree_json_out

    if st["raw"]:
        raw_tree_path.write_text(st["raw"] + "\n", encoding="utf-8")
    paths_path.write_text("\n".join(st["paths"]) + ("\n" if st["paths"] else ""), encoding="utf-8")
    tree_json_path.write_text(json.dumps(st["tree"], ensure_ascii=False, indent=2), encoding="utf-8")

    print("Mermaid blocks:", len(mermaids))
    for f in mermaid_files:
        print("  ->", f)
    print("Wrote:", raw_tree_path, paths_path, tree_json_path, sep="\\n  -> ")

    # 3) 代码文件抽出
    if args.code_out_root:
        written = extract_code_files(md, Path(args.code_out_root), fallback="numbered" if args.code_fallback=="numbered" else None)
        print(f"Code files extracted: {len(written)}")
        for w in written:
            print("  ->", w)

if __name__ == "__main__":
    main()
