# cdc-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/cdc-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this cdc plan (debezium/log-based)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="源系统与连接器">
<action>Work on 源系统与连接器</action>
<template-output section="sources"/>
</step>

<step n="3" goal="顺序/幂等合并（MERGE）">
<action>Work on 顺序/幂等合并（merge）</action>
<template-output section="ordering"/>
</step>

<step n="4" goal="Schema 演进与兼容策略">
<action>Work on schema 演进与兼容策略</action>
<template-output section="schema_evolution"/>
</step>

<step n="5" goal="重放/回补与断点">
<action>Work on 重放/回补与断点</action>
<template-output section="reprocessing"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
