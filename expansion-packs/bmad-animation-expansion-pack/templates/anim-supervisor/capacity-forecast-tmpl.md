---
template_id: anim-supervisor/capacity-forecast
version: 1
purpose: 产能预测
fields:
  week: { type: string }
  loads: { type: table, columns: [animator, shots, complexity_sum, est_days, availability] }
  risks: { type: list, items: string }
outputs:
  - analytics/capacity-forecast-{{week}}.md
---

# Capacity Forecast — {{week}}

{{loads}}

- Risks: {{risks}}
