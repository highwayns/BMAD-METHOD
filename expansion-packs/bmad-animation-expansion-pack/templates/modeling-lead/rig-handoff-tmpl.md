---
template_id: modeling-lead/rig-handoff
version: 1
purpose: 向 Rig 交接
fields:
  asset: { type: string }
  loops: { type: list, items: string }
  weights_hint: { type: list, items: string }
  notes: { type: list, items: string }
outputs:
  - handoff/rig-handoff-{{asset}}.md
---

# Rig Handoff — {{asset}}

- Deform Loops: {{loops}}
- Weights Hints: {{weights_hint}}
- Notes: {{notes}}
