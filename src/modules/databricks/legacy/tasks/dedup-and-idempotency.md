# Deduplication & Idempotency

docOutputLocation: docs/streaming/dedup-idempotency.md

## Purpose

设计幂等键/去重策略（事件 id + 时间/版本），防止重复与乱序影响。

## Inputs

- templates/dedup-idempotency-tmpl.md
- data/idempotency-strategies-kb.md

## Steps

- 选择去重键；Exactly-once/At-least-once 策略与权衡
- 容忍窗口与冲突解决；旁路与回放

## Outputs

- docs/streaming/dedup-idempotency.md
