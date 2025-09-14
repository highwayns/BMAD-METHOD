---
template_id: compositing-lead/cryptoid-policy
version: 1
purpose: CryptoID 策略（类别/稳定性/颜色空间）
fields:
  show: { type: string }
  classes: { type: table, columns: [class, enabled, notes] }
  stability: { type: table, columns: [rule, detail] }
outputs:
  - specs/cryptoid-policy-{{show}}.md
---

# CryptoID Policy — {{show}}

{{classes}}
{{stability}}
