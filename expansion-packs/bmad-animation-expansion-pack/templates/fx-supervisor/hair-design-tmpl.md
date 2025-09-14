---
template_id: fx-supervisor/hair-design
version: 1
purpose: 毛发/群集摆动方案（FX侧）
fields:
  asset: { type: string }
  params: { type: table, columns: [stiffness, bend, drag, air_density, collisions, notes] }
outputs:
  - plans/hair-{{asset}}.md
---

# Hair Design — {{asset}}

{{params}}
