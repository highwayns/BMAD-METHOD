# task: qbr-pack

version: 1.0
role: vendor-procurement-manager
purpose: 形成季度业务回顾材料，推动共创与降本增效。
inputs: [业绩/成本/质量/风险, 改进/共创/旺季保障]
outputs: [docs/vendor/qbr-<vendor>-<period>.md]
steps:

- 渲染 templates/qbr-pack-tmpl.yaml
- 评审并形成行动清单
  acceptance:
- 结论清晰/行动可跟踪
- 双方签核
