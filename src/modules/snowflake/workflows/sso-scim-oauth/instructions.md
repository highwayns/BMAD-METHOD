# sso-scim-oauth - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/sso-scim-oauth/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this identity federation (sso/scim/oauth)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="SAML/OIDC 配置与映射">
<action>Work on saml/oidc 配置与映射</action>
<template-output section="sso"/>
</step>

<step n="3" goal="SCIM 供应与生命周期">
<action>Work on scim 供应与生命周期</action>
<template-output section="scim"/>
</step>

<step n="4" goal="OAuth 客户端与权限范围">
<action>Work on oauth 客户端与权限范围</action>
<template-output section="oauth"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
