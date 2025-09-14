---
template_id: layout-lead/stereo-plan
version: 1
purpose: 立体布局/深度预算
fields:
  seq: { type: string }
  targets: { type: table, columns: [shot, ioi, parallax_pct, comfort, notes] }
outputs:
  - specs/stereo-plan-{{seq}}.md
---

# Stereo Plan — {{seq}}

{{targets}}
