---
template_id: rigging-lead/picker-ui
version: 1
purpose: 控制器选择器与 PickWalk 规则
fields:
  asset: { type: string }
  hotzones: { type: table, columns: [zone, ctrl, key, notes] }
  pickwalk: { type: table, columns: [from, up, down, left, right] }
outputs:
  - ui/picker-ui-{{asset}}.md
---

# Picker UI — {{asset}}

## Hotzones

{{hotzones}}

## PickWalk

{{pickwalk}}
