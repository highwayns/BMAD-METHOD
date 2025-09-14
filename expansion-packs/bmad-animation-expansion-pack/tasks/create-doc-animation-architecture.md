# create-doc | Animation Production Architecture

<!-- BMAD Task Spec -->

## Purpose

产出标准化的《动画制作架构》文档，覆盖管线（Pipeline-as-Code）、资产/镜头管理、评审与合规、渲染预算与排期，并与 BMAD 清单联动形成交付质量门。

## Inputs

- 模板：templates/output/animation-architecture-tmpl.yaml
- 参考：命名规范、资产/镜头数据契约、评审平台配置、渲染预算
- 主清单：checklists/animation-production-checklist.md

## Key Activities & Instructions

### 1) Confirm Interaction Mode

- 选项 A **Incremental（默认）**：逐节展示模板占位符与 `custom_elicitation` 菜单，编号选择后再继续。
- 选项 B **YOLO**：一次性填充关键段落（可能牺牲细节）。

### 2) Prepare for Authoring

- 收集创意简报/剧本、命名规范、资产台账、镜头清单、评审节奏与签字流、渲染与预算。

### 3) Conduct Guided Authoring (Incremental, elicit: true)

对每个模板章节执行：

- 显示**编号选项(1–9)**的引导动作（如 DCC 栈选择、评审节奏、渲染引擎与队列策略、IP 安全等）
- 采集你的选择与补充信息 → 填充占位符 → 输出本节草稿
- 节末给出“完成本节/继续下一节”的选项

### 3') Rapid Authoring (YOLO)

- 以默认选项与占位符快速落稿；需要你事后补全细节。

### 4) Generate Final Doc

- 渲染到 `docs/animation-architecture.md`，附带 `<critical_rule>` 强规则高亮。
- 在“文档验证”章节自动生成与清单（第12章）的对照表。

## BMAD Integration Assessment

- 与开发/产品/架构（此处可映射为导演/制片/技术）的对齐点与缺口，形成改进项进入行动清单。

## Architectural Escalation Assessment

- 将 Critical/Significant 项进入技术/艺术评审会；Operational 项进入实施任务。

## Present & Plan

- 生成高层摘要页、技术实现说明与行动清单（负责人/截止/验收）。

## Execute Escalation Protocol

- 按分级触发评审或运维改进；记录决议与跟踪。

## Outputs

1. `docs/animation-architecture.md`
2. 清单对照表与强规则摘要
3. 行动计划（含负责人/截止/依赖/验收）
