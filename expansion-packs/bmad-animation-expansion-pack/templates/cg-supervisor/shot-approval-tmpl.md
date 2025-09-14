---
template_id: cg-supervisor/shot-approval
version: 1
purpose: 镜头审批记录
fields:
  seq: { type: string }
  shot: { type: string }
  decision: { type: string, enum: [approve, minor-fix, major-rework] }
  reasons: { type: text }
  evidence: { type: list, items: string }
outputs:
  - approvals/shot-{{seq}}-{{shot}}.md
---

# Shot Approval — {{seq}}-{{shot}}

- Decision: {{decision}}
- Reasons: {{reasons}}
- Evidence: {{evidence}}
