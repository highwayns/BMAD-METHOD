# task: production-workflow

version: 1.0
role: content-branding
purpose: 建立内容生产流水线与准入门槛。
outputs: [docs/content/workflow.md]
steps:

- 渲染 templates/production-workflow-tmpl.yaml
- 执行 legal-ip-privacy-check
  acceptance:
- 准入门槛达标
