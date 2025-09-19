# task: vendor-statement

version: 1.0
role: finance-billing-specialist
purpose: 输出供应商对账单与差异清单。
inputs: [条目, 状态/备注]
outputs: [reports/vendor-statement-<vendor>-<period>.md]
steps:

- 渲染 templates/vendor-statement-tmpl.yaml
- 执行 reconciliation-check 清单
  acceptance:
- 条目完整
- 差异明确
