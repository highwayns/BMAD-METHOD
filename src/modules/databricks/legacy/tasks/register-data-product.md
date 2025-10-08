# Register Data Product Task

docOutputLocation: docs/catalog/data-products.md

## Purpose

登记/更新数据产品（Owner、SLO、新鲜度、血缘、隐私级别、共享策略）。

## Steps

- 依据 data-product-registry-tmpl.yaml 填写条目
- 连接 Unity Catalog/Delta 表/特征表/服务端点
- 注册质量指标与告警路由

## Outputs

- registry/data-products/\*.yaml
- docs/catalog/data-products.md
