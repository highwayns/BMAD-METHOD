---
template_id: lookdev-shading-lead/lookdev-brief
version: 1
purpose: 外观开发简报
fields:
  asset: { type: string }
  style_anchors: { type: list, items: string }
  material_list: { type: list, items: string }
  refs: { type: list, items: url }
  physical_notes: { type: list, items: string }
outputs:
  - docs/lookdev-brief-{{asset}}.md
---

# LookDev Brief — {{asset}}

- Style Anchors: {{style_anchors}}
- Materials: {{material_list}}
- Physical Notes: {{physical_notes}}
- Refs: {{refs}}
