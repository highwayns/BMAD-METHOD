---
template_id: lookdev-shading-lead/approval-record
version: 1
purpose: 审批记录（镜头/资产）
fields:
  scope: { type: string }
  decision: { type: string, enum: [approve, minor-fix, major-rework] }
  reasons: { type: text }
  evidence: { type: list, items: string }
outputs:
  - approvals/approval-{{scope}}.md
---

# Approval — {{scope}}

- Decision: {{decision}}
- Reasons: {{reasons}}
- Evidence: {{evidence}}
