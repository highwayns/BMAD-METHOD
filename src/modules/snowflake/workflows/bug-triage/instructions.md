# bug-triage - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/bug-triage/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this bug triage & defect lifecycle</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="受理/分级/归属">
<action>Work on 受理/分级/归属</action>
<template-output section="intake"/>
</step>

<step n="3" goal="修复SLA/降级与例外">
<action>Work on 修复sla/降级与例外</action>
<template-output section="sla"/>
</step>

<step n="4" goal="验证/回归/关闭">
<action>Work on 验证/回归/关闭</action>
<template-output section="closure"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
