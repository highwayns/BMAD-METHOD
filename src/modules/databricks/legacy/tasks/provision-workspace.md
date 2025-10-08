# Provision Databricks Workspace Task

docOutputLocation: docs/platform/workspace-provision.md

## Purpose

在既定账户与网络基线下，按模板化参数创建/校准 Workspace、Cluster Policies、Pools、Permissions、Repos 基线。

## Inputs

- templates/workspace-configuration-tmpl.yaml
- checklists/databricks-workspace-setup-checklist.md

## Steps

1. 解析模板参数（区域/计费标签/VPC/私网/SCIM/SSO/审计导出）
2. 应用集群策略与机池（CPU/GPU/Spot/Auto-Termination）
3. 绑定 UC Metastore / External Locations / Storage Credentials
4. 配置 Repos 模板、禁用不合规运行模式（如无策略的 All-Purpose）
5. 执行工作区自检（Checklist）并产出工件

## Outputs

- docs/platform/workspace-provision.md（变更记录、截图或命令/JSON）
- configs/workspace/\*.yaml（落地配置）
