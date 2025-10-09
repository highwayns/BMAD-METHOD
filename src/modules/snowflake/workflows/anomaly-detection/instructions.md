# anomaly-detection - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/anomaly-detection/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this anomaly detection (stats/seasonality/ml)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="信号（延迟/失败率/新鲜度/成本）">
<action>Work on 信号（延迟/失败率/新鲜度/成本）</action>
<template-output section="signals"/>
</step>

<step n="3" goal="阈值/统计/季节/ML">
<action>Work on 阈值/统计/季节/ml</action>
<template-output section="models"/>
</step>

<step n="4" goal="告警与自动化处置">
<action>Work on 告警与自动化处置</action>
<template-output section="routing"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
