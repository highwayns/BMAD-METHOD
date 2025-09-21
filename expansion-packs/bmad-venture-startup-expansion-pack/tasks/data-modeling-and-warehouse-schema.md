# Data Modeling & Warehouse Schema

## Purpose

设计数仓模型（星型/数据仓湖/数据产品），面向分析与运营。

## Inputs

- 源数据样本/业务流程图
- templates/warehouse-schema-tmpl.yaml

## Outputs

- 主题域模型与加载策略。

## Steps

1. 定义事实/维度与粒度
2. 主外键与缓慢变更策略(SCD)
3. 增量/幂等/回填策略
4. 成本/性能与分区/索引
5. 质量与监控点
