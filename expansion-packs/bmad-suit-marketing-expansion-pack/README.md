# BMAD-Method｜西装营销（DTC/零售/定制）管理团队扩展包

## Overview

本扩展包为西装与定制类服装业务提供 **标准化的管理团队角色、代理、任务、输出模板、检查清单与编排**，帮助按 BMAD 方法落地 **从品牌定位→获客与内容→门店与量体→下单与生产→物流交付→售后与改衣→复购与会员** 的闭环。

## Purpose

在 BMAD 核心流程之外，补齐西装营销场景的：

- 客户/线索/订单数据契约与隐私（PII）、会员/权益/忠诚度
- 线上（自营站/电商/社媒/直播）+ 线下（门店/快闪）的全渠道编排
- 面料/尺码/量体/试穿/改衣流与生产排期协同
- 定价/促销/包套/礼盒策略，毛利与消化率
- 营销测量（MMM/归因）、KPI 仪表板与复盘

## When to Use This Pack

- 新建或升级西装/定制品牌的营销与门店运营
- 需要标准化角色分工、模板、质量门与交接契约
- 需要任务驱动的代理与统一检查清单

## What's Included

### Agents

- `agents/suit-marketing.md` — 西装营销运营代理（人格化、命令化、依赖映射）

### Templates (Output)

- `templates/output/suit-architecture-tmpl.yaml`
- `templates/output/suit-implementation-tmpl.yaml`

### Tasks

- `tasks/create-doc-suit-architecture.md` — 交互式产出《西装营销运营架构》
- `tasks/review-operations.md` — 渐进式/YOLO 复核
- `tasks/validate-operations.md` — 16 节检查清单驱动的验证与评分

### Checklists

- `checklists/suit-operations-checklist.md` — 16 大章节、上新/大促/结算前质量门

### Roles & Manifests

- `roles/*.md`（18 角色）与 `manifests/*`

### Workflows

- `workflows/*` — 编排手册、泳道图与交接契约

### Data & Policies

- `templates/data/*.csv`（客户/线索/活动/内容/面料/尺码/量体/订单/改衣/库存/KPI 等）与 `templates/policies/*`（隐私/广告合规/可持续/价格促销/退换改）

## Integration with Core BMad

1. **After Brand & Offering**：锁定定位/客群/货品结构 → 进入《运营架构》
2. **Parallel to Delivery**：营销/门店/生产/物流流水线联动
3. **Before Billing/Reporting**：走 `validate-operations` 与检查清单质量门

## Installation

**Manual**

```bash
# 将本扩展包克隆/下载至项目仓库，如 ./bmad-packs/suit-marketing
```

## Usage Examples

### 1) 生成运营架构文档

```
*agent suit-marketing → *create-doc suit-architecture
```

### 2) 复核运营流程

```
*agent suit-marketing → *review-operations
```

### 3) 验证与准入

```
*agent suit-marketing → *validate-operations
```

## Team Integration

- 将检查清单作为**上新/大促/结算**前质量门；在架构模板中引用**文档验证章节**与强规则。

## Dependencies

- 需要 DTC 电商/CRM/CDP/营销自动化/门店 POS/PLM/OMS/WMS；隐私/广告合规策略；变量渲染前需赋值。

## Customization

- 可自定义尺码/量体字段、面料库与供应商、促销规则、门店 SOP、KPI 面板与归因方法。

## Notes

- 模板变量使用 `{var}`；`<critical_rule>` 标记的规则为强制性。

---

_Version: 1.0.0_ · _Compatible with BMad Core >= 1.10_
