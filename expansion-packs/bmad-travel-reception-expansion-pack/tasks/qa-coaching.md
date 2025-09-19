# task: qa-coaching

version: 1.0
role: customer-service-care-lead
purpose: 建立质检抽样与教练改进闭环。
inputs: [抽样与维度, 教练与跟进]
outputs: [reports/qa-coaching-<period>.md]
steps:

- 渲染 templates/qa-coaching-plan-tmpl.yaml
- 执行 qa-sampling-check 清单
  acceptance:
- 质检客观一致
- 教练有成效
