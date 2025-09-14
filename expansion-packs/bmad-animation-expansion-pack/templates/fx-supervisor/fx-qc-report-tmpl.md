---
template_id: fx-supervisor/fx-qc-report
version: 1
purpose: FX QC 报告
fields:
  asset: { type: string }
  items: { type: table, columns: [area, issue, severity, evidence, fix] }
outputs:
  - qc/fx-qc-{{asset}}.md
---

# FX QC — {{asset}}

| Area | Issue | Sev | Evidence | Fix |
| ---- | ----- | --- | -------- | --- |

{{items}}
