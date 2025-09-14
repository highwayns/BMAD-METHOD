---
template_id: lookdev-shading-lead/displacement-calib
version: 1
purpose: 置换标定
fields:
  asset: { type: string }
  samples: { type: table, columns: [map, midlevel, scale, bounds, dir, result] }
  notes: { type: list, items: string }
outputs:
  - calib/displacement-{{asset}}.md
---

# Displacement Calibration — {{asset}}

{{samples}}

- Notes: {{notes}}
