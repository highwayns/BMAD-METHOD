---
template_id: rigging-lead/skinning-plan
version: 1
purpose: Skin 权重策略
fields:
  asset: { type: string }
  method: { type: string, enum: [LBS, DQS, Hybrid] }
  maps: { type: table, columns: [region, method, weights_hint, notes] }
  test_poses: { type: list, items: string }
outputs:
  - plans/skinning-plan-{{asset}}.md
---

# Skinning Plan — {{asset}}

- Method: {{method}}

## Maps

{{maps}}

- Test Poses: {{test_poses}}
