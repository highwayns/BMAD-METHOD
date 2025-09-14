---
template_id: post-supervisor/subtitles-plan
version: 1
purpose: 字幕/本地化计划
fields:
  locale: { type: string }
  style: { type: list, items: string }
  assets: { type: table, columns: [type, path, format, checksum] }
outputs:
  - plans/subtitles-{{locale}}.md
---

# Subtitles Plan — {{locale}}

- Style: {{style}}
  {{assets}}
