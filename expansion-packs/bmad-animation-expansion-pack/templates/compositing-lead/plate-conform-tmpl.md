---
template_id: compositing-lead/plate-conform
version: 1
purpose: 素材对账（时基/畸变/色彩）
fields:
  seq: { type: string }
  editorial: { type: table, columns: [shot, src_fps, tc_in, tc_out, handles, notes] }
  color: { type: table, columns: [colorspace, gamut, transfer, whitepoint] }
  distortion: { type: table, columns: [lens, k1, k2, p1, p2, center_x, center_y] }
outputs:
  - reports/plate-conform-{{seq}}.md
---

# Plate Conform — {{seq}}

{{editorial}}
{{color}}
{{distortion}}
