# task: lost-found

version: 1.0
role: transport-logistics-coordinator
purpose: 统一失物登记与归还闭环。
inputs: [拾获时间/地点/物品, 联系方式, 签收回执]
outputs: [docs/transport/lost-found-log.md]
steps:

- 渲染 templates/lost-found-log-tmpl.yaml
- 执行 lost-found-process 清单
  acceptance:
- 编号追踪
- 回执留存
