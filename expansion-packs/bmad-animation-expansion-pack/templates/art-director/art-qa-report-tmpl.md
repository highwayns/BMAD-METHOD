---
template_id: art-director/art-qa-report
version: 1
purpose: 视觉 QA 报告
fields:
  date: { type: date }
  findings: { type: table, columns: [area, issue, severity, evidence, fix] }
outputs:
  - qa/visual-qa-report-{{date}}.md
---

# Visual QA — {{date}}

| Area | Issue | Sev | Evidence | Fix |
| ---- | ----- | --- | -------- | --- |

{{findings}}
