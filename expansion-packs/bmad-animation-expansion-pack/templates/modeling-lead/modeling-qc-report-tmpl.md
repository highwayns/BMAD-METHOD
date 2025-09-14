---
template_id: modeling-lead/modeling-qc-report
version: 1
purpose: 建模综合QC报告
fields:
  asset: { type: string }
  items: { type: table, columns: [area, issue, severity, evidence, fix] }
outputs:
  - qc/modeling-qc-{{asset}}.md
---

# Modeling QC — {{asset}}

| Area | Issue | Sev | Evidence | Fix |
| ---- | ----- | --- | -------- | --- |

{{items}}
