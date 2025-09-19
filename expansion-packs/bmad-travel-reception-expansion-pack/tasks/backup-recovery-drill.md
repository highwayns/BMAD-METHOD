# task: backup-recovery-drill

version: 1.0
role: tech-systems-dms-crm
purpose: 备份/恢复演练与RPO/RTO验证。
inputs: [备份/恢复/演练记录]
outputs: [reports/sys/backup-drill-<date>.md]
steps:

- 渲染 templates/ops-runbook-tmpl.yaml（备份版）
- 执行 backup-recovery-check 清单
  acceptance:
- RPO/RTO达标
- 报告完整
