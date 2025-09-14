---
template_id: pm-asset/roadmap
version: 1
purpose: 路线图/里程碑
fields:
  product: { type: string }
  milestones: { type: table, columns: [name, date, owner, dependency, notes] }
outputs:
  - plans/roadmap-{{product}}.md
---

# Roadmap — {{product}}

{{milestones}}
