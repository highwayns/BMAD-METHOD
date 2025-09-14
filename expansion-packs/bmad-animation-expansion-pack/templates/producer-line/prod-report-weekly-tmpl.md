---
template_id: producer-line/prod-report-weekly
version: 1
purpose: 周度生产报告
fields:
  week: { type: string }
  highlights: { type: list, items: string }
  metrics: { type: table, columns: [name, value, target, trend] }
  risks: { type: list, items: string }
  plan_next: { type: list, items: string }
outputs:
  - reports/prod-weekly-{{week}}.md
---

# 周报 {{week}}

- 高光：{{highlights}}
- 指标：{{metrics}}
- 风险/问题：{{risks}}
- 下周计划：{{plan_next}}
