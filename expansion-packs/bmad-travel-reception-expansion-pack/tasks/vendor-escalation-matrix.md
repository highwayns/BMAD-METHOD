# task: vendor-escalation-matrix

version: 1.0
role: vendor-procurement-manager
purpose: 建立争议与故障的升级矩阵与时限。
inputs: [事件/等级/联系人/电话, 时段/备援/时限]
outputs: [docs/vendor/escalation-matrix-<vendor>.md]
steps:

- 渲染 templates/vendor-escalation-matrix-tmpl.yaml
- 执行 dispute-escalation-check 清单
  acceptance:
- 线路可达
- 时限清楚
