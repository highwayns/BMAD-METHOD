# BMAD-Method｜Databricks（Lakehouse）系统开发管理团队扩展包

## Overview

本扩展包为 Databricks 项目提供 **标准化的管理团队角色、代理、任务、输出模板、检查清单与编排**，帮助你以 BMAD 方法落地从 **架构→实施→验证→运行** 的完整闭环。

## Purpose

在 BMAD 核心流程之外，补齐 Databricks 场景下的：

- Unity Catalog（RBAC/治理）、集群策略与成本控制（FinOps）
- 数据契约、ELT（Autoloader/DLT/Jobs）
- Silver→Gold 语义层、Feature Store、Model Serving
- CI/CD、可观测性（Lakehouse Monitoring/SQL Alerts）、SLO 与事件复盘

## When to Use This Pack

- 新建或迁移到 Databricks 的数据平台/数据产品
- 需要标准化的角色分工、文档模板、质量门
- 需要以任务驱动的自动化代理与统一检查清单

## What's Included

### Agents

- `agents/databricks-lakehouse.md` — Databricks 平台代理（人格化、命令化、依赖映射）

### Templates (Output)

- `templates/output/databricks-architecture-tmpl.yaml`
- `templates/output/databricks-implementation-tmpl.yaml`

### Tasks

- `tasks/create-doc-databricks-architecture.md` — 交互式产出架构文档
- `tasks/review-infrastructure.md` — 渐进式/YOLO 复核
- `tasks/validate-infrastructure.md` — 16 节检查清单驱动的验证与评分

### Checklists

- `checklists/databricks-infrastructure-checklist.md` — 16 大章节、生产前质量门

### Roles & Manifests

- `roles/*.md`（18 角色）与 `manifests/*`

### Workflows

- `workflows/*` — 编排手册、泳道图与交接契约

## Integration with Core BMad

1. **After Architecture**：契约锁定后进入 Lakehouse 架构（Catalog/Schema/Tables/Permissions）
2. **Parallel to Development**：实施 DLT/Jobs、Silver→Gold、Feature/Model/Serving
3. **Before Deployment**：走 `validate-infrastructure` 与检查清单质量门

## Installation

**Manual**

```bash
# 将本扩展包克隆/下载至项目仓库，如 ./bmad-packs/databricks
```

## Usage Examples

### 1) 生成架构文档

```
*agent databricks-lakehouse → *create-doc databricks-architecture
```

### 2) 复核平台

```
*agent databricks-lakehouse → *review-infrastructure
```

### 3) 验证与准入

```
*agent databricks-lakehouse → *validate-infrastructure
```

## Team Integration

- 在团队流程中将本扩展包的检查清单作为**发布前质量门**；在架构模板中引用**文档验证章节**。

## Dependencies

- 需要 Databricks Workspace、Unity Catalog 与 Service Principal；CI 能访问 Token（渲染模板前请赋值变量）。

## Customization

- 可自定义 UC 层级/遮罩策略、集群策略与预算门槛、合规条目与报告样式。

## Notes

- 模板变量使用 `{var}`；`<critical_rule>` 标记的规则为强制性。
- 生产前务必先在非生产环境验证、并保留证据。

---

_Version: 1.0.0_ · _Compatible with BMad Core >= 1.10_
