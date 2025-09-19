# task: credit-note

version: 1.0
role: finance-billing-specialist
purpose: 生成信用票据（红字）并完成冲销/再开。
inputs: [原发票/金额/原因, 冲销与再开]
outputs: [docs/fin/credit-note-<client>-<invoice>.md]
steps:

- 渲染 templates/credit-note-tmpl.yaml
- 执行 credit-note-check 清单
  acceptance:
- 冲销清晰
- 回执在案
