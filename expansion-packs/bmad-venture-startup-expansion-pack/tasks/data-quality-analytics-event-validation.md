# Data Quality, Analytics & Event Validation

## Purpose

校验数据管道/埋点/指标与报表一致性。

## Inputs

- 事件方案/ETL/维表/报表
- templates/data-validation-sql-pack-tmpl.yaml
- data/ci-quality-gates-patterns.md

## Outputs

- 数据质量SQL包与差异报告。

## Steps

1. 维度/度量/口径对齐与数据字典
2. 事件校验：去重/顺序/延迟/丢失
3. 端到端对账（源→数仓→报表）
4. 回归套件 + 合成数据/时间旅行
5. 监控与异常升级
