---
template_id: director/style-bible
version: 1
purpose: 风格手册（色彩/光线/构图/镜头语言/音乐）
fields:
  palette: { type: list, items: string }
  lighting: { type: list, items: string }
  composition: { type: list, items: string }
  camera: { type: list, items: string }
  music: { type: list, items: string }
outputs:
  - docs/style-bible-{{version}}.md
---

# Style Bible v{{version}}

## Palette

- {{palette}}

## Lighting

- {{lighting}}

## Composition

- {{composition}}

## Camera

- {{camera}}

## Music

- {{music}}
