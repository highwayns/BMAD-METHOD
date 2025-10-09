# streaming-pipelines - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/streaming-pipelines/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this streaming pipelines (snowpipe/streaming)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="连接器/并发/重试">
<action>Work on 连接器/并发/重试</action>
<template-output section="connectors"/>
</step>

<step n="3" goal="成本/批量/吞吐">
<action>Work on 成本/批量/吞吐</action>
<template-output section="costs"/>
</step>

<step n="4" goal="观测/告警/死信">
<action>Work on 观测/告警/死信</action>
<template-output section="observability"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
