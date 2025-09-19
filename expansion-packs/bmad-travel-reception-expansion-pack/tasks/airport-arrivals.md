# task: airport-arrivals

version: 1.0
role: transport-logistics-coordinator
purpose: 汇总机场到达花名册并布置接机与车辆资源。
inputs: [航班清单, 接机人与车辆, 备选方案]
outputs: [docs/transport/airport-arrivals-roster.md]
steps:

- 渲染 templates/airport-arrivals-roster-tmpl.yaml
- 校对延误与车辆位
  acceptance:
- 航班/接机/车辆位一一对应
- 延误备选清晰
