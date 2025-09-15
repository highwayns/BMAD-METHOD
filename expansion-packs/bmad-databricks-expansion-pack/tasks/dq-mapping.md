# DQ Mapping

docOutputLocation: docs/contracts/dq-mapping.yaml

## Purpose

将业务质量规则映射到 DLT expectations/断路器与阈值。

## Inputs

- templates/dq-mapping-tmpl.yaml

## Steps

- 按字段/表/层级（Bronze/Silver/Gold）生成规则
- 产出 DLT 期望规范（可供管道消费）

## Outputs

- docs/contracts/dq-mapping.yaml
