---
template_id: pm-asset/training-plan
version: 1
purpose: 培训与推广计划
fields:
  product: { type: string }
  modules: { type: table, columns: [module, goal, materials, owner] }
  rollouts: { type: table, columns: [batch, audience, date] }
outputs:
  - docs/training-{{product}}.md
---

# Training Plan — {{product}}

{{modules}}
{{rollouts}}
