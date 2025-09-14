# validate-operations | Hospital/Clinic

<!-- BMAD Task Spec -->

## Purpose

以标准化 16 章节检查清单执行出院/结算/对账前验证与评分，生成准入与整改报告。

## Inputs

- checklists/hospital-operations-checklist.md
- QPS/感染/药事/计费/理赔/审计等证据

## Key Activities & Instructions

1. 选择 **Incremental** 或 **YOLO**；默认 Incremental
2. 逐条验证：记录证据链接、是/否与备注
3. 自动汇总评分与阻断项（Critical/High 阻断交付/结算）
4. 形成整改计划与复核时间窗

## BMAD Integration Assessment

- 与医疗/护理/药学/财务/信息/合规的一致性与依赖核查

## Architectural Escalation Assessment

- 将阻断项分流至医疗质量/感染控制/IT/财务评审或运营改进

## Outputs

- 验证结果表、合规率、阻断/警告项、整改计划与负责人
