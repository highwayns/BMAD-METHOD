---
template_id: pm-asset/prd
version: 1
purpose: 产品需求文档
fields:
  product: { type: string }
  goals: { type: list, items: string }
  personas: { type: table, columns: [role, goals, pains] }
  stories: { type: table, columns: [as_a, i_want, so_that, acceptance] }
  non_functional: { type: table, columns: [type, target] }
  metrics: { type: table, columns: [metric, target, method] }
outputs:
  - docs/prd-{{product}}.md
---

# PRD — {{product}}

- Goals: {{goals}}
  {{personas}}
  {{stories}}
  {{non_functional}}
  {{metrics}}
