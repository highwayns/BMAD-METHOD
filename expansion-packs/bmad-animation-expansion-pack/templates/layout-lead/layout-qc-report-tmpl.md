---
template_id: layout-lead/layout-qc-report
version: 1
purpose: 布局QC报告
fields:
  seq: { type: string }
  items: { type: table, columns: [area, issue, severity, evidence, fix] }
outputs:
  - qc/layout-qc-{{seq}}.md
---

# Layout QC — {{seq}}

| Area | Issue | Sev | Evidence | Fix |
| ---- | ----- | --- | -------- | --- |

{{items}}
