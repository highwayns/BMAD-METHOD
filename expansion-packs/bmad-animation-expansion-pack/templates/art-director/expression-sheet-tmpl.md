---
template_id: art-director/expression-sheet
version: 1
purpose: 表情设定页
fields:
  name: { type: string }
  emotions: { type: list, items: string }
  notes: { type: text }
outputs:
  - sheets/{{name}}-expressions.md
---

# Expression Sheet — {{name}}

- Emotions: {{emotions}}
- Notes: {{notes}}
