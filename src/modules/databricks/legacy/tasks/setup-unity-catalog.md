# Setup Unity Catalog Task

docOutputLocation: docs/platform/uc-setup.md

## Purpose

落地或校准 Metastore、Catalog/Schema、External Locations、Volumes、Storage Credentials、Grants、数据分级与标签。

## Steps

- 基于 uc-governance-policy-tmpl.yaml 生成策略集
- 建立分层数据域与命名规约（bronze/silver/gold；prod/stg/dev）
- 应用标签/分级/遮罩/行列级策略与视图
- 校验权限继承与跨工作区可见性

## Outputs

- docs/platform/uc-setup.md
- policies/uc/\*.sql|yaml
