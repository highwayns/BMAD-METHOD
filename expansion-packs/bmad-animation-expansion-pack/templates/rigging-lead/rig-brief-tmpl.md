---
template_id: rigging-lead/rig-brief
version: 1
purpose: 绑定简报（目标/接口/基线）
fields:
  asset: { type: string }
  goals: { type: list, items: string }
  anim_interfaces: { type: list, items: string }
  cfx_interfaces: { type: list, items: string }
  export_targets: { type: list, items: string }
outputs:
  - docs/rig-brief-{{asset}}.md
---

# Rig Brief — {{asset}}

- Goals: {{goals}}
- Anim Interfaces: {{anim_interfaces}}
- CFX Interfaces: {{cfx_interfaces}}
- Export Targets: {{export_targets}}
