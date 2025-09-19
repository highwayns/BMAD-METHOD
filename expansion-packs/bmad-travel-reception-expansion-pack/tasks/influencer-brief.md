# task: influencer-brief

version: 1.0
role: content-branding
purpose: KOL 合作Brief与交付/授权。
outputs: [docs/campaign/influencer-brief.md]
steps:

- 渲染 templates/influencer-brief-tmpl.yaml
  acceptance:
- 交付可验收
