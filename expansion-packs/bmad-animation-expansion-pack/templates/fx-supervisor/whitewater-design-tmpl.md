---
template_id: fx-supervisor/whitewater-design
version: 1
purpose: 白水方案
fields:
  asset: { type: string }
  params: { type: table, columns: [emission, aging, adhesion, kill_speed, notes] }
outputs:
  - plans/whitewater-{{asset}}.md
---

# Whitewater — {{asset}}

{{params}}
