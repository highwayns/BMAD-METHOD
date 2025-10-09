# release-train-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/release-train-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this release train plan (cadence/scope/gates)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="周期/窗口/冻结">
<action>Work on 周期/窗口/冻结</action>
<template-output section="cadence"/>
</step>

<step n="3" goal="跨域范围（ELT/DT/BI/ML/安全）">
<action>Work on 跨域范围（elt/dt/bi/ml/安全）</action>
<template-output section="scope"/>
</step>

<step n="4" goal="门禁清单/签字流程">
<action>Work on 门禁清单/签字流程</action>
<template-output section="gates"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
