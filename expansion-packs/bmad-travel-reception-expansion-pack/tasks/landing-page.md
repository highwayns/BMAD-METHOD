# task: landing-page

version: 1.0
role: content-branding
purpose: 落地页装配（品牌/证据/CTA）。
outputs: [docs/lp/landing-page.md]
steps:

- 渲染 templates/landing-page-tmpl.yaml
- 执行 brand-consistency-check 与 a11y-i18n-check
  acceptance:
- 品牌与A11y达标
