# BMAD-Method｜Snowflake 系统开发管理团队扩展包

## Overview

本扩展包为 Snowflake（Data Cloud）项目提供 **标准化的管理团队角色、代理、任务、输出模板、检查清单与编排**，帮助你以 BMAD 方法论落地从 **架构→实施→验证→运行** 的完整闭环。

## Purpose

在 BMAD 核心流程之外，补齐 Snowflake 场景下的：

- RBAC/治理、仓库策略与信用控制（FinOps）
- 数据契约、ELT（Stage/Copy/Snowpipe/Streams/Tasks）
- 动态表与语义层、Snowpark/模型 UDF
- CI/CD、可观测性（ACCOUNT_USAGE/ORGANIZATION_USAGE）、SLO 与事件复盘

## When to Use This Pack

- 新建或迁移到 Snowflake 的数据平台/数据产品
- 需要标准化的角色分工、文档模板、质量门
- 需要以任务驱动的自动化代理与统一检查清单

## What's Included

### Agents

- `agents/snowflake-data-cloud.md` — Snowflake 平台代理（人格化、命令化、依赖映射）

### Templates (Output)

- `templates/output/snowflake-architecture-tmpl.yaml`
- `templates/output/snowflake-implementation-tmpl.yaml`

### Tasks

- `tasks/create-doc-snowflake-architecture.md` — 交互式产出架构文档
- `tasks/review-infrastructure.md` — 渐进式/YOLO 复核
- `tasks/validate-infrastructure.md` — 16 节检查清单驱动的验证与评分

### Checklists

- `checklists/snowflake-infrastructure-checklist.md` — 16 大章节、生产前质量门

### Roles & Manifests

- `roles/*.md`（18 角色）与 `manifests/*`

### Workflows

- `workflows/*` — 编排手册、泳道图与交接契约

## Integration with Core BMad

1. **After Architecture**：契约锁定后进入 Snowflake 架构（DB/Schema/Warehouse/RBAC）
2. **Parallel to Development**：实施 ELT/Streaming、动态表/语义层、Snowpark
3. **Before Deployment**：走 `validate-infrastructure` 与检查清单质量门

## Installation

**Manual**

```bash
# 将本扩展包克隆/下载至项目仓库，如 ./bmad-packs/snowflake
```

## Usage Examples

### 1) 生成架构文档

```
*agent snowflake-data-cloud → *create-doc snowflake-architecture
```

### 2) 复核基础设施

```
*agent snowflake-data-cloud → *review-infrastructure
```

### 3) 验证与准入

```
*agent snowflake-data-cloud → *validate-infrastructure
```

## Team Integration

- 在团队流程中将本扩展包的检查清单作为**发布前质量门**；在架构模板中引用**文档验证章节**。

## Dependencies

- 需要 Snowflake 账号与 Workspace、仓库可用；CI 能访问密钥（使用占位变量前请赋值）。

## Customization

- 可自定义 RBAC 层级/遮罩策略、仓库策略与预算门槛、合规条目与报告样式。

## Notes

- 模板变量使用 `{var}`；`<critical_rule>` 标记的规则为强制性。
- 生产前务必先在非生产环境验证、并保留证据。

---

_Version: 1.0.0_ · _Compatible with BMad Core >= 1.10_
