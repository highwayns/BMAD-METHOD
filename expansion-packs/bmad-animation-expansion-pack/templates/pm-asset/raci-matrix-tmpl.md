---
template_id: pm-asset/raci-matrix
version: 1
purpose: RACI 矩阵
fields:
  context: { type: string }
  matrix: { type: table, columns: [activity, R, A, C, I] }
outputs:
  - docs/raci-{{context}}.md
---

# RACI — {{context}}

{{matrix}}
