#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
xml_splitter.py
----------------
Split a large XML file into multiple <max_mb MB chunks while preserving structural integrity.

Approach
- Stream with xml.etree.ElementTree.iterparse to avoid loading whole file.
- Identify repeating child element under the root (either provided via --item-tag or auto-detected).
- Accumulate complete items and, before writing a chunk, simulate serialization to ensure chunk size < limit.
- Each output chunk has the same root tag/attributes/namespaces as the original.
- If a single item itself exceeds the limit, it will be written alone (and may exceed the limit), with a warning.

Usage
------
python xml_splitter.py input.xml --out-dir out --max-mb 10 --item-tag Record

Auto-detection
--------------
If --item-tag is omitted, the script will sample the first N direct children of root
and choose the most frequent tag as the item element.
"""

from __future__ import annotations
import argparse
import collections
import xml.etree.ElementTree as ET
from pathlib import Path
import io
import os
from typing import Dict, List, Tuple, Optional

def detect_item_tag(
    xml_path: Path,
    sample_limit: int = 500
) -> Tuple[str, Dict[str, str], str, Dict[str, str]]:
    """
    Return (item_tag, ns_map, root_tag, root_attrib).
    Uses a streaming parse: collect namespaces, find root, tally direct children tags.
    """
    ET.register_namespace('', '')  # harmless placeholder to keep ET from adding ns0 unless needed

    ns_map = {}   # prefix -> uri
    tag_counts = collections.Counter()
    root_tag = None
    root_attrib = {}
    depth = 0
    seen_root = False

    # Capture namespaces
    events = ('start', 'end', 'start-ns')
    for event, elem in ET.iterparse(str(xml_path), events=events):
        if event == 'start-ns':
            prefix, uri = elem  # type: ignore
            ns_map[prefix or ''] = uri
            # Register to preserve prefixes on serialization
            try:
                ET.register_namespace(prefix or '', uri)
            except Exception:
                pass
            continue

        if event == 'start':
            depth += 1
            if not seen_root:
                root_tag = elem.tag
                root_attrib = dict(elem.attrib)
                seen_root = True
                depth_root = depth
            continue

        if event == 'end':
            # direct child of root => depth == 2 (root=1, child=2), but careful
            if seen_root and depth == 2 and elem is not None:
                tag_counts[elem.tag] += 1
            # clear to free memory
            elem.clear()
            depth -= 1

        # Stop after enough samples
        if sum(tag_counts.values()) >= sample_limit:
            break

    if not tag_counts:
        raise RuntimeError("无法自动检测 item 元素：根下没有可识别的重复子元素。请用 --item-tag 指定。")

    item_tag, _ = tag_counts.most_common(1)[0]
    return item_tag, ns_map, root_tag, root_attrib


def chunk_serialize_size(root_tag: str, root_attrib: Dict[str, str], item_bytes_list: List[bytes]) -> int:
    """
    Build a small tree in-memory and return its serialized byte size.
    """
    root = ET.Element(root_tag, root_attrib)
    for b in item_bytes_list:
        root.append(ET.fromstring(b))
    bio = io.BytesIO()
    ET.ElementTree(root).write(bio, encoding="utf-8", xml_declaration=True)
    return len(bio.getvalue())


def write_chunk(
    out_dir: Path,
    base_name: str,
    part_idx: int,
    root_tag: str,
    root_attrib: Dict[str, str],
    item_bytes_list: List[bytes]
) -> Path:
    """
    Write a chunk to disk as base_name.part_idx.xml
    """
    out_path = out_dir / f"{base_name}.part{part_idx:04d}.xml"
    root = ET.Element(root_tag, root_attrib)
    for b in item_bytes_list:
        root.append(ET.fromstring(b))
    ET.ElementTree(root).write(out_path, encoding="utf-8", xml_declaration=True)
    return out_path


def split_xml(
    xml_path: Path,
    out_dir: Path,
    max_mb: float = 10.0,
    item_tag: Optional[str] = None,
    base_name: Optional[str] = None,
    detect_samples: int = 500
) -> list[Path]:
    """
    Split xml_path into chunks whose sizes are less than max_mb (MB).
    Returns list of written chunk paths.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    max_bytes = int(max_mb * 1024 * 1024)
    base_name = base_name or xml_path.stem

    # Detect metadata
    if item_tag:
        # Also capture ns/root
        ns_map = {}
        root_tag = None
        root_attrib = {}
        for event, elem in ET.iterparse(str(xml_path), events=("start", "start-ns")):
            if event == "start-ns":
                prefix, uri = elem  # type: ignore
                ns_map[prefix or ""] = uri
                try:
                    ET.register_namespace(prefix or "", uri)
                except Exception:
                    pass
                continue
            if root_tag is None:
                root_tag = elem.tag
                root_attrib = dict(elem.attrib)
                break
    else:
        item_tag, ns_map, root_tag, root_attrib = detect_item_tag(xml_path, sample_limit=detect_samples)

    if root_tag is None:
        raise RuntimeError("无法识别根元素。")

    written_paths = []
    buffer = []
    part_idx = 1
    depth = 0
    root_depth = None

    events = ("start", "end", "start-ns")
    for event, elem in ET.iterparse(str(xml_path), events=events):
        if event == "start-ns":
            prefix, uri = elem  # type: ignore
            try:
                ET.register_namespace(prefix or "", uri)
            except Exception:
                pass
            continue

        if event == "start":
            depth += 1
            if root_depth is None:
                root_depth = depth
            continue

        if event == "end":
            if elem.tag == item_tag and depth == (root_depth + 1 if root_depth else 2):
                item_bytes = ET.tostring(elem, encoding="utf-8")
                if buffer:
                    probe = buffer + [item_bytes]
                    sz = chunk_serialize_size(root_tag, root_attrib, probe)
                    if sz > max_bytes:
                        out_path = write_chunk(out_dir, base_name, part_idx, root_tag, root_attrib, buffer)
                        written_paths.append(out_path)
                        part_idx += 1
                        buffer = [item_bytes]
                        sz_single = chunk_serialize_size(root_tag, root_attrib, buffer)
                        if sz_single > max_bytes:
                            out_path = write_chunk(out_dir, base_name, part_idx, root_tag, root_attrib, buffer)
                            written_paths.append(out_path)
                            part_idx += 1
                            buffer = []
                    else:
                        buffer.append(item_bytes)
                else:
                    buffer.append(item_bytes)
                    sz_single = chunk_serialize_size(root_tag, root_attrib, buffer)
                    if sz_single > max_bytes:
                        out_path = write_chunk(out_dir, base_name, part_idx, root_tag, root_attrib, buffer)
                        written_paths.append(out_path)
                        part_idx += 1
                        buffer = []
                elem.clear()
            else:
                elem.clear()
            depth -= 1

    if buffer:
        out_path = write_chunk(out_dir, base_name, part_idx, root_tag, root_attrib, buffer)
        written_paths.append(out_path)

    return written_paths


def main():
    import argparse
    ap = argparse.ArgumentParser(description="Split large XML into <max-MB chunks while keeping structure.")
    ap.add_argument("xml", help="Input XML file path")
    ap.add_argument("-o", "--out-dir", default="xml_parts", help="Output directory")
    ap.add_argument("--max-mb", type=float, default=10.0, help="Max size per chunk in MB (default 10)")
    ap.add_argument("--item-tag", default=None, help="Name of the repeating child element under the root")
    ap.add_argument("--base-name", default=None, help="Base name for output files (default: input.stem)")
    ap.add_argument("--detect-samples", type=int, default=500, help="Child sampling size for auto-detection")
    args = ap.parse_args()

    xml_path = Path(args.xml)
    out_dir = Path(args.out_dir)
    parts = split_xml(
        xml_path=xml_path,
        out_dir=out_dir,
        max_mb=args.max_mb,
        item_tag=args.item_tag,
        base_name=args.base_name,
        detect_samples=args.detect_samples,
    )
    print(f"Written {len(parts)} files:")
    for p in parts:
        print("  ->", p)

if __name__ == "__main__":
    main()
