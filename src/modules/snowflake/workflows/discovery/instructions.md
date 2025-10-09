# discovery - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/discovery/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this product discovery (ba)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="机会与业务问题">
<action>Work on 机会与业务问题</action>
<template-output section="opportunity"/>
</step>

<step n="3" goal="价值地图与衡量">
<action>Work on 价值地图与衡量</action>
<template-output section="value-map"/>
</step>

<step n="4" goal="业务流程（AS-IS/TO-BE）">
<action>Work on 业务流程（as-is/to-be）</action>
<template-output section="process"/>
</step>

<step n="5" goal="数据源与约束">
<action>Work on 数据源与约束</action>
<template-output section="data-sources"/>
</step>

<step n="6" goal="风险与依赖">
<action>Work on 风险与依赖</action>
<template-output section="risks"/>
</step>

<step n="7" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
