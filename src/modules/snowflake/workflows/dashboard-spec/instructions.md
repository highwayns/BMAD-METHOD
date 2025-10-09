# dashboard-spec - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/dashboard-spec/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this dashboard spec (stories/wireframes/acceptance)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="数据故事与关键问题">
<action>Work on 数据故事与关键问题</action>
<template-output section="stories"/>
</step>

<step n="3" goal="线框稿与交互（筛选/下钻/联动）">
<action>Work on 线框稿与交互（筛选/下钻/联动）</action>
<template-output section="wireframes"/>
</step>

<step n="4" goal="指标与图表（来源与刷新）">
<action>Work on 指标与图表（来源与刷新）</action>
<template-output section="metrics"/>
</step>

<step n="5" goal="权限与脱敏">
<action>Work on 权限与脱敏</action>
<template-output section="permissions"/>
</step>

<step n="6" goal="验收脚本与判定">
<action>Work on 验收脚本与判定</action>
<template-output section="acceptance"/>
</step>

<step n="7" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
