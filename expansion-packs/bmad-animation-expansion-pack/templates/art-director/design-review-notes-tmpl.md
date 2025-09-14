---
template_id: art-director/design-review-notes
version: 1
purpose: 设计评审记录
fields:
  date: { type: date }
  items: { type: table, columns: [topic, decision, owner, due, priority] }
outputs:
  - reviews/design-review-{{date}}.md
---

# Design Review — {{date}}

| Topic | Decision | Owner | Due | Priority |
| ----- | -------- | ----- | --- | -------- |

{{items}}
