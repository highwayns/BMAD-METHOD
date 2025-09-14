---
template_id: fx-supervisor/rbd-design
version: 1
purpose: RBD 方案
fields:
  asset: { type: string }
  fracture: { type: table, columns: [material, method, piece_count, cluster, notes] }
  constraints: { type: table, columns: [type, strength, break_cond, rest_length, notes] }
outputs:
  - plans/rbd-{{asset}}.md
---

# RBD Design — {{asset}}

## Fracture

{{fracture}}

## Constraints

{{constraints}}
