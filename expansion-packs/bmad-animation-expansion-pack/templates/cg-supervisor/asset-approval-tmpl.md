---
template_id: cg-supervisor/asset-approval
version: 1
purpose: 资产审批记录
fields:
  asset: { type: string }
  decision: { type: string, enum: [approve, minor-fix, major-rework] }
  reasons: { type: text }
  notes: { type: list, items: string }
outputs:
  - approvals/asset-{{asset}}.md
---

# Asset Approval — {{asset}}

- Decision: {{decision}}
- Reasons: {{reasons}}
- Notes: {{notes}}
