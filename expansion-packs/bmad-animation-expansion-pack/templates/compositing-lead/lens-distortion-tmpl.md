---
template_id: compositing-lead/lens-distortion
version: 1
purpose: 镜头畸变/回灌
fields:
  seq: { type: string }
  solves: { type: table, columns: [lens, k1, k2, p1, p2, center_x, center_y, note] }
outputs:
  - docs/lens-distortion-{{seq}}.md
---

# Lens Distortion — {{seq}}

{{solves}}
