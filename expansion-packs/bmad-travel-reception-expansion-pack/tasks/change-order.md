# task: change-order

version: 1.0
role: sales-account-manager
purpose: 管理客户变更并与运营/财务对齐差价与SLA。
inputs: [原订单, 变更请求, 成本核算]
outputs: [docs/sales/change-order-<booking_id>.md]
steps:

- templates/change-order-tmpl.yaml 渲染
- 与运营确认可行性与资源影响
- 与财务确认差价与开票
  acceptance:
- 影响分析与审批完备
- 与运营/财务对齐
