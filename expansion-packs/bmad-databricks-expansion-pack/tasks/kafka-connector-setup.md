# Kafka Connector Setup

docOutputLocation: docs/streaming/kafka-connector.md

## Purpose

配置 Kafka 读取（SASL/TLS/起始位点/主题策略/分区分配/压缩）。

## Inputs

- templates/kafka-connector-config-tmpl.json

## Steps

- 安全与认证参数；起始位点与位移提交策略
- 背压/重试/超时；幂等写入/去重策略

## Outputs

- docs/streaming/kafka-connector.md
