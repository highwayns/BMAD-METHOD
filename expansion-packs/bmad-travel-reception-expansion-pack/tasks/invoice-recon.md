# task: invoice-recon

version: 1.0
role: vendor-procurement-manager
purpose: 发票稽核与对账，关闭差异并沉淀规则。
inputs: [账期/供应商/金额, 差异明细]
outputs: [reports/invoice-recon-<period>.md]
steps:

- 渲染 templates/invoice-recon-tmpl.yaml
- 执行 invoice-audit-check
  acceptance:
- 差异闭环≥95%
- 规则更新
