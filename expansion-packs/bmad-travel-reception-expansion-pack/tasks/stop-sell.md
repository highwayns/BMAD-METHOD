# task: stop-sell

version: 1.0
role: vendor-procurement-manager
purpose: 启动停卖并对外口径一致，给出替代方案。
inputs: [原因/品类/渠道, 起止/恢复]
outputs: [docs/vendor/stop-sell-<vendor>-<date>.md]
steps:

- 渲染 templates/stop-sell-notice-tmpl.yaml
- 执行 stop-sell-activation-check
  acceptance:
- 通知清晰/替代到位
- 恢复条件明确
