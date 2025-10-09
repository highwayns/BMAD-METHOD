# quarterly-posture-review - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/quarterly-posture-review/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this quarterly posture review (reliability/cost/security)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="健康分（SLO/成本/事件/质量）">
<action>Work on 健康分（slo/成本/事件/质量）</action>
<template-output section="scorecard"/>
</step>

<step n="3" goal="风险与积压">
<action>Work on 风险与积压</action>
<template-output section="risks"/>
</step>

<step n="4" goal="改进项与路线图">
<action>Work on 改进项与路线图</action>
<template-output section="roadmap"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
