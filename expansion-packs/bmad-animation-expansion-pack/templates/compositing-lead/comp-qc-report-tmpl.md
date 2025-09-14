---
template_id: compositing-lead/comp-qc-report
version: 1
purpose: 合成 QC 报告
fields:
  seq: { type: string }
  items: { type: table, columns: [area, issue, severity, evidence, fix] }
outputs:
  - qc/comp-qc-{{seq}}.md
---

# Comp QC — {{seq}}

| Area | Issue | Sev | Evidence | Fix |
| ---- | ----- | --- | -------- | --- |

{{items}}
