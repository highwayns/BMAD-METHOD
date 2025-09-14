---
template_id: anim-supervisor/training-plan
version: 1
purpose: 培训计划
fields:
  season: { type: string }
  modules: { type: table, columns: [topic, goal, assgmt, due] }
  calibration: { type: list, items: string }
outputs:
  - training/training-plan-{{season}}.md
---

# Training Plan — {{season}}

{{modules}}

- Calibration: {{calibration}}
