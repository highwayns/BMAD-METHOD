# task: invoice-issue

version: 1.0
role: finance-billing-specialist
purpose: 基于订单与履约凭证出账并生成发票。
inputs: [客户信息, 订单/团号/币种/税率, 明细与折扣/补偿, 汇率日期]
outputs: [docs/fin/invoice-<client>-<order>.md]
steps:

- 渲染 templates/invoice-issue-tmpl.yaml（逐节提问）
- 执行 invoice-audit-check 清单
  acceptance:
- 三单一致/口径统一
- 发票编号与回执在案
