'''
# `tfe_workspace`

Refer to the Terraform Registory for docs: [`tfe_workspace`](https://www.terraform.io/docs/providers/tfe/r/workspace).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf
import constructs


class Workspace(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-tfe.workspace.Workspace",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/tfe/r/workspace tfe_workspace}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        organization: builtins.str,
        agent_pool_id: typing.Optional[builtins.str] = None,
        allow_destroy_plan: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        assessments_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_apply: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        execution_mode: typing.Optional[builtins.str] = None,
        file_triggers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        global_remote_state: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        operations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        queue_all_runs: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        remote_state_consumer_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        speculative_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ssh_key_id: typing.Optional[builtins.str] = None,
        structured_run_output_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tag_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        terraform_version: typing.Optional[builtins.str] = None,
        trigger_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        trigger_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        vcs_repo: typing.Optional[typing.Union["WorkspaceVcsRepo", typing.Dict[str, typing.Any]]] = None,
        working_directory: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/tfe/r/workspace tfe_workspace} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#name Workspace#name}.
        :param organization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#organization Workspace#organization}.
        :param agent_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#agent_pool_id Workspace#agent_pool_id}.
        :param allow_destroy_plan: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#allow_destroy_plan Workspace#allow_destroy_plan}.
        :param assessments_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#assessments_enabled Workspace#assessments_enabled}.
        :param auto_apply: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#auto_apply Workspace#auto_apply}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#description Workspace#description}.
        :param execution_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#execution_mode Workspace#execution_mode}.
        :param file_triggers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#file_triggers_enabled Workspace#file_triggers_enabled}.
        :param global_remote_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#global_remote_state Workspace#global_remote_state}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#id Workspace#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param operations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#operations Workspace#operations}.
        :param queue_all_runs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#queue_all_runs Workspace#queue_all_runs}.
        :param remote_state_consumer_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#remote_state_consumer_ids Workspace#remote_state_consumer_ids}.
        :param speculative_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#speculative_enabled Workspace#speculative_enabled}.
        :param ssh_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#ssh_key_id Workspace#ssh_key_id}.
        :param structured_run_output_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#structured_run_output_enabled Workspace#structured_run_output_enabled}.
        :param tag_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#tag_names Workspace#tag_names}.
        :param terraform_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#terraform_version Workspace#terraform_version}.
        :param trigger_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#trigger_patterns Workspace#trigger_patterns}.
        :param trigger_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#trigger_prefixes Workspace#trigger_prefixes}.
        :param vcs_repo: vcs_repo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#vcs_repo Workspace#vcs_repo}
        :param working_directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#working_directory Workspace#working_directory}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Workspace.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = WorkspaceConfig(
            name=name,
            organization=organization,
            agent_pool_id=agent_pool_id,
            allow_destroy_plan=allow_destroy_plan,
            assessments_enabled=assessments_enabled,
            auto_apply=auto_apply,
            description=description,
            execution_mode=execution_mode,
            file_triggers_enabled=file_triggers_enabled,
            global_remote_state=global_remote_state,
            id=id,
            operations=operations,
            queue_all_runs=queue_all_runs,
            remote_state_consumer_ids=remote_state_consumer_ids,
            speculative_enabled=speculative_enabled,
            ssh_key_id=ssh_key_id,
            structured_run_output_enabled=structured_run_output_enabled,
            tag_names=tag_names,
            terraform_version=terraform_version,
            trigger_patterns=trigger_patterns,
            trigger_prefixes=trigger_prefixes,
            vcs_repo=vcs_repo,
            working_directory=working_directory,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putVcsRepo")
    def put_vcs_repo(
        self,
        *,
        identifier: builtins.str,
        oauth_token_id: builtins.str,
        branch: typing.Optional[builtins.str] = None,
        ingress_submodules: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags_regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#identifier Workspace#identifier}.
        :param oauth_token_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#oauth_token_id Workspace#oauth_token_id}.
        :param branch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#branch Workspace#branch}.
        :param ingress_submodules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#ingress_submodules Workspace#ingress_submodules}.
        :param tags_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#tags_regex Workspace#tags_regex}.
        '''
        value = WorkspaceVcsRepo(
            identifier=identifier,
            oauth_token_id=oauth_token_id,
            branch=branch,
            ingress_submodules=ingress_submodules,
            tags_regex=tags_regex,
        )

        return typing.cast(None, jsii.invoke(self, "putVcsRepo", [value]))

    @jsii.member(jsii_name="resetAgentPoolId")
    def reset_agent_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAgentPoolId", []))

    @jsii.member(jsii_name="resetAllowDestroyPlan")
    def reset_allow_destroy_plan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowDestroyPlan", []))

    @jsii.member(jsii_name="resetAssessmentsEnabled")
    def reset_assessments_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssessmentsEnabled", []))

    @jsii.member(jsii_name="resetAutoApply")
    def reset_auto_apply(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoApply", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExecutionMode")
    def reset_execution_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutionMode", []))

    @jsii.member(jsii_name="resetFileTriggersEnabled")
    def reset_file_triggers_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileTriggersEnabled", []))

    @jsii.member(jsii_name="resetGlobalRemoteState")
    def reset_global_remote_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlobalRemoteState", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOperations")
    def reset_operations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperations", []))

    @jsii.member(jsii_name="resetQueueAllRuns")
    def reset_queue_all_runs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueueAllRuns", []))

    @jsii.member(jsii_name="resetRemoteStateConsumerIds")
    def reset_remote_state_consumer_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoteStateConsumerIds", []))

    @jsii.member(jsii_name="resetSpeculativeEnabled")
    def reset_speculative_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpeculativeEnabled", []))

    @jsii.member(jsii_name="resetSshKeyId")
    def reset_ssh_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshKeyId", []))

    @jsii.member(jsii_name="resetStructuredRunOutputEnabled")
    def reset_structured_run_output_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStructuredRunOutputEnabled", []))

    @jsii.member(jsii_name="resetTagNames")
    def reset_tag_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagNames", []))

    @jsii.member(jsii_name="resetTerraformVersion")
    def reset_terraform_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerraformVersion", []))

    @jsii.member(jsii_name="resetTriggerPatterns")
    def reset_trigger_patterns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggerPatterns", []))

    @jsii.member(jsii_name="resetTriggerPrefixes")
    def reset_trigger_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggerPrefixes", []))

    @jsii.member(jsii_name="resetVcsRepo")
    def reset_vcs_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVcsRepo", []))

    @jsii.member(jsii_name="resetWorkingDirectory")
    def reset_working_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkingDirectory", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="vcsRepo")
    def vcs_repo(self) -> "WorkspaceVcsRepoOutputReference":
        return typing.cast("WorkspaceVcsRepoOutputReference", jsii.get(self, "vcsRepo"))

    @builtins.property
    @jsii.member(jsii_name="agentPoolIdInput")
    def agent_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "agentPoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="allowDestroyPlanInput")
    def allow_destroy_plan_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowDestroyPlanInput"))

    @builtins.property
    @jsii.member(jsii_name="assessmentsEnabledInput")
    def assessments_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "assessmentsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="autoApplyInput")
    def auto_apply_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoApplyInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="executionModeInput")
    def execution_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="fileTriggersEnabledInput")
    def file_triggers_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fileTriggersEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="globalRemoteStateInput")
    def global_remote_state_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "globalRemoteStateInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="operationsInput")
    def operations_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "operationsInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationInput")
    def organization_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationInput"))

    @builtins.property
    @jsii.member(jsii_name="queueAllRunsInput")
    def queue_all_runs_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "queueAllRunsInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteStateConsumerIdsInput")
    def remote_state_consumer_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "remoteStateConsumerIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="speculativeEnabledInput")
    def speculative_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "speculativeEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="sshKeyIdInput")
    def ssh_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sshKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="structuredRunOutputEnabledInput")
    def structured_run_output_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "structuredRunOutputEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="tagNamesInput")
    def tag_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="terraformVersionInput")
    def terraform_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "terraformVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerPatternsInput")
    def trigger_patterns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "triggerPatternsInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerPrefixesInput")
    def trigger_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "triggerPrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="vcsRepoInput")
    def vcs_repo_input(self) -> typing.Optional["WorkspaceVcsRepo"]:
        return typing.cast(typing.Optional["WorkspaceVcsRepo"], jsii.get(self, "vcsRepoInput"))

    @builtins.property
    @jsii.member(jsii_name="workingDirectoryInput")
    def working_directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workingDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="agentPoolId")
    def agent_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "agentPoolId"))

    @agent_pool_id.setter
    def agent_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "agent_pool_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentPoolId", value)

    @builtins.property
    @jsii.member(jsii_name="allowDestroyPlan")
    def allow_destroy_plan(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowDestroyPlan"))

    @allow_destroy_plan.setter
    def allow_destroy_plan(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "allow_destroy_plan").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowDestroyPlan", value)

    @builtins.property
    @jsii.member(jsii_name="assessmentsEnabled")
    def assessments_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "assessmentsEnabled"))

    @assessments_enabled.setter
    def assessments_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "assessments_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assessmentsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="autoApply")
    def auto_apply(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoApply"))

    @auto_apply.setter
    def auto_apply(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "auto_apply").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoApply", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="executionMode")
    def execution_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionMode"))

    @execution_mode.setter
    def execution_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "execution_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionMode", value)

    @builtins.property
    @jsii.member(jsii_name="fileTriggersEnabled")
    def file_triggers_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fileTriggersEnabled"))

    @file_triggers_enabled.setter
    def file_triggers_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "file_triggers_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileTriggersEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="globalRemoteState")
    def global_remote_state(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "globalRemoteState"))

    @global_remote_state.setter
    def global_remote_state(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "global_remote_state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalRemoteState", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="operations")
    def operations(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "operations"))

    @operations.setter
    def operations(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "operations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operations", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "organization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="queueAllRuns")
    def queue_all_runs(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "queueAllRuns"))

    @queue_all_runs.setter
    def queue_all_runs(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "queue_all_runs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queueAllRuns", value)

    @builtins.property
    @jsii.member(jsii_name="remoteStateConsumerIds")
    def remote_state_consumer_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "remoteStateConsumerIds"))

    @remote_state_consumer_ids.setter
    def remote_state_consumer_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "remote_state_consumer_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteStateConsumerIds", value)

    @builtins.property
    @jsii.member(jsii_name="speculativeEnabled")
    def speculative_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "speculativeEnabled"))

    @speculative_enabled.setter
    def speculative_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "speculative_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "speculativeEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="sshKeyId")
    def ssh_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sshKeyId"))

    @ssh_key_id.setter
    def ssh_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "ssh_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="structuredRunOutputEnabled")
    def structured_run_output_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "structuredRunOutputEnabled"))

    @structured_run_output_enabled.setter
    def structured_run_output_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "structured_run_output_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "structuredRunOutputEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="tagNames")
    def tag_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tagNames"))

    @tag_names.setter
    def tag_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "tag_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagNames", value)

    @builtins.property
    @jsii.member(jsii_name="terraformVersion")
    def terraform_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "terraformVersion"))

    @terraform_version.setter
    def terraform_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "terraform_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformVersion", value)

    @builtins.property
    @jsii.member(jsii_name="triggerPatterns")
    def trigger_patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "triggerPatterns"))

    @trigger_patterns.setter
    def trigger_patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "trigger_patterns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggerPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="triggerPrefixes")
    def trigger_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "triggerPrefixes"))

    @trigger_prefixes.setter
    def trigger_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "trigger_prefixes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggerPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="workingDirectory")
    def working_directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workingDirectory"))

    @working_directory.setter
    def working_directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Workspace, "working_directory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workingDirectory", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-tfe.workspace.WorkspaceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "organization": "organization",
        "agent_pool_id": "agentPoolId",
        "allow_destroy_plan": "allowDestroyPlan",
        "assessments_enabled": "assessmentsEnabled",
        "auto_apply": "autoApply",
        "description": "description",
        "execution_mode": "executionMode",
        "file_triggers_enabled": "fileTriggersEnabled",
        "global_remote_state": "globalRemoteState",
        "id": "id",
        "operations": "operations",
        "queue_all_runs": "queueAllRuns",
        "remote_state_consumer_ids": "remoteStateConsumerIds",
        "speculative_enabled": "speculativeEnabled",
        "ssh_key_id": "sshKeyId",
        "structured_run_output_enabled": "structuredRunOutputEnabled",
        "tag_names": "tagNames",
        "terraform_version": "terraformVersion",
        "trigger_patterns": "triggerPatterns",
        "trigger_prefixes": "triggerPrefixes",
        "vcs_repo": "vcsRepo",
        "working_directory": "workingDirectory",
    },
)
class WorkspaceConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        name: builtins.str,
        organization: builtins.str,
        agent_pool_id: typing.Optional[builtins.str] = None,
        allow_destroy_plan: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        assessments_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_apply: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        execution_mode: typing.Optional[builtins.str] = None,
        file_triggers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        global_remote_state: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        operations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        queue_all_runs: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        remote_state_consumer_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        speculative_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ssh_key_id: typing.Optional[builtins.str] = None,
        structured_run_output_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tag_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        terraform_version: typing.Optional[builtins.str] = None,
        trigger_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        trigger_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        vcs_repo: typing.Optional[typing.Union["WorkspaceVcsRepo", typing.Dict[str, typing.Any]]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#name Workspace#name}.
        :param organization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#organization Workspace#organization}.
        :param agent_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#agent_pool_id Workspace#agent_pool_id}.
        :param allow_destroy_plan: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#allow_destroy_plan Workspace#allow_destroy_plan}.
        :param assessments_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#assessments_enabled Workspace#assessments_enabled}.
        :param auto_apply: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#auto_apply Workspace#auto_apply}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#description Workspace#description}.
        :param execution_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#execution_mode Workspace#execution_mode}.
        :param file_triggers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#file_triggers_enabled Workspace#file_triggers_enabled}.
        :param global_remote_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#global_remote_state Workspace#global_remote_state}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#id Workspace#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param operations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#operations Workspace#operations}.
        :param queue_all_runs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#queue_all_runs Workspace#queue_all_runs}.
        :param remote_state_consumer_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#remote_state_consumer_ids Workspace#remote_state_consumer_ids}.
        :param speculative_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#speculative_enabled Workspace#speculative_enabled}.
        :param ssh_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#ssh_key_id Workspace#ssh_key_id}.
        :param structured_run_output_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#structured_run_output_enabled Workspace#structured_run_output_enabled}.
        :param tag_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#tag_names Workspace#tag_names}.
        :param terraform_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#terraform_version Workspace#terraform_version}.
        :param trigger_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#trigger_patterns Workspace#trigger_patterns}.
        :param trigger_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#trigger_prefixes Workspace#trigger_prefixes}.
        :param vcs_repo: vcs_repo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#vcs_repo Workspace#vcs_repo}
        :param working_directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#working_directory Workspace#working_directory}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(vcs_repo, dict):
            vcs_repo = WorkspaceVcsRepo(**vcs_repo)
        if __debug__:
            type_hints = typing.get_type_hints(WorkspaceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument agent_pool_id", value=agent_pool_id, expected_type=type_hints["agent_pool_id"])
            check_type(argname="argument allow_destroy_plan", value=allow_destroy_plan, expected_type=type_hints["allow_destroy_plan"])
            check_type(argname="argument assessments_enabled", value=assessments_enabled, expected_type=type_hints["assessments_enabled"])
            check_type(argname="argument auto_apply", value=auto_apply, expected_type=type_hints["auto_apply"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument execution_mode", value=execution_mode, expected_type=type_hints["execution_mode"])
            check_type(argname="argument file_triggers_enabled", value=file_triggers_enabled, expected_type=type_hints["file_triggers_enabled"])
            check_type(argname="argument global_remote_state", value=global_remote_state, expected_type=type_hints["global_remote_state"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument operations", value=operations, expected_type=type_hints["operations"])
            check_type(argname="argument queue_all_runs", value=queue_all_runs, expected_type=type_hints["queue_all_runs"])
            check_type(argname="argument remote_state_consumer_ids", value=remote_state_consumer_ids, expected_type=type_hints["remote_state_consumer_ids"])
            check_type(argname="argument speculative_enabled", value=speculative_enabled, expected_type=type_hints["speculative_enabled"])
            check_type(argname="argument ssh_key_id", value=ssh_key_id, expected_type=type_hints["ssh_key_id"])
            check_type(argname="argument structured_run_output_enabled", value=structured_run_output_enabled, expected_type=type_hints["structured_run_output_enabled"])
            check_type(argname="argument tag_names", value=tag_names, expected_type=type_hints["tag_names"])
            check_type(argname="argument terraform_version", value=terraform_version, expected_type=type_hints["terraform_version"])
            check_type(argname="argument trigger_patterns", value=trigger_patterns, expected_type=type_hints["trigger_patterns"])
            check_type(argname="argument trigger_prefixes", value=trigger_prefixes, expected_type=type_hints["trigger_prefixes"])
            check_type(argname="argument vcs_repo", value=vcs_repo, expected_type=type_hints["vcs_repo"])
            check_type(argname="argument working_directory", value=working_directory, expected_type=type_hints["working_directory"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "organization": organization,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if agent_pool_id is not None:
            self._values["agent_pool_id"] = agent_pool_id
        if allow_destroy_plan is not None:
            self._values["allow_destroy_plan"] = allow_destroy_plan
        if assessments_enabled is not None:
            self._values["assessments_enabled"] = assessments_enabled
        if auto_apply is not None:
            self._values["auto_apply"] = auto_apply
        if description is not None:
            self._values["description"] = description
        if execution_mode is not None:
            self._values["execution_mode"] = execution_mode
        if file_triggers_enabled is not None:
            self._values["file_triggers_enabled"] = file_triggers_enabled
        if global_remote_state is not None:
            self._values["global_remote_state"] = global_remote_state
        if id is not None:
            self._values["id"] = id
        if operations is not None:
            self._values["operations"] = operations
        if queue_all_runs is not None:
            self._values["queue_all_runs"] = queue_all_runs
        if remote_state_consumer_ids is not None:
            self._values["remote_state_consumer_ids"] = remote_state_consumer_ids
        if speculative_enabled is not None:
            self._values["speculative_enabled"] = speculative_enabled
        if ssh_key_id is not None:
            self._values["ssh_key_id"] = ssh_key_id
        if structured_run_output_enabled is not None:
            self._values["structured_run_output_enabled"] = structured_run_output_enabled
        if tag_names is not None:
            self._values["tag_names"] = tag_names
        if terraform_version is not None:
            self._values["terraform_version"] = terraform_version
        if trigger_patterns is not None:
            self._values["trigger_patterns"] = trigger_patterns
        if trigger_prefixes is not None:
            self._values["trigger_prefixes"] = trigger_prefixes
        if vcs_repo is not None:
            self._values["vcs_repo"] = vcs_repo
        if working_directory is not None:
            self._values["working_directory"] = working_directory

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#name Workspace#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def organization(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#organization Workspace#organization}.'''
        result = self._values.get("organization")
        assert result is not None, "Required property 'organization' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#agent_pool_id Workspace#agent_pool_id}.'''
        result = self._values.get("agent_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def allow_destroy_plan(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#allow_destroy_plan Workspace#allow_destroy_plan}.'''
        result = self._values.get("allow_destroy_plan")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def assessments_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#assessments_enabled Workspace#assessments_enabled}.'''
        result = self._values.get("assessments_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auto_apply(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#auto_apply Workspace#auto_apply}.'''
        result = self._values.get("auto_apply")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#description Workspace#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#execution_mode Workspace#execution_mode}.'''
        result = self._values.get("execution_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_triggers_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#file_triggers_enabled Workspace#file_triggers_enabled}.'''
        result = self._values.get("file_triggers_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def global_remote_state(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#global_remote_state Workspace#global_remote_state}.'''
        result = self._values.get("global_remote_state")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#id Workspace#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operations(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#operations Workspace#operations}.'''
        result = self._values.get("operations")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def queue_all_runs(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#queue_all_runs Workspace#queue_all_runs}.'''
        result = self._values.get("queue_all_runs")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def remote_state_consumer_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#remote_state_consumer_ids Workspace#remote_state_consumer_ids}.'''
        result = self._values.get("remote_state_consumer_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def speculative_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#speculative_enabled Workspace#speculative_enabled}.'''
        result = self._values.get("speculative_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ssh_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#ssh_key_id Workspace#ssh_key_id}.'''
        result = self._values.get("ssh_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def structured_run_output_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#structured_run_output_enabled Workspace#structured_run_output_enabled}.'''
        result = self._values.get("structured_run_output_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tag_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#tag_names Workspace#tag_names}.'''
        result = self._values.get("tag_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def terraform_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#terraform_version Workspace#terraform_version}.'''
        result = self._values.get("terraform_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trigger_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#trigger_patterns Workspace#trigger_patterns}.'''
        result = self._values.get("trigger_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def trigger_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#trigger_prefixes Workspace#trigger_prefixes}.'''
        result = self._values.get("trigger_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def vcs_repo(self) -> typing.Optional["WorkspaceVcsRepo"]:
        '''vcs_repo block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#vcs_repo Workspace#vcs_repo}
        '''
        result = self._values.get("vcs_repo")
        return typing.cast(typing.Optional["WorkspaceVcsRepo"], result)

    @builtins.property
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#working_directory Workspace#working_directory}.'''
        result = self._values.get("working_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkspaceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-tfe.workspace.WorkspaceVcsRepo",
    jsii_struct_bases=[],
    name_mapping={
        "identifier": "identifier",
        "oauth_token_id": "oauthTokenId",
        "branch": "branch",
        "ingress_submodules": "ingressSubmodules",
        "tags_regex": "tagsRegex",
    },
)
class WorkspaceVcsRepo:
    def __init__(
        self,
        *,
        identifier: builtins.str,
        oauth_token_id: builtins.str,
        branch: typing.Optional[builtins.str] = None,
        ingress_submodules: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags_regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#identifier Workspace#identifier}.
        :param oauth_token_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#oauth_token_id Workspace#oauth_token_id}.
        :param branch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#branch Workspace#branch}.
        :param ingress_submodules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#ingress_submodules Workspace#ingress_submodules}.
        :param tags_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#tags_regex Workspace#tags_regex}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkspaceVcsRepo.__init__)
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
            check_type(argname="argument oauth_token_id", value=oauth_token_id, expected_type=type_hints["oauth_token_id"])
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument ingress_submodules", value=ingress_submodules, expected_type=type_hints["ingress_submodules"])
            check_type(argname="argument tags_regex", value=tags_regex, expected_type=type_hints["tags_regex"])
        self._values: typing.Dict[str, typing.Any] = {
            "identifier": identifier,
            "oauth_token_id": oauth_token_id,
        }
        if branch is not None:
            self._values["branch"] = branch
        if ingress_submodules is not None:
            self._values["ingress_submodules"] = ingress_submodules
        if tags_regex is not None:
            self._values["tags_regex"] = tags_regex

    @builtins.property
    def identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#identifier Workspace#identifier}.'''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oauth_token_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#oauth_token_id Workspace#oauth_token_id}.'''
        result = self._values.get("oauth_token_id")
        assert result is not None, "Required property 'oauth_token_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#branch Workspace#branch}.'''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingress_submodules(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#ingress_submodules Workspace#ingress_submodules}.'''
        result = self._values.get("ingress_submodules")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags_regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/workspace#tags_regex Workspace#tags_regex}.'''
        result = self._values.get("tags_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkspaceVcsRepo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkspaceVcsRepoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-tfe.workspace.WorkspaceVcsRepoOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkspaceVcsRepoOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetIngressSubmodules")
    def reset_ingress_submodules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressSubmodules", []))

    @jsii.member(jsii_name="resetTagsRegex")
    def reset_tags_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsRegex", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="identifierInput")
    def identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identifierInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressSubmodulesInput")
    def ingress_submodules_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ingressSubmodulesInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthTokenIdInput")
    def oauth_token_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthTokenIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsRegexInput")
    def tags_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagsRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkspaceVcsRepoOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="identifier")
    def identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identifier"))

    @identifier.setter
    def identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkspaceVcsRepoOutputReference, "identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identifier", value)

    @builtins.property
    @jsii.member(jsii_name="ingressSubmodules")
    def ingress_submodules(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ingressSubmodules"))

    @ingress_submodules.setter
    def ingress_submodules(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkspaceVcsRepoOutputReference, "ingress_submodules").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressSubmodules", value)

    @builtins.property
    @jsii.member(jsii_name="oauthTokenId")
    def oauth_token_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauthTokenId"))

    @oauth_token_id.setter
    def oauth_token_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkspaceVcsRepoOutputReference, "oauth_token_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthTokenId", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRegex")
    def tags_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagsRegex"))

    @tags_regex.setter
    def tags_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkspaceVcsRepoOutputReference, "tags_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRegex", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WorkspaceVcsRepo]:
        return typing.cast(typing.Optional[WorkspaceVcsRepo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[WorkspaceVcsRepo]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkspaceVcsRepoOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Workspace",
    "WorkspaceConfig",
    "WorkspaceVcsRepo",
    "WorkspaceVcsRepoOutputReference",
]

publication.publish()
