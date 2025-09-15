# Data Quality Rules & Circuit Breakers

docOutputLocation: docs/quality/dq-rules.md

## Purpose

定义质量规则字典（完整性、唯一性、范围、及时性）与断路器/降级策略。

## Steps

- 模板 dq-expectations-tmpl.yaml → 规则实例化
- 定义度量与配额（错误预算式质量目标）
- 生成修复脚本与回放指引（runbook-repair-tmpl.md）

## Outputs

- dq/rules/\*.yaml
- docs/quality/dq-rules.md
