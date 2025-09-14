---
template_id: lighting-lead/light-rig-library
version: 1
purpose: 灯光库与模板
fields:
  show: { type: string }
  rigs: { type: table, columns: [name, type, power, color_temp_k, ies, gobo, purpose] }
  policies: { type: list, items: string }
outputs:
  - library/light-rigs-{{show}}.yaml
---

# Light Rig Library — {{show}}

{{rigs}}

- Policies: {{policies}}
