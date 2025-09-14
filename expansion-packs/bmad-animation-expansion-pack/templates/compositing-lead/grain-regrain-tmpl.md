---
template_id: compositing-lead/grain-regrain
version: 1
purpose: 去噪/重加颗粒
fields:
  seq: { type: string }
  strategy:
    { type: table, columns: [shot, denoise, regrain_preset, noise_profile, threshold, notes] }
outputs:
  - docs/grain-regrain-{{seq}}.md
---

# Grain/Regrain — {{seq}}

{{strategy}}
