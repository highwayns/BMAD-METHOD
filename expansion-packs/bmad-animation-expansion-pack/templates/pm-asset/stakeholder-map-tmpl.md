---
template_id: pm-asset/stakeholder-map
version: 1
purpose: 干系人地图
fields:
  product: { type: string }
  contacts: { type: table, columns: [team, role, person, email, timezone] }
outputs:
  - docs/stakeholders-{{product}}.md
---

# Stakeholders — {{product}}

{{contacts}}
