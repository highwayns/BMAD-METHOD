# create-doc | Architecture Design Operations Architecture

<!-- BMAD Task Spec -->

## Purpose

产出标准化的《建筑设计运营架构》文档，覆盖委托/合同、场地与法规、概念/方案、初设/扩初、施工图、BIM 标准与协同、能源与可持续、报批与许可、招投标文件、施工配合（CA）、文控与移交，并与 BMAD 清单联动形成质量门。

## Inputs

- 模板：templates/output/arch-architecture-tmpl.yaml
- 参考：设计任务书/合同、场地资料与测绘、法规/审图要点、BIM 标准、协调计划、能耗/日照/风环境分析、报批清单、投标与工程量、CA 流程
- 主清单：checklists/arch-operations-checklist.md

## Key Activities & Instructions

### 1) Confirm Interaction Mode

- 选项 A **Incremental（默认）**：逐节展示模板占位符与 `custom_elicitation` 菜单，编号选择后继续。
- 选项 B **YOLO**：一次性填充关键段落（速度优先）。

### 2) Prepare for Authoring

- 收集合同与任务书、场地与测绘、法规清单、专业接口与矩阵、BIM 标准、分析与报批项、投标与工程量、CA 与文控。

### 3) Conduct Guided Authoring (Incremental, elicit: true)

对每个模板章节执行：

- 显示**编号选项(1–9)**（如法规核对、BIM 族与坐标、碰撞策略、能耗目标、报批清单、图纸台账、修订流等）
- 采集信息 → 填充占位符 → 输出本节草稿 → 节末“完成/下一节”

### 3') Rapid Authoring (YOLO)

- 以默认选项与占位符快速落稿，之后补齐细节。

### 4) Generate Final Doc

- 渲染到 `docs/arch-architecture.md`，附 `<critical_rule>` 高亮。
- 在“文档验证”章节生成与清单（第12章）的对照表。

## BMAD Integration Assessment

- 与结构/机电/室内/景观/幕墙/市政/造价/法务/招采/施工的对齐点与缺口，形成改进项与行动清单。

## Architectural Escalation Assessment

- 将 Critical/Significant 项进入合规/消防/报批/造价/法务评审；Operational 项进入实施任务。

## Outputs

1. `docs/arch-architecture.md`
2. 清单对照与强规则摘要
3. 行动计划（负责人/截止/依赖/验收）
