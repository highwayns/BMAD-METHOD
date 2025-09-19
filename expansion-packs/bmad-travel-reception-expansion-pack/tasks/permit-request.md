# task: permit-request

version: 1.0
role: transport-logistics-coordinator
purpose: 申请停车/通行证并归档批复与回执。
inputs: [城市/日期/时段, 上落客点/车牌, 表单/路线图/联系人]
outputs: [docs/transport/permit-request-<city>-<date>.md]
steps:

- 渲染 templates/parking-permit-request-tmpl.yaml
- 归档批复与回执
  acceptance:
- 资料齐全
- 回执在案
