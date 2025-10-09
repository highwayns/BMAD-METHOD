# verification - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/verification/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this verification (slis/smoke/backfill)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="冒烟/关键路径">
<action>Work on 冒烟/关键路径</action>
<template-output section="smoke"/>
</step>

<step n="3" goal="SLI 回落/回升">
<action>Work on sli 回落/回升</action>
<template-output section="slis"/>
</step>

<step n="4" goal="回填/差异/证据">
<action>Work on 回填/差异/证据</action>
<template-output section="backfill"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
