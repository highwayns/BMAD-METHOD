# DLT Batch Blueprint (Bronze→Silver→Gold)

docOutputLocation: docs/blueprints/dlt-batch.md

## Purpose

以 DLT 构建批处理流水线，内置期望(expections)、断路器、修复与回滚。

## Steps

- 以 templates/pipeline-spec-batch-tmpl.yaml 生成规范
- 定义幂等键/去重策略/时序对齐/慢变维（SCD）策略
- 配置期望规则与告警路由；定义数据修复与回滚Runbook

## Outputs

- pipelines/batch/\*.yaml
