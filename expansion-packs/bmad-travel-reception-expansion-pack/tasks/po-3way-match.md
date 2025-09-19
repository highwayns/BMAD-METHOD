# task: po-3way-match

version: 1.0
role: finance-billing-specialist
purpose: 完成PO/对账单/发票三单匹配与差异闭环。
inputs: [供应商/PO/发票, 对账单, 差异与处理]
outputs: [docs/fin/po-3wm-<vendor>-<po>.md]
steps:

- 渲染 templates/po-3way-match-tmpl.yaml
- 执行 po-3way-check 清单
  acceptance:
- 匹配完成
- 差异闭环
