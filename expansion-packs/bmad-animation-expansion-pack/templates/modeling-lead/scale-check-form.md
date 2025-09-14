---
template_id: modeling-lead/scale-check
version: 1
purpose: 实尺/单位/比例对账
fields:
  asset: { type: string }
  measures: { type: table, columns: [part, expected, measured, delta, unit] }
  decision: { type: string, enum: [ok, fix, remeasure] }
outputs:
  - reports/scale-check-{{asset}}.md
---

# Scale Check — {{asset}}

{{measures}}

- Decision: {{decision}}
