# Ingestion & Streaming Quick Knowledge (Snowflake)

- 批：External Stage + COPY + 验证；微批优先以稳定为先
- 流：Snowpipe/Snowpipe Streaming/Kafka/CDC；Exactly-Once by Effect 通过去重键与幂等合并达成
- 顺序与去重：事件时间/处理时间/水位线；MERGE/UPSERT + 审计
- 回放与回补：Checkpoint/审计表记录位点；隔离域回放与比对
- 可观测：lag/throughput/error/retry；任务失败与背压可视化
- 成本：分仓库/并发扩展/离峰降配；资源监控告警
