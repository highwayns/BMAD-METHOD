# DLT Pipeline (Batch)

docOutputLocation: docs/de/dlt-batch.md

## Purpose

以 DLT 实现批处理管道，内置期望、幂等键与修复流程。

## Inputs

- templates/pipeline-spec-batch-tmpl.yaml
- templates/expectations-tmpl.yaml

## Steps

- Bronze→Silver→Gold 分层与期望；幂等与去重

## Outputs

- pipelines/batch/\*.yaml
