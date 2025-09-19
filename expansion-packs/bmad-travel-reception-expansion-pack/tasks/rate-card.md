# task: rate-card

version: 1.0
role: vendor-procurement-manager
purpose: 建立价目与折扣体系，便于下单与对账。
inputs: [计价规则, 明细条目]
outputs: [docs/vendor/rate-card-<vendor>.md]
steps:

- 渲染 templates/rate-card-tmpl.yaml
- 执行 rate-parity-audit-check（按需）
  acceptance:
- 口径统一/字段完整
- 核算与对账无二义
