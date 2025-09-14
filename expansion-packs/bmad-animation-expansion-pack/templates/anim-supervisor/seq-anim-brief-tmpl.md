---
template_id: anim-supervisor/seq-anim-brief
version: 1
purpose: 序列动画启动简报
fields:
  seq: { type: string }
  beats: { type: list, items: string }
  cast: { type: list, items: string }
  tone: { type: list, items: string }
  interfaces: { type: table, columns: [dept, input, output, owner] }
outputs:
  - docs/seq-anim-brief-{{seq}}.md
---

# Seq Animation Brief — {{seq}}

- Beats: {{beats}}
- Cast: {{cast}}
- Tone: {{tone}}

## Interfaces

{{interfaces}}
