# task: driver-hours-compliance

version: 1.0
role: transport-logistics-coordinator
purpose: 规划司机班表，降低超时/疲劳驾驶风险。
inputs: [班表/休息/餐食, 连续驾驶与总时长]
outputs: [reports/driver-hours-compliance-YYYYMM.md]
steps:

- 渲染 templates/driver-hours-compliance-tmpl.yaml
- 执行 driver-hours-legal-check 清单
  acceptance:
- 工时与休息合规
- 证据留痕
