# purpose-limitation - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/purpose-limitation/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this purpose limitation (use-case boundaries/dp)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="目的定义/白名单/黑名单">
<action>Work on 目的定义/白名单/黑名单</action>
<template-output section="scope"/>
</step>

<step n="3" goal="运行时校验与告警">
<action>Work on 运行时校验与告警</action>
<template-output section="controls"/>
</step>

<step n="4" goal="证据留存与审计">
<action>Work on 证据留存与审计</action>
<template-output section="evidence"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
