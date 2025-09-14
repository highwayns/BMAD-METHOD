---
template_id: director/music-spotting
version: 1
purpose: 音乐定位会（入点/出点/动机/参考）
fields:
  cut: { type: string }
  cues: { type: table, columns: [tc_in, tc_out, intent, ref, notes] }
outputs:
  - music/spotting-{{cut}}.md
---

# Music Spotting — {{cut}}

| In  | Out | Intent | Ref | Notes |
| --- | --- | ------ | --- | ----- |

{{cues}}
