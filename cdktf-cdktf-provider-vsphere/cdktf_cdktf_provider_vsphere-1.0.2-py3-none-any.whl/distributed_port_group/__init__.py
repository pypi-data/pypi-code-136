'''
# `vsphere_distributed_port_group`

Refer to the Terraform Registory for docs: [`vsphere_distributed_port_group`](https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group).
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


class DistributedPortGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.distributedPortGroup.DistributedPortGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group vsphere_distributed_port_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        distributed_virtual_switch_uuid: builtins.str,
        name: builtins.str,
        active_uplinks: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_forged_transmits: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_mac_changes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_promiscuous: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_expand: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        block_all_ports: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        block_override_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        check_beacon: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        directpath_gen2_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        egress_shaping_average_bandwidth: typing.Optional[jsii.Number] = None,
        egress_shaping_burst_size: typing.Optional[jsii.Number] = None,
        egress_shaping_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        egress_shaping_peak_bandwidth: typing.Optional[jsii.Number] = None,
        failback: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ingress_shaping_average_bandwidth: typing.Optional[jsii.Number] = None,
        ingress_shaping_burst_size: typing.Optional[jsii.Number] = None,
        ingress_shaping_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ingress_shaping_peak_bandwidth: typing.Optional[jsii.Number] = None,
        lacp_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        lacp_mode: typing.Optional[builtins.str] = None,
        live_port_moving_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        netflow_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        netflow_override_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        network_resource_pool_key: typing.Optional[builtins.str] = None,
        network_resource_pool_override_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        notify_switches: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        number_of_ports: typing.Optional[jsii.Number] = None,
        port_config_reset_at_disconnect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        port_name_format: typing.Optional[builtins.str] = None,
        port_private_secondary_vlan_id: typing.Optional[jsii.Number] = None,
        security_policy_override_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        shaping_override_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        standby_uplinks: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        teaming_policy: typing.Optional[builtins.str] = None,
        traffic_filter_override_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tx_uplink: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        type: typing.Optional[builtins.str] = None,
        uplink_teaming_override_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        vlan_id: typing.Optional[jsii.Number] = None,
        vlan_override_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        vlan_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DistributedPortGroupVlanRange", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group vsphere_distributed_port_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param distributed_virtual_switch_uuid: The UUID of the DVS to attach this port group to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#distributed_virtual_switch_uuid DistributedPortGroup#distributed_virtual_switch_uuid}
        :param name: The name of the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#name DistributedPortGroup#name}
        :param active_uplinks: List of active uplinks used for load balancing, matching the names of the uplinks assigned in the DVS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#active_uplinks DistributedPortGroup#active_uplinks}
        :param allow_forged_transmits: Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than that of its own. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#allow_forged_transmits DistributedPortGroup#allow_forged_transmits}
        :param allow_mac_changes: Controls whether or not the Media Access Control (MAC) address can be changed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#allow_mac_changes DistributedPortGroup#allow_mac_changes}
        :param allow_promiscuous: Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#allow_promiscuous DistributedPortGroup#allow_promiscuous}
        :param auto_expand: Auto-expands the port group beyond the port count configured in number_of_ports when necessary. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#auto_expand DistributedPortGroup#auto_expand}
        :param block_all_ports: Indicates whether to block all ports by default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#block_all_ports DistributedPortGroup#block_all_ports}
        :param block_override_allowed: Allow the blocked setting of an individual port to override the setting in the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#block_override_allowed DistributedPortGroup#block_override_allowed}
        :param check_beacon: Enable beacon probing on the ports this policy applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#check_beacon DistributedPortGroup#check_beacon}
        :param custom_attributes: A list of custom attributes to set on this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#custom_attributes DistributedPortGroup#custom_attributes}
        :param description: The description of the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#description DistributedPortGroup#description}
        :param directpath_gen2_allowed: Allow VMDirectPath Gen2 on the ports this policy applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#directpath_gen2_allowed DistributedPortGroup#directpath_gen2_allowed}
        :param egress_shaping_average_bandwidth: The average egress bandwidth in bits per second if egress shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#egress_shaping_average_bandwidth DistributedPortGroup#egress_shaping_average_bandwidth}
        :param egress_shaping_burst_size: The maximum egress burst size allowed in bytes if egress shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#egress_shaping_burst_size DistributedPortGroup#egress_shaping_burst_size}
        :param egress_shaping_enabled: True if the traffic shaper is enabled for egress traffic on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#egress_shaping_enabled DistributedPortGroup#egress_shaping_enabled}
        :param egress_shaping_peak_bandwidth: The peak egress bandwidth during bursts in bits per second if egress traffic shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#egress_shaping_peak_bandwidth DistributedPortGroup#egress_shaping_peak_bandwidth}
        :param failback: If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#failback DistributedPortGroup#failback}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#id DistributedPortGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ingress_shaping_average_bandwidth: The average ingress bandwidth in bits per second if ingress shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#ingress_shaping_average_bandwidth DistributedPortGroup#ingress_shaping_average_bandwidth}
        :param ingress_shaping_burst_size: The maximum ingress burst size allowed in bytes if ingress shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#ingress_shaping_burst_size DistributedPortGroup#ingress_shaping_burst_size}
        :param ingress_shaping_enabled: True if the traffic shaper is enabled for ingress traffic on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#ingress_shaping_enabled DistributedPortGroup#ingress_shaping_enabled}
        :param ingress_shaping_peak_bandwidth: The peak ingress bandwidth during bursts in bits per second if ingress traffic shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#ingress_shaping_peak_bandwidth DistributedPortGroup#ingress_shaping_peak_bandwidth}
        :param lacp_enabled: Whether or not to enable LACP on all uplink ports. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#lacp_enabled DistributedPortGroup#lacp_enabled}
        :param lacp_mode: The uplink LACP mode to use. Can be one of active or passive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#lacp_mode DistributedPortGroup#lacp_mode}
        :param live_port_moving_allowed: Allow a live port to be moved in and out of the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#live_port_moving_allowed DistributedPortGroup#live_port_moving_allowed}
        :param netflow_enabled: Indicates whether to enable netflow on all ports. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#netflow_enabled DistributedPortGroup#netflow_enabled}
        :param netflow_override_allowed: Allow the enabling or disabling of Netflow on a port, contrary to the policy in the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#netflow_override_allowed DistributedPortGroup#netflow_override_allowed}
        :param network_resource_pool_key: The key of a network resource pool to associate with this portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#network_resource_pool_key DistributedPortGroup#network_resource_pool_key}
        :param network_resource_pool_override_allowed: Allow the network resource pool of an individual port to override the setting in the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#network_resource_pool_override_allowed DistributedPortGroup#network_resource_pool_override_allowed}
        :param notify_switches: If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#notify_switches DistributedPortGroup#notify_switches}
        :param number_of_ports: The number of ports in this portgroup. The DVS will expand and shrink by modifying this setting. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#number_of_ports DistributedPortGroup#number_of_ports}
        :param port_config_reset_at_disconnect: Reset the setting of any ports in this portgroup back to the default setting when the port disconnects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#port_config_reset_at_disconnect DistributedPortGroup#port_config_reset_at_disconnect}
        :param port_name_format: A template string to use when creating ports in the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#port_name_format DistributedPortGroup#port_name_format}
        :param port_private_secondary_vlan_id: The secondary VLAN ID for this port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#port_private_secondary_vlan_id DistributedPortGroup#port_private_secondary_vlan_id}
        :param security_policy_override_allowed: Allow security policy settings on a port to override those on the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#security_policy_override_allowed DistributedPortGroup#security_policy_override_allowed}
        :param shaping_override_allowed: Allow the traffic shaping policies of an individual port to override the settings in the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#shaping_override_allowed DistributedPortGroup#shaping_override_allowed}
        :param standby_uplinks: List of standby uplinks used for load balancing, matching the names of the uplinks assigned in the DVS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#standby_uplinks DistributedPortGroup#standby_uplinks}
        :param tags: A list of tag IDs to apply to this object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#tags DistributedPortGroup#tags}
        :param teaming_policy: The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, failover_explicit, or loadbalance_loadbased. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#teaming_policy DistributedPortGroup#teaming_policy}
        :param traffic_filter_override_allowed: Allow any filter policies set on the individual port to override those in the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#traffic_filter_override_allowed DistributedPortGroup#traffic_filter_override_allowed}
        :param tx_uplink: If true, a copy of packets sent to the switch will always be forwarded to an uplink in addition to the regular packet forwarded done by the switch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#tx_uplink DistributedPortGroup#tx_uplink}
        :param type: The type of portgroup. Can be one of earlyBinding (static) or ephemeral. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#type DistributedPortGroup#type}
        :param uplink_teaming_override_allowed: Allow the uplink teaming policies on a port to override those on the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#uplink_teaming_override_allowed DistributedPortGroup#uplink_teaming_override_allowed}
        :param vlan_id: The VLAN ID for single VLAN mode. 0 denotes no VLAN. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#vlan_id DistributedPortGroup#vlan_id}
        :param vlan_override_allowed: Allow the VLAN configuration on a port to override those on the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#vlan_override_allowed DistributedPortGroup#vlan_override_allowed}
        :param vlan_range: vlan_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#vlan_range DistributedPortGroup#vlan_range}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DistributedPortGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DistributedPortGroupConfig(
            distributed_virtual_switch_uuid=distributed_virtual_switch_uuid,
            name=name,
            active_uplinks=active_uplinks,
            allow_forged_transmits=allow_forged_transmits,
            allow_mac_changes=allow_mac_changes,
            allow_promiscuous=allow_promiscuous,
            auto_expand=auto_expand,
            block_all_ports=block_all_ports,
            block_override_allowed=block_override_allowed,
            check_beacon=check_beacon,
            custom_attributes=custom_attributes,
            description=description,
            directpath_gen2_allowed=directpath_gen2_allowed,
            egress_shaping_average_bandwidth=egress_shaping_average_bandwidth,
            egress_shaping_burst_size=egress_shaping_burst_size,
            egress_shaping_enabled=egress_shaping_enabled,
            egress_shaping_peak_bandwidth=egress_shaping_peak_bandwidth,
            failback=failback,
            id=id,
            ingress_shaping_average_bandwidth=ingress_shaping_average_bandwidth,
            ingress_shaping_burst_size=ingress_shaping_burst_size,
            ingress_shaping_enabled=ingress_shaping_enabled,
            ingress_shaping_peak_bandwidth=ingress_shaping_peak_bandwidth,
            lacp_enabled=lacp_enabled,
            lacp_mode=lacp_mode,
            live_port_moving_allowed=live_port_moving_allowed,
            netflow_enabled=netflow_enabled,
            netflow_override_allowed=netflow_override_allowed,
            network_resource_pool_key=network_resource_pool_key,
            network_resource_pool_override_allowed=network_resource_pool_override_allowed,
            notify_switches=notify_switches,
            number_of_ports=number_of_ports,
            port_config_reset_at_disconnect=port_config_reset_at_disconnect,
            port_name_format=port_name_format,
            port_private_secondary_vlan_id=port_private_secondary_vlan_id,
            security_policy_override_allowed=security_policy_override_allowed,
            shaping_override_allowed=shaping_override_allowed,
            standby_uplinks=standby_uplinks,
            tags=tags,
            teaming_policy=teaming_policy,
            traffic_filter_override_allowed=traffic_filter_override_allowed,
            tx_uplink=tx_uplink,
            type=type,
            uplink_teaming_override_allowed=uplink_teaming_override_allowed,
            vlan_id=vlan_id,
            vlan_override_allowed=vlan_override_allowed,
            vlan_range=vlan_range,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putVlanRange")
    def put_vlan_range(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DistributedPortGroupVlanRange", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DistributedPortGroup.put_vlan_range)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVlanRange", [value]))

    @jsii.member(jsii_name="resetActiveUplinks")
    def reset_active_uplinks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActiveUplinks", []))

    @jsii.member(jsii_name="resetAllowForgedTransmits")
    def reset_allow_forged_transmits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowForgedTransmits", []))

    @jsii.member(jsii_name="resetAllowMacChanges")
    def reset_allow_mac_changes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowMacChanges", []))

    @jsii.member(jsii_name="resetAllowPromiscuous")
    def reset_allow_promiscuous(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowPromiscuous", []))

    @jsii.member(jsii_name="resetAutoExpand")
    def reset_auto_expand(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoExpand", []))

    @jsii.member(jsii_name="resetBlockAllPorts")
    def reset_block_all_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockAllPorts", []))

    @jsii.member(jsii_name="resetBlockOverrideAllowed")
    def reset_block_override_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockOverrideAllowed", []))

    @jsii.member(jsii_name="resetCheckBeacon")
    def reset_check_beacon(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckBeacon", []))

    @jsii.member(jsii_name="resetCustomAttributes")
    def reset_custom_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomAttributes", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDirectpathGen2Allowed")
    def reset_directpath_gen2_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectpathGen2Allowed", []))

    @jsii.member(jsii_name="resetEgressShapingAverageBandwidth")
    def reset_egress_shaping_average_bandwidth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgressShapingAverageBandwidth", []))

    @jsii.member(jsii_name="resetEgressShapingBurstSize")
    def reset_egress_shaping_burst_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgressShapingBurstSize", []))

    @jsii.member(jsii_name="resetEgressShapingEnabled")
    def reset_egress_shaping_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgressShapingEnabled", []))

    @jsii.member(jsii_name="resetEgressShapingPeakBandwidth")
    def reset_egress_shaping_peak_bandwidth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgressShapingPeakBandwidth", []))

    @jsii.member(jsii_name="resetFailback")
    def reset_failback(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailback", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIngressShapingAverageBandwidth")
    def reset_ingress_shaping_average_bandwidth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressShapingAverageBandwidth", []))

    @jsii.member(jsii_name="resetIngressShapingBurstSize")
    def reset_ingress_shaping_burst_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressShapingBurstSize", []))

    @jsii.member(jsii_name="resetIngressShapingEnabled")
    def reset_ingress_shaping_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressShapingEnabled", []))

    @jsii.member(jsii_name="resetIngressShapingPeakBandwidth")
    def reset_ingress_shaping_peak_bandwidth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressShapingPeakBandwidth", []))

    @jsii.member(jsii_name="resetLacpEnabled")
    def reset_lacp_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLacpEnabled", []))

    @jsii.member(jsii_name="resetLacpMode")
    def reset_lacp_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLacpMode", []))

    @jsii.member(jsii_name="resetLivePortMovingAllowed")
    def reset_live_port_moving_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLivePortMovingAllowed", []))

    @jsii.member(jsii_name="resetNetflowEnabled")
    def reset_netflow_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetflowEnabled", []))

    @jsii.member(jsii_name="resetNetflowOverrideAllowed")
    def reset_netflow_override_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetflowOverrideAllowed", []))

    @jsii.member(jsii_name="resetNetworkResourcePoolKey")
    def reset_network_resource_pool_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkResourcePoolKey", []))

    @jsii.member(jsii_name="resetNetworkResourcePoolOverrideAllowed")
    def reset_network_resource_pool_override_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkResourcePoolOverrideAllowed", []))

    @jsii.member(jsii_name="resetNotifySwitches")
    def reset_notify_switches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotifySwitches", []))

    @jsii.member(jsii_name="resetNumberOfPorts")
    def reset_number_of_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumberOfPorts", []))

    @jsii.member(jsii_name="resetPortConfigResetAtDisconnect")
    def reset_port_config_reset_at_disconnect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortConfigResetAtDisconnect", []))

    @jsii.member(jsii_name="resetPortNameFormat")
    def reset_port_name_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortNameFormat", []))

    @jsii.member(jsii_name="resetPortPrivateSecondaryVlanId")
    def reset_port_private_secondary_vlan_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortPrivateSecondaryVlanId", []))

    @jsii.member(jsii_name="resetSecurityPolicyOverrideAllowed")
    def reset_security_policy_override_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityPolicyOverrideAllowed", []))

    @jsii.member(jsii_name="resetShapingOverrideAllowed")
    def reset_shaping_override_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShapingOverrideAllowed", []))

    @jsii.member(jsii_name="resetStandbyUplinks")
    def reset_standby_uplinks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStandbyUplinks", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTeamingPolicy")
    def reset_teaming_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeamingPolicy", []))

    @jsii.member(jsii_name="resetTrafficFilterOverrideAllowed")
    def reset_traffic_filter_override_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrafficFilterOverrideAllowed", []))

    @jsii.member(jsii_name="resetTxUplink")
    def reset_tx_uplink(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTxUplink", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetUplinkTeamingOverrideAllowed")
    def reset_uplink_teaming_override_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUplinkTeamingOverrideAllowed", []))

    @jsii.member(jsii_name="resetVlanId")
    def reset_vlan_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVlanId", []))

    @jsii.member(jsii_name="resetVlanOverrideAllowed")
    def reset_vlan_override_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVlanOverrideAllowed", []))

    @jsii.member(jsii_name="resetVlanRange")
    def reset_vlan_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVlanRange", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="configVersion")
    def config_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configVersion"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="vlanRange")
    def vlan_range(self) -> "DistributedPortGroupVlanRangeList":
        return typing.cast("DistributedPortGroupVlanRangeList", jsii.get(self, "vlanRange"))

    @builtins.property
    @jsii.member(jsii_name="activeUplinksInput")
    def active_uplinks_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "activeUplinksInput"))

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
    @jsii.member(jsii_name="autoExpandInput")
    def auto_expand_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoExpandInput"))

    @builtins.property
    @jsii.member(jsii_name="blockAllPortsInput")
    def block_all_ports_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "blockAllPortsInput"))

    @builtins.property
    @jsii.member(jsii_name="blockOverrideAllowedInput")
    def block_override_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "blockOverrideAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="checkBeaconInput")
    def check_beacon_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "checkBeaconInput"))

    @builtins.property
    @jsii.member(jsii_name="customAttributesInput")
    def custom_attributes_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="directpathGen2AllowedInput")
    def directpath_gen2_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "directpathGen2AllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="distributedVirtualSwitchUuidInput")
    def distributed_virtual_switch_uuid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "distributedVirtualSwitchUuidInput"))

    @builtins.property
    @jsii.member(jsii_name="egressShapingAverageBandwidthInput")
    def egress_shaping_average_bandwidth_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "egressShapingAverageBandwidthInput"))

    @builtins.property
    @jsii.member(jsii_name="egressShapingBurstSizeInput")
    def egress_shaping_burst_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "egressShapingBurstSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="egressShapingEnabledInput")
    def egress_shaping_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "egressShapingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="egressShapingPeakBandwidthInput")
    def egress_shaping_peak_bandwidth_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "egressShapingPeakBandwidthInput"))

    @builtins.property
    @jsii.member(jsii_name="failbackInput")
    def failback_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "failbackInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressShapingAverageBandwidthInput")
    def ingress_shaping_average_bandwidth_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ingressShapingAverageBandwidthInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressShapingBurstSizeInput")
    def ingress_shaping_burst_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ingressShapingBurstSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressShapingEnabledInput")
    def ingress_shaping_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ingressShapingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressShapingPeakBandwidthInput")
    def ingress_shaping_peak_bandwidth_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ingressShapingPeakBandwidthInput"))

    @builtins.property
    @jsii.member(jsii_name="lacpEnabledInput")
    def lacp_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "lacpEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="lacpModeInput")
    def lacp_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lacpModeInput"))

    @builtins.property
    @jsii.member(jsii_name="livePortMovingAllowedInput")
    def live_port_moving_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "livePortMovingAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="netflowEnabledInput")
    def netflow_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "netflowEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="netflowOverrideAllowedInput")
    def netflow_override_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "netflowOverrideAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="networkResourcePoolKeyInput")
    def network_resource_pool_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkResourcePoolKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="networkResourcePoolOverrideAllowedInput")
    def network_resource_pool_override_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "networkResourcePoolOverrideAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="notifySwitchesInput")
    def notify_switches_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "notifySwitchesInput"))

    @builtins.property
    @jsii.member(jsii_name="numberOfPortsInput")
    def number_of_ports_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberOfPortsInput"))

    @builtins.property
    @jsii.member(jsii_name="portConfigResetAtDisconnectInput")
    def port_config_reset_at_disconnect_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "portConfigResetAtDisconnectInput"))

    @builtins.property
    @jsii.member(jsii_name="portNameFormatInput")
    def port_name_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portNameFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="portPrivateSecondaryVlanIdInput")
    def port_private_secondary_vlan_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portPrivateSecondaryVlanIdInput"))

    @builtins.property
    @jsii.member(jsii_name="securityPolicyOverrideAllowedInput")
    def security_policy_override_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "securityPolicyOverrideAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="shapingOverrideAllowedInput")
    def shaping_override_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "shapingOverrideAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="standbyUplinksInput")
    def standby_uplinks_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "standbyUplinksInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="teamingPolicyInput")
    def teaming_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="trafficFilterOverrideAllowedInput")
    def traffic_filter_override_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "trafficFilterOverrideAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="txUplinkInput")
    def tx_uplink_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "txUplinkInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="uplinkTeamingOverrideAllowedInput")
    def uplink_teaming_override_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "uplinkTeamingOverrideAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="vlanIdInput")
    def vlan_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vlanIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vlanOverrideAllowedInput")
    def vlan_override_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "vlanOverrideAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="vlanRangeInput")
    def vlan_range_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DistributedPortGroupVlanRange"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DistributedPortGroupVlanRange"]]], jsii.get(self, "vlanRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="activeUplinks")
    def active_uplinks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "activeUplinks"))

    @active_uplinks.setter
    def active_uplinks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "active_uplinks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activeUplinks", value)

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
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "allow_forged_transmits").fset)
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
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "allow_mac_changes").fset)
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
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "allow_promiscuous").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowPromiscuous", value)

    @builtins.property
    @jsii.member(jsii_name="autoExpand")
    def auto_expand(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoExpand"))

    @auto_expand.setter
    def auto_expand(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "auto_expand").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoExpand", value)

    @builtins.property
    @jsii.member(jsii_name="blockAllPorts")
    def block_all_ports(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "blockAllPorts"))

    @block_all_ports.setter
    def block_all_ports(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "block_all_ports").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockAllPorts", value)

    @builtins.property
    @jsii.member(jsii_name="blockOverrideAllowed")
    def block_override_allowed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "blockOverrideAllowed"))

    @block_override_allowed.setter
    def block_override_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "block_override_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockOverrideAllowed", value)

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
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "check_beacon").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkBeacon", value)

    @builtins.property
    @jsii.member(jsii_name="customAttributes")
    def custom_attributes(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "customAttributes"))

    @custom_attributes.setter
    def custom_attributes(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "custom_attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="directpathGen2Allowed")
    def directpath_gen2_allowed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "directpathGen2Allowed"))

    @directpath_gen2_allowed.setter
    def directpath_gen2_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "directpath_gen2_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directpathGen2Allowed", value)

    @builtins.property
    @jsii.member(jsii_name="distributedVirtualSwitchUuid")
    def distributed_virtual_switch_uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "distributedVirtualSwitchUuid"))

    @distributed_virtual_switch_uuid.setter
    def distributed_virtual_switch_uuid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "distributed_virtual_switch_uuid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distributedVirtualSwitchUuid", value)

    @builtins.property
    @jsii.member(jsii_name="egressShapingAverageBandwidth")
    def egress_shaping_average_bandwidth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "egressShapingAverageBandwidth"))

    @egress_shaping_average_bandwidth.setter
    def egress_shaping_average_bandwidth(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "egress_shaping_average_bandwidth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egressShapingAverageBandwidth", value)

    @builtins.property
    @jsii.member(jsii_name="egressShapingBurstSize")
    def egress_shaping_burst_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "egressShapingBurstSize"))

    @egress_shaping_burst_size.setter
    def egress_shaping_burst_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "egress_shaping_burst_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egressShapingBurstSize", value)

    @builtins.property
    @jsii.member(jsii_name="egressShapingEnabled")
    def egress_shaping_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "egressShapingEnabled"))

    @egress_shaping_enabled.setter
    def egress_shaping_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "egress_shaping_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egressShapingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="egressShapingPeakBandwidth")
    def egress_shaping_peak_bandwidth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "egressShapingPeakBandwidth"))

    @egress_shaping_peak_bandwidth.setter
    def egress_shaping_peak_bandwidth(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "egress_shaping_peak_bandwidth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egressShapingPeakBandwidth", value)

    @builtins.property
    @jsii.member(jsii_name="failback")
    def failback(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "failback"))

    @failback.setter
    def failback(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "failback").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failback", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ingressShapingAverageBandwidth")
    def ingress_shaping_average_bandwidth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ingressShapingAverageBandwidth"))

    @ingress_shaping_average_bandwidth.setter
    def ingress_shaping_average_bandwidth(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "ingress_shaping_average_bandwidth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressShapingAverageBandwidth", value)

    @builtins.property
    @jsii.member(jsii_name="ingressShapingBurstSize")
    def ingress_shaping_burst_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ingressShapingBurstSize"))

    @ingress_shaping_burst_size.setter
    def ingress_shaping_burst_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "ingress_shaping_burst_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressShapingBurstSize", value)

    @builtins.property
    @jsii.member(jsii_name="ingressShapingEnabled")
    def ingress_shaping_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ingressShapingEnabled"))

    @ingress_shaping_enabled.setter
    def ingress_shaping_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "ingress_shaping_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressShapingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="ingressShapingPeakBandwidth")
    def ingress_shaping_peak_bandwidth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ingressShapingPeakBandwidth"))

    @ingress_shaping_peak_bandwidth.setter
    def ingress_shaping_peak_bandwidth(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "ingress_shaping_peak_bandwidth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressShapingPeakBandwidth", value)

    @builtins.property
    @jsii.member(jsii_name="lacpEnabled")
    def lacp_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "lacpEnabled"))

    @lacp_enabled.setter
    def lacp_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "lacp_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lacpEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="lacpMode")
    def lacp_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lacpMode"))

    @lacp_mode.setter
    def lacp_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "lacp_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lacpMode", value)

    @builtins.property
    @jsii.member(jsii_name="livePortMovingAllowed")
    def live_port_moving_allowed(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "livePortMovingAllowed"))

    @live_port_moving_allowed.setter
    def live_port_moving_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "live_port_moving_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "livePortMovingAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="netflowEnabled")
    def netflow_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "netflowEnabled"))

    @netflow_enabled.setter
    def netflow_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "netflow_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netflowEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="netflowOverrideAllowed")
    def netflow_override_allowed(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "netflowOverrideAllowed"))

    @netflow_override_allowed.setter
    def netflow_override_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "netflow_override_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netflowOverrideAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="networkResourcePoolKey")
    def network_resource_pool_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkResourcePoolKey"))

    @network_resource_pool_key.setter
    def network_resource_pool_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "network_resource_pool_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkResourcePoolKey", value)

    @builtins.property
    @jsii.member(jsii_name="networkResourcePoolOverrideAllowed")
    def network_resource_pool_override_allowed(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "networkResourcePoolOverrideAllowed"))

    @network_resource_pool_override_allowed.setter
    def network_resource_pool_override_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "network_resource_pool_override_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkResourcePoolOverrideAllowed", value)

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
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "notify_switches").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifySwitches", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfPorts")
    def number_of_ports(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numberOfPorts"))

    @number_of_ports.setter
    def number_of_ports(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "number_of_ports").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfPorts", value)

    @builtins.property
    @jsii.member(jsii_name="portConfigResetAtDisconnect")
    def port_config_reset_at_disconnect(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "portConfigResetAtDisconnect"))

    @port_config_reset_at_disconnect.setter
    def port_config_reset_at_disconnect(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "port_config_reset_at_disconnect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portConfigResetAtDisconnect", value)

    @builtins.property
    @jsii.member(jsii_name="portNameFormat")
    def port_name_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portNameFormat"))

    @port_name_format.setter
    def port_name_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "port_name_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portNameFormat", value)

    @builtins.property
    @jsii.member(jsii_name="portPrivateSecondaryVlanId")
    def port_private_secondary_vlan_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "portPrivateSecondaryVlanId"))

    @port_private_secondary_vlan_id.setter
    def port_private_secondary_vlan_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "port_private_secondary_vlan_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portPrivateSecondaryVlanId", value)

    @builtins.property
    @jsii.member(jsii_name="securityPolicyOverrideAllowed")
    def security_policy_override_allowed(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "securityPolicyOverrideAllowed"))

    @security_policy_override_allowed.setter
    def security_policy_override_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "security_policy_override_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityPolicyOverrideAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="shapingOverrideAllowed")
    def shaping_override_allowed(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "shapingOverrideAllowed"))

    @shaping_override_allowed.setter
    def shaping_override_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "shaping_override_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shapingOverrideAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="standbyUplinks")
    def standby_uplinks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "standbyUplinks"))

    @standby_uplinks.setter
    def standby_uplinks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "standby_uplinks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "standbyUplinks", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="teamingPolicy")
    def teaming_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "teamingPolicy"))

    @teaming_policy.setter
    def teaming_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "teaming_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="trafficFilterOverrideAllowed")
    def traffic_filter_override_allowed(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "trafficFilterOverrideAllowed"))

    @traffic_filter_override_allowed.setter
    def traffic_filter_override_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "traffic_filter_override_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trafficFilterOverrideAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="txUplink")
    def tx_uplink(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "txUplink"))

    @tx_uplink.setter
    def tx_uplink(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "tx_uplink").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "txUplink", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="uplinkTeamingOverrideAllowed")
    def uplink_teaming_override_allowed(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "uplinkTeamingOverrideAllowed"))

    @uplink_teaming_override_allowed.setter
    def uplink_teaming_override_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "uplink_teaming_override_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uplinkTeamingOverrideAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="vlanId")
    def vlan_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vlanId"))

    @vlan_id.setter
    def vlan_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "vlan_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vlanId", value)

    @builtins.property
    @jsii.member(jsii_name="vlanOverrideAllowed")
    def vlan_override_allowed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "vlanOverrideAllowed"))

    @vlan_override_allowed.setter
    def vlan_override_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroup, "vlan_override_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vlanOverrideAllowed", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.distributedPortGroup.DistributedPortGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "distributed_virtual_switch_uuid": "distributedVirtualSwitchUuid",
        "name": "name",
        "active_uplinks": "activeUplinks",
        "allow_forged_transmits": "allowForgedTransmits",
        "allow_mac_changes": "allowMacChanges",
        "allow_promiscuous": "allowPromiscuous",
        "auto_expand": "autoExpand",
        "block_all_ports": "blockAllPorts",
        "block_override_allowed": "blockOverrideAllowed",
        "check_beacon": "checkBeacon",
        "custom_attributes": "customAttributes",
        "description": "description",
        "directpath_gen2_allowed": "directpathGen2Allowed",
        "egress_shaping_average_bandwidth": "egressShapingAverageBandwidth",
        "egress_shaping_burst_size": "egressShapingBurstSize",
        "egress_shaping_enabled": "egressShapingEnabled",
        "egress_shaping_peak_bandwidth": "egressShapingPeakBandwidth",
        "failback": "failback",
        "id": "id",
        "ingress_shaping_average_bandwidth": "ingressShapingAverageBandwidth",
        "ingress_shaping_burst_size": "ingressShapingBurstSize",
        "ingress_shaping_enabled": "ingressShapingEnabled",
        "ingress_shaping_peak_bandwidth": "ingressShapingPeakBandwidth",
        "lacp_enabled": "lacpEnabled",
        "lacp_mode": "lacpMode",
        "live_port_moving_allowed": "livePortMovingAllowed",
        "netflow_enabled": "netflowEnabled",
        "netflow_override_allowed": "netflowOverrideAllowed",
        "network_resource_pool_key": "networkResourcePoolKey",
        "network_resource_pool_override_allowed": "networkResourcePoolOverrideAllowed",
        "notify_switches": "notifySwitches",
        "number_of_ports": "numberOfPorts",
        "port_config_reset_at_disconnect": "portConfigResetAtDisconnect",
        "port_name_format": "portNameFormat",
        "port_private_secondary_vlan_id": "portPrivateSecondaryVlanId",
        "security_policy_override_allowed": "securityPolicyOverrideAllowed",
        "shaping_override_allowed": "shapingOverrideAllowed",
        "standby_uplinks": "standbyUplinks",
        "tags": "tags",
        "teaming_policy": "teamingPolicy",
        "traffic_filter_override_allowed": "trafficFilterOverrideAllowed",
        "tx_uplink": "txUplink",
        "type": "type",
        "uplink_teaming_override_allowed": "uplinkTeamingOverrideAllowed",
        "vlan_id": "vlanId",
        "vlan_override_allowed": "vlanOverrideAllowed",
        "vlan_range": "vlanRange",
    },
)
class DistributedPortGroupConfig(cdktf.TerraformMetaArguments):
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
        distributed_virtual_switch_uuid: builtins.str,
        name: builtins.str,
        active_uplinks: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_forged_transmits: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_mac_changes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_promiscuous: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_expand: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        block_all_ports: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        block_override_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        check_beacon: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        directpath_gen2_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        egress_shaping_average_bandwidth: typing.Optional[jsii.Number] = None,
        egress_shaping_burst_size: typing.Optional[jsii.Number] = None,
        egress_shaping_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        egress_shaping_peak_bandwidth: typing.Optional[jsii.Number] = None,
        failback: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ingress_shaping_average_bandwidth: typing.Optional[jsii.Number] = None,
        ingress_shaping_burst_size: typing.Optional[jsii.Number] = None,
        ingress_shaping_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ingress_shaping_peak_bandwidth: typing.Optional[jsii.Number] = None,
        lacp_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        lacp_mode: typing.Optional[builtins.str] = None,
        live_port_moving_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        netflow_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        netflow_override_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        network_resource_pool_key: typing.Optional[builtins.str] = None,
        network_resource_pool_override_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        notify_switches: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        number_of_ports: typing.Optional[jsii.Number] = None,
        port_config_reset_at_disconnect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        port_name_format: typing.Optional[builtins.str] = None,
        port_private_secondary_vlan_id: typing.Optional[jsii.Number] = None,
        security_policy_override_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        shaping_override_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        standby_uplinks: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        teaming_policy: typing.Optional[builtins.str] = None,
        traffic_filter_override_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tx_uplink: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        type: typing.Optional[builtins.str] = None,
        uplink_teaming_override_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        vlan_id: typing.Optional[jsii.Number] = None,
        vlan_override_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        vlan_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DistributedPortGroupVlanRange", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param distributed_virtual_switch_uuid: The UUID of the DVS to attach this port group to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#distributed_virtual_switch_uuid DistributedPortGroup#distributed_virtual_switch_uuid}
        :param name: The name of the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#name DistributedPortGroup#name}
        :param active_uplinks: List of active uplinks used for load balancing, matching the names of the uplinks assigned in the DVS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#active_uplinks DistributedPortGroup#active_uplinks}
        :param allow_forged_transmits: Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than that of its own. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#allow_forged_transmits DistributedPortGroup#allow_forged_transmits}
        :param allow_mac_changes: Controls whether or not the Media Access Control (MAC) address can be changed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#allow_mac_changes DistributedPortGroup#allow_mac_changes}
        :param allow_promiscuous: Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#allow_promiscuous DistributedPortGroup#allow_promiscuous}
        :param auto_expand: Auto-expands the port group beyond the port count configured in number_of_ports when necessary. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#auto_expand DistributedPortGroup#auto_expand}
        :param block_all_ports: Indicates whether to block all ports by default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#block_all_ports DistributedPortGroup#block_all_ports}
        :param block_override_allowed: Allow the blocked setting of an individual port to override the setting in the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#block_override_allowed DistributedPortGroup#block_override_allowed}
        :param check_beacon: Enable beacon probing on the ports this policy applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#check_beacon DistributedPortGroup#check_beacon}
        :param custom_attributes: A list of custom attributes to set on this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#custom_attributes DistributedPortGroup#custom_attributes}
        :param description: The description of the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#description DistributedPortGroup#description}
        :param directpath_gen2_allowed: Allow VMDirectPath Gen2 on the ports this policy applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#directpath_gen2_allowed DistributedPortGroup#directpath_gen2_allowed}
        :param egress_shaping_average_bandwidth: The average egress bandwidth in bits per second if egress shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#egress_shaping_average_bandwidth DistributedPortGroup#egress_shaping_average_bandwidth}
        :param egress_shaping_burst_size: The maximum egress burst size allowed in bytes if egress shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#egress_shaping_burst_size DistributedPortGroup#egress_shaping_burst_size}
        :param egress_shaping_enabled: True if the traffic shaper is enabled for egress traffic on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#egress_shaping_enabled DistributedPortGroup#egress_shaping_enabled}
        :param egress_shaping_peak_bandwidth: The peak egress bandwidth during bursts in bits per second if egress traffic shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#egress_shaping_peak_bandwidth DistributedPortGroup#egress_shaping_peak_bandwidth}
        :param failback: If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#failback DistributedPortGroup#failback}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#id DistributedPortGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ingress_shaping_average_bandwidth: The average ingress bandwidth in bits per second if ingress shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#ingress_shaping_average_bandwidth DistributedPortGroup#ingress_shaping_average_bandwidth}
        :param ingress_shaping_burst_size: The maximum ingress burst size allowed in bytes if ingress shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#ingress_shaping_burst_size DistributedPortGroup#ingress_shaping_burst_size}
        :param ingress_shaping_enabled: True if the traffic shaper is enabled for ingress traffic on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#ingress_shaping_enabled DistributedPortGroup#ingress_shaping_enabled}
        :param ingress_shaping_peak_bandwidth: The peak ingress bandwidth during bursts in bits per second if ingress traffic shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#ingress_shaping_peak_bandwidth DistributedPortGroup#ingress_shaping_peak_bandwidth}
        :param lacp_enabled: Whether or not to enable LACP on all uplink ports. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#lacp_enabled DistributedPortGroup#lacp_enabled}
        :param lacp_mode: The uplink LACP mode to use. Can be one of active or passive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#lacp_mode DistributedPortGroup#lacp_mode}
        :param live_port_moving_allowed: Allow a live port to be moved in and out of the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#live_port_moving_allowed DistributedPortGroup#live_port_moving_allowed}
        :param netflow_enabled: Indicates whether to enable netflow on all ports. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#netflow_enabled DistributedPortGroup#netflow_enabled}
        :param netflow_override_allowed: Allow the enabling or disabling of Netflow on a port, contrary to the policy in the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#netflow_override_allowed DistributedPortGroup#netflow_override_allowed}
        :param network_resource_pool_key: The key of a network resource pool to associate with this portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#network_resource_pool_key DistributedPortGroup#network_resource_pool_key}
        :param network_resource_pool_override_allowed: Allow the network resource pool of an individual port to override the setting in the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#network_resource_pool_override_allowed DistributedPortGroup#network_resource_pool_override_allowed}
        :param notify_switches: If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#notify_switches DistributedPortGroup#notify_switches}
        :param number_of_ports: The number of ports in this portgroup. The DVS will expand and shrink by modifying this setting. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#number_of_ports DistributedPortGroup#number_of_ports}
        :param port_config_reset_at_disconnect: Reset the setting of any ports in this portgroup back to the default setting when the port disconnects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#port_config_reset_at_disconnect DistributedPortGroup#port_config_reset_at_disconnect}
        :param port_name_format: A template string to use when creating ports in the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#port_name_format DistributedPortGroup#port_name_format}
        :param port_private_secondary_vlan_id: The secondary VLAN ID for this port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#port_private_secondary_vlan_id DistributedPortGroup#port_private_secondary_vlan_id}
        :param security_policy_override_allowed: Allow security policy settings on a port to override those on the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#security_policy_override_allowed DistributedPortGroup#security_policy_override_allowed}
        :param shaping_override_allowed: Allow the traffic shaping policies of an individual port to override the settings in the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#shaping_override_allowed DistributedPortGroup#shaping_override_allowed}
        :param standby_uplinks: List of standby uplinks used for load balancing, matching the names of the uplinks assigned in the DVS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#standby_uplinks DistributedPortGroup#standby_uplinks}
        :param tags: A list of tag IDs to apply to this object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#tags DistributedPortGroup#tags}
        :param teaming_policy: The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, failover_explicit, or loadbalance_loadbased. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#teaming_policy DistributedPortGroup#teaming_policy}
        :param traffic_filter_override_allowed: Allow any filter policies set on the individual port to override those in the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#traffic_filter_override_allowed DistributedPortGroup#traffic_filter_override_allowed}
        :param tx_uplink: If true, a copy of packets sent to the switch will always be forwarded to an uplink in addition to the regular packet forwarded done by the switch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#tx_uplink DistributedPortGroup#tx_uplink}
        :param type: The type of portgroup. Can be one of earlyBinding (static) or ephemeral. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#type DistributedPortGroup#type}
        :param uplink_teaming_override_allowed: Allow the uplink teaming policies on a port to override those on the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#uplink_teaming_override_allowed DistributedPortGroup#uplink_teaming_override_allowed}
        :param vlan_id: The VLAN ID for single VLAN mode. 0 denotes no VLAN. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#vlan_id DistributedPortGroup#vlan_id}
        :param vlan_override_allowed: Allow the VLAN configuration on a port to override those on the portgroup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#vlan_override_allowed DistributedPortGroup#vlan_override_allowed}
        :param vlan_range: vlan_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#vlan_range DistributedPortGroup#vlan_range}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DistributedPortGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument distributed_virtual_switch_uuid", value=distributed_virtual_switch_uuid, expected_type=type_hints["distributed_virtual_switch_uuid"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument active_uplinks", value=active_uplinks, expected_type=type_hints["active_uplinks"])
            check_type(argname="argument allow_forged_transmits", value=allow_forged_transmits, expected_type=type_hints["allow_forged_transmits"])
            check_type(argname="argument allow_mac_changes", value=allow_mac_changes, expected_type=type_hints["allow_mac_changes"])
            check_type(argname="argument allow_promiscuous", value=allow_promiscuous, expected_type=type_hints["allow_promiscuous"])
            check_type(argname="argument auto_expand", value=auto_expand, expected_type=type_hints["auto_expand"])
            check_type(argname="argument block_all_ports", value=block_all_ports, expected_type=type_hints["block_all_ports"])
            check_type(argname="argument block_override_allowed", value=block_override_allowed, expected_type=type_hints["block_override_allowed"])
            check_type(argname="argument check_beacon", value=check_beacon, expected_type=type_hints["check_beacon"])
            check_type(argname="argument custom_attributes", value=custom_attributes, expected_type=type_hints["custom_attributes"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument directpath_gen2_allowed", value=directpath_gen2_allowed, expected_type=type_hints["directpath_gen2_allowed"])
            check_type(argname="argument egress_shaping_average_bandwidth", value=egress_shaping_average_bandwidth, expected_type=type_hints["egress_shaping_average_bandwidth"])
            check_type(argname="argument egress_shaping_burst_size", value=egress_shaping_burst_size, expected_type=type_hints["egress_shaping_burst_size"])
            check_type(argname="argument egress_shaping_enabled", value=egress_shaping_enabled, expected_type=type_hints["egress_shaping_enabled"])
            check_type(argname="argument egress_shaping_peak_bandwidth", value=egress_shaping_peak_bandwidth, expected_type=type_hints["egress_shaping_peak_bandwidth"])
            check_type(argname="argument failback", value=failback, expected_type=type_hints["failback"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ingress_shaping_average_bandwidth", value=ingress_shaping_average_bandwidth, expected_type=type_hints["ingress_shaping_average_bandwidth"])
            check_type(argname="argument ingress_shaping_burst_size", value=ingress_shaping_burst_size, expected_type=type_hints["ingress_shaping_burst_size"])
            check_type(argname="argument ingress_shaping_enabled", value=ingress_shaping_enabled, expected_type=type_hints["ingress_shaping_enabled"])
            check_type(argname="argument ingress_shaping_peak_bandwidth", value=ingress_shaping_peak_bandwidth, expected_type=type_hints["ingress_shaping_peak_bandwidth"])
            check_type(argname="argument lacp_enabled", value=lacp_enabled, expected_type=type_hints["lacp_enabled"])
            check_type(argname="argument lacp_mode", value=lacp_mode, expected_type=type_hints["lacp_mode"])
            check_type(argname="argument live_port_moving_allowed", value=live_port_moving_allowed, expected_type=type_hints["live_port_moving_allowed"])
            check_type(argname="argument netflow_enabled", value=netflow_enabled, expected_type=type_hints["netflow_enabled"])
            check_type(argname="argument netflow_override_allowed", value=netflow_override_allowed, expected_type=type_hints["netflow_override_allowed"])
            check_type(argname="argument network_resource_pool_key", value=network_resource_pool_key, expected_type=type_hints["network_resource_pool_key"])
            check_type(argname="argument network_resource_pool_override_allowed", value=network_resource_pool_override_allowed, expected_type=type_hints["network_resource_pool_override_allowed"])
            check_type(argname="argument notify_switches", value=notify_switches, expected_type=type_hints["notify_switches"])
            check_type(argname="argument number_of_ports", value=number_of_ports, expected_type=type_hints["number_of_ports"])
            check_type(argname="argument port_config_reset_at_disconnect", value=port_config_reset_at_disconnect, expected_type=type_hints["port_config_reset_at_disconnect"])
            check_type(argname="argument port_name_format", value=port_name_format, expected_type=type_hints["port_name_format"])
            check_type(argname="argument port_private_secondary_vlan_id", value=port_private_secondary_vlan_id, expected_type=type_hints["port_private_secondary_vlan_id"])
            check_type(argname="argument security_policy_override_allowed", value=security_policy_override_allowed, expected_type=type_hints["security_policy_override_allowed"])
            check_type(argname="argument shaping_override_allowed", value=shaping_override_allowed, expected_type=type_hints["shaping_override_allowed"])
            check_type(argname="argument standby_uplinks", value=standby_uplinks, expected_type=type_hints["standby_uplinks"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument teaming_policy", value=teaming_policy, expected_type=type_hints["teaming_policy"])
            check_type(argname="argument traffic_filter_override_allowed", value=traffic_filter_override_allowed, expected_type=type_hints["traffic_filter_override_allowed"])
            check_type(argname="argument tx_uplink", value=tx_uplink, expected_type=type_hints["tx_uplink"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument uplink_teaming_override_allowed", value=uplink_teaming_override_allowed, expected_type=type_hints["uplink_teaming_override_allowed"])
            check_type(argname="argument vlan_id", value=vlan_id, expected_type=type_hints["vlan_id"])
            check_type(argname="argument vlan_override_allowed", value=vlan_override_allowed, expected_type=type_hints["vlan_override_allowed"])
            check_type(argname="argument vlan_range", value=vlan_range, expected_type=type_hints["vlan_range"])
        self._values: typing.Dict[str, typing.Any] = {
            "distributed_virtual_switch_uuid": distributed_virtual_switch_uuid,
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
        if active_uplinks is not None:
            self._values["active_uplinks"] = active_uplinks
        if allow_forged_transmits is not None:
            self._values["allow_forged_transmits"] = allow_forged_transmits
        if allow_mac_changes is not None:
            self._values["allow_mac_changes"] = allow_mac_changes
        if allow_promiscuous is not None:
            self._values["allow_promiscuous"] = allow_promiscuous
        if auto_expand is not None:
            self._values["auto_expand"] = auto_expand
        if block_all_ports is not None:
            self._values["block_all_ports"] = block_all_ports
        if block_override_allowed is not None:
            self._values["block_override_allowed"] = block_override_allowed
        if check_beacon is not None:
            self._values["check_beacon"] = check_beacon
        if custom_attributes is not None:
            self._values["custom_attributes"] = custom_attributes
        if description is not None:
            self._values["description"] = description
        if directpath_gen2_allowed is not None:
            self._values["directpath_gen2_allowed"] = directpath_gen2_allowed
        if egress_shaping_average_bandwidth is not None:
            self._values["egress_shaping_average_bandwidth"] = egress_shaping_average_bandwidth
        if egress_shaping_burst_size is not None:
            self._values["egress_shaping_burst_size"] = egress_shaping_burst_size
        if egress_shaping_enabled is not None:
            self._values["egress_shaping_enabled"] = egress_shaping_enabled
        if egress_shaping_peak_bandwidth is not None:
            self._values["egress_shaping_peak_bandwidth"] = egress_shaping_peak_bandwidth
        if failback is not None:
            self._values["failback"] = failback
        if id is not None:
            self._values["id"] = id
        if ingress_shaping_average_bandwidth is not None:
            self._values["ingress_shaping_average_bandwidth"] = ingress_shaping_average_bandwidth
        if ingress_shaping_burst_size is not None:
            self._values["ingress_shaping_burst_size"] = ingress_shaping_burst_size
        if ingress_shaping_enabled is not None:
            self._values["ingress_shaping_enabled"] = ingress_shaping_enabled
        if ingress_shaping_peak_bandwidth is not None:
            self._values["ingress_shaping_peak_bandwidth"] = ingress_shaping_peak_bandwidth
        if lacp_enabled is not None:
            self._values["lacp_enabled"] = lacp_enabled
        if lacp_mode is not None:
            self._values["lacp_mode"] = lacp_mode
        if live_port_moving_allowed is not None:
            self._values["live_port_moving_allowed"] = live_port_moving_allowed
        if netflow_enabled is not None:
            self._values["netflow_enabled"] = netflow_enabled
        if netflow_override_allowed is not None:
            self._values["netflow_override_allowed"] = netflow_override_allowed
        if network_resource_pool_key is not None:
            self._values["network_resource_pool_key"] = network_resource_pool_key
        if network_resource_pool_override_allowed is not None:
            self._values["network_resource_pool_override_allowed"] = network_resource_pool_override_allowed
        if notify_switches is not None:
            self._values["notify_switches"] = notify_switches
        if number_of_ports is not None:
            self._values["number_of_ports"] = number_of_ports
        if port_config_reset_at_disconnect is not None:
            self._values["port_config_reset_at_disconnect"] = port_config_reset_at_disconnect
        if port_name_format is not None:
            self._values["port_name_format"] = port_name_format
        if port_private_secondary_vlan_id is not None:
            self._values["port_private_secondary_vlan_id"] = port_private_secondary_vlan_id
        if security_policy_override_allowed is not None:
            self._values["security_policy_override_allowed"] = security_policy_override_allowed
        if shaping_override_allowed is not None:
            self._values["shaping_override_allowed"] = shaping_override_allowed
        if standby_uplinks is not None:
            self._values["standby_uplinks"] = standby_uplinks
        if tags is not None:
            self._values["tags"] = tags
        if teaming_policy is not None:
            self._values["teaming_policy"] = teaming_policy
        if traffic_filter_override_allowed is not None:
            self._values["traffic_filter_override_allowed"] = traffic_filter_override_allowed
        if tx_uplink is not None:
            self._values["tx_uplink"] = tx_uplink
        if type is not None:
            self._values["type"] = type
        if uplink_teaming_override_allowed is not None:
            self._values["uplink_teaming_override_allowed"] = uplink_teaming_override_allowed
        if vlan_id is not None:
            self._values["vlan_id"] = vlan_id
        if vlan_override_allowed is not None:
            self._values["vlan_override_allowed"] = vlan_override_allowed
        if vlan_range is not None:
            self._values["vlan_range"] = vlan_range

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
    def distributed_virtual_switch_uuid(self) -> builtins.str:
        '''The UUID of the DVS to attach this port group to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#distributed_virtual_switch_uuid DistributedPortGroup#distributed_virtual_switch_uuid}
        '''
        result = self._values.get("distributed_virtual_switch_uuid")
        assert result is not None, "Required property 'distributed_virtual_switch_uuid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the portgroup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#name DistributedPortGroup#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active_uplinks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of active uplinks used for load balancing, matching the names of the uplinks assigned in the DVS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#active_uplinks DistributedPortGroup#active_uplinks}
        '''
        result = self._values.get("active_uplinks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_forged_transmits(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than that of its own.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#allow_forged_transmits DistributedPortGroup#allow_forged_transmits}
        '''
        result = self._values.get("allow_forged_transmits")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_mac_changes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Controls whether or not the Media Access Control (MAC) address can be changed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#allow_mac_changes DistributedPortGroup#allow_mac_changes}
        '''
        result = self._values.get("allow_mac_changes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_promiscuous(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable promiscuous mode on the network.

        This flag indicates whether or not all traffic is seen on a given port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#allow_promiscuous DistributedPortGroup#allow_promiscuous}
        '''
        result = self._values.get("allow_promiscuous")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auto_expand(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Auto-expands the port group beyond the port count configured in number_of_ports when necessary.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#auto_expand DistributedPortGroup#auto_expand}
        '''
        result = self._values.get("auto_expand")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def block_all_ports(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether to block all ports by default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#block_all_ports DistributedPortGroup#block_all_ports}
        '''
        result = self._values.get("block_all_ports")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def block_override_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow the blocked setting of an individual port to override the setting in the portgroup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#block_override_allowed DistributedPortGroup#block_override_allowed}
        '''
        result = self._values.get("block_override_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def check_beacon(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable beacon probing on the ports this policy applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#check_beacon DistributedPortGroup#check_beacon}
        '''
        result = self._values.get("check_beacon")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def custom_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of custom attributes to set on this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#custom_attributes DistributedPortGroup#custom_attributes}
        '''
        result = self._values.get("custom_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the portgroup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#description DistributedPortGroup#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directpath_gen2_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow VMDirectPath Gen2 on the ports this policy applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#directpath_gen2_allowed DistributedPortGroup#directpath_gen2_allowed}
        '''
        result = self._values.get("directpath_gen2_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def egress_shaping_average_bandwidth(self) -> typing.Optional[jsii.Number]:
        '''The average egress bandwidth in bits per second if egress shaping is enabled on the port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#egress_shaping_average_bandwidth DistributedPortGroup#egress_shaping_average_bandwidth}
        '''
        result = self._values.get("egress_shaping_average_bandwidth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def egress_shaping_burst_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum egress burst size allowed in bytes if egress shaping is enabled on the port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#egress_shaping_burst_size DistributedPortGroup#egress_shaping_burst_size}
        '''
        result = self._values.get("egress_shaping_burst_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def egress_shaping_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''True if the traffic shaper is enabled for egress traffic on the port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#egress_shaping_enabled DistributedPortGroup#egress_shaping_enabled}
        '''
        result = self._values.get("egress_shaping_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def egress_shaping_peak_bandwidth(self) -> typing.Optional[jsii.Number]:
        '''The peak egress bandwidth during bursts in bits per second if egress traffic shaping is enabled on the port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#egress_shaping_peak_bandwidth DistributedPortGroup#egress_shaping_peak_bandwidth}
        '''
        result = self._values.get("egress_shaping_peak_bandwidth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def failback(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#failback DistributedPortGroup#failback}
        '''
        result = self._values.get("failback")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#id DistributedPortGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingress_shaping_average_bandwidth(self) -> typing.Optional[jsii.Number]:
        '''The average ingress bandwidth in bits per second if ingress shaping is enabled on the port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#ingress_shaping_average_bandwidth DistributedPortGroup#ingress_shaping_average_bandwidth}
        '''
        result = self._values.get("ingress_shaping_average_bandwidth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ingress_shaping_burst_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum ingress burst size allowed in bytes if ingress shaping is enabled on the port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#ingress_shaping_burst_size DistributedPortGroup#ingress_shaping_burst_size}
        '''
        result = self._values.get("ingress_shaping_burst_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ingress_shaping_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''True if the traffic shaper is enabled for ingress traffic on the port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#ingress_shaping_enabled DistributedPortGroup#ingress_shaping_enabled}
        '''
        result = self._values.get("ingress_shaping_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ingress_shaping_peak_bandwidth(self) -> typing.Optional[jsii.Number]:
        '''The peak ingress bandwidth during bursts in bits per second if ingress traffic shaping is enabled on the port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#ingress_shaping_peak_bandwidth DistributedPortGroup#ingress_shaping_peak_bandwidth}
        '''
        result = self._values.get("ingress_shaping_peak_bandwidth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def lacp_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not to enable LACP on all uplink ports.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#lacp_enabled DistributedPortGroup#lacp_enabled}
        '''
        result = self._values.get("lacp_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def lacp_mode(self) -> typing.Optional[builtins.str]:
        '''The uplink LACP mode to use. Can be one of active or passive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#lacp_mode DistributedPortGroup#lacp_mode}
        '''
        result = self._values.get("lacp_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def live_port_moving_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow a live port to be moved in and out of the portgroup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#live_port_moving_allowed DistributedPortGroup#live_port_moving_allowed}
        '''
        result = self._values.get("live_port_moving_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def netflow_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether to enable netflow on all ports.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#netflow_enabled DistributedPortGroup#netflow_enabled}
        '''
        result = self._values.get("netflow_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def netflow_override_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow the enabling or disabling of Netflow on a port, contrary to the policy in the portgroup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#netflow_override_allowed DistributedPortGroup#netflow_override_allowed}
        '''
        result = self._values.get("netflow_override_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def network_resource_pool_key(self) -> typing.Optional[builtins.str]:
        '''The key of a network resource pool to associate with this portgroup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#network_resource_pool_key DistributedPortGroup#network_resource_pool_key}
        '''
        result = self._values.get("network_resource_pool_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_resource_pool_override_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow the network resource pool of an individual port to override the setting in the portgroup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#network_resource_pool_override_allowed DistributedPortGroup#network_resource_pool_override_allowed}
        '''
        result = self._values.get("network_resource_pool_override_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def notify_switches(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#notify_switches DistributedPortGroup#notify_switches}
        '''
        result = self._values.get("notify_switches")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def number_of_ports(self) -> typing.Optional[jsii.Number]:
        '''The number of ports in this portgroup. The DVS will expand and shrink by modifying this setting.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#number_of_ports DistributedPortGroup#number_of_ports}
        '''
        result = self._values.get("number_of_ports")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port_config_reset_at_disconnect(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Reset the setting of any ports in this portgroup back to the default setting when the port disconnects.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#port_config_reset_at_disconnect DistributedPortGroup#port_config_reset_at_disconnect}
        '''
        result = self._values.get("port_config_reset_at_disconnect")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def port_name_format(self) -> typing.Optional[builtins.str]:
        '''A template string to use when creating ports in the portgroup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#port_name_format DistributedPortGroup#port_name_format}
        '''
        result = self._values.get("port_name_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port_private_secondary_vlan_id(self) -> typing.Optional[jsii.Number]:
        '''The secondary VLAN ID for this port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#port_private_secondary_vlan_id DistributedPortGroup#port_private_secondary_vlan_id}
        '''
        result = self._values.get("port_private_secondary_vlan_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def security_policy_override_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow security policy settings on a port to override those on the portgroup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#security_policy_override_allowed DistributedPortGroup#security_policy_override_allowed}
        '''
        result = self._values.get("security_policy_override_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def shaping_override_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow the traffic shaping policies of an individual port to override the settings in the portgroup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#shaping_override_allowed DistributedPortGroup#shaping_override_allowed}
        '''
        result = self._values.get("shaping_override_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def standby_uplinks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of standby uplinks used for load balancing, matching the names of the uplinks assigned in the DVS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#standby_uplinks DistributedPortGroup#standby_uplinks}
        '''
        result = self._values.get("standby_uplinks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of tag IDs to apply to this object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#tags DistributedPortGroup#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def teaming_policy(self) -> typing.Optional[builtins.str]:
        '''The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, failover_explicit, or loadbalance_loadbased.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#teaming_policy DistributedPortGroup#teaming_policy}
        '''
        result = self._values.get("teaming_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def traffic_filter_override_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow any filter policies set on the individual port to override those in the portgroup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#traffic_filter_override_allowed DistributedPortGroup#traffic_filter_override_allowed}
        '''
        result = self._values.get("traffic_filter_override_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tx_uplink(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, a copy of packets sent to the switch will always be forwarded to an uplink in addition to the regular packet forwarded done by the switch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#tx_uplink DistributedPortGroup#tx_uplink}
        '''
        result = self._values.get("tx_uplink")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of portgroup. Can be one of earlyBinding (static) or ephemeral.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#type DistributedPortGroup#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uplink_teaming_override_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow the uplink teaming policies on a port to override those on the portgroup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#uplink_teaming_override_allowed DistributedPortGroup#uplink_teaming_override_allowed}
        '''
        result = self._values.get("uplink_teaming_override_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def vlan_id(self) -> typing.Optional[jsii.Number]:
        '''The VLAN ID for single VLAN mode. 0 denotes no VLAN.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#vlan_id DistributedPortGroup#vlan_id}
        '''
        result = self._values.get("vlan_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vlan_override_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow the VLAN configuration on a port to override those on the portgroup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#vlan_override_allowed DistributedPortGroup#vlan_override_allowed}
        '''
        result = self._values.get("vlan_override_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def vlan_range(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DistributedPortGroupVlanRange"]]]:
        '''vlan_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#vlan_range DistributedPortGroup#vlan_range}
        '''
        result = self._values.get("vlan_range")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DistributedPortGroupVlanRange"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DistributedPortGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.distributedPortGroup.DistributedPortGroupVlanRange",
    jsii_struct_bases=[],
    name_mapping={"max_vlan": "maxVlan", "min_vlan": "minVlan"},
)
class DistributedPortGroupVlanRange:
    def __init__(self, *, max_vlan: jsii.Number, min_vlan: jsii.Number) -> None:
        '''
        :param max_vlan: The minimum VLAN to use in the range. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#max_vlan DistributedPortGroup#max_vlan}
        :param min_vlan: The minimum VLAN to use in the range. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#min_vlan DistributedPortGroup#min_vlan}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DistributedPortGroupVlanRange.__init__)
            check_type(argname="argument max_vlan", value=max_vlan, expected_type=type_hints["max_vlan"])
            check_type(argname="argument min_vlan", value=min_vlan, expected_type=type_hints["min_vlan"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_vlan": max_vlan,
            "min_vlan": min_vlan,
        }

    @builtins.property
    def max_vlan(self) -> jsii.Number:
        '''The minimum VLAN to use in the range.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#max_vlan DistributedPortGroup#max_vlan}
        '''
        result = self._values.get("max_vlan")
        assert result is not None, "Required property 'max_vlan' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_vlan(self) -> jsii.Number:
        '''The minimum VLAN to use in the range.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_port_group#min_vlan DistributedPortGroup#min_vlan}
        '''
        result = self._values.get("min_vlan")
        assert result is not None, "Required property 'min_vlan' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DistributedPortGroupVlanRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DistributedPortGroupVlanRangeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.distributedPortGroup.DistributedPortGroupVlanRangeList",
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
            type_hints = typing.get_type_hints(DistributedPortGroupVlanRangeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DistributedPortGroupVlanRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DistributedPortGroupVlanRangeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DistributedPortGroupVlanRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroupVlanRangeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DistributedPortGroupVlanRangeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DistributedPortGroupVlanRangeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DistributedPortGroupVlanRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DistributedPortGroupVlanRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DistributedPortGroupVlanRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroupVlanRangeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DistributedPortGroupVlanRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.distributedPortGroup.DistributedPortGroupVlanRangeOutputReference",
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
            type_hints = typing.get_type_hints(DistributedPortGroupVlanRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="maxVlanInput")
    def max_vlan_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxVlanInput"))

    @builtins.property
    @jsii.member(jsii_name="minVlanInput")
    def min_vlan_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minVlanInput"))

    @builtins.property
    @jsii.member(jsii_name="maxVlan")
    def max_vlan(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxVlan"))

    @max_vlan.setter
    def max_vlan(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroupVlanRangeOutputReference, "max_vlan").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxVlan", value)

    @builtins.property
    @jsii.member(jsii_name="minVlan")
    def min_vlan(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minVlan"))

    @min_vlan.setter
    def min_vlan(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroupVlanRangeOutputReference, "min_vlan").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minVlan", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DistributedPortGroupVlanRange, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DistributedPortGroupVlanRange, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DistributedPortGroupVlanRange, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedPortGroupVlanRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DistributedPortGroup",
    "DistributedPortGroupConfig",
    "DistributedPortGroupVlanRange",
    "DistributedPortGroupVlanRangeList",
    "DistributedPortGroupVlanRangeOutputReference",
]

publication.publish()
