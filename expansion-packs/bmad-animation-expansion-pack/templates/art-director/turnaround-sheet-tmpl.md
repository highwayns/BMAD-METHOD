---
template_id: art-director/turnaround-sheet
version: 1
purpose: 三视图/转面页
fields:
  name: { type: string }
  views: { type: list, items: string }
  notes: { type: text }
outputs:
  - sheets/{{name}}-turnaround.md
---

# Turnaround — {{name}}

- Views: {{views}}
- Notes: {{notes}}
