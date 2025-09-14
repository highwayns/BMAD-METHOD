---
template_id: lighting-lead/farm-plan
version: 1
purpose: 渲染农场预算/队列
fields:
  seq: { type: string }
  batches: { type: table, columns: [name, priority, max_concurrent, retry, notes] }
  costs: { type: table, columns: [hourly, estimate_h, budget_h] }
outputs:
  - bench/farm-plan-{{seq}}.md
---

# Farm Plan — {{seq}}

{{batches}}
{{costs}}
