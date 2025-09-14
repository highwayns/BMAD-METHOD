---
template_id: art-director/moodboard
version: 1
purpose: 参考情绪板（可溯源链接）
fields:
  topic: { type: string }
  refs: { type: table, columns: [label, url, notes] }
outputs:
  - refs/moodboard-{{topic}}.md
---

# Moodboard — {{topic}}

{{refs}}
