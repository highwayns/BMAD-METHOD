# create-doc | Staffing HR Architecture

<!-- BMAD Task Spec -->

## Purpose

产出标准化的《Staffing HR 业务架构》文档，覆盖客户/岗位契约（Job Profile）、ATS/HRIS 集成、寻源与评测、面试与录用、入职与合规、培训、派遣与排班、薪资与结算、KPI 与合规，并与 BMAD 清单联动形成交付质量门。

## Inputs

- 模板：templates/output/staffing-architecture-tmpl.yaml
- 参考：岗位画像/能力模型、评测量表、隐私与合规策略、培训课程库、排班与薪资规则
- 主清单：checklists/staffing-operations-checklist.md

## Key Activities & Instructions

### 1) Confirm Interaction Mode

- 选项 A **Incremental（默认）**：逐节展示模板占位符与 `custom_elicitation` 菜单，编号选择后再继续。
- 选项 B **YOLO**：一次性填充关键段落（可能牺牲细节）。

### 2) Prepare for Authoring

- 收集客户需求（SLA/职位 JD/费率/合规）、ATS/HRIS 集成点、评测与面试流程、L&D 课程与排期、派遣与薪资规则。

### 3) Conduct Guided Authoring (Incremental, elicit: true)

对每个模板章节执行：

- 显示**编号选项(1–9)**的引导动作（如岗位数据契约、寻源渠道组合、评测矩阵、合规/隐私、派遣与排班规则、SLA 与 KPI 等）
- 采集你的选择与补充信息 → 填充占位符 → 输出本节草稿
- 节末给出“完成本节/继续下一节”的选项

### 3') Rapid Authoring (YOLO)

- 以默认选项与占位符快速落稿；需要你事后补全细节。

### 4) Generate Final Doc

- 渲染到 `docs/staffing-architecture.md`，附带 `<critical_rule>` 强规则高亮。
- 在“文档验证”章节自动生成与清单（第12章）的对照表。

## BMAD Integration Assessment

- 与销售/交付/法务/财务的对齐点与缺口，形成改进项进入行动清单。

## Architectural Escalation Assessment

- 将 Critical/Significant 项进入合规/法务/财务评审；Operational 项进入实施任务。

## Present & Plan

- 生成高层摘要页、操作设计说明与行动清单（负责人/截止/验收）。

## Execute Escalation Protocol

- 按分级触发评审或改进；记录决议与跟踪。

## Outputs

1. `docs/staffing-architecture.md`
2. 清单对照表与强规则摘要
3. 行动计划（含负责人/截止/依赖/验收）
