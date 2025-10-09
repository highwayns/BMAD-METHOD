# scheduling-policies - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/scheduling-policies/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this scheduling policies (off-peak/auto-suspend)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="工作日/夜间/周末与节假日">
<action>Work on 工作日/夜间/周末与节假日</action>
<template-output section="calendars"/>
</step>

<step n="3" goal="降配/停用/禁止大查询">
<action>Work on 降配/停用/禁止大查询</action>
<template-output section="policies"/>
</step>

<step n="4" goal="演练/回退/例外">
<action>Work on 演练/回退/例外</action>
<template-output section="validation"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
