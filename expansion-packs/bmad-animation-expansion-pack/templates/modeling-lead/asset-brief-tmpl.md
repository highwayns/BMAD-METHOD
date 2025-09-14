---
template_id: modeling-lead/asset-brief
version: 1
purpose: 建模简报（造型锚点/比例/模块划分）
fields:
  asset: { type: string }
  category: { type: string, enum: [character, prop, environment, vehicle] }
  scale_unit: { type: string, enum: [m, cm, mm] }
  refs: { type: list, items: url }
  shape_language: { type: list, items: string }
  dimensions: { type: table, columns: [part, size, unit, notes] }
  modules: { type: table, columns: [module, purpose, notes] }
outputs:
  - docs/model-brief-{{asset}}.md
---

# Model Brief — {{asset}}

- Category: {{category}} / Unit: {{scale_unit}}
- Shape Language: {{shape_language}}

## Dimensions

{{dimensions}}

## Modules

{{modules}}
