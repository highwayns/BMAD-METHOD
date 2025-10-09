# feature-store-design - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/feature-store-design/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this feature store design</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="实体/主键/时间列">
<action>Work on 实体/主键/时间列</action>
<template-output section="entities"/>
</step>

<step n="3" goal="特征定义（离线/在线一致）">
<action>Work on 特征定义（离线/在线一致）</action>
<template-output section="feature_defs"/>
</step>

<step n="4" goal="物化/刷新（DT/Tasks/优先级）">
<action>Work on 物化/刷新（dt/tasks/优先级）</action>
<template-output section="materialization"/>
</step>

<step n="5" goal="质量规则与上下界">
<action>Work on 质量规则与上下界</action>
<template-output section="quality"/>
</step>

<step n="6" goal="权限/标签/用途限定">
<action>Work on 权限/标签/用途限定</action>
<template-output section="access"/>
</step>

<step n="7" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
