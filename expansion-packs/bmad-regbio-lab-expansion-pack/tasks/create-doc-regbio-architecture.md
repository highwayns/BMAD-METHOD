# create-doc | RegBio Lab Operations Architecture

<!-- BMAD Task Spec -->

## Purpose

产出标准化的《再生生物实验室运营架构》文档，覆盖伦理/审批、生物安全/安保、样本/细胞/材料管理、培养/分化与工艺、QC 与 CQAs、设备/环境、LIMS/ELN、数据治理与可重复性、动物/功能验证、转化与移交，并与 BMAD 清单联动形成质量门。

## Inputs

- 模板：templates/output/regbio-architecture-tmpl.yaml
- 参考：伦理/审批清单、BSL 与生物安全政策、SOP/批记录、LIMS/ELN 结构、设备/环境监测、QC 面板与放行标准
- 主清单：checklists/regbio-operations-checklist.md

## Key Activities & Instructions

### 1) Confirm Interaction Mode

- 选项 A **Incremental（默认）**：逐节展示模板占位符与 `custom_elicitation` 菜单，编号选择后再继续。
- 选项 B **YOLO**：一次性填充关键段落（可能牺牲细节）。

### 2) Prepare for Authoring

- 收集协议与 SOP、审批号、细胞系台账、QC 与分化标准、设备/环境与 CMMS、数据/隐私政策。

### 3) Conduct Guided Authoring (Incremental, elicit: true)

对每个模板章节执行：

- 显示**编号选项(1–9)**的引导动作（如供体与同意、BSL 等级/隔离、细胞/类器官契约、CQAs 放行、动物与转化、数据与隐私等）
- 采集你的选择与补充信息 → 填充占位符 → 输出本节草稿
- 节末给出“完成本节/继续下一节”的选项

### 3') Rapid Authoring (YOLO)

- 以默认选项与占位符快速落稿；需要你事后补全细节。

### 4) Generate Final Doc

- 渲染到 `docs/regbio-architecture.md`，附带 `<critical_rule>` 强规则高亮。
- 在“文档验证”章节自动生成与清单（第12章）的对照表。

## BMAD Integration Assessment

- 与 PI/技术/动物/质量/数据的对齐点与缺口，形成改进项进入行动清单。

## Architectural Escalation Assessment

- 将 Critical/Significant 项进入伦理/生安/质量/动物/信息评审；Operational 项进入实施任务。

## Present & Plan

- 生成高层摘要页、操作设计说明与行动清单（负责人/截止/验收）。

## Execute Escalation Protocol

- 按分级触发评审或改进；记录决议与跟踪。

## Outputs

1. `docs/regbio-architecture.md`
2. 清单对照表与强规则摘要
3. 行动计划（含负责人/截止/依赖/验收）
