# Compatibility Verification (Pact)

docOutputLocation: docs/contracts/compat-verification.md

## Purpose

以 Pact/样例回放验证兼容性，生成通过/阻塞报告。

## Inputs

- templates/pact-testcase-tmpl.json
- templates/sample-data-generator-tmpl.yaml

## Steps

- 基于旧版样例与新契约进行回放/断言
- 汇总通过率与阻塞项

## Outputs

- docs/contracts/compat-verification.md
