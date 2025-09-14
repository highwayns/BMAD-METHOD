---
template_id: modeling-lead/vendor-handoff
version: 1
purpose: 外包交接与回收
fields:
  batch: { type: string }
  contents: { type: table, columns: [item, path, checksum, notes] }
  standards: { type: list, items: string }
outputs:
  - vendor/vendor-handoff-{{batch}}.md
---

# Vendor Handoff — {{batch}}

{{contents}}

- Standards: {{standards}}
