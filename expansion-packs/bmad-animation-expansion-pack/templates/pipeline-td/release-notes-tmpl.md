---
template_id: pipeline-td/release-notes
version: 1
purpose: 版本发布说明
fields:
  version: { type: string }
  changes: { type: list, items: string }
  breaking: { type: list, items: string }
  rollback: { type: list, items: string }
outputs:
  - release/release-notes.md
---

# Release {{version}}

- Changes: {{changes}}
- Breaking: {{breaking}}
- Rollback: {{rollback}}
