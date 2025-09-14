# BMAD-Method｜旅游接待（Tour Operations）管理团队扩展包

## Overview

本扩展包为旅游接待（B2B 地接、B2C 小团、MICE 会奖）提供 **标准化的管理团队角色、代理、任务、输出模板、检查清单与编排**，帮助按 BMAD 方法落地 **从客户需求→行程设计→供应商与资源→预订→落地接待→应急与质量→结算与复盘** 的闭环。

## Purpose

在 BMAD 核心流程之外，补齐旅游接待的：

- 客户与游客数据契约、签证与保险、合规与隐私（PII）
- 行程策划与控房控位、供应商合同与 SLA（酒店/车导/餐/景点）
- 现场执行/调度、意外与应急预案、投诉处理与服务改进
- 费用与利润（FinOps for TourOps）、KPI 仪表板与复盘

## When to Use This Pack

- 新建或升级地接/旅行社的运营流程与文档
- 需要标准化的角色分工、模板、质量门与交接契约
- 需要任务驱动的自动化代理与统一检查清单

## What's Included

### Agents

- `agents/travel-reception.md` — 旅游接待运营代理（人格化、命令化、依赖映射）

### Templates (Output)

- `templates/output/travel-architecture-tmpl.yaml`
- `templates/output/travel-implementation-tmpl.yaml`

### Tasks

- `tasks/create-doc-travel-architecture.md` — 交互式产出《接待运营架构》
- `tasks/review-operations.md` — 渐进式/YOLO 复核
- `tasks/validate-operations.md` — 16 节检查清单驱动的验证与评分

### Checklists

- `checklists/travel-operations-checklist.md` — 16 大章节、出团/结算前质量门

### Roles & Manifests

- `roles/*.md`（18 角色）与 `manifests/*`

### Workflows

- `workflows/*` — 编排手册、泳道图与交接契约

### Data & Policies

- `templates/data/*.csv`（游客/行程/预订/房单/交通/供应商/KPI/发票等）与 `templates/policies/*`（安全/隐私/供应商SLA/退款）

## Integration with Core BMad

1. **After Client Intake**：锁定数据契约与条款 → 进入《接待运营架构》
2. **Parallel to Delivery**：设计/预订/落地执行流水线与 DMS/CRM/支付联动
3. **Before Billing/Reporting**：走 `validate-operations` 与检查清单质量门

## Installation

**Manual**

```bash
# 将本扩展包克隆/下载至项目仓库，如 ./bmad-packs/travel
```

## Usage Examples

### 1) 生成接待运营架构文档

```
*agent travel-reception → *create-doc travel-architecture
```

### 2) 复核运营流程

```
*agent travel-reception → *review-operations
```

### 3) 验证与准入

```
*agent travel-reception → *validate-operations
```

## Team Integration

- 将检查清单作为**出团/交付/结算**前质量门；在架构模板中引用**文档验证章节**与强规则。

## Dependencies

- 需要 DMS/CRM/支付与发票系统；供应商合同与价单；应急与保险策略；变量渲染前需赋值。

## Customization

- 可自定义命名规范、游客/订单数据契约、签证/保险模板、供应商评级规则、KPI 面板。

## Notes

- 模板变量使用 `{var}`；`<critical_rule>` 标记的规则为强制性。

---

_Version: 1.0.0_ · _Compatible with BMad Core >= 1.10_
