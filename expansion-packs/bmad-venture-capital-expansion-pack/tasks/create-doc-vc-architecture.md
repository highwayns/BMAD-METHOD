# create-doc | Venture Capital Operations Architecture

<!-- BMAD Task Spec -->

## Purpose

产出标准化的《VC 运营架构》文档，覆盖基金架构与合规、募资与 LP 关系、投资论点与组合构建、机会流与筛选、尽调与投决、法律文件与交割、投后赋能与治理、估值与报表、现金流与分配、风险与合规、KPI 与复盘，并与 BMAD 清单联动形成质量门。

## Inputs

- 模板：templates/output/vc-architecture-tmpl.yaml
- 参考：LPA/Side Letter、PPM/路演材料、投资策略与目标配比、CRM/管线、DD 清单、IC 模板、TS/SSA、估值政策、财报/审计、ESG/冲突管理、现金流模型
- 主清单：checklists/vc-operations-checklist.md

## Key Activities & Instructions

### 1) Confirm Interaction Mode

- 选项 A **Incremental（默认）**：逐节展示模板占位符与 `custom_elicitation` 菜单，编号选择后继续。
- 选项 B **YOLO**：一次性填充关键段落（速度优先）。

### 2) Prepare for Authoring

- 收集基金条款/合规清单、LP 名单与承诺、论点与目标持仓、管线与优先级、尽调材料、IC 模板与决议、法律与交割清单、投后与治理机制、估值与报表策略、现金流与分配模型、KPI 与风险登记。

### 3) Conduct Guided Authoring (Incremental, elicit: true)

对每个模板章节执行：

- 显示**编号选项(1–9)**（如 Thesis→Dealflow→Screening、尽调域、IC 会议、估值政策、Reserves 规则、LP 报告、ESG/冲突、公私市场对标等）
- 采集信息 → 填充占位符 → 输出本节草稿 → 节末“完成/下一节”

### 3') Rapid Authoring (YOLO)

- 以默认选项与占位符快速落稿，之后补齐细节。

### 4) Generate Final Doc

- 渲染到 `docs/vc-architecture.md`，附 `<critical_rule>` 高亮。
- 在“文档验证”章节生成与清单的对照表。

## Outputs

1. `docs/vc-architecture.md`
2. 清单对照与强规则摘要
3. 行动计划（负责人/截止/依赖/验收）
