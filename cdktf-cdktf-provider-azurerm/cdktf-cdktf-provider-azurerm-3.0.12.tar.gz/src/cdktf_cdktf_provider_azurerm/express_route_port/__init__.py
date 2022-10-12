'''
# `azurerm_express_route_port`

Refer to the Terraform Registory for docs: [`azurerm_express_route_port`](https://www.terraform.io/docs/providers/azurerm/r/express_route_port).
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


class ExpressRoutePort(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.expressRoutePort.ExpressRoutePort",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port azurerm_express_route_port}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        bandwidth_in_gbps: jsii.Number,
        encapsulation: builtins.str,
        location: builtins.str,
        name: builtins.str,
        peering_location: builtins.str,
        resource_group_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["ExpressRoutePortIdentity", typing.Dict[str, typing.Any]]] = None,
        link1: typing.Optional[typing.Union["ExpressRoutePortLink1", typing.Dict[str, typing.Any]]] = None,
        link2: typing.Optional[typing.Union["ExpressRoutePortLink2", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ExpressRoutePortTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port azurerm_express_route_port} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param bandwidth_in_gbps: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#bandwidth_in_gbps ExpressRoutePort#bandwidth_in_gbps}.
        :param encapsulation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#encapsulation ExpressRoutePort#encapsulation}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#location ExpressRoutePort#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#name ExpressRoutePort#name}.
        :param peering_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#peering_location ExpressRoutePort#peering_location}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#resource_group_name ExpressRoutePort#resource_group_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#id ExpressRoutePort#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#identity ExpressRoutePort#identity}
        :param link1: link1 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#link1 ExpressRoutePort#link1}
        :param link2: link2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#link2 ExpressRoutePort#link2}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#tags ExpressRoutePort#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#timeouts ExpressRoutePort#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExpressRoutePort.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ExpressRoutePortConfig(
            bandwidth_in_gbps=bandwidth_in_gbps,
            encapsulation=encapsulation,
            location=location,
            name=name,
            peering_location=peering_location,
            resource_group_name=resource_group_name,
            id=id,
            identity=identity,
            link1=link1,
            link2=link2,
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

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        identity_ids: typing.Sequence[builtins.str],
        type: builtins.str,
    ) -> None:
        '''
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#identity_ids ExpressRoutePort#identity_ids}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#type ExpressRoutePort#type}.
        '''
        value = ExpressRoutePortIdentity(identity_ids=identity_ids, type=type)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putLink1")
    def put_link1(
        self,
        *,
        admin_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        macsec_cak_keyvault_secret_id: typing.Optional[builtins.str] = None,
        macsec_cipher: typing.Optional[builtins.str] = None,
        macsec_ckn_keyvault_secret_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#admin_enabled ExpressRoutePort#admin_enabled}.
        :param macsec_cak_keyvault_secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#macsec_cak_keyvault_secret_id ExpressRoutePort#macsec_cak_keyvault_secret_id}.
        :param macsec_cipher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#macsec_cipher ExpressRoutePort#macsec_cipher}.
        :param macsec_ckn_keyvault_secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#macsec_ckn_keyvault_secret_id ExpressRoutePort#macsec_ckn_keyvault_secret_id}.
        '''
        value = ExpressRoutePortLink1(
            admin_enabled=admin_enabled,
            macsec_cak_keyvault_secret_id=macsec_cak_keyvault_secret_id,
            macsec_cipher=macsec_cipher,
            macsec_ckn_keyvault_secret_id=macsec_ckn_keyvault_secret_id,
        )

        return typing.cast(None, jsii.invoke(self, "putLink1", [value]))

    @jsii.member(jsii_name="putLink2")
    def put_link2(
        self,
        *,
        admin_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        macsec_cak_keyvault_secret_id: typing.Optional[builtins.str] = None,
        macsec_cipher: typing.Optional[builtins.str] = None,
        macsec_ckn_keyvault_secret_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#admin_enabled ExpressRoutePort#admin_enabled}.
        :param macsec_cak_keyvault_secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#macsec_cak_keyvault_secret_id ExpressRoutePort#macsec_cak_keyvault_secret_id}.
        :param macsec_cipher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#macsec_cipher ExpressRoutePort#macsec_cipher}.
        :param macsec_ckn_keyvault_secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#macsec_ckn_keyvault_secret_id ExpressRoutePort#macsec_ckn_keyvault_secret_id}.
        '''
        value = ExpressRoutePortLink2(
            admin_enabled=admin_enabled,
            macsec_cak_keyvault_secret_id=macsec_cak_keyvault_secret_id,
            macsec_cipher=macsec_cipher,
            macsec_ckn_keyvault_secret_id=macsec_ckn_keyvault_secret_id,
        )

        return typing.cast(None, jsii.invoke(self, "putLink2", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#create ExpressRoutePort#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#delete ExpressRoutePort#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#read ExpressRoutePort#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#update ExpressRoutePort#update}.
        '''
        value = ExpressRoutePortTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetLink1")
    def reset_link1(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLink1", []))

    @jsii.member(jsii_name="resetLink2")
    def reset_link2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLink2", []))

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
    @jsii.member(jsii_name="ethertype")
    def ethertype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ethertype"))

    @builtins.property
    @jsii.member(jsii_name="guid")
    def guid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "guid"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "ExpressRoutePortIdentityOutputReference":
        return typing.cast("ExpressRoutePortIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="link1")
    def link1(self) -> "ExpressRoutePortLink1OutputReference":
        return typing.cast("ExpressRoutePortLink1OutputReference", jsii.get(self, "link1"))

    @builtins.property
    @jsii.member(jsii_name="link2")
    def link2(self) -> "ExpressRoutePortLink2OutputReference":
        return typing.cast("ExpressRoutePortLink2OutputReference", jsii.get(self, "link2"))

    @builtins.property
    @jsii.member(jsii_name="mtu")
    def mtu(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mtu"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ExpressRoutePortTimeoutsOutputReference":
        return typing.cast("ExpressRoutePortTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="bandwidthInGbpsInput")
    def bandwidth_in_gbps_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bandwidthInGbpsInput"))

    @builtins.property
    @jsii.member(jsii_name="encapsulationInput")
    def encapsulation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encapsulationInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["ExpressRoutePortIdentity"]:
        return typing.cast(typing.Optional["ExpressRoutePortIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="link1Input")
    def link1_input(self) -> typing.Optional["ExpressRoutePortLink1"]:
        return typing.cast(typing.Optional["ExpressRoutePortLink1"], jsii.get(self, "link1Input"))

    @builtins.property
    @jsii.member(jsii_name="link2Input")
    def link2_input(self) -> typing.Optional["ExpressRoutePortLink2"]:
        return typing.cast(typing.Optional["ExpressRoutePortLink2"], jsii.get(self, "link2Input"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="peeringLocationInput")
    def peering_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peeringLocationInput"))

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
    ) -> typing.Optional[typing.Union["ExpressRoutePortTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ExpressRoutePortTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="bandwidthInGbps")
    def bandwidth_in_gbps(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bandwidthInGbps"))

    @bandwidth_in_gbps.setter
    def bandwidth_in_gbps(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePort, "bandwidth_in_gbps").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bandwidthInGbps", value)

    @builtins.property
    @jsii.member(jsii_name="encapsulation")
    def encapsulation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encapsulation"))

    @encapsulation.setter
    def encapsulation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePort, "encapsulation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encapsulation", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePort, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePort, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePort, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="peeringLocation")
    def peering_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peeringLocation"))

    @peering_location.setter
    def peering_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePort, "peering_location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peeringLocation", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePort, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePort, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.expressRoutePort.ExpressRoutePortConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "bandwidth_in_gbps": "bandwidthInGbps",
        "encapsulation": "encapsulation",
        "location": "location",
        "name": "name",
        "peering_location": "peeringLocation",
        "resource_group_name": "resourceGroupName",
        "id": "id",
        "identity": "identity",
        "link1": "link1",
        "link2": "link2",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class ExpressRoutePortConfig(cdktf.TerraformMetaArguments):
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
        bandwidth_in_gbps: jsii.Number,
        encapsulation: builtins.str,
        location: builtins.str,
        name: builtins.str,
        peering_location: builtins.str,
        resource_group_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["ExpressRoutePortIdentity", typing.Dict[str, typing.Any]]] = None,
        link1: typing.Optional[typing.Union["ExpressRoutePortLink1", typing.Dict[str, typing.Any]]] = None,
        link2: typing.Optional[typing.Union["ExpressRoutePortLink2", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ExpressRoutePortTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param bandwidth_in_gbps: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#bandwidth_in_gbps ExpressRoutePort#bandwidth_in_gbps}.
        :param encapsulation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#encapsulation ExpressRoutePort#encapsulation}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#location ExpressRoutePort#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#name ExpressRoutePort#name}.
        :param peering_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#peering_location ExpressRoutePort#peering_location}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#resource_group_name ExpressRoutePort#resource_group_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#id ExpressRoutePort#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#identity ExpressRoutePort#identity}
        :param link1: link1 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#link1 ExpressRoutePort#link1}
        :param link2: link2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#link2 ExpressRoutePort#link2}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#tags ExpressRoutePort#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#timeouts ExpressRoutePort#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(identity, dict):
            identity = ExpressRoutePortIdentity(**identity)
        if isinstance(link1, dict):
            link1 = ExpressRoutePortLink1(**link1)
        if isinstance(link2, dict):
            link2 = ExpressRoutePortLink2(**link2)
        if isinstance(timeouts, dict):
            timeouts = ExpressRoutePortTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ExpressRoutePortConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument bandwidth_in_gbps", value=bandwidth_in_gbps, expected_type=type_hints["bandwidth_in_gbps"])
            check_type(argname="argument encapsulation", value=encapsulation, expected_type=type_hints["encapsulation"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument peering_location", value=peering_location, expected_type=type_hints["peering_location"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument link1", value=link1, expected_type=type_hints["link1"])
            check_type(argname="argument link2", value=link2, expected_type=type_hints["link2"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "bandwidth_in_gbps": bandwidth_in_gbps,
            "encapsulation": encapsulation,
            "location": location,
            "name": name,
            "peering_location": peering_location,
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
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if link1 is not None:
            self._values["link1"] = link1
        if link2 is not None:
            self._values["link2"] = link2
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
    def bandwidth_in_gbps(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#bandwidth_in_gbps ExpressRoutePort#bandwidth_in_gbps}.'''
        result = self._values.get("bandwidth_in_gbps")
        assert result is not None, "Required property 'bandwidth_in_gbps' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def encapsulation(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#encapsulation ExpressRoutePort#encapsulation}.'''
        result = self._values.get("encapsulation")
        assert result is not None, "Required property 'encapsulation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#location ExpressRoutePort#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#name ExpressRoutePort#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def peering_location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#peering_location ExpressRoutePort#peering_location}.'''
        result = self._values.get("peering_location")
        assert result is not None, "Required property 'peering_location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#resource_group_name ExpressRoutePort#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#id ExpressRoutePort#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["ExpressRoutePortIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#identity ExpressRoutePort#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["ExpressRoutePortIdentity"], result)

    @builtins.property
    def link1(self) -> typing.Optional["ExpressRoutePortLink1"]:
        '''link1 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#link1 ExpressRoutePort#link1}
        '''
        result = self._values.get("link1")
        return typing.cast(typing.Optional["ExpressRoutePortLink1"], result)

    @builtins.property
    def link2(self) -> typing.Optional["ExpressRoutePortLink2"]:
        '''link2 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#link2 ExpressRoutePort#link2}
        '''
        result = self._values.get("link2")
        return typing.cast(typing.Optional["ExpressRoutePortLink2"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#tags ExpressRoutePort#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ExpressRoutePortTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#timeouts ExpressRoutePort#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ExpressRoutePortTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExpressRoutePortConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.expressRoutePort.ExpressRoutePortIdentity",
    jsii_struct_bases=[],
    name_mapping={"identity_ids": "identityIds", "type": "type"},
)
class ExpressRoutePortIdentity:
    def __init__(
        self,
        *,
        identity_ids: typing.Sequence[builtins.str],
        type: builtins.str,
    ) -> None:
        '''
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#identity_ids ExpressRoutePort#identity_ids}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#type ExpressRoutePort#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExpressRoutePortIdentity.__init__)
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "identity_ids": identity_ids,
            "type": type,
        }

    @builtins.property
    def identity_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#identity_ids ExpressRoutePort#identity_ids}.'''
        result = self._values.get("identity_ids")
        assert result is not None, "Required property 'identity_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#type ExpressRoutePort#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExpressRoutePortIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ExpressRoutePortIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.expressRoutePort.ExpressRoutePortIdentityOutputReference",
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
            type_hints = typing.get_type_hints(ExpressRoutePortIdentityOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ExpressRoutePortIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePortIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ExpressRoutePortIdentity]:
        return typing.cast(typing.Optional[ExpressRoutePortIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ExpressRoutePortIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePortIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.expressRoutePort.ExpressRoutePortLink1",
    jsii_struct_bases=[],
    name_mapping={
        "admin_enabled": "adminEnabled",
        "macsec_cak_keyvault_secret_id": "macsecCakKeyvaultSecretId",
        "macsec_cipher": "macsecCipher",
        "macsec_ckn_keyvault_secret_id": "macsecCknKeyvaultSecretId",
    },
)
class ExpressRoutePortLink1:
    def __init__(
        self,
        *,
        admin_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        macsec_cak_keyvault_secret_id: typing.Optional[builtins.str] = None,
        macsec_cipher: typing.Optional[builtins.str] = None,
        macsec_ckn_keyvault_secret_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#admin_enabled ExpressRoutePort#admin_enabled}.
        :param macsec_cak_keyvault_secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#macsec_cak_keyvault_secret_id ExpressRoutePort#macsec_cak_keyvault_secret_id}.
        :param macsec_cipher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#macsec_cipher ExpressRoutePort#macsec_cipher}.
        :param macsec_ckn_keyvault_secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#macsec_ckn_keyvault_secret_id ExpressRoutePort#macsec_ckn_keyvault_secret_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExpressRoutePortLink1.__init__)
            check_type(argname="argument admin_enabled", value=admin_enabled, expected_type=type_hints["admin_enabled"])
            check_type(argname="argument macsec_cak_keyvault_secret_id", value=macsec_cak_keyvault_secret_id, expected_type=type_hints["macsec_cak_keyvault_secret_id"])
            check_type(argname="argument macsec_cipher", value=macsec_cipher, expected_type=type_hints["macsec_cipher"])
            check_type(argname="argument macsec_ckn_keyvault_secret_id", value=macsec_ckn_keyvault_secret_id, expected_type=type_hints["macsec_ckn_keyvault_secret_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if admin_enabled is not None:
            self._values["admin_enabled"] = admin_enabled
        if macsec_cak_keyvault_secret_id is not None:
            self._values["macsec_cak_keyvault_secret_id"] = macsec_cak_keyvault_secret_id
        if macsec_cipher is not None:
            self._values["macsec_cipher"] = macsec_cipher
        if macsec_ckn_keyvault_secret_id is not None:
            self._values["macsec_ckn_keyvault_secret_id"] = macsec_ckn_keyvault_secret_id

    @builtins.property
    def admin_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#admin_enabled ExpressRoutePort#admin_enabled}.'''
        result = self._values.get("admin_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def macsec_cak_keyvault_secret_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#macsec_cak_keyvault_secret_id ExpressRoutePort#macsec_cak_keyvault_secret_id}.'''
        result = self._values.get("macsec_cak_keyvault_secret_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def macsec_cipher(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#macsec_cipher ExpressRoutePort#macsec_cipher}.'''
        result = self._values.get("macsec_cipher")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def macsec_ckn_keyvault_secret_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#macsec_ckn_keyvault_secret_id ExpressRoutePort#macsec_ckn_keyvault_secret_id}.'''
        result = self._values.get("macsec_ckn_keyvault_secret_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExpressRoutePortLink1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ExpressRoutePortLink1OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.expressRoutePort.ExpressRoutePortLink1OutputReference",
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
            type_hints = typing.get_type_hints(ExpressRoutePortLink1OutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAdminEnabled")
    def reset_admin_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminEnabled", []))

    @jsii.member(jsii_name="resetMacsecCakKeyvaultSecretId")
    def reset_macsec_cak_keyvault_secret_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMacsecCakKeyvaultSecretId", []))

    @jsii.member(jsii_name="resetMacsecCipher")
    def reset_macsec_cipher(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMacsecCipher", []))

    @jsii.member(jsii_name="resetMacsecCknKeyvaultSecretId")
    def reset_macsec_ckn_keyvault_secret_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMacsecCknKeyvaultSecretId", []))

    @builtins.property
    @jsii.member(jsii_name="connectorType")
    def connector_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectorType"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="interfaceName")
    def interface_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interfaceName"))

    @builtins.property
    @jsii.member(jsii_name="patchPanelId")
    def patch_panel_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "patchPanelId"))

    @builtins.property
    @jsii.member(jsii_name="rackId")
    def rack_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rackId"))

    @builtins.property
    @jsii.member(jsii_name="routerName")
    def router_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "routerName"))

    @builtins.property
    @jsii.member(jsii_name="adminEnabledInput")
    def admin_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "adminEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="macsecCakKeyvaultSecretIdInput")
    def macsec_cak_keyvault_secret_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "macsecCakKeyvaultSecretIdInput"))

    @builtins.property
    @jsii.member(jsii_name="macsecCipherInput")
    def macsec_cipher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "macsecCipherInput"))

    @builtins.property
    @jsii.member(jsii_name="macsecCknKeyvaultSecretIdInput")
    def macsec_ckn_keyvault_secret_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "macsecCknKeyvaultSecretIdInput"))

    @builtins.property
    @jsii.member(jsii_name="adminEnabled")
    def admin_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "adminEnabled"))

    @admin_enabled.setter
    def admin_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePortLink1OutputReference, "admin_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="macsecCakKeyvaultSecretId")
    def macsec_cak_keyvault_secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "macsecCakKeyvaultSecretId"))

    @macsec_cak_keyvault_secret_id.setter
    def macsec_cak_keyvault_secret_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePortLink1OutputReference, "macsec_cak_keyvault_secret_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "macsecCakKeyvaultSecretId", value)

    @builtins.property
    @jsii.member(jsii_name="macsecCipher")
    def macsec_cipher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "macsecCipher"))

    @macsec_cipher.setter
    def macsec_cipher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePortLink1OutputReference, "macsec_cipher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "macsecCipher", value)

    @builtins.property
    @jsii.member(jsii_name="macsecCknKeyvaultSecretId")
    def macsec_ckn_keyvault_secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "macsecCknKeyvaultSecretId"))

    @macsec_ckn_keyvault_secret_id.setter
    def macsec_ckn_keyvault_secret_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePortLink1OutputReference, "macsec_ckn_keyvault_secret_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "macsecCknKeyvaultSecretId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ExpressRoutePortLink1]:
        return typing.cast(typing.Optional[ExpressRoutePortLink1], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ExpressRoutePortLink1]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePortLink1OutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.expressRoutePort.ExpressRoutePortLink2",
    jsii_struct_bases=[],
    name_mapping={
        "admin_enabled": "adminEnabled",
        "macsec_cak_keyvault_secret_id": "macsecCakKeyvaultSecretId",
        "macsec_cipher": "macsecCipher",
        "macsec_ckn_keyvault_secret_id": "macsecCknKeyvaultSecretId",
    },
)
class ExpressRoutePortLink2:
    def __init__(
        self,
        *,
        admin_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        macsec_cak_keyvault_secret_id: typing.Optional[builtins.str] = None,
        macsec_cipher: typing.Optional[builtins.str] = None,
        macsec_ckn_keyvault_secret_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#admin_enabled ExpressRoutePort#admin_enabled}.
        :param macsec_cak_keyvault_secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#macsec_cak_keyvault_secret_id ExpressRoutePort#macsec_cak_keyvault_secret_id}.
        :param macsec_cipher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#macsec_cipher ExpressRoutePort#macsec_cipher}.
        :param macsec_ckn_keyvault_secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#macsec_ckn_keyvault_secret_id ExpressRoutePort#macsec_ckn_keyvault_secret_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExpressRoutePortLink2.__init__)
            check_type(argname="argument admin_enabled", value=admin_enabled, expected_type=type_hints["admin_enabled"])
            check_type(argname="argument macsec_cak_keyvault_secret_id", value=macsec_cak_keyvault_secret_id, expected_type=type_hints["macsec_cak_keyvault_secret_id"])
            check_type(argname="argument macsec_cipher", value=macsec_cipher, expected_type=type_hints["macsec_cipher"])
            check_type(argname="argument macsec_ckn_keyvault_secret_id", value=macsec_ckn_keyvault_secret_id, expected_type=type_hints["macsec_ckn_keyvault_secret_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if admin_enabled is not None:
            self._values["admin_enabled"] = admin_enabled
        if macsec_cak_keyvault_secret_id is not None:
            self._values["macsec_cak_keyvault_secret_id"] = macsec_cak_keyvault_secret_id
        if macsec_cipher is not None:
            self._values["macsec_cipher"] = macsec_cipher
        if macsec_ckn_keyvault_secret_id is not None:
            self._values["macsec_ckn_keyvault_secret_id"] = macsec_ckn_keyvault_secret_id

    @builtins.property
    def admin_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#admin_enabled ExpressRoutePort#admin_enabled}.'''
        result = self._values.get("admin_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def macsec_cak_keyvault_secret_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#macsec_cak_keyvault_secret_id ExpressRoutePort#macsec_cak_keyvault_secret_id}.'''
        result = self._values.get("macsec_cak_keyvault_secret_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def macsec_cipher(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#macsec_cipher ExpressRoutePort#macsec_cipher}.'''
        result = self._values.get("macsec_cipher")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def macsec_ckn_keyvault_secret_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#macsec_ckn_keyvault_secret_id ExpressRoutePort#macsec_ckn_keyvault_secret_id}.'''
        result = self._values.get("macsec_ckn_keyvault_secret_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExpressRoutePortLink2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ExpressRoutePortLink2OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.expressRoutePort.ExpressRoutePortLink2OutputReference",
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
            type_hints = typing.get_type_hints(ExpressRoutePortLink2OutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAdminEnabled")
    def reset_admin_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminEnabled", []))

    @jsii.member(jsii_name="resetMacsecCakKeyvaultSecretId")
    def reset_macsec_cak_keyvault_secret_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMacsecCakKeyvaultSecretId", []))

    @jsii.member(jsii_name="resetMacsecCipher")
    def reset_macsec_cipher(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMacsecCipher", []))

    @jsii.member(jsii_name="resetMacsecCknKeyvaultSecretId")
    def reset_macsec_ckn_keyvault_secret_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMacsecCknKeyvaultSecretId", []))

    @builtins.property
    @jsii.member(jsii_name="connectorType")
    def connector_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectorType"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="interfaceName")
    def interface_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interfaceName"))

    @builtins.property
    @jsii.member(jsii_name="patchPanelId")
    def patch_panel_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "patchPanelId"))

    @builtins.property
    @jsii.member(jsii_name="rackId")
    def rack_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rackId"))

    @builtins.property
    @jsii.member(jsii_name="routerName")
    def router_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "routerName"))

    @builtins.property
    @jsii.member(jsii_name="adminEnabledInput")
    def admin_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "adminEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="macsecCakKeyvaultSecretIdInput")
    def macsec_cak_keyvault_secret_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "macsecCakKeyvaultSecretIdInput"))

    @builtins.property
    @jsii.member(jsii_name="macsecCipherInput")
    def macsec_cipher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "macsecCipherInput"))

    @builtins.property
    @jsii.member(jsii_name="macsecCknKeyvaultSecretIdInput")
    def macsec_ckn_keyvault_secret_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "macsecCknKeyvaultSecretIdInput"))

    @builtins.property
    @jsii.member(jsii_name="adminEnabled")
    def admin_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "adminEnabled"))

    @admin_enabled.setter
    def admin_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePortLink2OutputReference, "admin_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="macsecCakKeyvaultSecretId")
    def macsec_cak_keyvault_secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "macsecCakKeyvaultSecretId"))

    @macsec_cak_keyvault_secret_id.setter
    def macsec_cak_keyvault_secret_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePortLink2OutputReference, "macsec_cak_keyvault_secret_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "macsecCakKeyvaultSecretId", value)

    @builtins.property
    @jsii.member(jsii_name="macsecCipher")
    def macsec_cipher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "macsecCipher"))

    @macsec_cipher.setter
    def macsec_cipher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePortLink2OutputReference, "macsec_cipher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "macsecCipher", value)

    @builtins.property
    @jsii.member(jsii_name="macsecCknKeyvaultSecretId")
    def macsec_ckn_keyvault_secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "macsecCknKeyvaultSecretId"))

    @macsec_ckn_keyvault_secret_id.setter
    def macsec_ckn_keyvault_secret_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePortLink2OutputReference, "macsec_ckn_keyvault_secret_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "macsecCknKeyvaultSecretId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ExpressRoutePortLink2]:
        return typing.cast(typing.Optional[ExpressRoutePortLink2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ExpressRoutePortLink2]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePortLink2OutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.expressRoutePort.ExpressRoutePortTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ExpressRoutePortTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#create ExpressRoutePort#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#delete ExpressRoutePort#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#read ExpressRoutePort#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#update ExpressRoutePort#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExpressRoutePortTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#create ExpressRoutePort#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#delete ExpressRoutePort#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#read ExpressRoutePort#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/express_route_port#update ExpressRoutePort#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExpressRoutePortTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ExpressRoutePortTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.expressRoutePort.ExpressRoutePortTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ExpressRoutePortTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ExpressRoutePortTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePortTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePortTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePortTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ExpressRoutePortTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ExpressRoutePortTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ExpressRoutePortTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExpressRoutePortTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ExpressRoutePort",
    "ExpressRoutePortConfig",
    "ExpressRoutePortIdentity",
    "ExpressRoutePortIdentityOutputReference",
    "ExpressRoutePortLink1",
    "ExpressRoutePortLink1OutputReference",
    "ExpressRoutePortLink2",
    "ExpressRoutePortLink2OutputReference",
    "ExpressRoutePortTimeouts",
    "ExpressRoutePortTimeoutsOutputReference",
]

publication.publish()
