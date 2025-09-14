# BMAD-Method｜人才招聘·培训·派遣（Staffing HR）管理团队扩展包

## Overview

本扩展包为“招聘→培训→派遣（外派/驻场）”业务提供 **标准化的管理团队角色、代理、任务、输出模板、检查清单与编排**，帮助你以 BMAD 方法落地**从客户需求→岗位画像→寻源→甄选→面试→Offer→入职培训→派遣→绩效与薪酬结算→报告合规**的闭环。

## Purpose

在 BMAD 核心流程之外，补齐 Staffing 场景的：

- 需求 intake/岗位画像（Job Profile 数据契约）、SLA 与费用条款
- 寻源与候选人管道、ATS/CRM 自动化、评测与面试
- 培训/认证（L&D）、入职与合规（背调/签字/保密）
- 派遣排班/工时/绩效、客户服务与续约、薪资与结算（FinOps for HR）
- 可观测与 KPI 仪表板、合规与数据隐私（PII/跨境）

## When to Use This Pack

- 新建或升级招聘+培训+派遣一体化服务
- 需要标准化“角色分工/文档模板/质量门/交接契约”
- 需要任务驱动的自动化代理与统一检查清单

## What's Included

### Agents

- `agents/staffing-hr.md` — Staffing HR 代理（人格化、命令化、依赖映射）

### Templates (Output)

- `templates/output/staffing-architecture-tmpl.yaml`
- `templates/output/staffing-implementation-tmpl.yaml`

### Tasks

- `tasks/create-doc-staffing-architecture.md` — 交互式产出《业务架构》
- `tasks/review-operations.md` — 渐进式/YOLO 复核
- `tasks/validate-operations.md` — 16 节检查清单驱动的验证与评分

### Checklists

- `checklists/staffing-operations-checklist.md` — 16 大章节、交付前质量门

### Roles & Manifests

- `roles/*.md`（18 角色）与 `manifests/*`

### Workflows

- `workflows/*` — 编排手册、泳道图与交接契约

### Data & Policies

- `templates/data/*.csv`（候选/职位/培训/派遣/KPI/客户）与 `templates/policies/*`（隐私/合规）

## Integration with Core BMad

1. **After Client Intake**：锁定岗位/条款（Job Profile & Contract）→ 进入《业务架构》
2. **Parallel to Delivery**：寻源/筛选/培训/派遣流水线运转，ATS/排班/薪资自动化
3. **Before Billing/Reporting**：走 `validate-operations` 与检查清单质量门

## Installation

**Manual**

```bash
# 将本扩展包克隆/下载至项目仓库，如 ./bmad-packs/staffing-hr
```

## Usage Examples

### 1) 生成业务架构文档

```
*agent staffing-hr → *create-doc staffing-architecture
```

### 2) 复核运营流程

```
*agent staffing-hr → *review-operations
```

### 3) 验证与准入

```
*agent staffing-hr → *validate-operations
```

## Team Integration

- 将本扩展包的检查清单作为**计费/结算/客户验收**前质量门；在架构模板中引用**文档验证章节**与强规则。

## Dependencies

- 需要 ATS/HRIS/排班/考勤/薪资系统；合规策略（隐私/背调/劳动法规）；变量渲染前需赋值。

## Customization

- 可自定义岗位数据契约、评测/面试流程、培训课程库、派遣排班规则、费用与 KPI。

## Notes

- 模板变量使用 `{var}`；`<critical_rule>` 标记的规则为强制性。
- 计费/交付前务必先在测试岗位/小批次派遣上验证，并保留审批与签字记录。

---

_Version: 1.0.0_ · _Compatible with BMad Core >= 1.10_
