# create-doc | Scientific Research Operations Architecture

<!-- BMAD Task Spec -->

## Purpose

产出标准化的《科研运营架构》文档，覆盖课题/资助、伦理与合规、研究方案与 SOP、样本/实验/仪器、数据管理与隐私、统计与复现、发表与署名、开放共享、知识产权与合作、经费与审计、风险与事件、KPI 与改进，并与 BMAD 清单联动形成质量门。

## Inputs

- 模板：templates/output/research-architecture-tmpl.yaml
- 参考：Proposal/Grant、IRB/IACUC/IBC 文档、DMP 与数据字典、SAP、实验 SOP、计算环境/依赖、署名与冲突声明、IP/合作协议、预算与采购、RCR 政策
- 主清单：checklists/research-operations-checklist.md

## Key Activities & Instructions

### 1) Confirm Interaction Mode

- 选项 A **Incremental（默认）**：逐节展示模板占位符与 `custom_elicitation` 菜单，编号选择后继续。
- 选项 B **YOLO**：一次性填充关键段落（速度优先）。

### 2) Prepare for Authoring

- 收集研究问题与设计、伦理批件与条件、数据契约、统计分析计划、实验 SOP 与校准/QA、计算环境与依赖、发表策略与共享清单、IP 与合作协议、预算与风控。

### 3) Conduct Guided Authoring (Incremental, elicit: true)

对每个模板章节执行：

- 显示**编号选项(1–9)**（如预注册/注册报告、DMP 字段、PII 脱敏、统计功效、容错与复现场景、署名与利益冲突、数据与代码发布等）
- 采集信息 → 填充占位符 → 输出本节草稿 → 节末“完成/下一节”

### 3') Rapid Authoring (YOLO)

- 以默认选项与占位符快速落稿，之后补齐细节。

### 4) Generate Final Doc

- 渲染到 `docs/research-architecture.md`，附 `<critical_rule>` 高亮。
- 在“文档验证”章节生成与清单（第12章）的对照表。

## Outputs

1. `docs/research-architecture.md`
2. 清单对照与强规则摘要
3. 行动计划（负责人/截止/依赖/验收）
