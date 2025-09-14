---
template_id: pm-asset/rfc
version: 1
purpose: 变更提案
fields:
  id: { type: string }
  context: { type: text }
  change: { type: text }
  compatibility: { type: list, items: string }
  impact: { type: text }
outputs:
  - docs/rfc-{{id}}.md
---

# RFC {{id}}

- Context: {{context}}
- Change: {{change}}
- Compatibility: {{compatibility}}
- Impact: {{impact}}
