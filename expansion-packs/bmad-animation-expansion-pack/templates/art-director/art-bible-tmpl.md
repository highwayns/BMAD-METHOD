---
template_id: art-director/art-bible
version: 1
purpose: 艺术圣经（愿景/视觉语言/资产规范/样张）
fields:
  version: { type: string, required: true }
  pillars:
    { type: list, items: string, example: ['形状语言', '色彩基线', '材质/光影', '构图与层次'] }
  references: { type: list, items: url }
  tokens_ref: { type: path, desc: '设计令牌：颜色/材质/线宽/字形' }
  keyframes_ref: { type: path }
outputs:
  - docs/art-bible-{{version}}.md
---

# Art Bible v{{version}}

## Pillars

- {{pillars}}

## References

- {{references}}

## Tokens

- {{tokens_ref}}

## Keyframes

- {{keyframes_ref}}
