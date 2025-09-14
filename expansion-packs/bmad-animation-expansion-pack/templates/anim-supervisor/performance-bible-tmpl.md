---
template_id: anim-supervisor/performance-bible
version: 1
purpose: 表演圣经（母题/节拍/姿态/节律）
fields:
  version: { type: string }
  motifs: { type: list, items: string }
  pose_keys: { type: list, items: string }
  rhythm_rules: { type: list, items: string }
  examples: { type: list, items: string }
outputs:
  - docs/performance-bible-{{version}}.md
---

# Performance Bible v{{version}}

- Motifs: {{motifs}}
- Poses: {{pose_keys}}
- Rhythm Rules: {{rhythm_rules}}
- Examples: {{examples}}
