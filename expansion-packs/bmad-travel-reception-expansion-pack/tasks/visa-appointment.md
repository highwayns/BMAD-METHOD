# task: visa-appointment

version: 1.0
role: visa-insurance-specialist
purpose: 完成受理中心预约与递交跟踪，固化证据链。
inputs: [VAC/时间段, 指纹/面试/邮寄, 回执/快递编号]
outputs: [docs/visa/appointment-<traveler>.md]
steps:

- 渲染 templates/visa-appointment-tmpl.yaml
- 执行 courier-tracking-check 清单
  acceptance:
- 预约成功与递交证据齐全
- 时限提醒就绪
