import yaml
import json
import os
import argparse
from datetime import datetime
import requests
from json2md import extract_jsondata

def load_input(yaml_text):
    """加载第一个yaml文件"""
    return yaml.safe_load(yaml_text)

def create_resume_new(jianli,pingjia,language, output_file):

    # 步骤2：启动 Workflow 执行
    # Dify Chat API endpoint
    url = "http://localhost/v1/chat-messages"

    # 请求头
    headers = {
        "Authorization": "Bearer app-0yUaa9f3ZxAGMzYjnhAu655V",
        "Content-Type": "application/json"
    }

    # 请求体
    payload = {
        "inputs": {
            "jianli": jianli,
            "pingjia": pingjia,
            "language": language
        },
        "query": "请提创建新的简历",
        "response_mode": "blocking",
        "conversation_id": "",
        "user": "abc-123"
    }

    # 发起 POST 请求
    response = requests.post(url, headers=headers, json=payload)

    # 检查响应状态
    if response.status_code == 200:
        result = response.json()
        # 保存响应到文件
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"✅ 已保存响应内容到 {output_file}")
    else:
        print(f"❌ 请求失败，状态码: {response.status_code}")
        print(response.text)

# ============ 程序入口 ============

if __name__ == "__main__":
    # 添加命令行参数解析
    parser = argparse.ArgumentParser(description="create new Resume file to json.")
    parser.add_argument("title", type=str, help="Resume filename.")
    args = parser.parse_args()

    # 生成工作流配置
    jianli_file = "./resume/"+args.title+".json"
    jianli = extract_jsondata(jianli_file)
    pingjia_file = "./resume_review/"+args.title+".json"
    pingjia = extract_jsondata(jianli_file)
    language = "日文"  # 假设语言为日文
    create_resume_new(jianli,pingjia,language, "./resume_new/"+args.title+".json")
    
    print(f"✅ 生成完了 {args.title}！")