# kafka-connector-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/kafka-connector-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this kafka connector plan (topic→table)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="Topic/分区/键策略">
<action>Work on topic/分区/键策略</action>
<template-output section="topics"/>
</step>

<step n="3" goal="Schema/兼容性（Avro/JSON/Schema Registry）">
<action>Work on schema/兼容性（avro/json/schema registry）</action>
<template-output section="schema"/>
</step>

<step n="4" goal="Offset 管理与回放">
<action>Work on offset 管理与回放</action>
<template-output section="offset"/>
</step>

<step n="5" goal="DLQ/再处理与报警">
<action>Work on dlq/再处理与报警</action>
<template-output section="dlq"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
