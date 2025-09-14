---
template_id: art-director/paintover-notes
version: 1
purpose: Paintover 批注记录
fields:
  date: { type: date }
  items: { type: table, columns: [seq, shot, issue, suggestion, priority] }
outputs:
  - reviews/paintover-notes-{{date}}.md
---

# Paintover Notes — {{date}}

| Seq | Shot | Issue | Suggestion | Priority |
| --- | ---- | ----- | ---------- | -------- |

{{items}}
