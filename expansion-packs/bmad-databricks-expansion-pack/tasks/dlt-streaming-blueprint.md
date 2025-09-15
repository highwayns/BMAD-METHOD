# DLT Streaming Blueprint (Unified Batch/Stream)

docOutputLocation: docs/blueprints/dlt-streaming.md

## Purpose

统一流批架构，保证 Exactly-once / At-least-once 的端到端契约与可重放。

## Steps

- Streaming 源/水位线/检查点/状态存储规划
- 延迟/乱序处理策略与容忍窗口
- 统一 Gold 语义层的聚合与指标

## Outputs

- pipelines/streaming/\*.yaml
