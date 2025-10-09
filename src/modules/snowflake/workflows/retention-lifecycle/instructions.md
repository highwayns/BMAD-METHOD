# retention-lifecycle - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/retention-lifecycle/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this retention/lifecycle (time travel/fail-safe/archive)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="Time Travel/Fail-safe/归档">
<action>Work on time travel/fail-safe/归档</action>
<template-output section="retention"/>
</step>

<step n="3" goal="存储分层与清理">
<action>Work on 存储分层与清理</action>
<template-output section="storage"/>
</step>

<step n="4" goal="法务留置与例外">
<action>Work on 法务留置与例外</action>
<template-output section="legal"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
