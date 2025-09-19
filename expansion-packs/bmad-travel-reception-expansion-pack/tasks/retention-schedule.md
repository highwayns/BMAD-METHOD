# task: retention-schedule

version: 1.0
role: legal-compliance
purpose: 建立文档与数据留存/销毁计划。
inputs: [文档/系统/期限/销毁]
outputs: [docs/legal/retention-schedule.md]
steps:

- 渲染 templates/retention-schedule-tmpl.yaml
- 执行 retention-check 清单
  acceptance:
- 期限明确
- 销毁可审计
