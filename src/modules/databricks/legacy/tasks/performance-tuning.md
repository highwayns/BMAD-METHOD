# Storage & Performance Tuning

docOutputLocation: docs/architecture/performance-tuning.md

## Purpose

存储布局与性能策略：分区/分桶/液态聚类、Z-ORDER、OPTIMIZE、文件大小与压缩。

## Steps

- 以 storage-layout-tmpl.yaml 描述表与分布策略
- 评估列裁剪/谓词下推/小文件合并
- 产出基线压测与建议（含成本权衡）

## Outputs

- storage/layout/\*.yaml
- reports/perf-baseline/\*.md
