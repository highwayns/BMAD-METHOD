# labeling-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/labeling-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this labeling & weak supervision plan</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="标注来源与质量管理">
<action>Work on 标注来源与质量管理</action>
<template-output section="sources"/>
</step>

<step n="3" goal="规则/启发/远程监督">
<action>Work on 规则/启发/远程监督</action>
<template-output section="heuristics"/>
</step>

<step n="4" goal="采样与评审">
<action>Work on 采样与评审</action>
<template-output section="sampling"/>
</step>

<step n="5" goal="PII/脱敏与用途限定">
<action>Work on pii/脱敏与用途限定</action>
<template-output section="privacy"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
