# ordering-dedup-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/ordering-dedup-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this ordering & de-duplication plan</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="去重键与幂等写（Natural/Surrogate）">
<action>Work on 去重键与幂等写（natural/surrogate）</action>
<template-output section="keys"/>
</step>

<step n="3" goal="时间窗/水位线与迟到处理">
<action>Work on 时间窗/水位线与迟到处理</action>
<template-output section="windows"/>
</step>

<step n="4" goal="MERGE/UPSERT 模式">
<action>Work on merge/upsert 模式</action>
<template-output section="merge"/>
</step>

<step n="5" goal="审计/对账与警戒">
<action>Work on 审计/对账与警戒</action>
<template-output section="audits"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
