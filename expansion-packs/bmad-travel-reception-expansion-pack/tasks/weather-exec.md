# task: weather-exec

version: 1.0
role: onsite-ops-lead
purpose: 根据预警执行改线/转场/取消与沟通补偿。
inputs: [预警等级/区域, 停运/封闭/改线, 通知/补偿]
outputs: [docs/onsite/weather-exec-YYYYMMDD.md]
steps:

- 渲染 templates/weather-action-exec-tmpl.yaml
- 执行 weather-closure-check 清单
  acceptance:
- 触发/执行/沟通闭环
- 证据链完整
