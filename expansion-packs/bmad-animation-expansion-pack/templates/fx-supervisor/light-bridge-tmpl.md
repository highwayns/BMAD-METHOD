---
template_id: fx-supervisor/light-bridge
version: 1
purpose: FX→Lighting 桥接
fields:
  seq: { type: string }
  anchors: { type: table, columns: [shot, exposure, aov_set, gray, chrome, notes] }
outputs:
  - bridges/light-bridge-{{seq}}.md
---

# Light Bridge — {{seq}}

{{anchors}}
