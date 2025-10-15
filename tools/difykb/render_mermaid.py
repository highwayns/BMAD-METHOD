#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render_mermaid.py
将 Mermaid 文本渲染为 PNG/SVG，支持：
  --backend mermaid-ink  (GET /img|/svg/{pako:...}?type=png|svg)
  --backend kroki        (POST /mermaid/png|svg)
带健康检查与回落逻辑。
"""

import argparse, base64, zlib, pathlib, sys, requests, os
from typing import Optional, List, Dict

def _encode_pako(s: str) -> str:
    # raw DEFLATE (RFC-1951), no zlib header/trailer
    comp = zlib.compressobj(level=9, wbits=-15)
    data = comp.compress(s.encode("utf-8")) + comp.flush()
    b64  = base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")
    return "pako:" + b64

def _has_img_route(host: str) -> bool:
    try:
        t = requests.head(f"{host.rstrip('/')}/img/base64:QQ", timeout=2)
        return t.status_code == 200
    except Exception:
        return False

def pick_ink_host(pref: Optional[str]) -> str:
    cand = [pref] if pref else []
    # 依次尝试：环境变量 -> 参数 -> 常见本地端口 -> 公共服务
    env = os.environ.get("MERMAID_HOST")
    if env and env not in cand: cand.insert(0, env)
    for h in cand + ["http://localhost:3001", "http://localhost:3001", "https://mermaid.ink"]:
        if h and _has_img_route(h):
            return h
    return "https://mermaid.ink"

def render_mermaid_ink(diagram: str, host: str, outfile: str,
                       theme="default", bgColor="!white", scale=2, fmt="png"):
    host = pick_ink_host(host)
    encoded = _encode_pako(diagram)
    path = "img" if fmt != "svg" else "svg"
    url  = f"{host.rstrip('/')}/{path}/{encoded}"
    params = {"type": fmt, "theme": theme, "bgColor": bgColor, "scale": str(scale)}
    r = requests.get(url, params=params, timeout=60)
    try:
        r.raise_for_status()
    except requests.HTTPError as e:
        hint = ""
        if r.status_code == 404:
            hint = "（疑似连接到了前端站点而非 mermaid.ink 渲染器；请确认端口与容器映射是否正确）"
        elif r.status_code == 431:
            hint = "（URL/请求头过长；请改用 Kroki 后端的 POST 模式）"
        raise SystemExit(f"[mermaid-ink] HTTP {r.status_code} {hint}\nURL: {r.url}") from e
    pathlib.Path(outfile).write_bytes(r.content)

def render_kroki(diagram: str, output: str, host="https://kroki.io", fmt="png", timeout=60):
    url = f"{host.rstrip('/')}/mermaid/{fmt}"
    headers = {"Content-Type": "text/plain; charset=utf-8"}
    r = requests.post(url, data=diagram.encode("utf-8"), headers=headers, timeout=timeout)
    r.raise_for_status()
    pathlib.Path(output).write_bytes(r.content)
    print(f"✅ 已保存：{output}")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--backend", choices=["mermaid-ink", "kroki"], default="mermaid-ink")
    p.add_argument("--host", help="服务地址：mermaid-ink 默认自动探测（本地→公共）；Kroki 默认 http://localhost:8006")
    p.add_argument("--format", choices=["png", "svg"], default="png", help="输出格式")
    p.add_argument("-i", "--input", help="Mermaid 源文件（.mmd）。留空或 '-' 则从标准输入读取。")
    p.add_argument("-o", "--output", default="diagram.png", help="输出文件名")
    p.add_argument("--theme", default="default")
    p.add_argument("--bg-color", default="!white")
    p.add_argument("--scale", type=float, default=2.0)
    args = p.parse_args()

    if args.input and args.input != "-":
        diagram = pathlib.Path(args.input).read_text(encoding="utf-8")
    else:
        diagram = sys.stdin.read()

    if args.backend == "mermaid-ink":
        # mermaid.ink：GET /img|/svg/{pako:...}?type=...
        out = args.output
        if args.format == "svg" and not out.lower().endswith(".svg"):
            out = pathlib.Path(out).with_suffix(".svg")
        render_mermaid_ink(diagram, args.host, str(out),
                           theme=args.theme, bgColor=args.bg_color,
                           scale=args.scale, fmt=args.format)
    else:
        # Kroki：POST /mermaid/{png|svg}
        out = args.output
        if args.format == "svg" and not out.lower().endswith(".svg"):
            out = pathlib.Path(out).with_suffix(".svg")
        render_kroki(diagram, str(out))

    print(f"✅ 输出已保存：{out}")

if __name__ == "__main__":
    main()
