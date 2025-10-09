# snowpipe-streaming-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/snowpipe-streaming-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this snowpipe streaming plan (low-latency)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="Endpoint/Client 参数">
<action>Work on endpoint/client 参数</action>
<template-output section="endpoints"/>
</step>

<step n="3" goal="批量/缓冲/压缩策略">
<action>Work on 批量/缓冲/压缩策略</action>
<template-output section="batching"/>
</step>

<step n="4" goal="顺序与幂等写">
<action>Work on 顺序与幂等写</action>
<template-output section="ordering"/>
</step>

<step n="5" goal="监控与回放">
<action>Work on 监控与回放</action>
<template-output section="observability"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
