# create-doc | Education & Training Operations Architecture

<!-- BMAD Task Spec -->

## Purpose

产出标准化的《教育培训运营架构》文档，覆盖治理与合规、项目/课程体系、教学设计与教研、授课交付与 LMS、测评与学术诚信、学习者服务与干预、数据治理与隐私、可及性与包容、市场与招生、合作与就业、财务与运营、KPI 与持续改进，并与 BMAD 清单联动形成质量门。

## Inputs

- 模板：templates/output/edu-architecture-tmpl.yaml
- 参考：项目/课程大纲、学习成果与 Rubric、授课/运营与 LMS 配置、评估与监考、学习者服务标准与干预策略、隐私/FERPA/数据字典、可及性与 UDL、招生漏斗与 CRM、合作/实习/就业、预算与资源、KPI 看板
- 主清单：checklists/edu-operations-checklist.md

## Key Activities & Instructions

### 1) Confirm Interaction Mode

- 选项 A **Incremental（默认）**：逐节展示模板占位符与 `custom_elicitation` 菜单，编号选择后继续。
- 选项 B **YOLO**：一次性填充关键段落（速度优先）。

### 2) Prepare for Authoring

- 收集治理与认证、项目/课程/模块、教学设计与教研、授课/排课/资源、评估与诚信、学习者画像/风险预警、数据与隐私、可及性、招生与合作、就业与成效、预算与设施。

### 3) Conduct Guided Authoring (Incremental, elicit: true)

对每个模板章节执行：

- 显示**编号选项(1–9)**（如 OBE 学习成果、Rubric 设计、评测蓝图、防作弊策略、WCAG/UDL、xAPI/埋点、保留干预、招生漏斗、企业合作与就业）
- 采集信息 → 填充占位符 → 输出本节草稿 → 节末“完成/下一节”

### 3') Rapid Authoring (YOLO)

- 以默认选项与占位符快速落稿，之后补齐细节。

### 4) Generate Final Doc

- 渲染到 `docs/edu-architecture.md`，附 `<critical_rule>` 高亮。
- 在“文档验证”章节生成与清单对照表。

## Outputs

1. `docs/edu-architecture.md`
2. 清单对照与强规则摘要
3. 行动计划（负责人/截止/依赖/验收）
