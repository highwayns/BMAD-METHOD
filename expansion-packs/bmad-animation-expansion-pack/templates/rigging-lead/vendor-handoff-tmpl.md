---
template_id: rigging-lead/vendor-handoff
version: 1
purpose: 供应商绑定交接
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
