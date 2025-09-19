# task: clause-library

version: 1.0
role: legal-compliance
purpose: 维护标准条款模块，支撑快速签约。
inputs: [模块/版本/适用/备注]
outputs: [docs/legal/standard-clauses.md]
steps:

- 渲染 templates/standard-clauses-tmpl.yaml
- 与合同评审联动
  acceptance:
- 可复用/可检索
- 版本可追溯
