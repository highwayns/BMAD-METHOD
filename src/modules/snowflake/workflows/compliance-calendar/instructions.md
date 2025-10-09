# compliance-calendar - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/compliance-calendar/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this compliance calendar (audits/reviews/exercises)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="月/季/年审计与复查">
<action>Work on 月/季/年审计与复查</action>
<template-output section="cadence"/>
</step>

<step n="3" goal="责任人与签字">
<action>Work on 责任人与签字</action>
<template-output section="owners"/>
</step>

<step n="4" goal="证据收集与档案">
<action>Work on 证据收集与档案</action>
<template-output section="evidence"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
