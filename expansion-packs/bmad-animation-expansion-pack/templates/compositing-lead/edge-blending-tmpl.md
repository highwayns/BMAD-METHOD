---
template_id: compositing-lead/edge-blending
version: 1
purpose: 边缘/溢色/半透明处理
fields:
  seq: { type: string }
  ops: { type: table, columns: [shot, issue, op, params, verify] }
outputs:
  - docs/edge-blending-{{seq}}.md
---

# Edge Blending — {{seq}}

{{ops}}
