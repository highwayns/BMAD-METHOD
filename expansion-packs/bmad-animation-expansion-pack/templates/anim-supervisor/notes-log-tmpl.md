---
template_id: anim-supervisor/notes-log
version: 1
purpose: 动画笔记聚合
fields:
  date: { type: date }
  notes: { type: table, columns: [seq, shot, tag, severity, note, owner, due] }
outputs:
  - notes/anim-notes-{{date}}.md
---

# Notes — {{date}}

| Seq | Shot | Tag | Sev | Note | Owner | Due |
| --- | ---- | --- | --- | ---- | ----- | --- |

{{notes}}
