'''
# `vsphere_host_port_group`

Refer to the Terraform Registory for docs: [`vsphere_host_port_group`](https://www.terraform.io/docs/providers/vsphere/r/host_port_group).
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


class HostPortGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.hostPortGroup.HostPortGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group vsphere_host_port_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        host_system_id: builtins.str,
        name: builtins.str,
        virtual_switch_name: builtins.str,
        active_nics: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_forged_transmits: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_mac_changes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_promiscuous: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        check_beacon: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        failback: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        notify_switches: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        shaping_average_bandwidth: typing.Optional[jsii.Number] = None,
        shaping_burst_size: typing.Optional[jsii.Number] = None,
        shaping_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        shaping_peak_bandwidth: typing.Optional[jsii.Number] = None,
        standby_nics: typing.Optional[typing.Sequence[builtins.str]] = None,
        teaming_policy: typing.Optional[builtins.str] = None,
        vlan_id: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group vsphere_host_port_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param host_system_id: The managed object ID of the host to set the virtual switch up on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#host_system_id HostPortGroup#host_system_id}
        :param name: The name of the port group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#name HostPortGroup#name}
        :param virtual_switch_name: The name of the virtual switch to bind this port group to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#virtual_switch_name HostPortGroup#virtual_switch_name}
        :param active_nics: List of active network adapters used for load balancing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#active_nics HostPortGroup#active_nics}
        :param allow_forged_transmits: Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than that of its own. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#allow_forged_transmits HostPortGroup#allow_forged_transmits}
        :param allow_mac_changes: Controls whether or not the Media Access Control (MAC) address can be changed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#allow_mac_changes HostPortGroup#allow_mac_changes}
        :param allow_promiscuous: Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#allow_promiscuous HostPortGroup#allow_promiscuous}
        :param check_beacon: Enable beacon probing. Requires that the vSwitch has been configured to use a beacon. If disabled, link status is used only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#check_beacon HostPortGroup#check_beacon}
        :param failback: If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#failback HostPortGroup#failback}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#id HostPortGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notify_switches: If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#notify_switches HostPortGroup#notify_switches}
        :param shaping_average_bandwidth: The average bandwidth in bits per second if traffic shaping is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#shaping_average_bandwidth HostPortGroup#shaping_average_bandwidth}
        :param shaping_burst_size: The maximum burst size allowed in bytes if traffic shaping is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#shaping_burst_size HostPortGroup#shaping_burst_size}
        :param shaping_enabled: Enable traffic shaping on this virtual switch or port group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#shaping_enabled HostPortGroup#shaping_enabled}
        :param shaping_peak_bandwidth: The peak bandwidth during bursts in bits per second if traffic shaping is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#shaping_peak_bandwidth HostPortGroup#shaping_peak_bandwidth}
        :param standby_nics: List of standby network adapters used for failover. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#standby_nics HostPortGroup#standby_nics}
        :param teaming_policy: The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, or failover_explicit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#teaming_policy HostPortGroup#teaming_policy}
        :param vlan_id: The VLAN ID/trunk mode for this port group. An ID of 0 denotes no tagging, an ID of 1-4094 tags with the specific ID, and an ID of 4095 enables trunk mode, allowing the guest to manage its own tagging. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#vlan_id HostPortGroup#vlan_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HostPortGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = HostPortGroupConfig(
            host_system_id=host_system_id,
            name=name,
            virtual_switch_name=virtual_switch_name,
            active_nics=active_nics,
            allow_forged_transmits=allow_forged_transmits,
            allow_mac_changes=allow_mac_changes,
            allow_promiscuous=allow_promiscuous,
            check_beacon=check_beacon,
            failback=failback,
            id=id,
            notify_switches=notify_switches,
            shaping_average_bandwidth=shaping_average_bandwidth,
            shaping_burst_size=shaping_burst_size,
            shaping_enabled=shaping_enabled,
            shaping_peak_bandwidth=shaping_peak_bandwidth,
            standby_nics=standby_nics,
            teaming_policy=teaming_policy,
            vlan_id=vlan_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetActiveNics")
    def reset_active_nics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActiveNics", []))

    @jsii.member(jsii_name="resetAllowForgedTransmits")
    def reset_allow_forged_transmits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowForgedTransmits", []))

    @jsii.member(jsii_name="resetAllowMacChanges")
    def reset_allow_mac_changes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowMacChanges", []))

    @jsii.member(jsii_name="resetAllowPromiscuous")
    def reset_allow_promiscuous(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowPromiscuous", []))

    @jsii.member(jsii_name="resetCheckBeacon")
    def reset_check_beacon(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckBeacon", []))

    @jsii.member(jsii_name="resetFailback")
    def reset_failback(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailback", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNotifySwitches")
    def reset_notify_switches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotifySwitches", []))

    @jsii.member(jsii_name="resetShapingAverageBandwidth")
    def reset_shaping_average_bandwidth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShapingAverageBandwidth", []))

    @jsii.member(jsii_name="resetShapingBurstSize")
    def reset_shaping_burst_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShapingBurstSize", []))

    @jsii.member(jsii_name="resetShapingEnabled")
    def reset_shaping_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShapingEnabled", []))

    @jsii.member(jsii_name="resetShapingPeakBandwidth")
    def reset_shaping_peak_bandwidth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShapingPeakBandwidth", []))

    @jsii.member(jsii_name="resetStandbyNics")
    def reset_standby_nics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStandbyNics", []))

    @jsii.member(jsii_name="resetTeamingPolicy")
    def reset_teaming_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeamingPolicy", []))

    @jsii.member(jsii_name="resetVlanId")
    def reset_vlan_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVlanId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="computedPolicy")
    def computed_policy(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "computedPolicy"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> "HostPortGroupPortsList":
        return typing.cast("HostPortGroupPortsList", jsii.get(self, "ports"))

    @builtins.property
    @jsii.member(jsii_name="activeNicsInput")
    def active_nics_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "activeNicsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowForgedTransmitsInput")
    def allow_forged_transmits_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowForgedTransmitsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowMacChangesInput")
    def allow_mac_changes_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowMacChangesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowPromiscuousInput")
    def allow_promiscuous_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowPromiscuousInput"))

    @builtins.property
    @jsii.member(jsii_name="checkBeaconInput")
    def check_beacon_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "checkBeaconInput"))

    @builtins.property
    @jsii.member(jsii_name="failbackInput")
    def failback_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "failbackInput"))

    @builtins.property
    @jsii.member(jsii_name="hostSystemIdInput")
    def host_system_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostSystemIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notifySwitchesInput")
    def notify_switches_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "notifySwitchesInput"))

    @builtins.property
    @jsii.member(jsii_name="shapingAverageBandwidthInput")
    def shaping_average_bandwidth_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "shapingAverageBandwidthInput"))

    @builtins.property
    @jsii.member(jsii_name="shapingBurstSizeInput")
    def shaping_burst_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "shapingBurstSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="shapingEnabledInput")
    def shaping_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "shapingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="shapingPeakBandwidthInput")
    def shaping_peak_bandwidth_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "shapingPeakBandwidthInput"))

    @builtins.property
    @jsii.member(jsii_name="standbyNicsInput")
    def standby_nics_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "standbyNicsInput"))

    @builtins.property
    @jsii.member(jsii_name="teamingPolicyInput")
    def teaming_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualSwitchNameInput")
    def virtual_switch_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualSwitchNameInput"))

    @builtins.property
    @jsii.member(jsii_name="vlanIdInput")
    def vlan_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vlanIdInput"))

    @builtins.property
    @jsii.member(jsii_name="activeNics")
    def active_nics(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "activeNics"))

    @active_nics.setter
    def active_nics(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroup, "active_nics").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activeNics", value)

    @builtins.property
    @jsii.member(jsii_name="allowForgedTransmits")
    def allow_forged_transmits(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowForgedTransmits"))

    @allow_forged_transmits.setter
    def allow_forged_transmits(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroup, "allow_forged_transmits").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowForgedTransmits", value)

    @builtins.property
    @jsii.member(jsii_name="allowMacChanges")
    def allow_mac_changes(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowMacChanges"))

    @allow_mac_changes.setter
    def allow_mac_changes(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroup, "allow_mac_changes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowMacChanges", value)

    @builtins.property
    @jsii.member(jsii_name="allowPromiscuous")
    def allow_promiscuous(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowPromiscuous"))

    @allow_promiscuous.setter
    def allow_promiscuous(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroup, "allow_promiscuous").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowPromiscuous", value)

    @builtins.property
    @jsii.member(jsii_name="checkBeacon")
    def check_beacon(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "checkBeacon"))

    @check_beacon.setter
    def check_beacon(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroup, "check_beacon").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkBeacon", value)

    @builtins.property
    @jsii.member(jsii_name="failback")
    def failback(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "failback"))

    @failback.setter
    def failback(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroup, "failback").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failback", value)

    @builtins.property
    @jsii.member(jsii_name="hostSystemId")
    def host_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostSystemId"))

    @host_system_id.setter
    def host_system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroup, "host_system_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostSystemId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroup, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notifySwitches")
    def notify_switches(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "notifySwitches"))

    @notify_switches.setter
    def notify_switches(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroup, "notify_switches").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifySwitches", value)

    @builtins.property
    @jsii.member(jsii_name="shapingAverageBandwidth")
    def shaping_average_bandwidth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "shapingAverageBandwidth"))

    @shaping_average_bandwidth.setter
    def shaping_average_bandwidth(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroup, "shaping_average_bandwidth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shapingAverageBandwidth", value)

    @builtins.property
    @jsii.member(jsii_name="shapingBurstSize")
    def shaping_burst_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "shapingBurstSize"))

    @shaping_burst_size.setter
    def shaping_burst_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroup, "shaping_burst_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shapingBurstSize", value)

    @builtins.property
    @jsii.member(jsii_name="shapingEnabled")
    def shaping_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "shapingEnabled"))

    @shaping_enabled.setter
    def shaping_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroup, "shaping_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shapingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="shapingPeakBandwidth")
    def shaping_peak_bandwidth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "shapingPeakBandwidth"))

    @shaping_peak_bandwidth.setter
    def shaping_peak_bandwidth(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroup, "shaping_peak_bandwidth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shapingPeakBandwidth", value)

    @builtins.property
    @jsii.member(jsii_name="standbyNics")
    def standby_nics(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "standbyNics"))

    @standby_nics.setter
    def standby_nics(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroup, "standby_nics").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "standbyNics", value)

    @builtins.property
    @jsii.member(jsii_name="teamingPolicy")
    def teaming_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "teamingPolicy"))

    @teaming_policy.setter
    def teaming_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroup, "teaming_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="virtualSwitchName")
    def virtual_switch_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualSwitchName"))

    @virtual_switch_name.setter
    def virtual_switch_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroup, "virtual_switch_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualSwitchName", value)

    @builtins.property
    @jsii.member(jsii_name="vlanId")
    def vlan_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vlanId"))

    @vlan_id.setter
    def vlan_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroup, "vlan_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vlanId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.hostPortGroup.HostPortGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "host_system_id": "hostSystemId",
        "name": "name",
        "virtual_switch_name": "virtualSwitchName",
        "active_nics": "activeNics",
        "allow_forged_transmits": "allowForgedTransmits",
        "allow_mac_changes": "allowMacChanges",
        "allow_promiscuous": "allowPromiscuous",
        "check_beacon": "checkBeacon",
        "failback": "failback",
        "id": "id",
        "notify_switches": "notifySwitches",
        "shaping_average_bandwidth": "shapingAverageBandwidth",
        "shaping_burst_size": "shapingBurstSize",
        "shaping_enabled": "shapingEnabled",
        "shaping_peak_bandwidth": "shapingPeakBandwidth",
        "standby_nics": "standbyNics",
        "teaming_policy": "teamingPolicy",
        "vlan_id": "vlanId",
    },
)
class HostPortGroupConfig(cdktf.TerraformMetaArguments):
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
        host_system_id: builtins.str,
        name: builtins.str,
        virtual_switch_name: builtins.str,
        active_nics: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_forged_transmits: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_mac_changes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_promiscuous: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        check_beacon: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        failback: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        notify_switches: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        shaping_average_bandwidth: typing.Optional[jsii.Number] = None,
        shaping_burst_size: typing.Optional[jsii.Number] = None,
        shaping_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        shaping_peak_bandwidth: typing.Optional[jsii.Number] = None,
        standby_nics: typing.Optional[typing.Sequence[builtins.str]] = None,
        teaming_policy: typing.Optional[builtins.str] = None,
        vlan_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param host_system_id: The managed object ID of the host to set the virtual switch up on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#host_system_id HostPortGroup#host_system_id}
        :param name: The name of the port group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#name HostPortGroup#name}
        :param virtual_switch_name: The name of the virtual switch to bind this port group to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#virtual_switch_name HostPortGroup#virtual_switch_name}
        :param active_nics: List of active network adapters used for load balancing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#active_nics HostPortGroup#active_nics}
        :param allow_forged_transmits: Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than that of its own. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#allow_forged_transmits HostPortGroup#allow_forged_transmits}
        :param allow_mac_changes: Controls whether or not the Media Access Control (MAC) address can be changed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#allow_mac_changes HostPortGroup#allow_mac_changes}
        :param allow_promiscuous: Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#allow_promiscuous HostPortGroup#allow_promiscuous}
        :param check_beacon: Enable beacon probing. Requires that the vSwitch has been configured to use a beacon. If disabled, link status is used only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#check_beacon HostPortGroup#check_beacon}
        :param failback: If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#failback HostPortGroup#failback}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#id HostPortGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notify_switches: If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#notify_switches HostPortGroup#notify_switches}
        :param shaping_average_bandwidth: The average bandwidth in bits per second if traffic shaping is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#shaping_average_bandwidth HostPortGroup#shaping_average_bandwidth}
        :param shaping_burst_size: The maximum burst size allowed in bytes if traffic shaping is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#shaping_burst_size HostPortGroup#shaping_burst_size}
        :param shaping_enabled: Enable traffic shaping on this virtual switch or port group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#shaping_enabled HostPortGroup#shaping_enabled}
        :param shaping_peak_bandwidth: The peak bandwidth during bursts in bits per second if traffic shaping is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#shaping_peak_bandwidth HostPortGroup#shaping_peak_bandwidth}
        :param standby_nics: List of standby network adapters used for failover. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#standby_nics HostPortGroup#standby_nics}
        :param teaming_policy: The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, or failover_explicit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#teaming_policy HostPortGroup#teaming_policy}
        :param vlan_id: The VLAN ID/trunk mode for this port group. An ID of 0 denotes no tagging, an ID of 1-4094 tags with the specific ID, and an ID of 4095 enables trunk mode, allowing the guest to manage its own tagging. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#vlan_id HostPortGroup#vlan_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(HostPortGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument host_system_id", value=host_system_id, expected_type=type_hints["host_system_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument virtual_switch_name", value=virtual_switch_name, expected_type=type_hints["virtual_switch_name"])
            check_type(argname="argument active_nics", value=active_nics, expected_type=type_hints["active_nics"])
            check_type(argname="argument allow_forged_transmits", value=allow_forged_transmits, expected_type=type_hints["allow_forged_transmits"])
            check_type(argname="argument allow_mac_changes", value=allow_mac_changes, expected_type=type_hints["allow_mac_changes"])
            check_type(argname="argument allow_promiscuous", value=allow_promiscuous, expected_type=type_hints["allow_promiscuous"])
            check_type(argname="argument check_beacon", value=check_beacon, expected_type=type_hints["check_beacon"])
            check_type(argname="argument failback", value=failback, expected_type=type_hints["failback"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument notify_switches", value=notify_switches, expected_type=type_hints["notify_switches"])
            check_type(argname="argument shaping_average_bandwidth", value=shaping_average_bandwidth, expected_type=type_hints["shaping_average_bandwidth"])
            check_type(argname="argument shaping_burst_size", value=shaping_burst_size, expected_type=type_hints["shaping_burst_size"])
            check_type(argname="argument shaping_enabled", value=shaping_enabled, expected_type=type_hints["shaping_enabled"])
            check_type(argname="argument shaping_peak_bandwidth", value=shaping_peak_bandwidth, expected_type=type_hints["shaping_peak_bandwidth"])
            check_type(argname="argument standby_nics", value=standby_nics, expected_type=type_hints["standby_nics"])
            check_type(argname="argument teaming_policy", value=teaming_policy, expected_type=type_hints["teaming_policy"])
            check_type(argname="argument vlan_id", value=vlan_id, expected_type=type_hints["vlan_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "host_system_id": host_system_id,
            "name": name,
            "virtual_switch_name": virtual_switch_name,
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
        if active_nics is not None:
            self._values["active_nics"] = active_nics
        if allow_forged_transmits is not None:
            self._values["allow_forged_transmits"] = allow_forged_transmits
        if allow_mac_changes is not None:
            self._values["allow_mac_changes"] = allow_mac_changes
        if allow_promiscuous is not None:
            self._values["allow_promiscuous"] = allow_promiscuous
        if check_beacon is not None:
            self._values["check_beacon"] = check_beacon
        if failback is not None:
            self._values["failback"] = failback
        if id is not None:
            self._values["id"] = id
        if notify_switches is not None:
            self._values["notify_switches"] = notify_switches
        if shaping_average_bandwidth is not None:
            self._values["shaping_average_bandwidth"] = shaping_average_bandwidth
        if shaping_burst_size is not None:
            self._values["shaping_burst_size"] = shaping_burst_size
        if shaping_enabled is not None:
            self._values["shaping_enabled"] = shaping_enabled
        if shaping_peak_bandwidth is not None:
            self._values["shaping_peak_bandwidth"] = shaping_peak_bandwidth
        if standby_nics is not None:
            self._values["standby_nics"] = standby_nics
        if teaming_policy is not None:
            self._values["teaming_policy"] = teaming_policy
        if vlan_id is not None:
            self._values["vlan_id"] = vlan_id

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
    def host_system_id(self) -> builtins.str:
        '''The managed object ID of the host to set the virtual switch up on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#host_system_id HostPortGroup#host_system_id}
        '''
        result = self._values.get("host_system_id")
        assert result is not None, "Required property 'host_system_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the port group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#name HostPortGroup#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_switch_name(self) -> builtins.str:
        '''The name of the virtual switch to bind this port group to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#virtual_switch_name HostPortGroup#virtual_switch_name}
        '''
        result = self._values.get("virtual_switch_name")
        assert result is not None, "Required property 'virtual_switch_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active_nics(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of active network adapters used for load balancing.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#active_nics HostPortGroup#active_nics}
        '''
        result = self._values.get("active_nics")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_forged_transmits(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than that of its own.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#allow_forged_transmits HostPortGroup#allow_forged_transmits}
        '''
        result = self._values.get("allow_forged_transmits")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_mac_changes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Controls whether or not the Media Access Control (MAC) address can be changed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#allow_mac_changes HostPortGroup#allow_mac_changes}
        '''
        result = self._values.get("allow_mac_changes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_promiscuous(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable promiscuous mode on the network.

        This flag indicates whether or not all traffic is seen on a given port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#allow_promiscuous HostPortGroup#allow_promiscuous}
        '''
        result = self._values.get("allow_promiscuous")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def check_beacon(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable beacon probing.

        Requires that the vSwitch has been configured to use a beacon. If disabled, link status is used only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#check_beacon HostPortGroup#check_beacon}
        '''
        result = self._values.get("check_beacon")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def failback(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#failback HostPortGroup#failback}
        '''
        result = self._values.get("failback")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#id HostPortGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notify_switches(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#notify_switches HostPortGroup#notify_switches}
        '''
        result = self._values.get("notify_switches")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def shaping_average_bandwidth(self) -> typing.Optional[jsii.Number]:
        '''The average bandwidth in bits per second if traffic shaping is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#shaping_average_bandwidth HostPortGroup#shaping_average_bandwidth}
        '''
        result = self._values.get("shaping_average_bandwidth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def shaping_burst_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum burst size allowed in bytes if traffic shaping is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#shaping_burst_size HostPortGroup#shaping_burst_size}
        '''
        result = self._values.get("shaping_burst_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def shaping_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable traffic shaping on this virtual switch or port group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#shaping_enabled HostPortGroup#shaping_enabled}
        '''
        result = self._values.get("shaping_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def shaping_peak_bandwidth(self) -> typing.Optional[jsii.Number]:
        '''The peak bandwidth during bursts in bits per second if traffic shaping is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#shaping_peak_bandwidth HostPortGroup#shaping_peak_bandwidth}
        '''
        result = self._values.get("shaping_peak_bandwidth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def standby_nics(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of standby network adapters used for failover.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#standby_nics HostPortGroup#standby_nics}
        '''
        result = self._values.get("standby_nics")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def teaming_policy(self) -> typing.Optional[builtins.str]:
        '''The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, or failover_explicit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#teaming_policy HostPortGroup#teaming_policy}
        '''
        result = self._values.get("teaming_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vlan_id(self) -> typing.Optional[jsii.Number]:
        '''The VLAN ID/trunk mode for this port group.

        An ID of 0 denotes no tagging, an ID of 1-4094 tags with the specific ID, and an ID of 4095 enables trunk mode, allowing the guest to manage its own tagging.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/host_port_group#vlan_id HostPortGroup#vlan_id}
        '''
        result = self._values.get("vlan_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostPortGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.hostPortGroup.HostPortGroupPorts",
    jsii_struct_bases=[],
    name_mapping={},
)
class HostPortGroupPorts:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostPortGroupPorts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HostPortGroupPortsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.hostPortGroup.HostPortGroupPortsList",
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
            type_hints = typing.get_type_hints(HostPortGroupPortsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "HostPortGroupPortsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HostPortGroupPortsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HostPortGroupPortsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroupPortsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(HostPortGroupPortsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(HostPortGroupPortsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class HostPortGroupPortsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.hostPortGroup.HostPortGroupPortsOutputReference",
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
            type_hints = typing.get_type_hints(HostPortGroupPortsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="macAddresses")
    def mac_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "macAddresses"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HostPortGroupPorts]:
        return typing.cast(typing.Optional[HostPortGroupPorts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[HostPortGroupPorts]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostPortGroupPortsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "HostPortGroup",
    "HostPortGroupConfig",
    "HostPortGroupPorts",
    "HostPortGroupPortsList",
    "HostPortGroupPortsOutputReference",
]

publication.publish()
