# task: cost-variance

version: 1.0
role: finance-billing-specialist
purpose: 识别成本差异与责任，并推动纠偏。
inputs: [类别/金额/原因/措施]
outputs: [reports/cost-variance-<period>.md]
steps:

- 渲染 templates/cost-variance-tmpl.yaml
- 与供应/运营联动CAPA
  acceptance:
- 纠偏责任到人
- 截止可追踪
