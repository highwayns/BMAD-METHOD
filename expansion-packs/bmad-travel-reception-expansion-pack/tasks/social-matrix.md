# task: social-matrix

version: 1.0
role: content-branding
purpose: 社媒矩阵与UTM规范。
outputs: [docs/campaign/social-matrix.md]
steps:

- 渲染 templates/social-matrix-tmpl.yaml
- 执行 social-safety-check
  acceptance:
- 追踪可用
