---
template_id: fx-supervisor/flip-design
version: 1
purpose: FLIP 方案
fields:
  asset: { type: string }
  params: { type: table, columns: [viscosity, surface_tension, particle_sep, narrow_band, notes] }
  whitewater: { type: table, columns: [foam, spray, bubble, threshold, notes] }
outputs:
  - plans/flip-{{asset}}.md
---

# FLIP Design — {{asset}}

{{params}}

## Whitewater

{{whitewater}}
