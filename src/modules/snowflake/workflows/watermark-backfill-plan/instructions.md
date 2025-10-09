# watermark-backfill-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/watermark-backfill-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this watermark & backfill plan</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="水位线选择与存储（审计表/Checkpoint）">
<action>Work on 水位线选择与存储（审计表/checkpoint）</action>
<template-output section="watermark"/>
</step>

<step n="3" goal="回放策略（范围/速率/幂等）">
<action>Work on 回放策略（范围/速率/幂等）</action>
<template-output section="replay"/>
</step>

<step n="4" goal="隔离域与比对校验">
<action>Work on 隔离域与比对校验</action>
<template-output section="isolation"/>
</step>

<step n="5" goal="切换/回退与验证">
<action>Work on 切换/回退与验证</action>
<template-output section="cutover"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
