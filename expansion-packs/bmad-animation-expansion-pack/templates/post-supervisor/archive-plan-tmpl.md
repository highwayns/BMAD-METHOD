---
template_id: post-supervisor/archive-plan
version: 1
purpose: 归档与安全
fields:
  show: { type: string }
  storage: { type: table, columns: [tier, location, retention, checksum, encryption] }
  access: { type: list, items: string }
  watermark: { type: list, items: string }
outputs:
  - docs/archive-plan-{{show}}.md
---

# Archive Plan — {{show}}

{{storage}}

- Access: {{access}}
- Watermark: {{watermark}}
