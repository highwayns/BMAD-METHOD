# task: ar-aging

version: 1.0
role: finance-billing-specialist
purpose: 生成应收账龄表并设置催收节奏与升级。
inputs: [账龄区间, 催收与升级]
outputs: [reports/ar-aging-<period>.md]
steps:

- 渲染 templates/ar-aging-tmpl.yaml
- 执行 ar-collection-check 清单
  acceptance:
- 催收节奏明确
- 升级路径可达
