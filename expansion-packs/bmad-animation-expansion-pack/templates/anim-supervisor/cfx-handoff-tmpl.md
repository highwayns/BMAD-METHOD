---
template_id: anim-supervisor/cfx-handoff
version: 1
purpose: 与 CFX 的交接
fields:
  seq: { type: string }
  items: { type: table, columns: [shot, cache, notes] }
  collisions: { type: list, items: string }
outputs:
  - handoff/cfx-handshake-{{seq}}.md
---

# CFX Handshake — {{seq}}

{{items}}

- Collisions: {{collisions}}
