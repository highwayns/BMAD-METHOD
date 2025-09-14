---
template_id: compositing-lead/matte-id-policy
version: 1
purpose: 抠像/ID/遮罩政策
fields:
  show: { type: string }
  policies: { type: table, columns: [topic, rule, owner] }
outputs:
  - specs/matte-id-policy-{{show}}.md
---

# Matte/ID Policy — {{show}}

{{policies}}
