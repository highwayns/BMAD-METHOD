# triage - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/triage/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this triage & assignment (ic/tech lead/comms/recorder)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="宣布 SEV/角色/桥接/频道">
<action>Work on 宣布 sev/角色/桥接/频道</action>
<template-output section="declare"/>
</step>

<step n="3" goal="证据收集（SQL/日志/变更）">
<action>Work on 证据收集（sql/日志/变更）</action>
<template-output section="evidences"/>
</step>

<step n="4" goal="假设与快速实验/回退保护">
<action>Work on 假设与快速实验/回退保护</action>
<template-output section="hypo"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
