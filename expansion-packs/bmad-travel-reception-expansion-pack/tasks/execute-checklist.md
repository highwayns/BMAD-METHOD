# task: execute-checklist

version: 1.0
role: sales-account-manager
purpose: 执行并记录一次检查看板。
inputs: [清单路径, 责任人/执行时间]
outputs: [reports/checklist-run-YYYYMMDD.md]
steps:

- 加载清单并逐项勾选
- 未通过项记录原因与整改人/时限
- 生成运行报告并归档
  acceptance:
- 全量项状态可回溯
- 纠正措施有负责人/截止
