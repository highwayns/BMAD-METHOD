import requests
import argparse
import sqlite3
import httpx

KBDB_PATH = "/home/tei952/sayama/00.standard_and_tool/standards/ai_poc/AI_Powered_system_manager/project_data/project_config.db"

def setup_database(db_path):
    """连接到 SQLite 数据库并创建表"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # 创建 knowledgebase 表（知识库）
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS knowledgebase (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print(f"✅ 数据库和表已设置: {db_path}")


def create_knowledgebase(key, value):
    """
    向 projects 表中插入一条新的项目记录。

    参数:
        db_path (str): SQLite 数据库文件路径
        key (str): 项目唯一 ID
        value (str): 项目名称

    返回:
        bool: 插入是否成功
    """
    try:
        conn = sqlite3.connect(KBDB_PATH)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO knowledgebase (key, value)
            VALUES (?, ?)
        ''', (key, value))

        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        print(f"❌ 插入失败：知识库 ID '{key}' 已存在。")
        return False
    except Exception as e:
        print(f"❌ 插入失败：{e}")
        return False


def login_and_get_token(base_url, email, password, language='en-US'):
    url = f"{base_url}/login"
    payload = {
        "email": email,
        "password": password,
        "language": language,
        "remember_me": True
    }

    response = httpx.post(url, json=payload)
    response.raise_for_status()

    data = response.json()
    if data.get("result") == "success":
        return {
            "access_token": data["data"]["access_token"],
            "refresh_token": data["data"]["refresh_token"]
        }
    else:
        raise Exception("Login failed: " + str(data))

def create_dataset(api_key, kb_name, base_url="http://localhost/v1"):

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    create_dataset_payload = {
        "name": f"{kb_name}",
        "permission": "only_me"
    }

    response = requests.post(
        f"{base_url}/datasets",
        headers=headers,
        json=create_dataset_payload
    )
    id = response.json().get("id")
    if not id:
        raise Exception("创建知识库失败，返回结果：" + str(response.json()))
    create_knowledgebase(
        key=kb_name,
        value=id
    )
    print("创建知识库返回结果：", response.status_code, response.json())
# ============ 程序入口 ============

if __name__ == "__main__":
    # 添加命令行参数解析
    parser = argparse.ArgumentParser(description="Generate knowledgebase.")
    parser.add_argument("knowledgebase", type=str, help="knowledgebase name.")
    args = parser.parse_args()

    tokens = login_and_get_token(
        base_url="http://localhost/console/api",  # 你的 Dify 地址
        email="tei952@hotmail.com",
        password="Zjhuen1915"
    )

    print("Access Token:", tokens["access_token"])
    BASE_URL = 'http://localhost/console/api'
    # 示例调用
    setup_database(KBDB_PATH)
    create_dataset(
        api_key=tokens["access_token"],
        kb_name=args.knowledgebase,
        base_url=BASE_URL
    )

    print(f"✅ 知识库创建完了！")
