# task: tone-style-guide

version: 1.0
role: content-branding
purpose: 统一中英日语体/句式与示例。
outputs: [docs/brand/tone-style-guide.md]
steps:

- 渲染 templates/tone-style-guide-tmpl.yaml
- 执行 a11y-i18n-check
  acceptance:
- 敬语与译法一致
