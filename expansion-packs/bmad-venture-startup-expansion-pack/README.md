# BMAD-Method｜风投创业（Venture-backed Startup）管理团队扩展包

## Overview

本扩展包面向**风投支持的初创企业/创业工场/加速器团队**，提供 **标准化的管理团队角色、代理、任务、输出模板、检查清单与编排**，
以 BMAD 方法实现 **从机会论点→用户研究→PMF→产品与工程→安全合规→增长与销售→客户成功→募资与董事会→财务与风控** 的闭环。

## Purpose

补齐风投创业场景的：

- **机会论点/产品战略/OKR**，问题-方案/市场-产品匹配（PMF）
- **产品研发与交付**（SDLC/Backlog/路线图/发布/质量）
- **DevOps/云/IaC/CI-CD/可观测性** 与 **安全与隐私合规**（SOC 2/GDPR/ISO 27001）
- **数据与分析**（埋点/归因/指标仓/实验/因果）
- **增长/营销/销售/RevOps/合同** 与 **客户成功/支持**
- **募资/Cap Table/董事会治理** 与 **财务/预算/Runway/风控**

## What's Included

- **Agents**：`agents/venture-startup.md`
- **Templates (Output)**：`templates/output/vs-architecture-tmpl.yaml`、`templates/output/vs-implementation-tmpl.yaml`
- **Tasks**：`tasks/create-doc-vs-architecture.md`、`tasks/review-operations.md`、`tasks/validate-operations.md`
- **Checklists**：`checklists/vs-operations-checklist.md`（16 大质量门）
- **Roles & Manifests**：`roles/*.md`（18 角色）与 `manifests/*`
- **Workflows**：`workflows/*`（编排手册、Mermaid 泳道图与交接契约）
- **Data & Policies**：`templates/data/*.csv` 与 `templates/policies/*`，`templates/monitoring/*`

## Integration with Core BMAD

1. **After Venture Thesis & Opportunity**：锁定目标用户/价值主张/商业模式 → 进入《运营架构》
2. **Parallel to Build→Measure→Learn**：产品/工程/增长/销售/CS/数据流水线联动
3. **Before Fundraising/Board/Release**：走 `validate-operations` 与检查清单质量门

## Usage

```
*agent venture-startup → *create-doc vs-architecture
*agent venture-startup → *review-operations
*agent venture-startup → *validate-operations
```

## Notes

- 模板变量使用 `{var}`；`<critical_rule>` 为强规则。
- 本扩展用于流程与文档标准化，不替代监管/合规要求。

---

_Version: 1.0.0_ · _Compatible with BMAD Core >= 1.10_ · _Last Updated: 2025-09-10_
