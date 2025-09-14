---
template_id: anim-supervisor/acting-brief
version: 1
purpose: 表演简报/节拍表
fields:
  seq: { type: string }
  shot: { type: string }
  logline: { type: text }
  beats: { type: table, columns: [tc, beat, intent, subtext, ref] }
  reference_links: { type: list, items: url }
outputs:
  - docs/acting-brief-{{seq}}-{{shot}}.md
---

# Acting Brief — {{seq}}-{{shot}}

- Logline: {{logline}}

## Beats

{{beats}}

- Refs: {{reference_links}}
