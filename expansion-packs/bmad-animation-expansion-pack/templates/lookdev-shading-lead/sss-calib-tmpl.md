---
template_id: lookdev-shading-lead/sss-calib
version: 1
purpose: SSS 标定
fields:
  asset: { type: string }
  tests: { type: table, columns: [material, radius, weight, albedo, result] }
outputs:
  - calib/sss-{{asset}}.md
---

# SSS Calibration — {{asset}}

{{tests}}
