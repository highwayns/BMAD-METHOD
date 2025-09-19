# task: visa-tracking

version: 1.0
role: visa-insurance-specialist
purpose: 跟踪出签节点并记录证据与承诺时效。
inputs: [节点/时间/渠道, 备注/证据]
outputs: [docs/visa/tracking-<traveler>.md]
steps:

- 渲染 templates/visa-tracking-log-tmpl.yaml
- 提醒与升级阈值设定
  acceptance:
- 节点完整
- 延迟自动提醒
