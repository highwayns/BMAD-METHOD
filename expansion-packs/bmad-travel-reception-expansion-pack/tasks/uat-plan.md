# task: uat-plan

version: 1.0
role: tech-systems-dms-crm
purpose: 输出UAT测试计划与通过标准。
inputs: [用例/数据/验收]
outputs: [docs/sys/uat-plan.md]
steps:

- 渲染 templates/training-guide-tmpl.yaml（转为UAT表述）
- 执行 api-go-live-check 与 data-quality-check
  acceptance:
- 用例覆盖率≥90%
- 缺陷闭环
