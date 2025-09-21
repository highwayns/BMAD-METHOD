# Kubernetes Platform & GitOps

## Purpose

建设K8s平台/多租户/工具链与GitOps发布。

## Inputs

- 集群/工作负载/网络/存储/安全
- templates/k8s-platform-contract-and-addon-tmpl.yaml
- checklists/k8s-and-platform-hygiene.md

## Outputs

- 平台合约与附加组件清单。

## Steps

1. 多集群/命名空间与配额/准入控制
2. 镜像/供应链安全与签名/策略
3. Ingress/Service Mesh/网络策略
4. GitOps流水线/漂移/回滚
5. SLO与容量/弹性扩缩容
