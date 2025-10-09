# metric-layer - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/metric-layer/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this metric layer (definitions/slis/ownership)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="术语与口径（反例/边界）">
<action>Work on 术语与口径（反例/边界）</action>
<template-output section="glossary"/>
</step>

<step n="3" goal="公式/窗口/去重">
<action>Work on 公式/窗口/去重</action>
<template-output section="formulas"/>
</step>

<step n="4" goal="溯源（来源表/转换）">
<action>Work on 溯源（来源表/转换）</action>
<template-output section="lineage"/>
</step>

<step n="5" goal="验证规则与阈值">
<action>Work on 验证规则与阈值</action>
<template-output section="validation"/>
</step>

<step n="6" goal="Owner/发布与版本">
<action>Work on owner/发布与版本</action>
<template-output section="ownership"/>
</step>

<step n="7" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
