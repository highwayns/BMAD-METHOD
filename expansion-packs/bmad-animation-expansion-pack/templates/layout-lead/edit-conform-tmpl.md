---
template_id: layout-lead/edit-conform
version: 1
purpose: 剪辑对账（EDL/AAF→镜头映射）
fields:
  seq: { type: string }
  edit_source: { type: string }
  mapping: { type: table, columns: [cut_in, cut_out, timecode, shot, notes] }
outputs:
  - docs/edit-conform-{{seq}}.md
---

# Edit Conform — {{seq}}

- Source: {{edit_source}}
  {{mapping}}
