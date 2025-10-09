# realtime-scoring - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/realtime-scoring/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this realtime scoring (udf/udtf/api)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="端点/并发/队列/背压">
<action>Work on 端点/并发/队列/背压</action>
<template-output section="endpoints"/>
</step>

<step n="3" goal="幂等等价与去重键">
<action>Work on 幂等等价与去重键</action>
<template-output section="idempotency"/>
</step>

<step n="4" goal="延迟SLO/监控与回退">
<action>Work on 延迟slo/监控与回退</action>
<template-output section="latency"/>
</step>

<step n="5" goal="权限/速率限制/审计">
<action>Work on 权限/速率限制/审计</action>
<template-output section="security"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
