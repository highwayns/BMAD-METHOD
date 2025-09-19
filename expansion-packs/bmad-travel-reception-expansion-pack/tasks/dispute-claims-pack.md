# task: dispute-claims-pack

version: 1.0
role: legal-compliance
purpose: 形成纠纷/理赔/诉讼资料包与路径建议。
inputs: [事实/证据/时间线/责任, 路径与成本]
outputs: [docs/legal/dispute-<case>.md]
steps:

- 渲染 templates/dispute-claims-pack-tmpl.yaml
- 执行 dispute-litigation-check 清单
  acceptance:
- 路径清楚
- 保密与口径一致
