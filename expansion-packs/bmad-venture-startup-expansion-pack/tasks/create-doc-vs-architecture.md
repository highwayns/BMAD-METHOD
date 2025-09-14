# create-doc | Venture-backed Startup Operations Architecture

<!-- BMAD Task Spec -->

## Purpose

产出标准化的《风投创业运营架构》文档，覆盖机会论点与商业模式、用户研究与 PMF 假设、OKR/北极星指标、产品与工程（SDLC/发布/质量）、云与 DevOps、隐私与安全、数据与实验、增长与营销、销售与合同、客户成功与支持、募资与董事会、财务与风控、KPI 与复盘，并与 BMAD 清单联动形成质量门。

## Inputs

- 模板：templates/output/vs-architecture-tmpl.yaml
- 参考：机会论点/竞品、客户访谈/调研、产品路线图与待办、架构/云/成本、合规（隐私/SOC2/ISO）、数据模型与埋点、实验与归因、增长与销售漏斗、CS/支持、募资材料与 Cap Table、预算/Runway/财务模型
- 主清单：checklists/vs-operations-checklist.md

## Key Activities & Instructions

### 1) Confirm Interaction Mode

- 选项 A **Incremental（默认）**：逐节展示模板占位符与 `custom_elicitation` 菜单，编号选择后继续。
- 选项 B **YOLO**：一次性填充关键段落（速度优先）。

### 2) Prepare for Authoring

- 收集产品/市场洞察、OKR 与北极星、架构与成本、发布与质量、隐私/安全与供应链、数据与实验、增长与销售、CS 与支持、募资与治理、财务与风控。

### 3) Conduct Guided Authoring (Incremental, elicit: true)

对每个模板章节执行：

- 显示**编号选项(1–9)**（如 PMF 假设、指标与埋点、实验设计、发布策略、权限与加密、增长实验池、CRM/合同/合规、CS 触发器、董事会节奏等）
- 采集信息 → 填充占位符 → 输出本节草稿 → 节末“完成/下一节”

### 3') Rapid Authoring (YOLO)

- 以默认选项与占位符快速落稿，之后补齐细节。

### 4) Generate Final Doc

- 渲染到 `docs/vs-architecture.md`，附 `<critical_rule>` 高亮。
- 在“文档验证”章节生成与清单的对照表。

## Outputs

1. `docs/vs-architecture.md`
2. 清单对照与强规则摘要
3. 行动计划（负责人/截止/依赖/验收）
