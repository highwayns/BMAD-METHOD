# create-doc | Travel Reception Operations Architecture

<!-- BMAD Task Spec -->

## Purpose

产出标准化的《旅游接待运营架构》文档，覆盖客户与游客数据契约、行程策划与预算、供应商合同与 SLA、预订与对账、落地执行与应急、保险与签证、KPI 与复盘，并与 BMAD 清单联动形成质量门。

## Inputs

- 模板：templates/output/travel-architecture-tmpl.yaml
- 参考：客户条款/价目、游客信息/同意、签证/保险模板、供应商合同、现场 SOP、结算与发票规则
- 主清单：checklists/travel-operations-checklist.md

## Key Activities & Instructions

### 1) Confirm Interaction Mode

- 选项 A **Incremental（默认）**：逐节展示模板占位符与 `custom_elicitation` 菜单，编号选择后再继续。
- 选项 B **YOLO**：一次性填充关键段落（可能牺牲细节）。

### 2) Prepare for Authoring

- 收集客户需求与预算、游客数据契约、供应商名录与价单、行程与房车位、应急预案与保险/签证模板。

### 3) Conduct Guided Authoring (Incremental, elicit: true)

对每个模板章节执行：

- 显示**编号选项(1–9)**的引导动作（如数据契约、控房控位、车导资源、签证保险、风险与应急、KPI/成本等）
- 采集你的选择与补充信息 → 填充占位符 → 输出本节草稿
- 节末给出“完成本节/继续下一节”的选项

### 3') Rapid Authoring (YOLO)

- 以默认选项与占位符快速落稿；需要你事后补全细节。

### 4) Generate Final Doc

- 渲染到 `docs/travel-architecture.md`，附带 `<critical_rule>` 强规则高亮。
- 在“文档验证”章节自动生成与清单（第12章）的对照表。

## BMAD Integration Assessment

- 与销售/供应商/客服/财务/法务的对齐点与缺口，形成改进项进入行动清单。

## Architectural Escalation Assessment

- 将 Critical/Significant 项进入安全/合规/财务评审；Operational 项进入实施任务。

## Present & Plan

- 生成高层摘要页、操作设计说明与行动清单（负责人/截止/验收）。

## Execute Escalation Protocol

- 按分级触发评审或改进；记录决议与跟踪。

## Outputs

1. `docs/travel-architecture.md`
2. 清单对照表与强规则摘要
3. 行动计划（含负责人/截止/依赖/验收）
