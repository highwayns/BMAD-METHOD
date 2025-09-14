---
template_id: fx-supervisor/destruction-plan
version: 1
purpose: 破坏分期计划
fields:
  asset: { type: string }
  stages: { type: table, columns: [phase, driver, cache, notes] }
outputs:
  - plans/destruction-{{asset}}.md
---

# Destruction Plan — {{asset}}

{{stages}}
