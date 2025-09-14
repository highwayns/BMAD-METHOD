---
template_id: post-supervisor/cost-report
version: 1
purpose: 成本与燃尽
fields:
  week: { type: string }
  summary: { type: table, columns: [bucket, baseline, actual, variance] }
  notes: { type: list, items: string }
outputs:
  - reports/cost-{{week}}.md
---

# Cost Report — {{week}}

{{summary}}

- Notes: {{notes}}
