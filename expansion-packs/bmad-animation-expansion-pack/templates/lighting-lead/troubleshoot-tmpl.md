---
template_id: lighting-lead/troubleshoot
version: 1
purpose: 渲染问题排查
fields:
  renderer: { type: string }
  issues: { type: table, columns: [symptom, cause, fix, verify] }
outputs:
  - docs/troubleshoot-{{renderer}}.md
---

# Troubleshoot — {{renderer}}

{{issues}}
