# experiment-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/experiment-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this experiment plan (hypothesis/a-b)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="假设与机制">
<action>Work on 假设与机制</action>
<template-output section="hypothesis"/>
</step>

<step n="3" goal="设计（分流/样本量/盲法/干预）">
<action>Work on 设计（分流/样本量/盲法/干预）</action>
<template-output section="design"/>
</step>

<step n="4" goal="指标与判定标准">
<action>Work on 指标与判定标准</action>
<template-output section="metrics"/>
</step>

<step n="5" goal="Guardrail 指标与停机规则">
<action>Work on guardrail 指标与停机规则</action>
<template-output section="guardrails"/>
</step>

<step n="6" goal="伦理与风险">
<action>Work on 伦理与风险</action>
<template-output section="ethics"/>
</step>

<step n="7" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
