---
template_id: lookdev-shading-lead/pbr-map-authoring
version: 1
purpose: PBR 贴图出图规范
fields:
  asset: { type: string }
  maps: { type: table, columns: [name, bitdepth, colorspace, packing, udim, notes] }
  naming: { type: table, columns: [token, rule, example] }
outputs:
  - specs/pbr-map-authoring-{{asset}}.md
---

# PBR Map Authoring — {{asset}}

{{maps}}

## Naming

{{naming}}
