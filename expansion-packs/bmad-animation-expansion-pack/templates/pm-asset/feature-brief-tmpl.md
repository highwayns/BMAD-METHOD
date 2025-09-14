---
template_id: pm-asset/feature-brief
version: 1
purpose: 特性简报/背景/方案/权衡
fields:
  name: { type: string }
  problem: { type: text }
  proposal: { type: text }
  alternatives: { type: list, items: string }
  acceptance: { type: list, items: string }
outputs:
  - specs/feature-{{name}}.md
---

# Feature Brief — {{name}}

- Problem: {{problem}}
- Proposal: {{proposal}}
- Alternatives: {{alternatives}}
- Acceptance: {{acceptance}}
