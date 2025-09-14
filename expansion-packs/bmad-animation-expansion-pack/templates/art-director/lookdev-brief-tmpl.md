---
template_id: art-director/lookdev-brief
version: 1
purpose: LookDev 简报/审批
fields:
  asset: { type: string }
  intent: { type: text }
  palette_id: { type: string }
  material_notes: { type: list, items: string }
  lighting_keys: { type: list, items: string }
  success_criteria: { type: list, items: string }
  decision: { type: string, enum: [approve, minor-fix, major-rework], required: false }
outputs:
  - lookdev/lookdev-brief-{{asset}}.md
---

# LookDev Brief — {{asset}}

- Intent: {{intent}}
- Palette: {{palette_id}}
- Material: {{material_notes}}
- Lighting Keys: {{lighting_keys}}
- Success Criteria: {{success_criteria}}
- Decision: {{decision}}
