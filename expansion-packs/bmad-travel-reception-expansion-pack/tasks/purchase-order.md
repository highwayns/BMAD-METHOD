# task: purchase-order

version: 1.0
role: vendor-procurement-manager
purpose: 生成PO并与合同/价目/税票口径一致。
inputs: [供应商/PO号/日期/币种, 合同/价目/税率, 明细与交付]
outputs: [docs/vendor/po-<id>.md]
steps:

- 渲染 templates/purchase-order-tmpl.yaml
- 与运营/财务对齐交付与开票信息
  acceptance:
- 三单一致
- 交付路径明确
