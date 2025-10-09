# compliance-mapping - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/compliance-mapping/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this compliance mapping (gdpr/sox/iso/pii)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="控制→条款映射矩阵">
<action>Work on 控制→条款映射矩阵</action>
<template-output section="controls"/>
</step>

<step n="3" goal="证据与报告生成">
<action>Work on 证据与报告生成</action>
<template-output section="evidence"/>
</step>

<step n="4" goal="内外部审计对接">
<action>Work on 内外部审计对接</action>
<template-output section="audits"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
