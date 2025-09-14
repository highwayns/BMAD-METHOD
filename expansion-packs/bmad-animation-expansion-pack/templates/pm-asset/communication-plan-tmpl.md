---
template_id: pm-asset/communication-plan
version: 1
purpose: 沟通计划
fields:
  context: { type: string }
  plan: { type: table, columns: [channel, audience, cadence, owner, artifact] }
outputs:
  - docs/comm-{{context}}.md
---

# Communication Plan — {{context}}

{{plan}}
