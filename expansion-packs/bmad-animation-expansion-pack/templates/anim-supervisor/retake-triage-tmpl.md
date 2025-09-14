---
template_id: anim-supervisor/retake-triage
version: 1
purpose: 返修分级/路线
fields:
  date: { type: date }
  items: { type: table, columns: [seq, shot, reason, level, route, owner, due] }
outputs:
  - change/retake-triage-{{date}}.md
---

# Retake Triage — {{date}}

{{items}}
