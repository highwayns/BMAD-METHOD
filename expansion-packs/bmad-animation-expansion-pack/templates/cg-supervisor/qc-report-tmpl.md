---
template_id: cg-supervisor/qc-report
version: 1
purpose: QC 报告
fields:
  scope: { type: string }
  items: { type: table, columns: [area, issue, severity, evidence, fix] }
outputs:
  - qc/qc-{{scope}}.md
---

# QC — {{scope}}

| Area | Issue | Sev | Evidence | Fix |
| ---- | ----- | --- | -------- | --- |

{{items}}
