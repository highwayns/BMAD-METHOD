---
template_id: cg-supervisor/dailies-agenda
version: 1
purpose: Dailies 议程
fields:
  date: { type: date }
  items: { type: table, columns: [seq, shot, status, owner, notes] }
  actions: { type: table, columns: [who, what, due, priority] }
outputs:
  - reviews/dailies-{{date}}.md
---

# Dailies — {{date}}

{{items}}

## Actions

{{actions}}
