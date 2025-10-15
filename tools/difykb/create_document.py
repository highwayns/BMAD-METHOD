import yaml
import json
import os
import argparse
from datetime import datetime
import requests
from pathlib import Path

def create_document(local_file, token, title, language, output_file):

    # 步骤1：上传文件到 Dify
    with open(local_file, "rb") as f:
        file_name = local_file.split("/")[-1]
        files = {
            "file": (file_name, f, "application/octet-stream")
        }
        headers = {"Authorization": f"Bearer {token}"}
        r = requests.post(f"http://localhost/v1/files/upload", headers=headers, files=files)
        r.raise_for_status()
        file_meta = r.json()
        file_var_id = file_meta["id"]
        print("file_var_id:", file_var_id)
        file_meta["mime_type"] = "application/pdf"
        file_id = file_meta.get("id")
        file_meta["file_ids"]= [file_id]
        info_list = {
            "data_source_type": "upload_file",
            "file_info_list": file_meta
        }

        # 步骤2：启动 Workflow 执行
        # Dify Chat API endpoint
        url = "http://localhost/v1/workflows/run"

        # 请求头
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        # 请求体
        payload = {
            "inputs": {
                "file": {
                      "transfer_method": "local_file",
                      "upload_file_id": file_id,
                      "type": "document"
                  },
                "title": title,
                "language": language
            },
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
    parser = argparse.ArgumentParser(description="Generate project document for system development.")
    parser.add_argument("project", type=str, help="project name.")
    parser.add_argument("flowid", type=str, help="workflow id.")
    parser.add_argument("token", type=str, help="token of the workflow.")
    parser.add_argument("language", type=str, help="language of the workflow.")
    args = parser.parse_args()

    # 生成工作流配置
    local_file = "./projects/"+args.project + ".pdf"
    token = args.token
    title = args.project
    language = args.language
    output_path = "./projects/"+args.project+"/"+args.flowid
    output_file = output_path+"/"+args.language+".json"
    category_output_folder = Path(output_path) 
    os.makedirs(category_output_folder, exist_ok=True)

    create_document(local_file, token, title, language, output_file)

    print(f"✅ 生成完了 {args.project}-{args.flowid} ！")