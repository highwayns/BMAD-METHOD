# Create Document: Snowflake Architecture Overview

type: task
id: pm-create-doc-snowflake-architecture
owner: Product Manager
updated: 2025-09-24

intent: |
Produce a business-facing architecture overview that ties features to Snowflake components
(accounts, databases/schemas, warehouses, security model, data products, SLAs).

inputs:

- product-requirements.md
- business-process-map.md
- target-architecture.md (if exists; else capture assumptions)

steps:

- Gather: consolidate diagrams and decisions from Architect & Platform Owner
- Structure: use the provided template sections (scope, topology, security, SLAs, risks)
- Validate: review with Architect/Security/Privacy for accuracy and feasibility
- Publish: commit to docs/architecture/overview.md and link in PRD

outputs:

- docs/architecture/overview.md

evidence:

- Sign-offs from Architect, Security, Privacy
- Links to source diagrams and ADRs

acceptance_criteria:

- ✅ Covers topology (envs/regions), warehouses, storage, governance, DR
- ✅ Maps features↔components and lists non-functional requirements
- ✅ All risks and open questions captured with owners and due dates
