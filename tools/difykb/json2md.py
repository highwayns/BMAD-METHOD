import json
import os
import argparse
import re
from typing import List

def tutorial_to_md(json_file, md_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    course_name = data['data']['outputs']['course_name']
    chapters = data['data']['outputs']['course']

    # 开始写markdown
    with open(md_file, 'w', encoding='utf-8') as md:
        md.write(f'# {course_name}\n\n')
        for chapter in chapters:
            info = chapter['info']
            # 输出章节标题和小节标题
            md.write(f"## {info['chapter']} {info['title']}\n\n")
            md.write(f"### {info['subtitle']}\n\n")
            # 输出课程内容
            md.write(chapter['course'].strip())
            md.write('\n\n---\n\n') # 分隔线


def application_to_md(json_file, md_file):
    """
    读取 JSON 文件，提取 outputs.text 字段内容，格式化为 Markdown 保存
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        obj = json.load(f)

    # 定位到 outputs.text（支持直接在根或多级嵌套）
    outputs = None
    if 'outputs' in obj:
        outputs = obj['outputs']
    elif 'data' in obj and 'outputs' in obj['data']:
        outputs = obj['data']['outputs']
    else:
        raise ValueError("JSON结构中未找到 outputs 字段！")
    
    text = outputs.get('text', '').strip()
    # 替换 \n\n 为 markdown 段落，单独一行的\n为换行
    # 其实 markdown 支持双回车分段，直接写就行
    md_text = text.replace('\n\n', '\n\n').replace('\n', '\n')
    # 你也可以处理英文冒号换成 markdown 标题
    md_text = md_text.replace('Proposal Title:', '## Proposal Title\n')
    md_text = md_text.replace('Executive Summary:', '## Executive Summary\n')

    with open(md_file, 'w', encoding='utf-8') as md:
        md.write(md_text)

    print(f'Markdown已写入：{md_file}')

def extract_yaml_blocks(text: str) -> List[str]:
    """
    Return all contents between ```yaml ... ``` (or ```yml ... ```).
    Strips the surrounding fences but preserves inner whitespace.
    """
    pattern = re.compile(r"```ya?ml\s*(.*?)\s*```", re.DOTALL | re.IGNORECASE)
    return pattern.findall(text)

def result_to_md(json_file, md_file):
    """
    读取 JSON 文件，提取 outputs.text 字段内容，格式化为 Markdown 保存
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        obj = json.load(f)

    # 定位到 outputs.text（支持直接在根或多级嵌套）
    outputs = None
    if 'outputs' in obj:
        outputs = obj['outputs']
    elif 'data' in obj and 'outputs' in obj['data']:
        outputs = obj['data']['outputs']
    else:
        raise ValueError("JSON结构中未找到 outputs 字段！")
    
    text = outputs.get('result', '').strip()
    #text = extract_yaml_blocks(text)
    # 替换 \n\n 为 markdown 段落，单独一行的\n为换行
    # 其实 markdown 支持双回车分段，直接写就行
    md_text = text.replace('\n\n', '\n\n').replace('\n', '\n')
    # 你也可以处理英文冒号换成 markdown 标题
    md_text = md_text.replace('Proposal Title:', '## Proposal Title\n')
    md_text = md_text.replace('Executive Summary:', '## Executive Summary\n')

    with open(md_file, 'w', encoding='utf-8') as md:
        md.write(md_text)

    print(f'Markdown已写入：{md_file}')

def translate_to_md(json_file, md_file):
    """
    读取 JSON 文件，提取 outputs.text 字段内容，格式化为 Markdown 保存
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        obj = json.load(f)

    # 定位到 outputs.text（支持直接在根或多级嵌套）
    outputs = None
    if 'outputs' in obj:
        outputs = obj['outputs']
    elif 'data' in obj and 'outputs' in obj['data']:
        outputs = obj['data']['outputs']
    else:
        raise ValueError("JSON结构中未找到 outputs 字段！")
    
    text = outputs.get('final', '').strip()
    # 替换 \n\n 为 markdown 段落，单独一行的\n为换行
    # 其实 markdown 支持双回车分段，直接写就行
    md_text = text.replace('\n\n', '\n\n').replace('\n', '\n')
    # 你也可以处理英文冒号换成 markdown 标题
    md_text = md_text.replace('Proposal Title:', '## Proposal Title\n')
    md_text = md_text.replace('Executive Summary:', '## Executive Summary\n')

    with open(md_file, 'w', encoding='utf-8') as md:
        md.write(md_text)

    print(f'Markdown已写入：{md_file}')

def answer_to_md(json_file, md_file):
    """
    读取 JSON 文件，提取 outputs.text 字段内容，格式化为 Markdown 保存
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        obj = json.load(f)

    # 定位到 outputs.text（支持直接在根或多级嵌套）
    answer = None
    if 'answer' in obj:
        answer = obj['answer']
    elif 'data' in obj and 'answer' in obj['data']:
        outputs = obj['data']['answer']
    else:
        raise ValueError("JSON结构中未找到 answer 字段！")
    
    text = answer.strip()
    # 替换 \n\n 为 markdown 段落，单独一行的\n为换行
    # 其实 markdown 支持双回车分段，直接写就行
    md_text = text.replace('\n\n', '\n\n').replace('\n', '\n')
    # 你也可以处理英文冒号换成 markdown 标题
    md_text = md_text.replace('Proposal Title:', '## Proposal Title\n')
    md_text = md_text.replace('Executive Summary:', '## Executive Summary\n')

    with open(md_file, 'w', encoding='utf-8') as md:
        md.write(md_text)

    print(f'Markdown已写入：{md_file}')

import json

def html_to_md(html):
    """将HTML字符串转为Markdown（简单场景）"""
    try:
        from markdownify import markdownify as md
    except ImportError:
        raise ImportError("请先运行：pip install markdownify")
    return md(html, heading_style="ATX")  # 支持#风格标题

def report_to_md(json_file, md_file):
    """
    读取JSON文件，提取outputs.output字段，将HTML内容转为Markdown
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        obj = json.load(f)

    # 定位 outputs.output
    outputs = None
    if 'outputs' in obj:
        outputs = obj['outputs']
    elif 'data' in obj and 'outputs' in obj['data']:
        outputs = obj['data']['outputs']
    else:
        raise ValueError("JSON结构中未找到 outputs 字段！")

    html = outputs.get('output', '').strip()
    md_text = html_to_md(html)

    with open(md_file, 'w', encoding='utf-8') as md:
        md.write(md_text)
    print(f'Markdown已写入：{md_file}')

# ----------------------------
# 前面方法都保留，只需再加此方法即可
# ----------------------------

# 可选：直接对象转Markdown字符串（不写文件）
def outputs_output_to_md_string(obj):
    outputs = None
    if 'outputs' in obj:
        outputs = obj['outputs']
    elif 'data' in obj and 'outputs' in obj['data']:
        outputs = obj['data']['outputs']
    else:
        raise ValueError("JSON结构中未找到 outputs 字段！")

    html = outputs.get('output', '').strip()
    md_text = html_to_md(html)
    return md_text

def extract_jsondata(json_input_file: str):
    """
    从包含输出 text 字段的 JSON 字符串中提取 YAML 内容，并写入 .yml 文件
    :param json_input_str: 原始 JSON 字符串（包含 YAML 字符串在 outputs.text 中）
    :param output_file: 保存的目标 yml 文件路径
    """
    try:
        with open(json_input_file, "r", encoding="utf-8") as f:
            json_str = f.read()
        # 先将 JSON 字符串转为 Python 对象
        json_input = json.loads(json_str)
        
        # 提取 outputs.text 字符串
        raw_text = json_input["data"]["outputs"]["text"]
        return raw_text        
    except Exception as e:
        print(f"❌ 发生错误: {e}")

import re
from pathlib import Path
from typing import Tuple
from copy import deepcopy
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap, CommentedSeq

FENCE_RE = re.compile(r"```(ya?ml)\s*(.*?)\s*```", re.IGNORECASE | re.DOTALL)

yaml_rt = YAML(typ="rt")        # round-trip，保留注释/顺序/缩进
yaml_rt.indent(mapping=2, sequence=2, offset=0)
yaml_rt.width = 10**9           # 避免自动换行

def _common_left_margin(s: str) -> str:
    margins = []
    for line in s.splitlines():
        if not line.strip():
            continue
        m = re.match(r"[ \t]*", line)
        margins.append(m.group(0))
    if not margins:
        return ""
    prefix = margins[0]
    for m in margins[1:]:
        i = 0
        while i < len(prefix) and i < len(m) and prefix[i] == m[i]:
            i += 1
        prefix = prefix[:i]
        if not prefix:
            break
    return prefix

def _indent_with_margin(s: str, margin: str) -> str:
    return "\n".join(margin + line if line else margin for line in s.splitlines())

def _find_yaml_block_with_commands(text: str):
    """
    返回：((start,end), lang, data(CommentedMap), inner_src(str), left_margin(str))
    """
    for m in FENCE_RE.finditer(text):
        lang = m.group(1)
        inner_src = m.group(2)
        try:
            data = yaml_rt.load(inner_src)
        except Exception:
            continue
        if isinstance(data, CommentedMap) and "commands" in data:
            left_margin = _common_left_margin(inner_src)
            return (m.span(), lang, data, inner_src, left_margin)
    raise ValueError("未找到包含 'commands' 键的 ```yaml 代码块。")

def _dump_rt(data: CommentedMap) -> str:
    from io import StringIO
    buf = StringIO()
    yaml_rt.dump(data, buf)
    return buf.getvalue().rstrip("\n")

def replace_commands_block(src_path: str, dst_path: str, out_path: str) -> None:
    src_text = Path(src_path).read_text(encoding="utf-8")
    dst_text = Path(dst_path).read_text(encoding="utf-8")

    (_s_span, _s_lang, s_yaml, _s_inner, _s_margin) = _find_yaml_block_with_commands(src_text)
    (d_span, d_lang, d_yaml, d_inner, d_margin) = _find_yaml_block_with_commands(dst_text)

    if "commands" not in s_yaml:
        raise ValueError("源 YAML 未包含 'commands' 键。")

    # 深拷贝源 commands（带注释）
    s_commands = deepcopy(s_yaml["commands"])
    # 替换目标的 commands 值（保持目标文件其它键的注释/格式）
    d_yaml["commands"] = s_commands

    # 可选：若希望把源 commands 键的行内注释/前置注释一起带过去
    if hasattr(s_yaml, "ca") and hasattr(d_yaml, "ca"):
        if s_yaml.ca.items.get("commands"):
            d_yaml.ca.items["commands"] = s_yaml.ca.items.get("commands")

    dumped = _dump_rt(d_yaml)
    dumped_with_margin = _indent_with_margin(dumped, d_margin)
    new_fenced = f"```{d_lang}\n{dumped_with_margin}\n```"

    d_start, d_end = d_span
    new_text = dst_text[:d_start] + new_fenced + dst_text[d_end:]
    Path(out_path).write_text(new_text, encoding="utf-8")

# 使用示例
# replace_commands_block_preserve_comments(
#     src_path="01-manufacturing-director.updated.md",
#     dst_path="some-other-agent.md",
#     out_path="some-other-agent.commands-replaced.md"
# )

def getConversation_id(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    conversation_id = data['conversation_id']
    return conversation_id

if __name__ == "__main__":
    # 添加命令行参数解析
    parser = argparse.ArgumentParser(description="Generate poc document for project.")
    parser.add_argument("project", type=str, help="project name.")
    parser.add_argument("language", type=str, help="language of the workflow.")
    args = parser.parse_args()
    file_path = f"./projects/{args.project}/PO-00/{args.language}.json"
    output_path = f"./projects/{args.project}/PO-00/{args.language}.md"
    application_to_md(file_path, output_path)
