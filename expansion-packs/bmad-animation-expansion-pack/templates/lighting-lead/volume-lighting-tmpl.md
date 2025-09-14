---
template_id: lighting-lead/volume-lighting
version: 1
purpose: 体积光/参与介质
fields:
  seq: { type: string }
  settings: { type: table, columns: [scattering, absorption, anisotropy, step, max_dist] }
  aovs: { type: table, columns: [name, bitdepth, colorspace] }
outputs:
  - plans/volume-lighting-{{seq}}.md
---

# Volume Lighting — {{seq}}

{{settings}}
{{aovs}}
