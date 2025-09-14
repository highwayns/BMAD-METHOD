# validate-infrastructure | Databricks

<!-- BMAD Task Spec -->

## Purpose

以标准化 16 章节检查清单执行生产前验证与评分，生成准入与整改报告。

## Inputs

- checklists/databricks-infrastructure-checklist.md
- 监控/CI/审计与账单证据

## Key Activities & Instructions

1. 选择 **Incremental** 或 **YOLO**；默认 Incremental
2. 逐条验证：记录证据链接、是/否与备注
3. 自动汇总评分与阻断项（Critical/High 阻断上线）
4. 形成整改计划与复核时间窗

## BMAD Integration Assessment

- 与架构/开发/产品的一致性与依赖核查

## Architectural Escalation Assessment

- 将阻断项分流至架构评审或运维改进

## Outputs

- 验证结果表、合规率、阻断/警告项、整改计划与负责人
