# task: sanctions-screening-log

version: 1.0
role: legal-compliance
purpose: 记录并复核制裁/名单筛查结果。
inputs: [对象/来源/命中/处理]
outputs: [reports/legal/sanctions-<period>.md]
steps:

- 渲染 templates/sanctions-screening-log-tmpl.yaml
- 执行 sanctions-screening-check 清单
  acceptance:
- 命中复核完备
- 报表可追溯
