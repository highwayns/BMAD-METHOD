---
template_id: layout-lead/camera-blocking
version: 1
purpose: 机位/轨迹/速度曲线
fields:
  seq: { type: string }
  tracks: { type: table, columns: [shot, rig, move, duration, speed_curve, notes] }
outputs:
  - docs/camera-blocking-{{seq}}.md
---

# Camera Blocking — {{seq}}

{{tracks}}
