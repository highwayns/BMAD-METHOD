# snowpipe-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/snowpipe-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this snowpipe plan (auto-ingest/retry/dlq)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="触发与通知（队列/事件）">
<action>Work on 触发与通知（队列/事件）</action>
<template-output section="triggers"/>
</step>

<step n="3" goal="重试/死信/补偿">
<action>Work on 重试/死信/补偿</action>
<template-output section="retries"/>
</step>

<step n="4" goal="权限与网络">
<action>Work on 权限与网络</action>
<template-output section="security"/>
</step>

<step n="5" goal="监控与告警">
<action>Work on 监控与告警</action>
<template-output section="observability"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
