# task: assignment

version: 1.0
role: guide-leader-manager
purpose: 根据多维规则完成导游匹配与派单。
inputs: [匹配规则, 订单任务, 备选人选]
outputs: [docs/guide/assignment-YYYYMMDD.md]
steps:

- 渲染 templates/assignment-matching-tmpl.yaml
- 通知并收集接单回执/定位签到
  acceptance:
- 匹配规则可解释
- 接单回执齐备
