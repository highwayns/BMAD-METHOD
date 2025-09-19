# task: localization-kit

version: 1.0
role: content-branding
purpose: 本地化工具包与术语库。
outputs: [docs/l10n/localization-kit.md]
steps:

- 渲染 templates/localization-kit-tmpl.yaml
- 执行 a11y-i18n-check
  acceptance:
- 术语一致
