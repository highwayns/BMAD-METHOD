---
template_id: rigging-lead/corrective-shapes
version: 1
purpose: 纠正形态/驱动网络
fields:
  asset: { type: string }
  correctives: { type: table, columns: [pose, region, driver, method, notes] }
  bake_targets: { type: list, items: string }
outputs:
  - specs/correctives-{{asset}}.yaml
---

# Correctives — {{asset}}

{{correctives}}

- Bake Targets: {{bake_targets}}
