# Runbook Program & Auto-remediation

## Purpose

建设运行手册与自动修复策略。

## Inputs

- 历史事故/告警/处理脚本
- templates/runbook-tmpl.yaml
- checklists/runbook-quality-and-autofix.md

## Outputs

- Runbook库与自动化清单。

## Steps

1. 为TOP告警编写Runbook
2. 把Runbook链接进告警与看板
3. 自动化脚本/Runbook测试
4. 知识回写与搜索可用性
5. 月度清理过期/重复Runbook
