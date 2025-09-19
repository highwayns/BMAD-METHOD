# task: booking-request

version: 1.0
role: hotel-contracting-manager
purpose: 按合同价表向酒店发起预订，确保字段口径与政策一致。
inputs: [订单摘要, 房型/餐食/人数, 付款/担保, 特殊需求]
outputs: [docs/hotel/booking-request-<booking_id>.md]
steps:

- 渲染 templates/booking-request-tmpl.yaml
- 与预抵确认清单联动
  acceptance:
- 字段完整/政策一致
- 酒店确认回执归档
