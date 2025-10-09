# schema-tests - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/schema-tests/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this schema tests (ddl/constraints)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="DDL 变更与幂等">
<action>Work on ddl 变更与幂等</action>
<template-output section="ddl"/>
</step>

<step n="3" goal="约束/索引/聚簇策略">
<action>Work on 约束/索引/聚簇策略</action>
<template-output section="constraints"/>
</step>

<step n="4" goal="兼容性与回退">
<action>Work on 兼容性与回退</action>
<template-output section="compatibility"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
