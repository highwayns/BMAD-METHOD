---
template_id: layout-lead/handoff-lighting
version: 1
purpose: 向 Lighting 交接
fields:
  seq: { type: string }
  contents: { type: table, columns: [item, path, version, notes] }
  aov_ref: { type: list, items: string }
outputs:
  - handoff/handoff-lighting-{{seq}}.md
---

# Handoff to Lighting — {{seq}}

{{contents}}

- AOV Reference: {{aov_ref}}
