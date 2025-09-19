# task: case-triage

version: 1.0
role: customer-service-care-lead
purpose: 完成分级/归属与编号方案，明确责任与下一步。
inputs: [等级与域, 责任方, 方案与时限]
outputs: [docs/care/case-triage-<case_id>.md]
steps:

- 渲染 templates/case-triage-tmpl.yaml
- 执行 triage-check 清单
  acceptance:
- 分级/归属/责任清晰
- 下一步时间承诺
