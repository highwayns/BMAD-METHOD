---
template_id: anim-supervisor/dailies-agenda
version: 1
purpose: 动画 Dailies 议程与行动项
fields:
  date: { type: date }
  items: { type: table, columns: [seq, shot, owner, status, notes] }
  actions: { type: table, columns: [who, what, due, priority] }
outputs:
  - reviews/anim-dailies-{{date}}.md
---

# Animation Dailies — {{date}}

{{items}}

## Actions

{{actions}}
