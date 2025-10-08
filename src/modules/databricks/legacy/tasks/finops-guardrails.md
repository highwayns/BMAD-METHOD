# FinOps Guardrails Task

docOutputLocation: docs/finops/guardrails.md

## Purpose

通过策略+自动化实现成本护栏与预算达成。

## Steps

- 设定配额/Idle-Stop/机池容量上限/Spot 比例
- 周期化输出 finops-report-tmpl.yaml 报告
- 触发超额告警与例外审批

## Outputs

- docs/finops/guardrails.md
- reports/finops/\*.md
