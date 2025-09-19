# task: vendor-onboarding

version: 1.0
role: vendor-procurement-manager
purpose: 完成准入合规与数据契约，入库可下单。
inputs: [企业/资质/保险, 税票/收款, 政策承诺/数据字段]
outputs: [docs/vendor/onboarding-<vendor>.md]
steps:

- 渲染 templates/vendor-onboarding-tmpl.yaml
- 执行 anti-bribery-check / insurance-compliance-check / tax-invoice-check / data-contract-check
  acceptance:
- 证照/保险/税票齐全
- 数据契约通过
