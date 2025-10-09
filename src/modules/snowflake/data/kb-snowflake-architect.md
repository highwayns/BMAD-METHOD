# Snowflake Architect Knowledge (Quick Ref)

- 多账户策略可提升账务清晰与隔离度；跨区复制 + 时间穿梭提升韧性
- 身份：IdP+SCIM，组→角色映射；保留break-glass账户并演练
- 治理：标签/分类绑定策略（脱敏/行列访问）；契约化Schema与指标
- 工程：Streams/Tasks/Pipes + Dynamic Tables 结合批/流；Snowpark用于复杂UDF/ML
- 可观测：Account Usage/Information Schema 指标；失败率/延迟/信用消耗
- FinOps：按负载分仓库；自动挂起/恢复；资源监控阈值与动作；成本看板复盘
- 容灾：复制/故障转移；Runbook 与演练制度
