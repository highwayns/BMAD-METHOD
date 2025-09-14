# validate-operations | Travel Reception

<!-- BMAD Task Spec -->

## Purpose

以标准化 16 章节检查清单执行出团/结算前验证与评分，生成准入与整改报告。

## Inputs

- checklists/travel-operations-checklist.md
- 订单/游客/供应商/保险/发票 等证据与审计日志

## Key Activities & Instructions

1. 选择 **Incremental** 或 **YOLO**；默认 Incremental
2. 逐条验证：记录证据链接、是/否与备注
3. 自动汇总评分与阻断项（Critical/High 阻断出团/结算）
4. 形成整改计划与复核时间窗

## BMAD Integration Assessment

- 与销售/供应商/客服/财务/法务的一致性与依赖核查

## Architectural Escalation Assessment

- 将阻断项分流至安全/合规/财务评审或运营改进

## Outputs

- 验证结果表、合规率、阻断/警告项、整改计划与负责人
