---
template_id: layout-lead/shot-plan
version: 1
purpose: 镜头计划（blocking/coverage/优先级）
fields:
  seq: { type: string }
  shots: { type: table, columns: [shot, objective, move, lens, priority, owner, due] }
outputs:
  - plans/shot-plan-{{seq}}.md
---

# Shot Plan — {{seq}}

{{shots}}
