# task: apology-script

version: 1.0
role: customer-service-care-lead
purpose: 形成标准道歉脚本并在各渠道复用。
inputs: [四段式话术, 回执确认]
outputs: [docs/care/apology-script.md]
steps:

- 渲染 templates/apology-script-tmpl.yaml
- 执行 apology-quality-check 清单
  acceptance:
- 话术清晰真诚
- 回执可追溯
