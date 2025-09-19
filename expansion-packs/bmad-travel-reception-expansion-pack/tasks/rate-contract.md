# task: rate-contract

version: 1.0
role: hotel-contracting-manager
purpose: 生成并归档“酒店合同与价表”，统一口径并通过抽检。
inputs: [合同期限, 价表, 政策, 审批链]
outputs: [docs/hotel/rate-contract-<hotel>-<YYYY>.md]
steps:

- 渲染 templates/rate-contract-tmpl.yaml
- 价表/配额导入系统并抽查
  acceptance:
- 条款齐全/口径一致
- 导入抽查通过
