# task: eod-report

version: 1.0
role: onsite-ops-lead
purpose: 形成当日收工报告与改进行动台账。
inputs: [KPI与事件, 经验与行动]
outputs: [reports/onsite-eod-YYYYMMDD.md]
steps:

- 渲染 templates/eod-report-tmpl.yaml
- 汇总问题台账与责任/期限
  acceptance:
- KPI可追溯
- 行动闭环
