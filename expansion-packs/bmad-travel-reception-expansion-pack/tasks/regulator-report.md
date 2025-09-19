# task: regulator-report

version: 1.0
role: legal-compliance
purpose: 完成监管报备并固化证据与批注。
inputs: [渠道/模板/期限/联系人]
outputs: [reports/legal/regulator-report-<id>.md]
steps:

- 渲染 templates/regulator-report-tmpl.yaml
- 执行 regulator-reporting-check 清单
  acceptance:
- 时限达标
- 记录可追溯
