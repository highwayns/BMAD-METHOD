# bi-release - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/bi-release/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this bi release (views/semantic layer/caching)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="语义层/口径/变更说明">
<action>Work on 语义层/口径/变更说明</action>
<template-output section="semantic"/>
</step>

<step n="3" goal="缓存策略/SOS/MV">
<action>Work on 缓存策略/sos/mv</action>
<template-output section="cache"/>
</step>

<step n="4" goal="UAT/验收/回退">
<action>Work on uat/验收/回退</action>
<template-output section="uat"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
