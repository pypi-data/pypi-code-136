'''
# `azurerm_blueprint_assignment`

Refer to the Terraform Registory for docs: [`azurerm_blueprint_assignment`](https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment).
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


class BlueprintAssignment(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.blueprintAssignment.BlueprintAssignment",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment azurerm_blueprint_assignment}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        identity: typing.Union["BlueprintAssignmentIdentity", typing.Dict[str, typing.Any]],
        location: builtins.str,
        name: builtins.str,
        target_subscription_id: builtins.str,
        version_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        lock_exclude_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        lock_exclude_principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        lock_mode: typing.Optional[builtins.str] = None,
        parameter_values: typing.Optional[builtins.str] = None,
        resource_groups: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["BlueprintAssignmentTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment azurerm_blueprint_assignment} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#identity BlueprintAssignment#identity}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#location BlueprintAssignment#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#name BlueprintAssignment#name}.
        :param target_subscription_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#target_subscription_id BlueprintAssignment#target_subscription_id}.
        :param version_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#version_id BlueprintAssignment#version_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#id BlueprintAssignment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lock_exclude_actions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#lock_exclude_actions BlueprintAssignment#lock_exclude_actions}.
        :param lock_exclude_principals: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#lock_exclude_principals BlueprintAssignment#lock_exclude_principals}.
        :param lock_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#lock_mode BlueprintAssignment#lock_mode}.
        :param parameter_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#parameter_values BlueprintAssignment#parameter_values}.
        :param resource_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#resource_groups BlueprintAssignment#resource_groups}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#timeouts BlueprintAssignment#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BlueprintAssignment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = BlueprintAssignmentConfig(
            identity=identity,
            location=location,
            name=name,
            target_subscription_id=target_subscription_id,
            version_id=version_id,
            id=id,
            lock_exclude_actions=lock_exclude_actions,
            lock_exclude_principals=lock_exclude_principals,
            lock_mode=lock_mode,
            parameter_values=parameter_values,
            resource_groups=resource_groups,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        identity_ids: typing.Sequence[builtins.str],
        type: builtins.str,
    ) -> None:
        '''
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#identity_ids BlueprintAssignment#identity_ids}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#type BlueprintAssignment#type}.
        '''
        value = BlueprintAssignmentIdentity(identity_ids=identity_ids, type=type)

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#create BlueprintAssignment#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#delete BlueprintAssignment#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#read BlueprintAssignment#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#update BlueprintAssignment#update}.
        '''
        value = BlueprintAssignmentTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLockExcludeActions")
    def reset_lock_exclude_actions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLockExcludeActions", []))

    @jsii.member(jsii_name="resetLockExcludePrincipals")
    def reset_lock_exclude_principals(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLockExcludePrincipals", []))

    @jsii.member(jsii_name="resetLockMode")
    def reset_lock_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLockMode", []))

    @jsii.member(jsii_name="resetParameterValues")
    def reset_parameter_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameterValues", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="blueprintName")
    def blueprint_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "blueprintName"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "BlueprintAssignmentIdentityOutputReference":
        return typing.cast("BlueprintAssignmentIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "BlueprintAssignmentTimeoutsOutputReference":
        return typing.cast("BlueprintAssignmentTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["BlueprintAssignmentIdentity"]:
        return typing.cast(typing.Optional["BlueprintAssignmentIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="lockExcludeActionsInput")
    def lock_exclude_actions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "lockExcludeActionsInput"))

    @builtins.property
    @jsii.member(jsii_name="lockExcludePrincipalsInput")
    def lock_exclude_principals_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "lockExcludePrincipalsInput"))

    @builtins.property
    @jsii.member(jsii_name="lockModeInput")
    def lock_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lockModeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterValuesInput")
    def parameter_values_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="targetSubscriptionIdInput")
    def target_subscription_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetSubscriptionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["BlueprintAssignmentTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["BlueprintAssignmentTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionIdInput")
    def version_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BlueprintAssignment, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BlueprintAssignment, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="lockExcludeActions")
    def lock_exclude_actions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "lockExcludeActions"))

    @lock_exclude_actions.setter
    def lock_exclude_actions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BlueprintAssignment, "lock_exclude_actions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lockExcludeActions", value)

    @builtins.property
    @jsii.member(jsii_name="lockExcludePrincipals")
    def lock_exclude_principals(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "lockExcludePrincipals"))

    @lock_exclude_principals.setter
    def lock_exclude_principals(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BlueprintAssignment, "lock_exclude_principals").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lockExcludePrincipals", value)

    @builtins.property
    @jsii.member(jsii_name="lockMode")
    def lock_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lockMode"))

    @lock_mode.setter
    def lock_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BlueprintAssignment, "lock_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lockMode", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BlueprintAssignment, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameterValues")
    def parameter_values(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterValues"))

    @parameter_values.setter
    def parameter_values(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BlueprintAssignment, "parameter_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterValues", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BlueprintAssignment, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="targetSubscriptionId")
    def target_subscription_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetSubscriptionId"))

    @target_subscription_id.setter
    def target_subscription_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BlueprintAssignment, "target_subscription_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetSubscriptionId", value)

    @builtins.property
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionId"))

    @version_id.setter
    def version_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BlueprintAssignment, "version_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.blueprintAssignment.BlueprintAssignmentConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "identity": "identity",
        "location": "location",
        "name": "name",
        "target_subscription_id": "targetSubscriptionId",
        "version_id": "versionId",
        "id": "id",
        "lock_exclude_actions": "lockExcludeActions",
        "lock_exclude_principals": "lockExcludePrincipals",
        "lock_mode": "lockMode",
        "parameter_values": "parameterValues",
        "resource_groups": "resourceGroups",
        "timeouts": "timeouts",
    },
)
class BlueprintAssignmentConfig(cdktf.TerraformMetaArguments):
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
        identity: typing.Union["BlueprintAssignmentIdentity", typing.Dict[str, typing.Any]],
        location: builtins.str,
        name: builtins.str,
        target_subscription_id: builtins.str,
        version_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        lock_exclude_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        lock_exclude_principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        lock_mode: typing.Optional[builtins.str] = None,
        parameter_values: typing.Optional[builtins.str] = None,
        resource_groups: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["BlueprintAssignmentTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#identity BlueprintAssignment#identity}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#location BlueprintAssignment#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#name BlueprintAssignment#name}.
        :param target_subscription_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#target_subscription_id BlueprintAssignment#target_subscription_id}.
        :param version_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#version_id BlueprintAssignment#version_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#id BlueprintAssignment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lock_exclude_actions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#lock_exclude_actions BlueprintAssignment#lock_exclude_actions}.
        :param lock_exclude_principals: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#lock_exclude_principals BlueprintAssignment#lock_exclude_principals}.
        :param lock_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#lock_mode BlueprintAssignment#lock_mode}.
        :param parameter_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#parameter_values BlueprintAssignment#parameter_values}.
        :param resource_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#resource_groups BlueprintAssignment#resource_groups}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#timeouts BlueprintAssignment#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(identity, dict):
            identity = BlueprintAssignmentIdentity(**identity)
        if isinstance(timeouts, dict):
            timeouts = BlueprintAssignmentTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(BlueprintAssignmentConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target_subscription_id", value=target_subscription_id, expected_type=type_hints["target_subscription_id"])
            check_type(argname="argument version_id", value=version_id, expected_type=type_hints["version_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lock_exclude_actions", value=lock_exclude_actions, expected_type=type_hints["lock_exclude_actions"])
            check_type(argname="argument lock_exclude_principals", value=lock_exclude_principals, expected_type=type_hints["lock_exclude_principals"])
            check_type(argname="argument lock_mode", value=lock_mode, expected_type=type_hints["lock_mode"])
            check_type(argname="argument parameter_values", value=parameter_values, expected_type=type_hints["parameter_values"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "identity": identity,
            "location": location,
            "name": name,
            "target_subscription_id": target_subscription_id,
            "version_id": version_id,
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
        if id is not None:
            self._values["id"] = id
        if lock_exclude_actions is not None:
            self._values["lock_exclude_actions"] = lock_exclude_actions
        if lock_exclude_principals is not None:
            self._values["lock_exclude_principals"] = lock_exclude_principals
        if lock_mode is not None:
            self._values["lock_mode"] = lock_mode
        if parameter_values is not None:
            self._values["parameter_values"] = parameter_values
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def identity(self) -> "BlueprintAssignmentIdentity":
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#identity BlueprintAssignment#identity}
        '''
        result = self._values.get("identity")
        assert result is not None, "Required property 'identity' is missing"
        return typing.cast("BlueprintAssignmentIdentity", result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#location BlueprintAssignment#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#name BlueprintAssignment#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_subscription_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#target_subscription_id BlueprintAssignment#target_subscription_id}.'''
        result = self._values.get("target_subscription_id")
        assert result is not None, "Required property 'target_subscription_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#version_id BlueprintAssignment#version_id}.'''
        result = self._values.get("version_id")
        assert result is not None, "Required property 'version_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#id BlueprintAssignment#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lock_exclude_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#lock_exclude_actions BlueprintAssignment#lock_exclude_actions}.'''
        result = self._values.get("lock_exclude_actions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def lock_exclude_principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#lock_exclude_principals BlueprintAssignment#lock_exclude_principals}.'''
        result = self._values.get("lock_exclude_principals")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def lock_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#lock_mode BlueprintAssignment#lock_mode}.'''
        result = self._values.get("lock_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_values(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#parameter_values BlueprintAssignment#parameter_values}.'''
        result = self._values.get("parameter_values")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#resource_groups BlueprintAssignment#resource_groups}.'''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["BlueprintAssignmentTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#timeouts BlueprintAssignment#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["BlueprintAssignmentTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BlueprintAssignmentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.blueprintAssignment.BlueprintAssignmentIdentity",
    jsii_struct_bases=[],
    name_mapping={"identity_ids": "identityIds", "type": "type"},
)
class BlueprintAssignmentIdentity:
    def __init__(
        self,
        *,
        identity_ids: typing.Sequence[builtins.str],
        type: builtins.str,
    ) -> None:
        '''
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#identity_ids BlueprintAssignment#identity_ids}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#type BlueprintAssignment#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BlueprintAssignmentIdentity.__init__)
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "identity_ids": identity_ids,
            "type": type,
        }

    @builtins.property
    def identity_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#identity_ids BlueprintAssignment#identity_ids}.'''
        result = self._values.get("identity_ids")
        assert result is not None, "Required property 'identity_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#type BlueprintAssignment#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BlueprintAssignmentIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BlueprintAssignmentIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.blueprintAssignment.BlueprintAssignmentIdentityOutputReference",
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
            type_hints = typing.get_type_hints(BlueprintAssignmentIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(BlueprintAssignmentIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BlueprintAssignmentIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BlueprintAssignmentIdentity]:
        return typing.cast(typing.Optional[BlueprintAssignmentIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BlueprintAssignmentIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BlueprintAssignmentIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.blueprintAssignment.BlueprintAssignmentTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class BlueprintAssignmentTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#create BlueprintAssignment#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#delete BlueprintAssignment#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#read BlueprintAssignment#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#update BlueprintAssignment#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BlueprintAssignmentTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#create BlueprintAssignment#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#delete BlueprintAssignment#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#read BlueprintAssignment#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/blueprint_assignment#update BlueprintAssignment#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BlueprintAssignmentTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BlueprintAssignmentTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.blueprintAssignment.BlueprintAssignmentTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(BlueprintAssignmentTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(BlueprintAssignmentTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BlueprintAssignmentTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BlueprintAssignmentTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BlueprintAssignmentTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BlueprintAssignmentTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BlueprintAssignmentTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BlueprintAssignmentTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BlueprintAssignmentTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "BlueprintAssignment",
    "BlueprintAssignmentConfig",
    "BlueprintAssignmentIdentity",
    "BlueprintAssignmentIdentityOutputReference",
    "BlueprintAssignmentTimeouts",
    "BlueprintAssignmentTimeoutsOutputReference",
]

publication.publish()
