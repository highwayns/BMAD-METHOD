---
template_id: cg-supervisor/kpi-report
version: 1
purpose: 周度 KPI
fields:
  week: { type: string }
  metrics: { type: table, columns: [name, value, target, status] }
  insights: { type: list, items: string }
  actions: { type: table, columns: [who, what, due] }
outputs:
  - reports/kpi-{{week}}.md
---

# KPI — {{week}}

{{metrics}}

## Insights

- {{insights}}

## Actions

{{actions}}
