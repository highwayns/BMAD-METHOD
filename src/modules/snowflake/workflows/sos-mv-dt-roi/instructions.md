# sos-mv-dt-roi - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/sos-mv-dt-roi/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this sos/mv/dt roi & tuning</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="候选对象/命中率/延迟">
<action>Work on 候选对象/命中率/延迟</action>
<template-output section="candidates"/>
</step>

<step n="3" goal="维护成本/刷新频率">
<action>Work on 维护成本/刷新频率</action>
<template-output section="costs"/>
</step>

<step n="4" goal="ROI 评估与决策">
<action>Work on roi 评估与决策</action>
<template-output section="outcome"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
