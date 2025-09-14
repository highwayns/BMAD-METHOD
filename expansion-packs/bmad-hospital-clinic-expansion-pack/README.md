# BMAD-Method｜医院/诊所管理团队扩展包

## Overview

本扩展包为医院/诊所提供 **标准化的管理团队角色、代理、任务、输出模板、检查清单与编排**，帮助按 BMAD 方法落实 **从预约→接诊→诊疗→检验/影像→处方/药房→住院/手术→出院随访→理赔与合规** 的闭环。

## Purpose

在 BMAD 核心流程之外，补齐医疗机构的：

- 医疗质量与患者安全（QPS）、临床路径、应急与感染控制
- EHR/EMR/HIS/PACS/LIS 等系统与集成、隐私与合规（PHI/同意）
- 门急诊/住院/手术/麻醉/检验/影像/药房/护理/公共卫生协同
- 收入周期管理（RCM：挂号/计费/理赔/对账）、KPI 仪表板与事件复盘

## When to Use This Pack

- 新建或升级医院/诊所运营与信息化流程
- 需要标准化的角色分工、文档模板、质量门与交接契约
- 需要任务驱动的自动化代理与统一检查清单

## What's Included

### Agents

- `agents/hospital-clinic.md` — 医疗机构运营代理（人格化、命令化、依赖映射）

### Templates (Output)

- `templates/output/hospital-architecture-tmpl.yaml`
- `templates/output/hospital-implementation-tmpl.yaml`

### Tasks

- `tasks/create-doc-hospital-architecture.md` — 交互式产出《医院/诊所运营架构》
- `tasks/review-operations.md` — 渐进式/YOLO 复核
- `tasks/validate-operations.md` — 16 节检查清单驱动的验证与评分

### Checklists

- `checklists/hospital-operations-checklist.md` — 16 大章节、出院/结算前质量门

### Roles & Manifests

- `roles/*.md`（18 角色）与 `manifests/*`

### Workflows

- `workflows/*` — 编排手册、泳道图与交接契约

### Data & Policies

- `templates/data/*.csv`（患者/预约/医嘱/处方/库存/KPI）与 `templates/policies/*`（隐私/感染控制/应急）

## Integration with Core BMad

1. **After Care Model & Policies**：锁定临床路径与政策 → 进入《运营架构》
2. **Parallel to Clinical Ops**：门诊/住院/手术/检验/药房等流水线运行，信息系统联动
3. **Before Billing/Reporting**：走 `validate-operations` 与检查清单质量门

## Installation

**Manual**

```bash
# 将本扩展包克隆/下载至项目仓库，如 ./bmad-packs/hospital-clinic
```

## Usage Examples

### 1) 生成运营架构文档

```
*agent hospital-clinic → *create-doc hospital-architecture
```

### 2) 复核运营流程

```
*agent hospital-clinic → *review-operations
```

### 3) 验证与准入

```
*agent hospital-clinic → *validate-operations
```

## Team Integration

- 将本扩展包的检查清单作为**出院/结算/对账/合规**前质量门；在架构模板中引用**文档验证章节**与强规则。

## Dependencies

- 需要 EHR/EMR/HIS/RCM/排班/库存系统；隐私/合规/感染控制政策；变量渲染前需赋值。

## Customization

- 可自定义临床路径/预约策略、感染控制标准、药品目录与库存阈值、计费与理赔规则、KPI 面板。

## Notes

- 模板变量使用 `{var}`；`<critical_rule>` 标记的规则为强制性。
- 本扩展用于**流程与文档标准化**，不替代专业医疗建议。

---

_Version: 1.0.0_ · _Compatible with BMad Core >= 1.10_
