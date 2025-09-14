---
template_id: cg-supervisor/retake-form
version: 1
purpose: 返修/重渲申请单
fields:
  seq: { type: string }
  shot: { type: string }
  reason: { type: text }
  expected: { type: text }
  priority: { type: string, enum: [P0, P1, P2] }
outputs:
  - change/retake-{{seq}}-{{shot}}.md
---

# Retake — {{seq}}-{{shot}}

- Reason: {{reason}}
- Expected: {{expected}}
- Priority: {{priority}}
