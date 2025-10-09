# evidence-pack - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/evidence-pack/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this evidence pack (audit/compliance)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="内容（时间线/日志/SQL/截图/签字）">
<action>Work on 内容（时间线/日志/sql/截图/签字）</action>
<template-output section="contents"/>
</step>

<step n="3" goal="控制-条款映射（ISO/SOX/GDPR）">
<action>Work on 控制-条款映射（iso/sox/gdpr）</action>
<template-output section="mapping"/>
</step>

<step n="4" goal="归档与检索">
<action>Work on 归档与检索</action>
<template-output section="archive"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
