# task: ap-batch-payment

version: 1.0
role: finance-billing-specialist
purpose: 组织应付批次，兼顾现金与早付折扣。
inputs: [供应商/币种/金额/付款日, 优先级/早付折扣]
outputs: [docs/fin/ap-batch-<period>.md]
steps:

- 渲染 templates/ap-batch-payment-tmpl.yaml
- 执行 ap-payment-check 清单
  acceptance:
- 合规可付
- 现金节奏合理
