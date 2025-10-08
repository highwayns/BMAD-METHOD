# Watermarks & Lateness

docOutputLocation: docs/streaming/watermarks-lateness.md

## Purpose

定义事件时间水位与乱序容忍窗口，平衡延迟与完整性。

## Inputs

- templates/watermark-config-tmpl.yaml
- data/watermarking-lateness-kb.md

## Steps

- 评估乱序分布，确定 allowedLateness 与窗口策略
- 定义延迟/新鲜度 SLO 与异常响应

## Outputs

- docs/streaming/watermarks-lateness.md
