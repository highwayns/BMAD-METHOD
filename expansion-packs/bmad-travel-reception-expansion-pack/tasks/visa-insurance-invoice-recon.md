# task: visa-insurance-invoice-recon

version: 1.0
role: visa-insurance-specialist
purpose: 完成签证/保险费用对账与差异闭环。
inputs: [账期/供应商, 单据与应计]
outputs: [reports/visa-insurance-recon-<period>.md]
steps:

- 渲染 templates/visa-insurance-invoice-recon-tmpl.yaml
- 列出差异/责任人/期限
  acceptance:
- 差异闭环≥95%
- 回款计划明确
