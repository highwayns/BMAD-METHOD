---
template_id: pm-asset/asset-lifecycle-spec
version: 1
purpose: 资产生命周期/状态机
fields:
  domain: { type: string }
  states: { type: table, columns: [state, entry, exit, guard] }
  transitions: { type: table, columns: [from, to, event, guard] }
outputs:
  - specs/asset-lifecycle-{{domain}}.yaml
---

states:
{{states}}
transitions:
{{transitions}}
