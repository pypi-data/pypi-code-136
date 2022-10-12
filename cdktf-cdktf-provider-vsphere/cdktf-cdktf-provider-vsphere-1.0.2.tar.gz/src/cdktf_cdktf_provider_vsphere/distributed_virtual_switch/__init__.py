'''
# `vsphere_distributed_virtual_switch`

Refer to the Terraform Registory for docs: [`vsphere_distributed_virtual_switch`](https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch).
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


class DistributedVirtualSwitch(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.distributedVirtualSwitch.DistributedVirtualSwitch",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch vsphere_distributed_virtual_switch}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        datacenter_id: builtins.str,
        name: builtins.str,
        active_uplinks: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_forged_transmits: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_mac_changes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_promiscuous: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        backupnfc_maximum_mbit: typing.Optional[jsii.Number] = None,
        backupnfc_reservation_mbit: typing.Optional[jsii.Number] = None,
        backupnfc_share_count: typing.Optional[jsii.Number] = None,
        backupnfc_share_level: typing.Optional[builtins.str] = None,
        block_all_ports: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        check_beacon: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        contact_detail: typing.Optional[builtins.str] = None,
        contact_name: typing.Optional[builtins.str] = None,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        directpath_gen2_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        egress_shaping_average_bandwidth: typing.Optional[jsii.Number] = None,
        egress_shaping_burst_size: typing.Optional[jsii.Number] = None,
        egress_shaping_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        egress_shaping_peak_bandwidth: typing.Optional[jsii.Number] = None,
        failback: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        faulttolerance_maximum_mbit: typing.Optional[jsii.Number] = None,
        faulttolerance_reservation_mbit: typing.Optional[jsii.Number] = None,
        faulttolerance_share_count: typing.Optional[jsii.Number] = None,
        faulttolerance_share_level: typing.Optional[builtins.str] = None,
        folder: typing.Optional[builtins.str] = None,
        hbr_maximum_mbit: typing.Optional[jsii.Number] = None,
        hbr_reservation_mbit: typing.Optional[jsii.Number] = None,
        hbr_share_count: typing.Optional[jsii.Number] = None,
        hbr_share_level: typing.Optional[builtins.str] = None,
        host: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DistributedVirtualSwitchHost", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        ignore_other_pvlan_mappings: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ingress_shaping_average_bandwidth: typing.Optional[jsii.Number] = None,
        ingress_shaping_burst_size: typing.Optional[jsii.Number] = None,
        ingress_shaping_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ingress_shaping_peak_bandwidth: typing.Optional[jsii.Number] = None,
        ipv4_address: typing.Optional[builtins.str] = None,
        iscsi_maximum_mbit: typing.Optional[jsii.Number] = None,
        iscsi_reservation_mbit: typing.Optional[jsii.Number] = None,
        iscsi_share_count: typing.Optional[jsii.Number] = None,
        iscsi_share_level: typing.Optional[builtins.str] = None,
        lacp_api_version: typing.Optional[builtins.str] = None,
        lacp_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        lacp_mode: typing.Optional[builtins.str] = None,
        link_discovery_operation: typing.Optional[builtins.str] = None,
        link_discovery_protocol: typing.Optional[builtins.str] = None,
        management_maximum_mbit: typing.Optional[jsii.Number] = None,
        management_reservation_mbit: typing.Optional[jsii.Number] = None,
        management_share_count: typing.Optional[jsii.Number] = None,
        management_share_level: typing.Optional[builtins.str] = None,
        max_mtu: typing.Optional[jsii.Number] = None,
        multicast_filtering_mode: typing.Optional[builtins.str] = None,
        netflow_active_flow_timeout: typing.Optional[jsii.Number] = None,
        netflow_collector_ip_address: typing.Optional[builtins.str] = None,
        netflow_collector_port: typing.Optional[jsii.Number] = None,
        netflow_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        netflow_idle_flow_timeout: typing.Optional[jsii.Number] = None,
        netflow_internal_flows_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        netflow_observation_domain_id: typing.Optional[jsii.Number] = None,
        netflow_sampling_rate: typing.Optional[jsii.Number] = None,
        network_resource_control_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        network_resource_control_version: typing.Optional[builtins.str] = None,
        nfs_maximum_mbit: typing.Optional[jsii.Number] = None,
        nfs_reservation_mbit: typing.Optional[jsii.Number] = None,
        nfs_share_count: typing.Optional[jsii.Number] = None,
        nfs_share_level: typing.Optional[builtins.str] = None,
        notify_switches: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        port_private_secondary_vlan_id: typing.Optional[jsii.Number] = None,
        pvlan_mapping: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DistributedVirtualSwitchPvlanMapping", typing.Dict[str, typing.Any]]]]] = None,
        standby_uplinks: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        teaming_policy: typing.Optional[builtins.str] = None,
        tx_uplink: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        uplinks: typing.Optional[typing.Sequence[builtins.str]] = None,
        vdp_maximum_mbit: typing.Optional[jsii.Number] = None,
        vdp_reservation_mbit: typing.Optional[jsii.Number] = None,
        vdp_share_count: typing.Optional[jsii.Number] = None,
        vdp_share_level: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
        virtualmachine_maximum_mbit: typing.Optional[jsii.Number] = None,
        virtualmachine_reservation_mbit: typing.Optional[jsii.Number] = None,
        virtualmachine_share_count: typing.Optional[jsii.Number] = None,
        virtualmachine_share_level: typing.Optional[builtins.str] = None,
        vlan_id: typing.Optional[jsii.Number] = None,
        vlan_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DistributedVirtualSwitchVlanRange", typing.Dict[str, typing.Any]]]]] = None,
        vmotion_maximum_mbit: typing.Optional[jsii.Number] = None,
        vmotion_reservation_mbit: typing.Optional[jsii.Number] = None,
        vmotion_share_count: typing.Optional[jsii.Number] = None,
        vmotion_share_level: typing.Optional[builtins.str] = None,
        vsan_maximum_mbit: typing.Optional[jsii.Number] = None,
        vsan_reservation_mbit: typing.Optional[jsii.Number] = None,
        vsan_share_count: typing.Optional[jsii.Number] = None,
        vsan_share_level: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch vsphere_distributed_virtual_switch} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param datacenter_id: The ID of the datacenter to create this virtual switch in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#datacenter_id DistributedVirtualSwitch#datacenter_id}
        :param name: The name for the DVS. Must be unique in the folder that it is being created in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#name DistributedVirtualSwitch#name}
        :param active_uplinks: List of active uplinks used for load balancing, matching the names of the uplinks assigned in the DVS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#active_uplinks DistributedVirtualSwitch#active_uplinks}
        :param allow_forged_transmits: Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than that of its own. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#allow_forged_transmits DistributedVirtualSwitch#allow_forged_transmits}
        :param allow_mac_changes: Controls whether or not the Media Access Control (MAC) address can be changed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#allow_mac_changes DistributedVirtualSwitch#allow_mac_changes}
        :param allow_promiscuous: Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#allow_promiscuous DistributedVirtualSwitch#allow_promiscuous}
        :param backupnfc_maximum_mbit: The maximum allowed usage for the backupNfc traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#backupnfc_maximum_mbit DistributedVirtualSwitch#backupnfc_maximum_mbit}
        :param backupnfc_reservation_mbit: The amount of guaranteed bandwidth for the backupNfc traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#backupnfc_reservation_mbit DistributedVirtualSwitch#backupnfc_reservation_mbit}
        :param backupnfc_share_count: The amount of shares to allocate to the backupNfc traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#backupnfc_share_count DistributedVirtualSwitch#backupnfc_share_count}
        :param backupnfc_share_level: The allocation level for the backupNfc traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#backupnfc_share_level DistributedVirtualSwitch#backupnfc_share_level}
        :param block_all_ports: Indicates whether to block all ports by default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#block_all_ports DistributedVirtualSwitch#block_all_ports}
        :param check_beacon: Enable beacon probing on the ports this policy applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#check_beacon DistributedVirtualSwitch#check_beacon}
        :param contact_detail: The contact detail for this DVS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#contact_detail DistributedVirtualSwitch#contact_detail}
        :param contact_name: The contact name for this DVS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#contact_name DistributedVirtualSwitch#contact_name}
        :param custom_attributes: A list of custom attributes to set on this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#custom_attributes DistributedVirtualSwitch#custom_attributes}
        :param description: The description of the DVS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#description DistributedVirtualSwitch#description}
        :param directpath_gen2_allowed: Allow VMDirectPath Gen2 on the ports this policy applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#directpath_gen2_allowed DistributedVirtualSwitch#directpath_gen2_allowed}
        :param egress_shaping_average_bandwidth: The average egress bandwidth in bits per second if egress shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#egress_shaping_average_bandwidth DistributedVirtualSwitch#egress_shaping_average_bandwidth}
        :param egress_shaping_burst_size: The maximum egress burst size allowed in bytes if egress shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#egress_shaping_burst_size DistributedVirtualSwitch#egress_shaping_burst_size}
        :param egress_shaping_enabled: True if the traffic shaper is enabled for egress traffic on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#egress_shaping_enabled DistributedVirtualSwitch#egress_shaping_enabled}
        :param egress_shaping_peak_bandwidth: The peak egress bandwidth during bursts in bits per second if egress traffic shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#egress_shaping_peak_bandwidth DistributedVirtualSwitch#egress_shaping_peak_bandwidth}
        :param failback: If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#failback DistributedVirtualSwitch#failback}
        :param faulttolerance_maximum_mbit: The maximum allowed usage for the faultTolerance traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#faulttolerance_maximum_mbit DistributedVirtualSwitch#faulttolerance_maximum_mbit}
        :param faulttolerance_reservation_mbit: The amount of guaranteed bandwidth for the faultTolerance traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#faulttolerance_reservation_mbit DistributedVirtualSwitch#faulttolerance_reservation_mbit}
        :param faulttolerance_share_count: The amount of shares to allocate to the faultTolerance traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#faulttolerance_share_count DistributedVirtualSwitch#faulttolerance_share_count}
        :param faulttolerance_share_level: The allocation level for the faultTolerance traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#faulttolerance_share_level DistributedVirtualSwitch#faulttolerance_share_level}
        :param folder: The folder to create this virtual switch in, relative to the datacenter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#folder DistributedVirtualSwitch#folder}
        :param hbr_maximum_mbit: The maximum allowed usage for the hbr traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#hbr_maximum_mbit DistributedVirtualSwitch#hbr_maximum_mbit}
        :param hbr_reservation_mbit: The amount of guaranteed bandwidth for the hbr traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#hbr_reservation_mbit DistributedVirtualSwitch#hbr_reservation_mbit}
        :param hbr_share_count: The amount of shares to allocate to the hbr traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#hbr_share_count DistributedVirtualSwitch#hbr_share_count}
        :param hbr_share_level: The allocation level for the hbr traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#hbr_share_level DistributedVirtualSwitch#hbr_share_level}
        :param host: host block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#host DistributedVirtualSwitch#host}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#id DistributedVirtualSwitch#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignore_other_pvlan_mappings: Whether to ignore existing PVLAN mappings not managed by this resource. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#ignore_other_pvlan_mappings DistributedVirtualSwitch#ignore_other_pvlan_mappings}
        :param ingress_shaping_average_bandwidth: The average ingress bandwidth in bits per second if ingress shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#ingress_shaping_average_bandwidth DistributedVirtualSwitch#ingress_shaping_average_bandwidth}
        :param ingress_shaping_burst_size: The maximum ingress burst size allowed in bytes if ingress shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#ingress_shaping_burst_size DistributedVirtualSwitch#ingress_shaping_burst_size}
        :param ingress_shaping_enabled: True if the traffic shaper is enabled for ingress traffic on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#ingress_shaping_enabled DistributedVirtualSwitch#ingress_shaping_enabled}
        :param ingress_shaping_peak_bandwidth: The peak ingress bandwidth during bursts in bits per second if ingress traffic shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#ingress_shaping_peak_bandwidth DistributedVirtualSwitch#ingress_shaping_peak_bandwidth}
        :param ipv4_address: The IPv4 address of the switch. This can be used to see the DVS as a unique device with NetFlow. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#ipv4_address DistributedVirtualSwitch#ipv4_address}
        :param iscsi_maximum_mbit: The maximum allowed usage for the iSCSI traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#iscsi_maximum_mbit DistributedVirtualSwitch#iscsi_maximum_mbit}
        :param iscsi_reservation_mbit: The amount of guaranteed bandwidth for the iSCSI traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#iscsi_reservation_mbit DistributedVirtualSwitch#iscsi_reservation_mbit}
        :param iscsi_share_count: The amount of shares to allocate to the iSCSI traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#iscsi_share_count DistributedVirtualSwitch#iscsi_share_count}
        :param iscsi_share_level: The allocation level for the iSCSI traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#iscsi_share_level DistributedVirtualSwitch#iscsi_share_level}
        :param lacp_api_version: The Link Aggregation Control Protocol group version in the switch. Can be one of singleLag or multipleLag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#lacp_api_version DistributedVirtualSwitch#lacp_api_version}
        :param lacp_enabled: Whether or not to enable LACP on all uplink ports. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#lacp_enabled DistributedVirtualSwitch#lacp_enabled}
        :param lacp_mode: The uplink LACP mode to use. Can be one of active or passive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#lacp_mode DistributedVirtualSwitch#lacp_mode}
        :param link_discovery_operation: Whether to advertise or listen for link discovery. Valid values are advertise, both, listen, and none. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#link_discovery_operation DistributedVirtualSwitch#link_discovery_operation}
        :param link_discovery_protocol: The discovery protocol type. Valid values are cdp and lldp. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#link_discovery_protocol DistributedVirtualSwitch#link_discovery_protocol}
        :param management_maximum_mbit: The maximum allowed usage for the management traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#management_maximum_mbit DistributedVirtualSwitch#management_maximum_mbit}
        :param management_reservation_mbit: The amount of guaranteed bandwidth for the management traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#management_reservation_mbit DistributedVirtualSwitch#management_reservation_mbit}
        :param management_share_count: The amount of shares to allocate to the management traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#management_share_count DistributedVirtualSwitch#management_share_count}
        :param management_share_level: The allocation level for the management traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#management_share_level DistributedVirtualSwitch#management_share_level}
        :param max_mtu: The maximum MTU on the switch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#max_mtu DistributedVirtualSwitch#max_mtu}
        :param multicast_filtering_mode: The multicast filtering mode on the switch. Can be one of legacyFiltering, or snooping. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#multicast_filtering_mode DistributedVirtualSwitch#multicast_filtering_mode}
        :param netflow_active_flow_timeout: The number of seconds after which active flows are forced to be exported to the collector. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_active_flow_timeout DistributedVirtualSwitch#netflow_active_flow_timeout}
        :param netflow_collector_ip_address: IP address for the netflow collector, using IPv4 or IPv6. IPv6 is supported in vSphere Distributed Switch Version 6.0 or later. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_collector_ip_address DistributedVirtualSwitch#netflow_collector_ip_address}
        :param netflow_collector_port: The port for the netflow collector. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_collector_port DistributedVirtualSwitch#netflow_collector_port}
        :param netflow_enabled: Indicates whether to enable netflow on all ports. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_enabled DistributedVirtualSwitch#netflow_enabled}
        :param netflow_idle_flow_timeout: The number of seconds after which idle flows are forced to be exported to the collector. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_idle_flow_timeout DistributedVirtualSwitch#netflow_idle_flow_timeout}
        :param netflow_internal_flows_only: Whether to limit analysis to traffic that has both source and destination served by the same host. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_internal_flows_only DistributedVirtualSwitch#netflow_internal_flows_only}
        :param netflow_observation_domain_id: The observation Domain ID for the netflow collector. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_observation_domain_id DistributedVirtualSwitch#netflow_observation_domain_id}
        :param netflow_sampling_rate: The ratio of total number of packets to the number of packets analyzed. Set to 0 to disable sampling, meaning that all packets are analyzed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_sampling_rate DistributedVirtualSwitch#netflow_sampling_rate}
        :param network_resource_control_enabled: Whether or not to enable network resource control, enabling advanced traffic shaping and resource control features. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#network_resource_control_enabled DistributedVirtualSwitch#network_resource_control_enabled}
        :param network_resource_control_version: The network I/O control version to use. Can be one of version2 or version3. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#network_resource_control_version DistributedVirtualSwitch#network_resource_control_version}
        :param nfs_maximum_mbit: The maximum allowed usage for the nfs traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#nfs_maximum_mbit DistributedVirtualSwitch#nfs_maximum_mbit}
        :param nfs_reservation_mbit: The amount of guaranteed bandwidth for the nfs traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#nfs_reservation_mbit DistributedVirtualSwitch#nfs_reservation_mbit}
        :param nfs_share_count: The amount of shares to allocate to the nfs traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#nfs_share_count DistributedVirtualSwitch#nfs_share_count}
        :param nfs_share_level: The allocation level for the nfs traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#nfs_share_level DistributedVirtualSwitch#nfs_share_level}
        :param notify_switches: If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#notify_switches DistributedVirtualSwitch#notify_switches}
        :param port_private_secondary_vlan_id: The secondary VLAN ID for this port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#port_private_secondary_vlan_id DistributedVirtualSwitch#port_private_secondary_vlan_id}
        :param pvlan_mapping: pvlan_mapping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#pvlan_mapping DistributedVirtualSwitch#pvlan_mapping}
        :param standby_uplinks: List of standby uplinks used for load balancing, matching the names of the uplinks assigned in the DVS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#standby_uplinks DistributedVirtualSwitch#standby_uplinks}
        :param tags: A list of tag IDs to apply to this object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#tags DistributedVirtualSwitch#tags}
        :param teaming_policy: The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, failover_explicit, or loadbalance_loadbased. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#teaming_policy DistributedVirtualSwitch#teaming_policy}
        :param tx_uplink: If true, a copy of packets sent to the switch will always be forwarded to an uplink in addition to the regular packet forwarded done by the switch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#tx_uplink DistributedVirtualSwitch#tx_uplink}
        :param uplinks: A list of uplink ports. The contents of this list control both the uplink count and names of the uplinks on the DVS across hosts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#uplinks DistributedVirtualSwitch#uplinks}
        :param vdp_maximum_mbit: The maximum allowed usage for the vdp traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vdp_maximum_mbit DistributedVirtualSwitch#vdp_maximum_mbit}
        :param vdp_reservation_mbit: The amount of guaranteed bandwidth for the vdp traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vdp_reservation_mbit DistributedVirtualSwitch#vdp_reservation_mbit}
        :param vdp_share_count: The amount of shares to allocate to the vdp traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vdp_share_count DistributedVirtualSwitch#vdp_share_count}
        :param vdp_share_level: The allocation level for the vdp traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vdp_share_level DistributedVirtualSwitch#vdp_share_level}
        :param version: The version of this virtual switch. Allowed versions are 7.0.3, 7.0.0, 6.6.0, 6.5.0, 6.0.0, 5.5.0, 5.1.0, and 5.0.0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#version DistributedVirtualSwitch#version}
        :param virtualmachine_maximum_mbit: The maximum allowed usage for the virtualMachine traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#virtualmachine_maximum_mbit DistributedVirtualSwitch#virtualmachine_maximum_mbit}
        :param virtualmachine_reservation_mbit: The amount of guaranteed bandwidth for the virtualMachine traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#virtualmachine_reservation_mbit DistributedVirtualSwitch#virtualmachine_reservation_mbit}
        :param virtualmachine_share_count: The amount of shares to allocate to the virtualMachine traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#virtualmachine_share_count DistributedVirtualSwitch#virtualmachine_share_count}
        :param virtualmachine_share_level: The allocation level for the virtualMachine traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#virtualmachine_share_level DistributedVirtualSwitch#virtualmachine_share_level}
        :param vlan_id: The VLAN ID for single VLAN mode. 0 denotes no VLAN. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vlan_id DistributedVirtualSwitch#vlan_id}
        :param vlan_range: vlan_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vlan_range DistributedVirtualSwitch#vlan_range}
        :param vmotion_maximum_mbit: The maximum allowed usage for the vmotion traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vmotion_maximum_mbit DistributedVirtualSwitch#vmotion_maximum_mbit}
        :param vmotion_reservation_mbit: The amount of guaranteed bandwidth for the vmotion traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vmotion_reservation_mbit DistributedVirtualSwitch#vmotion_reservation_mbit}
        :param vmotion_share_count: The amount of shares to allocate to the vmotion traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vmotion_share_count DistributedVirtualSwitch#vmotion_share_count}
        :param vmotion_share_level: The allocation level for the vmotion traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vmotion_share_level DistributedVirtualSwitch#vmotion_share_level}
        :param vsan_maximum_mbit: The maximum allowed usage for the vsan traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vsan_maximum_mbit DistributedVirtualSwitch#vsan_maximum_mbit}
        :param vsan_reservation_mbit: The amount of guaranteed bandwidth for the vsan traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vsan_reservation_mbit DistributedVirtualSwitch#vsan_reservation_mbit}
        :param vsan_share_count: The amount of shares to allocate to the vsan traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vsan_share_count DistributedVirtualSwitch#vsan_share_count}
        :param vsan_share_level: The allocation level for the vsan traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vsan_share_level DistributedVirtualSwitch#vsan_share_level}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DistributedVirtualSwitch.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DistributedVirtualSwitchConfig(
            datacenter_id=datacenter_id,
            name=name,
            active_uplinks=active_uplinks,
            allow_forged_transmits=allow_forged_transmits,
            allow_mac_changes=allow_mac_changes,
            allow_promiscuous=allow_promiscuous,
            backupnfc_maximum_mbit=backupnfc_maximum_mbit,
            backupnfc_reservation_mbit=backupnfc_reservation_mbit,
            backupnfc_share_count=backupnfc_share_count,
            backupnfc_share_level=backupnfc_share_level,
            block_all_ports=block_all_ports,
            check_beacon=check_beacon,
            contact_detail=contact_detail,
            contact_name=contact_name,
            custom_attributes=custom_attributes,
            description=description,
            directpath_gen2_allowed=directpath_gen2_allowed,
            egress_shaping_average_bandwidth=egress_shaping_average_bandwidth,
            egress_shaping_burst_size=egress_shaping_burst_size,
            egress_shaping_enabled=egress_shaping_enabled,
            egress_shaping_peak_bandwidth=egress_shaping_peak_bandwidth,
            failback=failback,
            faulttolerance_maximum_mbit=faulttolerance_maximum_mbit,
            faulttolerance_reservation_mbit=faulttolerance_reservation_mbit,
            faulttolerance_share_count=faulttolerance_share_count,
            faulttolerance_share_level=faulttolerance_share_level,
            folder=folder,
            hbr_maximum_mbit=hbr_maximum_mbit,
            hbr_reservation_mbit=hbr_reservation_mbit,
            hbr_share_count=hbr_share_count,
            hbr_share_level=hbr_share_level,
            host=host,
            id=id,
            ignore_other_pvlan_mappings=ignore_other_pvlan_mappings,
            ingress_shaping_average_bandwidth=ingress_shaping_average_bandwidth,
            ingress_shaping_burst_size=ingress_shaping_burst_size,
            ingress_shaping_enabled=ingress_shaping_enabled,
            ingress_shaping_peak_bandwidth=ingress_shaping_peak_bandwidth,
            ipv4_address=ipv4_address,
            iscsi_maximum_mbit=iscsi_maximum_mbit,
            iscsi_reservation_mbit=iscsi_reservation_mbit,
            iscsi_share_count=iscsi_share_count,
            iscsi_share_level=iscsi_share_level,
            lacp_api_version=lacp_api_version,
            lacp_enabled=lacp_enabled,
            lacp_mode=lacp_mode,
            link_discovery_operation=link_discovery_operation,
            link_discovery_protocol=link_discovery_protocol,
            management_maximum_mbit=management_maximum_mbit,
            management_reservation_mbit=management_reservation_mbit,
            management_share_count=management_share_count,
            management_share_level=management_share_level,
            max_mtu=max_mtu,
            multicast_filtering_mode=multicast_filtering_mode,
            netflow_active_flow_timeout=netflow_active_flow_timeout,
            netflow_collector_ip_address=netflow_collector_ip_address,
            netflow_collector_port=netflow_collector_port,
            netflow_enabled=netflow_enabled,
            netflow_idle_flow_timeout=netflow_idle_flow_timeout,
            netflow_internal_flows_only=netflow_internal_flows_only,
            netflow_observation_domain_id=netflow_observation_domain_id,
            netflow_sampling_rate=netflow_sampling_rate,
            network_resource_control_enabled=network_resource_control_enabled,
            network_resource_control_version=network_resource_control_version,
            nfs_maximum_mbit=nfs_maximum_mbit,
            nfs_reservation_mbit=nfs_reservation_mbit,
            nfs_share_count=nfs_share_count,
            nfs_share_level=nfs_share_level,
            notify_switches=notify_switches,
            port_private_secondary_vlan_id=port_private_secondary_vlan_id,
            pvlan_mapping=pvlan_mapping,
            standby_uplinks=standby_uplinks,
            tags=tags,
            teaming_policy=teaming_policy,
            tx_uplink=tx_uplink,
            uplinks=uplinks,
            vdp_maximum_mbit=vdp_maximum_mbit,
            vdp_reservation_mbit=vdp_reservation_mbit,
            vdp_share_count=vdp_share_count,
            vdp_share_level=vdp_share_level,
            version=version,
            virtualmachine_maximum_mbit=virtualmachine_maximum_mbit,
            virtualmachine_reservation_mbit=virtualmachine_reservation_mbit,
            virtualmachine_share_count=virtualmachine_share_count,
            virtualmachine_share_level=virtualmachine_share_level,
            vlan_id=vlan_id,
            vlan_range=vlan_range,
            vmotion_maximum_mbit=vmotion_maximum_mbit,
            vmotion_reservation_mbit=vmotion_reservation_mbit,
            vmotion_share_count=vmotion_share_count,
            vmotion_share_level=vmotion_share_level,
            vsan_maximum_mbit=vsan_maximum_mbit,
            vsan_reservation_mbit=vsan_reservation_mbit,
            vsan_share_count=vsan_share_count,
            vsan_share_level=vsan_share_level,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putHost")
    def put_host(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DistributedVirtualSwitchHost", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DistributedVirtualSwitch.put_host)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHost", [value]))

    @jsii.member(jsii_name="putPvlanMapping")
    def put_pvlan_mapping(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DistributedVirtualSwitchPvlanMapping", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DistributedVirtualSwitch.put_pvlan_mapping)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPvlanMapping", [value]))

    @jsii.member(jsii_name="putVlanRange")
    def put_vlan_range(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DistributedVirtualSwitchVlanRange", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DistributedVirtualSwitch.put_vlan_range)
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

    @jsii.member(jsii_name="resetBackupnfcMaximumMbit")
    def reset_backupnfc_maximum_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupnfcMaximumMbit", []))

    @jsii.member(jsii_name="resetBackupnfcReservationMbit")
    def reset_backupnfc_reservation_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupnfcReservationMbit", []))

    @jsii.member(jsii_name="resetBackupnfcShareCount")
    def reset_backupnfc_share_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupnfcShareCount", []))

    @jsii.member(jsii_name="resetBackupnfcShareLevel")
    def reset_backupnfc_share_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupnfcShareLevel", []))

    @jsii.member(jsii_name="resetBlockAllPorts")
    def reset_block_all_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockAllPorts", []))

    @jsii.member(jsii_name="resetCheckBeacon")
    def reset_check_beacon(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckBeacon", []))

    @jsii.member(jsii_name="resetContactDetail")
    def reset_contact_detail(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContactDetail", []))

    @jsii.member(jsii_name="resetContactName")
    def reset_contact_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContactName", []))

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

    @jsii.member(jsii_name="resetFaulttoleranceMaximumMbit")
    def reset_faulttolerance_maximum_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFaulttoleranceMaximumMbit", []))

    @jsii.member(jsii_name="resetFaulttoleranceReservationMbit")
    def reset_faulttolerance_reservation_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFaulttoleranceReservationMbit", []))

    @jsii.member(jsii_name="resetFaulttoleranceShareCount")
    def reset_faulttolerance_share_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFaulttoleranceShareCount", []))

    @jsii.member(jsii_name="resetFaulttoleranceShareLevel")
    def reset_faulttolerance_share_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFaulttoleranceShareLevel", []))

    @jsii.member(jsii_name="resetFolder")
    def reset_folder(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFolder", []))

    @jsii.member(jsii_name="resetHbrMaximumMbit")
    def reset_hbr_maximum_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHbrMaximumMbit", []))

    @jsii.member(jsii_name="resetHbrReservationMbit")
    def reset_hbr_reservation_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHbrReservationMbit", []))

    @jsii.member(jsii_name="resetHbrShareCount")
    def reset_hbr_share_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHbrShareCount", []))

    @jsii.member(jsii_name="resetHbrShareLevel")
    def reset_hbr_share_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHbrShareLevel", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIgnoreOtherPvlanMappings")
    def reset_ignore_other_pvlan_mappings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreOtherPvlanMappings", []))

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

    @jsii.member(jsii_name="resetIpv4Address")
    def reset_ipv4_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv4Address", []))

    @jsii.member(jsii_name="resetIscsiMaximumMbit")
    def reset_iscsi_maximum_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIscsiMaximumMbit", []))

    @jsii.member(jsii_name="resetIscsiReservationMbit")
    def reset_iscsi_reservation_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIscsiReservationMbit", []))

    @jsii.member(jsii_name="resetIscsiShareCount")
    def reset_iscsi_share_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIscsiShareCount", []))

    @jsii.member(jsii_name="resetIscsiShareLevel")
    def reset_iscsi_share_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIscsiShareLevel", []))

    @jsii.member(jsii_name="resetLacpApiVersion")
    def reset_lacp_api_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLacpApiVersion", []))

    @jsii.member(jsii_name="resetLacpEnabled")
    def reset_lacp_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLacpEnabled", []))

    @jsii.member(jsii_name="resetLacpMode")
    def reset_lacp_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLacpMode", []))

    @jsii.member(jsii_name="resetLinkDiscoveryOperation")
    def reset_link_discovery_operation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkDiscoveryOperation", []))

    @jsii.member(jsii_name="resetLinkDiscoveryProtocol")
    def reset_link_discovery_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkDiscoveryProtocol", []))

    @jsii.member(jsii_name="resetManagementMaximumMbit")
    def reset_management_maximum_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagementMaximumMbit", []))

    @jsii.member(jsii_name="resetManagementReservationMbit")
    def reset_management_reservation_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagementReservationMbit", []))

    @jsii.member(jsii_name="resetManagementShareCount")
    def reset_management_share_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagementShareCount", []))

    @jsii.member(jsii_name="resetManagementShareLevel")
    def reset_management_share_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagementShareLevel", []))

    @jsii.member(jsii_name="resetMaxMtu")
    def reset_max_mtu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxMtu", []))

    @jsii.member(jsii_name="resetMulticastFilteringMode")
    def reset_multicast_filtering_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMulticastFilteringMode", []))

    @jsii.member(jsii_name="resetNetflowActiveFlowTimeout")
    def reset_netflow_active_flow_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetflowActiveFlowTimeout", []))

    @jsii.member(jsii_name="resetNetflowCollectorIpAddress")
    def reset_netflow_collector_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetflowCollectorIpAddress", []))

    @jsii.member(jsii_name="resetNetflowCollectorPort")
    def reset_netflow_collector_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetflowCollectorPort", []))

    @jsii.member(jsii_name="resetNetflowEnabled")
    def reset_netflow_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetflowEnabled", []))

    @jsii.member(jsii_name="resetNetflowIdleFlowTimeout")
    def reset_netflow_idle_flow_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetflowIdleFlowTimeout", []))

    @jsii.member(jsii_name="resetNetflowInternalFlowsOnly")
    def reset_netflow_internal_flows_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetflowInternalFlowsOnly", []))

    @jsii.member(jsii_name="resetNetflowObservationDomainId")
    def reset_netflow_observation_domain_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetflowObservationDomainId", []))

    @jsii.member(jsii_name="resetNetflowSamplingRate")
    def reset_netflow_sampling_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetflowSamplingRate", []))

    @jsii.member(jsii_name="resetNetworkResourceControlEnabled")
    def reset_network_resource_control_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkResourceControlEnabled", []))

    @jsii.member(jsii_name="resetNetworkResourceControlVersion")
    def reset_network_resource_control_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkResourceControlVersion", []))

    @jsii.member(jsii_name="resetNfsMaximumMbit")
    def reset_nfs_maximum_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNfsMaximumMbit", []))

    @jsii.member(jsii_name="resetNfsReservationMbit")
    def reset_nfs_reservation_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNfsReservationMbit", []))

    @jsii.member(jsii_name="resetNfsShareCount")
    def reset_nfs_share_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNfsShareCount", []))

    @jsii.member(jsii_name="resetNfsShareLevel")
    def reset_nfs_share_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNfsShareLevel", []))

    @jsii.member(jsii_name="resetNotifySwitches")
    def reset_notify_switches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotifySwitches", []))

    @jsii.member(jsii_name="resetPortPrivateSecondaryVlanId")
    def reset_port_private_secondary_vlan_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortPrivateSecondaryVlanId", []))

    @jsii.member(jsii_name="resetPvlanMapping")
    def reset_pvlan_mapping(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPvlanMapping", []))

    @jsii.member(jsii_name="resetStandbyUplinks")
    def reset_standby_uplinks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStandbyUplinks", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTeamingPolicy")
    def reset_teaming_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeamingPolicy", []))

    @jsii.member(jsii_name="resetTxUplink")
    def reset_tx_uplink(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTxUplink", []))

    @jsii.member(jsii_name="resetUplinks")
    def reset_uplinks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUplinks", []))

    @jsii.member(jsii_name="resetVdpMaximumMbit")
    def reset_vdp_maximum_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVdpMaximumMbit", []))

    @jsii.member(jsii_name="resetVdpReservationMbit")
    def reset_vdp_reservation_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVdpReservationMbit", []))

    @jsii.member(jsii_name="resetVdpShareCount")
    def reset_vdp_share_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVdpShareCount", []))

    @jsii.member(jsii_name="resetVdpShareLevel")
    def reset_vdp_share_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVdpShareLevel", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @jsii.member(jsii_name="resetVirtualmachineMaximumMbit")
    def reset_virtualmachine_maximum_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualmachineMaximumMbit", []))

    @jsii.member(jsii_name="resetVirtualmachineReservationMbit")
    def reset_virtualmachine_reservation_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualmachineReservationMbit", []))

    @jsii.member(jsii_name="resetVirtualmachineShareCount")
    def reset_virtualmachine_share_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualmachineShareCount", []))

    @jsii.member(jsii_name="resetVirtualmachineShareLevel")
    def reset_virtualmachine_share_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualmachineShareLevel", []))

    @jsii.member(jsii_name="resetVlanId")
    def reset_vlan_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVlanId", []))

    @jsii.member(jsii_name="resetVlanRange")
    def reset_vlan_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVlanRange", []))

    @jsii.member(jsii_name="resetVmotionMaximumMbit")
    def reset_vmotion_maximum_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVmotionMaximumMbit", []))

    @jsii.member(jsii_name="resetVmotionReservationMbit")
    def reset_vmotion_reservation_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVmotionReservationMbit", []))

    @jsii.member(jsii_name="resetVmotionShareCount")
    def reset_vmotion_share_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVmotionShareCount", []))

    @jsii.member(jsii_name="resetVmotionShareLevel")
    def reset_vmotion_share_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVmotionShareLevel", []))

    @jsii.member(jsii_name="resetVsanMaximumMbit")
    def reset_vsan_maximum_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVsanMaximumMbit", []))

    @jsii.member(jsii_name="resetVsanReservationMbit")
    def reset_vsan_reservation_mbit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVsanReservationMbit", []))

    @jsii.member(jsii_name="resetVsanShareCount")
    def reset_vsan_share_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVsanShareCount", []))

    @jsii.member(jsii_name="resetVsanShareLevel")
    def reset_vsan_share_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVsanShareLevel", []))

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
    @jsii.member(jsii_name="host")
    def host(self) -> "DistributedVirtualSwitchHostList":
        return typing.cast("DistributedVirtualSwitchHostList", jsii.get(self, "host"))

    @builtins.property
    @jsii.member(jsii_name="pvlanMapping")
    def pvlan_mapping(self) -> "DistributedVirtualSwitchPvlanMappingList":
        return typing.cast("DistributedVirtualSwitchPvlanMappingList", jsii.get(self, "pvlanMapping"))

    @builtins.property
    @jsii.member(jsii_name="vlanRange")
    def vlan_range(self) -> "DistributedVirtualSwitchVlanRangeList":
        return typing.cast("DistributedVirtualSwitchVlanRangeList", jsii.get(self, "vlanRange"))

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
    @jsii.member(jsii_name="backupnfcMaximumMbitInput")
    def backupnfc_maximum_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupnfcMaximumMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="backupnfcReservationMbitInput")
    def backupnfc_reservation_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupnfcReservationMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="backupnfcShareCountInput")
    def backupnfc_share_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupnfcShareCountInput"))

    @builtins.property
    @jsii.member(jsii_name="backupnfcShareLevelInput")
    def backupnfc_share_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupnfcShareLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="blockAllPortsInput")
    def block_all_ports_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "blockAllPortsInput"))

    @builtins.property
    @jsii.member(jsii_name="checkBeaconInput")
    def check_beacon_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "checkBeaconInput"))

    @builtins.property
    @jsii.member(jsii_name="contactDetailInput")
    def contact_detail_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contactDetailInput"))

    @builtins.property
    @jsii.member(jsii_name="contactNameInput")
    def contact_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contactNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customAttributesInput")
    def custom_attributes_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterIdInput")
    def datacenter_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datacenterIdInput"))

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
    @jsii.member(jsii_name="faulttoleranceMaximumMbitInput")
    def faulttolerance_maximum_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "faulttoleranceMaximumMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="faulttoleranceReservationMbitInput")
    def faulttolerance_reservation_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "faulttoleranceReservationMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="faulttoleranceShareCountInput")
    def faulttolerance_share_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "faulttoleranceShareCountInput"))

    @builtins.property
    @jsii.member(jsii_name="faulttoleranceShareLevelInput")
    def faulttolerance_share_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "faulttoleranceShareLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="folderInput")
    def folder_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "folderInput"))

    @builtins.property
    @jsii.member(jsii_name="hbrMaximumMbitInput")
    def hbr_maximum_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hbrMaximumMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="hbrReservationMbitInput")
    def hbr_reservation_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hbrReservationMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="hbrShareCountInput")
    def hbr_share_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hbrShareCountInput"))

    @builtins.property
    @jsii.member(jsii_name="hbrShareLevelInput")
    def hbr_share_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hbrShareLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DistributedVirtualSwitchHost"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DistributedVirtualSwitchHost"]]], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreOtherPvlanMappingsInput")
    def ignore_other_pvlan_mappings_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreOtherPvlanMappingsInput"))

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
    @jsii.member(jsii_name="ipv4AddressInput")
    def ipv4_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv4AddressInput"))

    @builtins.property
    @jsii.member(jsii_name="iscsiMaximumMbitInput")
    def iscsi_maximum_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iscsiMaximumMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="iscsiReservationMbitInput")
    def iscsi_reservation_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iscsiReservationMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="iscsiShareCountInput")
    def iscsi_share_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iscsiShareCountInput"))

    @builtins.property
    @jsii.member(jsii_name="iscsiShareLevelInput")
    def iscsi_share_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iscsiShareLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="lacpApiVersionInput")
    def lacp_api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lacpApiVersionInput"))

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
    @jsii.member(jsii_name="linkDiscoveryOperationInput")
    def link_discovery_operation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "linkDiscoveryOperationInput"))

    @builtins.property
    @jsii.member(jsii_name="linkDiscoveryProtocolInput")
    def link_discovery_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "linkDiscoveryProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="managementMaximumMbitInput")
    def management_maximum_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "managementMaximumMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="managementReservationMbitInput")
    def management_reservation_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "managementReservationMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="managementShareCountInput")
    def management_share_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "managementShareCountInput"))

    @builtins.property
    @jsii.member(jsii_name="managementShareLevelInput")
    def management_share_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managementShareLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="maxMtuInput")
    def max_mtu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxMtuInput"))

    @builtins.property
    @jsii.member(jsii_name="multicastFilteringModeInput")
    def multicast_filtering_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "multicastFilteringModeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="netflowActiveFlowTimeoutInput")
    def netflow_active_flow_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netflowActiveFlowTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="netflowCollectorIpAddressInput")
    def netflow_collector_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "netflowCollectorIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="netflowCollectorPortInput")
    def netflow_collector_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netflowCollectorPortInput"))

    @builtins.property
    @jsii.member(jsii_name="netflowEnabledInput")
    def netflow_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "netflowEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="netflowIdleFlowTimeoutInput")
    def netflow_idle_flow_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netflowIdleFlowTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="netflowInternalFlowsOnlyInput")
    def netflow_internal_flows_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "netflowInternalFlowsOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="netflowObservationDomainIdInput")
    def netflow_observation_domain_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netflowObservationDomainIdInput"))

    @builtins.property
    @jsii.member(jsii_name="netflowSamplingRateInput")
    def netflow_sampling_rate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netflowSamplingRateInput"))

    @builtins.property
    @jsii.member(jsii_name="networkResourceControlEnabledInput")
    def network_resource_control_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "networkResourceControlEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="networkResourceControlVersionInput")
    def network_resource_control_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkResourceControlVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="nfsMaximumMbitInput")
    def nfs_maximum_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nfsMaximumMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="nfsReservationMbitInput")
    def nfs_reservation_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nfsReservationMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="nfsShareCountInput")
    def nfs_share_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nfsShareCountInput"))

    @builtins.property
    @jsii.member(jsii_name="nfsShareLevelInput")
    def nfs_share_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nfsShareLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="notifySwitchesInput")
    def notify_switches_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "notifySwitchesInput"))

    @builtins.property
    @jsii.member(jsii_name="portPrivateSecondaryVlanIdInput")
    def port_private_secondary_vlan_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portPrivateSecondaryVlanIdInput"))

    @builtins.property
    @jsii.member(jsii_name="pvlanMappingInput")
    def pvlan_mapping_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DistributedVirtualSwitchPvlanMapping"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DistributedVirtualSwitchPvlanMapping"]]], jsii.get(self, "pvlanMappingInput"))

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
    @jsii.member(jsii_name="txUplinkInput")
    def tx_uplink_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "txUplinkInput"))

    @builtins.property
    @jsii.member(jsii_name="uplinksInput")
    def uplinks_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "uplinksInput"))

    @builtins.property
    @jsii.member(jsii_name="vdpMaximumMbitInput")
    def vdp_maximum_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vdpMaximumMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="vdpReservationMbitInput")
    def vdp_reservation_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vdpReservationMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="vdpShareCountInput")
    def vdp_share_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vdpShareCountInput"))

    @builtins.property
    @jsii.member(jsii_name="vdpShareLevelInput")
    def vdp_share_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vdpShareLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualmachineMaximumMbitInput")
    def virtualmachine_maximum_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "virtualmachineMaximumMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualmachineReservationMbitInput")
    def virtualmachine_reservation_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "virtualmachineReservationMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualmachineShareCountInput")
    def virtualmachine_share_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "virtualmachineShareCountInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualmachineShareLevelInput")
    def virtualmachine_share_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualmachineShareLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="vlanIdInput")
    def vlan_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vlanIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vlanRangeInput")
    def vlan_range_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DistributedVirtualSwitchVlanRange"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DistributedVirtualSwitchVlanRange"]]], jsii.get(self, "vlanRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="vmotionMaximumMbitInput")
    def vmotion_maximum_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vmotionMaximumMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="vmotionReservationMbitInput")
    def vmotion_reservation_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vmotionReservationMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="vmotionShareCountInput")
    def vmotion_share_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vmotionShareCountInput"))

    @builtins.property
    @jsii.member(jsii_name="vmotionShareLevelInput")
    def vmotion_share_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmotionShareLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="vsanMaximumMbitInput")
    def vsan_maximum_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vsanMaximumMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="vsanReservationMbitInput")
    def vsan_reservation_mbit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vsanReservationMbitInput"))

    @builtins.property
    @jsii.member(jsii_name="vsanShareCountInput")
    def vsan_share_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vsanShareCountInput"))

    @builtins.property
    @jsii.member(jsii_name="vsanShareLevelInput")
    def vsan_share_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vsanShareLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="activeUplinks")
    def active_uplinks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "activeUplinks"))

    @active_uplinks.setter
    def active_uplinks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "active_uplinks").fset)
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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "allow_forged_transmits").fset)
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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "allow_mac_changes").fset)
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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "allow_promiscuous").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowPromiscuous", value)

    @builtins.property
    @jsii.member(jsii_name="backupnfcMaximumMbit")
    def backupnfc_maximum_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backupnfcMaximumMbit"))

    @backupnfc_maximum_mbit.setter
    def backupnfc_maximum_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "backupnfc_maximum_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupnfcMaximumMbit", value)

    @builtins.property
    @jsii.member(jsii_name="backupnfcReservationMbit")
    def backupnfc_reservation_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backupnfcReservationMbit"))

    @backupnfc_reservation_mbit.setter
    def backupnfc_reservation_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "backupnfc_reservation_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupnfcReservationMbit", value)

    @builtins.property
    @jsii.member(jsii_name="backupnfcShareCount")
    def backupnfc_share_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backupnfcShareCount"))

    @backupnfc_share_count.setter
    def backupnfc_share_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "backupnfc_share_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupnfcShareCount", value)

    @builtins.property
    @jsii.member(jsii_name="backupnfcShareLevel")
    def backupnfc_share_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupnfcShareLevel"))

    @backupnfc_share_level.setter
    def backupnfc_share_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "backupnfc_share_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupnfcShareLevel", value)

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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "block_all_ports").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockAllPorts", value)

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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "check_beacon").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkBeacon", value)

    @builtins.property
    @jsii.member(jsii_name="contactDetail")
    def contact_detail(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contactDetail"))

    @contact_detail.setter
    def contact_detail(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "contact_detail").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactDetail", value)

    @builtins.property
    @jsii.member(jsii_name="contactName")
    def contact_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contactName"))

    @contact_name.setter
    def contact_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "contact_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactName", value)

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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "custom_attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datacenterId"))

    @datacenter_id.setter
    def datacenter_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "datacenter_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenterId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "description").fset)
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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "directpath_gen2_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directpathGen2Allowed", value)

    @builtins.property
    @jsii.member(jsii_name="egressShapingAverageBandwidth")
    def egress_shaping_average_bandwidth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "egressShapingAverageBandwidth"))

    @egress_shaping_average_bandwidth.setter
    def egress_shaping_average_bandwidth(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "egress_shaping_average_bandwidth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egressShapingAverageBandwidth", value)

    @builtins.property
    @jsii.member(jsii_name="egressShapingBurstSize")
    def egress_shaping_burst_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "egressShapingBurstSize"))

    @egress_shaping_burst_size.setter
    def egress_shaping_burst_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "egress_shaping_burst_size").fset)
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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "egress_shaping_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egressShapingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="egressShapingPeakBandwidth")
    def egress_shaping_peak_bandwidth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "egressShapingPeakBandwidth"))

    @egress_shaping_peak_bandwidth.setter
    def egress_shaping_peak_bandwidth(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "egress_shaping_peak_bandwidth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egressShapingPeakBandwidth", value)

    @builtins.property
    @jsii.member(jsii_name="failback")
    def failback(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "failback"))

    @failback.setter
    def failback(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "failback").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failback", value)

    @builtins.property
    @jsii.member(jsii_name="faulttoleranceMaximumMbit")
    def faulttolerance_maximum_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "faulttoleranceMaximumMbit"))

    @faulttolerance_maximum_mbit.setter
    def faulttolerance_maximum_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "faulttolerance_maximum_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "faulttoleranceMaximumMbit", value)

    @builtins.property
    @jsii.member(jsii_name="faulttoleranceReservationMbit")
    def faulttolerance_reservation_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "faulttoleranceReservationMbit"))

    @faulttolerance_reservation_mbit.setter
    def faulttolerance_reservation_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "faulttolerance_reservation_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "faulttoleranceReservationMbit", value)

    @builtins.property
    @jsii.member(jsii_name="faulttoleranceShareCount")
    def faulttolerance_share_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "faulttoleranceShareCount"))

    @faulttolerance_share_count.setter
    def faulttolerance_share_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "faulttolerance_share_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "faulttoleranceShareCount", value)

    @builtins.property
    @jsii.member(jsii_name="faulttoleranceShareLevel")
    def faulttolerance_share_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "faulttoleranceShareLevel"))

    @faulttolerance_share_level.setter
    def faulttolerance_share_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "faulttolerance_share_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "faulttoleranceShareLevel", value)

    @builtins.property
    @jsii.member(jsii_name="folder")
    def folder(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "folder"))

    @folder.setter
    def folder(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "folder").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "folder", value)

    @builtins.property
    @jsii.member(jsii_name="hbrMaximumMbit")
    def hbr_maximum_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hbrMaximumMbit"))

    @hbr_maximum_mbit.setter
    def hbr_maximum_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "hbr_maximum_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hbrMaximumMbit", value)

    @builtins.property
    @jsii.member(jsii_name="hbrReservationMbit")
    def hbr_reservation_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hbrReservationMbit"))

    @hbr_reservation_mbit.setter
    def hbr_reservation_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "hbr_reservation_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hbrReservationMbit", value)

    @builtins.property
    @jsii.member(jsii_name="hbrShareCount")
    def hbr_share_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hbrShareCount"))

    @hbr_share_count.setter
    def hbr_share_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "hbr_share_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hbrShareCount", value)

    @builtins.property
    @jsii.member(jsii_name="hbrShareLevel")
    def hbr_share_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hbrShareLevel"))

    @hbr_share_level.setter
    def hbr_share_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "hbr_share_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hbrShareLevel", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreOtherPvlanMappings")
    def ignore_other_pvlan_mappings(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreOtherPvlanMappings"))

    @ignore_other_pvlan_mappings.setter
    def ignore_other_pvlan_mappings(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "ignore_other_pvlan_mappings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreOtherPvlanMappings", value)

    @builtins.property
    @jsii.member(jsii_name="ingressShapingAverageBandwidth")
    def ingress_shaping_average_bandwidth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ingressShapingAverageBandwidth"))

    @ingress_shaping_average_bandwidth.setter
    def ingress_shaping_average_bandwidth(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "ingress_shaping_average_bandwidth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressShapingAverageBandwidth", value)

    @builtins.property
    @jsii.member(jsii_name="ingressShapingBurstSize")
    def ingress_shaping_burst_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ingressShapingBurstSize"))

    @ingress_shaping_burst_size.setter
    def ingress_shaping_burst_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "ingress_shaping_burst_size").fset)
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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "ingress_shaping_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressShapingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="ingressShapingPeakBandwidth")
    def ingress_shaping_peak_bandwidth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ingressShapingPeakBandwidth"))

    @ingress_shaping_peak_bandwidth.setter
    def ingress_shaping_peak_bandwidth(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "ingress_shaping_peak_bandwidth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressShapingPeakBandwidth", value)

    @builtins.property
    @jsii.member(jsii_name="ipv4Address")
    def ipv4_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv4Address"))

    @ipv4_address.setter
    def ipv4_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "ipv4_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv4Address", value)

    @builtins.property
    @jsii.member(jsii_name="iscsiMaximumMbit")
    def iscsi_maximum_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iscsiMaximumMbit"))

    @iscsi_maximum_mbit.setter
    def iscsi_maximum_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "iscsi_maximum_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iscsiMaximumMbit", value)

    @builtins.property
    @jsii.member(jsii_name="iscsiReservationMbit")
    def iscsi_reservation_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iscsiReservationMbit"))

    @iscsi_reservation_mbit.setter
    def iscsi_reservation_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "iscsi_reservation_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iscsiReservationMbit", value)

    @builtins.property
    @jsii.member(jsii_name="iscsiShareCount")
    def iscsi_share_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iscsiShareCount"))

    @iscsi_share_count.setter
    def iscsi_share_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "iscsi_share_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iscsiShareCount", value)

    @builtins.property
    @jsii.member(jsii_name="iscsiShareLevel")
    def iscsi_share_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iscsiShareLevel"))

    @iscsi_share_level.setter
    def iscsi_share_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "iscsi_share_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iscsiShareLevel", value)

    @builtins.property
    @jsii.member(jsii_name="lacpApiVersion")
    def lacp_api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lacpApiVersion"))

    @lacp_api_version.setter
    def lacp_api_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "lacp_api_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lacpApiVersion", value)

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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "lacp_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lacpEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="lacpMode")
    def lacp_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lacpMode"))

    @lacp_mode.setter
    def lacp_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "lacp_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lacpMode", value)

    @builtins.property
    @jsii.member(jsii_name="linkDiscoveryOperation")
    def link_discovery_operation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "linkDiscoveryOperation"))

    @link_discovery_operation.setter
    def link_discovery_operation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "link_discovery_operation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkDiscoveryOperation", value)

    @builtins.property
    @jsii.member(jsii_name="linkDiscoveryProtocol")
    def link_discovery_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "linkDiscoveryProtocol"))

    @link_discovery_protocol.setter
    def link_discovery_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "link_discovery_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkDiscoveryProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="managementMaximumMbit")
    def management_maximum_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "managementMaximumMbit"))

    @management_maximum_mbit.setter
    def management_maximum_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "management_maximum_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managementMaximumMbit", value)

    @builtins.property
    @jsii.member(jsii_name="managementReservationMbit")
    def management_reservation_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "managementReservationMbit"))

    @management_reservation_mbit.setter
    def management_reservation_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "management_reservation_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managementReservationMbit", value)

    @builtins.property
    @jsii.member(jsii_name="managementShareCount")
    def management_share_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "managementShareCount"))

    @management_share_count.setter
    def management_share_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "management_share_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managementShareCount", value)

    @builtins.property
    @jsii.member(jsii_name="managementShareLevel")
    def management_share_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managementShareLevel"))

    @management_share_level.setter
    def management_share_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "management_share_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managementShareLevel", value)

    @builtins.property
    @jsii.member(jsii_name="maxMtu")
    def max_mtu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxMtu"))

    @max_mtu.setter
    def max_mtu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "max_mtu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxMtu", value)

    @builtins.property
    @jsii.member(jsii_name="multicastFilteringMode")
    def multicast_filtering_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "multicastFilteringMode"))

    @multicast_filtering_mode.setter
    def multicast_filtering_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "multicast_filtering_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multicastFilteringMode", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="netflowActiveFlowTimeout")
    def netflow_active_flow_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netflowActiveFlowTimeout"))

    @netflow_active_flow_timeout.setter
    def netflow_active_flow_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "netflow_active_flow_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netflowActiveFlowTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="netflowCollectorIpAddress")
    def netflow_collector_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "netflowCollectorIpAddress"))

    @netflow_collector_ip_address.setter
    def netflow_collector_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "netflow_collector_ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netflowCollectorIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="netflowCollectorPort")
    def netflow_collector_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netflowCollectorPort"))

    @netflow_collector_port.setter
    def netflow_collector_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "netflow_collector_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netflowCollectorPort", value)

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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "netflow_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netflowEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="netflowIdleFlowTimeout")
    def netflow_idle_flow_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netflowIdleFlowTimeout"))

    @netflow_idle_flow_timeout.setter
    def netflow_idle_flow_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "netflow_idle_flow_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netflowIdleFlowTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="netflowInternalFlowsOnly")
    def netflow_internal_flows_only(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "netflowInternalFlowsOnly"))

    @netflow_internal_flows_only.setter
    def netflow_internal_flows_only(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "netflow_internal_flows_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netflowInternalFlowsOnly", value)

    @builtins.property
    @jsii.member(jsii_name="netflowObservationDomainId")
    def netflow_observation_domain_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netflowObservationDomainId"))

    @netflow_observation_domain_id.setter
    def netflow_observation_domain_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "netflow_observation_domain_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netflowObservationDomainId", value)

    @builtins.property
    @jsii.member(jsii_name="netflowSamplingRate")
    def netflow_sampling_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netflowSamplingRate"))

    @netflow_sampling_rate.setter
    def netflow_sampling_rate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "netflow_sampling_rate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netflowSamplingRate", value)

    @builtins.property
    @jsii.member(jsii_name="networkResourceControlEnabled")
    def network_resource_control_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "networkResourceControlEnabled"))

    @network_resource_control_enabled.setter
    def network_resource_control_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "network_resource_control_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkResourceControlEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="networkResourceControlVersion")
    def network_resource_control_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkResourceControlVersion"))

    @network_resource_control_version.setter
    def network_resource_control_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "network_resource_control_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkResourceControlVersion", value)

    @builtins.property
    @jsii.member(jsii_name="nfsMaximumMbit")
    def nfs_maximum_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nfsMaximumMbit"))

    @nfs_maximum_mbit.setter
    def nfs_maximum_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "nfs_maximum_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nfsMaximumMbit", value)

    @builtins.property
    @jsii.member(jsii_name="nfsReservationMbit")
    def nfs_reservation_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nfsReservationMbit"))

    @nfs_reservation_mbit.setter
    def nfs_reservation_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "nfs_reservation_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nfsReservationMbit", value)

    @builtins.property
    @jsii.member(jsii_name="nfsShareCount")
    def nfs_share_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nfsShareCount"))

    @nfs_share_count.setter
    def nfs_share_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "nfs_share_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nfsShareCount", value)

    @builtins.property
    @jsii.member(jsii_name="nfsShareLevel")
    def nfs_share_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nfsShareLevel"))

    @nfs_share_level.setter
    def nfs_share_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "nfs_share_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nfsShareLevel", value)

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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "notify_switches").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifySwitches", value)

    @builtins.property
    @jsii.member(jsii_name="portPrivateSecondaryVlanId")
    def port_private_secondary_vlan_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "portPrivateSecondaryVlanId"))

    @port_private_secondary_vlan_id.setter
    def port_private_secondary_vlan_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "port_private_secondary_vlan_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portPrivateSecondaryVlanId", value)

    @builtins.property
    @jsii.member(jsii_name="standbyUplinks")
    def standby_uplinks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "standbyUplinks"))

    @standby_uplinks.setter
    def standby_uplinks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "standby_uplinks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "standbyUplinks", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="teamingPolicy")
    def teaming_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "teamingPolicy"))

    @teaming_policy.setter
    def teaming_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "teaming_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="txUplink")
    def tx_uplink(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "txUplink"))

    @tx_uplink.setter
    def tx_uplink(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "tx_uplink").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "txUplink", value)

    @builtins.property
    @jsii.member(jsii_name="uplinks")
    def uplinks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "uplinks"))

    @uplinks.setter
    def uplinks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "uplinks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uplinks", value)

    @builtins.property
    @jsii.member(jsii_name="vdpMaximumMbit")
    def vdp_maximum_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vdpMaximumMbit"))

    @vdp_maximum_mbit.setter
    def vdp_maximum_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "vdp_maximum_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vdpMaximumMbit", value)

    @builtins.property
    @jsii.member(jsii_name="vdpReservationMbit")
    def vdp_reservation_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vdpReservationMbit"))

    @vdp_reservation_mbit.setter
    def vdp_reservation_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "vdp_reservation_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vdpReservationMbit", value)

    @builtins.property
    @jsii.member(jsii_name="vdpShareCount")
    def vdp_share_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vdpShareCount"))

    @vdp_share_count.setter
    def vdp_share_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "vdp_share_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vdpShareCount", value)

    @builtins.property
    @jsii.member(jsii_name="vdpShareLevel")
    def vdp_share_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vdpShareLevel"))

    @vdp_share_level.setter
    def vdp_share_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "vdp_share_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vdpShareLevel", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="virtualmachineMaximumMbit")
    def virtualmachine_maximum_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "virtualmachineMaximumMbit"))

    @virtualmachine_maximum_mbit.setter
    def virtualmachine_maximum_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "virtualmachine_maximum_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualmachineMaximumMbit", value)

    @builtins.property
    @jsii.member(jsii_name="virtualmachineReservationMbit")
    def virtualmachine_reservation_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "virtualmachineReservationMbit"))

    @virtualmachine_reservation_mbit.setter
    def virtualmachine_reservation_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "virtualmachine_reservation_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualmachineReservationMbit", value)

    @builtins.property
    @jsii.member(jsii_name="virtualmachineShareCount")
    def virtualmachine_share_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "virtualmachineShareCount"))

    @virtualmachine_share_count.setter
    def virtualmachine_share_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "virtualmachine_share_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualmachineShareCount", value)

    @builtins.property
    @jsii.member(jsii_name="virtualmachineShareLevel")
    def virtualmachine_share_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualmachineShareLevel"))

    @virtualmachine_share_level.setter
    def virtualmachine_share_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "virtualmachine_share_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualmachineShareLevel", value)

    @builtins.property
    @jsii.member(jsii_name="vlanId")
    def vlan_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vlanId"))

    @vlan_id.setter
    def vlan_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "vlan_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vlanId", value)

    @builtins.property
    @jsii.member(jsii_name="vmotionMaximumMbit")
    def vmotion_maximum_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vmotionMaximumMbit"))

    @vmotion_maximum_mbit.setter
    def vmotion_maximum_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "vmotion_maximum_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmotionMaximumMbit", value)

    @builtins.property
    @jsii.member(jsii_name="vmotionReservationMbit")
    def vmotion_reservation_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vmotionReservationMbit"))

    @vmotion_reservation_mbit.setter
    def vmotion_reservation_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "vmotion_reservation_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmotionReservationMbit", value)

    @builtins.property
    @jsii.member(jsii_name="vmotionShareCount")
    def vmotion_share_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vmotionShareCount"))

    @vmotion_share_count.setter
    def vmotion_share_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "vmotion_share_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmotionShareCount", value)

    @builtins.property
    @jsii.member(jsii_name="vmotionShareLevel")
    def vmotion_share_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmotionShareLevel"))

    @vmotion_share_level.setter
    def vmotion_share_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "vmotion_share_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmotionShareLevel", value)

    @builtins.property
    @jsii.member(jsii_name="vsanMaximumMbit")
    def vsan_maximum_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vsanMaximumMbit"))

    @vsan_maximum_mbit.setter
    def vsan_maximum_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "vsan_maximum_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vsanMaximumMbit", value)

    @builtins.property
    @jsii.member(jsii_name="vsanReservationMbit")
    def vsan_reservation_mbit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vsanReservationMbit"))

    @vsan_reservation_mbit.setter
    def vsan_reservation_mbit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "vsan_reservation_mbit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vsanReservationMbit", value)

    @builtins.property
    @jsii.member(jsii_name="vsanShareCount")
    def vsan_share_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vsanShareCount"))

    @vsan_share_count.setter
    def vsan_share_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "vsan_share_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vsanShareCount", value)

    @builtins.property
    @jsii.member(jsii_name="vsanShareLevel")
    def vsan_share_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vsanShareLevel"))

    @vsan_share_level.setter
    def vsan_share_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitch, "vsan_share_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vsanShareLevel", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.distributedVirtualSwitch.DistributedVirtualSwitchConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "datacenter_id": "datacenterId",
        "name": "name",
        "active_uplinks": "activeUplinks",
        "allow_forged_transmits": "allowForgedTransmits",
        "allow_mac_changes": "allowMacChanges",
        "allow_promiscuous": "allowPromiscuous",
        "backupnfc_maximum_mbit": "backupnfcMaximumMbit",
        "backupnfc_reservation_mbit": "backupnfcReservationMbit",
        "backupnfc_share_count": "backupnfcShareCount",
        "backupnfc_share_level": "backupnfcShareLevel",
        "block_all_ports": "blockAllPorts",
        "check_beacon": "checkBeacon",
        "contact_detail": "contactDetail",
        "contact_name": "contactName",
        "custom_attributes": "customAttributes",
        "description": "description",
        "directpath_gen2_allowed": "directpathGen2Allowed",
        "egress_shaping_average_bandwidth": "egressShapingAverageBandwidth",
        "egress_shaping_burst_size": "egressShapingBurstSize",
        "egress_shaping_enabled": "egressShapingEnabled",
        "egress_shaping_peak_bandwidth": "egressShapingPeakBandwidth",
        "failback": "failback",
        "faulttolerance_maximum_mbit": "faulttoleranceMaximumMbit",
        "faulttolerance_reservation_mbit": "faulttoleranceReservationMbit",
        "faulttolerance_share_count": "faulttoleranceShareCount",
        "faulttolerance_share_level": "faulttoleranceShareLevel",
        "folder": "folder",
        "hbr_maximum_mbit": "hbrMaximumMbit",
        "hbr_reservation_mbit": "hbrReservationMbit",
        "hbr_share_count": "hbrShareCount",
        "hbr_share_level": "hbrShareLevel",
        "host": "host",
        "id": "id",
        "ignore_other_pvlan_mappings": "ignoreOtherPvlanMappings",
        "ingress_shaping_average_bandwidth": "ingressShapingAverageBandwidth",
        "ingress_shaping_burst_size": "ingressShapingBurstSize",
        "ingress_shaping_enabled": "ingressShapingEnabled",
        "ingress_shaping_peak_bandwidth": "ingressShapingPeakBandwidth",
        "ipv4_address": "ipv4Address",
        "iscsi_maximum_mbit": "iscsiMaximumMbit",
        "iscsi_reservation_mbit": "iscsiReservationMbit",
        "iscsi_share_count": "iscsiShareCount",
        "iscsi_share_level": "iscsiShareLevel",
        "lacp_api_version": "lacpApiVersion",
        "lacp_enabled": "lacpEnabled",
        "lacp_mode": "lacpMode",
        "link_discovery_operation": "linkDiscoveryOperation",
        "link_discovery_protocol": "linkDiscoveryProtocol",
        "management_maximum_mbit": "managementMaximumMbit",
        "management_reservation_mbit": "managementReservationMbit",
        "management_share_count": "managementShareCount",
        "management_share_level": "managementShareLevel",
        "max_mtu": "maxMtu",
        "multicast_filtering_mode": "multicastFilteringMode",
        "netflow_active_flow_timeout": "netflowActiveFlowTimeout",
        "netflow_collector_ip_address": "netflowCollectorIpAddress",
        "netflow_collector_port": "netflowCollectorPort",
        "netflow_enabled": "netflowEnabled",
        "netflow_idle_flow_timeout": "netflowIdleFlowTimeout",
        "netflow_internal_flows_only": "netflowInternalFlowsOnly",
        "netflow_observation_domain_id": "netflowObservationDomainId",
        "netflow_sampling_rate": "netflowSamplingRate",
        "network_resource_control_enabled": "networkResourceControlEnabled",
        "network_resource_control_version": "networkResourceControlVersion",
        "nfs_maximum_mbit": "nfsMaximumMbit",
        "nfs_reservation_mbit": "nfsReservationMbit",
        "nfs_share_count": "nfsShareCount",
        "nfs_share_level": "nfsShareLevel",
        "notify_switches": "notifySwitches",
        "port_private_secondary_vlan_id": "portPrivateSecondaryVlanId",
        "pvlan_mapping": "pvlanMapping",
        "standby_uplinks": "standbyUplinks",
        "tags": "tags",
        "teaming_policy": "teamingPolicy",
        "tx_uplink": "txUplink",
        "uplinks": "uplinks",
        "vdp_maximum_mbit": "vdpMaximumMbit",
        "vdp_reservation_mbit": "vdpReservationMbit",
        "vdp_share_count": "vdpShareCount",
        "vdp_share_level": "vdpShareLevel",
        "version": "version",
        "virtualmachine_maximum_mbit": "virtualmachineMaximumMbit",
        "virtualmachine_reservation_mbit": "virtualmachineReservationMbit",
        "virtualmachine_share_count": "virtualmachineShareCount",
        "virtualmachine_share_level": "virtualmachineShareLevel",
        "vlan_id": "vlanId",
        "vlan_range": "vlanRange",
        "vmotion_maximum_mbit": "vmotionMaximumMbit",
        "vmotion_reservation_mbit": "vmotionReservationMbit",
        "vmotion_share_count": "vmotionShareCount",
        "vmotion_share_level": "vmotionShareLevel",
        "vsan_maximum_mbit": "vsanMaximumMbit",
        "vsan_reservation_mbit": "vsanReservationMbit",
        "vsan_share_count": "vsanShareCount",
        "vsan_share_level": "vsanShareLevel",
    },
)
class DistributedVirtualSwitchConfig(cdktf.TerraformMetaArguments):
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
        datacenter_id: builtins.str,
        name: builtins.str,
        active_uplinks: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_forged_transmits: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_mac_changes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_promiscuous: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        backupnfc_maximum_mbit: typing.Optional[jsii.Number] = None,
        backupnfc_reservation_mbit: typing.Optional[jsii.Number] = None,
        backupnfc_share_count: typing.Optional[jsii.Number] = None,
        backupnfc_share_level: typing.Optional[builtins.str] = None,
        block_all_ports: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        check_beacon: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        contact_detail: typing.Optional[builtins.str] = None,
        contact_name: typing.Optional[builtins.str] = None,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        directpath_gen2_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        egress_shaping_average_bandwidth: typing.Optional[jsii.Number] = None,
        egress_shaping_burst_size: typing.Optional[jsii.Number] = None,
        egress_shaping_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        egress_shaping_peak_bandwidth: typing.Optional[jsii.Number] = None,
        failback: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        faulttolerance_maximum_mbit: typing.Optional[jsii.Number] = None,
        faulttolerance_reservation_mbit: typing.Optional[jsii.Number] = None,
        faulttolerance_share_count: typing.Optional[jsii.Number] = None,
        faulttolerance_share_level: typing.Optional[builtins.str] = None,
        folder: typing.Optional[builtins.str] = None,
        hbr_maximum_mbit: typing.Optional[jsii.Number] = None,
        hbr_reservation_mbit: typing.Optional[jsii.Number] = None,
        hbr_share_count: typing.Optional[jsii.Number] = None,
        hbr_share_level: typing.Optional[builtins.str] = None,
        host: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DistributedVirtualSwitchHost", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        ignore_other_pvlan_mappings: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ingress_shaping_average_bandwidth: typing.Optional[jsii.Number] = None,
        ingress_shaping_burst_size: typing.Optional[jsii.Number] = None,
        ingress_shaping_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ingress_shaping_peak_bandwidth: typing.Optional[jsii.Number] = None,
        ipv4_address: typing.Optional[builtins.str] = None,
        iscsi_maximum_mbit: typing.Optional[jsii.Number] = None,
        iscsi_reservation_mbit: typing.Optional[jsii.Number] = None,
        iscsi_share_count: typing.Optional[jsii.Number] = None,
        iscsi_share_level: typing.Optional[builtins.str] = None,
        lacp_api_version: typing.Optional[builtins.str] = None,
        lacp_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        lacp_mode: typing.Optional[builtins.str] = None,
        link_discovery_operation: typing.Optional[builtins.str] = None,
        link_discovery_protocol: typing.Optional[builtins.str] = None,
        management_maximum_mbit: typing.Optional[jsii.Number] = None,
        management_reservation_mbit: typing.Optional[jsii.Number] = None,
        management_share_count: typing.Optional[jsii.Number] = None,
        management_share_level: typing.Optional[builtins.str] = None,
        max_mtu: typing.Optional[jsii.Number] = None,
        multicast_filtering_mode: typing.Optional[builtins.str] = None,
        netflow_active_flow_timeout: typing.Optional[jsii.Number] = None,
        netflow_collector_ip_address: typing.Optional[builtins.str] = None,
        netflow_collector_port: typing.Optional[jsii.Number] = None,
        netflow_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        netflow_idle_flow_timeout: typing.Optional[jsii.Number] = None,
        netflow_internal_flows_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        netflow_observation_domain_id: typing.Optional[jsii.Number] = None,
        netflow_sampling_rate: typing.Optional[jsii.Number] = None,
        network_resource_control_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        network_resource_control_version: typing.Optional[builtins.str] = None,
        nfs_maximum_mbit: typing.Optional[jsii.Number] = None,
        nfs_reservation_mbit: typing.Optional[jsii.Number] = None,
        nfs_share_count: typing.Optional[jsii.Number] = None,
        nfs_share_level: typing.Optional[builtins.str] = None,
        notify_switches: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        port_private_secondary_vlan_id: typing.Optional[jsii.Number] = None,
        pvlan_mapping: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DistributedVirtualSwitchPvlanMapping", typing.Dict[str, typing.Any]]]]] = None,
        standby_uplinks: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        teaming_policy: typing.Optional[builtins.str] = None,
        tx_uplink: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        uplinks: typing.Optional[typing.Sequence[builtins.str]] = None,
        vdp_maximum_mbit: typing.Optional[jsii.Number] = None,
        vdp_reservation_mbit: typing.Optional[jsii.Number] = None,
        vdp_share_count: typing.Optional[jsii.Number] = None,
        vdp_share_level: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
        virtualmachine_maximum_mbit: typing.Optional[jsii.Number] = None,
        virtualmachine_reservation_mbit: typing.Optional[jsii.Number] = None,
        virtualmachine_share_count: typing.Optional[jsii.Number] = None,
        virtualmachine_share_level: typing.Optional[builtins.str] = None,
        vlan_id: typing.Optional[jsii.Number] = None,
        vlan_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DistributedVirtualSwitchVlanRange", typing.Dict[str, typing.Any]]]]] = None,
        vmotion_maximum_mbit: typing.Optional[jsii.Number] = None,
        vmotion_reservation_mbit: typing.Optional[jsii.Number] = None,
        vmotion_share_count: typing.Optional[jsii.Number] = None,
        vmotion_share_level: typing.Optional[builtins.str] = None,
        vsan_maximum_mbit: typing.Optional[jsii.Number] = None,
        vsan_reservation_mbit: typing.Optional[jsii.Number] = None,
        vsan_share_count: typing.Optional[jsii.Number] = None,
        vsan_share_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param datacenter_id: The ID of the datacenter to create this virtual switch in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#datacenter_id DistributedVirtualSwitch#datacenter_id}
        :param name: The name for the DVS. Must be unique in the folder that it is being created in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#name DistributedVirtualSwitch#name}
        :param active_uplinks: List of active uplinks used for load balancing, matching the names of the uplinks assigned in the DVS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#active_uplinks DistributedVirtualSwitch#active_uplinks}
        :param allow_forged_transmits: Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than that of its own. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#allow_forged_transmits DistributedVirtualSwitch#allow_forged_transmits}
        :param allow_mac_changes: Controls whether or not the Media Access Control (MAC) address can be changed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#allow_mac_changes DistributedVirtualSwitch#allow_mac_changes}
        :param allow_promiscuous: Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#allow_promiscuous DistributedVirtualSwitch#allow_promiscuous}
        :param backupnfc_maximum_mbit: The maximum allowed usage for the backupNfc traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#backupnfc_maximum_mbit DistributedVirtualSwitch#backupnfc_maximum_mbit}
        :param backupnfc_reservation_mbit: The amount of guaranteed bandwidth for the backupNfc traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#backupnfc_reservation_mbit DistributedVirtualSwitch#backupnfc_reservation_mbit}
        :param backupnfc_share_count: The amount of shares to allocate to the backupNfc traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#backupnfc_share_count DistributedVirtualSwitch#backupnfc_share_count}
        :param backupnfc_share_level: The allocation level for the backupNfc traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#backupnfc_share_level DistributedVirtualSwitch#backupnfc_share_level}
        :param block_all_ports: Indicates whether to block all ports by default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#block_all_ports DistributedVirtualSwitch#block_all_ports}
        :param check_beacon: Enable beacon probing on the ports this policy applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#check_beacon DistributedVirtualSwitch#check_beacon}
        :param contact_detail: The contact detail for this DVS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#contact_detail DistributedVirtualSwitch#contact_detail}
        :param contact_name: The contact name for this DVS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#contact_name DistributedVirtualSwitch#contact_name}
        :param custom_attributes: A list of custom attributes to set on this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#custom_attributes DistributedVirtualSwitch#custom_attributes}
        :param description: The description of the DVS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#description DistributedVirtualSwitch#description}
        :param directpath_gen2_allowed: Allow VMDirectPath Gen2 on the ports this policy applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#directpath_gen2_allowed DistributedVirtualSwitch#directpath_gen2_allowed}
        :param egress_shaping_average_bandwidth: The average egress bandwidth in bits per second if egress shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#egress_shaping_average_bandwidth DistributedVirtualSwitch#egress_shaping_average_bandwidth}
        :param egress_shaping_burst_size: The maximum egress burst size allowed in bytes if egress shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#egress_shaping_burst_size DistributedVirtualSwitch#egress_shaping_burst_size}
        :param egress_shaping_enabled: True if the traffic shaper is enabled for egress traffic on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#egress_shaping_enabled DistributedVirtualSwitch#egress_shaping_enabled}
        :param egress_shaping_peak_bandwidth: The peak egress bandwidth during bursts in bits per second if egress traffic shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#egress_shaping_peak_bandwidth DistributedVirtualSwitch#egress_shaping_peak_bandwidth}
        :param failback: If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#failback DistributedVirtualSwitch#failback}
        :param faulttolerance_maximum_mbit: The maximum allowed usage for the faultTolerance traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#faulttolerance_maximum_mbit DistributedVirtualSwitch#faulttolerance_maximum_mbit}
        :param faulttolerance_reservation_mbit: The amount of guaranteed bandwidth for the faultTolerance traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#faulttolerance_reservation_mbit DistributedVirtualSwitch#faulttolerance_reservation_mbit}
        :param faulttolerance_share_count: The amount of shares to allocate to the faultTolerance traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#faulttolerance_share_count DistributedVirtualSwitch#faulttolerance_share_count}
        :param faulttolerance_share_level: The allocation level for the faultTolerance traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#faulttolerance_share_level DistributedVirtualSwitch#faulttolerance_share_level}
        :param folder: The folder to create this virtual switch in, relative to the datacenter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#folder DistributedVirtualSwitch#folder}
        :param hbr_maximum_mbit: The maximum allowed usage for the hbr traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#hbr_maximum_mbit DistributedVirtualSwitch#hbr_maximum_mbit}
        :param hbr_reservation_mbit: The amount of guaranteed bandwidth for the hbr traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#hbr_reservation_mbit DistributedVirtualSwitch#hbr_reservation_mbit}
        :param hbr_share_count: The amount of shares to allocate to the hbr traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#hbr_share_count DistributedVirtualSwitch#hbr_share_count}
        :param hbr_share_level: The allocation level for the hbr traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#hbr_share_level DistributedVirtualSwitch#hbr_share_level}
        :param host: host block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#host DistributedVirtualSwitch#host}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#id DistributedVirtualSwitch#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignore_other_pvlan_mappings: Whether to ignore existing PVLAN mappings not managed by this resource. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#ignore_other_pvlan_mappings DistributedVirtualSwitch#ignore_other_pvlan_mappings}
        :param ingress_shaping_average_bandwidth: The average ingress bandwidth in bits per second if ingress shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#ingress_shaping_average_bandwidth DistributedVirtualSwitch#ingress_shaping_average_bandwidth}
        :param ingress_shaping_burst_size: The maximum ingress burst size allowed in bytes if ingress shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#ingress_shaping_burst_size DistributedVirtualSwitch#ingress_shaping_burst_size}
        :param ingress_shaping_enabled: True if the traffic shaper is enabled for ingress traffic on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#ingress_shaping_enabled DistributedVirtualSwitch#ingress_shaping_enabled}
        :param ingress_shaping_peak_bandwidth: The peak ingress bandwidth during bursts in bits per second if ingress traffic shaping is enabled on the port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#ingress_shaping_peak_bandwidth DistributedVirtualSwitch#ingress_shaping_peak_bandwidth}
        :param ipv4_address: The IPv4 address of the switch. This can be used to see the DVS as a unique device with NetFlow. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#ipv4_address DistributedVirtualSwitch#ipv4_address}
        :param iscsi_maximum_mbit: The maximum allowed usage for the iSCSI traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#iscsi_maximum_mbit DistributedVirtualSwitch#iscsi_maximum_mbit}
        :param iscsi_reservation_mbit: The amount of guaranteed bandwidth for the iSCSI traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#iscsi_reservation_mbit DistributedVirtualSwitch#iscsi_reservation_mbit}
        :param iscsi_share_count: The amount of shares to allocate to the iSCSI traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#iscsi_share_count DistributedVirtualSwitch#iscsi_share_count}
        :param iscsi_share_level: The allocation level for the iSCSI traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#iscsi_share_level DistributedVirtualSwitch#iscsi_share_level}
        :param lacp_api_version: The Link Aggregation Control Protocol group version in the switch. Can be one of singleLag or multipleLag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#lacp_api_version DistributedVirtualSwitch#lacp_api_version}
        :param lacp_enabled: Whether or not to enable LACP on all uplink ports. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#lacp_enabled DistributedVirtualSwitch#lacp_enabled}
        :param lacp_mode: The uplink LACP mode to use. Can be one of active or passive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#lacp_mode DistributedVirtualSwitch#lacp_mode}
        :param link_discovery_operation: Whether to advertise or listen for link discovery. Valid values are advertise, both, listen, and none. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#link_discovery_operation DistributedVirtualSwitch#link_discovery_operation}
        :param link_discovery_protocol: The discovery protocol type. Valid values are cdp and lldp. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#link_discovery_protocol DistributedVirtualSwitch#link_discovery_protocol}
        :param management_maximum_mbit: The maximum allowed usage for the management traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#management_maximum_mbit DistributedVirtualSwitch#management_maximum_mbit}
        :param management_reservation_mbit: The amount of guaranteed bandwidth for the management traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#management_reservation_mbit DistributedVirtualSwitch#management_reservation_mbit}
        :param management_share_count: The amount of shares to allocate to the management traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#management_share_count DistributedVirtualSwitch#management_share_count}
        :param management_share_level: The allocation level for the management traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#management_share_level DistributedVirtualSwitch#management_share_level}
        :param max_mtu: The maximum MTU on the switch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#max_mtu DistributedVirtualSwitch#max_mtu}
        :param multicast_filtering_mode: The multicast filtering mode on the switch. Can be one of legacyFiltering, or snooping. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#multicast_filtering_mode DistributedVirtualSwitch#multicast_filtering_mode}
        :param netflow_active_flow_timeout: The number of seconds after which active flows are forced to be exported to the collector. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_active_flow_timeout DistributedVirtualSwitch#netflow_active_flow_timeout}
        :param netflow_collector_ip_address: IP address for the netflow collector, using IPv4 or IPv6. IPv6 is supported in vSphere Distributed Switch Version 6.0 or later. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_collector_ip_address DistributedVirtualSwitch#netflow_collector_ip_address}
        :param netflow_collector_port: The port for the netflow collector. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_collector_port DistributedVirtualSwitch#netflow_collector_port}
        :param netflow_enabled: Indicates whether to enable netflow on all ports. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_enabled DistributedVirtualSwitch#netflow_enabled}
        :param netflow_idle_flow_timeout: The number of seconds after which idle flows are forced to be exported to the collector. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_idle_flow_timeout DistributedVirtualSwitch#netflow_idle_flow_timeout}
        :param netflow_internal_flows_only: Whether to limit analysis to traffic that has both source and destination served by the same host. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_internal_flows_only DistributedVirtualSwitch#netflow_internal_flows_only}
        :param netflow_observation_domain_id: The observation Domain ID for the netflow collector. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_observation_domain_id DistributedVirtualSwitch#netflow_observation_domain_id}
        :param netflow_sampling_rate: The ratio of total number of packets to the number of packets analyzed. Set to 0 to disable sampling, meaning that all packets are analyzed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_sampling_rate DistributedVirtualSwitch#netflow_sampling_rate}
        :param network_resource_control_enabled: Whether or not to enable network resource control, enabling advanced traffic shaping and resource control features. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#network_resource_control_enabled DistributedVirtualSwitch#network_resource_control_enabled}
        :param network_resource_control_version: The network I/O control version to use. Can be one of version2 or version3. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#network_resource_control_version DistributedVirtualSwitch#network_resource_control_version}
        :param nfs_maximum_mbit: The maximum allowed usage for the nfs traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#nfs_maximum_mbit DistributedVirtualSwitch#nfs_maximum_mbit}
        :param nfs_reservation_mbit: The amount of guaranteed bandwidth for the nfs traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#nfs_reservation_mbit DistributedVirtualSwitch#nfs_reservation_mbit}
        :param nfs_share_count: The amount of shares to allocate to the nfs traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#nfs_share_count DistributedVirtualSwitch#nfs_share_count}
        :param nfs_share_level: The allocation level for the nfs traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#nfs_share_level DistributedVirtualSwitch#nfs_share_level}
        :param notify_switches: If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#notify_switches DistributedVirtualSwitch#notify_switches}
        :param port_private_secondary_vlan_id: The secondary VLAN ID for this port. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#port_private_secondary_vlan_id DistributedVirtualSwitch#port_private_secondary_vlan_id}
        :param pvlan_mapping: pvlan_mapping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#pvlan_mapping DistributedVirtualSwitch#pvlan_mapping}
        :param standby_uplinks: List of standby uplinks used for load balancing, matching the names of the uplinks assigned in the DVS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#standby_uplinks DistributedVirtualSwitch#standby_uplinks}
        :param tags: A list of tag IDs to apply to this object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#tags DistributedVirtualSwitch#tags}
        :param teaming_policy: The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, failover_explicit, or loadbalance_loadbased. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#teaming_policy DistributedVirtualSwitch#teaming_policy}
        :param tx_uplink: If true, a copy of packets sent to the switch will always be forwarded to an uplink in addition to the regular packet forwarded done by the switch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#tx_uplink DistributedVirtualSwitch#tx_uplink}
        :param uplinks: A list of uplink ports. The contents of this list control both the uplink count and names of the uplinks on the DVS across hosts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#uplinks DistributedVirtualSwitch#uplinks}
        :param vdp_maximum_mbit: The maximum allowed usage for the vdp traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vdp_maximum_mbit DistributedVirtualSwitch#vdp_maximum_mbit}
        :param vdp_reservation_mbit: The amount of guaranteed bandwidth for the vdp traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vdp_reservation_mbit DistributedVirtualSwitch#vdp_reservation_mbit}
        :param vdp_share_count: The amount of shares to allocate to the vdp traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vdp_share_count DistributedVirtualSwitch#vdp_share_count}
        :param vdp_share_level: The allocation level for the vdp traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vdp_share_level DistributedVirtualSwitch#vdp_share_level}
        :param version: The version of this virtual switch. Allowed versions are 7.0.3, 7.0.0, 6.6.0, 6.5.0, 6.0.0, 5.5.0, 5.1.0, and 5.0.0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#version DistributedVirtualSwitch#version}
        :param virtualmachine_maximum_mbit: The maximum allowed usage for the virtualMachine traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#virtualmachine_maximum_mbit DistributedVirtualSwitch#virtualmachine_maximum_mbit}
        :param virtualmachine_reservation_mbit: The amount of guaranteed bandwidth for the virtualMachine traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#virtualmachine_reservation_mbit DistributedVirtualSwitch#virtualmachine_reservation_mbit}
        :param virtualmachine_share_count: The amount of shares to allocate to the virtualMachine traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#virtualmachine_share_count DistributedVirtualSwitch#virtualmachine_share_count}
        :param virtualmachine_share_level: The allocation level for the virtualMachine traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#virtualmachine_share_level DistributedVirtualSwitch#virtualmachine_share_level}
        :param vlan_id: The VLAN ID for single VLAN mode. 0 denotes no VLAN. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vlan_id DistributedVirtualSwitch#vlan_id}
        :param vlan_range: vlan_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vlan_range DistributedVirtualSwitch#vlan_range}
        :param vmotion_maximum_mbit: The maximum allowed usage for the vmotion traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vmotion_maximum_mbit DistributedVirtualSwitch#vmotion_maximum_mbit}
        :param vmotion_reservation_mbit: The amount of guaranteed bandwidth for the vmotion traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vmotion_reservation_mbit DistributedVirtualSwitch#vmotion_reservation_mbit}
        :param vmotion_share_count: The amount of shares to allocate to the vmotion traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vmotion_share_count DistributedVirtualSwitch#vmotion_share_count}
        :param vmotion_share_level: The allocation level for the vmotion traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vmotion_share_level DistributedVirtualSwitch#vmotion_share_level}
        :param vsan_maximum_mbit: The maximum allowed usage for the vsan traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vsan_maximum_mbit DistributedVirtualSwitch#vsan_maximum_mbit}
        :param vsan_reservation_mbit: The amount of guaranteed bandwidth for the vsan traffic class, in Mbits/sec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vsan_reservation_mbit DistributedVirtualSwitch#vsan_reservation_mbit}
        :param vsan_share_count: The amount of shares to allocate to the vsan traffic class for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vsan_share_count DistributedVirtualSwitch#vsan_share_count}
        :param vsan_share_level: The allocation level for the vsan traffic class. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vsan_share_level DistributedVirtualSwitch#vsan_share_level}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DistributedVirtualSwitchConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument datacenter_id", value=datacenter_id, expected_type=type_hints["datacenter_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument active_uplinks", value=active_uplinks, expected_type=type_hints["active_uplinks"])
            check_type(argname="argument allow_forged_transmits", value=allow_forged_transmits, expected_type=type_hints["allow_forged_transmits"])
            check_type(argname="argument allow_mac_changes", value=allow_mac_changes, expected_type=type_hints["allow_mac_changes"])
            check_type(argname="argument allow_promiscuous", value=allow_promiscuous, expected_type=type_hints["allow_promiscuous"])
            check_type(argname="argument backupnfc_maximum_mbit", value=backupnfc_maximum_mbit, expected_type=type_hints["backupnfc_maximum_mbit"])
            check_type(argname="argument backupnfc_reservation_mbit", value=backupnfc_reservation_mbit, expected_type=type_hints["backupnfc_reservation_mbit"])
            check_type(argname="argument backupnfc_share_count", value=backupnfc_share_count, expected_type=type_hints["backupnfc_share_count"])
            check_type(argname="argument backupnfc_share_level", value=backupnfc_share_level, expected_type=type_hints["backupnfc_share_level"])
            check_type(argname="argument block_all_ports", value=block_all_ports, expected_type=type_hints["block_all_ports"])
            check_type(argname="argument check_beacon", value=check_beacon, expected_type=type_hints["check_beacon"])
            check_type(argname="argument contact_detail", value=contact_detail, expected_type=type_hints["contact_detail"])
            check_type(argname="argument contact_name", value=contact_name, expected_type=type_hints["contact_name"])
            check_type(argname="argument custom_attributes", value=custom_attributes, expected_type=type_hints["custom_attributes"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument directpath_gen2_allowed", value=directpath_gen2_allowed, expected_type=type_hints["directpath_gen2_allowed"])
            check_type(argname="argument egress_shaping_average_bandwidth", value=egress_shaping_average_bandwidth, expected_type=type_hints["egress_shaping_average_bandwidth"])
            check_type(argname="argument egress_shaping_burst_size", value=egress_shaping_burst_size, expected_type=type_hints["egress_shaping_burst_size"])
            check_type(argname="argument egress_shaping_enabled", value=egress_shaping_enabled, expected_type=type_hints["egress_shaping_enabled"])
            check_type(argname="argument egress_shaping_peak_bandwidth", value=egress_shaping_peak_bandwidth, expected_type=type_hints["egress_shaping_peak_bandwidth"])
            check_type(argname="argument failback", value=failback, expected_type=type_hints["failback"])
            check_type(argname="argument faulttolerance_maximum_mbit", value=faulttolerance_maximum_mbit, expected_type=type_hints["faulttolerance_maximum_mbit"])
            check_type(argname="argument faulttolerance_reservation_mbit", value=faulttolerance_reservation_mbit, expected_type=type_hints["faulttolerance_reservation_mbit"])
            check_type(argname="argument faulttolerance_share_count", value=faulttolerance_share_count, expected_type=type_hints["faulttolerance_share_count"])
            check_type(argname="argument faulttolerance_share_level", value=faulttolerance_share_level, expected_type=type_hints["faulttolerance_share_level"])
            check_type(argname="argument folder", value=folder, expected_type=type_hints["folder"])
            check_type(argname="argument hbr_maximum_mbit", value=hbr_maximum_mbit, expected_type=type_hints["hbr_maximum_mbit"])
            check_type(argname="argument hbr_reservation_mbit", value=hbr_reservation_mbit, expected_type=type_hints["hbr_reservation_mbit"])
            check_type(argname="argument hbr_share_count", value=hbr_share_count, expected_type=type_hints["hbr_share_count"])
            check_type(argname="argument hbr_share_level", value=hbr_share_level, expected_type=type_hints["hbr_share_level"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ignore_other_pvlan_mappings", value=ignore_other_pvlan_mappings, expected_type=type_hints["ignore_other_pvlan_mappings"])
            check_type(argname="argument ingress_shaping_average_bandwidth", value=ingress_shaping_average_bandwidth, expected_type=type_hints["ingress_shaping_average_bandwidth"])
            check_type(argname="argument ingress_shaping_burst_size", value=ingress_shaping_burst_size, expected_type=type_hints["ingress_shaping_burst_size"])
            check_type(argname="argument ingress_shaping_enabled", value=ingress_shaping_enabled, expected_type=type_hints["ingress_shaping_enabled"])
            check_type(argname="argument ingress_shaping_peak_bandwidth", value=ingress_shaping_peak_bandwidth, expected_type=type_hints["ingress_shaping_peak_bandwidth"])
            check_type(argname="argument ipv4_address", value=ipv4_address, expected_type=type_hints["ipv4_address"])
            check_type(argname="argument iscsi_maximum_mbit", value=iscsi_maximum_mbit, expected_type=type_hints["iscsi_maximum_mbit"])
            check_type(argname="argument iscsi_reservation_mbit", value=iscsi_reservation_mbit, expected_type=type_hints["iscsi_reservation_mbit"])
            check_type(argname="argument iscsi_share_count", value=iscsi_share_count, expected_type=type_hints["iscsi_share_count"])
            check_type(argname="argument iscsi_share_level", value=iscsi_share_level, expected_type=type_hints["iscsi_share_level"])
            check_type(argname="argument lacp_api_version", value=lacp_api_version, expected_type=type_hints["lacp_api_version"])
            check_type(argname="argument lacp_enabled", value=lacp_enabled, expected_type=type_hints["lacp_enabled"])
            check_type(argname="argument lacp_mode", value=lacp_mode, expected_type=type_hints["lacp_mode"])
            check_type(argname="argument link_discovery_operation", value=link_discovery_operation, expected_type=type_hints["link_discovery_operation"])
            check_type(argname="argument link_discovery_protocol", value=link_discovery_protocol, expected_type=type_hints["link_discovery_protocol"])
            check_type(argname="argument management_maximum_mbit", value=management_maximum_mbit, expected_type=type_hints["management_maximum_mbit"])
            check_type(argname="argument management_reservation_mbit", value=management_reservation_mbit, expected_type=type_hints["management_reservation_mbit"])
            check_type(argname="argument management_share_count", value=management_share_count, expected_type=type_hints["management_share_count"])
            check_type(argname="argument management_share_level", value=management_share_level, expected_type=type_hints["management_share_level"])
            check_type(argname="argument max_mtu", value=max_mtu, expected_type=type_hints["max_mtu"])
            check_type(argname="argument multicast_filtering_mode", value=multicast_filtering_mode, expected_type=type_hints["multicast_filtering_mode"])
            check_type(argname="argument netflow_active_flow_timeout", value=netflow_active_flow_timeout, expected_type=type_hints["netflow_active_flow_timeout"])
            check_type(argname="argument netflow_collector_ip_address", value=netflow_collector_ip_address, expected_type=type_hints["netflow_collector_ip_address"])
            check_type(argname="argument netflow_collector_port", value=netflow_collector_port, expected_type=type_hints["netflow_collector_port"])
            check_type(argname="argument netflow_enabled", value=netflow_enabled, expected_type=type_hints["netflow_enabled"])
            check_type(argname="argument netflow_idle_flow_timeout", value=netflow_idle_flow_timeout, expected_type=type_hints["netflow_idle_flow_timeout"])
            check_type(argname="argument netflow_internal_flows_only", value=netflow_internal_flows_only, expected_type=type_hints["netflow_internal_flows_only"])
            check_type(argname="argument netflow_observation_domain_id", value=netflow_observation_domain_id, expected_type=type_hints["netflow_observation_domain_id"])
            check_type(argname="argument netflow_sampling_rate", value=netflow_sampling_rate, expected_type=type_hints["netflow_sampling_rate"])
            check_type(argname="argument network_resource_control_enabled", value=network_resource_control_enabled, expected_type=type_hints["network_resource_control_enabled"])
            check_type(argname="argument network_resource_control_version", value=network_resource_control_version, expected_type=type_hints["network_resource_control_version"])
            check_type(argname="argument nfs_maximum_mbit", value=nfs_maximum_mbit, expected_type=type_hints["nfs_maximum_mbit"])
            check_type(argname="argument nfs_reservation_mbit", value=nfs_reservation_mbit, expected_type=type_hints["nfs_reservation_mbit"])
            check_type(argname="argument nfs_share_count", value=nfs_share_count, expected_type=type_hints["nfs_share_count"])
            check_type(argname="argument nfs_share_level", value=nfs_share_level, expected_type=type_hints["nfs_share_level"])
            check_type(argname="argument notify_switches", value=notify_switches, expected_type=type_hints["notify_switches"])
            check_type(argname="argument port_private_secondary_vlan_id", value=port_private_secondary_vlan_id, expected_type=type_hints["port_private_secondary_vlan_id"])
            check_type(argname="argument pvlan_mapping", value=pvlan_mapping, expected_type=type_hints["pvlan_mapping"])
            check_type(argname="argument standby_uplinks", value=standby_uplinks, expected_type=type_hints["standby_uplinks"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument teaming_policy", value=teaming_policy, expected_type=type_hints["teaming_policy"])
            check_type(argname="argument tx_uplink", value=tx_uplink, expected_type=type_hints["tx_uplink"])
            check_type(argname="argument uplinks", value=uplinks, expected_type=type_hints["uplinks"])
            check_type(argname="argument vdp_maximum_mbit", value=vdp_maximum_mbit, expected_type=type_hints["vdp_maximum_mbit"])
            check_type(argname="argument vdp_reservation_mbit", value=vdp_reservation_mbit, expected_type=type_hints["vdp_reservation_mbit"])
            check_type(argname="argument vdp_share_count", value=vdp_share_count, expected_type=type_hints["vdp_share_count"])
            check_type(argname="argument vdp_share_level", value=vdp_share_level, expected_type=type_hints["vdp_share_level"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument virtualmachine_maximum_mbit", value=virtualmachine_maximum_mbit, expected_type=type_hints["virtualmachine_maximum_mbit"])
            check_type(argname="argument virtualmachine_reservation_mbit", value=virtualmachine_reservation_mbit, expected_type=type_hints["virtualmachine_reservation_mbit"])
            check_type(argname="argument virtualmachine_share_count", value=virtualmachine_share_count, expected_type=type_hints["virtualmachine_share_count"])
            check_type(argname="argument virtualmachine_share_level", value=virtualmachine_share_level, expected_type=type_hints["virtualmachine_share_level"])
            check_type(argname="argument vlan_id", value=vlan_id, expected_type=type_hints["vlan_id"])
            check_type(argname="argument vlan_range", value=vlan_range, expected_type=type_hints["vlan_range"])
            check_type(argname="argument vmotion_maximum_mbit", value=vmotion_maximum_mbit, expected_type=type_hints["vmotion_maximum_mbit"])
            check_type(argname="argument vmotion_reservation_mbit", value=vmotion_reservation_mbit, expected_type=type_hints["vmotion_reservation_mbit"])
            check_type(argname="argument vmotion_share_count", value=vmotion_share_count, expected_type=type_hints["vmotion_share_count"])
            check_type(argname="argument vmotion_share_level", value=vmotion_share_level, expected_type=type_hints["vmotion_share_level"])
            check_type(argname="argument vsan_maximum_mbit", value=vsan_maximum_mbit, expected_type=type_hints["vsan_maximum_mbit"])
            check_type(argname="argument vsan_reservation_mbit", value=vsan_reservation_mbit, expected_type=type_hints["vsan_reservation_mbit"])
            check_type(argname="argument vsan_share_count", value=vsan_share_count, expected_type=type_hints["vsan_share_count"])
            check_type(argname="argument vsan_share_level", value=vsan_share_level, expected_type=type_hints["vsan_share_level"])
        self._values: typing.Dict[str, typing.Any] = {
            "datacenter_id": datacenter_id,
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
        if backupnfc_maximum_mbit is not None:
            self._values["backupnfc_maximum_mbit"] = backupnfc_maximum_mbit
        if backupnfc_reservation_mbit is not None:
            self._values["backupnfc_reservation_mbit"] = backupnfc_reservation_mbit
        if backupnfc_share_count is not None:
            self._values["backupnfc_share_count"] = backupnfc_share_count
        if backupnfc_share_level is not None:
            self._values["backupnfc_share_level"] = backupnfc_share_level
        if block_all_ports is not None:
            self._values["block_all_ports"] = block_all_ports
        if check_beacon is not None:
            self._values["check_beacon"] = check_beacon
        if contact_detail is not None:
            self._values["contact_detail"] = contact_detail
        if contact_name is not None:
            self._values["contact_name"] = contact_name
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
        if faulttolerance_maximum_mbit is not None:
            self._values["faulttolerance_maximum_mbit"] = faulttolerance_maximum_mbit
        if faulttolerance_reservation_mbit is not None:
            self._values["faulttolerance_reservation_mbit"] = faulttolerance_reservation_mbit
        if faulttolerance_share_count is not None:
            self._values["faulttolerance_share_count"] = faulttolerance_share_count
        if faulttolerance_share_level is not None:
            self._values["faulttolerance_share_level"] = faulttolerance_share_level
        if folder is not None:
            self._values["folder"] = folder
        if hbr_maximum_mbit is not None:
            self._values["hbr_maximum_mbit"] = hbr_maximum_mbit
        if hbr_reservation_mbit is not None:
            self._values["hbr_reservation_mbit"] = hbr_reservation_mbit
        if hbr_share_count is not None:
            self._values["hbr_share_count"] = hbr_share_count
        if hbr_share_level is not None:
            self._values["hbr_share_level"] = hbr_share_level
        if host is not None:
            self._values["host"] = host
        if id is not None:
            self._values["id"] = id
        if ignore_other_pvlan_mappings is not None:
            self._values["ignore_other_pvlan_mappings"] = ignore_other_pvlan_mappings
        if ingress_shaping_average_bandwidth is not None:
            self._values["ingress_shaping_average_bandwidth"] = ingress_shaping_average_bandwidth
        if ingress_shaping_burst_size is not None:
            self._values["ingress_shaping_burst_size"] = ingress_shaping_burst_size
        if ingress_shaping_enabled is not None:
            self._values["ingress_shaping_enabled"] = ingress_shaping_enabled
        if ingress_shaping_peak_bandwidth is not None:
            self._values["ingress_shaping_peak_bandwidth"] = ingress_shaping_peak_bandwidth
        if ipv4_address is not None:
            self._values["ipv4_address"] = ipv4_address
        if iscsi_maximum_mbit is not None:
            self._values["iscsi_maximum_mbit"] = iscsi_maximum_mbit
        if iscsi_reservation_mbit is not None:
            self._values["iscsi_reservation_mbit"] = iscsi_reservation_mbit
        if iscsi_share_count is not None:
            self._values["iscsi_share_count"] = iscsi_share_count
        if iscsi_share_level is not None:
            self._values["iscsi_share_level"] = iscsi_share_level
        if lacp_api_version is not None:
            self._values["lacp_api_version"] = lacp_api_version
        if lacp_enabled is not None:
            self._values["lacp_enabled"] = lacp_enabled
        if lacp_mode is not None:
            self._values["lacp_mode"] = lacp_mode
        if link_discovery_operation is not None:
            self._values["link_discovery_operation"] = link_discovery_operation
        if link_discovery_protocol is not None:
            self._values["link_discovery_protocol"] = link_discovery_protocol
        if management_maximum_mbit is not None:
            self._values["management_maximum_mbit"] = management_maximum_mbit
        if management_reservation_mbit is not None:
            self._values["management_reservation_mbit"] = management_reservation_mbit
        if management_share_count is not None:
            self._values["management_share_count"] = management_share_count
        if management_share_level is not None:
            self._values["management_share_level"] = management_share_level
        if max_mtu is not None:
            self._values["max_mtu"] = max_mtu
        if multicast_filtering_mode is not None:
            self._values["multicast_filtering_mode"] = multicast_filtering_mode
        if netflow_active_flow_timeout is not None:
            self._values["netflow_active_flow_timeout"] = netflow_active_flow_timeout
        if netflow_collector_ip_address is not None:
            self._values["netflow_collector_ip_address"] = netflow_collector_ip_address
        if netflow_collector_port is not None:
            self._values["netflow_collector_port"] = netflow_collector_port
        if netflow_enabled is not None:
            self._values["netflow_enabled"] = netflow_enabled
        if netflow_idle_flow_timeout is not None:
            self._values["netflow_idle_flow_timeout"] = netflow_idle_flow_timeout
        if netflow_internal_flows_only is not None:
            self._values["netflow_internal_flows_only"] = netflow_internal_flows_only
        if netflow_observation_domain_id is not None:
            self._values["netflow_observation_domain_id"] = netflow_observation_domain_id
        if netflow_sampling_rate is not None:
            self._values["netflow_sampling_rate"] = netflow_sampling_rate
        if network_resource_control_enabled is not None:
            self._values["network_resource_control_enabled"] = network_resource_control_enabled
        if network_resource_control_version is not None:
            self._values["network_resource_control_version"] = network_resource_control_version
        if nfs_maximum_mbit is not None:
            self._values["nfs_maximum_mbit"] = nfs_maximum_mbit
        if nfs_reservation_mbit is not None:
            self._values["nfs_reservation_mbit"] = nfs_reservation_mbit
        if nfs_share_count is not None:
            self._values["nfs_share_count"] = nfs_share_count
        if nfs_share_level is not None:
            self._values["nfs_share_level"] = nfs_share_level
        if notify_switches is not None:
            self._values["notify_switches"] = notify_switches
        if port_private_secondary_vlan_id is not None:
            self._values["port_private_secondary_vlan_id"] = port_private_secondary_vlan_id
        if pvlan_mapping is not None:
            self._values["pvlan_mapping"] = pvlan_mapping
        if standby_uplinks is not None:
            self._values["standby_uplinks"] = standby_uplinks
        if tags is not None:
            self._values["tags"] = tags
        if teaming_policy is not None:
            self._values["teaming_policy"] = teaming_policy
        if tx_uplink is not None:
            self._values["tx_uplink"] = tx_uplink
        if uplinks is not None:
            self._values["uplinks"] = uplinks
        if vdp_maximum_mbit is not None:
            self._values["vdp_maximum_mbit"] = vdp_maximum_mbit
        if vdp_reservation_mbit is not None:
            self._values["vdp_reservation_mbit"] = vdp_reservation_mbit
        if vdp_share_count is not None:
            self._values["vdp_share_count"] = vdp_share_count
        if vdp_share_level is not None:
            self._values["vdp_share_level"] = vdp_share_level
        if version is not None:
            self._values["version"] = version
        if virtualmachine_maximum_mbit is not None:
            self._values["virtualmachine_maximum_mbit"] = virtualmachine_maximum_mbit
        if virtualmachine_reservation_mbit is not None:
            self._values["virtualmachine_reservation_mbit"] = virtualmachine_reservation_mbit
        if virtualmachine_share_count is not None:
            self._values["virtualmachine_share_count"] = virtualmachine_share_count
        if virtualmachine_share_level is not None:
            self._values["virtualmachine_share_level"] = virtualmachine_share_level
        if vlan_id is not None:
            self._values["vlan_id"] = vlan_id
        if vlan_range is not None:
            self._values["vlan_range"] = vlan_range
        if vmotion_maximum_mbit is not None:
            self._values["vmotion_maximum_mbit"] = vmotion_maximum_mbit
        if vmotion_reservation_mbit is not None:
            self._values["vmotion_reservation_mbit"] = vmotion_reservation_mbit
        if vmotion_share_count is not None:
            self._values["vmotion_share_count"] = vmotion_share_count
        if vmotion_share_level is not None:
            self._values["vmotion_share_level"] = vmotion_share_level
        if vsan_maximum_mbit is not None:
            self._values["vsan_maximum_mbit"] = vsan_maximum_mbit
        if vsan_reservation_mbit is not None:
            self._values["vsan_reservation_mbit"] = vsan_reservation_mbit
        if vsan_share_count is not None:
            self._values["vsan_share_count"] = vsan_share_count
        if vsan_share_level is not None:
            self._values["vsan_share_level"] = vsan_share_level

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
    def datacenter_id(self) -> builtins.str:
        '''The ID of the datacenter to create this virtual switch in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#datacenter_id DistributedVirtualSwitch#datacenter_id}
        '''
        result = self._values.get("datacenter_id")
        assert result is not None, "Required property 'datacenter_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for the DVS. Must be unique in the folder that it is being created in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#name DistributedVirtualSwitch#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active_uplinks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of active uplinks used for load balancing, matching the names of the uplinks assigned in the DVS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#active_uplinks DistributedVirtualSwitch#active_uplinks}
        '''
        result = self._values.get("active_uplinks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_forged_transmits(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than that of its own.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#allow_forged_transmits DistributedVirtualSwitch#allow_forged_transmits}
        '''
        result = self._values.get("allow_forged_transmits")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_mac_changes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Controls whether or not the Media Access Control (MAC) address can be changed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#allow_mac_changes DistributedVirtualSwitch#allow_mac_changes}
        '''
        result = self._values.get("allow_mac_changes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_promiscuous(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable promiscuous mode on the network.

        This flag indicates whether or not all traffic is seen on a given port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#allow_promiscuous DistributedVirtualSwitch#allow_promiscuous}
        '''
        result = self._values.get("allow_promiscuous")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def backupnfc_maximum_mbit(self) -> typing.Optional[jsii.Number]:
        '''The maximum allowed usage for the backupNfc traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#backupnfc_maximum_mbit DistributedVirtualSwitch#backupnfc_maximum_mbit}
        '''
        result = self._values.get("backupnfc_maximum_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def backupnfc_reservation_mbit(self) -> typing.Optional[jsii.Number]:
        '''The amount of guaranteed bandwidth for the backupNfc traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#backupnfc_reservation_mbit DistributedVirtualSwitch#backupnfc_reservation_mbit}
        '''
        result = self._values.get("backupnfc_reservation_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def backupnfc_share_count(self) -> typing.Optional[jsii.Number]:
        '''The amount of shares to allocate to the backupNfc traffic class for a custom share level.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#backupnfc_share_count DistributedVirtualSwitch#backupnfc_share_count}
        '''
        result = self._values.get("backupnfc_share_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def backupnfc_share_level(self) -> typing.Optional[builtins.str]:
        '''The allocation level for the backupNfc traffic class. Can be one of high, low, normal, or custom.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#backupnfc_share_level DistributedVirtualSwitch#backupnfc_share_level}
        '''
        result = self._values.get("backupnfc_share_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def block_all_ports(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether to block all ports by default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#block_all_ports DistributedVirtualSwitch#block_all_ports}
        '''
        result = self._values.get("block_all_ports")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def check_beacon(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable beacon probing on the ports this policy applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#check_beacon DistributedVirtualSwitch#check_beacon}
        '''
        result = self._values.get("check_beacon")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def contact_detail(self) -> typing.Optional[builtins.str]:
        '''The contact detail for this DVS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#contact_detail DistributedVirtualSwitch#contact_detail}
        '''
        result = self._values.get("contact_detail")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def contact_name(self) -> typing.Optional[builtins.str]:
        '''The contact name for this DVS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#contact_name DistributedVirtualSwitch#contact_name}
        '''
        result = self._values.get("contact_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of custom attributes to set on this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#custom_attributes DistributedVirtualSwitch#custom_attributes}
        '''
        result = self._values.get("custom_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the DVS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#description DistributedVirtualSwitch#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directpath_gen2_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow VMDirectPath Gen2 on the ports this policy applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#directpath_gen2_allowed DistributedVirtualSwitch#directpath_gen2_allowed}
        '''
        result = self._values.get("directpath_gen2_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def egress_shaping_average_bandwidth(self) -> typing.Optional[jsii.Number]:
        '''The average egress bandwidth in bits per second if egress shaping is enabled on the port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#egress_shaping_average_bandwidth DistributedVirtualSwitch#egress_shaping_average_bandwidth}
        '''
        result = self._values.get("egress_shaping_average_bandwidth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def egress_shaping_burst_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum egress burst size allowed in bytes if egress shaping is enabled on the port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#egress_shaping_burst_size DistributedVirtualSwitch#egress_shaping_burst_size}
        '''
        result = self._values.get("egress_shaping_burst_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def egress_shaping_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''True if the traffic shaper is enabled for egress traffic on the port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#egress_shaping_enabled DistributedVirtualSwitch#egress_shaping_enabled}
        '''
        result = self._values.get("egress_shaping_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def egress_shaping_peak_bandwidth(self) -> typing.Optional[jsii.Number]:
        '''The peak egress bandwidth during bursts in bits per second if egress traffic shaping is enabled on the port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#egress_shaping_peak_bandwidth DistributedVirtualSwitch#egress_shaping_peak_bandwidth}
        '''
        result = self._values.get("egress_shaping_peak_bandwidth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def failback(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#failback DistributedVirtualSwitch#failback}
        '''
        result = self._values.get("failback")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def faulttolerance_maximum_mbit(self) -> typing.Optional[jsii.Number]:
        '''The maximum allowed usage for the faultTolerance traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#faulttolerance_maximum_mbit DistributedVirtualSwitch#faulttolerance_maximum_mbit}
        '''
        result = self._values.get("faulttolerance_maximum_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def faulttolerance_reservation_mbit(self) -> typing.Optional[jsii.Number]:
        '''The amount of guaranteed bandwidth for the faultTolerance traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#faulttolerance_reservation_mbit DistributedVirtualSwitch#faulttolerance_reservation_mbit}
        '''
        result = self._values.get("faulttolerance_reservation_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def faulttolerance_share_count(self) -> typing.Optional[jsii.Number]:
        '''The amount of shares to allocate to the faultTolerance traffic class for a custom share level.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#faulttolerance_share_count DistributedVirtualSwitch#faulttolerance_share_count}
        '''
        result = self._values.get("faulttolerance_share_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def faulttolerance_share_level(self) -> typing.Optional[builtins.str]:
        '''The allocation level for the faultTolerance traffic class. Can be one of high, low, normal, or custom.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#faulttolerance_share_level DistributedVirtualSwitch#faulttolerance_share_level}
        '''
        result = self._values.get("faulttolerance_share_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def folder(self) -> typing.Optional[builtins.str]:
        '''The folder to create this virtual switch in, relative to the datacenter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#folder DistributedVirtualSwitch#folder}
        '''
        result = self._values.get("folder")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hbr_maximum_mbit(self) -> typing.Optional[jsii.Number]:
        '''The maximum allowed usage for the hbr traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#hbr_maximum_mbit DistributedVirtualSwitch#hbr_maximum_mbit}
        '''
        result = self._values.get("hbr_maximum_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def hbr_reservation_mbit(self) -> typing.Optional[jsii.Number]:
        '''The amount of guaranteed bandwidth for the hbr traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#hbr_reservation_mbit DistributedVirtualSwitch#hbr_reservation_mbit}
        '''
        result = self._values.get("hbr_reservation_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def hbr_share_count(self) -> typing.Optional[jsii.Number]:
        '''The amount of shares to allocate to the hbr traffic class for a custom share level.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#hbr_share_count DistributedVirtualSwitch#hbr_share_count}
        '''
        result = self._values.get("hbr_share_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def hbr_share_level(self) -> typing.Optional[builtins.str]:
        '''The allocation level for the hbr traffic class. Can be one of high, low, normal, or custom.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#hbr_share_level DistributedVirtualSwitch#hbr_share_level}
        '''
        result = self._values.get("hbr_share_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DistributedVirtualSwitchHost"]]]:
        '''host block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#host DistributedVirtualSwitch#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DistributedVirtualSwitchHost"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#id DistributedVirtualSwitch#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_other_pvlan_mappings(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to ignore existing PVLAN mappings not managed by this resource. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#ignore_other_pvlan_mappings DistributedVirtualSwitch#ignore_other_pvlan_mappings}
        '''
        result = self._values.get("ignore_other_pvlan_mappings")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ingress_shaping_average_bandwidth(self) -> typing.Optional[jsii.Number]:
        '''The average ingress bandwidth in bits per second if ingress shaping is enabled on the port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#ingress_shaping_average_bandwidth DistributedVirtualSwitch#ingress_shaping_average_bandwidth}
        '''
        result = self._values.get("ingress_shaping_average_bandwidth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ingress_shaping_burst_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum ingress burst size allowed in bytes if ingress shaping is enabled on the port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#ingress_shaping_burst_size DistributedVirtualSwitch#ingress_shaping_burst_size}
        '''
        result = self._values.get("ingress_shaping_burst_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ingress_shaping_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''True if the traffic shaper is enabled for ingress traffic on the port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#ingress_shaping_enabled DistributedVirtualSwitch#ingress_shaping_enabled}
        '''
        result = self._values.get("ingress_shaping_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ingress_shaping_peak_bandwidth(self) -> typing.Optional[jsii.Number]:
        '''The peak ingress bandwidth during bursts in bits per second if ingress traffic shaping is enabled on the port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#ingress_shaping_peak_bandwidth DistributedVirtualSwitch#ingress_shaping_peak_bandwidth}
        '''
        result = self._values.get("ingress_shaping_peak_bandwidth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ipv4_address(self) -> typing.Optional[builtins.str]:
        '''The IPv4 address of the switch.

        This can be used to see the DVS as a unique device with NetFlow.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#ipv4_address DistributedVirtualSwitch#ipv4_address}
        '''
        result = self._values.get("ipv4_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iscsi_maximum_mbit(self) -> typing.Optional[jsii.Number]:
        '''The maximum allowed usage for the iSCSI traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#iscsi_maximum_mbit DistributedVirtualSwitch#iscsi_maximum_mbit}
        '''
        result = self._values.get("iscsi_maximum_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def iscsi_reservation_mbit(self) -> typing.Optional[jsii.Number]:
        '''The amount of guaranteed bandwidth for the iSCSI traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#iscsi_reservation_mbit DistributedVirtualSwitch#iscsi_reservation_mbit}
        '''
        result = self._values.get("iscsi_reservation_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def iscsi_share_count(self) -> typing.Optional[jsii.Number]:
        '''The amount of shares to allocate to the iSCSI traffic class for a custom share level.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#iscsi_share_count DistributedVirtualSwitch#iscsi_share_count}
        '''
        result = self._values.get("iscsi_share_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def iscsi_share_level(self) -> typing.Optional[builtins.str]:
        '''The allocation level for the iSCSI traffic class. Can be one of high, low, normal, or custom.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#iscsi_share_level DistributedVirtualSwitch#iscsi_share_level}
        '''
        result = self._values.get("iscsi_share_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lacp_api_version(self) -> typing.Optional[builtins.str]:
        '''The Link Aggregation Control Protocol group version in the switch. Can be one of singleLag or multipleLag.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#lacp_api_version DistributedVirtualSwitch#lacp_api_version}
        '''
        result = self._values.get("lacp_api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lacp_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not to enable LACP on all uplink ports.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#lacp_enabled DistributedVirtualSwitch#lacp_enabled}
        '''
        result = self._values.get("lacp_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def lacp_mode(self) -> typing.Optional[builtins.str]:
        '''The uplink LACP mode to use. Can be one of active or passive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#lacp_mode DistributedVirtualSwitch#lacp_mode}
        '''
        result = self._values.get("lacp_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def link_discovery_operation(self) -> typing.Optional[builtins.str]:
        '''Whether to advertise or listen for link discovery. Valid values are advertise, both, listen, and none.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#link_discovery_operation DistributedVirtualSwitch#link_discovery_operation}
        '''
        result = self._values.get("link_discovery_operation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def link_discovery_protocol(self) -> typing.Optional[builtins.str]:
        '''The discovery protocol type. Valid values are cdp and lldp.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#link_discovery_protocol DistributedVirtualSwitch#link_discovery_protocol}
        '''
        result = self._values.get("link_discovery_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def management_maximum_mbit(self) -> typing.Optional[jsii.Number]:
        '''The maximum allowed usage for the management traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#management_maximum_mbit DistributedVirtualSwitch#management_maximum_mbit}
        '''
        result = self._values.get("management_maximum_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def management_reservation_mbit(self) -> typing.Optional[jsii.Number]:
        '''The amount of guaranteed bandwidth for the management traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#management_reservation_mbit DistributedVirtualSwitch#management_reservation_mbit}
        '''
        result = self._values.get("management_reservation_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def management_share_count(self) -> typing.Optional[jsii.Number]:
        '''The amount of shares to allocate to the management traffic class for a custom share level.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#management_share_count DistributedVirtualSwitch#management_share_count}
        '''
        result = self._values.get("management_share_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def management_share_level(self) -> typing.Optional[builtins.str]:
        '''The allocation level for the management traffic class. Can be one of high, low, normal, or custom.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#management_share_level DistributedVirtualSwitch#management_share_level}
        '''
        result = self._values.get("management_share_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_mtu(self) -> typing.Optional[jsii.Number]:
        '''The maximum MTU on the switch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#max_mtu DistributedVirtualSwitch#max_mtu}
        '''
        result = self._values.get("max_mtu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def multicast_filtering_mode(self) -> typing.Optional[builtins.str]:
        '''The multicast filtering mode on the switch. Can be one of legacyFiltering, or snooping.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#multicast_filtering_mode DistributedVirtualSwitch#multicast_filtering_mode}
        '''
        result = self._values.get("multicast_filtering_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def netflow_active_flow_timeout(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds after which active flows are forced to be exported to the collector.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_active_flow_timeout DistributedVirtualSwitch#netflow_active_flow_timeout}
        '''
        result = self._values.get("netflow_active_flow_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def netflow_collector_ip_address(self) -> typing.Optional[builtins.str]:
        '''IP address for the netflow collector, using IPv4 or IPv6.

        IPv6 is supported in vSphere Distributed Switch Version 6.0 or later.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_collector_ip_address DistributedVirtualSwitch#netflow_collector_ip_address}
        '''
        result = self._values.get("netflow_collector_ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def netflow_collector_port(self) -> typing.Optional[jsii.Number]:
        '''The port for the netflow collector.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_collector_port DistributedVirtualSwitch#netflow_collector_port}
        '''
        result = self._values.get("netflow_collector_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def netflow_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether to enable netflow on all ports.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_enabled DistributedVirtualSwitch#netflow_enabled}
        '''
        result = self._values.get("netflow_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def netflow_idle_flow_timeout(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds after which idle flows are forced to be exported to the collector.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_idle_flow_timeout DistributedVirtualSwitch#netflow_idle_flow_timeout}
        '''
        result = self._values.get("netflow_idle_flow_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def netflow_internal_flows_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to limit analysis to traffic that has both source and destination served by the same host.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_internal_flows_only DistributedVirtualSwitch#netflow_internal_flows_only}
        '''
        result = self._values.get("netflow_internal_flows_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def netflow_observation_domain_id(self) -> typing.Optional[jsii.Number]:
        '''The observation Domain ID for the netflow collector.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_observation_domain_id DistributedVirtualSwitch#netflow_observation_domain_id}
        '''
        result = self._values.get("netflow_observation_domain_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def netflow_sampling_rate(self) -> typing.Optional[jsii.Number]:
        '''The ratio of total number of packets to the number of packets analyzed.

        Set to 0 to disable sampling, meaning that all packets are analyzed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#netflow_sampling_rate DistributedVirtualSwitch#netflow_sampling_rate}
        '''
        result = self._values.get("netflow_sampling_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def network_resource_control_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not to enable network resource control, enabling advanced traffic shaping and resource control features.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#network_resource_control_enabled DistributedVirtualSwitch#network_resource_control_enabled}
        '''
        result = self._values.get("network_resource_control_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def network_resource_control_version(self) -> typing.Optional[builtins.str]:
        '''The network I/O control version to use. Can be one of version2 or version3.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#network_resource_control_version DistributedVirtualSwitch#network_resource_control_version}
        '''
        result = self._values.get("network_resource_control_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nfs_maximum_mbit(self) -> typing.Optional[jsii.Number]:
        '''The maximum allowed usage for the nfs traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#nfs_maximum_mbit DistributedVirtualSwitch#nfs_maximum_mbit}
        '''
        result = self._values.get("nfs_maximum_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def nfs_reservation_mbit(self) -> typing.Optional[jsii.Number]:
        '''The amount of guaranteed bandwidth for the nfs traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#nfs_reservation_mbit DistributedVirtualSwitch#nfs_reservation_mbit}
        '''
        result = self._values.get("nfs_reservation_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def nfs_share_count(self) -> typing.Optional[jsii.Number]:
        '''The amount of shares to allocate to the nfs traffic class for a custom share level.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#nfs_share_count DistributedVirtualSwitch#nfs_share_count}
        '''
        result = self._values.get("nfs_share_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def nfs_share_level(self) -> typing.Optional[builtins.str]:
        '''The allocation level for the nfs traffic class. Can be one of high, low, normal, or custom.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#nfs_share_level DistributedVirtualSwitch#nfs_share_level}
        '''
        result = self._values.get("nfs_share_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notify_switches(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#notify_switches DistributedVirtualSwitch#notify_switches}
        '''
        result = self._values.get("notify_switches")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def port_private_secondary_vlan_id(self) -> typing.Optional[jsii.Number]:
        '''The secondary VLAN ID for this port.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#port_private_secondary_vlan_id DistributedVirtualSwitch#port_private_secondary_vlan_id}
        '''
        result = self._values.get("port_private_secondary_vlan_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pvlan_mapping(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DistributedVirtualSwitchPvlanMapping"]]]:
        '''pvlan_mapping block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#pvlan_mapping DistributedVirtualSwitch#pvlan_mapping}
        '''
        result = self._values.get("pvlan_mapping")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DistributedVirtualSwitchPvlanMapping"]]], result)

    @builtins.property
    def standby_uplinks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of standby uplinks used for load balancing, matching the names of the uplinks assigned in the DVS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#standby_uplinks DistributedVirtualSwitch#standby_uplinks}
        '''
        result = self._values.get("standby_uplinks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of tag IDs to apply to this object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#tags DistributedVirtualSwitch#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def teaming_policy(self) -> typing.Optional[builtins.str]:
        '''The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, failover_explicit, or loadbalance_loadbased.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#teaming_policy DistributedVirtualSwitch#teaming_policy}
        '''
        result = self._values.get("teaming_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tx_uplink(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, a copy of packets sent to the switch will always be forwarded to an uplink in addition to the regular packet forwarded done by the switch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#tx_uplink DistributedVirtualSwitch#tx_uplink}
        '''
        result = self._values.get("tx_uplink")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def uplinks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of uplink ports.

        The contents of this list control both the uplink count and names of the uplinks on the DVS across hosts.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#uplinks DistributedVirtualSwitch#uplinks}
        '''
        result = self._values.get("uplinks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def vdp_maximum_mbit(self) -> typing.Optional[jsii.Number]:
        '''The maximum allowed usage for the vdp traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vdp_maximum_mbit DistributedVirtualSwitch#vdp_maximum_mbit}
        '''
        result = self._values.get("vdp_maximum_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vdp_reservation_mbit(self) -> typing.Optional[jsii.Number]:
        '''The amount of guaranteed bandwidth for the vdp traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vdp_reservation_mbit DistributedVirtualSwitch#vdp_reservation_mbit}
        '''
        result = self._values.get("vdp_reservation_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vdp_share_count(self) -> typing.Optional[jsii.Number]:
        '''The amount of shares to allocate to the vdp traffic class for a custom share level.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vdp_share_count DistributedVirtualSwitch#vdp_share_count}
        '''
        result = self._values.get("vdp_share_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vdp_share_level(self) -> typing.Optional[builtins.str]:
        '''The allocation level for the vdp traffic class. Can be one of high, low, normal, or custom.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vdp_share_level DistributedVirtualSwitch#vdp_share_level}
        '''
        result = self._values.get("vdp_share_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''The version of this virtual switch. Allowed versions are 7.0.3, 7.0.0, 6.6.0, 6.5.0, 6.0.0, 5.5.0, 5.1.0, and 5.0.0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#version DistributedVirtualSwitch#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtualmachine_maximum_mbit(self) -> typing.Optional[jsii.Number]:
        '''The maximum allowed usage for the virtualMachine traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#virtualmachine_maximum_mbit DistributedVirtualSwitch#virtualmachine_maximum_mbit}
        '''
        result = self._values.get("virtualmachine_maximum_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def virtualmachine_reservation_mbit(self) -> typing.Optional[jsii.Number]:
        '''The amount of guaranteed bandwidth for the virtualMachine traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#virtualmachine_reservation_mbit DistributedVirtualSwitch#virtualmachine_reservation_mbit}
        '''
        result = self._values.get("virtualmachine_reservation_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def virtualmachine_share_count(self) -> typing.Optional[jsii.Number]:
        '''The amount of shares to allocate to the virtualMachine traffic class for a custom share level.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#virtualmachine_share_count DistributedVirtualSwitch#virtualmachine_share_count}
        '''
        result = self._values.get("virtualmachine_share_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def virtualmachine_share_level(self) -> typing.Optional[builtins.str]:
        '''The allocation level for the virtualMachine traffic class. Can be one of high, low, normal, or custom.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#virtualmachine_share_level DistributedVirtualSwitch#virtualmachine_share_level}
        '''
        result = self._values.get("virtualmachine_share_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vlan_id(self) -> typing.Optional[jsii.Number]:
        '''The VLAN ID for single VLAN mode. 0 denotes no VLAN.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vlan_id DistributedVirtualSwitch#vlan_id}
        '''
        result = self._values.get("vlan_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vlan_range(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DistributedVirtualSwitchVlanRange"]]]:
        '''vlan_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vlan_range DistributedVirtualSwitch#vlan_range}
        '''
        result = self._values.get("vlan_range")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DistributedVirtualSwitchVlanRange"]]], result)

    @builtins.property
    def vmotion_maximum_mbit(self) -> typing.Optional[jsii.Number]:
        '''The maximum allowed usage for the vmotion traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vmotion_maximum_mbit DistributedVirtualSwitch#vmotion_maximum_mbit}
        '''
        result = self._values.get("vmotion_maximum_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vmotion_reservation_mbit(self) -> typing.Optional[jsii.Number]:
        '''The amount of guaranteed bandwidth for the vmotion traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vmotion_reservation_mbit DistributedVirtualSwitch#vmotion_reservation_mbit}
        '''
        result = self._values.get("vmotion_reservation_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vmotion_share_count(self) -> typing.Optional[jsii.Number]:
        '''The amount of shares to allocate to the vmotion traffic class for a custom share level.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vmotion_share_count DistributedVirtualSwitch#vmotion_share_count}
        '''
        result = self._values.get("vmotion_share_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vmotion_share_level(self) -> typing.Optional[builtins.str]:
        '''The allocation level for the vmotion traffic class. Can be one of high, low, normal, or custom.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vmotion_share_level DistributedVirtualSwitch#vmotion_share_level}
        '''
        result = self._values.get("vmotion_share_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vsan_maximum_mbit(self) -> typing.Optional[jsii.Number]:
        '''The maximum allowed usage for the vsan traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vsan_maximum_mbit DistributedVirtualSwitch#vsan_maximum_mbit}
        '''
        result = self._values.get("vsan_maximum_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vsan_reservation_mbit(self) -> typing.Optional[jsii.Number]:
        '''The amount of guaranteed bandwidth for the vsan traffic class, in Mbits/sec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vsan_reservation_mbit DistributedVirtualSwitch#vsan_reservation_mbit}
        '''
        result = self._values.get("vsan_reservation_mbit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vsan_share_count(self) -> typing.Optional[jsii.Number]:
        '''The amount of shares to allocate to the vsan traffic class for a custom share level.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vsan_share_count DistributedVirtualSwitch#vsan_share_count}
        '''
        result = self._values.get("vsan_share_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vsan_share_level(self) -> typing.Optional[builtins.str]:
        '''The allocation level for the vsan traffic class. Can be one of high, low, normal, or custom.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#vsan_share_level DistributedVirtualSwitch#vsan_share_level}
        '''
        result = self._values.get("vsan_share_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DistributedVirtualSwitchConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.distributedVirtualSwitch.DistributedVirtualSwitchHost",
    jsii_struct_bases=[],
    name_mapping={"host_system_id": "hostSystemId", "devices": "devices"},
)
class DistributedVirtualSwitchHost:
    def __init__(
        self,
        *,
        host_system_id: builtins.str,
        devices: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param host_system_id: The managed object ID of the host this specification applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#host_system_id DistributedVirtualSwitch#host_system_id}
        :param devices: Name of the physical NIC to be added to the proxy switch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#devices DistributedVirtualSwitch#devices}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DistributedVirtualSwitchHost.__init__)
            check_type(argname="argument host_system_id", value=host_system_id, expected_type=type_hints["host_system_id"])
            check_type(argname="argument devices", value=devices, expected_type=type_hints["devices"])
        self._values: typing.Dict[str, typing.Any] = {
            "host_system_id": host_system_id,
        }
        if devices is not None:
            self._values["devices"] = devices

    @builtins.property
    def host_system_id(self) -> builtins.str:
        '''The managed object ID of the host this specification applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#host_system_id DistributedVirtualSwitch#host_system_id}
        '''
        result = self._values.get("host_system_id")
        assert result is not None, "Required property 'host_system_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def devices(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Name of the physical NIC to be added to the proxy switch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#devices DistributedVirtualSwitch#devices}
        '''
        result = self._values.get("devices")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DistributedVirtualSwitchHost(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DistributedVirtualSwitchHostList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.distributedVirtualSwitch.DistributedVirtualSwitchHostList",
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
            type_hints = typing.get_type_hints(DistributedVirtualSwitchHostList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DistributedVirtualSwitchHostOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DistributedVirtualSwitchHostList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DistributedVirtualSwitchHostOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchHostList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchHostList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchHostList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DistributedVirtualSwitchHost]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DistributedVirtualSwitchHost]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DistributedVirtualSwitchHost]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchHostList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DistributedVirtualSwitchHostOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.distributedVirtualSwitch.DistributedVirtualSwitchHostOutputReference",
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
            type_hints = typing.get_type_hints(DistributedVirtualSwitchHostOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDevices")
    def reset_devices(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDevices", []))

    @builtins.property
    @jsii.member(jsii_name="devicesInput")
    def devices_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "devicesInput"))

    @builtins.property
    @jsii.member(jsii_name="hostSystemIdInput")
    def host_system_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostSystemIdInput"))

    @builtins.property
    @jsii.member(jsii_name="devices")
    def devices(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "devices"))

    @devices.setter
    def devices(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchHostOutputReference, "devices").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "devices", value)

    @builtins.property
    @jsii.member(jsii_name="hostSystemId")
    def host_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostSystemId"))

    @host_system_id.setter
    def host_system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchHostOutputReference, "host_system_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostSystemId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DistributedVirtualSwitchHost, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DistributedVirtualSwitchHost, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DistributedVirtualSwitchHost, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchHostOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.distributedVirtualSwitch.DistributedVirtualSwitchPvlanMapping",
    jsii_struct_bases=[],
    name_mapping={
        "primary_vlan_id": "primaryVlanId",
        "pvlan_type": "pvlanType",
        "secondary_vlan_id": "secondaryVlanId",
    },
)
class DistributedVirtualSwitchPvlanMapping:
    def __init__(
        self,
        *,
        primary_vlan_id: jsii.Number,
        pvlan_type: builtins.str,
        secondary_vlan_id: jsii.Number,
    ) -> None:
        '''
        :param primary_vlan_id: The primary VLAN ID. The VLAN IDs of 0 and 4095 are reserved and cannot be used in this property. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#primary_vlan_id DistributedVirtualSwitch#primary_vlan_id}
        :param pvlan_type: The private VLAN type. Valid values are promiscuous, community and isolated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#pvlan_type DistributedVirtualSwitch#pvlan_type}
        :param secondary_vlan_id: The secondary VLAN ID. The VLAN IDs of 0 and 4095 are reserved and cannot be used in this property. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#secondary_vlan_id DistributedVirtualSwitch#secondary_vlan_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DistributedVirtualSwitchPvlanMapping.__init__)
            check_type(argname="argument primary_vlan_id", value=primary_vlan_id, expected_type=type_hints["primary_vlan_id"])
            check_type(argname="argument pvlan_type", value=pvlan_type, expected_type=type_hints["pvlan_type"])
            check_type(argname="argument secondary_vlan_id", value=secondary_vlan_id, expected_type=type_hints["secondary_vlan_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "primary_vlan_id": primary_vlan_id,
            "pvlan_type": pvlan_type,
            "secondary_vlan_id": secondary_vlan_id,
        }

    @builtins.property
    def primary_vlan_id(self) -> jsii.Number:
        '''The primary VLAN ID.

        The VLAN IDs of 0 and 4095 are reserved and cannot be used in this property.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#primary_vlan_id DistributedVirtualSwitch#primary_vlan_id}
        '''
        result = self._values.get("primary_vlan_id")
        assert result is not None, "Required property 'primary_vlan_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def pvlan_type(self) -> builtins.str:
        '''The private VLAN type. Valid values are promiscuous, community and isolated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#pvlan_type DistributedVirtualSwitch#pvlan_type}
        '''
        result = self._values.get("pvlan_type")
        assert result is not None, "Required property 'pvlan_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secondary_vlan_id(self) -> jsii.Number:
        '''The secondary VLAN ID.

        The VLAN IDs of 0 and 4095 are reserved and cannot be used in this property.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#secondary_vlan_id DistributedVirtualSwitch#secondary_vlan_id}
        '''
        result = self._values.get("secondary_vlan_id")
        assert result is not None, "Required property 'secondary_vlan_id' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DistributedVirtualSwitchPvlanMapping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DistributedVirtualSwitchPvlanMappingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.distributedVirtualSwitch.DistributedVirtualSwitchPvlanMappingList",
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
            type_hints = typing.get_type_hints(DistributedVirtualSwitchPvlanMappingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DistributedVirtualSwitchPvlanMappingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DistributedVirtualSwitchPvlanMappingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DistributedVirtualSwitchPvlanMappingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchPvlanMappingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchPvlanMappingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchPvlanMappingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DistributedVirtualSwitchPvlanMapping]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DistributedVirtualSwitchPvlanMapping]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DistributedVirtualSwitchPvlanMapping]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchPvlanMappingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DistributedVirtualSwitchPvlanMappingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.distributedVirtualSwitch.DistributedVirtualSwitchPvlanMappingOutputReference",
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
            type_hints = typing.get_type_hints(DistributedVirtualSwitchPvlanMappingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="primaryVlanIdInput")
    def primary_vlan_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "primaryVlanIdInput"))

    @builtins.property
    @jsii.member(jsii_name="pvlanTypeInput")
    def pvlan_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pvlanTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="secondaryVlanIdInput")
    def secondary_vlan_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "secondaryVlanIdInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryVlanId")
    def primary_vlan_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "primaryVlanId"))

    @primary_vlan_id.setter
    def primary_vlan_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchPvlanMappingOutputReference, "primary_vlan_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryVlanId", value)

    @builtins.property
    @jsii.member(jsii_name="pvlanType")
    def pvlan_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pvlanType"))

    @pvlan_type.setter
    def pvlan_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchPvlanMappingOutputReference, "pvlan_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pvlanType", value)

    @builtins.property
    @jsii.member(jsii_name="secondaryVlanId")
    def secondary_vlan_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "secondaryVlanId"))

    @secondary_vlan_id.setter
    def secondary_vlan_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchPvlanMappingOutputReference, "secondary_vlan_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secondaryVlanId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DistributedVirtualSwitchPvlanMapping, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DistributedVirtualSwitchPvlanMapping, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DistributedVirtualSwitchPvlanMapping, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchPvlanMappingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.distributedVirtualSwitch.DistributedVirtualSwitchVlanRange",
    jsii_struct_bases=[],
    name_mapping={"max_vlan": "maxVlan", "min_vlan": "minVlan"},
)
class DistributedVirtualSwitchVlanRange:
    def __init__(self, *, max_vlan: jsii.Number, min_vlan: jsii.Number) -> None:
        '''
        :param max_vlan: The minimum VLAN to use in the range. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#max_vlan DistributedVirtualSwitch#max_vlan}
        :param min_vlan: The minimum VLAN to use in the range. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#min_vlan DistributedVirtualSwitch#min_vlan}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DistributedVirtualSwitchVlanRange.__init__)
            check_type(argname="argument max_vlan", value=max_vlan, expected_type=type_hints["max_vlan"])
            check_type(argname="argument min_vlan", value=min_vlan, expected_type=type_hints["min_vlan"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_vlan": max_vlan,
            "min_vlan": min_vlan,
        }

    @builtins.property
    def max_vlan(self) -> jsii.Number:
        '''The minimum VLAN to use in the range.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#max_vlan DistributedVirtualSwitch#max_vlan}
        '''
        result = self._values.get("max_vlan")
        assert result is not None, "Required property 'max_vlan' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_vlan(self) -> jsii.Number:
        '''The minimum VLAN to use in the range.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch#min_vlan DistributedVirtualSwitch#min_vlan}
        '''
        result = self._values.get("min_vlan")
        assert result is not None, "Required property 'min_vlan' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DistributedVirtualSwitchVlanRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DistributedVirtualSwitchVlanRangeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.distributedVirtualSwitch.DistributedVirtualSwitchVlanRangeList",
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
            type_hints = typing.get_type_hints(DistributedVirtualSwitchVlanRangeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DistributedVirtualSwitchVlanRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DistributedVirtualSwitchVlanRangeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DistributedVirtualSwitchVlanRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchVlanRangeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchVlanRangeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchVlanRangeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DistributedVirtualSwitchVlanRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DistributedVirtualSwitchVlanRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DistributedVirtualSwitchVlanRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchVlanRangeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DistributedVirtualSwitchVlanRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.distributedVirtualSwitch.DistributedVirtualSwitchVlanRangeOutputReference",
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
            type_hints = typing.get_type_hints(DistributedVirtualSwitchVlanRangeOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchVlanRangeOutputReference, "max_vlan").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxVlan", value)

    @builtins.property
    @jsii.member(jsii_name="minVlan")
    def min_vlan(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minVlan"))

    @min_vlan.setter
    def min_vlan(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchVlanRangeOutputReference, "min_vlan").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minVlan", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DistributedVirtualSwitchVlanRange, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DistributedVirtualSwitchVlanRange, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DistributedVirtualSwitchVlanRange, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DistributedVirtualSwitchVlanRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DistributedVirtualSwitch",
    "DistributedVirtualSwitchConfig",
    "DistributedVirtualSwitchHost",
    "DistributedVirtualSwitchHostList",
    "DistributedVirtualSwitchHostOutputReference",
    "DistributedVirtualSwitchPvlanMapping",
    "DistributedVirtualSwitchPvlanMappingList",
    "DistributedVirtualSwitchPvlanMappingOutputReference",
    "DistributedVirtualSwitchVlanRange",
    "DistributedVirtualSwitchVlanRangeList",
    "DistributedVirtualSwitchVlanRangeOutputReference",
]

publication.publish()
