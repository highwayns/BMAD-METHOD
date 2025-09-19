# task: dpia

version: 1.0
role: legal-compliance
purpose: 进行隐私影响评估并形成缓解措施。
inputs: [数据类别/流向/处理者, 风险/措施/残余]
outputs: [reports/legal/dpia-<project>.md]
steps:

- 渲染 templates/dpia-tmpl.yaml（逐节提问）
- 执行 data-transfer-check 清单
  acceptance:
- 风险识别充分
- 控制措施落地
