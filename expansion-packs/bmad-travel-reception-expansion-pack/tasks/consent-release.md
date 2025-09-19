# task: consent-release

version: 1.0
role: content-branding
purpose: 被摄人同意与授权文本。
outputs: [docs/legal/consent-release.md]
steps:

- 渲染 templates/consent-release-tmpl.yaml
- 执行 legal-ip-privacy-check
  acceptance:
- 同意可追溯
