# cost-attribution-tags - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/cost-attribution-tags/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this cost attribution (tags/roles/warehouses/projects)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="标签分类法与命名">
<action>Work on 标签分类法与命名</action>
<template-output section="taxonomy"/>
</step>

<step n="3" goal="归属在对象/作业/视图传播">
<action>Work on 归属在对象/作业/视图传播</action>
<template-output section="propagation"/>
</step>

<step n="4" goal="报表/对账与签字">
<action>Work on 报表/对账与签字</action>
<template-output section="reports"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
