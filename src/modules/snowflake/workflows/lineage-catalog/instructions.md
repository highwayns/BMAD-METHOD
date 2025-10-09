# lineage-catalog - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/lineage-catalog/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this lineage & catalog integration</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="元数据/Owner/标签/保留">
<action>Work on 元数据/owner/标签/保留</action>
<template-output section="catalog"/>
</step>

<step n="3" goal="字段级血缘与事件传播">
<action>Work on 字段级血缘与事件传播</action>
<template-output section="lineage"/>
</step>

<step n="4" goal="与 Catalog/BI/ML 集成">
<action>Work on 与 catalog/bi/ml 集成</action>
<template-output section="integration"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
