# task: booking-amend-cancel

version: 1.0
role: hotel-contracting-manager
purpose: 管理变更/取消并同步财务影响与发票调整。
inputs: [订单/酒店/日期, 变更内容/原因, 费用差额/罚金]
outputs: [docs/hotel/booking-amend-cancel-<booking_id>.md]
steps:

- 渲染 templates/booking-amend-cancel-tmpl.yaml
- 同步财务与客户/运营
  acceptance:
- 影响明确/审批留痕
- 客户与酒店确认在案
