# task: press-kit

version: 1.0
role: content-branding
purpose: 媒体资料包（简介/亮点/图库）。
outputs: [docs/pr/press-kit.md]
steps:

- 渲染 templates/press-kit-tmpl.yaml
  acceptance:
- 授权明晰
