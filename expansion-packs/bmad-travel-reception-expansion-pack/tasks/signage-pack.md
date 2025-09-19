# task: signage-pack

version: 1.0
role: onsite-ops-lead
purpose: 盘点现场物料（指示牌/围栏/地贴/胸卡等）并安排回收。
inputs: [名称/数量/放置点, 负责人/回收时间]
outputs: [docs/onsite/signage-pack-YYYYMMDD.md]
steps:

- 渲染 templates/signage-pack-list-tmpl.yaml
- 贴地执行并回收归档
  acceptance:
- 物料在位并回收
- 责任人到位
