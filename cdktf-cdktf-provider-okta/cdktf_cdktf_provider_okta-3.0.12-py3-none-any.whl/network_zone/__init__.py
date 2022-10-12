'''
# `okta_network_zone`

Refer to the Terraform Registory for docs: [`okta_network_zone`](https://www.terraform.io/docs/providers/okta/r/network_zone).
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


class NetworkZone(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-okta.networkZone.NetworkZone",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/okta/r/network_zone okta_network_zone}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        asns: typing.Optional[typing.Sequence[builtins.str]] = None,
        dynamic_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
        dynamic_proxy_type: typing.Optional[builtins.str] = None,
        gateways: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        proxies: typing.Optional[typing.Sequence[builtins.str]] = None,
        usage: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/okta/r/network_zone okta_network_zone} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the Network Zone Resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#name NetworkZone#name}
        :param type: Type of the Network Zone - can either be IP or DYNAMIC only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#type NetworkZone#type}
        :param asns: Format of each array value: a string representation of an ASN numeric value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#asns NetworkZone#asns}
        :param dynamic_locations: Array of locations ISO-3166-1(2). Format code: countryCode OR countryCode-regionCode. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#dynamic_locations NetworkZone#dynamic_locations}
        :param dynamic_proxy_type: Type of proxy being controlled by this network zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#dynamic_proxy_type NetworkZone#dynamic_proxy_type}
        :param gateways: Array of values in CIDR/range form depending on the way it's been declared (i.e. CIDR will contain /suffix). Please check API docs for examples. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#gateways NetworkZone#gateways}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#id NetworkZone#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param proxies: Array of values in CIDR/range form depending on the way it's been declared (i.e. CIDR will contain /suffix). Please check API docs for examples. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#proxies NetworkZone#proxies}
        :param usage: Zone's purpose: POLICY or BLOCKLIST. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#usage NetworkZone#usage}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkZone.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NetworkZoneConfig(
            name=name,
            type=type,
            asns=asns,
            dynamic_locations=dynamic_locations,
            dynamic_proxy_type=dynamic_proxy_type,
            gateways=gateways,
            id=id,
            proxies=proxies,
            usage=usage,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAsns")
    def reset_asns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAsns", []))

    @jsii.member(jsii_name="resetDynamicLocations")
    def reset_dynamic_locations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamicLocations", []))

    @jsii.member(jsii_name="resetDynamicProxyType")
    def reset_dynamic_proxy_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamicProxyType", []))

    @jsii.member(jsii_name="resetGateways")
    def reset_gateways(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGateways", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProxies")
    def reset_proxies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxies", []))

    @jsii.member(jsii_name="resetUsage")
    def reset_usage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsage", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="asnsInput")
    def asns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "asnsInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamicLocationsInput")
    def dynamic_locations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dynamicLocationsInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamicProxyTypeInput")
    def dynamic_proxy_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dynamicProxyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewaysInput")
    def gateways_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "gatewaysInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="proxiesInput")
    def proxies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "proxiesInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="usageInput")
    def usage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usageInput"))

    @builtins.property
    @jsii.member(jsii_name="asns")
    def asns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "asns"))

    @asns.setter
    def asns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkZone, "asns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "asns", value)

    @builtins.property
    @jsii.member(jsii_name="dynamicLocations")
    def dynamic_locations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dynamicLocations"))

    @dynamic_locations.setter
    def dynamic_locations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkZone, "dynamic_locations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynamicLocations", value)

    @builtins.property
    @jsii.member(jsii_name="dynamicProxyType")
    def dynamic_proxy_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dynamicProxyType"))

    @dynamic_proxy_type.setter
    def dynamic_proxy_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkZone, "dynamic_proxy_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynamicProxyType", value)

    @builtins.property
    @jsii.member(jsii_name="gateways")
    def gateways(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "gateways"))

    @gateways.setter
    def gateways(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkZone, "gateways").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gateways", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkZone, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkZone, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="proxies")
    def proxies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "proxies"))

    @proxies.setter
    def proxies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkZone, "proxies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxies", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkZone, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="usage")
    def usage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usage"))

    @usage.setter
    def usage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkZone, "usage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usage", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-okta.networkZone.NetworkZoneConfig",
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
        "type": "type",
        "asns": "asns",
        "dynamic_locations": "dynamicLocations",
        "dynamic_proxy_type": "dynamicProxyType",
        "gateways": "gateways",
        "id": "id",
        "proxies": "proxies",
        "usage": "usage",
    },
)
class NetworkZoneConfig(cdktf.TerraformMetaArguments):
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
        type: builtins.str,
        asns: typing.Optional[typing.Sequence[builtins.str]] = None,
        dynamic_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
        dynamic_proxy_type: typing.Optional[builtins.str] = None,
        gateways: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        proxies: typing.Optional[typing.Sequence[builtins.str]] = None,
        usage: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the Network Zone Resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#name NetworkZone#name}
        :param type: Type of the Network Zone - can either be IP or DYNAMIC only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#type NetworkZone#type}
        :param asns: Format of each array value: a string representation of an ASN numeric value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#asns NetworkZone#asns}
        :param dynamic_locations: Array of locations ISO-3166-1(2). Format code: countryCode OR countryCode-regionCode. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#dynamic_locations NetworkZone#dynamic_locations}
        :param dynamic_proxy_type: Type of proxy being controlled by this network zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#dynamic_proxy_type NetworkZone#dynamic_proxy_type}
        :param gateways: Array of values in CIDR/range form depending on the way it's been declared (i.e. CIDR will contain /suffix). Please check API docs for examples. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#gateways NetworkZone#gateways}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#id NetworkZone#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param proxies: Array of values in CIDR/range form depending on the way it's been declared (i.e. CIDR will contain /suffix). Please check API docs for examples. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#proxies NetworkZone#proxies}
        :param usage: Zone's purpose: POLICY or BLOCKLIST. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#usage NetworkZone#usage}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(NetworkZoneConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument asns", value=asns, expected_type=type_hints["asns"])
            check_type(argname="argument dynamic_locations", value=dynamic_locations, expected_type=type_hints["dynamic_locations"])
            check_type(argname="argument dynamic_proxy_type", value=dynamic_proxy_type, expected_type=type_hints["dynamic_proxy_type"])
            check_type(argname="argument gateways", value=gateways, expected_type=type_hints["gateways"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument proxies", value=proxies, expected_type=type_hints["proxies"])
            check_type(argname="argument usage", value=usage, expected_type=type_hints["usage"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
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
        if asns is not None:
            self._values["asns"] = asns
        if dynamic_locations is not None:
            self._values["dynamic_locations"] = dynamic_locations
        if dynamic_proxy_type is not None:
            self._values["dynamic_proxy_type"] = dynamic_proxy_type
        if gateways is not None:
            self._values["gateways"] = gateways
        if id is not None:
            self._values["id"] = id
        if proxies is not None:
            self._values["proxies"] = proxies
        if usage is not None:
            self._values["usage"] = usage

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
        '''Name of the Network Zone Resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#name NetworkZone#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of the Network Zone - can either be IP or DYNAMIC only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#type NetworkZone#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Format of each array value: a string representation of an ASN numeric value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#asns NetworkZone#asns}
        '''
        result = self._values.get("asns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def dynamic_locations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Array of locations ISO-3166-1(2). Format code: countryCode OR countryCode-regionCode.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#dynamic_locations NetworkZone#dynamic_locations}
        '''
        result = self._values.get("dynamic_locations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def dynamic_proxy_type(self) -> typing.Optional[builtins.str]:
        '''Type of proxy being controlled by this network zone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#dynamic_proxy_type NetworkZone#dynamic_proxy_type}
        '''
        result = self._values.get("dynamic_proxy_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gateways(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Array of values in CIDR/range form depending on the way it's been declared (i.e. CIDR will contain /suffix). Please check API docs for examples.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#gateways NetworkZone#gateways}
        '''
        result = self._values.get("gateways")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#id NetworkZone#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Array of values in CIDR/range form depending on the way it's been declared (i.e. CIDR will contain /suffix). Please check API docs for examples.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#proxies NetworkZone#proxies}
        '''
        result = self._values.get("proxies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def usage(self) -> typing.Optional[builtins.str]:
        '''Zone's purpose: POLICY or BLOCKLIST.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/network_zone#usage NetworkZone#usage}
        '''
        result = self._values.get("usage")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkZoneConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "NetworkZone",
    "NetworkZoneConfig",
]

publication.publish()
