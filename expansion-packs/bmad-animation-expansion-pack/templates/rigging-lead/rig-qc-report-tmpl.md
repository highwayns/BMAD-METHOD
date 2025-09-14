---
template_id: rigging-lead/rig-qc-report
version: 1
purpose: 绑定 QC 报告
fields:
  asset: { type: string }
  items: { type: table, columns: [area, issue, severity, evidence, fix] }
outputs:
  - qc/rig-qc-{{asset}}.md
---

# Rig QC — {{asset}}

| Area | Issue | Sev | Evidence | Fix |
| ---- | ----- | --- | -------- | --- |

{{items}}
