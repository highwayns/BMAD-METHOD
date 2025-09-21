# Health Score Model & Early Warning

## Purpose

构建健康度模型（使用/价值/支持/关系）与预警机制。

## Inputs

- 数据字段字典/阈值与标签
- templates/health-score-model-tmpl.yaml
- data/health-score-signals-examples.md

## Outputs

- 健康度定义/阈值/标签与预警策略。

## Steps

1. 选择信号与权重/窗口
2. 定义阈值/护栏/冷却期
3. 构建自动告警与队列路由
4. 与行动手册/剧本绑定
5. 每季度回测与再标定
