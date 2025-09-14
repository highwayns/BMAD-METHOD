---
template_id: modeling-lead/retopo-plan
version: 1
purpose: 重拓扑方案
fields:
  asset: { type: string }
  loops: { type: table, columns: [region, loop_rule, reason] }
  poles: { type: table, columns: [coord, type, mitigation] }
  budgets: { type: table, columns: [zone, target_tris, tolerance] }
outputs:
  - plans/retopo-plan-{{asset}}.md
---

# Retopo Plan — {{asset}}

## Loops

{{loops}}

## Poles

{{poles}}

## Budgets

{{budgets}}
