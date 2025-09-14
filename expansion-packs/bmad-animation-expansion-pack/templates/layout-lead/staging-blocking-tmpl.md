---
template_id: layout-lead/staging-blocking
version: 1
purpose: 走位/屏幕方向
fields:
  seq: { type: string }
  staging: { type: table, columns: [shot, path, screen_dir, eyeline, notes] }
outputs:
  - docs/staging-blocking-{{seq}}.md
---

# Staging — {{seq}}

{{staging}}
