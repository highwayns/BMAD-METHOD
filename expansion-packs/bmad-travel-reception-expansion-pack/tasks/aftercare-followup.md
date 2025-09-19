# task: aftercare-followup

version: 1.0
role: customer-service-care-lead
purpose: 统一售后回访节奏，找回NPS与口碑。
inputs: [回访对象/时间/问卷, 未闭环问题]
outputs: [docs/care/aftercare-followup-<period>.md]
steps:

- 渲染 templates/aftercare-followup-tmpl.yaml
- 执行 aftercare-check 清单
  acceptance:
- 回访覆盖率达标
- 闭环推进有效
