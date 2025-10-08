# DLT Streaming Pipeline

docOutputLocation: docs/streaming/dlt-streaming.md

## Purpose

以 DLT 实现流式 Bronze→Silver→Gold，包含期望、旁路与回放。

## Inputs

- templates/streaming-pipeline-spec-tmpl.yaml
- templates/expectations-streaming-tmpl.yaml

## Steps

- Bronze→Silver→Gold 分层、事件时间列、水位与延迟容忍策略
- 期望/断路器与 DLQ；回放与对账

## Outputs

- docs/streaming/dlt-streaming.md
