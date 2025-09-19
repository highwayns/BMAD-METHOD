# task: refund-comp

version: 1.0
role: sales-account-manager
purpose: 规范退款/补偿流程并与财务/运营一致。
inputs: [订单/触发原因/证据, 金额测算]
outputs: [reports/refund-comp-<booking_id>.md]
steps:

- templates/refund-compensation-tmpl.yaml 渲染
- 审批与支付/回执追踪
  acceptance:
- 金额与证据匹配
- 审批留痕
