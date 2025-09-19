# 仓库事故 Runbook（队列/并发/溢写）

- 读取 `warehouse-triage.sql` 指标，识别队列/溢写热点
- 临时扩容或隔离高优先级仓库；配置 AUTO_SUSPEND 与并发
- 同步 FinOps 护栏与回退窗口
