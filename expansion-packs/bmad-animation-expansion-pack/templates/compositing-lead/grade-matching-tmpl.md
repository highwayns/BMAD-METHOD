---
template_id: compositing-lead/grade-matching
version: 1
purpose: 颜色匹配/参考/校正
fields:
  seq: { type: string }
  anchors: { type: table, columns: [shot, gray_nits, chrome_nits, wb_k, note] }
  ops: { type: table, columns: [order, op, params, note] }
outputs:
  - docs/grade-matching-{{seq}}.md
---

# Grade Matching — {{seq}}

{{anchors}}
{{ops}}
