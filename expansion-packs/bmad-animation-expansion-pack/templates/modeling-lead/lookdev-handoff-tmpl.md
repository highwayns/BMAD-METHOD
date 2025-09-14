---
template_id: modeling-lead/lookdev-handoff
version: 1
purpose: 向 LookDev 交接
fields:
  asset: { type: string }
  contents: { type: table, columns: [item, path, notes] }
  maps: { type: list, items: string }
outputs:
  - handoff/lookdev-handoff-{{asset}}.md
---

# LookDev Handoff — {{asset}}

{{contents}}

- Expected Maps: {{maps}}
