---
template_id: pm-asset/release-notes
version: 1
purpose: 发布说明与回退
fields:
  version: { type: string }
  changes: { type: table, columns: [type, desc, issue] }
  rollback: { type: list, items: string }
  known_issues: { type: list, items: string }
outputs:
  - release/release-{{version}}.md
---

# Release Notes — {{version}}

{{changes}}

- Rollback: {{rollback}}
- Known Issues: {{known_issues}}
