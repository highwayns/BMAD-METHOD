#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update_or_Add_Document.py

功能：
- 按“文档名称”在本地 SQLite 表 `kb_documents` 中检索：
  - 若存在：取出 document_id，调用 Dify 的“更新文档”接口（支持按文件或文本更新）
  - 若不存在：走“新规添加”流程，并把记录写入 `kb_documents`

依赖：
- 与 Add_Document_enhanced.py 共用同一数据库（包含 knowledgebase 与 kb_documents 两表）
- 使用 /console/api 登录获取 access_token；如果你的环境用 /v1 API Key，请自行改造 headers

用法示例（按文件更新/新建）：
  python3 Update_or_Add_Document.py <knowledgebase_key> --doc-name "产品手册-安装" --file /path/to/manual.pdf \
    --base-url http://localhost/console/api --email you@example.com --password ****

用法示例（按文本更新/新建）：
  python3 Update_or_Add_Document.py <knowledgebase_key> --doc-name "FAQ-排错" --text "这里是新的FAQ文本..." \
    --base-url http://localhost/console/api --email you@example.com --password ****
"""
import os
import argparse
import sqlite3
import requests
import httpx

# === 配置区（与你的环境保持一致） ===
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
    return sqlite3.connect(KBDB_PATH)

def init_db():
    conn = get_db_conn()
    with conn:
        conn.execute(DOC_TABLE_SQL)
    conn.close()

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

def login_and_get_token(base_url, email, password, language='en-US'):
    url = f"{base_url}/login"
    payload = {"email": email, "password": password, "language": language, "remember_me": True}
    r = httpx.post(url, json=payload, timeout=30.0)
    r.raise_for_status()
    data = r.json()
    if data.get("result") == "success":
        return data["data"]["access_token"]
    raise RuntimeError(f"Login failed: {data}")

def get_dataset_id_by_key(key: str) -> str:
    conn = get_db_conn()
    try:
        cur = conn.cursor()
        cur.execute("SELECT value FROM knowledgebase WHERE key = ?", (key,))
        row = cur.fetchone()
        return row[0] if row else None
    finally:
        conn.close()

def find_doc_record_by_name(doc_name: str, kb_id: str):
    conn = get_db_conn()
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, kb_id, doc_id, doc_name, file_id, file_name FROM kb_documents WHERE doc_name = ? AND kb_id = ? ORDER BY id DESC LIMIT 1", (doc_name, kb_id))
        row = cur.fetchone()
        if row:
            keys = ["id","kb_id","doc_id","doc_name","file_id","file_name"]
            return dict(zip(keys, row))
        return None
    finally:
        conn.close()

def insert_doc_record(kb_id: str, doc_id: str, doc_name: str, file_id: str, file_name: str):
    conn = get_db_conn()
    try:
        with conn:
            conn.execute(
                "INSERT INTO kb_documents (kb_id, doc_id, doc_name, file_id, file_name) VALUES (?, ?, ?, ?, ?)",
                (kb_id, doc_id, doc_name, file_id, file_name)
            )
    finally:
        conn.close()

def delete_doc_record_file(kb_id: str, doc_name: str, file_id: str, file_name: str):
    # 仅更新最近一条匹配记录的 file 信息；不改 doc_id/kb_id
    conn = get_db_conn()
    try:
        with conn:
            conn.execute(
                "DELETE FROM kb_documents WHERE id = (SELECT id FROM kb_documents WHERE kb_id=? AND doc_name=? ORDER BY id DESC LIMIT 1)",
                (kb_id, doc_name)
            )
    finally:
        conn.close()

def upload_file_for_update(access_token, base_url, file_path):
    headers = {"Authorization": f"Bearer {access_token}"}
    with open(file_path, "rb") as f:
        files = {"file": (os.path.basename(file_path), f)}
        resp = requests.post(f"{base_url}/files/upload", headers=headers, files=files, timeout=60)
    if resp.status_code not in (200,201):
        raise RuntimeError(f"文件上传失败：{resp.status_code} {resp.text}")
    data = resp.json()
    return data

def delete_document_by_file(access_token, base_url, dataset_id, document_id, file_id):
    headers = {"Authorization": f"Bearer {access_token}"}
    #payload = {"file_id": file_id}
    # 不同版本路径可能不同，这里采用较新的 update-by-file 路径（若你的版本不支持，请调整为旧接口）
    url = f"{base_url}/datasets/{dataset_id}/documents/{document_id}"
    resp = requests.delete(url, headers=headers, timeout=60)
    #if resp.status_code not in (200,202,204):
    #    raise RuntimeError(f"更新文档失败：{resp.status_code} {resp.text}")
    #return resp.json()

def update_document_by_text(access_token, base_url, dataset_id, document_id, text):
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        "text": text,
        "indexing_technique": "economy",   # 或 high_quality
        "process_rule": {"mode": "automatic"}
    }
    url = f"{base_url}/datasets/{dataset_id}/documents/{document_id}/update-by-text"
    resp = requests.post(url, headers=headers, json=payload, timeout=60)
    if resp.status_code not in (200,201,202):
        raise RuntimeError(f"更新文档失败：{resp.status_code} {resp.text}")
    return resp.json()

def add_new_document(access_token, base_url, dataset_id, file_path=None, text=None, doc_name=""):
    headers = {"Authorization": f"Bearer {access_token}"}
    file_id = None
    file_name = None

    if file_path:
        file_info = upload_file_for_update(access_token, base_url, file_path)
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
        url = f"{base_url}/datasets/{dataset_id}/documents"
        resp = requests.post(url, headers=headers, json=add_doc_payload, timeout=60)
        if resp.status_code not in (200,201,202):
            raise RuntimeError(f"添加文档失败：{resp.status_code} {resp.text}")
        data = resp.json()
        doc_id, doc_name = extract_document_fields(data, default_name=file_name)
        return {"doc_id": doc_id, "doc_name": doc_name or file_name, "file_id": file_id, "file_name": file_name}

    elif text is not None:
        payload = {
            "indexing_technique": "economy",
            "doc_form": "text_model",
            "data_source": {
                "type": "text",
                "text": text
            },
            "process_rule": {"mode": "automatic"},
            "name": doc_name or "text_document"
        }
        url = f"{base_url}/datasets/{dataset_id}/documents"
        resp = requests.post(url, headers=headers, json=payload, timeout=60)
        if resp.status_code not in (200,201,202):
            raise RuntimeError(f"添加文档失败：{resp.status_code} {resp.text}")
        data = resp.json()
        doc_id, doc_name = extract_document_fields(data, default_name=file_name)
        return {"doc_id": doc_id, "doc_name": doc_name or "text_document", "file_id": None, "file_name": None}

    else:
        raise ValueError("add_new_document 需要 file_path 或 text 至少一个")

def main():
    parser = argparse.ArgumentParser(description="按文档名称更新 Dify 知识库文档；名称不存在则新建并登记到本地表。")
    parser.add_argument("knowledgebase", type=str, help="本地 knowledgebase 表中的 key，用于取 dataset_id")
    parser.add_argument("--doc-name", required=True, help="文档名称（在本地表中检索用）")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", dest="file_path", help="用于更新/新建的文件路径")
    group.add_argument("--text", dest="text_content", help="用于更新/新建的纯文本内容")

    parser.add_argument("--base-url", default="http://localhost/console/api")
    parser.add_argument("--email", default="tei952@hotmail.com")
    parser.add_argument("--password", default="Zjhuen1915")
    args = parser.parse_args()

    # 1) 初始化表（若不存在则创建）
    init_db()

    # 2) 取 dataset_id
    dataset_id = get_dataset_id_by_key(args.knowledgebase)
    if not dataset_id:
        raise SystemExit(f"未在 knowledgebase 表中找到 key={args.knowledgebase} 的 dataset_id")

    # 3) 登录获取 access_token
    access_token = login_and_get_token(args.base_url, args.email, args.password)

    # 4) 本地查询文档是否存在
    rec = find_doc_record_by_name(args.doc_name, kb_id=dataset_id)

    if rec:
        # === 更新路径 ===
        document_id = rec["doc_id"]
        print(f"🔄 本地已存在文档：doc_name='{args.doc_name}', doc_id='{document_id}' → 执行更新")

        if args.file_path:
            # 先上传新文件，拿到 file_id
            file_info = upload_file_for_update(access_token, args.base_url, args.file_path)
            file_id = file_info.get("id") or safe_get(file_info, "data", "id")
            # 调用更新接口
            delete_document_by_file(access_token, args.base_url, dataset_id, document_id, file_id)
            # 更新本地记录中的 file_id/file_name（便于追溯）
            delete_doc_record_file(dataset_id, args.doc_name, file_id=file_id, file_name=os.path.basename(args.file_path))
            result = add_new_document(access_token, args.base_url, dataset_id, file_path=args.file_path, doc_name=args.doc_name)
            insert_doc_record(kb_id=dataset_id, doc_id=result["doc_id"] or "UNKNOWN", doc_name=result["doc_name"], file_id=result["file_id"], file_name=result["file_name"])

            print("✅ 更新成功（按文件）。")
        else:
            data = update_document_by_text(access_token, args.base_url, dataset_id, document_id, args.text_content)
            print("✅ 更新成功（按文本）。")

    else:
        # === 新建路径 ===
        print(f"🆕 本地不存在文档名 '{args.doc_name}' 的记录 → 执行新建")
        if args.file_path:
            result = add_new_document(access_token, args.base_url, dataset_id, file_path=args.file_path, doc_name=args.doc_name)
            insert_doc_record(kb_id=dataset_id, doc_id=result["doc_id"] or "UNKNOWN", doc_name=result["doc_name"], file_id=result["file_id"], file_name=result["file_name"])
            print(f"✅ 新建成功并登记：doc_id={result['doc_id']}, name={result['doc_name']}")
        else:
            result = add_new_document(access_token, args.base_url, dataset_id, text=args.text_content, doc_name=args.doc_name)
            insert_doc_record(kb_id=dataset_id, doc_id=result["doc_id"] or "UNKNOWN", doc_name=result["doc_name"], file_id=None, file_name=None)
            print(f"✅ 新建成功并登记：doc_id={result['doc_id']}, name={result['doc_name']}")

if __name__ == "__main__":
    main()
