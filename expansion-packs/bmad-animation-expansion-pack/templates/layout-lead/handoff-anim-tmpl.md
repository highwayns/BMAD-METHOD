---
template_id: layout-lead/handoff-anim
version: 1
purpose: 向 Animation 交接
fields:
  seq: { type: string }
  contents: { type: table, columns: [item, path, version, notes] }
outputs:
  - handoff/handoff-anim-{{seq}}.md
---

# Handoff to Animation — {{seq}}

{{contents}}
