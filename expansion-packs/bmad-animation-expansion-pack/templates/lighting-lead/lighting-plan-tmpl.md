---
template_id: lighting-lead/lighting-plan
version: 1
purpose: 镜头灯光计划
fields:
  seq: { type: string }
  shots: { type: table, columns: [shot, objective, rig, owner, priority, due] }
outputs:
  - plans/lighting-plan-{{seq}}.md
---

# Lighting Plan — {{seq}}

{{shots}}
