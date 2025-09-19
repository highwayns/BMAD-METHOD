# task: tax-vat-return

version: 1.0
role: finance-billing-specialist
purpose: 形成税务申报草稿与计算依据。
inputs: [税种/期间/税率, 销项/进项/应纳]
outputs: [reports/tax-vat-<period>.md]
steps:

- 渲染 templates/tax-vat-return-tmpl.yaml
- 执行 tax-compliance-check 清单
  acceptance:
- 计算可追溯
- 票据齐全
