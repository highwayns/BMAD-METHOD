# DE Quick Knowledge (Snowflake)

- 优先分仓库以隔离工作负载；自动挂起/恢复 + 并发扩展
- 批处理 ELT：Stage/Copy → Transform（dbt/Streams/Tasks/Dynamic Tables）
- 流式：Pipes/Tasks + 幂等/去重/迟到处理；背压/慢启动
- Snowpark：包管理/权限/UDF/SP 安全沙箱
- 观测：Account Usage/Information Schema → KPI/SLI 仪表盘与告警
- 成本：Resource Monitor + 预算阈值 + 调度；复盘与优化
