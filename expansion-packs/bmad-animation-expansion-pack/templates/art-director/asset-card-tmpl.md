---
template_id: art-director/asset-card
version: 1
purpose: 资产卡片（设计→生产桥接）
fields:
  asset_id: { type: string }
  type: { type: string, enum: [character, environment, prop] }
  design_refs: { type: list, items: url }
  spec_ref: { type: path }
  lookdev_ref: { type: path }
  status: { type: string, enum: [design, review, approved, handoff] }
outputs:
  - assets/{{asset_id}}-card.md
---

# Asset Card — {{asset_id}}

- Type: {{type}}
- Design Refs: {{design_refs}}
- Spec: {{spec_ref}}
- LookDev: {{lookdev_ref}}
- Status: {{status}}
