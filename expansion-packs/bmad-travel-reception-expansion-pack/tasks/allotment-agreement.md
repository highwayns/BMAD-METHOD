# task: allotment-agreement

version: 1.0
role: vendor-procurement-manager
purpose: 制定配额/释放/罚则与停卖触发，旺季保供。
inputs: [配额与释放, 黑名单与停卖]
outputs: [docs/vendor/allotment-<vendor>.md]
steps:

- 渲染 templates/allotment-agreement-tmpl.yaml
- 执行 allotment-release-check 与 stop-sell-activation-check
  acceptance:
- 释放曲线清晰
- 停卖机制可执行
