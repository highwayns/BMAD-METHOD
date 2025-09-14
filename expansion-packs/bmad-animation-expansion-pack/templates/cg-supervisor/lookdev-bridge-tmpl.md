---
template_id: cg-supervisor/lookdev-bridge
version: 1
purpose: LookDev→Lighting 桥接
fields:
  seq: { type: string }
  assets: { type: table, columns: [asset, mat_version, palette_id, notes] }
  aov_contract: { type: list, items: string }
  color_pipeline: { type: string }
outputs:
  - bridges/lookdev-to-light-{{seq}}.md
---

# LookDev→Lighting — {{seq}}

- AOV Contract: {{aov_contract}}
- Color Pipeline: {{color_pipeline}}

## Assets

{{assets}}
