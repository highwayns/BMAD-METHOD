---
template_id: rigging-lead/space-switch-map
version: 1
purpose: 空间切换/父子约定
fields:
  asset: { type: string }
  switches: { type: table, columns: [ctrl, spaces, default, record_attr, notes] }
  autos: { type: list, items: string }
outputs:
  - specs/space-switch-{{asset}}.md
---

# Space Switch Map — {{asset}}

{{switches}}

- Auto behaviors: {{autos}}
