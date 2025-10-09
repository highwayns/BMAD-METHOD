# security-privacy - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/security-privacy/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this security & privacy</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="RBAC/最小权限">
<action>Work on rbac/最小权限</action>
<template-output section="rbac"/>
</step>

<step n="3" goal="标签/掩码/行列策略">
<action>Work on 标签/掩码/行列策略</action>
<template-output section="masking"/>
</step>

<step n="4" goal="审计与保留">
<action>Work on 审计与保留</action>
<template-output section="audit"/>
</step>

<step n="5" goal="共享/再分发限制">
<action>Work on 共享/再分发限制</action>
<template-output section="sharing"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
