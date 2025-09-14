# BMAD-Method｜再生生物实验室（Regenerative Biology Lab）管理团队扩展包

## Overview

本扩展包为再生生物实验室（干细胞/类器官/组织工程/前临床）提供 **标准化的管理团队角色、代理、任务、输出模板、检查清单与编排**，帮助以 BMAD 方法落地**从样本/供体→细胞系/材料→培养与分化→组装与评价→动物/功能验证→数据与合规→转化与移交**的闭环。

## Purpose

在 BMAD 核心流程之外，补齐 RegBio 场景的：

- 伦理与审批（IRB/IEC/IACUC）、生物安全/安保、GxP 就绪（GLP/GMP-like）
- 细胞系溯源/鉴定、无支原体/无菌、分化与质量属性（CQAs）标准化
- LIMS/ELN、样本与库存、设备校准/维护、环境监测
- 多组学/成像/功能检测、数据治理（FAIR）、隐私与 IP/MTA
- 技术转移/可重复性、冷链与运输、归档与发表/专利

## When to Use This Pack

- 新建或升级再生生物实验室/平台
- 需要标准化的角色分工、文档模板、质量门、交接契约
- 需要任务驱动的代理与统一检查清单

## What's Included

### Agents

- `agents/regbio-lab.md` — 实验室运营代理（人格化、命令化、依赖映射）

### Templates (Output)

- `templates/output/regbio-architecture-tmpl.yaml`
- `templates/output/regbio-implementation-tmpl.yaml`

### Tasks

- `tasks/create-doc-regbio-architecture.md` — 交互式产出《实验室运营架构》
- `tasks/review-operations.md` — 渐进式/YOLO 复核
- `tasks/validate-operations.md` — 16 节检查清单驱动的验证与评分

### Checklists

- `checklists/regbio-operations-checklist.md` — 16 大章节、出库/发表/转化前质量门

### Roles & Manifests

- `roles/*.md`（18 角色）与 `manifests/*`

### Workflows

- `workflows/*` — 编排手册、泳道图与交接契约

### Data & Policies

- `templates/data/*.csv`（细胞系/供体/样本/实验/QC/设备/审批/KPI 等）与 `templates/policies/*`（生物安全/伦理/基因编辑/数据治理）

## Integration with Core BMad

1. **After Governance & Ethics**：锁定伦理/审批与 SOP → 进入《运营架构》
2. **Parallel to Lab Operations**：培养/分化/组装/检测流水线与 LIMS/ELN 联动
3. **Before Transfer/Publication**：走 `validate-operations` 与检查清单质量门

## Installation

**Manual**

```bash
# 将本扩展包克隆/下载至项目仓库，如 ./bmad-packs/regbio-lab
```

## Usage Examples

### 1) 生成运营架构文档

```
*agent regbio-lab → *create-doc regbio-architecture
```

### 2) 复核运营流程

```
*agent regbio-lab → *review-operations
```

### 3) 验证与准入

```
*agent regbio-lab → *validate-operations
```

## Team Integration

- 将本扩展包的检查清单作为**出库/提交发表/技术转移**前质量门；在架构模板中引用**文档验证章节**与强规则。

## Dependencies

- 需要 LIMS/ELN、样本与库存管理、设备 CMMS/维护、环境监测；伦理/隐私/生物安全政策；变量渲染前需赋值。

## Customization

- 可自定义细胞系/类器官/组织工程工艺、CQAs 与放行标准、动物/功能验证方案、数据标准与可视化报表。

## Notes

- 模板变量使用 `{var}`；`<critical_rule>` 标记的规则为强制性。
- 本扩展用于流程与文档标准化，不替代专业伦理/合规/临床建议。

---

_Version: 1.0.0_ · _Compatible with BMad Core >= 1.10_
