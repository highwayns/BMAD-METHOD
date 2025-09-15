# Setup DLT Pipeline Task

docOutputLocation: docs/pipelines/dlt-setup.md

## Purpose

以 DLT 为基干，定义 Bronze→Silver→Gold 流水线，启用期望数据质量规则、断路器与重试策略。

## Steps

- pipeline-spec-tmpl.yaml → 生成 DLT 规范
- 绑定作业/机池/策略，设置 Auto-Stop 与成本标签
- 配置期望值（expectations）与告警
- 验证 SLO（延迟/吞吐/失败率）并产出基线图表

## Outputs

- pipelines/\*.yaml
- docs/pipelines/dlt-setup.md
