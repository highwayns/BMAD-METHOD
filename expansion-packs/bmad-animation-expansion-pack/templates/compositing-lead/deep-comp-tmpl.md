---
template_id: compositing-lead/deep-comp
version: 1
purpose: Deep 合成/体积/遮挡
fields:
  seq: { type: string }
  passes: { type: table, columns: [shot, deep_input, z_tolerance, merge_ops, notes] }
outputs:
  - docs/deep-comp-{{seq}}.md
---

# Deep Comp — {{seq}}

{{passes}}
