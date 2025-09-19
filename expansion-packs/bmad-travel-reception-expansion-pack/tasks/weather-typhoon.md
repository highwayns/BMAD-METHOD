# task: weather-typhoon

version: 1.0
role: transport-logistics-coordinator
purpose: 面对台风/暴雪/暴雨等，制定改线/取消/改期方案。
inputs: [预警等级与区域, 停运/封闭清单, 客户沟通/补偿方案]
outputs: [docs/transport/weather-typhoon-plan.md]
steps:

- 渲染 templates/weather-typhoon-reroute-tmpl.yaml
- 执行 weather-typhoon-check 与 road-closure-diversion-check
  acceptance:
- 触发阈值明确
- 方案A/B/C就绪
