---
template_id: cg-supervisor/seq-brief
version: 1
purpose: 序列启动简报
fields:
  seq: { type: string }
  goals: { type: list, items: string }
  milestones: { type: list, items: string }
  risks: { type: list, items: string }
  interfaces: { type: table, columns: [dept, input, output, owner] }
outputs:
  - docs/seq-brief-{{seq}}.md
---

# Sequence Brief — {{seq}}

- Goals: {{goals}}
- Milestones: {{milestones}}
- Risks: {{risks}}

## Interfaces

{{interfaces}}
