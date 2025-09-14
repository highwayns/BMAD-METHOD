---
template_id: compositing-lead/render-pull
version: 1
purpose: 渲染拉取/版本对账
fields:
  seq: { type: string }
  pulls: { type: table, columns: [shot, version, source, checksum, result] }
outputs:
  - reports/render-pull-{{seq}}.md
---

# Render Pull — {{seq}}

{{pulls}}
