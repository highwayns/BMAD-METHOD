---
template_id: art-director/texture-look-bible
version: 1
purpose: 材质/纹理 Look Bible
fields:
  categories: { type: list, items: string }
  pbr_params: { type: table, columns: [material, basecolor, roughness, metalness, specular, notes] }
  tex_naming: { type: list, items: string }
outputs:
  - lookdev/texture-look-bible-{{version}}.md
---

# Texture / Look Bible v{{version}}

- Categories: {{categories}}
- PBR Params:
  {{pbr_params}}
- Texture Naming:
  {{tex_naming}}
