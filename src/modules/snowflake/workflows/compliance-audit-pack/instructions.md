# compliance-audit-pack - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/compliance-audit-pack/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this compliance audit pack (evidence/sign-offs)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="证据（审批/门禁/发布/回退/验证）">
<action>Work on 证据（审批/门禁/发布/回退/验证）</action>
<template-output section="evidence"/>
</step>

<step n="3" goal="控制-条款映射（SOX/ISO/GDPR）">
<action>Work on 控制-条款映射（sox/iso/gdpr）</action>
<template-output section="mappings"/>
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
