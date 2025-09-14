---
template_id: anim-supervisor/facial-calib
version: 1
purpose: 面部 Rig 标定
fields:
  char: { type: string }
  poses: { type: table, columns: [pose, value, notes] }
  extremes: { type: list, items: string }
  combos: { type: list, items: string }
outputs:
  - facial/facial-calib-{{char}}.md
---

# Facial Calib — {{char}}

## Poses

{{poses}}

- Extremes: {{extremes}}
- Combos: {{combos}}
