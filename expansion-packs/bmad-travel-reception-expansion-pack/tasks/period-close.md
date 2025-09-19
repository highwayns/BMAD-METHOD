# task: period-close

version: 1.0
role: finance-billing-specialist
purpose: 组织期间结账（截止/应计/调节/报表）。
inputs: [截止/递延/应计/摊销/调节]
outputs: [reports/period-close-<period>.md]
steps:

- 渲染 templates/period-close-checklist-tmpl.yaml
- 执行 close-period-check 清单
  acceptance:
- T+N按时完成
- 报表与底稿齐全
