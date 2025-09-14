---
template_id: cg-supervisor/shot-brief
version: 1
purpose: 镜头任务单
fields:
  seq: { type: string }
  shot: { type: string }
  cut: { type: string }
  intent: { type: text }
  aov_set: { type: string }
  notes: { type: list, items: string }
outputs:
  - docs/shot-brief-{{seq}}-{{shot}}.md
---

# Shot Brief — {{seq}}-{{shot}} ({{cut}})

- Intent: {{intent}}
- AOV Set: {{aov_set}}
- Notes: {{notes}}
