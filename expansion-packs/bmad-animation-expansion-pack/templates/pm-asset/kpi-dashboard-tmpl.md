---
template_id: pm-asset/kpi-dashboard
version: 1
purpose: KPI 仪表盘
fields:
  week: { type: string }
  metrics: { type: table, columns: [name, value, target, status] }
  actions: { type: table, columns: [who, what, due] }
outputs:
  - reports/kpi-{{week}}.md
---

# KPI — {{week}}

{{metrics}}
{{actions}}
