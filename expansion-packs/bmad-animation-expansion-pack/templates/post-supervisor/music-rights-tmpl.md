---
template_id: post-supervisor/music-rights
version: 1
purpose: 音乐版权/曲目单
fields:
  show: { type: string }
  cues: { type: table, columns: [cue, title, composer, publisher, duration, usage, clearance] }
outputs:
  - docs/music-rights-{{show}}.md
---

# Music Rights — {{show}}

{{cues}}
