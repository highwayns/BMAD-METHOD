---
template_id: pm-asset/data-model
version: 1
purpose: 数据模型/命名/事件
fields:
  domain: { type: string }
  entities: { type: table, columns: [name, fields, keys] }
  events: { type: table, columns: [name, payload, source] }
outputs:
  - specs/data-model-{{domain}}.yaml
---

entities:
{{entities}}
events:
{{events}}
