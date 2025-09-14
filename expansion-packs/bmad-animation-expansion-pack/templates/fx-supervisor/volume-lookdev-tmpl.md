---
template_id: fx-supervisor/volume-lookdev
version: 1
purpose: 体积着色/灯测/AOV
fields:
  asset: { type: string }
  shaders: { type: table, columns: [name, scatter, absorption, anisotropy, emission] }
  aovs: { type: table, columns: [name, bitdepth, colorspace, premult] }
outputs:
  - look/volume-lookdev-{{asset}}.md
---

# Volume LookDev — {{asset}}

{{shaders}}
{{aovs}}
