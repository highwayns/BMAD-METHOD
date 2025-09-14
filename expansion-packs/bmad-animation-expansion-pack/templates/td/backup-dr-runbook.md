---
template_id: td/backup-dr-runbook
version: 1
purpose: 备份/容灾运行手册
fields:
  rpo: { type: string }
  rto: { type: string }
  procedures: { type: table, columns: [step, owner, expected, evidence] }
outputs:
  - dr/backup-dr-runbook.md
---

# Backup/DR Runbook

- RPO: {{rpo}} / RTO: {{rto}}
  {{procedures}}
