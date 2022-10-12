'''
# `azurerm_iot_security_device_group`

Refer to the Terraform Registory for docs: [`azurerm_iot_security_device_group`](https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group).
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


class IotSecurityDeviceGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iotSecurityDeviceGroup.IotSecurityDeviceGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group azurerm_iot_security_device_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        iothub_id: builtins.str,
        name: builtins.str,
        allow_rule: typing.Optional[typing.Union["IotSecurityDeviceGroupAllowRule", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        range_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IotSecurityDeviceGroupRangeRule", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["IotSecurityDeviceGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group azurerm_iot_security_device_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param iothub_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#iothub_id IotSecurityDeviceGroup#iothub_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#name IotSecurityDeviceGroup#name}.
        :param allow_rule: allow_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#allow_rule IotSecurityDeviceGroup#allow_rule}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#id IotSecurityDeviceGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param range_rule: range_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#range_rule IotSecurityDeviceGroup#range_rule}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#timeouts IotSecurityDeviceGroup#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IotSecurityDeviceGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IotSecurityDeviceGroupConfig(
            iothub_id=iothub_id,
            name=name,
            allow_rule=allow_rule,
            id=id,
            range_rule=range_rule,
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

    @jsii.member(jsii_name="putAllowRule")
    def put_allow_rule(
        self,
        *,
        connection_from_ips_not_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection_to_ips_not_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
        local_users_not_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
        processes_not_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection_from_ips_not_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#connection_from_ips_not_allowed IotSecurityDeviceGroup#connection_from_ips_not_allowed}.
        :param connection_to_ips_not_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#connection_to_ips_not_allowed IotSecurityDeviceGroup#connection_to_ips_not_allowed}.
        :param local_users_not_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#local_users_not_allowed IotSecurityDeviceGroup#local_users_not_allowed}.
        :param processes_not_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#processes_not_allowed IotSecurityDeviceGroup#processes_not_allowed}.
        '''
        value = IotSecurityDeviceGroupAllowRule(
            connection_from_ips_not_allowed=connection_from_ips_not_allowed,
            connection_to_ips_not_allowed=connection_to_ips_not_allowed,
            local_users_not_allowed=local_users_not_allowed,
            processes_not_allowed=processes_not_allowed,
        )

        return typing.cast(None, jsii.invoke(self, "putAllowRule", [value]))

    @jsii.member(jsii_name="putRangeRule")
    def put_range_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IotSecurityDeviceGroupRangeRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IotSecurityDeviceGroup.put_range_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRangeRule", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#create IotSecurityDeviceGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#delete IotSecurityDeviceGroup#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#read IotSecurityDeviceGroup#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#update IotSecurityDeviceGroup#update}.
        '''
        value = IotSecurityDeviceGroupTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAllowRule")
    def reset_allow_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowRule", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRangeRule")
    def reset_range_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRangeRule", []))

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
    @jsii.member(jsii_name="allowRule")
    def allow_rule(self) -> "IotSecurityDeviceGroupAllowRuleOutputReference":
        return typing.cast("IotSecurityDeviceGroupAllowRuleOutputReference", jsii.get(self, "allowRule"))

    @builtins.property
    @jsii.member(jsii_name="rangeRule")
    def range_rule(self) -> "IotSecurityDeviceGroupRangeRuleList":
        return typing.cast("IotSecurityDeviceGroupRangeRuleList", jsii.get(self, "rangeRule"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "IotSecurityDeviceGroupTimeoutsOutputReference":
        return typing.cast("IotSecurityDeviceGroupTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="allowRuleInput")
    def allow_rule_input(self) -> typing.Optional["IotSecurityDeviceGroupAllowRule"]:
        return typing.cast(typing.Optional["IotSecurityDeviceGroupAllowRule"], jsii.get(self, "allowRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="iothubIdInput")
    def iothub_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iothubIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeRuleInput")
    def range_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IotSecurityDeviceGroupRangeRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IotSecurityDeviceGroupRangeRule"]]], jsii.get(self, "rangeRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["IotSecurityDeviceGroupTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["IotSecurityDeviceGroupTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="iothubId")
    def iothub_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iothubId"))

    @iothub_id.setter
    def iothub_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroup, "iothub_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iothubId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroup, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iotSecurityDeviceGroup.IotSecurityDeviceGroupAllowRule",
    jsii_struct_bases=[],
    name_mapping={
        "connection_from_ips_not_allowed": "connectionFromIpsNotAllowed",
        "connection_to_ips_not_allowed": "connectionToIpsNotAllowed",
        "local_users_not_allowed": "localUsersNotAllowed",
        "processes_not_allowed": "processesNotAllowed",
    },
)
class IotSecurityDeviceGroupAllowRule:
    def __init__(
        self,
        *,
        connection_from_ips_not_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection_to_ips_not_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
        local_users_not_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
        processes_not_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection_from_ips_not_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#connection_from_ips_not_allowed IotSecurityDeviceGroup#connection_from_ips_not_allowed}.
        :param connection_to_ips_not_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#connection_to_ips_not_allowed IotSecurityDeviceGroup#connection_to_ips_not_allowed}.
        :param local_users_not_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#local_users_not_allowed IotSecurityDeviceGroup#local_users_not_allowed}.
        :param processes_not_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#processes_not_allowed IotSecurityDeviceGroup#processes_not_allowed}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IotSecurityDeviceGroupAllowRule.__init__)
            check_type(argname="argument connection_from_ips_not_allowed", value=connection_from_ips_not_allowed, expected_type=type_hints["connection_from_ips_not_allowed"])
            check_type(argname="argument connection_to_ips_not_allowed", value=connection_to_ips_not_allowed, expected_type=type_hints["connection_to_ips_not_allowed"])
            check_type(argname="argument local_users_not_allowed", value=local_users_not_allowed, expected_type=type_hints["local_users_not_allowed"])
            check_type(argname="argument processes_not_allowed", value=processes_not_allowed, expected_type=type_hints["processes_not_allowed"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_from_ips_not_allowed is not None:
            self._values["connection_from_ips_not_allowed"] = connection_from_ips_not_allowed
        if connection_to_ips_not_allowed is not None:
            self._values["connection_to_ips_not_allowed"] = connection_to_ips_not_allowed
        if local_users_not_allowed is not None:
            self._values["local_users_not_allowed"] = local_users_not_allowed
        if processes_not_allowed is not None:
            self._values["processes_not_allowed"] = processes_not_allowed

    @builtins.property
    def connection_from_ips_not_allowed(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#connection_from_ips_not_allowed IotSecurityDeviceGroup#connection_from_ips_not_allowed}.'''
        result = self._values.get("connection_from_ips_not_allowed")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def connection_to_ips_not_allowed(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#connection_to_ips_not_allowed IotSecurityDeviceGroup#connection_to_ips_not_allowed}.'''
        result = self._values.get("connection_to_ips_not_allowed")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def local_users_not_allowed(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#local_users_not_allowed IotSecurityDeviceGroup#local_users_not_allowed}.'''
        result = self._values.get("local_users_not_allowed")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def processes_not_allowed(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#processes_not_allowed IotSecurityDeviceGroup#processes_not_allowed}.'''
        result = self._values.get("processes_not_allowed")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotSecurityDeviceGroupAllowRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotSecurityDeviceGroupAllowRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iotSecurityDeviceGroup.IotSecurityDeviceGroupAllowRuleOutputReference",
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
            type_hints = typing.get_type_hints(IotSecurityDeviceGroupAllowRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectionFromIpsNotAllowed")
    def reset_connection_from_ips_not_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionFromIpsNotAllowed", []))

    @jsii.member(jsii_name="resetConnectionToIpsNotAllowed")
    def reset_connection_to_ips_not_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionToIpsNotAllowed", []))

    @jsii.member(jsii_name="resetLocalUsersNotAllowed")
    def reset_local_users_not_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalUsersNotAllowed", []))

    @jsii.member(jsii_name="resetProcessesNotAllowed")
    def reset_processes_not_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessesNotAllowed", []))

    @builtins.property
    @jsii.member(jsii_name="connectionFromIpsNotAllowedInput")
    def connection_from_ips_not_allowed_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "connectionFromIpsNotAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionToIpsNotAllowedInput")
    def connection_to_ips_not_allowed_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "connectionToIpsNotAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="localUsersNotAllowedInput")
    def local_users_not_allowed_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "localUsersNotAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="processesNotAllowedInput")
    def processes_not_allowed_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "processesNotAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionFromIpsNotAllowed")
    def connection_from_ips_not_allowed(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "connectionFromIpsNotAllowed"))

    @connection_from_ips_not_allowed.setter
    def connection_from_ips_not_allowed(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupAllowRuleOutputReference, "connection_from_ips_not_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionFromIpsNotAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="connectionToIpsNotAllowed")
    def connection_to_ips_not_allowed(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "connectionToIpsNotAllowed"))

    @connection_to_ips_not_allowed.setter
    def connection_to_ips_not_allowed(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupAllowRuleOutputReference, "connection_to_ips_not_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionToIpsNotAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="localUsersNotAllowed")
    def local_users_not_allowed(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "localUsersNotAllowed"))

    @local_users_not_allowed.setter
    def local_users_not_allowed(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupAllowRuleOutputReference, "local_users_not_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localUsersNotAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="processesNotAllowed")
    def processes_not_allowed(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "processesNotAllowed"))

    @processes_not_allowed.setter
    def processes_not_allowed(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupAllowRuleOutputReference, "processes_not_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "processesNotAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotSecurityDeviceGroupAllowRule]:
        return typing.cast(typing.Optional[IotSecurityDeviceGroupAllowRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotSecurityDeviceGroupAllowRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupAllowRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iotSecurityDeviceGroup.IotSecurityDeviceGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "iothub_id": "iothubId",
        "name": "name",
        "allow_rule": "allowRule",
        "id": "id",
        "range_rule": "rangeRule",
        "timeouts": "timeouts",
    },
)
class IotSecurityDeviceGroupConfig(cdktf.TerraformMetaArguments):
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
        iothub_id: builtins.str,
        name: builtins.str,
        allow_rule: typing.Optional[typing.Union[IotSecurityDeviceGroupAllowRule, typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        range_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IotSecurityDeviceGroupRangeRule", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["IotSecurityDeviceGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param iothub_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#iothub_id IotSecurityDeviceGroup#iothub_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#name IotSecurityDeviceGroup#name}.
        :param allow_rule: allow_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#allow_rule IotSecurityDeviceGroup#allow_rule}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#id IotSecurityDeviceGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param range_rule: range_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#range_rule IotSecurityDeviceGroup#range_rule}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#timeouts IotSecurityDeviceGroup#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(allow_rule, dict):
            allow_rule = IotSecurityDeviceGroupAllowRule(**allow_rule)
        if isinstance(timeouts, dict):
            timeouts = IotSecurityDeviceGroupTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(IotSecurityDeviceGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument iothub_id", value=iothub_id, expected_type=type_hints["iothub_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allow_rule", value=allow_rule, expected_type=type_hints["allow_rule"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument range_rule", value=range_rule, expected_type=type_hints["range_rule"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "iothub_id": iothub_id,
            "name": name,
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
        if allow_rule is not None:
            self._values["allow_rule"] = allow_rule
        if id is not None:
            self._values["id"] = id
        if range_rule is not None:
            self._values["range_rule"] = range_rule
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
    def iothub_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#iothub_id IotSecurityDeviceGroup#iothub_id}.'''
        result = self._values.get("iothub_id")
        assert result is not None, "Required property 'iothub_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#name IotSecurityDeviceGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_rule(self) -> typing.Optional[IotSecurityDeviceGroupAllowRule]:
        '''allow_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#allow_rule IotSecurityDeviceGroup#allow_rule}
        '''
        result = self._values.get("allow_rule")
        return typing.cast(typing.Optional[IotSecurityDeviceGroupAllowRule], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#id IotSecurityDeviceGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def range_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IotSecurityDeviceGroupRangeRule"]]]:
        '''range_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#range_rule IotSecurityDeviceGroup#range_rule}
        '''
        result = self._values.get("range_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IotSecurityDeviceGroupRangeRule"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["IotSecurityDeviceGroupTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#timeouts IotSecurityDeviceGroup#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["IotSecurityDeviceGroupTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotSecurityDeviceGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iotSecurityDeviceGroup.IotSecurityDeviceGroupRangeRule",
    jsii_struct_bases=[],
    name_mapping={"duration": "duration", "max": "max", "min": "min", "type": "type"},
)
class IotSecurityDeviceGroupRangeRule:
    def __init__(
        self,
        *,
        duration: builtins.str,
        max: jsii.Number,
        min: jsii.Number,
        type: builtins.str,
    ) -> None:
        '''
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#duration IotSecurityDeviceGroup#duration}.
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#max IotSecurityDeviceGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#min IotSecurityDeviceGroup#min}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#type IotSecurityDeviceGroup#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IotSecurityDeviceGroupRangeRule.__init__)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "duration": duration,
            "max": max,
            "min": min,
            "type": type,
        }

    @builtins.property
    def duration(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#duration IotSecurityDeviceGroup#duration}.'''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#max IotSecurityDeviceGroup#max}.'''
        result = self._values.get("max")
        assert result is not None, "Required property 'max' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#min IotSecurityDeviceGroup#min}.'''
        result = self._values.get("min")
        assert result is not None, "Required property 'min' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#type IotSecurityDeviceGroup#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotSecurityDeviceGroupRangeRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotSecurityDeviceGroupRangeRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iotSecurityDeviceGroup.IotSecurityDeviceGroupRangeRuleList",
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
            type_hints = typing.get_type_hints(IotSecurityDeviceGroupRangeRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "IotSecurityDeviceGroupRangeRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IotSecurityDeviceGroupRangeRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotSecurityDeviceGroupRangeRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupRangeRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupRangeRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupRangeRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotSecurityDeviceGroupRangeRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotSecurityDeviceGroupRangeRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotSecurityDeviceGroupRangeRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupRangeRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotSecurityDeviceGroupRangeRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iotSecurityDeviceGroup.IotSecurityDeviceGroupRangeRuleOutputReference",
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
            type_hints = typing.get_type_hints(IotSecurityDeviceGroupRangeRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupRangeRuleOutputReference, "duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupRangeRuleOutputReference, "max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupRangeRuleOutputReference, "min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupRangeRuleOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotSecurityDeviceGroupRangeRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotSecurityDeviceGroupRangeRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotSecurityDeviceGroupRangeRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupRangeRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iotSecurityDeviceGroup.IotSecurityDeviceGroupTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class IotSecurityDeviceGroupTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#create IotSecurityDeviceGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#delete IotSecurityDeviceGroup#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#read IotSecurityDeviceGroup#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#update IotSecurityDeviceGroup#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IotSecurityDeviceGroupTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#create IotSecurityDeviceGroup#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#delete IotSecurityDeviceGroup#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#read IotSecurityDeviceGroup#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_security_device_group#update IotSecurityDeviceGroup#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotSecurityDeviceGroupTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotSecurityDeviceGroupTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iotSecurityDeviceGroup.IotSecurityDeviceGroupTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(IotSecurityDeviceGroupTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotSecurityDeviceGroupTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotSecurityDeviceGroupTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotSecurityDeviceGroupTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotSecurityDeviceGroupTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "IotSecurityDeviceGroup",
    "IotSecurityDeviceGroupAllowRule",
    "IotSecurityDeviceGroupAllowRuleOutputReference",
    "IotSecurityDeviceGroupConfig",
    "IotSecurityDeviceGroupRangeRule",
    "IotSecurityDeviceGroupRangeRuleList",
    "IotSecurityDeviceGroupRangeRuleOutputReference",
    "IotSecurityDeviceGroupTimeouts",
    "IotSecurityDeviceGroupTimeoutsOutputReference",
]

publication.publish()
