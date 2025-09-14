---
template_id: post-supervisor/kpi-report
version: 1
purpose: 周度 KPI
fields:
  week: { type: string }
  metrics: { type: table, columns: [name, value, target, status] }
  actions: { type: table, columns: [who, what, due] }
outputs:
  - reports/post-kpi-{{week}}.md
---

# Post KPI — {{week}}

{{metrics}}
{{actions}}
