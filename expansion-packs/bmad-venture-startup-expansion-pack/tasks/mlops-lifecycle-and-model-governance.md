# MLOps Lifecycle & Model Governance

## Purpose

覆盖数据→训练→评测→发布→监控→回滚的模型全生命周期治理。

## Inputs

- templates/ml-model-card-tmpl.yaml
- templates/ml-eval-plan-tmpl.yaml
- templates/model-release-checklist-tmpl.yaml

## Outputs

- 模型卡、评测计划与上线检查、监控与回滚策略。

## Steps

1. 定义任务/数据集/指标与基线
2. 设计评测集与对齐业务指标
3. 灰度上线与A/B评测
4. 漂移/偏差/滥用监控
5. 回滚策略与再训练节奏
