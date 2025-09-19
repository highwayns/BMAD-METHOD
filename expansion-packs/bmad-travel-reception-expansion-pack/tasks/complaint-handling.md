# task: complaint-handling

version: 1.0
role: guide-leader-manager
purpose: 规范投诉受理、处置与复盘。
inputs: [投诉内容与证据, 分级与时限, 处理与补偿]
outputs: [reports/complaint-<id>.md]
steps:

- 渲染 templates/complaint-handling-tmpl.yaml
- 执行 complaint-intake-check 清单
  acceptance:
- 证据充分/口径统一
- 闭环在案
