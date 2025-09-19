# task: shift-roster

version: 1.0
role: onsite-ops-lead
purpose: 生成现场班表与交接事项。
inputs: [岗位/姓名/呼号/时间, 联系方式/交接]
outputs: [docs/onsite/shift-roster-YYYYMMDD.md]
steps:

- 渲染 templates/shift-roster-tmpl.yaml
- 发布并收集回执
  acceptance:
- 呼号/时段覆盖完整
- 回执留存
