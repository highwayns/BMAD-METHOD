# create-doc | Databricks Lakehouse Architecture

<!-- BMAD Task Spec -->

## Purpose

产出标准化的《Databricks 架构文档》，覆盖 Catalog/Schema/Tables/Permissions、DLT/Autoloader/Jobs、Silver→Gold、Feature Store、Model Serving、Observability 与 FinOps，并与 BMAD 清单联动形成上线质量门。

## Inputs

- 模板：templates/output/databricks-architecture-tmpl.yaml
- 参考：domain-data-map、data-contract、uc-catalog-policy、cluster-policy
- 主清单：checklists/databricks-infrastructure-checklist.md

## Key Activities & Instructions

### 1) Confirm Interaction Mode

- 选项 A **Incremental（默认）**：逐节展示模板占位符与 `custom_elicitation` 菜单，编号选择后再继续。
- 选项 B **YOLO**：一次性填充关键段落（可能牺牲细节）。

### 2) Prepare for Authoring

- 收集契约、域模型、UC 权限草案、集群策略与成本预算、DLT/Jobs/Serving 设计稿。

### 3) Conduct Guided Authoring (Incremental, elicit: true)

对每个模板章节执行：

- 显示**编号选项(1–9)**的引导动作（如分域/表权限、摄取/流式策略、成本守护栏等）
- 采集你的选择与补充信息 → 填充占位符 → 输出本节草稿
- 节末给出“完成本节/继续下一节”的选项

### 3') Rapid Authoring (YOLO)

- 以默认选项与占位符快速落稿；需要你事后补全细节。

### 4) Generate Final Doc

- 渲染到 `docs/databricks-architecture.md`，附带 `<critical_rule>` 强规则高亮。
- 在“文档验证”章节自动生成与清单（第12章）的对照表。

## BMAD Integration Assessment

- 与开发/产品/架构的对齐点与缺口，形成改进项进入行动清单。

## Architectural Escalation Assessment

- 将 Critical/Significant 项进入架构评审；Operational 项进入实施任务。

## Present & Plan

- 生成高层摘要页、技术实现说明与行动清单（负责人/截止/验收）。

## Execute Escalation Protocol

- 按分级触发架构会审或运维改进；记录决议与跟踪。

## Outputs

1. `docs/databricks-architecture.md`
2. 清单对照表与强规则摘要
3. 行动计划（含负责人/截止/依赖/验收）
