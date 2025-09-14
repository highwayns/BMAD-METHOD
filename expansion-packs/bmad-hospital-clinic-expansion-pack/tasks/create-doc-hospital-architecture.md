# create-doc | Hospital/Clinic Operations Architecture

<!-- BMAD Task Spec -->

## Purpose

产出标准化的《医院/诊所运营架构》文档，覆盖患者旅程/临床路径、患者安全与感染控制、EHR/EMR/HIS 集成、医嘱/检验/影像/药房流程、排班与物资、RCM（计费/理赔/对账）、KPI 与合规，并与 BMAD 清单联动形成质量门。

## Inputs

- 模板：templates/output/hospital-architecture-tmpl.yaml
- 参考：护理与诊疗标准、感染控制政策、EHR/EMR/HIS 集成点、药品与耗材目录、RCM 规则
- 主清单：checklists/hospital-operations-checklist.md

## Key Activities & Instructions

### 1) Confirm Interaction Mode

- 选项 A **Incremental（默认）**：逐节展示模板占位符与 `custom_elicitation` 菜单，编号选择后再继续。
- 选项 B **YOLO**：一次性填充关键段落（可能牺牲细节）。

### 2) Prepare for Authoring

- 收集临床路径/医嘱集、感染控制/应急政策、集成清单、药品/耗材目录、预约与排班规则、RCM 费表与理赔规则。

### 3) Conduct Guided Authoring (Incremental, elicit: true)

对每个模板章节执行：

- 显示**编号选项(1–9)**的引导动作（如隐私与同意管理、分诊/预约策略、手术/麻醉安全核对、药品与库存阈值、应急预案、RCM 控制等）
- 采集你的选择与补充信息 → 填充占位符 → 输出本节草稿
- 节末给出“完成本节/继续下一节”的选项

### 3') Rapid Authoring (YOLO)

- 以默认选项与占位符快速落稿；需要你事后补全细节。

### 4) Generate Final Doc

- 渲染到 `docs/hospital-architecture.md`，附带 `<critical_rule>` 强规则高亮。
- 在“文档验证”章节自动生成与清单（第12章）的对照表。

## BMAD Integration Assessment

- 与医疗/护理/药学/财务/信息/合规的对齐点与缺口，形成改进项进入行动清单。

## Architectural Escalation Assessment

- 将 Critical/Significant 项进入医疗质量/感染控制/信息化/财务评审；Operational 项进入实施任务。

## Present & Plan

- 生成高层摘要页、操作设计说明与行动清单（负责人/截止/验收）。

## Execute Escalation Protocol

- 按分级触发评审或改进；记录决议与跟踪。

## Outputs

1. `docs/hospital-architecture.md`
2. 清单对照表与强规则摘要
3. 行动计划（含负责人/截止/依赖/验收）
