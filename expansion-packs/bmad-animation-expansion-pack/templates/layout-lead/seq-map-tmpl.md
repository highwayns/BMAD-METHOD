---
template_id: layout-lead/seq-map
version: 1
purpose: 序列拆解与 coverage 设计
fields:
  seq: { type: string }
  beats: { type: table, columns: [beat, purpose, priority, notes] }
  coverage: { type: table, columns: [shot, type, lens_hint, notes] }
outputs:
  - plans/seq-breakdown-{{seq}}.md
---

# Sequence Breakdown — {{seq}}

## Beats

{{beats}}

## Coverage

{{coverage}}
