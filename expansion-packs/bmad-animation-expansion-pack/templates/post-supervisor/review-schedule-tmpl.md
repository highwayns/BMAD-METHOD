---
template_id: post-supervisor/review-schedule
version: 1
purpose: Review/Dailies 议程
fields:
  week: { type: string }
  agenda: { type: table, columns: [date, start, duration, room, topics, owners] }
outputs:
  - schedules/review-{{week}}.md
---

# Review Schedule — {{week}}

{{agenda}}
