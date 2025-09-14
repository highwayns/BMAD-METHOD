---
template_id: lookdev-shading-lead/usdshade-authoring
version: 1
purpose: USDShade/MaterialX 编制与绑定
fields:
  asset: { type: string }
  materials: { type: table, columns: [path, subset, mx_path, usdshade_path, variant] }
  bindings: { type: table, columns: [geom, material, purpose] }
outputs:
  - usd/usdshade-{{asset}}.md
---

# USDShade Authoring — {{asset}}

## Materials

{{materials}}

## Bindings

{{bindings}}
