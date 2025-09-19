# task: outage-comms

version: 1.0
role: customer-service-care-lead
purpose: 组织故障/大面积中断的外部沟通与FAQ/补偿口径。
inputs: [影响范围/受众, 通知频率/渠道, FAQ与补偿]
outputs: [docs/care/outage-comms-<incident>.md]
steps:

- 渲染 templates/outage-incident-comms-tmpl.yaml
- 执行 outage-comms-check 清单
  acceptance:
- 信息透明一致
- 负面舆情可控
