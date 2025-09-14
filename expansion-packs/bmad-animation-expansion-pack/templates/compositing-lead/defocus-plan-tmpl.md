---
template_id: compositing-lead/defocus-plan
version: 1
purpose: Defocus/Bokeh/光斑
fields:
  seq: { type: string }
  params: { type: table, columns: [shot, coc, blades, angle, highlight_halo, chroma_ab, notes] }
outputs:
  - docs/defocus-plan-{{seq}}.md
---

# Defocus Plan — {{seq}}

{{params}}
