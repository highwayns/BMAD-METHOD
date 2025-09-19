# task: rfp-rfq

version: 1.0
role: vendor-procurement-manager
purpose: 组织RFP/RFQ并形成可比价与条款建议。
inputs: [需求范围, 价格结构, SLA/KPI, 合规与隐私]
outputs: [docs/vendor/rfp-<project>.md]
steps:

- 渲染 templates/rfp-rfq-pack-tmpl.yaml
- 比价与条款评估，形成推荐
  acceptance:
- 可比性强/条款清晰
- 决策建议可执行
