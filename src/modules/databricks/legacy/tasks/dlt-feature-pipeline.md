# DLT Feature Pipeline

docOutputLocation: docs/ml/features/dlt-feature-pipeline.md

## Purpose

用 DLT 实现离线/准实时特征管道，内置期望与断路器。

## Inputs

- templates/dlt-feature-pipeline-tmpl.yaml

## Steps

- Bronze→Silver→Feature 表；期望与 DLQ；幂等与回放
- 存储布局与性能优化（液态聚类/Z-ORDER）

## Outputs

- docs/ml/features/dlt-feature-pipeline.md
