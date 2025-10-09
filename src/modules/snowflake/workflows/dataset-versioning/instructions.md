# dataset-versioning - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/dataset-versioning/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this dataset versioning strategy</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="快照策略（日期/增量/回补）">
<action>Work on 快照策略（日期/增量/回补）</action>
<template-output section="snapshots"/>
</step>

<step n="3" goal="可复现（种子/随机性/环境）">
<action>Work on 可复现（种子/随机性/环境）</action>
<template-output section="reproducibility"/>
</step>

<step n="4" goal="血缘与口径变更记录">
<action>Work on 血缘与口径变更记录</action>
<template-output section="lineage"/>
</step>

<step n="5" goal="存储/保留/加密">
<action>Work on 存储/保留/加密</action>
<template-output section="storage"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
