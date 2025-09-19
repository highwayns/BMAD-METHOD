# task: generate-dispatch

version: 1.0
role: transport-logistics-coordinator
purpose: 生成当日日派单与联络单并分发现场。
inputs: [当日订单, 航班/列车, 司机/车辆/牌照]
outputs: [docs/transport/daily-dispatch-YYYYMMDD.md]
steps:

- 渲染 templates/daily-dispatch-tmpl.yaml
- 校对司机/车辆与集合点
- 分发并归档
  acceptance:
- 任务逐条可执行
- 值班与联络清晰
