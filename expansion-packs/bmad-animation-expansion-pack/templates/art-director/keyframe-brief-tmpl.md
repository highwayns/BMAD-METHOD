---
template_id: art-director/keyframe-brief
version: 1
purpose: 关键帧/Lighting Keys 指南
fields:
  seq: { type: string }
  targets: { type: table, columns: [shot, intent, palette_id, notes] }
  references: { type: list, items: url }
outputs:
  - lookdev/keyframes-{{seq}}.md
---

# Keyframes — {{seq}}

- Targets:
  {{targets}}
- References:
  {{references}}
