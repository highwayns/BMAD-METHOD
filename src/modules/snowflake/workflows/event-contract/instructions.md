# event-contract - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/event-contract/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this event contract (streaming/cdc)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="事件名/Schema/示例Payload">
<action>Work on 事件名/schema/示例payload</action>
<template-output section="event"/>
</step>

<step n="3" goal="语义（一次性/至少一次/幂等）">
<action>Work on 语义（一次性/至少一次/幂等）</action>
<template-output section="semantics"/>
</step>

<step n="4" goal="顺序与重复处理">
<action>Work on 顺序与重复处理</action>
<template-output section="ordering"/>
</step>

<step n="5" goal="延迟与新鲜度SLO">
<action>Work on 延迟与新鲜度slo</action>
<template-output section="freshness"/>
</step>

<step n="6" goal="兼容性策略（扩展字段/弃用字段）">
<action>Work on 兼容性策略（扩展字段/弃用字段）</action>
<template-output section="compatibility"/>
</step>

<step n="7" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
