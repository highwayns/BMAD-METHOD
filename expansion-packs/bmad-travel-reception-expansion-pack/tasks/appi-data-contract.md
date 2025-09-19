# task: appi-data-contract

version: 1.0
role: customer-service-care-lead
purpose: 明确APPI数据契约（最小必要/共享/存留/脱敏）。
inputs: [字段/用途/存留时限, 第三方共享/脱敏]
outputs: [docs/care/appi-data-contract.md]
steps:

- 渲染 templates/appi-data-contract-tmpl.yaml
- 执行 privacy-appi-check 清单
  acceptance:
- 合规明确
- 审批留痕
