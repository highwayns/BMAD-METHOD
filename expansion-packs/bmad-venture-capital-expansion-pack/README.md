# BMAD-Method｜风险投资（VC）管理团队扩展包

## Overview

本扩展包为风险投资基金（基金设立/募资/投后/退出）提供 **标准化的管理团队角色、代理、任务、输出模板、检查清单与编排**，
按 BMAD 方法实现 **从基金架构→募资与LP关系→投资论点与筛选→尽调与投决→投后赋能与治理→估值与报表→退出与分配** 的闭环。

## Purpose

补齐 VC 场景的：

- 基金架构、LPA/Side Letter、管理费与分配机制（瀑布）
- 投资论点、Dealflow/CRM、IC 决策、尽调（商业/财税/法务/技术/ESG）
- 估值与持仓（ASC 820/IFRS 13）、季度/年度报告、审计
- 投后赋能（招聘/市场/BD/增长/社区）、董事会治理与信息权
- 资金调用与分配、现金流/预实差、合规（AML/KYC/SFC/SEC 等）
- KPI 仪表板（TVPI/DPI/IRR/PME、Hit Rate、Loss Ratio、Ownership、Reserves）

## What's Included

- **Agents**：`agents/venture-capital.md`
- **Templates (Output)**：`templates/output/vc-architecture-tmpl.yaml`、`templates/output/vc-implementation-tmpl.yaml`
- **Tasks**：`tasks/create-doc-vc-architecture.md`、`tasks/review-operations.md`、`tasks/validate-operations.md`
- **Checklists**：`checklists/vc-operations-checklist.md`（16 大质量门）
- **Roles & Manifests**：`roles/*.md`（18 角色）与 `manifests/*`
- **Workflows**：`workflows/*`（编排手册、Mermaid 泳道图与交接契约）
- **Data & Policies**：`templates/data/*.csv` 与 `templates/policies/*`，`templates/monitoring/*`

## Integration with Core BMAD

1. **After Fund Blueprint**：锁定基金结构/条款/合规 → 进入《运营架构》
2. **Parallel to Investing**：投前/投中/投后流水线联动
3. **Before LP Reporting/Audit/Distributions**：走 `validate-operations` 与检查清单质量门

## Usage

```
*agent venture-capital → *create-doc vc-architecture
*agent venture-capital → *review-operations
*agent venture-capital → *validate-operations
```

## Notes

- 模板变量使用 `{var}`；`<critical_rule>` 为强规则。
- 本扩展包用于流程与文档标准化，不替代当地监管/合规要求。

---

_Version: 1.0.0_ · _Compatible with BMAD Core >= 1.10_ · _Last Updated: 2025-09-10_
