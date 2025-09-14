# create-doc | Suit Marketing Operations Architecture

<!-- BMAD Task Spec -->

## Purpose

产出标准化的《西装营销运营架构》文档，覆盖品牌与定位、客群与数据契约、全渠道营销与内容、门店/量体/改衣协同、定价与促销、下单与生产/物流、KPI 与合规，并与 BMAD 清单联动形成质量门。

## Inputs

- 模板：templates/output/suit-architecture-tmpl.yaml
- 参考：品牌与定位文件、CRM/CDP 字段与口径、活动计划/预算、面料与款式库、门店 SOP、价格与促销策略、OMS/WMS 对接
- 主清单：checklists/suit-operations-checklist.md

## Key Activities & Instructions

### 1) Confirm Interaction Mode

- 选项 A **Incremental（默认）**：逐节展示模板占位符与 `custom_elicitation` 菜单，编号选择后再继续。
- 选项 B **YOLO**：一次性填充关键段落（可能牺牲细节）。

### 2) Prepare for Authoring

- 收集人群画像、归因与数据契约、货品结构与面料库、门店/量体与改衣流程、定价/促销/大促规划、运营 KPI。

### 3) Conduct Guided Authoring (Incremental, elicit: true)

对每个模板章节执行：

- 显示**编号选项(1–9)**的引导动作（如数据契约、渠道配比、活动日历、量体字段、改衣 SLA、促销与价格护城河、KPI 等）
- 采集你的选择与补充信息 → 填充占位符 → 输出本节草稿
- 节末给出“完成本节/继续下一节”的选项

### 3') Rapid Authoring (YOLO)

- 以默认选项与占位符快速落稿；需要你事后补全细节。

### 4) Generate Final Doc

- 渲染到 `docs/suit-architecture.md`，附带 `<critical_rule>` 强规则高亮。
- 在“文档验证”章节自动生成与清单（第12章）的对照表。

## BMAD Integration Assessment

- 与品牌/电商/门店/供应/财务/法务的对齐点与缺口，形成改进项进入行动清单。

## Architectural Escalation Assessment

- 将 Critical/Significant 项进入品牌/合规/供应/财务评审；Operational 项进入实施任务。

## Present & Plan

- 生成高层摘要页、操作设计说明与行动清单（负责人/截止/验收）。

## Execute Escalation Protocol

- 按分级触发评审或改进；记录决议与跟踪。

## Outputs

1. `docs/suit-architecture.md`
2. 清单对照表与强规则摘要
3. 行动计划（含负责人/截止/依赖/验收）
