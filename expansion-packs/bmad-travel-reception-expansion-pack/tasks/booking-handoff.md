# task: booking-handoff

version: 1.0
role: sales-account-manager
purpose: 将已签订单与数据契约完整交接给运营，确保可执行。
inputs: [合同/订单资料, 旅客/行程/票务数据, 条款]
outputs: [docs/sales/booking-handoff-<booking_id>.md]
steps:

- templates/booking-handoff-tmpl.yaml 渲染
- 执行 booking-data-quality 清单
- 归档与回执
  acceptance:
- 数据完整与清单通过
- 运营已确认接收
