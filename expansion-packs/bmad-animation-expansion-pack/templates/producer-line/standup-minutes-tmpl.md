---
template_id: producer-line/standup-minutes
version: 1
purpose: 站会纪要
fields:
  date: { type: date }
  yesterday: { type: list, items: string }
  today: { type: list, items: string }
  blockers: { type: list, items: string }
  actions: { type: table, columns: [who, what, due, status] }
outputs:
  - meetings/standup-{{date}}.md
---

# 站会纪要 {{date}}

- 昨日：{{yesterday}}
- 今日：{{today}}
- 阻塞：{{blockers}}
- 行动项：{{actions}}
