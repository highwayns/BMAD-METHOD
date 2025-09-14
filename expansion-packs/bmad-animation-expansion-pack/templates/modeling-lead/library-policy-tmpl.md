---
template_id: modeling-lead/library-policy
version: 1
purpose: 资产库治理策略
fields:
  tags: { type: list, items: string }
  deprecation: { type: list, items: string }
  review_cycle: { type: list, items: string }
outputs:
  - library/library-policy.md
---

# Library Policy

- Tags: {{tags}}
- Deprecation: {{deprecation}}
- Review Cycle: {{review_cycle}}
