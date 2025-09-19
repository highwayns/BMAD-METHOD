# task: care-shift-roster

version: 1.0
role: customer-service-care-lead
purpose: 生成客服排班并标注备援与技能标签。
inputs: [渠道/客服/时段, 备援/技能标签]
outputs: [docs/care/care-shift-roster-YYYYMM.md]
steps:

- 渲染 templates/care-shift-roster-tmpl.yaml
- 公告并回执
  acceptance:
- 覆盖完整
- 溢出处理明确
