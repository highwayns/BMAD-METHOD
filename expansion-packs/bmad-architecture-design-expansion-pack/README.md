# BMAD-Method｜建筑设计（Architecture / AEC）管理团队扩展包

## Overview

本扩展包为建筑设计与交付（前期策划/概念/方案/初设/扩初/施工图/BIM/报批/招投标/施工配合/竣工移交/后评估）提供
**标准化的管理团队角色、代理、任务、输出模板、检查清单与编排**，按 BMAD 方法实现 **从委托与合同→场地与法规→方案与协同→
BIM 与协调→报批与许可→招采与施工配合→质量与变更→竣工与运维资料** 的闭环。

## Purpose

补齐 AEC 场景的：

- 法规/规范/消防/无障碍/节能/装配式等 **合规与报批**
- **BIM 标准**（LOD/IFC/族/坐标/碰撞）、模型 QA 与交付包
- **多专业协同**（建/结/机电/室内/景观/幕墙/市政），接口与责任矩阵
- **成本估算与 VE**、投标图与工程量清单、变更与签证
- **可持续/能耗/日照/风环境**分析，LEED/BREEAM/中国绿建
- **文控/修订/图签**与图纸台账、RFI/Submittal/会议纪要留痕

## What's Included

- Agents：`agents/architecture-design.md`
- Templates (Output)：`templates/output/arch-architecture-tmpl.yaml`、`templates/output/arch-implementation-tmpl.yaml`
- Tasks：`tasks/create-doc-arch-architecture.md`、`tasks/review-operations.md`、`tasks/validate-operations.md`
- Checklists：`checklists/arch-operations-checklist.md`（16 大质量门）
- Roles & Manifests：`roles/*.md`（18 角色）与 `manifests/*`
- Workflows：`workflows/*`（编排手册、Mermaid 泳道图与交接契约）
- Data & Policies：`templates/data/*.csv` 与 `templates/policies/*`，`templates/monitoring/*`

## Integration with Core BMAD

1. **After Appointment & Brief**：锁定委托范围/合同条款/设计任务书 → 进入《运营架构》
2. **Parallel to Delivery**：方案/深化/BIM/报批/招采/施工配合流水线联动
3. **Before Permit/Tender**：走 `validate-operations` 与检查清单质量门

## Usage

```
*agent architecture-design → *create-doc arch-architecture
*agent architecture-design → *review-operations
*agent architecture-design → *validate-operations
```

## Notes

- 模板变量使用 `{var}`；`<critical_rule>` 为强规则。
- 本扩展包用于流程与文档标准化，不替代当地法规/审图中心要求。

---

_Version: 1.0.0_ · _Compatible with BMAD Core >= 1.10_ · _Last Updated: 2025-09-10_
