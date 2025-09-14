---
template_id: art-director/typography-title
version: 1
purpose: 片头/字形/品牌视觉
fields:
  version: { type: string }
  logo_usage: { type: list, items: string }
  title_styles: { type: list, items: string }
  lower_thirds: { type: list, items: string }
  caption_rules: { type: list, items: string }
outputs:
  - brand/typography-title-{{version}}.md
---

# Typography & Title v{{version}}

- Logo: {{logo_usage}}
- Titles: {{title_styles}}
- Lower Thirds: {{lower_thirds}}
- Captions: {{caption_rules}}
