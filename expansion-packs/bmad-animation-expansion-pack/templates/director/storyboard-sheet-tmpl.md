---
template_id: director/storyboard-sheet
version: 1
purpose: 分镜页（图框/台词/机位/运动/备注）
fields:
  seq: { type: string }
  shot: { type: string }
  panel_desc: { type: text }
  dialog: { type: text }
  camera: { type: string }
  move: { type: string }
  notes: { type: text }
outputs:
  - boards/storyboard-{{seq}}-{{shot}}.md
---

# Storyboard {{seq}}-{{shot}}

- 描述：{{panel_desc}}
- 台词：{{dialog}}
- 机位：{{camera}} / 运动：{{move}}
- 备注：{{notes}}
