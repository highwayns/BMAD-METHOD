---
template_id: director/lookdev-approval
version: 1
purpose: LookDev 审批单
fields:
  asset: { type: string }
  palette: { type: list, items: string }
  lighting_notes: { type: list, items: string }
  materials_notes: { type: list, items: string }
  decision: { type: string, enum: [approve, minor-fix, major-rework] }
  reasons: { type: text }
outputs:
  - reviews/lookdev-approval-{{asset}}.md
---

# LookDev Approval — {{asset}}

- Palette: {{palette}}
- Lighting: {{lighting_notes}}
- Materials: {{materials_notes}}
- Decision: {{decision}}
- Reasons: {{reasons}}
