---
template_id: cg-supervisor/coverage-matrix
version: 1
purpose: 覆盖矩阵
fields:
  seq: { type: string }
  shots: { type: table, columns: [shot, layout, anim, fx, light, comp, risk] }
outputs:
  - dashboards/coverage-{{seq}}.md
---

# Coverage — {{seq}}

| Shot | Layout | Anim | FX  | Light | Comp | Risk |
| ---- | ------ | ---- | --- | ----- | ---- | ---- |

{{shots}}
