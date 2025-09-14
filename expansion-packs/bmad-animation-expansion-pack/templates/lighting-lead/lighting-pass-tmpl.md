---
template_id: lighting-lead/lighting-pass
version: 1
purpose: 灯光分层/渲染通道策略
fields:
  seq: { type: string }
  passes: { type: table, columns: [name, contents, notes] }
outputs:
  - plans/lighting-pass-{{seq}}.md
---

# Lighting Pass — {{seq}}

{{passes}}
