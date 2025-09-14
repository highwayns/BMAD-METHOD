---
template_id: director/dailies-notes
version: 1
purpose: Dailies 审片记录
fields:
  date: { type: date }
  items: { type: table, columns: [seq, shot, version, verdict, notes, priority] }
outputs:
  - reviews/dailies-notes-{{date}}.md
---

# Dailies — {{date}}

| Seq | Shot | Ver | Verdict | Notes | Priority |
| --- | ---- | --- | ------- | ----- | -------- |

{{items}}
