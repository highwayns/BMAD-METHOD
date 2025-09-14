---
template_id: director/client-review-agenda
version: 1
purpose: 客户评审议程与记录
fields:
  date: { type: date }
  topics: { type: list, items: string }
  decisions: { type: table, columns: [topic, decision, owner, due] }
outputs:
  - client/review-{{date}}.md
---

# Client Review — {{date}}

- Topics: {{topics}}
- Decisions: {{decisions}}
