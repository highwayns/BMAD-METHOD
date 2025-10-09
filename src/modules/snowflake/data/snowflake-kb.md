# Snowflake Knowledge (PO Quick Ref)

- 账户/组织：多账户隔离可提升治理与账务清晰度；跨区复制/故障转移提升韧性
- 身份：建议 IdP + SCIM，同步组→角色映射；保留 break-glass 账户并定期演练
- 治理：标签/分类→策略（屏蔽/行列访问），统一词汇与数据契约
- 数据工程：优先 Streams/Tasks/Pipes 与 Dynamic Tables；批+流结合；Snowpark for complex UDF/ML
- 可观测：Account Usage/Information Schema → 指标面板（信用消耗/失败率/查询延迟）
- FinOps：按工作负载分仓库，自动挂起/恢复；资源监控告警；周月复盘与成本看板
- 数据共享：安全共享/Marketplace；合同与撤销流程配套；Provider/Consumer 双端演练
