# task: content-brief

version: 1.0
role: content-branding
purpose: 单篇内容 Brief（含证据/法务/A11y）。
outputs: [docs/content/brief-<id>.md]
steps:

- 渲染 templates/content-brief-tmpl.yaml
- 执行 fact-accuracy-check 与 a11y-i18n-check
  acceptance:
- 证据链完整
