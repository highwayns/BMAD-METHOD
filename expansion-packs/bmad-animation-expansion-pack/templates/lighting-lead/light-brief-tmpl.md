---
template_id: lighting-lead/light-brief
version: 1
purpose: 灯光简报（风格锚点/参考/范围）
fields:
  seq: { type: string }
  style_anchors: { type: list, items: string }
  refs: { type: list, items: url }
  assumptions: { type: list, items: string }
  risks: { type: list, items: string }
outputs:
  - docs/light-brief-{{seq}}.md
---

# Light Brief — {{seq}}

- Style Anchors: {{style_anchors}}
- Assumptions: {{assumptions}}
- Risks: {{risks}}
- Refs: {{refs}}
