---
template_id: lighting-lead/integration-plan
version: 1
purpose: 实拍对账/合成桥接
fields:
  seq: { type: string }
  plates: { type: table, columns: [shot, gray, chrome, color_chart, wb_k, exposure_note] }
  tricks: { type: list, items: string }
outputs:
  - docs/integration-plan-{{seq}}.md
---

# Integration Plan — {{seq}}

{{plates}}

- Tricks: {{tricks}}
