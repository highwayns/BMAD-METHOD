# task: itinerary-proof

version: 1.0
role: visa-insurance-specialist
purpose: 生成签证用行程/住宿/交通证明材料包。
inputs: [日程/城市/交通, 酒店信息, 机票/车船预订单]
outputs: [docs/visa/itinerary-proof-<traveler>.md]
steps:

- 渲染 templates/itinerary-proof-tmpl.yaml
- 执行 itinerary-proof-check 清单
  acceptance:
- 逻辑自洽/口径统一
- 联系方式清晰
