---
template_id: post-supervisor/post-brief
version: 1
purpose: 后期简报（范围/里程碑/风险）
fields:
  show: { type: string }
  scope: { type: list, items: string }
  milestones: { type: table, columns: [name, date, owner, notes] }
  risks: { type: table, columns: [id, description, impact, likelihood, mitigation] }
outputs:
  - docs/post-brief-{{show}}.md
---

# Post Brief — {{show}}

- Scope: {{scope}}
  {{milestones}}
  {{risks}}
