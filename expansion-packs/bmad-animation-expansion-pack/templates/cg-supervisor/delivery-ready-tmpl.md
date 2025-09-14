---
template_id: cg-supervisor/delivery-ready
version: 1
purpose: 交付就绪评估
fields:
  cut: { type: string }
  checks: { type: table, columns: [item, status, evidence, owner] }
  summary: { type: text }
outputs:
  - delivery/delivery-ready-{{cut}}.md
---

# Delivery Ready — {{cut}}

{{checks}}

## Summary

{{summary}}
