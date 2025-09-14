---
template_id: lookdev-shading-lead/hair-shading-calib
version: 1
purpose: 毛发着色标定
fields:
  asset: { type: string }
  params: { type: table, columns: [melanin, roughR, roughTT, tilt, absorption, result] }
outputs:
  - calib/hair-{{asset}}.md
---

# Hair Shading Calibration — {{asset}}

{{params}}
