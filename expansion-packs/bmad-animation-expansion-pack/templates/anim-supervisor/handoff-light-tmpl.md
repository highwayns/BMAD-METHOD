---
template_id: anim-supervisor/handoff-light
version: 1
purpose: 向 Lighting 的交接
fields:
  seq: { type: string }
  items: { type: table, columns: [shot, cache, playblast, notes] }
outputs:
  - handoff/handoff-light-{{seq}}.md
---

# Handoff to Light — {{seq}}

{{items}}
