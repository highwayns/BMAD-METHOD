---
template_id: compositing-lead/comp-brief
version: 1
purpose: 合成简报（风格锚点/参考/范围）
fields:
  seq: { type: string }
  style_anchors: { type: list, items: string }
  refs: { type: list, items: url }
  assumptions: { type: list, items: string }
  risks: { type: list, items: string }
outputs:
  - docs/comp-brief-{{seq}}.md
---

# Comp Brief — {{seq}}

- Style Anchors: {{style_anchors}}
- Assumptions: {{assumptions}}
- Risks: {{risks}}
- Refs: {{refs}}
