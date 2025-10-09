# close-incident - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/close-incident/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this close incident (docs/evidence/approvals)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="关闭标准与验收">
<action>Work on 关闭标准与验收</action>
<template-output section="criteria"/>
</step>

<step n="3" goal="文档/证据/签字">
<action>Work on 文档/证据/签字</action>
<template-output section="docs"/>
</step>

<step n="4" goal="交接到问题管理">
<action>Work on 交接到问题管理</action>
<template-output section="handover"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
