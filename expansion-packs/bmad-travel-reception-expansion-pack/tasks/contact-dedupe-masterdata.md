# task: contact-dedupe-masterdata

version: 1.0
role: tech-systems-dms-crm
purpose: 建立去重与主数据治理策略与流程。
inputs: [标准化/匹配/合并/回滚]
outputs: [docs/sys/masterdata-<domain>.md]
steps:

- 渲染 templates/training-guide-tmpl.yaml（流程培训说明）
- 执行 dedupe-masterdata-check 清单
  acceptance:
- 重复率下降
- 回滚无损
