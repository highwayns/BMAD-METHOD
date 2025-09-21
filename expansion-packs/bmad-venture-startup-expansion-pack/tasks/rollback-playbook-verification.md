# Rollback Playbook & Verification

## Purpose

把回滚做成可随时触发的工程能力。

## Inputs

- 回滚脚本/数据库策略/特性开关
- templates/rollback-runbook-tmpl.yaml
- checklists/rollback-verification.md

## Outputs

- 回滚运行手册与验证清单。

## Steps

1. 触发条件/授权与一键化
2. 数据/模式/迁移回滚策略
3. 回滚后验证与缓存/索引修复
4. 用户补偿与公告模板
5. 演练与度量：MTTR/触发到恢复
