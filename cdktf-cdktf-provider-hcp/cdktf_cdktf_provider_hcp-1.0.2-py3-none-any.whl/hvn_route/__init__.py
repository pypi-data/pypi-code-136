'''
# `hcp_hvn_route`

Refer to the Terraform Registory for docs: [`hcp_hvn_route`](https://www.terraform.io/docs/providers/hcp/r/hvn_route).
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


class HvnRoute(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.hvnRoute.HvnRoute",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route hcp_hvn_route}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        destination_cidr: builtins.str,
        hvn_link: builtins.str,
        hvn_route_id: builtins.str,
        target_link: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["HvnRouteTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route hcp_hvn_route} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param destination_cidr: The destination CIDR of the HVN route. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#destination_cidr HvnRoute#destination_cidr}
        :param hvn_link: The ``self_link`` of the HashiCorp Virtual Network (HVN). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#hvn_link HvnRoute#hvn_link}
        :param hvn_route_id: The ID of the HVN route. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#hvn_route_id HvnRoute#hvn_route_id}
        :param target_link: A unique URL identifying the target of the HVN route. Examples of the target: ```aws_network_peering`` <aws_network_peering.md>`_, ```aws_transit_gateway_attachment`` <aws_transit_gateway_attachment.md>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#target_link HvnRoute#target_link}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#id HvnRoute#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#timeouts HvnRoute#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HvnRoute.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = HvnRouteConfig(
            destination_cidr=destination_cidr,
            hvn_link=hvn_link,
            hvn_route_id=hvn_route_id,
            target_link=target_link,
            id=id,
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

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#create HvnRoute#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#default HvnRoute#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#delete HvnRoute#delete}.
        '''
        value = HvnRouteTimeouts(create=create, default=default, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "HvnRouteTimeoutsOutputReference":
        return typing.cast("HvnRouteTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="destinationCidrInput")
    def destination_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="hvnLinkInput")
    def hvn_link_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hvnLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="hvnRouteIdInput")
    def hvn_route_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hvnRouteIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="targetLinkInput")
    def target_link_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["HvnRouteTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["HvnRouteTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationCidr")
    def destination_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationCidr"))

    @destination_cidr.setter
    def destination_cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HvnRoute, "destination_cidr").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationCidr", value)

    @builtins.property
    @jsii.member(jsii_name="hvnLink")
    def hvn_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hvnLink"))

    @hvn_link.setter
    def hvn_link(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HvnRoute, "hvn_link").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hvnLink", value)

    @builtins.property
    @jsii.member(jsii_name="hvnRouteId")
    def hvn_route_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hvnRouteId"))

    @hvn_route_id.setter
    def hvn_route_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HvnRoute, "hvn_route_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hvnRouteId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HvnRoute, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="targetLink")
    def target_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetLink"))

    @target_link.setter
    def target_link(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HvnRoute, "target_link").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetLink", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.hvnRoute.HvnRouteConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "destination_cidr": "destinationCidr",
        "hvn_link": "hvnLink",
        "hvn_route_id": "hvnRouteId",
        "target_link": "targetLink",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class HvnRouteConfig(cdktf.TerraformMetaArguments):
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
        destination_cidr: builtins.str,
        hvn_link: builtins.str,
        hvn_route_id: builtins.str,
        target_link: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["HvnRouteTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param destination_cidr: The destination CIDR of the HVN route. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#destination_cidr HvnRoute#destination_cidr}
        :param hvn_link: The ``self_link`` of the HashiCorp Virtual Network (HVN). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#hvn_link HvnRoute#hvn_link}
        :param hvn_route_id: The ID of the HVN route. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#hvn_route_id HvnRoute#hvn_route_id}
        :param target_link: A unique URL identifying the target of the HVN route. Examples of the target: ```aws_network_peering`` <aws_network_peering.md>`_, ```aws_transit_gateway_attachment`` <aws_transit_gateway_attachment.md>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#target_link HvnRoute#target_link}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#id HvnRoute#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#timeouts HvnRoute#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = HvnRouteTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(HvnRouteConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument destination_cidr", value=destination_cidr, expected_type=type_hints["destination_cidr"])
            check_type(argname="argument hvn_link", value=hvn_link, expected_type=type_hints["hvn_link"])
            check_type(argname="argument hvn_route_id", value=hvn_route_id, expected_type=type_hints["hvn_route_id"])
            check_type(argname="argument target_link", value=target_link, expected_type=type_hints["target_link"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination_cidr": destination_cidr,
            "hvn_link": hvn_link,
            "hvn_route_id": hvn_route_id,
            "target_link": target_link,
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
    def destination_cidr(self) -> builtins.str:
        '''The destination CIDR of the HVN route.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#destination_cidr HvnRoute#destination_cidr}
        '''
        result = self._values.get("destination_cidr")
        assert result is not None, "Required property 'destination_cidr' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hvn_link(self) -> builtins.str:
        '''The ``self_link`` of the HashiCorp Virtual Network (HVN).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#hvn_link HvnRoute#hvn_link}
        '''
        result = self._values.get("hvn_link")
        assert result is not None, "Required property 'hvn_link' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hvn_route_id(self) -> builtins.str:
        '''The ID of the HVN route.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#hvn_route_id HvnRoute#hvn_route_id}
        '''
        result = self._values.get("hvn_route_id")
        assert result is not None, "Required property 'hvn_route_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_link(self) -> builtins.str:
        '''A unique URL identifying the target of the HVN route. Examples of the target: ```aws_network_peering`` <aws_network_peering.md>`_, ```aws_transit_gateway_attachment`` <aws_transit_gateway_attachment.md>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#target_link HvnRoute#target_link}
        '''
        result = self._values.get("target_link")
        assert result is not None, "Required property 'target_link' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#id HvnRoute#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["HvnRouteTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#timeouts HvnRoute#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["HvnRouteTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HvnRouteConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.hvnRoute.HvnRouteTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "default": "default", "delete": "delete"},
)
class HvnRouteTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#create HvnRoute#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#default HvnRoute#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#delete HvnRoute#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HvnRouteTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if default is not None:
            self._values["default"] = default
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#create HvnRoute#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#default HvnRoute#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/hvn_route#delete HvnRoute#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HvnRouteTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HvnRouteTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.hvnRoute.HvnRouteTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(HvnRouteTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HvnRouteTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HvnRouteTimeoutsOutputReference, "default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HvnRouteTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HvnRouteTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HvnRouteTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HvnRouteTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HvnRouteTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "HvnRoute",
    "HvnRouteConfig",
    "HvnRouteTimeouts",
    "HvnRouteTimeoutsOutputReference",
]

publication.publish()
