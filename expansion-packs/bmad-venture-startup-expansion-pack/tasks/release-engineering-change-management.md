# Release Engineering & Change Management

## Purpose

统一CI/CD/发布门/灰度与回滚策略。

## Inputs

- 流水线/分支策略/特性开关/变更记录
- templates/release-plan-and-rollback-tmpl.yaml
- templates/change-request-and-risk-assessment-tmpl.yaml
- checklists/release-gates-and-change-controls.md

## Outputs

- 发布计划/回滚与变更风险评估。

## Steps

1. 变更分级与审批/同伴评审
2. 金丝雀/蓝绿/批次/暂停与回滚
3. 数据库变更策略（向前兼容）
4. 变更成功率与失败率监控
5. 事后复盘→改进流水线
