# Design Data Contracts Task

docOutputLocation: docs/contracts/data-contracts.md

## Purpose

为每条上/下游链路定义数据契约与演进策略（向前/向后兼容），明确破坏性变更流程。

## Inputs

- templates/data-contract-tmpl.yaml

## Steps

- 为每个接口/表定义 schema、主键/唯一性、时序列/水位线
- 约定错误处理/死信/重放窗口
- 设定演进策略：可空新增/枚举扩展/弃用周期/版本策略

## Outputs

- contracts/\*.yaml
