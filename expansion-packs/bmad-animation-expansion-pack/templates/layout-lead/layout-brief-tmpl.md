---
template_id: layout-lead/layout-brief
version: 1
purpose: 布局简报（范围/参考/基线）
fields:
  seq: { type: string }
  style_anchors: { type: list, items: string }
  refs: { type: list, items: url }
  assumptions: { type: list, items: string }
  risks: { type: list, items: string }
outputs:
  - docs/layout-brief-{{seq}}.md
---

# Layout Brief — {{seq}}

- Style Anchors: {{style_anchors}}
- Assumptions: {{assumptions}}
- Risks: {{risks}}
- Refs: {{refs}}
