# {{project_name}} · Ingestion & Loading Plan

**Document ID**: {{document_id}}
**Version**: {{version}}
**Date**: {{date}}
**Author**: {{author}}
**Status**: {{status}}

---

## Executive Summary

Brief overview of the ingestion strategy and key decisions.

---

## 1. Data Sources Inventory

### {{sources}}

List all data sources with:

| Source ID | Type | Format | Volume | Frequency | Owner |
|-----------|------|--------|---------|-----------|-------|
| | | | | | |

### Data Contracts

Document schema contracts and SLAs for each source.

---

## 2. Stage Configuration

### {{staging}}

### External Stages

**S3/Azure/GCS Configuration**:
```sql
CREATE OR REPLACE STAGE {{stage_name}}
    URL='{{stage_url}}'
    CREDENTIALS=({{credentials}})
    ENCRYPTION=(TYPE='{{encryption_type}}')
    FILE_FORMAT=(TYPE='{{format_type}}');
```

### Internal Stages

Document internal staging strategy and retention.

### Directory Structure

```
/landing/{{source}}/{{yyyy}}/{{mm}}/{{dd}}/
```

---

## 3. COPY Strategy

### {{copy}}

### Copy Configuration

```sql
COPY INTO {{target_table}}
FROM @{{stage_name}}/{{path}}
FILE_FORMAT = ({{file_format}})
ON_ERROR = '{{error_handling}}'
PATTERN = '{{file_pattern}}'
;
```

### Parallelization

- Warehouse size: {{warehouse_size}}
- Max file size: {{max_file_size}}
- Concurrency: {{concurrency_level}}

### Error Handling

- Error threshold: {{error_threshold}}
- Dead letter queue: {{dlq_location}}
- Retry logic: {{retry_strategy}}

---

## 4. Snowpipe Configuration

### {{snowpipe}}

### Auto-Ingest Setup

```sql
CREATE OR REPLACE PIPE {{pipe_name}}
    AUTO_INGEST = TRUE
    AS
    COPY INTO {{target_table}}
    FROM @{{stage_name}}
    FILE_FORMAT = ({{file_format}});
```

### Event Notification

- Cloud provider: {{cloud_provider}}
- Event source: {{event_source}}
- Notification channel: {{notification_channel}}

### Monitoring

- Pipe status checks: {{monitoring_interval}}
- Alert thresholds: {{alert_config}}
- On-call rotation: {{oncall_team}}

---

## 5. Schema Evolution

### {{schema-evolution}}

### Version Control

| Version | Date | Changes | Migration Script |
|---------|------|---------|------------------|
| | | | |

### Evolution Strategy

- Backward compatibility: {{backward_compat}}
- Breaking change process: {{breaking_change_process}}
- Schema registry: {{schema_registry_url}}

---

## 6. Security & Compliance

### {{security}}

### Access Control

```sql
GRANT USAGE ON STAGE {{stage_name}} TO ROLE {{role_name}};
GRANT READ ON STAGE {{stage_name}} TO ROLE {{role_name}};
```

### Encryption

- At-rest: {{encryption_at_rest}}
- In-transit: {{encryption_in_transit}}
- Key management: {{key_management_service}}

### Network Policies

```sql
CREATE OR REPLACE NETWORK POLICY {{policy_name}}
    ALLOWED_IP_LIST = ('{{ip_ranges}}');
```

### Audit Logging

- Access logs: {{access_log_location}}
- Error logs: {{error_log_location}}
- Retention period: {{retention_days}} days

---

## 7. Performance & Cost Optimization

### Warehouse Sizing

| Workload | Warehouse Size | Auto-suspend | Scaling Policy |
|----------|----------------|--------------|----------------|
| | | | |

### Cost Controls

- Budget: {{monthly_budget}}
- Resource monitors: {{resource_monitor_config}}
- Cost allocation tags: {{cost_tags}}

---

## 8. Operational Runbook

### Monitoring

- Dashboard: {{dashboard_url}}
- Key metrics: {{key_metrics}}
- SLOs: {{slo_targets}}

### Incident Response

- Escalation path: {{escalation_path}}
- Runbook: {{runbook_url}}
- Contact: {{oncall_contact}}

---

## 9. Testing & Validation

### Test Plan

- [ ] Stage accessibility test
- [ ] COPY command validation
- [ ] Error handling verification
- [ ] Snowpipe smoke test
- [ ] Performance benchmarking
- [ ] Security audit

---

## 10. Deployment Checklist

- [ ] Stages created and tested
- [ ] File formats configured
- [ ] COPY commands validated
- [ ] Snowpipes deployed (if applicable)
- [ ] Monitoring configured
- [ ] Documentation complete
- [ ] Team trained
- [ ] Runbook reviewed

---

## Sign-off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Data Engineering Lead | | | |
| Platform Owner | | | |
| Security Engineer | | | |
| SRE | | | |

---

**Document Control**
- Last Updated: {{last_updated}}
- Next Review: {{next_review}}
- Version History: {{version_history}}
