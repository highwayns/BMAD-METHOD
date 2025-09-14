---
template_id: fx-supervisor/cloth-design
version: 1
purpose: 布料方案（FX侧）
fields:
  asset: { type: string }
  params:
    { type: table, columns: [bend, stretch, shear, damping, collision_thickness, substeps, notes] }
outputs:
  - plans/cloth-{{asset}}.md
---

# Cloth Design — {{asset}}

{{params}}
