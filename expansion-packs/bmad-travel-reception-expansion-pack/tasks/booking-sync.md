# task: booking-sync

version: 1.0
role: tech-systems-dms-crm
purpose: 订单/行程/发票与CRM同步（单向或双向）。
inputs: [映射/ID/幂等/错误处理]
outputs: [docs/sys/booking-sync.md]
steps:

- 渲染 templates/api-integration-tmpl.yaml
- 执行 api-go-live-check 与 data-contract-check
  acceptance:
- 无重复/无漏单
- 对账一致
