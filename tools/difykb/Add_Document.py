#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add_Document_enhanced.py
- 初始化时：若不存在文档数据表则自动创建
- 成功将文件加入 Dify 知识库后：把文档名称、文档ID（document_id）、知识库ID（dataset_id/knowledgebase_id）、文件ID(file_id) 等写入文档数据表
- 兼容 /console/api 与 /v1 风格，仍使用原脚本的登录与上传逻辑
"""
import os
import argparse
import sqlite3
from datetime import datetime
import requests
import httpx

# === 配置区 ===
KBDB_PATH = "/home/tei952/sayama/00.standard_and_tool/standards/ai_poc/AI_Powered_system_manager/project_data/project_config.db"

DOC_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS kb_documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kb_id TEXT NOT NULL,
    doc_id TEXT NOT NULL,
    doc_name TEXT,
    file_id TEXT,
    file_name TEXT,
    created_at TEXT DEFAULT (datetime('now'))
);
"""

def get_db_conn():
    os.makedirs(os.path.dirname(KBDB_PATH), exist_ok=True)
    conn = sqlite3.connect(KBDB_PATH)
    return conn

def init_db():
    try:
        conn = get_db_conn()
        with conn:
            conn.execute(DOC_TABLE_SQL)
        conn.close()
        print("✅ 文档数据表检查/创建完成：kb_documents")
    except Exception as e:
        print(f"❌ 文档数据表初始化失败: {e}")

def get_knowledgebase_value(key: str) -> str:
    """
    根据 key 从 knowledgebase 表中查询 value（知识库ID）。
    """
    try:
        conn = get_db_conn()
        cursor = conn.cursor()
        cursor.execute('SELECT value FROM knowledgebase WHERE key = ?', (key,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return row[0]
        else:
            print(f"⚠️ 未找到 key='{key}' 对应的知识库记录。")
            return None
    except Exception as e:
        print(f"❌ 查询知识库ID失败：{e}")
        return None

def login_and_get_token(base_url, email, password, language='en-US'):
    url = f"{base_url}/login"
    payload = {
        "email": email,
        "password": password,
        "language": language,
        "remember_me": True
    }
    r = httpx.post(url, json=payload, timeout=30.0)
    r.raise_for_status()
    data = r.json()
    if data.get("result") == "success":
        return {
            "access_token": data["data"]["access_token"],
            "refresh_token": data["data"]["refresh_token"]
        }
    raise RuntimeError(f"Login failed: {data}")

def safe_get(d, *keys, default=None):
    cur = d
    for k in keys:
        if isinstance(cur, dict) and k in cur:
            cur = cur[k]
        else:
            return default
    return cur

def extract_document_fields(resp_json, default_name=None):
    """
    稳健提取 document_id 与 document_name，兼容以下结构：
      - {"id": "...", "name": "..."}
      - {"data": {"id": "...", "name": "..."}}
      - {"documents": [{"id": "...", "name": "..."}], "batch": "..."}  # 你的示例
      - {"data": {"documents": [{"id": "...", "name": "..."}]}}
    """
    doc_id = None
    doc_name = None

    # 顶层
    doc_id = (resp_json.get("id") or doc_id)
    doc_name = (resp_json.get("name") or doc_name)

    # data.*
    data = resp_json.get("data")
    if isinstance(data, dict):
        doc_id = data.get("id") or doc_id
        doc_name = data.get("name") or doc_name
        docs = data.get("documents")
        if isinstance(docs, list) and docs:
            first = docs[0] if isinstance(docs[0], dict) else None
            if first:
                doc_id = first.get("id") or doc_id
                doc_name = first.get("name") or doc_name

    # 顶层 documents 列表（示例）
    docs = resp_json.get("documents")
    if isinstance(docs, list) and docs:
        first = docs[0] if isinstance(docs[0], dict) else None
        if first:
            doc_id = first.get("id") or doc_id
            doc_name = first.get("name") or doc_name

    if not doc_name and default_name:
        doc_name = default_name

    return doc_id, doc_name

def record_document(kb_id: str, doc_id: str, doc_name: str, file_id: str, file_name: str):
    try:
        conn = get_db_conn()
        with conn:
            conn.execute(
                'INSERT INTO kb_documents (kb_id, doc_id, doc_name, file_id, file_name) VALUES (?, ?, ?, ?, ?)',
                (kb_id, doc_id, doc_name, file_id, file_name)
            )
        conn.close()
        print(f"🗂️ 已写入文档记录：kb_id={kb_id}, doc_id={doc_id}, doc_name={doc_name}, file_id={file_id}")
    except Exception as e:
        print(f"❌ 写入文档数据表失败：{e}")

def upload_and_add_to_dataset(access_token, dataset_id, file_path, base_url="http://localhost/console/api"):
    headers = {"Authorization": f"Bearer {access_token}"}

    # 1) 上传文件
    with open(file_path, "rb") as f:
        files = {"file": (os.path.basename(file_path), f)}
        upload_resp = requests.post(f"{base_url}/files/upload", headers=headers, files=files, timeout=60)
    if upload_resp.status_code not in (200, 201):
        print("❌ 文件上传失败:", upload_resp.status_code, upload_resp.text)
        return False

    file_info = upload_resp.json()
    file_info["mime_type"] = "application/pdf"
    file_id = file_info.get("id") or safe_get(file_info, "data", "id")
    file_info["file_ids"]= [file_id]
    info_list = {
        "data_source_type": "upload_file",
        "file_info_list": file_info
    }
    file_name = os.path.basename(file_path)
    print("✅ 上传成功 file_id=", file_id)

    # 2) 加入知识库
    add_doc_payload = {
        #"indexing_technique": "economy",   # 或 high_quality，按需调整
        "indexing_technique": "economy",
        "doc_form": "text_model",
        "data_source": {
            "type": "file",
            "file_ids": [file_id],
            "info_list": info_list
        },
        "process_rule": {"mode": "automatic"}
    }
    add_resp = requests.post(
        f"{base_url}/datasets/{dataset_id}/documents",
        headers=headers,
        json=add_doc_payload,
        timeout=60
    )
    print("📨 加入知识库响应:", add_resp.status_code)

    if add_resp.status_code not in (200, 201, 202):
        print("❌ 添加文档失败:", add_resp.text)
        return False

    data = add_resp.json()
    print("📄 文档添加响应数据:", data)
    # 兼容多种返回结构，尽力拿到 document_id / name
    doc_id, doc_name = extract_document_fields(data, default_name=file_name)
    if not doc_id:
        doc_id = safe_get(data, "data", "documents", 0, "id")
        doc_name = doc_name or safe_get(data, "data", "documents", 0, "name") or file_name

    if not doc_id:
        print("⚠️ 未能从响应中解析到 document_id，将仅记录 file_id 与文件名。")

    # 写入本地文档数据表
    record_document(kb_id=dataset_id, doc_id=doc_id or "UNKNOWN", doc_name=doc_name, file_id=file_id, file_name=file_name)
    print("✅ 文档已添加到知识库，并写入本地数据表。")
    return True

def main():
    parser = argparse.ArgumentParser(description="将文件上传并加入 Dify 知识库，同时记录到本地文档数据表。")
    parser.add_argument("knowledgebase", type=str, help="本地 knowledgebase 表中配置的 key（用于取 dataset_id）")
    parser.add_argument("filepath", type=str, help="要加入知识库的文件路径")
    parser.add_argument("--base-url", default="http://localhost/console/api", help="Dify 后台基础 URL，如 http://localhost/console/api 或 http://localhost/v1")
    parser.add_argument("--email", default="tei952@hotmail.com")
    parser.add_argument("--password", default="Zjhuen1915")
    args = parser.parse_args()

    # 1) 初始化表
    init_db()

    # 2) 登录取 token
    tokens = login_and_get_token(
        base_url=args.base_url,
        email=args.email,
        password=args.password
    )
    access_token = tokens["access_token"]
    print("🔑 Access Token 获取成功")

    # 3) 解析知识库ID
    dataset_id = get_knowledgebase_value(args.knowledgebase)
    if not dataset_id:
        raise SystemExit("未获取到知识库ID，终止。")

    # 4) 单文件处理
    filepath = args.filepath
    if not os.path.isfile(filepath):
        raise SystemExit(f"文件不存在：{filepath}")
    print("📄 正在处理文件：", filepath)

    ok = upload_and_add_to_dataset(access_token, dataset_id, filepath, base_url=args.base_url)
    if ok:
        print(f"🎉 完成：已加入知识库并记录到表 kb_documents ：{filepath}")
    else:
        print("结束：未成功加入知识库。")

if __name__ == "__main__":
    main()
