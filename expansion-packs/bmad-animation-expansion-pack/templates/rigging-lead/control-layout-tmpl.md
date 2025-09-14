---
template_id: rigging-lead/control-layout
version: 1
purpose: 控制器布局/颜色/层级
fields:
  asset: { type: string }
  controls: { type: table, columns: [ctrl, color, shape, parent, pickwalk, notes] }
  layers: { type: list, items: string }
outputs:
  - docs/control-layout-{{asset}}.md
---

# Control Layout — {{asset}}

{{controls}}

- Display Layers: {{layers}}
