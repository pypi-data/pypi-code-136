'''
# `azurerm_logic_app_workflow`

Refer to the Terraform Registory for docs: [`azurerm_logic_app_workflow`](https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow).
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


class LogicAppWorkflow(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflow",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow azurerm_logic_app_workflow}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        access_control: typing.Optional[typing.Union["LogicAppWorkflowAccessControl", typing.Dict[str, typing.Any]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["LogicAppWorkflowIdentity", typing.Dict[str, typing.Any]]] = None,
        integration_service_environment_id: typing.Optional[builtins.str] = None,
        logic_app_integration_account_id: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["LogicAppWorkflowTimeouts", typing.Dict[str, typing.Any]]] = None,
        workflow_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        workflow_schema: typing.Optional[builtins.str] = None,
        workflow_version: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow azurerm_logic_app_workflow} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#location LogicAppWorkflow#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#name LogicAppWorkflow#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#resource_group_name LogicAppWorkflow#resource_group_name}.
        :param access_control: access_control block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#access_control LogicAppWorkflow#access_control}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#enabled LogicAppWorkflow#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#id LogicAppWorkflow#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#identity LogicAppWorkflow#identity}
        :param integration_service_environment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#integration_service_environment_id LogicAppWorkflow#integration_service_environment_id}.
        :param logic_app_integration_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#logic_app_integration_account_id LogicAppWorkflow#logic_app_integration_account_id}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#parameters LogicAppWorkflow#parameters}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#tags LogicAppWorkflow#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#timeouts LogicAppWorkflow#timeouts}
        :param workflow_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#workflow_parameters LogicAppWorkflow#workflow_parameters}.
        :param workflow_schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#workflow_schema LogicAppWorkflow#workflow_schema}.
        :param workflow_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#workflow_version LogicAppWorkflow#workflow_version}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflow.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LogicAppWorkflowConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            access_control=access_control,
            enabled=enabled,
            id=id,
            identity=identity,
            integration_service_environment_id=integration_service_environment_id,
            logic_app_integration_account_id=logic_app_integration_account_id,
            parameters=parameters,
            tags=tags,
            timeouts=timeouts,
            workflow_parameters=workflow_parameters,
            workflow_schema=workflow_schema,
            workflow_version=workflow_version,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAccessControl")
    def put_access_control(
        self,
        *,
        action: typing.Optional[typing.Union["LogicAppWorkflowAccessControlAction", typing.Dict[str, typing.Any]]] = None,
        content: typing.Optional[typing.Union["LogicAppWorkflowAccessControlContent", typing.Dict[str, typing.Any]]] = None,
        trigger: typing.Optional[typing.Union["LogicAppWorkflowAccessControlTrigger", typing.Dict[str, typing.Any]]] = None,
        workflow_management: typing.Optional[typing.Union["LogicAppWorkflowAccessControlWorkflowManagement", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#action LogicAppWorkflow#action}
        :param content: content block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#content LogicAppWorkflow#content}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#trigger LogicAppWorkflow#trigger}
        :param workflow_management: workflow_management block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#workflow_management LogicAppWorkflow#workflow_management}
        '''
        value = LogicAppWorkflowAccessControl(
            action=action,
            content=content,
            trigger=trigger,
            workflow_management=workflow_management,
        )

        return typing.cast(None, jsii.invoke(self, "putAccessControl", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#type LogicAppWorkflow#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#identity_ids LogicAppWorkflow#identity_ids}.
        '''
        value = LogicAppWorkflowIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#create LogicAppWorkflow#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#delete LogicAppWorkflow#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#read LogicAppWorkflow#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#update LogicAppWorkflow#update}.
        '''
        value = LogicAppWorkflowTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAccessControl")
    def reset_access_control(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessControl", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetIntegrationServiceEnvironmentId")
    def reset_integration_service_environment_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntegrationServiceEnvironmentId", []))

    @jsii.member(jsii_name="resetLogicAppIntegrationAccountId")
    def reset_logic_app_integration_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogicAppIntegrationAccountId", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWorkflowParameters")
    def reset_workflow_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkflowParameters", []))

    @jsii.member(jsii_name="resetWorkflowSchema")
    def reset_workflow_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkflowSchema", []))

    @jsii.member(jsii_name="resetWorkflowVersion")
    def reset_workflow_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkflowVersion", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accessControl")
    def access_control(self) -> "LogicAppWorkflowAccessControlOutputReference":
        return typing.cast("LogicAppWorkflowAccessControlOutputReference", jsii.get(self, "accessControl"))

    @builtins.property
    @jsii.member(jsii_name="accessEndpoint")
    def access_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="connectorEndpointIpAddresses")
    def connector_endpoint_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "connectorEndpointIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="connectorOutboundIpAddresses")
    def connector_outbound_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "connectorOutboundIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "LogicAppWorkflowIdentityOutputReference":
        return typing.cast("LogicAppWorkflowIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LogicAppWorkflowTimeoutsOutputReference":
        return typing.cast("LogicAppWorkflowTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="workflowEndpointIpAddresses")
    def workflow_endpoint_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "workflowEndpointIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="workflowOutboundIpAddresses")
    def workflow_outbound_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "workflowOutboundIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="accessControlInput")
    def access_control_input(self) -> typing.Optional["LogicAppWorkflowAccessControl"]:
        return typing.cast(typing.Optional["LogicAppWorkflowAccessControl"], jsii.get(self, "accessControlInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["LogicAppWorkflowIdentity"]:
        return typing.cast(typing.Optional["LogicAppWorkflowIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationServiceEnvironmentIdInput")
    def integration_service_environment_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationServiceEnvironmentIdInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="logicAppIntegrationAccountIdInput")
    def logic_app_integration_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logicAppIntegrationAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LogicAppWorkflowTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LogicAppWorkflowTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="workflowParametersInput")
    def workflow_parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "workflowParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="workflowSchemaInput")
    def workflow_schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workflowSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="workflowVersionInput")
    def workflow_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workflowVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflow, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflow, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="integrationServiceEnvironmentId")
    def integration_service_environment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "integrationServiceEnvironmentId"))

    @integration_service_environment_id.setter
    def integration_service_environment_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflow, "integration_service_environment_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationServiceEnvironmentId", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflow, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="logicAppIntegrationAccountId")
    def logic_app_integration_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logicAppIntegrationAccountId"))

    @logic_app_integration_account_id.setter
    def logic_app_integration_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflow, "logic_app_integration_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logicAppIntegrationAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflow, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflow, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflow, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflow, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="workflowParameters")
    def workflow_parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "workflowParameters"))

    @workflow_parameters.setter
    def workflow_parameters(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflow, "workflow_parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workflowParameters", value)

    @builtins.property
    @jsii.member(jsii_name="workflowSchema")
    def workflow_schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workflowSchema"))

    @workflow_schema.setter
    def workflow_schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflow, "workflow_schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workflowSchema", value)

    @builtins.property
    @jsii.member(jsii_name="workflowVersion")
    def workflow_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workflowVersion"))

    @workflow_version.setter
    def workflow_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflow, "workflow_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workflowVersion", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowAccessControl",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "content": "content",
        "trigger": "trigger",
        "workflow_management": "workflowManagement",
    },
)
class LogicAppWorkflowAccessControl:
    def __init__(
        self,
        *,
        action: typing.Optional[typing.Union["LogicAppWorkflowAccessControlAction", typing.Dict[str, typing.Any]]] = None,
        content: typing.Optional[typing.Union["LogicAppWorkflowAccessControlContent", typing.Dict[str, typing.Any]]] = None,
        trigger: typing.Optional[typing.Union["LogicAppWorkflowAccessControlTrigger", typing.Dict[str, typing.Any]]] = None,
        workflow_management: typing.Optional[typing.Union["LogicAppWorkflowAccessControlWorkflowManagement", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#action LogicAppWorkflow#action}
        :param content: content block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#content LogicAppWorkflow#content}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#trigger LogicAppWorkflow#trigger}
        :param workflow_management: workflow_management block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#workflow_management LogicAppWorkflow#workflow_management}
        '''
        if isinstance(action, dict):
            action = LogicAppWorkflowAccessControlAction(**action)
        if isinstance(content, dict):
            content = LogicAppWorkflowAccessControlContent(**content)
        if isinstance(trigger, dict):
            trigger = LogicAppWorkflowAccessControlTrigger(**trigger)
        if isinstance(workflow_management, dict):
            workflow_management = LogicAppWorkflowAccessControlWorkflowManagement(**workflow_management)
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControl.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
            check_type(argname="argument workflow_management", value=workflow_management, expected_type=type_hints["workflow_management"])
        self._values: typing.Dict[str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if content is not None:
            self._values["content"] = content
        if trigger is not None:
            self._values["trigger"] = trigger
        if workflow_management is not None:
            self._values["workflow_management"] = workflow_management

    @builtins.property
    def action(self) -> typing.Optional["LogicAppWorkflowAccessControlAction"]:
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#action LogicAppWorkflow#action}
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional["LogicAppWorkflowAccessControlAction"], result)

    @builtins.property
    def content(self) -> typing.Optional["LogicAppWorkflowAccessControlContent"]:
        '''content block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#content LogicAppWorkflow#content}
        '''
        result = self._values.get("content")
        return typing.cast(typing.Optional["LogicAppWorkflowAccessControlContent"], result)

    @builtins.property
    def trigger(self) -> typing.Optional["LogicAppWorkflowAccessControlTrigger"]:
        '''trigger block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#trigger LogicAppWorkflow#trigger}
        '''
        result = self._values.get("trigger")
        return typing.cast(typing.Optional["LogicAppWorkflowAccessControlTrigger"], result)

    @builtins.property
    def workflow_management(
        self,
    ) -> typing.Optional["LogicAppWorkflowAccessControlWorkflowManagement"]:
        '''workflow_management block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#workflow_management LogicAppWorkflow#workflow_management}
        '''
        result = self._values.get("workflow_management")
        return typing.cast(typing.Optional["LogicAppWorkflowAccessControlWorkflowManagement"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppWorkflowAccessControl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowAccessControlAction",
    jsii_struct_bases=[],
    name_mapping={"allowed_caller_ip_address_range": "allowedCallerIpAddressRange"},
)
class LogicAppWorkflowAccessControlAction:
    def __init__(
        self,
        *,
        allowed_caller_ip_address_range: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param allowed_caller_ip_address_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#allowed_caller_ip_address_range LogicAppWorkflow#allowed_caller_ip_address_range}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlAction.__init__)
            check_type(argname="argument allowed_caller_ip_address_range", value=allowed_caller_ip_address_range, expected_type=type_hints["allowed_caller_ip_address_range"])
        self._values: typing.Dict[str, typing.Any] = {
            "allowed_caller_ip_address_range": allowed_caller_ip_address_range,
        }

    @builtins.property
    def allowed_caller_ip_address_range(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#allowed_caller_ip_address_range LogicAppWorkflow#allowed_caller_ip_address_range}.'''
        result = self._values.get("allowed_caller_ip_address_range")
        assert result is not None, "Required property 'allowed_caller_ip_address_range' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppWorkflowAccessControlAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogicAppWorkflowAccessControlActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowAccessControlActionOutputReference",
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
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="allowedCallerIpAddressRangeInput")
    def allowed_caller_ip_address_range_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedCallerIpAddressRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedCallerIpAddressRange")
    def allowed_caller_ip_address_range(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedCallerIpAddressRange"))

    @allowed_caller_ip_address_range.setter
    def allowed_caller_ip_address_range(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlActionOutputReference, "allowed_caller_ip_address_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedCallerIpAddressRange", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LogicAppWorkflowAccessControlAction]:
        return typing.cast(typing.Optional[LogicAppWorkflowAccessControlAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogicAppWorkflowAccessControlAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowAccessControlContent",
    jsii_struct_bases=[],
    name_mapping={"allowed_caller_ip_address_range": "allowedCallerIpAddressRange"},
)
class LogicAppWorkflowAccessControlContent:
    def __init__(
        self,
        *,
        allowed_caller_ip_address_range: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param allowed_caller_ip_address_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#allowed_caller_ip_address_range LogicAppWorkflow#allowed_caller_ip_address_range}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlContent.__init__)
            check_type(argname="argument allowed_caller_ip_address_range", value=allowed_caller_ip_address_range, expected_type=type_hints["allowed_caller_ip_address_range"])
        self._values: typing.Dict[str, typing.Any] = {
            "allowed_caller_ip_address_range": allowed_caller_ip_address_range,
        }

    @builtins.property
    def allowed_caller_ip_address_range(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#allowed_caller_ip_address_range LogicAppWorkflow#allowed_caller_ip_address_range}.'''
        result = self._values.get("allowed_caller_ip_address_range")
        assert result is not None, "Required property 'allowed_caller_ip_address_range' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppWorkflowAccessControlContent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogicAppWorkflowAccessControlContentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowAccessControlContentOutputReference",
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
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlContentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="allowedCallerIpAddressRangeInput")
    def allowed_caller_ip_address_range_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedCallerIpAddressRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedCallerIpAddressRange")
    def allowed_caller_ip_address_range(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedCallerIpAddressRange"))

    @allowed_caller_ip_address_range.setter
    def allowed_caller_ip_address_range(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlContentOutputReference, "allowed_caller_ip_address_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedCallerIpAddressRange", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LogicAppWorkflowAccessControlContent]:
        return typing.cast(typing.Optional[LogicAppWorkflowAccessControlContent], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogicAppWorkflowAccessControlContent],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlContentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogicAppWorkflowAccessControlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowAccessControlOutputReference",
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
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        allowed_caller_ip_address_range: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param allowed_caller_ip_address_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#allowed_caller_ip_address_range LogicAppWorkflow#allowed_caller_ip_address_range}.
        '''
        value = LogicAppWorkflowAccessControlAction(
            allowed_caller_ip_address_range=allowed_caller_ip_address_range
        )

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putContent")
    def put_content(
        self,
        *,
        allowed_caller_ip_address_range: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param allowed_caller_ip_address_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#allowed_caller_ip_address_range LogicAppWorkflow#allowed_caller_ip_address_range}.
        '''
        value = LogicAppWorkflowAccessControlContent(
            allowed_caller_ip_address_range=allowed_caller_ip_address_range
        )

        return typing.cast(None, jsii.invoke(self, "putContent", [value]))

    @jsii.member(jsii_name="putTrigger")
    def put_trigger(
        self,
        *,
        allowed_caller_ip_address_range: typing.Sequence[builtins.str],
        open_authentication_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicy", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param allowed_caller_ip_address_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#allowed_caller_ip_address_range LogicAppWorkflow#allowed_caller_ip_address_range}.
        :param open_authentication_policy: open_authentication_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#open_authentication_policy LogicAppWorkflow#open_authentication_policy}
        '''
        value = LogicAppWorkflowAccessControlTrigger(
            allowed_caller_ip_address_range=allowed_caller_ip_address_range,
            open_authentication_policy=open_authentication_policy,
        )

        return typing.cast(None, jsii.invoke(self, "putTrigger", [value]))

    @jsii.member(jsii_name="putWorkflowManagement")
    def put_workflow_management(
        self,
        *,
        allowed_caller_ip_address_range: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param allowed_caller_ip_address_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#allowed_caller_ip_address_range LogicAppWorkflow#allowed_caller_ip_address_range}.
        '''
        value = LogicAppWorkflowAccessControlWorkflowManagement(
            allowed_caller_ip_address_range=allowed_caller_ip_address_range
        )

        return typing.cast(None, jsii.invoke(self, "putWorkflowManagement", [value]))

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetContent")
    def reset_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContent", []))

    @jsii.member(jsii_name="resetTrigger")
    def reset_trigger(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrigger", []))

    @jsii.member(jsii_name="resetWorkflowManagement")
    def reset_workflow_management(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkflowManagement", []))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> LogicAppWorkflowAccessControlActionOutputReference:
        return typing.cast(LogicAppWorkflowAccessControlActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> LogicAppWorkflowAccessControlContentOutputReference:
        return typing.cast(LogicAppWorkflowAccessControlContentOutputReference, jsii.get(self, "content"))

    @builtins.property
    @jsii.member(jsii_name="trigger")
    def trigger(self) -> "LogicAppWorkflowAccessControlTriggerOutputReference":
        return typing.cast("LogicAppWorkflowAccessControlTriggerOutputReference", jsii.get(self, "trigger"))

    @builtins.property
    @jsii.member(jsii_name="workflowManagement")
    def workflow_management(
        self,
    ) -> "LogicAppWorkflowAccessControlWorkflowManagementOutputReference":
        return typing.cast("LogicAppWorkflowAccessControlWorkflowManagementOutputReference", jsii.get(self, "workflowManagement"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[LogicAppWorkflowAccessControlAction]:
        return typing.cast(typing.Optional[LogicAppWorkflowAccessControlAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[LogicAppWorkflowAccessControlContent]:
        return typing.cast(typing.Optional[LogicAppWorkflowAccessControlContent], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerInput")
    def trigger_input(self) -> typing.Optional["LogicAppWorkflowAccessControlTrigger"]:
        return typing.cast(typing.Optional["LogicAppWorkflowAccessControlTrigger"], jsii.get(self, "triggerInput"))

    @builtins.property
    @jsii.member(jsii_name="workflowManagementInput")
    def workflow_management_input(
        self,
    ) -> typing.Optional["LogicAppWorkflowAccessControlWorkflowManagement"]:
        return typing.cast(typing.Optional["LogicAppWorkflowAccessControlWorkflowManagement"], jsii.get(self, "workflowManagementInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LogicAppWorkflowAccessControl]:
        return typing.cast(typing.Optional[LogicAppWorkflowAccessControl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogicAppWorkflowAccessControl],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowAccessControlTrigger",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_caller_ip_address_range": "allowedCallerIpAddressRange",
        "open_authentication_policy": "openAuthenticationPolicy",
    },
)
class LogicAppWorkflowAccessControlTrigger:
    def __init__(
        self,
        *,
        allowed_caller_ip_address_range: typing.Sequence[builtins.str],
        open_authentication_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicy", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param allowed_caller_ip_address_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#allowed_caller_ip_address_range LogicAppWorkflow#allowed_caller_ip_address_range}.
        :param open_authentication_policy: open_authentication_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#open_authentication_policy LogicAppWorkflow#open_authentication_policy}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlTrigger.__init__)
            check_type(argname="argument allowed_caller_ip_address_range", value=allowed_caller_ip_address_range, expected_type=type_hints["allowed_caller_ip_address_range"])
            check_type(argname="argument open_authentication_policy", value=open_authentication_policy, expected_type=type_hints["open_authentication_policy"])
        self._values: typing.Dict[str, typing.Any] = {
            "allowed_caller_ip_address_range": allowed_caller_ip_address_range,
        }
        if open_authentication_policy is not None:
            self._values["open_authentication_policy"] = open_authentication_policy

    @builtins.property
    def allowed_caller_ip_address_range(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#allowed_caller_ip_address_range LogicAppWorkflow#allowed_caller_ip_address_range}.'''
        result = self._values.get("allowed_caller_ip_address_range")
        assert result is not None, "Required property 'allowed_caller_ip_address_range' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def open_authentication_policy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicy"]]]:
        '''open_authentication_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#open_authentication_policy LogicAppWorkflow#open_authentication_policy}
        '''
        result = self._values.get("open_authentication_policy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicy"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppWorkflowAccessControlTrigger(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicy",
    jsii_struct_bases=[],
    name_mapping={"claim": "claim", "name": "name"},
)
class LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicy:
    def __init__(
        self,
        *,
        claim: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaim", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
    ) -> None:
        '''
        :param claim: claim block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#claim LogicAppWorkflow#claim}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#name LogicAppWorkflow#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicy.__init__)
            check_type(argname="argument claim", value=claim, expected_type=type_hints["claim"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "claim": claim,
            "name": name,
        }

    @builtins.property
    def claim(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaim"]]:
        '''claim block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#claim LogicAppWorkflow#claim}
        '''
        result = self._values.get("claim")
        assert result is not None, "Required property 'claim' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaim"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#name LogicAppWorkflow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaim",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaim:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#name LogicAppWorkflow#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#value LogicAppWorkflow#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaim.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#name LogicAppWorkflow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#value LogicAppWorkflow#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaim(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaim]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaim]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaim]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaim, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaim, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaim, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putClaim")
    def put_claim(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaim, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyOutputReference.put_claim)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putClaim", [value]))

    @builtins.property
    @jsii.member(jsii_name="claim")
    def claim(
        self,
    ) -> LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimList:
        return typing.cast(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimList, jsii.get(self, "claim"))

    @builtins.property
    @jsii.member(jsii_name="claimInput")
    def claim_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaim]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaim]]], jsii.get(self, "claimInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LogicAppWorkflowAccessControlTriggerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowAccessControlTriggerOutputReference",
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
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlTriggerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOpenAuthenticationPolicy")
    def put_open_authentication_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicy, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlTriggerOutputReference.put_open_authentication_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOpenAuthenticationPolicy", [value]))

    @jsii.member(jsii_name="resetOpenAuthenticationPolicy")
    def reset_open_authentication_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpenAuthenticationPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="openAuthenticationPolicy")
    def open_authentication_policy(
        self,
    ) -> LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyList:
        return typing.cast(LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyList, jsii.get(self, "openAuthenticationPolicy"))

    @builtins.property
    @jsii.member(jsii_name="allowedCallerIpAddressRangeInput")
    def allowed_caller_ip_address_range_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedCallerIpAddressRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="openAuthenticationPolicyInput")
    def open_authentication_policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicy]]], jsii.get(self, "openAuthenticationPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedCallerIpAddressRange")
    def allowed_caller_ip_address_range(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedCallerIpAddressRange"))

    @allowed_caller_ip_address_range.setter
    def allowed_caller_ip_address_range(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlTriggerOutputReference, "allowed_caller_ip_address_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedCallerIpAddressRange", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LogicAppWorkflowAccessControlTrigger]:
        return typing.cast(typing.Optional[LogicAppWorkflowAccessControlTrigger], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogicAppWorkflowAccessControlTrigger],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlTriggerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowAccessControlWorkflowManagement",
    jsii_struct_bases=[],
    name_mapping={"allowed_caller_ip_address_range": "allowedCallerIpAddressRange"},
)
class LogicAppWorkflowAccessControlWorkflowManagement:
    def __init__(
        self,
        *,
        allowed_caller_ip_address_range: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param allowed_caller_ip_address_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#allowed_caller_ip_address_range LogicAppWorkflow#allowed_caller_ip_address_range}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlWorkflowManagement.__init__)
            check_type(argname="argument allowed_caller_ip_address_range", value=allowed_caller_ip_address_range, expected_type=type_hints["allowed_caller_ip_address_range"])
        self._values: typing.Dict[str, typing.Any] = {
            "allowed_caller_ip_address_range": allowed_caller_ip_address_range,
        }

    @builtins.property
    def allowed_caller_ip_address_range(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#allowed_caller_ip_address_range LogicAppWorkflow#allowed_caller_ip_address_range}.'''
        result = self._values.get("allowed_caller_ip_address_range")
        assert result is not None, "Required property 'allowed_caller_ip_address_range' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppWorkflowAccessControlWorkflowManagement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogicAppWorkflowAccessControlWorkflowManagementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowAccessControlWorkflowManagementOutputReference",
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
            type_hints = typing.get_type_hints(LogicAppWorkflowAccessControlWorkflowManagementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="allowedCallerIpAddressRangeInput")
    def allowed_caller_ip_address_range_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedCallerIpAddressRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedCallerIpAddressRange")
    def allowed_caller_ip_address_range(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedCallerIpAddressRange"))

    @allowed_caller_ip_address_range.setter
    def allowed_caller_ip_address_range(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlWorkflowManagementOutputReference, "allowed_caller_ip_address_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedCallerIpAddressRange", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogicAppWorkflowAccessControlWorkflowManagement]:
        return typing.cast(typing.Optional[LogicAppWorkflowAccessControlWorkflowManagement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogicAppWorkflowAccessControlWorkflowManagement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowAccessControlWorkflowManagementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "access_control": "accessControl",
        "enabled": "enabled",
        "id": "id",
        "identity": "identity",
        "integration_service_environment_id": "integrationServiceEnvironmentId",
        "logic_app_integration_account_id": "logicAppIntegrationAccountId",
        "parameters": "parameters",
        "tags": "tags",
        "timeouts": "timeouts",
        "workflow_parameters": "workflowParameters",
        "workflow_schema": "workflowSchema",
        "workflow_version": "workflowVersion",
    },
)
class LogicAppWorkflowConfig(cdktf.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        access_control: typing.Optional[typing.Union[LogicAppWorkflowAccessControl, typing.Dict[str, typing.Any]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["LogicAppWorkflowIdentity", typing.Dict[str, typing.Any]]] = None,
        integration_service_environment_id: typing.Optional[builtins.str] = None,
        logic_app_integration_account_id: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["LogicAppWorkflowTimeouts", typing.Dict[str, typing.Any]]] = None,
        workflow_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        workflow_schema: typing.Optional[builtins.str] = None,
        workflow_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#location LogicAppWorkflow#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#name LogicAppWorkflow#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#resource_group_name LogicAppWorkflow#resource_group_name}.
        :param access_control: access_control block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#access_control LogicAppWorkflow#access_control}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#enabled LogicAppWorkflow#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#id LogicAppWorkflow#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#identity LogicAppWorkflow#identity}
        :param integration_service_environment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#integration_service_environment_id LogicAppWorkflow#integration_service_environment_id}.
        :param logic_app_integration_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#logic_app_integration_account_id LogicAppWorkflow#logic_app_integration_account_id}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#parameters LogicAppWorkflow#parameters}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#tags LogicAppWorkflow#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#timeouts LogicAppWorkflow#timeouts}
        :param workflow_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#workflow_parameters LogicAppWorkflow#workflow_parameters}.
        :param workflow_schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#workflow_schema LogicAppWorkflow#workflow_schema}.
        :param workflow_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#workflow_version LogicAppWorkflow#workflow_version}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(access_control, dict):
            access_control = LogicAppWorkflowAccessControl(**access_control)
        if isinstance(identity, dict):
            identity = LogicAppWorkflowIdentity(**identity)
        if isinstance(timeouts, dict):
            timeouts = LogicAppWorkflowTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflowConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument access_control", value=access_control, expected_type=type_hints["access_control"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument integration_service_environment_id", value=integration_service_environment_id, expected_type=type_hints["integration_service_environment_id"])
            check_type(argname="argument logic_app_integration_account_id", value=logic_app_integration_account_id, expected_type=type_hints["logic_app_integration_account_id"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument workflow_parameters", value=workflow_parameters, expected_type=type_hints["workflow_parameters"])
            check_type(argname="argument workflow_schema", value=workflow_schema, expected_type=type_hints["workflow_schema"])
            check_type(argname="argument workflow_version", value=workflow_version, expected_type=type_hints["workflow_version"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
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
        if access_control is not None:
            self._values["access_control"] = access_control
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if integration_service_environment_id is not None:
            self._values["integration_service_environment_id"] = integration_service_environment_id
        if logic_app_integration_account_id is not None:
            self._values["logic_app_integration_account_id"] = logic_app_integration_account_id
        if parameters is not None:
            self._values["parameters"] = parameters
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if workflow_parameters is not None:
            self._values["workflow_parameters"] = workflow_parameters
        if workflow_schema is not None:
            self._values["workflow_schema"] = workflow_schema
        if workflow_version is not None:
            self._values["workflow_version"] = workflow_version

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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#location LogicAppWorkflow#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#name LogicAppWorkflow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#resource_group_name LogicAppWorkflow#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_control(self) -> typing.Optional[LogicAppWorkflowAccessControl]:
        '''access_control block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#access_control LogicAppWorkflow#access_control}
        '''
        result = self._values.get("access_control")
        return typing.cast(typing.Optional[LogicAppWorkflowAccessControl], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#enabled LogicAppWorkflow#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#id LogicAppWorkflow#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["LogicAppWorkflowIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#identity LogicAppWorkflow#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["LogicAppWorkflowIdentity"], result)

    @builtins.property
    def integration_service_environment_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#integration_service_environment_id LogicAppWorkflow#integration_service_environment_id}.'''
        result = self._values.get("integration_service_environment_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logic_app_integration_account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#logic_app_integration_account_id LogicAppWorkflow#logic_app_integration_account_id}.'''
        result = self._values.get("logic_app_integration_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#parameters LogicAppWorkflow#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#tags LogicAppWorkflow#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LogicAppWorkflowTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#timeouts LogicAppWorkflow#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LogicAppWorkflowTimeouts"], result)

    @builtins.property
    def workflow_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#workflow_parameters LogicAppWorkflow#workflow_parameters}.'''
        result = self._values.get("workflow_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def workflow_schema(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#workflow_schema LogicAppWorkflow#workflow_schema}.'''
        result = self._values.get("workflow_schema")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workflow_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#workflow_version LogicAppWorkflow#workflow_version}.'''
        result = self._values.get("workflow_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppWorkflowConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class LogicAppWorkflowIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#type LogicAppWorkflow#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#identity_ids LogicAppWorkflow#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflowIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#type LogicAppWorkflow#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#identity_ids LogicAppWorkflow#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppWorkflowIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogicAppWorkflowIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowIdentityOutputReference",
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
            type_hints = typing.get_type_hints(LogicAppWorkflowIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdentityIds")
    def reset_identity_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityIds", []))

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @builtins.property
    @jsii.member(jsii_name="identityIdsInput")
    def identity_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identityIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="identityIds")
    def identity_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identityIds"))

    @identity_ids.setter
    def identity_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LogicAppWorkflowIdentity]:
        return typing.cast(typing.Optional[LogicAppWorkflowIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LogicAppWorkflowIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class LogicAppWorkflowTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#create LogicAppWorkflow#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#delete LogicAppWorkflow#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#read LogicAppWorkflow#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#update LogicAppWorkflow#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppWorkflowTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#create LogicAppWorkflow#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#delete LogicAppWorkflow#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#read LogicAppWorkflow#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow#update LogicAppWorkflow#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppWorkflowTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogicAppWorkflowTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppWorkflow.LogicAppWorkflowTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(LogicAppWorkflowTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LogicAppWorkflowTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LogicAppWorkflowTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LogicAppWorkflowTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppWorkflowTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LogicAppWorkflow",
    "LogicAppWorkflowAccessControl",
    "LogicAppWorkflowAccessControlAction",
    "LogicAppWorkflowAccessControlActionOutputReference",
    "LogicAppWorkflowAccessControlContent",
    "LogicAppWorkflowAccessControlContentOutputReference",
    "LogicAppWorkflowAccessControlOutputReference",
    "LogicAppWorkflowAccessControlTrigger",
    "LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicy",
    "LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaim",
    "LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimList",
    "LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyClaimOutputReference",
    "LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyList",
    "LogicAppWorkflowAccessControlTriggerOpenAuthenticationPolicyOutputReference",
    "LogicAppWorkflowAccessControlTriggerOutputReference",
    "LogicAppWorkflowAccessControlWorkflowManagement",
    "LogicAppWorkflowAccessControlWorkflowManagementOutputReference",
    "LogicAppWorkflowConfig",
    "LogicAppWorkflowIdentity",
    "LogicAppWorkflowIdentityOutputReference",
    "LogicAppWorkflowTimeouts",
    "LogicAppWorkflowTimeoutsOutputReference",
]

publication.publish()
