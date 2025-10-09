# Ingestion Plan Workflow Instructions

**Critical**: Reference workflow.xml from bmad/core for XML tag definitions.

## Workflow Goal
Create a comprehensive ingestion and loading plan covering Stage/Copy/Snowpipe strategies, security, and schema evolution.

## Steps

### Step 1: Understand Requirements
<action>
Ask the user about their data ingestion requirements:
- Data sources (files, APIs, databases, streams)
- Volume and frequency
- File formats and schemas
- Security and compliance needs
- Performance requirements
</action>

### Step 2: Define Data Sources
<template-output section="sources">
Document all data sources with:
- Source system/location
- Data format and structure
- Volume and velocity
- Update patterns (batch/streaming/real-time)
- Data contracts and schemas
</template-output>

### Step 3: Stage Configuration
<template-output section="staging">
Define external and internal stage strategy:
- Stage locations (S3, Azure, GCS)
- Encryption configuration
- Directory structure
- Retention policies
- Access controls
</template-output>

### Step 4: Copy Strategy
<template-output section="copy">
Document COPY command parameters:
- Parallelization settings
- Error handling (ON_ERROR)
- File format options
- Transformation logic
- Scheduling and orchestration
</template-output>

### Step 5: Snowpipe Configuration
<template-output section="snowpipe">
Define Snowpipe setup if real-time/streaming:
- Event notification configuration
- Auto-ingest settings
- Error handling and DLQ
- Monitoring and alerts
- Backfill strategies
</template-output>

### Step 6: Schema Evolution
<template-output section="schema-evolution">
Document schema management:
- Schema versioning strategy
- Evolution handling
- Contract validation
- Breaking change procedures
</template-output>

### Step 7: Security Configuration
<template-output section="security">
Document security measures:
- Role-based access control
- Network policies
- Encryption (at-rest, in-transit)
- Key management
- Audit logging
</template-output>

### Step 8: Review and Validation
<check>
Verify all sections are complete:
- [ ] All data sources documented
- [ ] Stage configuration defined
- [ ] Copy strategy specified
- [ ] Security controls documented
- [ ] Schema evolution plan ready
</check>

### Step 9: Output Document
<ask>
Ready to generate the final ingestion plan document?
</ask>

<action>
Generate the complete ingestion plan using the template and user inputs.
</action>
