---
template_id: modeling-lead/lod-table
version: 1
purpose: LOD/代理策略
fields:
  asset: { type: string }
  levels: { type: table, columns: [lod, tris, purpose, switch_distance, notes] }
outputs:
  - specs/lod-table-{{asset}}.md
---

# LOD Table — {{asset}}

{{levels}}
