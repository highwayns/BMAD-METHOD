# rfc-new - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/rfc-new/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this new rfc (change proposal)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="概述/目标/范围">
<action>Work on 概述/目标/范围</action>
<template-output section="summary"/>
</step>

<step n="3" goal="影响面（对象/作业/权限/成本）">
<action>Work on 影响面（对象/作业/权限/成本）</action>
<template-output section="impact"/>
</step>

<step n="4" goal="风险/缓解/回退">
<action>Work on 风险/缓解/回退</action>
<template-output section="risk"/>
</step>

<step n="5" goal="实施计划/时窗/负责人">
<action>Work on 实施计划/时窗/负责人</action>
<template-output section="plan"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
