---
template_id: lighting-lead/denoise-plan
version: 1
purpose: 去噪方案
fields:
  renderer: { type: string }
  params:
    { type: table, columns: [denoiser, type, frames, strength, variance, albedo, normal, notes] }
  metrics: { type: table, columns: [name, value, goal] }
outputs:
  - specs/denoise-plan-{{renderer}}.md
---

# Denoise Plan — {{renderer}}

{{params}}
{{metrics}}
