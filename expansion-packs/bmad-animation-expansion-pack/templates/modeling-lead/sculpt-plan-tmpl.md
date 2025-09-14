---
template_id: modeling-lead/sculpt-plan
version: 1
purpose: 雕刻/形体分级计划
fields:
  asset: { type: string }
  passes: { type: table, columns: [pass, focus, refs, notes] }
outputs:
  - plans/sculpt-plan-{{asset}}.md
---

# Sculpt Plan — {{asset}}

{{passes}}
