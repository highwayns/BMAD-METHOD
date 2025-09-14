---
template_id: rigging-lead/facial-rig-plan
version: 1
purpose: 面部绑定与 FACS/ARKit 映射
fields:
  asset: { type: string }
  controls: { type: table, columns: [area, ctrl, min, max, default, notes] }
  mapping: { type: table, columns: [arkit, facs, ctrl, invert, scale] }
  poses: { type: table, columns: [pose, driver, target, notes] }
outputs:
  - facial/facial-rig-plan-{{asset}}.md
---

# Facial Rig Plan — {{asset}}

## Controls

{{controls}}

## Mapping

{{mapping}}

## Poses

{{poses}}
