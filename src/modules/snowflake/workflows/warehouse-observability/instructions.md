# warehouse-observability - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/warehouse-observability/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this warehouse observability (queues/concurrency/spill)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="队列/并发与热点">
<action>Work on 队列/并发与热点</action>
<template-output section="queues"/>
</step>

<step n="3" goal="溢写/内存/缓存命中">
<action>Work on 溢写/内存/缓存命中</action>
<template-output section="spill"/>
</step>

<step n="4" goal="扩缩容/隔离与SLA">
<action>Work on 扩缩容/隔离与sla</action>
<template-output section="scaling"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
