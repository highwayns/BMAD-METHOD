# Latency SLO & Alerts

docOutputLocation: docs/streaming/latency-slo.md

## Purpose

定义并监控端到端延迟/新鲜度 SLO 与告警路由。

## Inputs

- templates/latency-slo-tmpl.yaml
- templates/observability-dashboards-tmpl.md

## Steps

- SLI 定义（ingest→gold 延迟、滞后、失败率）
- 告警阈值/抑制与演练；错误预算策略

## Outputs

- docs/streaming/latency-slo.md
