# Ingestion Blueprint (Auto Loader + CDC)

docOutputLocation: docs/blueprints/ingestion.md

## Purpose

给出 Auto Loader/云存储监听/Schema Evolution/列映射与 CDC（Change Feed）的黄金路径。

## Steps

- 选择到 Bronze 的源端模式（文件/消息/数据库 + CDC）
- Auto Loader 参数：cloudFiles.\*，Schema Hints/Evolution 策略
- 安全与治理：UC External Location、权限与标签
- 生成落地样例与回放/补数流程

## Outputs

- docs/blueprints/ingestion.md
- samples/ingestion/\*.py
