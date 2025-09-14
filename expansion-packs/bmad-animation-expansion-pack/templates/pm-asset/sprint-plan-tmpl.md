---
template_id: pm-asset/sprint-plan
version: 1
purpose: 迭代计划
fields:
  iteration: { type: string }
  capacity: { type: table, columns: [role, people, days] }
  goals: { type: list, items: string }
  risks: { type: list, items: string }
outputs:
  - plans/sprint-{{iteration}}.md
---

# Sprint Plan — {{iteration}}

- Goals: {{goals}}
- Risks: {{risks}}
  {{capacity}}
