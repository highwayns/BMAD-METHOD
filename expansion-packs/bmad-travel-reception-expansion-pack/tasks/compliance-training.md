# task: compliance-training

version: 1.0
role: legal-compliance
purpose: 设计合规培训计划与记录通过率。
inputs: [主题/对象/频次/通过率]
outputs: [reports/legal/training-<period>.md]
steps:

- 渲染 templates/compliance-training-plan-tmpl.yaml
- 执行 training-compliance-check 清单
  acceptance:
- 覆盖率与通过率达标
- 补课闭环
