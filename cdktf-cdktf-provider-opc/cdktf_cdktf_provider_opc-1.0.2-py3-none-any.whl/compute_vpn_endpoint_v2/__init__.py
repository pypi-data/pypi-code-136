'''
# `opc_compute_vpn_endpoint_v2`

Refer to the Terraform Registory for docs: [`opc_compute_vpn_endpoint_v2`](https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2).
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


class ComputeVpnEndpointV2(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeVpnEndpointV2.ComputeVpnEndpointV2",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2 opc_compute_vpn_endpoint_v2}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        customer_vpn_gateway: builtins.str,
        ip_network: builtins.str,
        name: builtins.str,
        pre_shared_key: builtins.str,
        reachable_routes: typing.Sequence[builtins.str],
        vnic_sets: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ike_identifier: typing.Optional[builtins.str] = None,
        phase_one_settings: typing.Optional[typing.Union["ComputeVpnEndpointV2PhaseOneSettings", typing.Dict[str, typing.Any]]] = None,
        phase_two_settings: typing.Optional[typing.Union["ComputeVpnEndpointV2PhaseTwoSettings", typing.Dict[str, typing.Any]]] = None,
        require_perfect_forward_secrecy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ComputeVpnEndpointV2Timeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2 opc_compute_vpn_endpoint_v2} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param customer_vpn_gateway: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#customer_vpn_gateway ComputeVpnEndpointV2#customer_vpn_gateway}.
        :param ip_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#ip_network ComputeVpnEndpointV2#ip_network}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#name ComputeVpnEndpointV2#name}.
        :param pre_shared_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#pre_shared_key ComputeVpnEndpointV2#pre_shared_key}.
        :param reachable_routes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#reachable_routes ComputeVpnEndpointV2#reachable_routes}.
        :param vnic_sets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#vnic_sets ComputeVpnEndpointV2#vnic_sets}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#description ComputeVpnEndpointV2#description}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#enabled ComputeVpnEndpointV2#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#id ComputeVpnEndpointV2#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ike_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#ike_identifier ComputeVpnEndpointV2#ike_identifier}.
        :param phase_one_settings: phase_one_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#phase_one_settings ComputeVpnEndpointV2#phase_one_settings}
        :param phase_two_settings: phase_two_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#phase_two_settings ComputeVpnEndpointV2#phase_two_settings}
        :param require_perfect_forward_secrecy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#require_perfect_forward_secrecy ComputeVpnEndpointV2#require_perfect_forward_secrecy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#tags ComputeVpnEndpointV2#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#timeouts ComputeVpnEndpointV2#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeVpnEndpointV2.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ComputeVpnEndpointV2Config(
            customer_vpn_gateway=customer_vpn_gateway,
            ip_network=ip_network,
            name=name,
            pre_shared_key=pre_shared_key,
            reachable_routes=reachable_routes,
            vnic_sets=vnic_sets,
            description=description,
            enabled=enabled,
            id=id,
            ike_identifier=ike_identifier,
            phase_one_settings=phase_one_settings,
            phase_two_settings=phase_two_settings,
            require_perfect_forward_secrecy=require_perfect_forward_secrecy,
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

    @jsii.member(jsii_name="putPhaseOneSettings")
    def put_phase_one_settings(
        self,
        *,
        dh_group: builtins.str,
        encryption: builtins.str,
        hash: builtins.str,
        lifetime: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dh_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#dh_group ComputeVpnEndpointV2#dh_group}.
        :param encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#encryption ComputeVpnEndpointV2#encryption}.
        :param hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#hash ComputeVpnEndpointV2#hash}.
        :param lifetime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#lifetime ComputeVpnEndpointV2#lifetime}.
        '''
        value = ComputeVpnEndpointV2PhaseOneSettings(
            dh_group=dh_group, encryption=encryption, hash=hash, lifetime=lifetime
        )

        return typing.cast(None, jsii.invoke(self, "putPhaseOneSettings", [value]))

    @jsii.member(jsii_name="putPhaseTwoSettings")
    def put_phase_two_settings(
        self,
        *,
        encryption: builtins.str,
        hash: builtins.str,
        lifetime: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#encryption ComputeVpnEndpointV2#encryption}.
        :param hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#hash ComputeVpnEndpointV2#hash}.
        :param lifetime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#lifetime ComputeVpnEndpointV2#lifetime}.
        '''
        value = ComputeVpnEndpointV2PhaseTwoSettings(
            encryption=encryption, hash=hash, lifetime=lifetime
        )

        return typing.cast(None, jsii.invoke(self, "putPhaseTwoSettings", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#create ComputeVpnEndpointV2#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#delete ComputeVpnEndpointV2#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#update ComputeVpnEndpointV2#update}.
        '''
        value = ComputeVpnEndpointV2Timeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIkeIdentifier")
    def reset_ike_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIkeIdentifier", []))

    @jsii.member(jsii_name="resetPhaseOneSettings")
    def reset_phase_one_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhaseOneSettings", []))

    @jsii.member(jsii_name="resetPhaseTwoSettings")
    def reset_phase_two_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhaseTwoSettings", []))

    @jsii.member(jsii_name="resetRequirePerfectForwardSecrecy")
    def reset_require_perfect_forward_secrecy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequirePerfectForwardSecrecy", []))

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
    @jsii.member(jsii_name="localGatewayIpAddress")
    def local_gateway_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localGatewayIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="localGatewayPrivateIpAddress")
    def local_gateway_private_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localGatewayPrivateIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="phaseOneSettings")
    def phase_one_settings(
        self,
    ) -> "ComputeVpnEndpointV2PhaseOneSettingsOutputReference":
        return typing.cast("ComputeVpnEndpointV2PhaseOneSettingsOutputReference", jsii.get(self, "phaseOneSettings"))

    @builtins.property
    @jsii.member(jsii_name="phaseTwoSettings")
    def phase_two_settings(
        self,
    ) -> "ComputeVpnEndpointV2PhaseTwoSettingsOutputReference":
        return typing.cast("ComputeVpnEndpointV2PhaseTwoSettingsOutputReference", jsii.get(self, "phaseTwoSettings"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ComputeVpnEndpointV2TimeoutsOutputReference":
        return typing.cast("ComputeVpnEndpointV2TimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="tunnelStatus")
    def tunnel_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnelStatus"))

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @builtins.property
    @jsii.member(jsii_name="customerVpnGatewayInput")
    def customer_vpn_gateway_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerVpnGatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ikeIdentifierInput")
    def ike_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ikeIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="ipNetworkInput")
    def ip_network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="phaseOneSettingsInput")
    def phase_one_settings_input(
        self,
    ) -> typing.Optional["ComputeVpnEndpointV2PhaseOneSettings"]:
        return typing.cast(typing.Optional["ComputeVpnEndpointV2PhaseOneSettings"], jsii.get(self, "phaseOneSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="phaseTwoSettingsInput")
    def phase_two_settings_input(
        self,
    ) -> typing.Optional["ComputeVpnEndpointV2PhaseTwoSettings"]:
        return typing.cast(typing.Optional["ComputeVpnEndpointV2PhaseTwoSettings"], jsii.get(self, "phaseTwoSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="preSharedKeyInput")
    def pre_shared_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preSharedKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="reachableRoutesInput")
    def reachable_routes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "reachableRoutesInput"))

    @builtins.property
    @jsii.member(jsii_name="requirePerfectForwardSecrecyInput")
    def require_perfect_forward_secrecy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requirePerfectForwardSecrecyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ComputeVpnEndpointV2Timeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ComputeVpnEndpointV2Timeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vnicSetsInput")
    def vnic_sets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vnicSetsInput"))

    @builtins.property
    @jsii.member(jsii_name="customerVpnGateway")
    def customer_vpn_gateway(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerVpnGateway"))

    @customer_vpn_gateway.setter
    def customer_vpn_gateway(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2, "customer_vpn_gateway").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerVpnGateway", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ikeIdentifier")
    def ike_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ikeIdentifier"))

    @ike_identifier.setter
    def ike_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2, "ike_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ikeIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="ipNetwork")
    def ip_network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipNetwork"))

    @ip_network.setter
    def ip_network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2, "ip_network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="preSharedKey")
    def pre_shared_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preSharedKey"))

    @pre_shared_key.setter
    def pre_shared_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2, "pre_shared_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preSharedKey", value)

    @builtins.property
    @jsii.member(jsii_name="reachableRoutes")
    def reachable_routes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "reachableRoutes"))

    @reachable_routes.setter
    def reachable_routes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2, "reachable_routes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reachableRoutes", value)

    @builtins.property
    @jsii.member(jsii_name="requirePerfectForwardSecrecy")
    def require_perfect_forward_secrecy(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requirePerfectForwardSecrecy"))

    @require_perfect_forward_secrecy.setter
    def require_perfect_forward_secrecy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2, "require_perfect_forward_secrecy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requirePerfectForwardSecrecy", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="vnicSets")
    def vnic_sets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vnicSets"))

    @vnic_sets.setter
    def vnic_sets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2, "vnic_sets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vnicSets", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeVpnEndpointV2.ComputeVpnEndpointV2Config",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "customer_vpn_gateway": "customerVpnGateway",
        "ip_network": "ipNetwork",
        "name": "name",
        "pre_shared_key": "preSharedKey",
        "reachable_routes": "reachableRoutes",
        "vnic_sets": "vnicSets",
        "description": "description",
        "enabled": "enabled",
        "id": "id",
        "ike_identifier": "ikeIdentifier",
        "phase_one_settings": "phaseOneSettings",
        "phase_two_settings": "phaseTwoSettings",
        "require_perfect_forward_secrecy": "requirePerfectForwardSecrecy",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class ComputeVpnEndpointV2Config(cdktf.TerraformMetaArguments):
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
        customer_vpn_gateway: builtins.str,
        ip_network: builtins.str,
        name: builtins.str,
        pre_shared_key: builtins.str,
        reachable_routes: typing.Sequence[builtins.str],
        vnic_sets: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ike_identifier: typing.Optional[builtins.str] = None,
        phase_one_settings: typing.Optional[typing.Union["ComputeVpnEndpointV2PhaseOneSettings", typing.Dict[str, typing.Any]]] = None,
        phase_two_settings: typing.Optional[typing.Union["ComputeVpnEndpointV2PhaseTwoSettings", typing.Dict[str, typing.Any]]] = None,
        require_perfect_forward_secrecy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ComputeVpnEndpointV2Timeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param customer_vpn_gateway: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#customer_vpn_gateway ComputeVpnEndpointV2#customer_vpn_gateway}.
        :param ip_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#ip_network ComputeVpnEndpointV2#ip_network}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#name ComputeVpnEndpointV2#name}.
        :param pre_shared_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#pre_shared_key ComputeVpnEndpointV2#pre_shared_key}.
        :param reachable_routes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#reachable_routes ComputeVpnEndpointV2#reachable_routes}.
        :param vnic_sets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#vnic_sets ComputeVpnEndpointV2#vnic_sets}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#description ComputeVpnEndpointV2#description}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#enabled ComputeVpnEndpointV2#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#id ComputeVpnEndpointV2#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ike_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#ike_identifier ComputeVpnEndpointV2#ike_identifier}.
        :param phase_one_settings: phase_one_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#phase_one_settings ComputeVpnEndpointV2#phase_one_settings}
        :param phase_two_settings: phase_two_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#phase_two_settings ComputeVpnEndpointV2#phase_two_settings}
        :param require_perfect_forward_secrecy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#require_perfect_forward_secrecy ComputeVpnEndpointV2#require_perfect_forward_secrecy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#tags ComputeVpnEndpointV2#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#timeouts ComputeVpnEndpointV2#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(phase_one_settings, dict):
            phase_one_settings = ComputeVpnEndpointV2PhaseOneSettings(**phase_one_settings)
        if isinstance(phase_two_settings, dict):
            phase_two_settings = ComputeVpnEndpointV2PhaseTwoSettings(**phase_two_settings)
        if isinstance(timeouts, dict):
            timeouts = ComputeVpnEndpointV2Timeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeVpnEndpointV2Config.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument customer_vpn_gateway", value=customer_vpn_gateway, expected_type=type_hints["customer_vpn_gateway"])
            check_type(argname="argument ip_network", value=ip_network, expected_type=type_hints["ip_network"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument pre_shared_key", value=pre_shared_key, expected_type=type_hints["pre_shared_key"])
            check_type(argname="argument reachable_routes", value=reachable_routes, expected_type=type_hints["reachable_routes"])
            check_type(argname="argument vnic_sets", value=vnic_sets, expected_type=type_hints["vnic_sets"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ike_identifier", value=ike_identifier, expected_type=type_hints["ike_identifier"])
            check_type(argname="argument phase_one_settings", value=phase_one_settings, expected_type=type_hints["phase_one_settings"])
            check_type(argname="argument phase_two_settings", value=phase_two_settings, expected_type=type_hints["phase_two_settings"])
            check_type(argname="argument require_perfect_forward_secrecy", value=require_perfect_forward_secrecy, expected_type=type_hints["require_perfect_forward_secrecy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "customer_vpn_gateway": customer_vpn_gateway,
            "ip_network": ip_network,
            "name": name,
            "pre_shared_key": pre_shared_key,
            "reachable_routes": reachable_routes,
            "vnic_sets": vnic_sets,
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
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if ike_identifier is not None:
            self._values["ike_identifier"] = ike_identifier
        if phase_one_settings is not None:
            self._values["phase_one_settings"] = phase_one_settings
        if phase_two_settings is not None:
            self._values["phase_two_settings"] = phase_two_settings
        if require_perfect_forward_secrecy is not None:
            self._values["require_perfect_forward_secrecy"] = require_perfect_forward_secrecy
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
    def customer_vpn_gateway(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#customer_vpn_gateway ComputeVpnEndpointV2#customer_vpn_gateway}.'''
        result = self._values.get("customer_vpn_gateway")
        assert result is not None, "Required property 'customer_vpn_gateway' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip_network(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#ip_network ComputeVpnEndpointV2#ip_network}.'''
        result = self._values.get("ip_network")
        assert result is not None, "Required property 'ip_network' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#name ComputeVpnEndpointV2#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pre_shared_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#pre_shared_key ComputeVpnEndpointV2#pre_shared_key}.'''
        result = self._values.get("pre_shared_key")
        assert result is not None, "Required property 'pre_shared_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def reachable_routes(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#reachable_routes ComputeVpnEndpointV2#reachable_routes}.'''
        result = self._values.get("reachable_routes")
        assert result is not None, "Required property 'reachable_routes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vnic_sets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#vnic_sets ComputeVpnEndpointV2#vnic_sets}.'''
        result = self._values.get("vnic_sets")
        assert result is not None, "Required property 'vnic_sets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#description ComputeVpnEndpointV2#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#enabled ComputeVpnEndpointV2#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#id ComputeVpnEndpointV2#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ike_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#ike_identifier ComputeVpnEndpointV2#ike_identifier}.'''
        result = self._values.get("ike_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def phase_one_settings(
        self,
    ) -> typing.Optional["ComputeVpnEndpointV2PhaseOneSettings"]:
        '''phase_one_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#phase_one_settings ComputeVpnEndpointV2#phase_one_settings}
        '''
        result = self._values.get("phase_one_settings")
        return typing.cast(typing.Optional["ComputeVpnEndpointV2PhaseOneSettings"], result)

    @builtins.property
    def phase_two_settings(
        self,
    ) -> typing.Optional["ComputeVpnEndpointV2PhaseTwoSettings"]:
        '''phase_two_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#phase_two_settings ComputeVpnEndpointV2#phase_two_settings}
        '''
        result = self._values.get("phase_two_settings")
        return typing.cast(typing.Optional["ComputeVpnEndpointV2PhaseTwoSettings"], result)

    @builtins.property
    def require_perfect_forward_secrecy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#require_perfect_forward_secrecy ComputeVpnEndpointV2#require_perfect_forward_secrecy}.'''
        result = self._values.get("require_perfect_forward_secrecy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#tags ComputeVpnEndpointV2#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ComputeVpnEndpointV2Timeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#timeouts ComputeVpnEndpointV2#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ComputeVpnEndpointV2Timeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeVpnEndpointV2Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeVpnEndpointV2.ComputeVpnEndpointV2PhaseOneSettings",
    jsii_struct_bases=[],
    name_mapping={
        "dh_group": "dhGroup",
        "encryption": "encryption",
        "hash": "hash",
        "lifetime": "lifetime",
    },
)
class ComputeVpnEndpointV2PhaseOneSettings:
    def __init__(
        self,
        *,
        dh_group: builtins.str,
        encryption: builtins.str,
        hash: builtins.str,
        lifetime: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dh_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#dh_group ComputeVpnEndpointV2#dh_group}.
        :param encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#encryption ComputeVpnEndpointV2#encryption}.
        :param hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#hash ComputeVpnEndpointV2#hash}.
        :param lifetime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#lifetime ComputeVpnEndpointV2#lifetime}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeVpnEndpointV2PhaseOneSettings.__init__)
            check_type(argname="argument dh_group", value=dh_group, expected_type=type_hints["dh_group"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument hash", value=hash, expected_type=type_hints["hash"])
            check_type(argname="argument lifetime", value=lifetime, expected_type=type_hints["lifetime"])
        self._values: typing.Dict[str, typing.Any] = {
            "dh_group": dh_group,
            "encryption": encryption,
            "hash": hash,
        }
        if lifetime is not None:
            self._values["lifetime"] = lifetime

    @builtins.property
    def dh_group(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#dh_group ComputeVpnEndpointV2#dh_group}.'''
        result = self._values.get("dh_group")
        assert result is not None, "Required property 'dh_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encryption(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#encryption ComputeVpnEndpointV2#encryption}.'''
        result = self._values.get("encryption")
        assert result is not None, "Required property 'encryption' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hash(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#hash ComputeVpnEndpointV2#hash}.'''
        result = self._values.get("hash")
        assert result is not None, "Required property 'hash' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lifetime(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#lifetime ComputeVpnEndpointV2#lifetime}.'''
        result = self._values.get("lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeVpnEndpointV2PhaseOneSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeVpnEndpointV2PhaseOneSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeVpnEndpointV2.ComputeVpnEndpointV2PhaseOneSettingsOutputReference",
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
            type_hints = typing.get_type_hints(ComputeVpnEndpointV2PhaseOneSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLifetime")
    def reset_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifetime", []))

    @builtins.property
    @jsii.member(jsii_name="dhGroupInput")
    def dh_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dhGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionInput")
    def encryption_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="hashInput")
    def hash_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hashInput"))

    @builtins.property
    @jsii.member(jsii_name="lifetimeInput")
    def lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="dhGroup")
    def dh_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dhGroup"))

    @dh_group.setter
    def dh_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2PhaseOneSettingsOutputReference, "dh_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dhGroup", value)

    @builtins.property
    @jsii.member(jsii_name="encryption")
    def encryption(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryption"))

    @encryption.setter
    def encryption(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2PhaseOneSettingsOutputReference, "encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryption", value)

    @builtins.property
    @jsii.member(jsii_name="hash")
    def hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hash"))

    @hash.setter
    def hash(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2PhaseOneSettingsOutputReference, "hash").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hash", value)

    @builtins.property
    @jsii.member(jsii_name="lifetime")
    def lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lifetime"))

    @lifetime.setter
    def lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2PhaseOneSettingsOutputReference, "lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifetime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ComputeVpnEndpointV2PhaseOneSettings]:
        return typing.cast(typing.Optional[ComputeVpnEndpointV2PhaseOneSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeVpnEndpointV2PhaseOneSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2PhaseOneSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeVpnEndpointV2.ComputeVpnEndpointV2PhaseTwoSettings",
    jsii_struct_bases=[],
    name_mapping={"encryption": "encryption", "hash": "hash", "lifetime": "lifetime"},
)
class ComputeVpnEndpointV2PhaseTwoSettings:
    def __init__(
        self,
        *,
        encryption: builtins.str,
        hash: builtins.str,
        lifetime: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#encryption ComputeVpnEndpointV2#encryption}.
        :param hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#hash ComputeVpnEndpointV2#hash}.
        :param lifetime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#lifetime ComputeVpnEndpointV2#lifetime}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeVpnEndpointV2PhaseTwoSettings.__init__)
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument hash", value=hash, expected_type=type_hints["hash"])
            check_type(argname="argument lifetime", value=lifetime, expected_type=type_hints["lifetime"])
        self._values: typing.Dict[str, typing.Any] = {
            "encryption": encryption,
            "hash": hash,
        }
        if lifetime is not None:
            self._values["lifetime"] = lifetime

    @builtins.property
    def encryption(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#encryption ComputeVpnEndpointV2#encryption}.'''
        result = self._values.get("encryption")
        assert result is not None, "Required property 'encryption' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hash(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#hash ComputeVpnEndpointV2#hash}.'''
        result = self._values.get("hash")
        assert result is not None, "Required property 'hash' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lifetime(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#lifetime ComputeVpnEndpointV2#lifetime}.'''
        result = self._values.get("lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeVpnEndpointV2PhaseTwoSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeVpnEndpointV2PhaseTwoSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeVpnEndpointV2.ComputeVpnEndpointV2PhaseTwoSettingsOutputReference",
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
            type_hints = typing.get_type_hints(ComputeVpnEndpointV2PhaseTwoSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLifetime")
    def reset_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifetime", []))

    @builtins.property
    @jsii.member(jsii_name="encryptionInput")
    def encryption_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="hashInput")
    def hash_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hashInput"))

    @builtins.property
    @jsii.member(jsii_name="lifetimeInput")
    def lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="encryption")
    def encryption(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryption"))

    @encryption.setter
    def encryption(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2PhaseTwoSettingsOutputReference, "encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryption", value)

    @builtins.property
    @jsii.member(jsii_name="hash")
    def hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hash"))

    @hash.setter
    def hash(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2PhaseTwoSettingsOutputReference, "hash").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hash", value)

    @builtins.property
    @jsii.member(jsii_name="lifetime")
    def lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lifetime"))

    @lifetime.setter
    def lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2PhaseTwoSettingsOutputReference, "lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifetime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ComputeVpnEndpointV2PhaseTwoSettings]:
        return typing.cast(typing.Optional[ComputeVpnEndpointV2PhaseTwoSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeVpnEndpointV2PhaseTwoSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2PhaseTwoSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeVpnEndpointV2.ComputeVpnEndpointV2Timeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class ComputeVpnEndpointV2Timeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#create ComputeVpnEndpointV2#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#delete ComputeVpnEndpointV2#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#update ComputeVpnEndpointV2#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeVpnEndpointV2Timeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#create ComputeVpnEndpointV2#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#delete ComputeVpnEndpointV2#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#update ComputeVpnEndpointV2#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeVpnEndpointV2Timeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeVpnEndpointV2TimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeVpnEndpointV2.ComputeVpnEndpointV2TimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ComputeVpnEndpointV2TimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

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
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2TimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2TimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2TimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeVpnEndpointV2Timeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeVpnEndpointV2Timeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeVpnEndpointV2Timeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeVpnEndpointV2TimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ComputeVpnEndpointV2",
    "ComputeVpnEndpointV2Config",
    "ComputeVpnEndpointV2PhaseOneSettings",
    "ComputeVpnEndpointV2PhaseOneSettingsOutputReference",
    "ComputeVpnEndpointV2PhaseTwoSettings",
    "ComputeVpnEndpointV2PhaseTwoSettingsOutputReference",
    "ComputeVpnEndpointV2Timeouts",
    "ComputeVpnEndpointV2TimeoutsOutputReference",
]

publication.publish()
