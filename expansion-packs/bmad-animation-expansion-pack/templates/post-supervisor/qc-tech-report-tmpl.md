---
template_id: post-supervisor/qc-tech-report
version: 1
purpose: 技术 QC 报告
fields:
  package: { type: string }
  checks: { type: table, columns: [area, issue, severity, evidence, fix] }
outputs:
  - qc/qc-tech-{{package}}.md
---

# Technical QC — {{package}}

{{checks}}
