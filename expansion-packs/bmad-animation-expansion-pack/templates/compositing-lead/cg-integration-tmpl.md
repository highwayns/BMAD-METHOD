---
template_id: compositing-lead/cg-integration
version: 1
purpose: CG 与实拍对账
fields:
  seq: { type: string }
  items: { type: table, columns: [shot, shadow, contact, reflection, occlusion, notes] }
outputs:
  - docs/cg-integration-{{seq}}.md
---

# CG Integration — {{seq}}

{{items}}
