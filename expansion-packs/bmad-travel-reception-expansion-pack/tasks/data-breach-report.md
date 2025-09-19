# task: data-breach-report

version: 1.0
role: risk-safety-manager
purpose: 处理数据与隐私事件并完成通知与补救。
inputs: [影响评估, 通知与报备, 客户沟通与补救]
outputs: [reports/data-breach-<id>.md]
steps:

- 渲染 templates/data-breach-report-tmpl.yaml
- 执行 data-breach-check 清单
  acceptance:
- 止损有效
- 通知合规
