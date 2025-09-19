# task: vendor-sla-review

version: 1.0
role: operations-director
purpose: 按季度评审供应商 SLA，更新黑白名单与改进项。
inputs:

- 近90天履约数据
- 合同与合规材料
  outputs:
- reports/vendor-sla-review-YYYYQ.md
  steps:
- create-doc → templates/vendor-sla-tmpl.yaml
- 形成整改计划与复核节奏
- 结果进入供应商名录与价格条款更新
  acceptance:
- 指标、证据与整改闭环明确
- 合规（APPI/资质/保险）通过
