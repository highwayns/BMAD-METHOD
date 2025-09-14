---
template_id: anim-supervisor/lipsync-cuesheet
version: 1
purpose: 口型定位与情绪标注
fields:
  seq: { type: string }
  shot: { type: string }
  cues: { type: table, columns: [tc, phoneme, word, intent, notes] }
outputs:
  - facial/lipsync-{{seq}}-{{shot}}.md
---

# LipSync — {{seq}}-{{shot}}

| TC  | Phoneme | Word | Intent | Notes |
| --- | ------- | ---- | ------ | ----- |

{{cues}}
