---
template_id: anim-supervisor/kpi-report
version: 1
purpose: 动画 KPI 报告
fields:
  week: { type: string }
  metrics: { type: table, columns: [name, value, target, status] }
  insights: { type: list, items: string }
  actions: { type: table, columns: [who, what, due] }
outputs:
  - reports/anim-kpi-{{week}}.md
---

# Anim KPI — {{week}}

{{metrics}}

## Insights

- {{insights}}

## Actions

{{actions}}
