---
template_id: compositing-lead/retime-integration
version: 1
purpose: 重定时/运动模糊一致
fields:
  seq: { type: string }
  steps: { type: table, columns: [shot, method, motion_vectors, mb_rebuild, notes] }
outputs:
  - docs/retime-integration-{{seq}}.md
---

# Retime Integration — {{seq}}

{{steps}}
