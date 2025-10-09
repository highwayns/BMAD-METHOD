# snowpipe-streaming-observability - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/snowpipe-streaming-observability/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this snowpipe & streaming observability</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="文件/批量/频率与延迟">
<action>Work on 文件/批量/频率与延迟</action>
<template-output section="pattern"/>
</step>

<step n="3" goal="并发/重试/死信">
<action>Work on 并发/重试/死信</action>
<template-output section="concurrency"/>
</step>

<step n="4" goal="成本/量/峰值">
<action>Work on 成本/量/峰值</action>
<template-output section="costs"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
