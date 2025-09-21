# Reliability Reviews & Quality Gates

## Purpose

建立Reliability Review与上线质量门。

## Inputs

- 服务目录/最近变更/性能与事故数据
- templates/reliability-review-checklist-tmpl.yaml
- checklists/production-readiness.md

## Outputs

- Review记录与结论。

## Steps

1. 筛选高风险变更进入Review
2. 按SLO/错误预算/容量评估风险
3. 达标则放行/否则行动清单
4. 记录例外与回滚保护
5. 季度汇总与改进行动
