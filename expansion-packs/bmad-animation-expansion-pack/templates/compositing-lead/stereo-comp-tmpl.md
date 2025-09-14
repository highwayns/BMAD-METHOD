---
template_id: compositing-lead/stereo-comp
version: 1
purpose: 立体合成
fields:
  seq: { type: string }
  budget: { type: table, columns: [shot, parallax_pct, window, vertical_align, notes] }
outputs:
  - docs/stereo-comp-{{seq}}.md
---

# Stereo Comp — {{seq}}

{{budget}}
