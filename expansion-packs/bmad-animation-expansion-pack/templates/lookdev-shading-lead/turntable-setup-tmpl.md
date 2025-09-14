---
template_id: lookdev-shading-lead/turntable-setup
version: 1
purpose: 灯测台/回归场景
fields:
  asset: { type: string }
  hdri: { type: string }
  key_fill_rim: { type: table, columns: [light, intensity, color, radius] }
  props: { type: list, items: string }
  outputs: { type: table, columns: [camera, frame, exposure, note] }
outputs:
  - tests/turntable-{{asset}}.md
---

# Turntable — {{asset}}

- HDRI: {{hdri}}
- K/F/R:
  {{key_fill_rim}}
- Props: {{props}}
- Outputs:
  {{outputs}}
