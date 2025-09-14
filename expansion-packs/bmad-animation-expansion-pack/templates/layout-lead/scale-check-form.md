---
template_id: layout-lead/scale-check
version: 1
purpose: 实尺/单位/比例对账
fields:
  seq: { type: string }
  measures: { type: table, columns: [asset, expected_m, measured_m, delta_m, note] }
  decision: { type: string, enum: [ok, fix, remeasure] }
outputs:
  - reports/scale-check-{{seq}}.md
---

# Scale Check — {{seq}}

{{measures}}

- Decision: {{decision}}
