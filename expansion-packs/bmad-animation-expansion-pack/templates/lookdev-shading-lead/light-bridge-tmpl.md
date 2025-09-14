---
template_id: lookdev-shading-lead/light-bridge
version: 1
purpose: LookDev→Lighting 桥接
fields:
  seq: { type: string }
  anchors: { type: table, columns: [shot, exposure, gray, chrome, aov_set, notes] }
outputs:
  - bridges/light-bridge-{{seq}}.md
---

# Light Bridge — {{seq}}

{{anchors}}
