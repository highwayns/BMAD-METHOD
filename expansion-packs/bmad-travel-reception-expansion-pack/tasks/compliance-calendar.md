# task: compliance-calendar

version: 1.0
role: legal-compliance
purpose: 建立年度合规日历与时限管理。
inputs: [事项/频率/责任/期限]
outputs: [docs/legal/compliance-calendar.md]
steps:

- 渲染 templates/compliance-calendar-tmpl.yaml
- 周期回顾与提醒
  acceptance:
- 时限受控
- 责任明确
