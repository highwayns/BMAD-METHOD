# task: daily-dispatch

version: 1.0
role: operations-director
purpose: 生成当日日派单与联络单。
inputs:

- 当日订单与资源池
- 航班/车次/集合点信息
  outputs:
- docs/ops/daily-dispatch-YYYYMMDD.md
  steps:
- 启动 create-doc 使用 templates/daily-dispatch-tmpl.yaml
- 校对司机/导游/车辆与票务码
- 分发至现场群与归档
  acceptance:
- 任务逐条完整且可执行
- 值班/联络方式清晰
- 版本与发布时间标注
