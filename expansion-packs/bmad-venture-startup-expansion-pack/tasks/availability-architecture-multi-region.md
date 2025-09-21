# Availability Architecture & Multi-region

## Purpose

为关键服务设计高可用/多区域架构。

## Inputs

- 服务SLA/依赖/数据一致性要求
- templates/availability-architecture-tmpl.yaml
- checklists/production-readiness.md

## Outputs

- 可用性架构说明书。

## Steps

1. 单点与故障域分析
2. 冗余/隔离/降级/排队策略
3. 地域/可用区/读写拓扑
4. 一致性/分区容错/冲突处理
5. 容量/成本/复杂度权衡
