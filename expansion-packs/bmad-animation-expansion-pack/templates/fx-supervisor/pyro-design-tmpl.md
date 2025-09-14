---
template_id: fx-supervisor/pyro-design
version: 1
purpose: Pyro 方案
fields:
  asset: { type: string }
  stages: { type: table, columns: [stage, temp, fuel, buoyancy, cooling, vorticity, notes] }
  shading: { type: table, columns: [aov_set, scatter, absorption, emission, blackbody] }
outputs:
  - plans/pyro-{{asset}}.md
---

# Pyro Design — {{asset}}

## Stages

{{stages}}

## Shading

{{shading}}
