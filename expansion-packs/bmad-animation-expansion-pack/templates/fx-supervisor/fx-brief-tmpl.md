---
template_id: fx-supervisor/fx-brief
version: 1
purpose: FX 简报
fields:
  seq: { type: string }
  style_anchors: { type: list, items: string }
  refs: { type: list, items: url }
  physical_notes: { type: list, items: string }
  risks: { type: list, items: string }
outputs:
  - docs/fx-brief-{{seq}}.md
---

# FX Brief — {{seq}}

- Style Anchors: {{style_anchors}}
- Physical Notes: {{physical_notes}}
- Risks: {{risks}}
- Refs: {{refs}}
