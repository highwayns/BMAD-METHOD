---
template_id: rigging-lead/fkik-design
version: 1
purpose: FK/IK/Twist 设计
fields:
  asset: { type: string }
  limbs: { type: table, columns: [limb, fk_chain, ik_solver, pole, twist_joints, stretch, notes] }
outputs:
  - docs/fkik-design-{{asset}}.md
---

# FK/IK Design — {{asset}}

{{limbs}}
