---
template_id: lookdev-shading-lead/look-matching
version: 1
purpose: 概念对齐/实物比对
fields:
  asset: { type: string }
  method: { type: string, enum: [side-by-side, histogram, deltaE] }
  metrics: { type: table, columns: [name, value, goal] }
  deltas: { type: list, items: string }
outputs:
  - reports/look-matching-{{asset}}.md
---

# Look Matching — {{asset}}

- Method: {{method}}
  {{metrics}}
- Deltas: {{deltas}}
