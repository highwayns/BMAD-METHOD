# gate-check - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/gate-check/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this release gate check (go/no-go)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="清单通过与签字">
<action>Work on 清单通过与签字</action>
<template-output section="checklists"/>
</step>

<step n="3" goal="监控就绪与窗口">
<action>Work on 监控就绪与窗口</action>
<template-output section="monitoring"/>
</step>

<step n="4" goal="Owner/签字与验收">
<action>Work on owner/签字与验收</action>
<template-output section="signoff"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
