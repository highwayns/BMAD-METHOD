# task: proposal-quote

version: 1.0
role: sales-account-manager
purpose: 生成可成交的方案+报价，并内嵌毛利保护。
inputs: [lead-brief, 成本与价规, 旺季规则]
outputs: [docs/sales/proposal-quote.md]
steps:

- templates/proposal-quote-tmpl.yaml 渲染
- 校验毛利阈值与旺季价规
- 生成客户版与内部版（含成本）
  acceptance:
- 报价口径一致且可溯源
- 毛利达标并留痕
