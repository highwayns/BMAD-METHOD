---
template_id: anim-supervisor/shot-assign
version: 1
purpose: 镜头分配与复杂度评估
fields:
  seq: { type: string }
  shots: { type: table, columns: [shot, chars, complexity, owner, est_days, notes] }
outputs:
  - assignments/shot-assign-{{seq}}.md
---

# Shot Assign — {{seq}}

| Shot | Chars | Complexity | Owner | Est(D) | Notes |
| ---- | ----- | ---------- | ----- | ------ | ----- |

{{shots}}
