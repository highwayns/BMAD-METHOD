# BMAD-Method｜科学研究管理团队扩展包

## Overview

本扩展包针对科研组织（高校/研究所/企业研发）提供 **标准化的管理团队角色、代理、任务、输出模板、检查清单与编排**，
以 BMAD 方法落地 **从课题立项与资助→伦理与合规→实验/采样/数据→分析与复现→发表与共享→知识转化** 的闭环。

## Purpose

补齐科研管理场景的：

- **研究诚信（RCR）与伦理合规**（IRB/IACUC/IBC/数据隐私）
- **数据管理计划（DMP）与安全**、元数据/标注、版本与追溯
- **统计分析计划（SAP）与复现**、代码与计算环境治理
- **实验室管理与 EHS**、设备校准与维护、试剂与样本追踪
- **学术发表与署名伦理**、开放科学（数据/代码/预注册/预印本）
- **经费与预算**、知识产权与技术转移、合作与材料转移（MTA）

## What's Included

- Agents：`agents/scientific-research.md`
- Templates (Output)：`templates/output/research-architecture-tmpl.yaml`、`templates/output/research-implementation-tmpl.yaml`
- Tasks：`tasks/create-doc-research-architecture.md`、`tasks/review-operations.md`、`tasks/validate-operations.md`
- Checklists：`checklists/research-operations-checklist.md`（16 大质量门）
- Roles & Manifests：`roles/*.md`（18 角色）与 `manifests/*`
- Workflows：`workflows/*`（编排手册、Mermaid 泳道图与交接契约）
- Data & Policies：`templates/data/*.csv` 与 `templates/policies/*`，`templates/monitoring/*`

## Integration with Core BMAD

1. **After Idea→Proposal**：锁定研究问题/方法/资源与伦理边界 → 进入《运营架构》
2. **Parallel to Execution**：样本/实验/仪器/数据/分析/复现/发表流水线联动
3. **Before Publication/Release**：走 `validate-operations` 与检查清单质量门

## Usage

```
*agent scientific-research → *create-doc research-architecture
*agent scientific-research → *review-operations
*agent scientific-research → *validate-operations
```

## Notes

- 模板变量使用 `{var}`；`<critical_rule>` 为强规则。
- 本扩展用于流程与文档标准化，不替代监管机构/伦理委员会/基金委的正式要求。

---

_Version: 1.0.0_ · _Compatible with BMAD Core >= 1.10_ · _Last Updated: 2025-09-10_
