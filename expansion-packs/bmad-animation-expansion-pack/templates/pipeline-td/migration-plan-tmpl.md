---
template_id: pipeline-td/migration-plan
version: 1
purpose: 迁移计划
fields:
  scope: { type: string }
  steps: { type: table, columns: [step, owner, expected, fallback] }
  schedule: { type: string }
  verification: { type: list, items: string }
outputs:
  - migrations/migration-plan.md
---

# Migration Plan — {{scope}}

{{steps}}

- Schedule: {{schedule}}
- Verification: {{verification}}
