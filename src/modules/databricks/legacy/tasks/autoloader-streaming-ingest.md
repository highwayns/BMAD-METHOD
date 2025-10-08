# Autoloader Streaming Ingest

docOutputLocation: docs/streaming/autoloader-ingest.md

## Purpose

使用 Autoloader 实现目录级事件流采集，配置 schema hints/evolution、DLQ 与 checkpoint。

## Inputs

- templates/autoloader-streaming-config-tmpl.json

## Steps

- 配置 cloudFiles.\* 参数与 schema hints；启用 incremental listing
- 配置 checkpoint、DLQ 与幂等键生成策略

## Outputs

- docs/streaming/autoloader-ingest.md
