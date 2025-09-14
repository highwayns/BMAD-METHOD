---
template_id: fx-supervisor/grains-design
version: 1
purpose: 颗粒方案
fields:
  asset: { type: string }
  params: { type: table, columns: [material, stiffness, cohesion, friction, damping, notes] }
outputs:
  - plans/grains-{{asset}}.md
---

# Grains Design — {{asset}}

{{params}}
