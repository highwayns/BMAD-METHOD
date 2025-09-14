---
template_id: art-director/style-guide
version: 1
purpose: 风格手册（配色/线条/笔触/材质/噪点/字形/UI）
fields:
  version: { type: string }
  palette_id: { type: string }
  line_style: { type: string }
  brush_style: { type: string }
  texture_rules: { type: list, items: string }
  typography: { type: list, items: string }
  ui_elements: { type: list, items: string }
outputs:
  - docs/style-guide-{{version}}.md
---

# Style Guide v{{version}}

- Palette: {{palette_id}}
- Line: {{line_style}} / Brush: {{brush_style}}
- Texture Rules: {{texture_rules}}
- Typography: {{typography}}
- UI Elements: {{ui_elements}}
