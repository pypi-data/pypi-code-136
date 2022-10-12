'''
# `azurerm_iothub_dps`

Refer to the Terraform Registory for docs: [`azurerm_iothub_dps`](https://www.terraform.io/docs/providers/azurerm/r/iothub_dps).
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


class IothubDps(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iothubDps.IothubDps",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps azurerm_iothub_dps}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku: typing.Union["IothubDpsSku", typing.Dict[str, typing.Any]],
        allocation_policy: typing.Optional[builtins.str] = None,
        data_residency_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ip_filter_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IothubDpsIpFilterRule", typing.Dict[str, typing.Any]]]]] = None,
        linked_hub: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IothubDpsLinkedHub", typing.Dict[str, typing.Any]]]]] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["IothubDpsTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps azurerm_iothub_dps} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#location IothubDps#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#name IothubDps#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#resource_group_name IothubDps#resource_group_name}.
        :param sku: sku block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#sku IothubDps#sku}
        :param allocation_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#allocation_policy IothubDps#allocation_policy}.
        :param data_residency_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#data_residency_enabled IothubDps#data_residency_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#id IothubDps#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_filter_rule: ip_filter_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#ip_filter_rule IothubDps#ip_filter_rule}
        :param linked_hub: linked_hub block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#linked_hub IothubDps#linked_hub}
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#public_network_access_enabled IothubDps#public_network_access_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#tags IothubDps#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#timeouts IothubDps#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IothubDps.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IothubDpsConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            sku=sku,
            allocation_policy=allocation_policy,
            data_residency_enabled=data_residency_enabled,
            id=id,
            ip_filter_rule=ip_filter_rule,
            linked_hub=linked_hub,
            public_network_access_enabled=public_network_access_enabled,
            tags=tags,
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

    @jsii.member(jsii_name="putIpFilterRule")
    def put_ip_filter_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IothubDpsIpFilterRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IothubDps.put_ip_filter_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpFilterRule", [value]))

    @jsii.member(jsii_name="putLinkedHub")
    def put_linked_hub(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IothubDpsLinkedHub", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IothubDps.put_linked_hub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLinkedHub", [value]))

    @jsii.member(jsii_name="putSku")
    def put_sku(self, *, capacity: jsii.Number, name: builtins.str) -> None:
        '''
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#capacity IothubDps#capacity}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#name IothubDps#name}.
        '''
        value = IothubDpsSku(capacity=capacity, name=name)

        return typing.cast(None, jsii.invoke(self, "putSku", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#create IothubDps#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#delete IothubDps#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#read IothubDps#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#update IothubDps#update}.
        '''
        value = IothubDpsTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAllocationPolicy")
    def reset_allocation_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllocationPolicy", []))

    @jsii.member(jsii_name="resetDataResidencyEnabled")
    def reset_data_residency_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataResidencyEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpFilterRule")
    def reset_ip_filter_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpFilterRule", []))

    @jsii.member(jsii_name="resetLinkedHub")
    def reset_linked_hub(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkedHub", []))

    @jsii.member(jsii_name="resetPublicNetworkAccessEnabled")
    def reset_public_network_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicNetworkAccessEnabled", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="deviceProvisioningHostName")
    def device_provisioning_host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceProvisioningHostName"))

    @builtins.property
    @jsii.member(jsii_name="idScope")
    def id_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idScope"))

    @builtins.property
    @jsii.member(jsii_name="ipFilterRule")
    def ip_filter_rule(self) -> "IothubDpsIpFilterRuleList":
        return typing.cast("IothubDpsIpFilterRuleList", jsii.get(self, "ipFilterRule"))

    @builtins.property
    @jsii.member(jsii_name="linkedHub")
    def linked_hub(self) -> "IothubDpsLinkedHubList":
        return typing.cast("IothubDpsLinkedHubList", jsii.get(self, "linkedHub"))

    @builtins.property
    @jsii.member(jsii_name="serviceOperationsHostName")
    def service_operations_host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceOperationsHostName"))

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> "IothubDpsSkuOutputReference":
        return typing.cast("IothubDpsSkuOutputReference", jsii.get(self, "sku"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "IothubDpsTimeoutsOutputReference":
        return typing.cast("IothubDpsTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="allocationPolicyInput")
    def allocation_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocationPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="dataResidencyEnabledInput")
    def data_residency_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dataResidencyEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipFilterRuleInput")
    def ip_filter_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IothubDpsIpFilterRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IothubDpsIpFilterRule"]]], jsii.get(self, "ipFilterRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedHubInput")
    def linked_hub_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IothubDpsLinkedHub"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IothubDpsLinkedHub"]]], jsii.get(self, "linkedHubInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabledInput")
    def public_network_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicNetworkAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional["IothubDpsSku"]:
        return typing.cast(typing.Optional["IothubDpsSku"], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["IothubDpsTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["IothubDpsTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationPolicy")
    def allocation_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allocationPolicy"))

    @allocation_policy.setter
    def allocation_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDps, "allocation_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="dataResidencyEnabled")
    def data_residency_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dataResidencyEnabled"))

    @data_residency_enabled.setter
    def data_residency_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDps, "data_residency_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataResidencyEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDps, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDps, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDps, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabled")
    def public_network_access_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publicNetworkAccessEnabled"))

    @public_network_access_enabled.setter
    def public_network_access_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDps, "public_network_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicNetworkAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDps, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDps, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iothubDps.IothubDpsConfig",
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
        "sku": "sku",
        "allocation_policy": "allocationPolicy",
        "data_residency_enabled": "dataResidencyEnabled",
        "id": "id",
        "ip_filter_rule": "ipFilterRule",
        "linked_hub": "linkedHub",
        "public_network_access_enabled": "publicNetworkAccessEnabled",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class IothubDpsConfig(cdktf.TerraformMetaArguments):
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
        sku: typing.Union["IothubDpsSku", typing.Dict[str, typing.Any]],
        allocation_policy: typing.Optional[builtins.str] = None,
        data_residency_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ip_filter_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IothubDpsIpFilterRule", typing.Dict[str, typing.Any]]]]] = None,
        linked_hub: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IothubDpsLinkedHub", typing.Dict[str, typing.Any]]]]] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["IothubDpsTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#location IothubDps#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#name IothubDps#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#resource_group_name IothubDps#resource_group_name}.
        :param sku: sku block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#sku IothubDps#sku}
        :param allocation_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#allocation_policy IothubDps#allocation_policy}.
        :param data_residency_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#data_residency_enabled IothubDps#data_residency_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#id IothubDps#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_filter_rule: ip_filter_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#ip_filter_rule IothubDps#ip_filter_rule}
        :param linked_hub: linked_hub block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#linked_hub IothubDps#linked_hub}
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#public_network_access_enabled IothubDps#public_network_access_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#tags IothubDps#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#timeouts IothubDps#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(sku, dict):
            sku = IothubDpsSku(**sku)
        if isinstance(timeouts, dict):
            timeouts = IothubDpsTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(IothubDpsConfig.__init__)
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
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument allocation_policy", value=allocation_policy, expected_type=type_hints["allocation_policy"])
            check_type(argname="argument data_residency_enabled", value=data_residency_enabled, expected_type=type_hints["data_residency_enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_filter_rule", value=ip_filter_rule, expected_type=type_hints["ip_filter_rule"])
            check_type(argname="argument linked_hub", value=linked_hub, expected_type=type_hints["linked_hub"])
            check_type(argname="argument public_network_access_enabled", value=public_network_access_enabled, expected_type=type_hints["public_network_access_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "sku": sku,
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
        if allocation_policy is not None:
            self._values["allocation_policy"] = allocation_policy
        if data_residency_enabled is not None:
            self._values["data_residency_enabled"] = data_residency_enabled
        if id is not None:
            self._values["id"] = id
        if ip_filter_rule is not None:
            self._values["ip_filter_rule"] = ip_filter_rule
        if linked_hub is not None:
            self._values["linked_hub"] = linked_hub
        if public_network_access_enabled is not None:
            self._values["public_network_access_enabled"] = public_network_access_enabled
        if tags is not None:
            self._values["tags"] = tags
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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#location IothubDps#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#name IothubDps#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#resource_group_name IothubDps#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> "IothubDpsSku":
        '''sku block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#sku IothubDps#sku}
        '''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast("IothubDpsSku", result)

    @builtins.property
    def allocation_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#allocation_policy IothubDps#allocation_policy}.'''
        result = self._values.get("allocation_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_residency_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#data_residency_enabled IothubDps#data_residency_enabled}.'''
        result = self._values.get("data_residency_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#id IothubDps#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_filter_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IothubDpsIpFilterRule"]]]:
        '''ip_filter_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#ip_filter_rule IothubDps#ip_filter_rule}
        '''
        result = self._values.get("ip_filter_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IothubDpsIpFilterRule"]]], result)

    @builtins.property
    def linked_hub(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IothubDpsLinkedHub"]]]:
        '''linked_hub block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#linked_hub IothubDps#linked_hub}
        '''
        result = self._values.get("linked_hub")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IothubDpsLinkedHub"]]], result)

    @builtins.property
    def public_network_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#public_network_access_enabled IothubDps#public_network_access_enabled}.'''
        result = self._values.get("public_network_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#tags IothubDps#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["IothubDpsTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#timeouts IothubDps#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["IothubDpsTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IothubDpsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iothubDps.IothubDpsIpFilterRule",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "ip_mask": "ipMask",
        "name": "name",
        "target": "target",
    },
)
class IothubDpsIpFilterRule:
    def __init__(
        self,
        *,
        action: builtins.str,
        ip_mask: builtins.str,
        name: builtins.str,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#action IothubDps#action}.
        :param ip_mask: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#ip_mask IothubDps#ip_mask}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#name IothubDps#name}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#target IothubDps#target}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IothubDpsIpFilterRule.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument ip_mask", value=ip_mask, expected_type=type_hints["ip_mask"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "ip_mask": ip_mask,
            "name": name,
        }
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#action IothubDps#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip_mask(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#ip_mask IothubDps#ip_mask}.'''
        result = self._values.get("ip_mask")
        assert result is not None, "Required property 'ip_mask' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#name IothubDps#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#target IothubDps#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IothubDpsIpFilterRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IothubDpsIpFilterRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iothubDps.IothubDpsIpFilterRuleList",
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
            type_hints = typing.get_type_hints(IothubDpsIpFilterRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IothubDpsIpFilterRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IothubDpsIpFilterRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IothubDpsIpFilterRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsIpFilterRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(IothubDpsIpFilterRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(IothubDpsIpFilterRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IothubDpsIpFilterRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IothubDpsIpFilterRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IothubDpsIpFilterRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsIpFilterRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IothubDpsIpFilterRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iothubDps.IothubDpsIpFilterRuleOutputReference",
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
            type_hints = typing.get_type_hints(IothubDpsIpFilterRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="ipMaskInput")
    def ip_mask_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipMaskInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsIpFilterRuleOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="ipMask")
    def ip_mask(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipMask"))

    @ip_mask.setter
    def ip_mask(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsIpFilterRuleOutputReference, "ip_mask").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipMask", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsIpFilterRuleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsIpFilterRuleOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IothubDpsIpFilterRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IothubDpsIpFilterRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IothubDpsIpFilterRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsIpFilterRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iothubDps.IothubDpsLinkedHub",
    jsii_struct_bases=[],
    name_mapping={
        "connection_string": "connectionString",
        "location": "location",
        "allocation_weight": "allocationWeight",
        "apply_allocation_policy": "applyAllocationPolicy",
    },
)
class IothubDpsLinkedHub:
    def __init__(
        self,
        *,
        connection_string: builtins.str,
        location: builtins.str,
        allocation_weight: typing.Optional[jsii.Number] = None,
        apply_allocation_policy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#connection_string IothubDps#connection_string}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#location IothubDps#location}.
        :param allocation_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#allocation_weight IothubDps#allocation_weight}.
        :param apply_allocation_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#apply_allocation_policy IothubDps#apply_allocation_policy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IothubDpsLinkedHub.__init__)
            check_type(argname="argument connection_string", value=connection_string, expected_type=type_hints["connection_string"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument allocation_weight", value=allocation_weight, expected_type=type_hints["allocation_weight"])
            check_type(argname="argument apply_allocation_policy", value=apply_allocation_policy, expected_type=type_hints["apply_allocation_policy"])
        self._values: typing.Dict[str, typing.Any] = {
            "connection_string": connection_string,
            "location": location,
        }
        if allocation_weight is not None:
            self._values["allocation_weight"] = allocation_weight
        if apply_allocation_policy is not None:
            self._values["apply_allocation_policy"] = apply_allocation_policy

    @builtins.property
    def connection_string(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#connection_string IothubDps#connection_string}.'''
        result = self._values.get("connection_string")
        assert result is not None, "Required property 'connection_string' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#location IothubDps#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allocation_weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#allocation_weight IothubDps#allocation_weight}.'''
        result = self._values.get("allocation_weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def apply_allocation_policy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#apply_allocation_policy IothubDps#apply_allocation_policy}.'''
        result = self._values.get("apply_allocation_policy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IothubDpsLinkedHub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IothubDpsLinkedHubList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iothubDps.IothubDpsLinkedHubList",
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
            type_hints = typing.get_type_hints(IothubDpsLinkedHubList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IothubDpsLinkedHubOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IothubDpsLinkedHubList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IothubDpsLinkedHubOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsLinkedHubList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(IothubDpsLinkedHubList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(IothubDpsLinkedHubList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IothubDpsLinkedHub]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IothubDpsLinkedHub]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IothubDpsLinkedHub]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsLinkedHubList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IothubDpsLinkedHubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iothubDps.IothubDpsLinkedHubOutputReference",
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
            type_hints = typing.get_type_hints(IothubDpsLinkedHubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllocationWeight")
    def reset_allocation_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllocationWeight", []))

    @jsii.member(jsii_name="resetApplyAllocationPolicy")
    def reset_apply_allocation_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplyAllocationPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="allocationWeightInput")
    def allocation_weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "allocationWeightInput"))

    @builtins.property
    @jsii.member(jsii_name="applyAllocationPolicyInput")
    def apply_allocation_policy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "applyAllocationPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionStringInput")
    def connection_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionStringInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationWeight")
    def allocation_weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "allocationWeight"))

    @allocation_weight.setter
    def allocation_weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsLinkedHubOutputReference, "allocation_weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationWeight", value)

    @builtins.property
    @jsii.member(jsii_name="applyAllocationPolicy")
    def apply_allocation_policy(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "applyAllocationPolicy"))

    @apply_allocation_policy.setter
    def apply_allocation_policy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsLinkedHubOutputReference, "apply_allocation_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applyAllocationPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="connectionString")
    def connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionString"))

    @connection_string.setter
    def connection_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsLinkedHubOutputReference, "connection_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionString", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsLinkedHubOutputReference, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IothubDpsLinkedHub, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IothubDpsLinkedHub, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IothubDpsLinkedHub, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsLinkedHubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iothubDps.IothubDpsSku",
    jsii_struct_bases=[],
    name_mapping={"capacity": "capacity", "name": "name"},
)
class IothubDpsSku:
    def __init__(self, *, capacity: jsii.Number, name: builtins.str) -> None:
        '''
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#capacity IothubDps#capacity}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#name IothubDps#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IothubDpsSku.__init__)
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "capacity": capacity,
            "name": name,
        }

    @builtins.property
    def capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#capacity IothubDps#capacity}.'''
        result = self._values.get("capacity")
        assert result is not None, "Required property 'capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#name IothubDps#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IothubDpsSku(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IothubDpsSkuOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iothubDps.IothubDpsSkuOutputReference",
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
            type_hints = typing.get_type_hints(IothubDpsSkuOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsSkuOutputReference, "capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacity", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsSkuOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IothubDpsSku]:
        return typing.cast(typing.Optional[IothubDpsSku], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IothubDpsSku]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsSkuOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iothubDps.IothubDpsTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class IothubDpsTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#create IothubDps#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#delete IothubDps#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#read IothubDps#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#update IothubDps#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IothubDpsTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#create IothubDps#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#delete IothubDps#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#read IothubDps#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps#update IothubDps#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IothubDpsTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IothubDpsTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iothubDps.IothubDpsTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(IothubDpsTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(IothubDpsTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IothubDpsTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IothubDpsTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IothubDpsTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "IothubDps",
    "IothubDpsConfig",
    "IothubDpsIpFilterRule",
    "IothubDpsIpFilterRuleList",
    "IothubDpsIpFilterRuleOutputReference",
    "IothubDpsLinkedHub",
    "IothubDpsLinkedHubList",
    "IothubDpsLinkedHubOutputReference",
    "IothubDpsSku",
    "IothubDpsSkuOutputReference",
    "IothubDpsTimeouts",
    "IothubDpsTimeoutsOutputReference",
]

publication.publish()
