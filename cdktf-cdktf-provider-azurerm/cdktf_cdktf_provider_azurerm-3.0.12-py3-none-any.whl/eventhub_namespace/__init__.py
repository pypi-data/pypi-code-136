'''
# `azurerm_eventhub_namespace`

Refer to the Terraform Registory for docs: [`azurerm_eventhub_namespace`](https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace).
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


class EventhubNamespace(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventhubNamespace.EventhubNamespace",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace azurerm_eventhub_namespace}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku: builtins.str,
        auto_inflate_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        capacity: typing.Optional[jsii.Number] = None,
        dedicated_cluster_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["EventhubNamespaceIdentity", typing.Dict[str, typing.Any]]] = None,
        local_authentication_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        maximum_throughput_units: typing.Optional[jsii.Number] = None,
        minimum_tls_version: typing.Optional[builtins.str] = None,
        network_rulesets: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventhubNamespaceNetworkRulesets", typing.Dict[str, typing.Any]]]]] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["EventhubNamespaceTimeouts", typing.Dict[str, typing.Any]]] = None,
        zone_redundant: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace azurerm_eventhub_namespace} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#location EventhubNamespace#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#name EventhubNamespace#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#resource_group_name EventhubNamespace#resource_group_name}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#sku EventhubNamespace#sku}.
        :param auto_inflate_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#auto_inflate_enabled EventhubNamespace#auto_inflate_enabled}.
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#capacity EventhubNamespace#capacity}.
        :param dedicated_cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#dedicated_cluster_id EventhubNamespace#dedicated_cluster_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#id EventhubNamespace#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#identity EventhubNamespace#identity}
        :param local_authentication_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#local_authentication_enabled EventhubNamespace#local_authentication_enabled}.
        :param maximum_throughput_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#maximum_throughput_units EventhubNamespace#maximum_throughput_units}.
        :param minimum_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#minimum_tls_version EventhubNamespace#minimum_tls_version}.
        :param network_rulesets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#network_rulesets EventhubNamespace#network_rulesets}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#public_network_access_enabled EventhubNamespace#public_network_access_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#tags EventhubNamespace#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#timeouts EventhubNamespace#timeouts}
        :param zone_redundant: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#zone_redundant EventhubNamespace#zone_redundant}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventhubNamespace.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EventhubNamespaceConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            sku=sku,
            auto_inflate_enabled=auto_inflate_enabled,
            capacity=capacity,
            dedicated_cluster_id=dedicated_cluster_id,
            id=id,
            identity=identity,
            local_authentication_enabled=local_authentication_enabled,
            maximum_throughput_units=maximum_throughput_units,
            minimum_tls_version=minimum_tls_version,
            network_rulesets=network_rulesets,
            public_network_access_enabled=public_network_access_enabled,
            tags=tags,
            timeouts=timeouts,
            zone_redundant=zone_redundant,
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
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#type EventhubNamespace#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#identity_ids EventhubNamespace#identity_ids}.
        '''
        value = EventhubNamespaceIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putNetworkRulesets")
    def put_network_rulesets(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventhubNamespaceNetworkRulesets", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventhubNamespace.put_network_rulesets)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkRulesets", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#create EventhubNamespace#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#delete EventhubNamespace#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#read EventhubNamespace#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#update EventhubNamespace#update}.
        '''
        value = EventhubNamespaceTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAutoInflateEnabled")
    def reset_auto_inflate_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoInflateEnabled", []))

    @jsii.member(jsii_name="resetCapacity")
    def reset_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacity", []))

    @jsii.member(jsii_name="resetDedicatedClusterId")
    def reset_dedicated_cluster_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDedicatedClusterId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetLocalAuthenticationEnabled")
    def reset_local_authentication_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalAuthenticationEnabled", []))

    @jsii.member(jsii_name="resetMaximumThroughputUnits")
    def reset_maximum_throughput_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumThroughputUnits", []))

    @jsii.member(jsii_name="resetMinimumTlsVersion")
    def reset_minimum_tls_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumTlsVersion", []))

    @jsii.member(jsii_name="resetNetworkRulesets")
    def reset_network_rulesets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkRulesets", []))

    @jsii.member(jsii_name="resetPublicNetworkAccessEnabled")
    def reset_public_network_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicNetworkAccessEnabled", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetZoneRedundant")
    def reset_zone_redundant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneRedundant", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="defaultPrimaryConnectionString")
    def default_primary_connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultPrimaryConnectionString"))

    @builtins.property
    @jsii.member(jsii_name="defaultPrimaryConnectionStringAlias")
    def default_primary_connection_string_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultPrimaryConnectionStringAlias"))

    @builtins.property
    @jsii.member(jsii_name="defaultPrimaryKey")
    def default_primary_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultPrimaryKey"))

    @builtins.property
    @jsii.member(jsii_name="defaultSecondaryConnectionString")
    def default_secondary_connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultSecondaryConnectionString"))

    @builtins.property
    @jsii.member(jsii_name="defaultSecondaryConnectionStringAlias")
    def default_secondary_connection_string_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultSecondaryConnectionStringAlias"))

    @builtins.property
    @jsii.member(jsii_name="defaultSecondaryKey")
    def default_secondary_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultSecondaryKey"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "EventhubNamespaceIdentityOutputReference":
        return typing.cast("EventhubNamespaceIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="networkRulesets")
    def network_rulesets(self) -> "EventhubNamespaceNetworkRulesetsList":
        return typing.cast("EventhubNamespaceNetworkRulesetsList", jsii.get(self, "networkRulesets"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "EventhubNamespaceTimeoutsOutputReference":
        return typing.cast("EventhubNamespaceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="autoInflateEnabledInput")
    def auto_inflate_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoInflateEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="dedicatedClusterIdInput")
    def dedicated_cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dedicatedClusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["EventhubNamespaceIdentity"]:
        return typing.cast(typing.Optional["EventhubNamespaceIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="localAuthenticationEnabledInput")
    def local_authentication_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "localAuthenticationEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumThroughputUnitsInput")
    def maximum_throughput_units_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumThroughputUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumTlsVersionInput")
    def minimum_tls_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumTlsVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkRulesetsInput")
    def network_rulesets_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventhubNamespaceNetworkRulesets"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventhubNamespaceNetworkRulesets"]]], jsii.get(self, "networkRulesetsInput"))

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
    def sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["EventhubNamespaceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["EventhubNamespaceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneRedundantInput")
    def zone_redundant_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "zoneRedundantInput"))

    @builtins.property
    @jsii.member(jsii_name="autoInflateEnabled")
    def auto_inflate_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoInflateEnabled"))

    @auto_inflate_enabled.setter
    def auto_inflate_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespace, "auto_inflate_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoInflateEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespace, "capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacity", value)

    @builtins.property
    @jsii.member(jsii_name="dedicatedClusterId")
    def dedicated_cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dedicatedClusterId"))

    @dedicated_cluster_id.setter
    def dedicated_cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespace, "dedicated_cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dedicatedClusterId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespace, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="localAuthenticationEnabled")
    def local_authentication_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "localAuthenticationEnabled"))

    @local_authentication_enabled.setter
    def local_authentication_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespace, "local_authentication_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localAuthenticationEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespace, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="maximumThroughputUnits")
    def maximum_throughput_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumThroughputUnits"))

    @maximum_throughput_units.setter
    def maximum_throughput_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespace, "maximum_throughput_units").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumThroughputUnits", value)

    @builtins.property
    @jsii.member(jsii_name="minimumTlsVersion")
    def minimum_tls_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimumTlsVersion"))

    @minimum_tls_version.setter
    def minimum_tls_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespace, "minimum_tls_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumTlsVersion", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespace, "name").fset)
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
            type_hints = typing.get_type_hints(getattr(EventhubNamespace, "public_network_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicNetworkAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespace, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespace, "sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespace, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="zoneRedundant")
    def zone_redundant(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "zoneRedundant"))

    @zone_redundant.setter
    def zone_redundant(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespace, "zone_redundant").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneRedundant", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventhubNamespace.EventhubNamespaceConfig",
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
        "auto_inflate_enabled": "autoInflateEnabled",
        "capacity": "capacity",
        "dedicated_cluster_id": "dedicatedClusterId",
        "id": "id",
        "identity": "identity",
        "local_authentication_enabled": "localAuthenticationEnabled",
        "maximum_throughput_units": "maximumThroughputUnits",
        "minimum_tls_version": "minimumTlsVersion",
        "network_rulesets": "networkRulesets",
        "public_network_access_enabled": "publicNetworkAccessEnabled",
        "tags": "tags",
        "timeouts": "timeouts",
        "zone_redundant": "zoneRedundant",
    },
)
class EventhubNamespaceConfig(cdktf.TerraformMetaArguments):
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
        sku: builtins.str,
        auto_inflate_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        capacity: typing.Optional[jsii.Number] = None,
        dedicated_cluster_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["EventhubNamespaceIdentity", typing.Dict[str, typing.Any]]] = None,
        local_authentication_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        maximum_throughput_units: typing.Optional[jsii.Number] = None,
        minimum_tls_version: typing.Optional[builtins.str] = None,
        network_rulesets: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventhubNamespaceNetworkRulesets", typing.Dict[str, typing.Any]]]]] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["EventhubNamespaceTimeouts", typing.Dict[str, typing.Any]]] = None,
        zone_redundant: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#location EventhubNamespace#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#name EventhubNamespace#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#resource_group_name EventhubNamespace#resource_group_name}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#sku EventhubNamespace#sku}.
        :param auto_inflate_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#auto_inflate_enabled EventhubNamespace#auto_inflate_enabled}.
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#capacity EventhubNamespace#capacity}.
        :param dedicated_cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#dedicated_cluster_id EventhubNamespace#dedicated_cluster_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#id EventhubNamespace#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#identity EventhubNamespace#identity}
        :param local_authentication_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#local_authentication_enabled EventhubNamespace#local_authentication_enabled}.
        :param maximum_throughput_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#maximum_throughput_units EventhubNamespace#maximum_throughput_units}.
        :param minimum_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#minimum_tls_version EventhubNamespace#minimum_tls_version}.
        :param network_rulesets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#network_rulesets EventhubNamespace#network_rulesets}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#public_network_access_enabled EventhubNamespace#public_network_access_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#tags EventhubNamespace#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#timeouts EventhubNamespace#timeouts}
        :param zone_redundant: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#zone_redundant EventhubNamespace#zone_redundant}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(identity, dict):
            identity = EventhubNamespaceIdentity(**identity)
        if isinstance(timeouts, dict):
            timeouts = EventhubNamespaceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(EventhubNamespaceConfig.__init__)
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
            check_type(argname="argument auto_inflate_enabled", value=auto_inflate_enabled, expected_type=type_hints["auto_inflate_enabled"])
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument dedicated_cluster_id", value=dedicated_cluster_id, expected_type=type_hints["dedicated_cluster_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument local_authentication_enabled", value=local_authentication_enabled, expected_type=type_hints["local_authentication_enabled"])
            check_type(argname="argument maximum_throughput_units", value=maximum_throughput_units, expected_type=type_hints["maximum_throughput_units"])
            check_type(argname="argument minimum_tls_version", value=minimum_tls_version, expected_type=type_hints["minimum_tls_version"])
            check_type(argname="argument network_rulesets", value=network_rulesets, expected_type=type_hints["network_rulesets"])
            check_type(argname="argument public_network_access_enabled", value=public_network_access_enabled, expected_type=type_hints["public_network_access_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument zone_redundant", value=zone_redundant, expected_type=type_hints["zone_redundant"])
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
        if auto_inflate_enabled is not None:
            self._values["auto_inflate_enabled"] = auto_inflate_enabled
        if capacity is not None:
            self._values["capacity"] = capacity
        if dedicated_cluster_id is not None:
            self._values["dedicated_cluster_id"] = dedicated_cluster_id
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if local_authentication_enabled is not None:
            self._values["local_authentication_enabled"] = local_authentication_enabled
        if maximum_throughput_units is not None:
            self._values["maximum_throughput_units"] = maximum_throughput_units
        if minimum_tls_version is not None:
            self._values["minimum_tls_version"] = minimum_tls_version
        if network_rulesets is not None:
            self._values["network_rulesets"] = network_rulesets
        if public_network_access_enabled is not None:
            self._values["public_network_access_enabled"] = public_network_access_enabled
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if zone_redundant is not None:
            self._values["zone_redundant"] = zone_redundant

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#location EventhubNamespace#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#name EventhubNamespace#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#resource_group_name EventhubNamespace#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#sku EventhubNamespace#sku}.'''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_inflate_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#auto_inflate_enabled EventhubNamespace#auto_inflate_enabled}.'''
        result = self._values.get("auto_inflate_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#capacity EventhubNamespace#capacity}.'''
        result = self._values.get("capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dedicated_cluster_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#dedicated_cluster_id EventhubNamespace#dedicated_cluster_id}.'''
        result = self._values.get("dedicated_cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#id EventhubNamespace#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["EventhubNamespaceIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#identity EventhubNamespace#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["EventhubNamespaceIdentity"], result)

    @builtins.property
    def local_authentication_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#local_authentication_enabled EventhubNamespace#local_authentication_enabled}.'''
        result = self._values.get("local_authentication_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def maximum_throughput_units(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#maximum_throughput_units EventhubNamespace#maximum_throughput_units}.'''
        result = self._values.get("maximum_throughput_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minimum_tls_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#minimum_tls_version EventhubNamespace#minimum_tls_version}.'''
        result = self._values.get("minimum_tls_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_rulesets(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventhubNamespaceNetworkRulesets"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#network_rulesets EventhubNamespace#network_rulesets}.'''
        result = self._values.get("network_rulesets")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventhubNamespaceNetworkRulesets"]]], result)

    @builtins.property
    def public_network_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#public_network_access_enabled EventhubNamespace#public_network_access_enabled}.'''
        result = self._values.get("public_network_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#tags EventhubNamespace#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["EventhubNamespaceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#timeouts EventhubNamespace#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["EventhubNamespaceTimeouts"], result)

    @builtins.property
    def zone_redundant(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#zone_redundant EventhubNamespace#zone_redundant}.'''
        result = self._values.get("zone_redundant")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventhubNamespaceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventhubNamespace.EventhubNamespaceIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class EventhubNamespaceIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#type EventhubNamespace#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#identity_ids EventhubNamespace#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventhubNamespaceIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#type EventhubNamespace#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#identity_ids EventhubNamespace#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventhubNamespaceIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventhubNamespaceIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventhubNamespace.EventhubNamespaceIdentityOutputReference",
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
            type_hints = typing.get_type_hints(EventhubNamespaceIdentityOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EventhubNamespaceIdentity]:
        return typing.cast(typing.Optional[EventhubNamespaceIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[EventhubNamespaceIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventhubNamespace.EventhubNamespaceNetworkRulesets",
    jsii_struct_bases=[],
    name_mapping={
        "default_action": "defaultAction",
        "ip_rule": "ipRule",
        "public_network_access_enabled": "publicNetworkAccessEnabled",
        "trusted_service_access_enabled": "trustedServiceAccessEnabled",
        "virtual_network_rule": "virtualNetworkRule",
    },
)
class EventhubNamespaceNetworkRulesets:
    def __init__(
        self,
        *,
        default_action: typing.Optional[builtins.str] = None,
        ip_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventhubNamespaceNetworkRulesetsIpRule", typing.Dict[str, typing.Any]]]]] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        trusted_service_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        virtual_network_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventhubNamespaceNetworkRulesetsVirtualNetworkRule", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param default_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#default_action EventhubNamespace#default_action}.
        :param ip_rule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#ip_rule EventhubNamespace#ip_rule}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#public_network_access_enabled EventhubNamespace#public_network_access_enabled}.
        :param trusted_service_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#trusted_service_access_enabled EventhubNamespace#trusted_service_access_enabled}.
        :param virtual_network_rule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#virtual_network_rule EventhubNamespace#virtual_network_rule}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventhubNamespaceNetworkRulesets.__init__)
            check_type(argname="argument default_action", value=default_action, expected_type=type_hints["default_action"])
            check_type(argname="argument ip_rule", value=ip_rule, expected_type=type_hints["ip_rule"])
            check_type(argname="argument public_network_access_enabled", value=public_network_access_enabled, expected_type=type_hints["public_network_access_enabled"])
            check_type(argname="argument trusted_service_access_enabled", value=trusted_service_access_enabled, expected_type=type_hints["trusted_service_access_enabled"])
            check_type(argname="argument virtual_network_rule", value=virtual_network_rule, expected_type=type_hints["virtual_network_rule"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default_action is not None:
            self._values["default_action"] = default_action
        if ip_rule is not None:
            self._values["ip_rule"] = ip_rule
        if public_network_access_enabled is not None:
            self._values["public_network_access_enabled"] = public_network_access_enabled
        if trusted_service_access_enabled is not None:
            self._values["trusted_service_access_enabled"] = trusted_service_access_enabled
        if virtual_network_rule is not None:
            self._values["virtual_network_rule"] = virtual_network_rule

    @builtins.property
    def default_action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#default_action EventhubNamespace#default_action}.'''
        result = self._values.get("default_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventhubNamespaceNetworkRulesetsIpRule"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#ip_rule EventhubNamespace#ip_rule}.'''
        result = self._values.get("ip_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventhubNamespaceNetworkRulesetsIpRule"]]], result)

    @builtins.property
    def public_network_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#public_network_access_enabled EventhubNamespace#public_network_access_enabled}.'''
        result = self._values.get("public_network_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def trusted_service_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#trusted_service_access_enabled EventhubNamespace#trusted_service_access_enabled}.'''
        result = self._values.get("trusted_service_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def virtual_network_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventhubNamespaceNetworkRulesetsVirtualNetworkRule"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#virtual_network_rule EventhubNamespace#virtual_network_rule}.'''
        result = self._values.get("virtual_network_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventhubNamespaceNetworkRulesetsVirtualNetworkRule"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventhubNamespaceNetworkRulesets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventhubNamespace.EventhubNamespaceNetworkRulesetsIpRule",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "ip_mask": "ipMask"},
)
class EventhubNamespaceNetworkRulesetsIpRule:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        ip_mask: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#action EventhubNamespace#action}.
        :param ip_mask: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#ip_mask EventhubNamespace#ip_mask}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventhubNamespaceNetworkRulesetsIpRule.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument ip_mask", value=ip_mask, expected_type=type_hints["ip_mask"])
        self._values: typing.Dict[str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if ip_mask is not None:
            self._values["ip_mask"] = ip_mask

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#action EventhubNamespace#action}.'''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_mask(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#ip_mask EventhubNamespace#ip_mask}.'''
        result = self._values.get("ip_mask")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventhubNamespaceNetworkRulesetsIpRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventhubNamespaceNetworkRulesetsIpRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventhubNamespace.EventhubNamespaceNetworkRulesetsIpRuleList",
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
            type_hints = typing.get_type_hints(EventhubNamespaceNetworkRulesetsIpRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventhubNamespaceNetworkRulesetsIpRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventhubNamespaceNetworkRulesetsIpRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventhubNamespaceNetworkRulesetsIpRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsIpRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsIpRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsIpRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventhubNamespaceNetworkRulesetsIpRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventhubNamespaceNetworkRulesetsIpRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventhubNamespaceNetworkRulesetsIpRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsIpRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventhubNamespaceNetworkRulesetsIpRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventhubNamespace.EventhubNamespaceNetworkRulesetsIpRuleOutputReference",
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
            type_hints = typing.get_type_hints(EventhubNamespaceNetworkRulesetsIpRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetIpMask")
    def reset_ip_mask(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpMask", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="ipMaskInput")
    def ip_mask_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipMaskInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsIpRuleOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="ipMask")
    def ip_mask(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipMask"))

    @ip_mask.setter
    def ip_mask(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsIpRuleOutputReference, "ip_mask").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipMask", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventhubNamespaceNetworkRulesetsIpRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventhubNamespaceNetworkRulesetsIpRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventhubNamespaceNetworkRulesetsIpRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsIpRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventhubNamespaceNetworkRulesetsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventhubNamespace.EventhubNamespaceNetworkRulesetsList",
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
            type_hints = typing.get_type_hints(EventhubNamespaceNetworkRulesetsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventhubNamespaceNetworkRulesetsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventhubNamespaceNetworkRulesetsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventhubNamespaceNetworkRulesetsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventhubNamespaceNetworkRulesets]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventhubNamespaceNetworkRulesets]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventhubNamespaceNetworkRulesets]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventhubNamespaceNetworkRulesetsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventhubNamespace.EventhubNamespaceNetworkRulesetsOutputReference",
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
            type_hints = typing.get_type_hints(EventhubNamespaceNetworkRulesetsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putIpRule")
    def put_ip_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventhubNamespaceNetworkRulesetsIpRule, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventhubNamespaceNetworkRulesetsOutputReference.put_ip_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpRule", [value]))

    @jsii.member(jsii_name="putVirtualNetworkRule")
    def put_virtual_network_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventhubNamespaceNetworkRulesetsVirtualNetworkRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventhubNamespaceNetworkRulesetsOutputReference.put_virtual_network_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVirtualNetworkRule", [value]))

    @jsii.member(jsii_name="resetDefaultAction")
    def reset_default_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultAction", []))

    @jsii.member(jsii_name="resetIpRule")
    def reset_ip_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpRule", []))

    @jsii.member(jsii_name="resetPublicNetworkAccessEnabled")
    def reset_public_network_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicNetworkAccessEnabled", []))

    @jsii.member(jsii_name="resetTrustedServiceAccessEnabled")
    def reset_trusted_service_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustedServiceAccessEnabled", []))

    @jsii.member(jsii_name="resetVirtualNetworkRule")
    def reset_virtual_network_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkRule", []))

    @builtins.property
    @jsii.member(jsii_name="ipRule")
    def ip_rule(self) -> EventhubNamespaceNetworkRulesetsIpRuleList:
        return typing.cast(EventhubNamespaceNetworkRulesetsIpRuleList, jsii.get(self, "ipRule"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkRule")
    def virtual_network_rule(
        self,
    ) -> "EventhubNamespaceNetworkRulesetsVirtualNetworkRuleList":
        return typing.cast("EventhubNamespaceNetworkRulesetsVirtualNetworkRuleList", jsii.get(self, "virtualNetworkRule"))

    @builtins.property
    @jsii.member(jsii_name="defaultActionInput")
    def default_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultActionInput"))

    @builtins.property
    @jsii.member(jsii_name="ipRuleInput")
    def ip_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventhubNamespaceNetworkRulesetsIpRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventhubNamespaceNetworkRulesetsIpRule]]], jsii.get(self, "ipRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabledInput")
    def public_network_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicNetworkAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="trustedServiceAccessEnabledInput")
    def trusted_service_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "trustedServiceAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkRuleInput")
    def virtual_network_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventhubNamespaceNetworkRulesetsVirtualNetworkRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventhubNamespaceNetworkRulesetsVirtualNetworkRule"]]], jsii.get(self, "virtualNetworkRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultAction")
    def default_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultAction"))

    @default_action.setter
    def default_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsOutputReference, "default_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAction", value)

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
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsOutputReference, "public_network_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicNetworkAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="trustedServiceAccessEnabled")
    def trusted_service_access_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "trustedServiceAccessEnabled"))

    @trusted_service_access_enabled.setter
    def trusted_service_access_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsOutputReference, "trusted_service_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustedServiceAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventhubNamespaceNetworkRulesets, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventhubNamespaceNetworkRulesets, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventhubNamespaceNetworkRulesets, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventhubNamespace.EventhubNamespaceNetworkRulesetsVirtualNetworkRule",
    jsii_struct_bases=[],
    name_mapping={
        "ignore_missing_virtual_network_service_endpoint": "ignoreMissingVirtualNetworkServiceEndpoint",
        "subnet_id": "subnetId",
    },
)
class EventhubNamespaceNetworkRulesetsVirtualNetworkRule:
    def __init__(
        self,
        *,
        ignore_missing_virtual_network_service_endpoint: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ignore_missing_virtual_network_service_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#ignore_missing_virtual_network_service_endpoint EventhubNamespace#ignore_missing_virtual_network_service_endpoint}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#subnet_id EventhubNamespace#subnet_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventhubNamespaceNetworkRulesetsVirtualNetworkRule.__init__)
            check_type(argname="argument ignore_missing_virtual_network_service_endpoint", value=ignore_missing_virtual_network_service_endpoint, expected_type=type_hints["ignore_missing_virtual_network_service_endpoint"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ignore_missing_virtual_network_service_endpoint is not None:
            self._values["ignore_missing_virtual_network_service_endpoint"] = ignore_missing_virtual_network_service_endpoint
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id

    @builtins.property
    def ignore_missing_virtual_network_service_endpoint(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#ignore_missing_virtual_network_service_endpoint EventhubNamespace#ignore_missing_virtual_network_service_endpoint}.'''
        result = self._values.get("ignore_missing_virtual_network_service_endpoint")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#subnet_id EventhubNamespace#subnet_id}.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventhubNamespaceNetworkRulesetsVirtualNetworkRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventhubNamespaceNetworkRulesetsVirtualNetworkRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventhubNamespace.EventhubNamespaceNetworkRulesetsVirtualNetworkRuleList",
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
            type_hints = typing.get_type_hints(EventhubNamespaceNetworkRulesetsVirtualNetworkRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventhubNamespaceNetworkRulesetsVirtualNetworkRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventhubNamespaceNetworkRulesetsVirtualNetworkRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventhubNamespaceNetworkRulesetsVirtualNetworkRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsVirtualNetworkRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsVirtualNetworkRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsVirtualNetworkRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventhubNamespaceNetworkRulesetsVirtualNetworkRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventhubNamespaceNetworkRulesetsVirtualNetworkRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventhubNamespaceNetworkRulesetsVirtualNetworkRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsVirtualNetworkRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventhubNamespaceNetworkRulesetsVirtualNetworkRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventhubNamespace.EventhubNamespaceNetworkRulesetsVirtualNetworkRuleOutputReference",
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
            type_hints = typing.get_type_hints(EventhubNamespaceNetworkRulesetsVirtualNetworkRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIgnoreMissingVirtualNetworkServiceEndpoint")
    def reset_ignore_missing_virtual_network_service_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreMissingVirtualNetworkServiceEndpoint", []))

    @jsii.member(jsii_name="resetSubnetId")
    def reset_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetId", []))

    @builtins.property
    @jsii.member(jsii_name="ignoreMissingVirtualNetworkServiceEndpointInput")
    def ignore_missing_virtual_network_service_endpoint_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreMissingVirtualNetworkServiceEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreMissingVirtualNetworkServiceEndpoint")
    def ignore_missing_virtual_network_service_endpoint(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreMissingVirtualNetworkServiceEndpoint"))

    @ignore_missing_virtual_network_service_endpoint.setter
    def ignore_missing_virtual_network_service_endpoint(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsVirtualNetworkRuleOutputReference, "ignore_missing_virtual_network_service_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreMissingVirtualNetworkServiceEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsVirtualNetworkRuleOutputReference, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventhubNamespaceNetworkRulesetsVirtualNetworkRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventhubNamespaceNetworkRulesetsVirtualNetworkRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventhubNamespaceNetworkRulesetsVirtualNetworkRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceNetworkRulesetsVirtualNetworkRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventhubNamespace.EventhubNamespaceTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class EventhubNamespaceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#create EventhubNamespace#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#delete EventhubNamespace#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#read EventhubNamespace#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#update EventhubNamespace#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventhubNamespaceTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#create EventhubNamespace#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#delete EventhubNamespace#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#read EventhubNamespace#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace#update EventhubNamespace#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventhubNamespaceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventhubNamespaceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventhubNamespace.EventhubNamespaceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(EventhubNamespaceTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventhubNamespaceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventhubNamespaceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventhubNamespaceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubNamespaceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "EventhubNamespace",
    "EventhubNamespaceConfig",
    "EventhubNamespaceIdentity",
    "EventhubNamespaceIdentityOutputReference",
    "EventhubNamespaceNetworkRulesets",
    "EventhubNamespaceNetworkRulesetsIpRule",
    "EventhubNamespaceNetworkRulesetsIpRuleList",
    "EventhubNamespaceNetworkRulesetsIpRuleOutputReference",
    "EventhubNamespaceNetworkRulesetsList",
    "EventhubNamespaceNetworkRulesetsOutputReference",
    "EventhubNamespaceNetworkRulesetsVirtualNetworkRule",
    "EventhubNamespaceNetworkRulesetsVirtualNetworkRuleList",
    "EventhubNamespaceNetworkRulesetsVirtualNetworkRuleOutputReference",
    "EventhubNamespaceTimeouts",
    "EventhubNamespaceTimeoutsOutputReference",
]

publication.publish()
