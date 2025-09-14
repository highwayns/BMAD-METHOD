---
template_id: anim-supervisor/anim-qc-report
version: 1
purpose: 动画 QC 报告
fields:
  seq: { type: string }
  shot: { type: string }
  items: { type: table, columns: [area, issue, severity, evidence, fix] }
outputs:
  - qc/anim-qc-{{seq}}-{{shot}}.md
---

# Animation QC — {{seq}}-{{shot}}

| Area | Issue | Sev | Evidence | Fix |
| ---- | ----- | --- | -------- | --- |

{{items}}
