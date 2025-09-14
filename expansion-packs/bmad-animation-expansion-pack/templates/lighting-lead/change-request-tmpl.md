---
template_id: lighting-lead/change-request
version: 1
purpose: 变更请求
fields:
  id: { type: string }
  impact: { type: text }
  rollback: { type: text }
  communication: { type: list, items: string }
outputs:
  - change/change-request-{{id}}.md
---

# Change Request — {{id}}

- Impact: {{impact}}
- Rollback: {{rollback}}
- Communication: {{communication}}
