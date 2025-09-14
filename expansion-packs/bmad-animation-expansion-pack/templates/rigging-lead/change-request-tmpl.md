---
template_id: rigging-lead/change-request
version: 1
purpose: 绑定变更请求
fields:
  id: { type: string }
  impact: { type: text }
  rollback: { type: text }
  migration: { type: list, items: string }
outputs:
  - change/change-request-{{id}}.md
---

# Change Request — {{id}}

- Impact: {{impact}}
- Rollback: {{rollback}}
- Migration: {{migration}}
