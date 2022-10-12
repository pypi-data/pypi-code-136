'''
# `google_compute_instance_from_template`

Refer to the Terraform Registory for docs: [`google_compute_instance_from_template`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template).
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


class GoogleComputeInstanceFromTemplate(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplate",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template google_compute_instance_from_template}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        source_instance_template: builtins.str,
        advanced_machine_features: typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateAdvancedMachineFeatures", typing.Dict[str, typing.Any]]] = None,
        allow_stopping_for_update: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        attached_disk: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateAttachedDisk", typing.Dict[str, typing.Any]]]]] = None,
        boot_disk: typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateBootDisk", typing.Dict[str, typing.Any]]] = None,
        can_ip_forward: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        confidential_instance_config: typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateConfidentialInstanceConfig", typing.Dict[str, typing.Any]]] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        desired_status: typing.Optional[builtins.str] = None,
        enable_display: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        guest_accelerator: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateGuestAccelerator", typing.Dict[str, typing.Any]]]]] = None,
        hostname: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        machine_type: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        metadata_startup_script: typing.Optional[builtins.str] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        network_interface: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateNetworkInterface", typing.Dict[str, typing.Any]]]]] = None,
        network_performance_config: typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateNetworkPerformanceConfig", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        reservation_affinity: typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateReservationAffinity", typing.Dict[str, typing.Any]]] = None,
        resource_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        scheduling: typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateScheduling", typing.Dict[str, typing.Any]]] = None,
        scratch_disk: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateScratchDisk", typing.Dict[str, typing.Any]]]]] = None,
        service_account: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateServiceAccount", typing.Dict[str, typing.Any]]]]] = None,
        shielded_instance_config: typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateShieldedInstanceConfig", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateTimeouts", typing.Dict[str, typing.Any]]] = None,
        zone: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template google_compute_instance_from_template} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the instance. One of name or self_link must be provided. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#name GoogleComputeInstanceFromTemplate#name}
        :param source_instance_template: Name or self link of an instance template to create the instance based on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#source_instance_template GoogleComputeInstanceFromTemplate#source_instance_template}
        :param advanced_machine_features: advanced_machine_features block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#advanced_machine_features GoogleComputeInstanceFromTemplate#advanced_machine_features}
        :param allow_stopping_for_update: If true, allows Terraform to stop the instance to update its properties. If you try to update a property that requires stopping the instance without setting this field, the update will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#allow_stopping_for_update GoogleComputeInstanceFromTemplate#allow_stopping_for_update}
        :param attached_disk: List of disks attached to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#attached_disk GoogleComputeInstanceFromTemplate#attached_disk}
        :param boot_disk: boot_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#boot_disk GoogleComputeInstanceFromTemplate#boot_disk}
        :param can_ip_forward: Whether sending and receiving of packets with non-matching source or destination IPs is allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#can_ip_forward GoogleComputeInstanceFromTemplate#can_ip_forward}
        :param confidential_instance_config: confidential_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#confidential_instance_config GoogleComputeInstanceFromTemplate#confidential_instance_config}
        :param deletion_protection: Whether deletion protection is enabled on this instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#deletion_protection GoogleComputeInstanceFromTemplate#deletion_protection}
        :param description: A brief description of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#description GoogleComputeInstanceFromTemplate#description}
        :param desired_status: Desired status of the instance. Either "RUNNING" or "TERMINATED". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#desired_status GoogleComputeInstanceFromTemplate#desired_status}
        :param enable_display: Whether the instance has virtual displays enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#enable_display GoogleComputeInstanceFromTemplate#enable_display}
        :param guest_accelerator: List of the type and count of accelerator cards attached to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#guest_accelerator GoogleComputeInstanceFromTemplate#guest_accelerator}
        :param hostname: A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid. Valid format is a series of labels 1-63 characters long matching the regular expression `a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_, concatenated with periods. The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#hostname GoogleComputeInstanceFromTemplate#hostname}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#id GoogleComputeInstanceFromTemplate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: A set of key/value label pairs assigned to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#labels GoogleComputeInstanceFromTemplate#labels}
        :param machine_type: The machine type to create. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#machine_type GoogleComputeInstanceFromTemplate#machine_type}
        :param metadata: Metadata key/value pairs made available within the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#metadata GoogleComputeInstanceFromTemplate#metadata}
        :param metadata_startup_script: Metadata startup scripts made available within the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#metadata_startup_script GoogleComputeInstanceFromTemplate#metadata_startup_script}
        :param min_cpu_platform: The minimum CPU platform specified for the VM instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#min_cpu_platform GoogleComputeInstanceFromTemplate#min_cpu_platform}
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#network_interface GoogleComputeInstanceFromTemplate#network_interface}
        :param network_performance_config: network_performance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#network_performance_config GoogleComputeInstanceFromTemplate#network_performance_config}
        :param project: The ID of the project in which the resource belongs. If self_link is provided, this value is ignored. If neither self_link nor project are provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#project GoogleComputeInstanceFromTemplate#project}
        :param reservation_affinity: reservation_affinity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#reservation_affinity GoogleComputeInstanceFromTemplate#reservation_affinity}
        :param resource_policies: A list of self_links of resource policies to attach to the instance. Currently a max of 1 resource policy is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#resource_policies GoogleComputeInstanceFromTemplate#resource_policies}
        :param scheduling: scheduling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#scheduling GoogleComputeInstanceFromTemplate#scheduling}
        :param scratch_disk: The scratch disks attached to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#scratch_disk GoogleComputeInstanceFromTemplate#scratch_disk}
        :param service_account: The service account to attach to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#service_account GoogleComputeInstanceFromTemplate#service_account}
        :param shielded_instance_config: shielded_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#shielded_instance_config GoogleComputeInstanceFromTemplate#shielded_instance_config}
        :param tags: The list of tags attached to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#tags GoogleComputeInstanceFromTemplate#tags}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#timeouts GoogleComputeInstanceFromTemplate#timeouts}
        :param zone: The zone of the instance. If self_link is provided, this value is ignored. If neither self_link nor zone are provided, the provider zone is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#zone GoogleComputeInstanceFromTemplate#zone}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplate.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeInstanceFromTemplateConfig(
            name=name,
            source_instance_template=source_instance_template,
            advanced_machine_features=advanced_machine_features,
            allow_stopping_for_update=allow_stopping_for_update,
            attached_disk=attached_disk,
            boot_disk=boot_disk,
            can_ip_forward=can_ip_forward,
            confidential_instance_config=confidential_instance_config,
            deletion_protection=deletion_protection,
            description=description,
            desired_status=desired_status,
            enable_display=enable_display,
            guest_accelerator=guest_accelerator,
            hostname=hostname,
            id=id,
            labels=labels,
            machine_type=machine_type,
            metadata=metadata,
            metadata_startup_script=metadata_startup_script,
            min_cpu_platform=min_cpu_platform,
            network_interface=network_interface,
            network_performance_config=network_performance_config,
            project=project,
            reservation_affinity=reservation_affinity,
            resource_policies=resource_policies,
            scheduling=scheduling,
            scratch_disk=scratch_disk,
            service_account=service_account,
            shielded_instance_config=shielded_instance_config,
            tags=tags,
            timeouts=timeouts,
            zone=zone,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAdvancedMachineFeatures")
    def put_advanced_machine_features(
        self,
        *,
        enable_nested_virtualization: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        threads_per_core: typing.Optional[jsii.Number] = None,
        visible_core_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enable_nested_virtualization: Whether to enable nested virtualization or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#enable_nested_virtualization GoogleComputeInstanceFromTemplate#enable_nested_virtualization}
        :param threads_per_core: The number of threads per physical core. To disable simultaneous multithreading (SMT) set this to 1. If unset, the maximum number of threads supported per core by the underlying processor is assumed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#threads_per_core GoogleComputeInstanceFromTemplate#threads_per_core}
        :param visible_core_count: The number of physical cores to expose to an instance. Multiply by the number of threads per core to compute the total number of virtual CPUs to expose to the instance. If unset, the number of cores is inferred from the instance's nominal CPU count and the underlying platform's SMT width. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#visible_core_count GoogleComputeInstanceFromTemplate#visible_core_count}
        '''
        value = GoogleComputeInstanceFromTemplateAdvancedMachineFeatures(
            enable_nested_virtualization=enable_nested_virtualization,
            threads_per_core=threads_per_core,
            visible_core_count=visible_core_count,
        )

        return typing.cast(None, jsii.invoke(self, "putAdvancedMachineFeatures", [value]))

    @jsii.member(jsii_name="putAttachedDisk")
    def put_attached_disk(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateAttachedDisk", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplate.put_attached_disk)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAttachedDisk", [value]))

    @jsii.member(jsii_name="putBootDisk")
    def put_boot_disk(
        self,
        *,
        auto_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        device_name: typing.Optional[builtins.str] = None,
        disk_encryption_key_raw: typing.Optional[builtins.str] = None,
        initialize_params: typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateBootDiskInitializeParams", typing.Dict[str, typing.Any]]] = None,
        kms_key_self_link: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_delete: Whether the disk will be auto-deleted when the instance is deleted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#auto_delete GoogleComputeInstanceFromTemplate#auto_delete}
        :param device_name: Name with which attached disk will be accessible under /dev/disk/by-id/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#device_name GoogleComputeInstanceFromTemplate#device_name}
        :param disk_encryption_key_raw: A 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to encrypt this disk. Only one of kms_key_self_link and disk_encryption_key_raw may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#disk_encryption_key_raw GoogleComputeInstanceFromTemplate#disk_encryption_key_raw}
        :param initialize_params: initialize_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#initialize_params GoogleComputeInstanceFromTemplate#initialize_params}
        :param kms_key_self_link: The self_link of the encryption key that is stored in Google Cloud KMS to encrypt this disk. Only one of kms_key_self_link and disk_encryption_key_raw may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#kms_key_self_link GoogleComputeInstanceFromTemplate#kms_key_self_link}
        :param mode: Read/write mode for the disk. One of "READ_ONLY" or "READ_WRITE". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#mode GoogleComputeInstanceFromTemplate#mode}
        :param source: The name or self_link of the disk attached to this instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#source GoogleComputeInstanceFromTemplate#source}
        '''
        value = GoogleComputeInstanceFromTemplateBootDisk(
            auto_delete=auto_delete,
            device_name=device_name,
            disk_encryption_key_raw=disk_encryption_key_raw,
            initialize_params=initialize_params,
            kms_key_self_link=kms_key_self_link,
            mode=mode,
            source=source,
        )

        return typing.cast(None, jsii.invoke(self, "putBootDisk", [value]))

    @jsii.member(jsii_name="putConfidentialInstanceConfig")
    def put_confidential_instance_config(
        self,
        *,
        enable_confidential_compute: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable_confidential_compute: Defines whether the instance should have confidential compute enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#enable_confidential_compute GoogleComputeInstanceFromTemplate#enable_confidential_compute}
        '''
        value = GoogleComputeInstanceFromTemplateConfidentialInstanceConfig(
            enable_confidential_compute=enable_confidential_compute
        )

        return typing.cast(None, jsii.invoke(self, "putConfidentialInstanceConfig", [value]))

    @jsii.member(jsii_name="putGuestAccelerator")
    def put_guest_accelerator(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateGuestAccelerator", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplate.put_guest_accelerator)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGuestAccelerator", [value]))

    @jsii.member(jsii_name="putNetworkInterface")
    def put_network_interface(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateNetworkInterface", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplate.put_network_interface)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkInterface", [value]))

    @jsii.member(jsii_name="putNetworkPerformanceConfig")
    def put_network_performance_config(
        self,
        *,
        total_egress_bandwidth_tier: builtins.str,
    ) -> None:
        '''
        :param total_egress_bandwidth_tier: The egress bandwidth tier to enable. Possible values:TIER_1, DEFAULT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#total_egress_bandwidth_tier GoogleComputeInstanceFromTemplate#total_egress_bandwidth_tier}
        '''
        value = GoogleComputeInstanceFromTemplateNetworkPerformanceConfig(
            total_egress_bandwidth_tier=total_egress_bandwidth_tier
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkPerformanceConfig", [value]))

    @jsii.member(jsii_name="putReservationAffinity")
    def put_reservation_affinity(
        self,
        *,
        type: builtins.str,
        specific_reservation: typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservation", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: The type of reservation from which this instance can consume resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#type GoogleComputeInstanceFromTemplate#type}
        :param specific_reservation: specific_reservation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#specific_reservation GoogleComputeInstanceFromTemplate#specific_reservation}
        '''
        value = GoogleComputeInstanceFromTemplateReservationAffinity(
            type=type, specific_reservation=specific_reservation
        )

        return typing.cast(None, jsii.invoke(self, "putReservationAffinity", [value]))

    @jsii.member(jsii_name="putScheduling")
    def put_scheduling(
        self,
        *,
        automatic_restart: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        instance_termination_action: typing.Optional[builtins.str] = None,
        min_node_cpus: typing.Optional[jsii.Number] = None,
        node_affinities: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateSchedulingNodeAffinities", typing.Dict[str, typing.Any]]]]] = None,
        on_host_maintenance: typing.Optional[builtins.str] = None,
        preemptible: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        provisioning_model: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param automatic_restart: Specifies if the instance should be restarted if it was terminated by Compute Engine (not a user). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#automatic_restart GoogleComputeInstanceFromTemplate#automatic_restart}
        :param instance_termination_action: Specifies the action GCE should take when SPOT VM is preempted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#instance_termination_action GoogleComputeInstanceFromTemplate#instance_termination_action}
        :param min_node_cpus: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#min_node_cpus GoogleComputeInstanceFromTemplate#min_node_cpus}.
        :param node_affinities: node_affinities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#node_affinities GoogleComputeInstanceFromTemplate#node_affinities}
        :param on_host_maintenance: Describes maintenance behavior for the instance. One of MIGRATE or TERMINATE,. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#on_host_maintenance GoogleComputeInstanceFromTemplate#on_host_maintenance}
        :param preemptible: Whether the instance is preemptible. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#preemptible GoogleComputeInstanceFromTemplate#preemptible}
        :param provisioning_model: Whether the instance is spot. If this is set as SPOT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#provisioning_model GoogleComputeInstanceFromTemplate#provisioning_model}
        '''
        value = GoogleComputeInstanceFromTemplateScheduling(
            automatic_restart=automatic_restart,
            instance_termination_action=instance_termination_action,
            min_node_cpus=min_node_cpus,
            node_affinities=node_affinities,
            on_host_maintenance=on_host_maintenance,
            preemptible=preemptible,
            provisioning_model=provisioning_model,
        )

        return typing.cast(None, jsii.invoke(self, "putScheduling", [value]))

    @jsii.member(jsii_name="putScratchDisk")
    def put_scratch_disk(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateScratchDisk", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplate.put_scratch_disk)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScratchDisk", [value]))

    @jsii.member(jsii_name="putServiceAccount")
    def put_service_account(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateServiceAccount", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplate.put_service_account)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putServiceAccount", [value]))

    @jsii.member(jsii_name="putShieldedInstanceConfig")
    def put_shielded_instance_config(
        self,
        *,
        enable_integrity_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_secure_boot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_vtpm: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_integrity_monitoring: Whether integrity monitoring is enabled for the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#enable_integrity_monitoring GoogleComputeInstanceFromTemplate#enable_integrity_monitoring}
        :param enable_secure_boot: Whether secure boot is enabled for the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#enable_secure_boot GoogleComputeInstanceFromTemplate#enable_secure_boot}
        :param enable_vtpm: Whether the instance uses vTPM. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#enable_vtpm GoogleComputeInstanceFromTemplate#enable_vtpm}
        '''
        value = GoogleComputeInstanceFromTemplateShieldedInstanceConfig(
            enable_integrity_monitoring=enable_integrity_monitoring,
            enable_secure_boot=enable_secure_boot,
            enable_vtpm=enable_vtpm,
        )

        return typing.cast(None, jsii.invoke(self, "putShieldedInstanceConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#create GoogleComputeInstanceFromTemplate#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#delete GoogleComputeInstanceFromTemplate#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#update GoogleComputeInstanceFromTemplate#update}.
        '''
        value = GoogleComputeInstanceFromTemplateTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAdvancedMachineFeatures")
    def reset_advanced_machine_features(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvancedMachineFeatures", []))

    @jsii.member(jsii_name="resetAllowStoppingForUpdate")
    def reset_allow_stopping_for_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowStoppingForUpdate", []))

    @jsii.member(jsii_name="resetAttachedDisk")
    def reset_attached_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttachedDisk", []))

    @jsii.member(jsii_name="resetBootDisk")
    def reset_boot_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDisk", []))

    @jsii.member(jsii_name="resetCanIpForward")
    def reset_can_ip_forward(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCanIpForward", []))

    @jsii.member(jsii_name="resetConfidentialInstanceConfig")
    def reset_confidential_instance_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfidentialInstanceConfig", []))

    @jsii.member(jsii_name="resetDeletionProtection")
    def reset_deletion_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeletionProtection", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDesiredStatus")
    def reset_desired_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredStatus", []))

    @jsii.member(jsii_name="resetEnableDisplay")
    def reset_enable_display(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableDisplay", []))

    @jsii.member(jsii_name="resetGuestAccelerator")
    def reset_guest_accelerator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGuestAccelerator", []))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetMachineType")
    def reset_machine_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMachineType", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetMetadataStartupScript")
    def reset_metadata_startup_script(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadataStartupScript", []))

    @jsii.member(jsii_name="resetMinCpuPlatform")
    def reset_min_cpu_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCpuPlatform", []))

    @jsii.member(jsii_name="resetNetworkInterface")
    def reset_network_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkInterface", []))

    @jsii.member(jsii_name="resetNetworkPerformanceConfig")
    def reset_network_performance_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkPerformanceConfig", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetReservationAffinity")
    def reset_reservation_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReservationAffinity", []))

    @jsii.member(jsii_name="resetResourcePolicies")
    def reset_resource_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourcePolicies", []))

    @jsii.member(jsii_name="resetScheduling")
    def reset_scheduling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduling", []))

    @jsii.member(jsii_name="resetScratchDisk")
    def reset_scratch_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScratchDisk", []))

    @jsii.member(jsii_name="resetServiceAccount")
    def reset_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccount", []))

    @jsii.member(jsii_name="resetShieldedInstanceConfig")
    def reset_shielded_instance_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShieldedInstanceConfig", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetZone")
    def reset_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZone", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="advancedMachineFeatures")
    def advanced_machine_features(
        self,
    ) -> "GoogleComputeInstanceFromTemplateAdvancedMachineFeaturesOutputReference":
        return typing.cast("GoogleComputeInstanceFromTemplateAdvancedMachineFeaturesOutputReference", jsii.get(self, "advancedMachineFeatures"))

    @builtins.property
    @jsii.member(jsii_name="attachedDisk")
    def attached_disk(self) -> "GoogleComputeInstanceFromTemplateAttachedDiskList":
        return typing.cast("GoogleComputeInstanceFromTemplateAttachedDiskList", jsii.get(self, "attachedDisk"))

    @builtins.property
    @jsii.member(jsii_name="bootDisk")
    def boot_disk(self) -> "GoogleComputeInstanceFromTemplateBootDiskOutputReference":
        return typing.cast("GoogleComputeInstanceFromTemplateBootDiskOutputReference", jsii.get(self, "bootDisk"))

    @builtins.property
    @jsii.member(jsii_name="confidentialInstanceConfig")
    def confidential_instance_config(
        self,
    ) -> "GoogleComputeInstanceFromTemplateConfidentialInstanceConfigOutputReference":
        return typing.cast("GoogleComputeInstanceFromTemplateConfidentialInstanceConfigOutputReference", jsii.get(self, "confidentialInstanceConfig"))

    @builtins.property
    @jsii.member(jsii_name="cpuPlatform")
    def cpu_platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpuPlatform"))

    @builtins.property
    @jsii.member(jsii_name="currentStatus")
    def current_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "currentStatus"))

    @builtins.property
    @jsii.member(jsii_name="guestAccelerator")
    def guest_accelerator(
        self,
    ) -> "GoogleComputeInstanceFromTemplateGuestAcceleratorList":
        return typing.cast("GoogleComputeInstanceFromTemplateGuestAcceleratorList", jsii.get(self, "guestAccelerator"))

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @builtins.property
    @jsii.member(jsii_name="labelFingerprint")
    def label_fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "labelFingerprint"))

    @builtins.property
    @jsii.member(jsii_name="metadataFingerprint")
    def metadata_fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metadataFingerprint"))

    @builtins.property
    @jsii.member(jsii_name="networkInterface")
    def network_interface(
        self,
    ) -> "GoogleComputeInstanceFromTemplateNetworkInterfaceList":
        return typing.cast("GoogleComputeInstanceFromTemplateNetworkInterfaceList", jsii.get(self, "networkInterface"))

    @builtins.property
    @jsii.member(jsii_name="networkPerformanceConfig")
    def network_performance_config(
        self,
    ) -> "GoogleComputeInstanceFromTemplateNetworkPerformanceConfigOutputReference":
        return typing.cast("GoogleComputeInstanceFromTemplateNetworkPerformanceConfigOutputReference", jsii.get(self, "networkPerformanceConfig"))

    @builtins.property
    @jsii.member(jsii_name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> "GoogleComputeInstanceFromTemplateReservationAffinityOutputReference":
        return typing.cast("GoogleComputeInstanceFromTemplateReservationAffinityOutputReference", jsii.get(self, "reservationAffinity"))

    @builtins.property
    @jsii.member(jsii_name="scheduling")
    def scheduling(
        self,
    ) -> "GoogleComputeInstanceFromTemplateSchedulingOutputReference":
        return typing.cast("GoogleComputeInstanceFromTemplateSchedulingOutputReference", jsii.get(self, "scheduling"))

    @builtins.property
    @jsii.member(jsii_name="scratchDisk")
    def scratch_disk(self) -> "GoogleComputeInstanceFromTemplateScratchDiskList":
        return typing.cast("GoogleComputeInstanceFromTemplateScratchDiskList", jsii.get(self, "scratchDisk"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> "GoogleComputeInstanceFromTemplateServiceAccountList":
        return typing.cast("GoogleComputeInstanceFromTemplateServiceAccountList", jsii.get(self, "serviceAccount"))

    @builtins.property
    @jsii.member(jsii_name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> "GoogleComputeInstanceFromTemplateShieldedInstanceConfigOutputReference":
        return typing.cast("GoogleComputeInstanceFromTemplateShieldedInstanceConfigOutputReference", jsii.get(self, "shieldedInstanceConfig"))

    @builtins.property
    @jsii.member(jsii_name="tagsFingerprint")
    def tags_fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagsFingerprint"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeInstanceFromTemplateTimeoutsOutputReference":
        return typing.cast("GoogleComputeInstanceFromTemplateTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="advancedMachineFeaturesInput")
    def advanced_machine_features_input(
        self,
    ) -> typing.Optional["GoogleComputeInstanceFromTemplateAdvancedMachineFeatures"]:
        return typing.cast(typing.Optional["GoogleComputeInstanceFromTemplateAdvancedMachineFeatures"], jsii.get(self, "advancedMachineFeaturesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowStoppingForUpdateInput")
    def allow_stopping_for_update_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowStoppingForUpdateInput"))

    @builtins.property
    @jsii.member(jsii_name="attachedDiskInput")
    def attached_disk_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateAttachedDisk"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateAttachedDisk"]]], jsii.get(self, "attachedDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskInput")
    def boot_disk_input(
        self,
    ) -> typing.Optional["GoogleComputeInstanceFromTemplateBootDisk"]:
        return typing.cast(typing.Optional["GoogleComputeInstanceFromTemplateBootDisk"], jsii.get(self, "bootDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="canIpForwardInput")
    def can_ip_forward_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "canIpForwardInput"))

    @builtins.property
    @jsii.member(jsii_name="confidentialInstanceConfigInput")
    def confidential_instance_config_input(
        self,
    ) -> typing.Optional["GoogleComputeInstanceFromTemplateConfidentialInstanceConfig"]:
        return typing.cast(typing.Optional["GoogleComputeInstanceFromTemplateConfidentialInstanceConfig"], jsii.get(self, "confidentialInstanceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="deletionProtectionInput")
    def deletion_protection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deletionProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredStatusInput")
    def desired_status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desiredStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="enableDisplayInput")
    def enable_display_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableDisplayInput"))

    @builtins.property
    @jsii.member(jsii_name="guestAcceleratorInput")
    def guest_accelerator_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateGuestAccelerator"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateGuestAccelerator"]]], jsii.get(self, "guestAcceleratorInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="machineTypeInput")
    def machine_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataStartupScriptInput")
    def metadata_startup_script_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadataStartupScriptInput"))

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatformInput")
    def min_cpu_platform_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minCpuPlatformInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceInput")
    def network_interface_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateNetworkInterface"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateNetworkInterface"]]], jsii.get(self, "networkInterfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="networkPerformanceConfigInput")
    def network_performance_config_input(
        self,
    ) -> typing.Optional["GoogleComputeInstanceFromTemplateNetworkPerformanceConfig"]:
        return typing.cast(typing.Optional["GoogleComputeInstanceFromTemplateNetworkPerformanceConfig"], jsii.get(self, "networkPerformanceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="reservationAffinityInput")
    def reservation_affinity_input(
        self,
    ) -> typing.Optional["GoogleComputeInstanceFromTemplateReservationAffinity"]:
        return typing.cast(typing.Optional["GoogleComputeInstanceFromTemplateReservationAffinity"], jsii.get(self, "reservationAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="resourcePoliciesInput")
    def resource_policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourcePoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="schedulingInput")
    def scheduling_input(
        self,
    ) -> typing.Optional["GoogleComputeInstanceFromTemplateScheduling"]:
        return typing.cast(typing.Optional["GoogleComputeInstanceFromTemplateScheduling"], jsii.get(self, "schedulingInput"))

    @builtins.property
    @jsii.member(jsii_name="scratchDiskInput")
    def scratch_disk_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateScratchDisk"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateScratchDisk"]]], jsii.get(self, "scratchDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountInput")
    def service_account_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateServiceAccount"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateServiceAccount"]]], jsii.get(self, "serviceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="shieldedInstanceConfigInput")
    def shielded_instance_config_input(
        self,
    ) -> typing.Optional["GoogleComputeInstanceFromTemplateShieldedInstanceConfig"]:
        return typing.cast(typing.Optional["GoogleComputeInstanceFromTemplateShieldedInstanceConfig"], jsii.get(self, "shieldedInstanceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInstanceTemplateInput")
    def source_instance_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInstanceTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="allowStoppingForUpdate")
    def allow_stopping_for_update(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowStoppingForUpdate"))

    @allow_stopping_for_update.setter
    def allow_stopping_for_update(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "allow_stopping_for_update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowStoppingForUpdate", value)

    @builtins.property
    @jsii.member(jsii_name="canIpForward")
    def can_ip_forward(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "canIpForward"))

    @can_ip_forward.setter
    def can_ip_forward(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "can_ip_forward").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "canIpForward", value)

    @builtins.property
    @jsii.member(jsii_name="deletionProtection")
    def deletion_protection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deletionProtection"))

    @deletion_protection.setter
    def deletion_protection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "deletion_protection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtection", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="desiredStatus")
    def desired_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "desiredStatus"))

    @desired_status.setter
    def desired_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "desired_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredStatus", value)

    @builtins.property
    @jsii.member(jsii_name="enableDisplay")
    def enable_display(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableDisplay"))

    @enable_display.setter
    def enable_display(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "enable_display").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDisplay", value)

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "hostname").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="machineType")
    def machine_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineType"))

    @machine_type.setter
    def machine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "machine_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineType", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "metadata").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="metadataStartupScript")
    def metadata_startup_script(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metadataStartupScript"))

    @metadata_startup_script.setter
    def metadata_startup_script(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "metadata_startup_script").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadataStartupScript", value)

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatform")
    def min_cpu_platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minCpuPlatform"))

    @min_cpu_platform.setter
    def min_cpu_platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "min_cpu_platform").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCpuPlatform", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="resourcePolicies")
    def resource_policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourcePolicies"))

    @resource_policies.setter
    def resource_policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "resource_policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourcePolicies", value)

    @builtins.property
    @jsii.member(jsii_name="sourceInstanceTemplate")
    def source_instance_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceInstanceTemplate"))

    @source_instance_template.setter
    def source_instance_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "source_instance_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceInstanceTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplate, "zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateAdvancedMachineFeatures",
    jsii_struct_bases=[],
    name_mapping={
        "enable_nested_virtualization": "enableNestedVirtualization",
        "threads_per_core": "threadsPerCore",
        "visible_core_count": "visibleCoreCount",
    },
)
class GoogleComputeInstanceFromTemplateAdvancedMachineFeatures:
    def __init__(
        self,
        *,
        enable_nested_virtualization: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        threads_per_core: typing.Optional[jsii.Number] = None,
        visible_core_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enable_nested_virtualization: Whether to enable nested virtualization or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#enable_nested_virtualization GoogleComputeInstanceFromTemplate#enable_nested_virtualization}
        :param threads_per_core: The number of threads per physical core. To disable simultaneous multithreading (SMT) set this to 1. If unset, the maximum number of threads supported per core by the underlying processor is assumed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#threads_per_core GoogleComputeInstanceFromTemplate#threads_per_core}
        :param visible_core_count: The number of physical cores to expose to an instance. Multiply by the number of threads per core to compute the total number of virtual CPUs to expose to the instance. If unset, the number of cores is inferred from the instance's nominal CPU count and the underlying platform's SMT width. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#visible_core_count GoogleComputeInstanceFromTemplate#visible_core_count}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateAdvancedMachineFeatures.__init__)
            check_type(argname="argument enable_nested_virtualization", value=enable_nested_virtualization, expected_type=type_hints["enable_nested_virtualization"])
            check_type(argname="argument threads_per_core", value=threads_per_core, expected_type=type_hints["threads_per_core"])
            check_type(argname="argument visible_core_count", value=visible_core_count, expected_type=type_hints["visible_core_count"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enable_nested_virtualization is not None:
            self._values["enable_nested_virtualization"] = enable_nested_virtualization
        if threads_per_core is not None:
            self._values["threads_per_core"] = threads_per_core
        if visible_core_count is not None:
            self._values["visible_core_count"] = visible_core_count

    @builtins.property
    def enable_nested_virtualization(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to enable nested virtualization or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#enable_nested_virtualization GoogleComputeInstanceFromTemplate#enable_nested_virtualization}
        '''
        result = self._values.get("enable_nested_virtualization")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def threads_per_core(self) -> typing.Optional[jsii.Number]:
        '''The number of threads per physical core.

        To disable simultaneous multithreading (SMT) set this to 1. If unset, the maximum number of threads supported per core by the underlying processor is assumed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#threads_per_core GoogleComputeInstanceFromTemplate#threads_per_core}
        '''
        result = self._values.get("threads_per_core")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def visible_core_count(self) -> typing.Optional[jsii.Number]:
        '''The number of physical cores to expose to an instance.

        Multiply by the number of threads per core to compute the total number of virtual CPUs to expose to the instance. If unset, the number of cores is inferred from the instance's nominal CPU count and the underlying platform's SMT width.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#visible_core_count GoogleComputeInstanceFromTemplate#visible_core_count}
        '''
        result = self._values.get("visible_core_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateAdvancedMachineFeatures(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceFromTemplateAdvancedMachineFeaturesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateAdvancedMachineFeaturesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateAdvancedMachineFeaturesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnableNestedVirtualization")
    def reset_enable_nested_virtualization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableNestedVirtualization", []))

    @jsii.member(jsii_name="resetThreadsPerCore")
    def reset_threads_per_core(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThreadsPerCore", []))

    @jsii.member(jsii_name="resetVisibleCoreCount")
    def reset_visible_core_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVisibleCoreCount", []))

    @builtins.property
    @jsii.member(jsii_name="enableNestedVirtualizationInput")
    def enable_nested_virtualization_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableNestedVirtualizationInput"))

    @builtins.property
    @jsii.member(jsii_name="threadsPerCoreInput")
    def threads_per_core_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "threadsPerCoreInput"))

    @builtins.property
    @jsii.member(jsii_name="visibleCoreCountInput")
    def visible_core_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "visibleCoreCountInput"))

    @builtins.property
    @jsii.member(jsii_name="enableNestedVirtualization")
    def enable_nested_virtualization(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableNestedVirtualization"))

    @enable_nested_virtualization.setter
    def enable_nested_virtualization(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateAdvancedMachineFeaturesOutputReference, "enable_nested_virtualization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableNestedVirtualization", value)

    @builtins.property
    @jsii.member(jsii_name="threadsPerCore")
    def threads_per_core(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threadsPerCore"))

    @threads_per_core.setter
    def threads_per_core(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateAdvancedMachineFeaturesOutputReference, "threads_per_core").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threadsPerCore", value)

    @builtins.property
    @jsii.member(jsii_name="visibleCoreCount")
    def visible_core_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "visibleCoreCount"))

    @visible_core_count.setter
    def visible_core_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateAdvancedMachineFeaturesOutputReference, "visible_core_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibleCoreCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInstanceFromTemplateAdvancedMachineFeatures]:
        return typing.cast(typing.Optional[GoogleComputeInstanceFromTemplateAdvancedMachineFeatures], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInstanceFromTemplateAdvancedMachineFeatures],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateAdvancedMachineFeaturesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateAttachedDisk",
    jsii_struct_bases=[],
    name_mapping={
        "device_name": "deviceName",
        "disk_encryption_key_raw": "diskEncryptionKeyRaw",
        "disk_encryption_key_sha256": "diskEncryptionKeySha256",
        "kms_key_self_link": "kmsKeySelfLink",
        "mode": "mode",
        "source": "source",
    },
)
class GoogleComputeInstanceFromTemplateAttachedDisk:
    def __init__(
        self,
        *,
        device_name: typing.Optional[builtins.str] = None,
        disk_encryption_key_raw: typing.Optional[builtins.str] = None,
        disk_encryption_key_sha256: typing.Optional[builtins.str] = None,
        kms_key_self_link: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param device_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#device_name GoogleComputeInstanceFromTemplate#device_name}.
        :param disk_encryption_key_raw: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#disk_encryption_key_raw GoogleComputeInstanceFromTemplate#disk_encryption_key_raw}.
        :param disk_encryption_key_sha256: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#disk_encryption_key_sha256 GoogleComputeInstanceFromTemplate#disk_encryption_key_sha256}.
        :param kms_key_self_link: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#kms_key_self_link GoogleComputeInstanceFromTemplate#kms_key_self_link}.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#mode GoogleComputeInstanceFromTemplate#mode}.
        :param source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#source GoogleComputeInstanceFromTemplate#source}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateAttachedDisk.__init__)
            check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
            check_type(argname="argument disk_encryption_key_raw", value=disk_encryption_key_raw, expected_type=type_hints["disk_encryption_key_raw"])
            check_type(argname="argument disk_encryption_key_sha256", value=disk_encryption_key_sha256, expected_type=type_hints["disk_encryption_key_sha256"])
            check_type(argname="argument kms_key_self_link", value=kms_key_self_link, expected_type=type_hints["kms_key_self_link"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[str, typing.Any] = {}
        if device_name is not None:
            self._values["device_name"] = device_name
        if disk_encryption_key_raw is not None:
            self._values["disk_encryption_key_raw"] = disk_encryption_key_raw
        if disk_encryption_key_sha256 is not None:
            self._values["disk_encryption_key_sha256"] = disk_encryption_key_sha256
        if kms_key_self_link is not None:
            self._values["kms_key_self_link"] = kms_key_self_link
        if mode is not None:
            self._values["mode"] = mode
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def device_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#device_name GoogleComputeInstanceFromTemplate#device_name}.'''
        result = self._values.get("device_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_encryption_key_raw(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#disk_encryption_key_raw GoogleComputeInstanceFromTemplate#disk_encryption_key_raw}.'''
        result = self._values.get("disk_encryption_key_raw")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_encryption_key_sha256(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#disk_encryption_key_sha256 GoogleComputeInstanceFromTemplate#disk_encryption_key_sha256}.'''
        result = self._values.get("disk_encryption_key_sha256")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_self_link(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#kms_key_self_link GoogleComputeInstanceFromTemplate#kms_key_self_link}.'''
        result = self._values.get("kms_key_self_link")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#mode GoogleComputeInstanceFromTemplate#mode}.'''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#source GoogleComputeInstanceFromTemplate#source}.'''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateAttachedDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceFromTemplateAttachedDiskList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateAttachedDiskList",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateAttachedDiskList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeInstanceFromTemplateAttachedDiskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateAttachedDiskList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeInstanceFromTemplateAttachedDiskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateAttachedDiskList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateAttachedDiskList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateAttachedDiskList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateAttachedDisk]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateAttachedDisk]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateAttachedDisk]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateAttachedDiskList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceFromTemplateAttachedDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateAttachedDiskOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateAttachedDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDeviceName")
    def reset_device_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceName", []))

    @jsii.member(jsii_name="resetDiskEncryptionKeyRaw")
    def reset_disk_encryption_key_raw(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskEncryptionKeyRaw", []))

    @jsii.member(jsii_name="resetDiskEncryptionKeySha256")
    def reset_disk_encryption_key_sha256(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskEncryptionKeySha256", []))

    @jsii.member(jsii_name="resetKmsKeySelfLink")
    def reset_kms_key_self_link(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeySelfLink", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @builtins.property
    @jsii.member(jsii_name="deviceNameInput")
    def device_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKeyRawInput")
    def disk_encryption_key_raw_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskEncryptionKeyRawInput"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKeySha256Input")
    def disk_encryption_key_sha256_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskEncryptionKeySha256Input"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeySelfLinkInput")
    def kms_key_self_link_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeySelfLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceName"))

    @device_name.setter
    def device_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateAttachedDiskOutputReference, "device_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceName", value)

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKeyRaw")
    def disk_encryption_key_raw(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskEncryptionKeyRaw"))

    @disk_encryption_key_raw.setter
    def disk_encryption_key_raw(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateAttachedDiskOutputReference, "disk_encryption_key_raw").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskEncryptionKeyRaw", value)

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKeySha256")
    def disk_encryption_key_sha256(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskEncryptionKeySha256"))

    @disk_encryption_key_sha256.setter
    def disk_encryption_key_sha256(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateAttachedDiskOutputReference, "disk_encryption_key_sha256").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskEncryptionKeySha256", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeySelfLink")
    def kms_key_self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeySelfLink"))

    @kms_key_self_link.setter
    def kms_key_self_link(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateAttachedDiskOutputReference, "kms_key_self_link").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeySelfLink", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateAttachedDiskOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateAttachedDiskOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateAttachedDisk, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateAttachedDisk, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateAttachedDisk, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateAttachedDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateBootDisk",
    jsii_struct_bases=[],
    name_mapping={
        "auto_delete": "autoDelete",
        "device_name": "deviceName",
        "disk_encryption_key_raw": "diskEncryptionKeyRaw",
        "initialize_params": "initializeParams",
        "kms_key_self_link": "kmsKeySelfLink",
        "mode": "mode",
        "source": "source",
    },
)
class GoogleComputeInstanceFromTemplateBootDisk:
    def __init__(
        self,
        *,
        auto_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        device_name: typing.Optional[builtins.str] = None,
        disk_encryption_key_raw: typing.Optional[builtins.str] = None,
        initialize_params: typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateBootDiskInitializeParams", typing.Dict[str, typing.Any]]] = None,
        kms_key_self_link: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_delete: Whether the disk will be auto-deleted when the instance is deleted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#auto_delete GoogleComputeInstanceFromTemplate#auto_delete}
        :param device_name: Name with which attached disk will be accessible under /dev/disk/by-id/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#device_name GoogleComputeInstanceFromTemplate#device_name}
        :param disk_encryption_key_raw: A 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to encrypt this disk. Only one of kms_key_self_link and disk_encryption_key_raw may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#disk_encryption_key_raw GoogleComputeInstanceFromTemplate#disk_encryption_key_raw}
        :param initialize_params: initialize_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#initialize_params GoogleComputeInstanceFromTemplate#initialize_params}
        :param kms_key_self_link: The self_link of the encryption key that is stored in Google Cloud KMS to encrypt this disk. Only one of kms_key_self_link and disk_encryption_key_raw may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#kms_key_self_link GoogleComputeInstanceFromTemplate#kms_key_self_link}
        :param mode: Read/write mode for the disk. One of "READ_ONLY" or "READ_WRITE". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#mode GoogleComputeInstanceFromTemplate#mode}
        :param source: The name or self_link of the disk attached to this instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#source GoogleComputeInstanceFromTemplate#source}
        '''
        if isinstance(initialize_params, dict):
            initialize_params = GoogleComputeInstanceFromTemplateBootDiskInitializeParams(**initialize_params)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateBootDisk.__init__)
            check_type(argname="argument auto_delete", value=auto_delete, expected_type=type_hints["auto_delete"])
            check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
            check_type(argname="argument disk_encryption_key_raw", value=disk_encryption_key_raw, expected_type=type_hints["disk_encryption_key_raw"])
            check_type(argname="argument initialize_params", value=initialize_params, expected_type=type_hints["initialize_params"])
            check_type(argname="argument kms_key_self_link", value=kms_key_self_link, expected_type=type_hints["kms_key_self_link"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_delete is not None:
            self._values["auto_delete"] = auto_delete
        if device_name is not None:
            self._values["device_name"] = device_name
        if disk_encryption_key_raw is not None:
            self._values["disk_encryption_key_raw"] = disk_encryption_key_raw
        if initialize_params is not None:
            self._values["initialize_params"] = initialize_params
        if kms_key_self_link is not None:
            self._values["kms_key_self_link"] = kms_key_self_link
        if mode is not None:
            self._values["mode"] = mode
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def auto_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the disk will be auto-deleted when the instance is deleted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#auto_delete GoogleComputeInstanceFromTemplate#auto_delete}
        '''
        result = self._values.get("auto_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def device_name(self) -> typing.Optional[builtins.str]:
        '''Name with which attached disk will be accessible under /dev/disk/by-id/.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#device_name GoogleComputeInstanceFromTemplate#device_name}
        '''
        result = self._values.get("device_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_encryption_key_raw(self) -> typing.Optional[builtins.str]:
        '''A 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to encrypt this disk.

        Only one of kms_key_self_link and disk_encryption_key_raw may be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#disk_encryption_key_raw GoogleComputeInstanceFromTemplate#disk_encryption_key_raw}
        '''
        result = self._values.get("disk_encryption_key_raw")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initialize_params(
        self,
    ) -> typing.Optional["GoogleComputeInstanceFromTemplateBootDiskInitializeParams"]:
        '''initialize_params block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#initialize_params GoogleComputeInstanceFromTemplate#initialize_params}
        '''
        result = self._values.get("initialize_params")
        return typing.cast(typing.Optional["GoogleComputeInstanceFromTemplateBootDiskInitializeParams"], result)

    @builtins.property
    def kms_key_self_link(self) -> typing.Optional[builtins.str]:
        '''The self_link of the encryption key that is stored in Google Cloud KMS to encrypt this disk.

        Only one of kms_key_self_link and disk_encryption_key_raw may be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#kms_key_self_link GoogleComputeInstanceFromTemplate#kms_key_self_link}
        '''
        result = self._values.get("kms_key_self_link")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Read/write mode for the disk. One of "READ_ONLY" or "READ_WRITE".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#mode GoogleComputeInstanceFromTemplate#mode}
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''The name or self_link of the disk attached to this instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#source GoogleComputeInstanceFromTemplate#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateBootDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateBootDiskInitializeParams",
    jsii_struct_bases=[],
    name_mapping={
        "image": "image",
        "labels": "labels",
        "size": "size",
        "type": "type",
    },
)
class GoogleComputeInstanceFromTemplateBootDiskInitializeParams:
    def __init__(
        self,
        *,
        image: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        size: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image: The image from which this disk was initialised. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#image GoogleComputeInstanceFromTemplate#image}
        :param labels: A set of key/value label pairs assigned to the disk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#labels GoogleComputeInstanceFromTemplate#labels}
        :param size: The size of the image in gigabytes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#size GoogleComputeInstanceFromTemplate#size}
        :param type: The Google Compute Engine disk type. Such as pd-standard, pd-ssd or pd-balanced. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#type GoogleComputeInstanceFromTemplate#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateBootDiskInitializeParams.__init__)
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if image is not None:
            self._values["image"] = image
        if labels is not None:
            self._values["labels"] = labels
        if size is not None:
            self._values["size"] = size
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def image(self) -> typing.Optional[builtins.str]:
        '''The image from which this disk was initialised.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#image GoogleComputeInstanceFromTemplate#image}
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A set of key/value label pairs assigned to the disk.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#labels GoogleComputeInstanceFromTemplate#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def size(self) -> typing.Optional[jsii.Number]:
        '''The size of the image in gigabytes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#size GoogleComputeInstanceFromTemplate#size}
        '''
        result = self._values.get("size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The Google Compute Engine disk type. Such as pd-standard, pd-ssd or pd-balanced.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#type GoogleComputeInstanceFromTemplate#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateBootDiskInitializeParams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceFromTemplateBootDiskInitializeParamsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateBootDiskInitializeParamsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateBootDiskInitializeParamsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetImage")
    def reset_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImage", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetSize")
    def reset_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSize", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @image.setter
    def image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateBootDiskInitializeParamsOutputReference, "image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "image", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateBootDiskInitializeParamsOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateBootDiskInitializeParamsOutputReference, "size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateBootDiskInitializeParamsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInstanceFromTemplateBootDiskInitializeParams]:
        return typing.cast(typing.Optional[GoogleComputeInstanceFromTemplateBootDiskInitializeParams], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInstanceFromTemplateBootDiskInitializeParams],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateBootDiskInitializeParamsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceFromTemplateBootDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateBootDiskOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateBootDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInitializeParams")
    def put_initialize_params(
        self,
        *,
        image: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        size: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image: The image from which this disk was initialised. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#image GoogleComputeInstanceFromTemplate#image}
        :param labels: A set of key/value label pairs assigned to the disk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#labels GoogleComputeInstanceFromTemplate#labels}
        :param size: The size of the image in gigabytes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#size GoogleComputeInstanceFromTemplate#size}
        :param type: The Google Compute Engine disk type. Such as pd-standard, pd-ssd or pd-balanced. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#type GoogleComputeInstanceFromTemplate#type}
        '''
        value = GoogleComputeInstanceFromTemplateBootDiskInitializeParams(
            image=image, labels=labels, size=size, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putInitializeParams", [value]))

    @jsii.member(jsii_name="resetAutoDelete")
    def reset_auto_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoDelete", []))

    @jsii.member(jsii_name="resetDeviceName")
    def reset_device_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceName", []))

    @jsii.member(jsii_name="resetDiskEncryptionKeyRaw")
    def reset_disk_encryption_key_raw(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskEncryptionKeyRaw", []))

    @jsii.member(jsii_name="resetInitializeParams")
    def reset_initialize_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitializeParams", []))

    @jsii.member(jsii_name="resetKmsKeySelfLink")
    def reset_kms_key_self_link(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeySelfLink", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKeySha256")
    def disk_encryption_key_sha256(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskEncryptionKeySha256"))

    @builtins.property
    @jsii.member(jsii_name="initializeParams")
    def initialize_params(
        self,
    ) -> GoogleComputeInstanceFromTemplateBootDiskInitializeParamsOutputReference:
        return typing.cast(GoogleComputeInstanceFromTemplateBootDiskInitializeParamsOutputReference, jsii.get(self, "initializeParams"))

    @builtins.property
    @jsii.member(jsii_name="autoDeleteInput")
    def auto_delete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoDeleteInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceNameInput")
    def device_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKeyRawInput")
    def disk_encryption_key_raw_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskEncryptionKeyRawInput"))

    @builtins.property
    @jsii.member(jsii_name="initializeParamsInput")
    def initialize_params_input(
        self,
    ) -> typing.Optional[GoogleComputeInstanceFromTemplateBootDiskInitializeParams]:
        return typing.cast(typing.Optional[GoogleComputeInstanceFromTemplateBootDiskInitializeParams], jsii.get(self, "initializeParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeySelfLinkInput")
    def kms_key_self_link_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeySelfLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="autoDelete")
    def auto_delete(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoDelete"))

    @auto_delete.setter
    def auto_delete(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateBootDiskOutputReference, "auto_delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoDelete", value)

    @builtins.property
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceName"))

    @device_name.setter
    def device_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateBootDiskOutputReference, "device_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceName", value)

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKeyRaw")
    def disk_encryption_key_raw(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskEncryptionKeyRaw"))

    @disk_encryption_key_raw.setter
    def disk_encryption_key_raw(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateBootDiskOutputReference, "disk_encryption_key_raw").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskEncryptionKeyRaw", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeySelfLink")
    def kms_key_self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeySelfLink"))

    @kms_key_self_link.setter
    def kms_key_self_link(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateBootDiskOutputReference, "kms_key_self_link").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeySelfLink", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateBootDiskOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateBootDiskOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInstanceFromTemplateBootDisk]:
        return typing.cast(typing.Optional[GoogleComputeInstanceFromTemplateBootDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInstanceFromTemplateBootDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateBootDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateConfidentialInstanceConfig",
    jsii_struct_bases=[],
    name_mapping={"enable_confidential_compute": "enableConfidentialCompute"},
)
class GoogleComputeInstanceFromTemplateConfidentialInstanceConfig:
    def __init__(
        self,
        *,
        enable_confidential_compute: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable_confidential_compute: Defines whether the instance should have confidential compute enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#enable_confidential_compute GoogleComputeInstanceFromTemplate#enable_confidential_compute}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateConfidentialInstanceConfig.__init__)
            check_type(argname="argument enable_confidential_compute", value=enable_confidential_compute, expected_type=type_hints["enable_confidential_compute"])
        self._values: typing.Dict[str, typing.Any] = {
            "enable_confidential_compute": enable_confidential_compute,
        }

    @builtins.property
    def enable_confidential_compute(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Defines whether the instance should have confidential compute enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#enable_confidential_compute GoogleComputeInstanceFromTemplate#enable_confidential_compute}
        '''
        result = self._values.get("enable_confidential_compute")
        assert result is not None, "Required property 'enable_confidential_compute' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateConfidentialInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceFromTemplateConfidentialInstanceConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateConfidentialInstanceConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateConfidentialInstanceConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="enableConfidentialComputeInput")
    def enable_confidential_compute_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableConfidentialComputeInput"))

    @builtins.property
    @jsii.member(jsii_name="enableConfidentialCompute")
    def enable_confidential_compute(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableConfidentialCompute"))

    @enable_confidential_compute.setter
    def enable_confidential_compute(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateConfidentialInstanceConfigOutputReference, "enable_confidential_compute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableConfidentialCompute", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInstanceFromTemplateConfidentialInstanceConfig]:
        return typing.cast(typing.Optional[GoogleComputeInstanceFromTemplateConfidentialInstanceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInstanceFromTemplateConfidentialInstanceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateConfidentialInstanceConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateConfig",
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
        "source_instance_template": "sourceInstanceTemplate",
        "advanced_machine_features": "advancedMachineFeatures",
        "allow_stopping_for_update": "allowStoppingForUpdate",
        "attached_disk": "attachedDisk",
        "boot_disk": "bootDisk",
        "can_ip_forward": "canIpForward",
        "confidential_instance_config": "confidentialInstanceConfig",
        "deletion_protection": "deletionProtection",
        "description": "description",
        "desired_status": "desiredStatus",
        "enable_display": "enableDisplay",
        "guest_accelerator": "guestAccelerator",
        "hostname": "hostname",
        "id": "id",
        "labels": "labels",
        "machine_type": "machineType",
        "metadata": "metadata",
        "metadata_startup_script": "metadataStartupScript",
        "min_cpu_platform": "minCpuPlatform",
        "network_interface": "networkInterface",
        "network_performance_config": "networkPerformanceConfig",
        "project": "project",
        "reservation_affinity": "reservationAffinity",
        "resource_policies": "resourcePolicies",
        "scheduling": "scheduling",
        "scratch_disk": "scratchDisk",
        "service_account": "serviceAccount",
        "shielded_instance_config": "shieldedInstanceConfig",
        "tags": "tags",
        "timeouts": "timeouts",
        "zone": "zone",
    },
)
class GoogleComputeInstanceFromTemplateConfig(cdktf.TerraformMetaArguments):
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
        source_instance_template: builtins.str,
        advanced_machine_features: typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateAdvancedMachineFeatures, typing.Dict[str, typing.Any]]] = None,
        allow_stopping_for_update: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        attached_disk: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeInstanceFromTemplateAttachedDisk, typing.Dict[str, typing.Any]]]]] = None,
        boot_disk: typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateBootDisk, typing.Dict[str, typing.Any]]] = None,
        can_ip_forward: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        confidential_instance_config: typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateConfidentialInstanceConfig, typing.Dict[str, typing.Any]]] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        desired_status: typing.Optional[builtins.str] = None,
        enable_display: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        guest_accelerator: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateGuestAccelerator", typing.Dict[str, typing.Any]]]]] = None,
        hostname: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        machine_type: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        metadata_startup_script: typing.Optional[builtins.str] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        network_interface: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateNetworkInterface", typing.Dict[str, typing.Any]]]]] = None,
        network_performance_config: typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateNetworkPerformanceConfig", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        reservation_affinity: typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateReservationAffinity", typing.Dict[str, typing.Any]]] = None,
        resource_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        scheduling: typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateScheduling", typing.Dict[str, typing.Any]]] = None,
        scratch_disk: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateScratchDisk", typing.Dict[str, typing.Any]]]]] = None,
        service_account: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateServiceAccount", typing.Dict[str, typing.Any]]]]] = None,
        shielded_instance_config: typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateShieldedInstanceConfig", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateTimeouts", typing.Dict[str, typing.Any]]] = None,
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the instance. One of name or self_link must be provided. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#name GoogleComputeInstanceFromTemplate#name}
        :param source_instance_template: Name or self link of an instance template to create the instance based on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#source_instance_template GoogleComputeInstanceFromTemplate#source_instance_template}
        :param advanced_machine_features: advanced_machine_features block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#advanced_machine_features GoogleComputeInstanceFromTemplate#advanced_machine_features}
        :param allow_stopping_for_update: If true, allows Terraform to stop the instance to update its properties. If you try to update a property that requires stopping the instance without setting this field, the update will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#allow_stopping_for_update GoogleComputeInstanceFromTemplate#allow_stopping_for_update}
        :param attached_disk: List of disks attached to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#attached_disk GoogleComputeInstanceFromTemplate#attached_disk}
        :param boot_disk: boot_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#boot_disk GoogleComputeInstanceFromTemplate#boot_disk}
        :param can_ip_forward: Whether sending and receiving of packets with non-matching source or destination IPs is allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#can_ip_forward GoogleComputeInstanceFromTemplate#can_ip_forward}
        :param confidential_instance_config: confidential_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#confidential_instance_config GoogleComputeInstanceFromTemplate#confidential_instance_config}
        :param deletion_protection: Whether deletion protection is enabled on this instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#deletion_protection GoogleComputeInstanceFromTemplate#deletion_protection}
        :param description: A brief description of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#description GoogleComputeInstanceFromTemplate#description}
        :param desired_status: Desired status of the instance. Either "RUNNING" or "TERMINATED". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#desired_status GoogleComputeInstanceFromTemplate#desired_status}
        :param enable_display: Whether the instance has virtual displays enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#enable_display GoogleComputeInstanceFromTemplate#enable_display}
        :param guest_accelerator: List of the type and count of accelerator cards attached to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#guest_accelerator GoogleComputeInstanceFromTemplate#guest_accelerator}
        :param hostname: A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid. Valid format is a series of labels 1-63 characters long matching the regular expression `a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_, concatenated with periods. The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#hostname GoogleComputeInstanceFromTemplate#hostname}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#id GoogleComputeInstanceFromTemplate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: A set of key/value label pairs assigned to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#labels GoogleComputeInstanceFromTemplate#labels}
        :param machine_type: The machine type to create. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#machine_type GoogleComputeInstanceFromTemplate#machine_type}
        :param metadata: Metadata key/value pairs made available within the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#metadata GoogleComputeInstanceFromTemplate#metadata}
        :param metadata_startup_script: Metadata startup scripts made available within the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#metadata_startup_script GoogleComputeInstanceFromTemplate#metadata_startup_script}
        :param min_cpu_platform: The minimum CPU platform specified for the VM instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#min_cpu_platform GoogleComputeInstanceFromTemplate#min_cpu_platform}
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#network_interface GoogleComputeInstanceFromTemplate#network_interface}
        :param network_performance_config: network_performance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#network_performance_config GoogleComputeInstanceFromTemplate#network_performance_config}
        :param project: The ID of the project in which the resource belongs. If self_link is provided, this value is ignored. If neither self_link nor project are provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#project GoogleComputeInstanceFromTemplate#project}
        :param reservation_affinity: reservation_affinity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#reservation_affinity GoogleComputeInstanceFromTemplate#reservation_affinity}
        :param resource_policies: A list of self_links of resource policies to attach to the instance. Currently a max of 1 resource policy is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#resource_policies GoogleComputeInstanceFromTemplate#resource_policies}
        :param scheduling: scheduling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#scheduling GoogleComputeInstanceFromTemplate#scheduling}
        :param scratch_disk: The scratch disks attached to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#scratch_disk GoogleComputeInstanceFromTemplate#scratch_disk}
        :param service_account: The service account to attach to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#service_account GoogleComputeInstanceFromTemplate#service_account}
        :param shielded_instance_config: shielded_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#shielded_instance_config GoogleComputeInstanceFromTemplate#shielded_instance_config}
        :param tags: The list of tags attached to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#tags GoogleComputeInstanceFromTemplate#tags}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#timeouts GoogleComputeInstanceFromTemplate#timeouts}
        :param zone: The zone of the instance. If self_link is provided, this value is ignored. If neither self_link nor zone are provided, the provider zone is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#zone GoogleComputeInstanceFromTemplate#zone}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(advanced_machine_features, dict):
            advanced_machine_features = GoogleComputeInstanceFromTemplateAdvancedMachineFeatures(**advanced_machine_features)
        if isinstance(boot_disk, dict):
            boot_disk = GoogleComputeInstanceFromTemplateBootDisk(**boot_disk)
        if isinstance(confidential_instance_config, dict):
            confidential_instance_config = GoogleComputeInstanceFromTemplateConfidentialInstanceConfig(**confidential_instance_config)
        if isinstance(network_performance_config, dict):
            network_performance_config = GoogleComputeInstanceFromTemplateNetworkPerformanceConfig(**network_performance_config)
        if isinstance(reservation_affinity, dict):
            reservation_affinity = GoogleComputeInstanceFromTemplateReservationAffinity(**reservation_affinity)
        if isinstance(scheduling, dict):
            scheduling = GoogleComputeInstanceFromTemplateScheduling(**scheduling)
        if isinstance(shielded_instance_config, dict):
            shielded_instance_config = GoogleComputeInstanceFromTemplateShieldedInstanceConfig(**shielded_instance_config)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeInstanceFromTemplateTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_instance_template", value=source_instance_template, expected_type=type_hints["source_instance_template"])
            check_type(argname="argument advanced_machine_features", value=advanced_machine_features, expected_type=type_hints["advanced_machine_features"])
            check_type(argname="argument allow_stopping_for_update", value=allow_stopping_for_update, expected_type=type_hints["allow_stopping_for_update"])
            check_type(argname="argument attached_disk", value=attached_disk, expected_type=type_hints["attached_disk"])
            check_type(argname="argument boot_disk", value=boot_disk, expected_type=type_hints["boot_disk"])
            check_type(argname="argument can_ip_forward", value=can_ip_forward, expected_type=type_hints["can_ip_forward"])
            check_type(argname="argument confidential_instance_config", value=confidential_instance_config, expected_type=type_hints["confidential_instance_config"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument desired_status", value=desired_status, expected_type=type_hints["desired_status"])
            check_type(argname="argument enable_display", value=enable_display, expected_type=type_hints["enable_display"])
            check_type(argname="argument guest_accelerator", value=guest_accelerator, expected_type=type_hints["guest_accelerator"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument metadata_startup_script", value=metadata_startup_script, expected_type=type_hints["metadata_startup_script"])
            check_type(argname="argument min_cpu_platform", value=min_cpu_platform, expected_type=type_hints["min_cpu_platform"])
            check_type(argname="argument network_interface", value=network_interface, expected_type=type_hints["network_interface"])
            check_type(argname="argument network_performance_config", value=network_performance_config, expected_type=type_hints["network_performance_config"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument reservation_affinity", value=reservation_affinity, expected_type=type_hints["reservation_affinity"])
            check_type(argname="argument resource_policies", value=resource_policies, expected_type=type_hints["resource_policies"])
            check_type(argname="argument scheduling", value=scheduling, expected_type=type_hints["scheduling"])
            check_type(argname="argument scratch_disk", value=scratch_disk, expected_type=type_hints["scratch_disk"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument shielded_instance_config", value=shielded_instance_config, expected_type=type_hints["shielded_instance_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "source_instance_template": source_instance_template,
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
        if advanced_machine_features is not None:
            self._values["advanced_machine_features"] = advanced_machine_features
        if allow_stopping_for_update is not None:
            self._values["allow_stopping_for_update"] = allow_stopping_for_update
        if attached_disk is not None:
            self._values["attached_disk"] = attached_disk
        if boot_disk is not None:
            self._values["boot_disk"] = boot_disk
        if can_ip_forward is not None:
            self._values["can_ip_forward"] = can_ip_forward
        if confidential_instance_config is not None:
            self._values["confidential_instance_config"] = confidential_instance_config
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if description is not None:
            self._values["description"] = description
        if desired_status is not None:
            self._values["desired_status"] = desired_status
        if enable_display is not None:
            self._values["enable_display"] = enable_display
        if guest_accelerator is not None:
            self._values["guest_accelerator"] = guest_accelerator
        if hostname is not None:
            self._values["hostname"] = hostname
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if machine_type is not None:
            self._values["machine_type"] = machine_type
        if metadata is not None:
            self._values["metadata"] = metadata
        if metadata_startup_script is not None:
            self._values["metadata_startup_script"] = metadata_startup_script
        if min_cpu_platform is not None:
            self._values["min_cpu_platform"] = min_cpu_platform
        if network_interface is not None:
            self._values["network_interface"] = network_interface
        if network_performance_config is not None:
            self._values["network_performance_config"] = network_performance_config
        if project is not None:
            self._values["project"] = project
        if reservation_affinity is not None:
            self._values["reservation_affinity"] = reservation_affinity
        if resource_policies is not None:
            self._values["resource_policies"] = resource_policies
        if scheduling is not None:
            self._values["scheduling"] = scheduling
        if scratch_disk is not None:
            self._values["scratch_disk"] = scratch_disk
        if service_account is not None:
            self._values["service_account"] = service_account
        if shielded_instance_config is not None:
            self._values["shielded_instance_config"] = shielded_instance_config
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if zone is not None:
            self._values["zone"] = zone

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
        '''The name of the instance. One of name or self_link must be provided.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#name GoogleComputeInstanceFromTemplate#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_instance_template(self) -> builtins.str:
        '''Name or self link of an instance template to create the instance based on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#source_instance_template GoogleComputeInstanceFromTemplate#source_instance_template}
        '''
        result = self._values.get("source_instance_template")
        assert result is not None, "Required property 'source_instance_template' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def advanced_machine_features(
        self,
    ) -> typing.Optional[GoogleComputeInstanceFromTemplateAdvancedMachineFeatures]:
        '''advanced_machine_features block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#advanced_machine_features GoogleComputeInstanceFromTemplate#advanced_machine_features}
        '''
        result = self._values.get("advanced_machine_features")
        return typing.cast(typing.Optional[GoogleComputeInstanceFromTemplateAdvancedMachineFeatures], result)

    @builtins.property
    def allow_stopping_for_update(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, allows Terraform to stop the instance to update its properties.

        If you try to update a property that requires stopping the instance without setting this field, the update will fail.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#allow_stopping_for_update GoogleComputeInstanceFromTemplate#allow_stopping_for_update}
        '''
        result = self._values.get("allow_stopping_for_update")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def attached_disk(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateAttachedDisk]]]:
        '''List of disks attached to the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#attached_disk GoogleComputeInstanceFromTemplate#attached_disk}
        '''
        result = self._values.get("attached_disk")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateAttachedDisk]]], result)

    @builtins.property
    def boot_disk(self) -> typing.Optional[GoogleComputeInstanceFromTemplateBootDisk]:
        '''boot_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#boot_disk GoogleComputeInstanceFromTemplate#boot_disk}
        '''
        result = self._values.get("boot_disk")
        return typing.cast(typing.Optional[GoogleComputeInstanceFromTemplateBootDisk], result)

    @builtins.property
    def can_ip_forward(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether sending and receiving of packets with non-matching source or destination IPs is allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#can_ip_forward GoogleComputeInstanceFromTemplate#can_ip_forward}
        '''
        result = self._values.get("can_ip_forward")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def confidential_instance_config(
        self,
    ) -> typing.Optional[GoogleComputeInstanceFromTemplateConfidentialInstanceConfig]:
        '''confidential_instance_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#confidential_instance_config GoogleComputeInstanceFromTemplate#confidential_instance_config}
        '''
        result = self._values.get("confidential_instance_config")
        return typing.cast(typing.Optional[GoogleComputeInstanceFromTemplateConfidentialInstanceConfig], result)

    @builtins.property
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether deletion protection is enabled on this instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#deletion_protection GoogleComputeInstanceFromTemplate#deletion_protection}
        '''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A brief description of the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#description GoogleComputeInstanceFromTemplate#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def desired_status(self) -> typing.Optional[builtins.str]:
        '''Desired status of the instance. Either "RUNNING" or "TERMINATED".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#desired_status GoogleComputeInstanceFromTemplate#desired_status}
        '''
        result = self._values.get("desired_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_display(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the instance has virtual displays enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#enable_display GoogleComputeInstanceFromTemplate#enable_display}
        '''
        result = self._values.get("enable_display")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def guest_accelerator(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateGuestAccelerator"]]]:
        '''List of the type and count of accelerator cards attached to the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#guest_accelerator GoogleComputeInstanceFromTemplate#guest_accelerator}
        '''
        result = self._values.get("guest_accelerator")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateGuestAccelerator"]]], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''A custom hostname for the instance.

        Must be a fully qualified DNS name and RFC-1035-valid. Valid format is a series of labels 1-63 characters long matching the regular expression `a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_, concatenated with periods. The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#hostname GoogleComputeInstanceFromTemplate#hostname}
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#id GoogleComputeInstanceFromTemplate#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A set of key/value label pairs assigned to the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#labels GoogleComputeInstanceFromTemplate#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def machine_type(self) -> typing.Optional[builtins.str]:
        '''The machine type to create.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#machine_type GoogleComputeInstanceFromTemplate#machine_type}
        '''
        result = self._values.get("machine_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Metadata key/value pairs made available within the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#metadata GoogleComputeInstanceFromTemplate#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def metadata_startup_script(self) -> typing.Optional[builtins.str]:
        '''Metadata startup scripts made available within the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#metadata_startup_script GoogleComputeInstanceFromTemplate#metadata_startup_script}
        '''
        result = self._values.get("metadata_startup_script")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_cpu_platform(self) -> typing.Optional[builtins.str]:
        '''The minimum CPU platform specified for the VM instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#min_cpu_platform GoogleComputeInstanceFromTemplate#min_cpu_platform}
        '''
        result = self._values.get("min_cpu_platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_interface(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateNetworkInterface"]]]:
        '''network_interface block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#network_interface GoogleComputeInstanceFromTemplate#network_interface}
        '''
        result = self._values.get("network_interface")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateNetworkInterface"]]], result)

    @builtins.property
    def network_performance_config(
        self,
    ) -> typing.Optional["GoogleComputeInstanceFromTemplateNetworkPerformanceConfig"]:
        '''network_performance_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#network_performance_config GoogleComputeInstanceFromTemplate#network_performance_config}
        '''
        result = self._values.get("network_performance_config")
        return typing.cast(typing.Optional["GoogleComputeInstanceFromTemplateNetworkPerformanceConfig"], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The ID of the project in which the resource belongs.

        If self_link is provided, this value is ignored. If neither self_link nor project are provided, the provider project is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#project GoogleComputeInstanceFromTemplate#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reservation_affinity(
        self,
    ) -> typing.Optional["GoogleComputeInstanceFromTemplateReservationAffinity"]:
        '''reservation_affinity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#reservation_affinity GoogleComputeInstanceFromTemplate#reservation_affinity}
        '''
        result = self._values.get("reservation_affinity")
        return typing.cast(typing.Optional["GoogleComputeInstanceFromTemplateReservationAffinity"], result)

    @builtins.property
    def resource_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of self_links of resource policies to attach to the instance.

        Currently a max of 1 resource policy is supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#resource_policies GoogleComputeInstanceFromTemplate#resource_policies}
        '''
        result = self._values.get("resource_policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def scheduling(
        self,
    ) -> typing.Optional["GoogleComputeInstanceFromTemplateScheduling"]:
        '''scheduling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#scheduling GoogleComputeInstanceFromTemplate#scheduling}
        '''
        result = self._values.get("scheduling")
        return typing.cast(typing.Optional["GoogleComputeInstanceFromTemplateScheduling"], result)

    @builtins.property
    def scratch_disk(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateScratchDisk"]]]:
        '''The scratch disks attached to the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#scratch_disk GoogleComputeInstanceFromTemplate#scratch_disk}
        '''
        result = self._values.get("scratch_disk")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateScratchDisk"]]], result)

    @builtins.property
    def service_account(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateServiceAccount"]]]:
        '''The service account to attach to the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#service_account GoogleComputeInstanceFromTemplate#service_account}
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateServiceAccount"]]], result)

    @builtins.property
    def shielded_instance_config(
        self,
    ) -> typing.Optional["GoogleComputeInstanceFromTemplateShieldedInstanceConfig"]:
        '''shielded_instance_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#shielded_instance_config GoogleComputeInstanceFromTemplate#shielded_instance_config}
        '''
        result = self._values.get("shielded_instance_config")
        return typing.cast(typing.Optional["GoogleComputeInstanceFromTemplateShieldedInstanceConfig"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of tags attached to the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#tags GoogleComputeInstanceFromTemplate#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeInstanceFromTemplateTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#timeouts GoogleComputeInstanceFromTemplate#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeInstanceFromTemplateTimeouts"], result)

    @builtins.property
    def zone(self) -> typing.Optional[builtins.str]:
        '''The zone of the instance.

        If self_link is provided, this value is ignored. If neither self_link nor zone are provided, the provider zone is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#zone GoogleComputeInstanceFromTemplate#zone}
        '''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateGuestAccelerator",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "type": "type"},
)
class GoogleComputeInstanceFromTemplateGuestAccelerator:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#count GoogleComputeInstanceFromTemplate#count}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#type GoogleComputeInstanceFromTemplate#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateGuestAccelerator.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#count GoogleComputeInstanceFromTemplate#count}.'''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#type GoogleComputeInstanceFromTemplate#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateGuestAccelerator(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceFromTemplateGuestAcceleratorList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateGuestAcceleratorList",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateGuestAcceleratorList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeInstanceFromTemplateGuestAcceleratorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateGuestAcceleratorList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeInstanceFromTemplateGuestAcceleratorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateGuestAcceleratorList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateGuestAcceleratorList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateGuestAcceleratorList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateGuestAccelerator]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateGuestAccelerator]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateGuestAccelerator]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateGuestAcceleratorList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceFromTemplateGuestAcceleratorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateGuestAcceleratorOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateGuestAcceleratorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateGuestAcceleratorOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateGuestAcceleratorOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateGuestAccelerator, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateGuestAccelerator, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateGuestAccelerator, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateGuestAcceleratorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateNetworkInterface",
    jsii_struct_bases=[],
    name_mapping={
        "access_config": "accessConfig",
        "alias_ip_range": "aliasIpRange",
        "ipv6_access_config": "ipv6AccessConfig",
        "network": "network",
        "network_ip": "networkIp",
        "nic_type": "nicType",
        "queue_count": "queueCount",
        "stack_type": "stackType",
        "subnetwork": "subnetwork",
        "subnetwork_project": "subnetworkProject",
    },
)
class GoogleComputeInstanceFromTemplateNetworkInterface:
    def __init__(
        self,
        *,
        access_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfig", typing.Dict[str, typing.Any]]]]] = None,
        alias_ip_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRange", typing.Dict[str, typing.Any]]]]] = None,
        ipv6_access_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfig", typing.Dict[str, typing.Any]]]]] = None,
        network: typing.Optional[builtins.str] = None,
        network_ip: typing.Optional[builtins.str] = None,
        nic_type: typing.Optional[builtins.str] = None,
        queue_count: typing.Optional[jsii.Number] = None,
        stack_type: typing.Optional[builtins.str] = None,
        subnetwork: typing.Optional[builtins.str] = None,
        subnetwork_project: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_config: Access configurations, i.e. IPs via which this instance can be accessed via the Internet. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#access_config GoogleComputeInstanceFromTemplate#access_config}
        :param alias_ip_range: An array of alias IP ranges for this network interface. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#alias_ip_range GoogleComputeInstanceFromTemplate#alias_ip_range}
        :param ipv6_access_config: ipv6_access_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#ipv6_access_config GoogleComputeInstanceFromTemplate#ipv6_access_config}
        :param network: The name or self_link of the network attached to this interface. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#network GoogleComputeInstanceFromTemplate#network}
        :param network_ip: The private IP address assigned to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#network_ip GoogleComputeInstanceFromTemplate#network_ip}
        :param nic_type: The type of vNIC to be used on this interface. Possible values:GVNIC, VIRTIO_NET. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#nic_type GoogleComputeInstanceFromTemplate#nic_type}
        :param queue_count: The networking queue count that's specified by users for the network interface. Both Rx and Tx queues will be set to this number. It will be empty if not specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#queue_count GoogleComputeInstanceFromTemplate#queue_count}
        :param stack_type: The stack type for this network interface to identify whether the IPv6 feature is enabled or not. If not specified, IPV4_ONLY will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#stack_type GoogleComputeInstanceFromTemplate#stack_type}
        :param subnetwork: The name or self_link of the subnetwork attached to this interface. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#subnetwork GoogleComputeInstanceFromTemplate#subnetwork}
        :param subnetwork_project: The project in which the subnetwork belongs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#subnetwork_project GoogleComputeInstanceFromTemplate#subnetwork_project}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterface.__init__)
            check_type(argname="argument access_config", value=access_config, expected_type=type_hints["access_config"])
            check_type(argname="argument alias_ip_range", value=alias_ip_range, expected_type=type_hints["alias_ip_range"])
            check_type(argname="argument ipv6_access_config", value=ipv6_access_config, expected_type=type_hints["ipv6_access_config"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument network_ip", value=network_ip, expected_type=type_hints["network_ip"])
            check_type(argname="argument nic_type", value=nic_type, expected_type=type_hints["nic_type"])
            check_type(argname="argument queue_count", value=queue_count, expected_type=type_hints["queue_count"])
            check_type(argname="argument stack_type", value=stack_type, expected_type=type_hints["stack_type"])
            check_type(argname="argument subnetwork", value=subnetwork, expected_type=type_hints["subnetwork"])
            check_type(argname="argument subnetwork_project", value=subnetwork_project, expected_type=type_hints["subnetwork_project"])
        self._values: typing.Dict[str, typing.Any] = {}
        if access_config is not None:
            self._values["access_config"] = access_config
        if alias_ip_range is not None:
            self._values["alias_ip_range"] = alias_ip_range
        if ipv6_access_config is not None:
            self._values["ipv6_access_config"] = ipv6_access_config
        if network is not None:
            self._values["network"] = network
        if network_ip is not None:
            self._values["network_ip"] = network_ip
        if nic_type is not None:
            self._values["nic_type"] = nic_type
        if queue_count is not None:
            self._values["queue_count"] = queue_count
        if stack_type is not None:
            self._values["stack_type"] = stack_type
        if subnetwork is not None:
            self._values["subnetwork"] = subnetwork
        if subnetwork_project is not None:
            self._values["subnetwork_project"] = subnetwork_project

    @builtins.property
    def access_config(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfig"]]]:
        '''Access configurations, i.e. IPs via which this instance can be accessed via the Internet.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#access_config GoogleComputeInstanceFromTemplate#access_config}
        '''
        result = self._values.get("access_config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfig"]]], result)

    @builtins.property
    def alias_ip_range(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRange"]]]:
        '''An array of alias IP ranges for this network interface.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#alias_ip_range GoogleComputeInstanceFromTemplate#alias_ip_range}
        '''
        result = self._values.get("alias_ip_range")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRange"]]], result)

    @builtins.property
    def ipv6_access_config(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfig"]]]:
        '''ipv6_access_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#ipv6_access_config GoogleComputeInstanceFromTemplate#ipv6_access_config}
        '''
        result = self._values.get("ipv6_access_config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfig"]]], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''The name or self_link of the network attached to this interface.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#network GoogleComputeInstanceFromTemplate#network}
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_ip(self) -> typing.Optional[builtins.str]:
        '''The private IP address assigned to the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#network_ip GoogleComputeInstanceFromTemplate#network_ip}
        '''
        result = self._values.get("network_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nic_type(self) -> typing.Optional[builtins.str]:
        '''The type of vNIC to be used on this interface. Possible values:GVNIC, VIRTIO_NET.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#nic_type GoogleComputeInstanceFromTemplate#nic_type}
        '''
        result = self._values.get("nic_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def queue_count(self) -> typing.Optional[jsii.Number]:
        '''The networking queue count that's specified by users for the network interface.

        Both Rx and Tx queues will be set to this number. It will be empty if not specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#queue_count GoogleComputeInstanceFromTemplate#queue_count}
        '''
        result = self._values.get("queue_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stack_type(self) -> typing.Optional[builtins.str]:
        '''The stack type for this network interface to identify whether the IPv6 feature is enabled or not.

        If not specified, IPV4_ONLY will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#stack_type GoogleComputeInstanceFromTemplate#stack_type}
        '''
        result = self._values.get("stack_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnetwork(self) -> typing.Optional[builtins.str]:
        '''The name or self_link of the subnetwork attached to this interface.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#subnetwork GoogleComputeInstanceFromTemplate#subnetwork}
        '''
        result = self._values.get("subnetwork")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnetwork_project(self) -> typing.Optional[builtins.str]:
        '''The project in which the subnetwork belongs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#subnetwork_project GoogleComputeInstanceFromTemplate#subnetwork_project}
        '''
        result = self._values.get("subnetwork_project")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateNetworkInterface(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfig",
    jsii_struct_bases=[],
    name_mapping={
        "nat_ip": "natIp",
        "network_tier": "networkTier",
        "public_ptr_domain_name": "publicPtrDomainName",
    },
)
class GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfig:
    def __init__(
        self,
        *,
        nat_ip: typing.Optional[builtins.str] = None,
        network_tier: typing.Optional[builtins.str] = None,
        public_ptr_domain_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param nat_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#nat_ip GoogleComputeInstanceFromTemplate#nat_ip}.
        :param network_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#network_tier GoogleComputeInstanceFromTemplate#network_tier}.
        :param public_ptr_domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#public_ptr_domain_name GoogleComputeInstanceFromTemplate#public_ptr_domain_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfig.__init__)
            check_type(argname="argument nat_ip", value=nat_ip, expected_type=type_hints["nat_ip"])
            check_type(argname="argument network_tier", value=network_tier, expected_type=type_hints["network_tier"])
            check_type(argname="argument public_ptr_domain_name", value=public_ptr_domain_name, expected_type=type_hints["public_ptr_domain_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if nat_ip is not None:
            self._values["nat_ip"] = nat_ip
        if network_tier is not None:
            self._values["network_tier"] = network_tier
        if public_ptr_domain_name is not None:
            self._values["public_ptr_domain_name"] = public_ptr_domain_name

    @builtins.property
    def nat_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#nat_ip GoogleComputeInstanceFromTemplate#nat_ip}.'''
        result = self._values.get("nat_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_tier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#network_tier GoogleComputeInstanceFromTemplate#network_tier}.'''
        result = self._values.get("network_tier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_ptr_domain_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#public_ptr_domain_name GoogleComputeInstanceFromTemplate#public_ptr_domain_name}.'''
        result = self._values.get("public_ptr_domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigList",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNatIp")
    def reset_nat_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNatIp", []))

    @jsii.member(jsii_name="resetNetworkTier")
    def reset_network_tier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkTier", []))

    @jsii.member(jsii_name="resetPublicPtrDomainName")
    def reset_public_ptr_domain_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicPtrDomainName", []))

    @builtins.property
    @jsii.member(jsii_name="natIpInput")
    def nat_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "natIpInput"))

    @builtins.property
    @jsii.member(jsii_name="networkTierInput")
    def network_tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkTierInput"))

    @builtins.property
    @jsii.member(jsii_name="publicPtrDomainNameInput")
    def public_ptr_domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicPtrDomainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="natIp")
    def nat_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "natIp"))

    @nat_ip.setter
    def nat_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigOutputReference, "nat_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "natIp", value)

    @builtins.property
    @jsii.member(jsii_name="networkTier")
    def network_tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkTier"))

    @network_tier.setter
    def network_tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigOutputReference, "network_tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkTier", value)

    @builtins.property
    @jsii.member(jsii_name="publicPtrDomainName")
    def public_ptr_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicPtrDomainName"))

    @public_ptr_domain_name.setter
    def public_ptr_domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigOutputReference, "public_ptr_domain_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicPtrDomainName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfig, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfig, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfig, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRange",
    jsii_struct_bases=[],
    name_mapping={
        "ip_cidr_range": "ipCidrRange",
        "subnetwork_range_name": "subnetworkRangeName",
    },
)
class GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRange:
    def __init__(
        self,
        *,
        ip_cidr_range: typing.Optional[builtins.str] = None,
        subnetwork_range_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ip_cidr_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#ip_cidr_range GoogleComputeInstanceFromTemplate#ip_cidr_range}.
        :param subnetwork_range_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#subnetwork_range_name GoogleComputeInstanceFromTemplate#subnetwork_range_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRange.__init__)
            check_type(argname="argument ip_cidr_range", value=ip_cidr_range, expected_type=type_hints["ip_cidr_range"])
            check_type(argname="argument subnetwork_range_name", value=subnetwork_range_name, expected_type=type_hints["subnetwork_range_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ip_cidr_range is not None:
            self._values["ip_cidr_range"] = ip_cidr_range
        if subnetwork_range_name is not None:
            self._values["subnetwork_range_name"] = subnetwork_range_name

    @builtins.property
    def ip_cidr_range(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#ip_cidr_range GoogleComputeInstanceFromTemplate#ip_cidr_range}.'''
        result = self._values.get("ip_cidr_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnetwork_range_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#subnetwork_range_name GoogleComputeInstanceFromTemplate#subnetwork_range_name}.'''
        result = self._values.get("subnetwork_range_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeList",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIpCidrRange")
    def reset_ip_cidr_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpCidrRange", []))

    @jsii.member(jsii_name="resetSubnetworkRangeName")
    def reset_subnetwork_range_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetworkRangeName", []))

    @builtins.property
    @jsii.member(jsii_name="ipCidrRangeInput")
    def ip_cidr_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipCidrRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetworkRangeNameInput")
    def subnetwork_range_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetworkRangeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="ipCidrRange")
    def ip_cidr_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipCidrRange"))

    @ip_cidr_range.setter
    def ip_cidr_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeOutputReference, "ip_cidr_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipCidrRange", value)

    @builtins.property
    @jsii.member(jsii_name="subnetworkRangeName")
    def subnetwork_range_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetworkRangeName"))

    @subnetwork_range_name.setter
    def subnetwork_range_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeOutputReference, "subnetwork_range_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetworkRangeName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRange, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRange, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRange, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfig",
    jsii_struct_bases=[],
    name_mapping={
        "network_tier": "networkTier",
        "public_ptr_domain_name": "publicPtrDomainName",
    },
)
class GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfig:
    def __init__(
        self,
        *,
        network_tier: builtins.str,
        public_ptr_domain_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param network_tier: The service-level to be provided for IPv6 traffic when the subnet has an external subnet. Only PREMIUM tier is valid for IPv6 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#network_tier GoogleComputeInstanceFromTemplate#network_tier}
        :param public_ptr_domain_name: The domain name to be used when creating DNSv6 records for the external IPv6 ranges. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#public_ptr_domain_name GoogleComputeInstanceFromTemplate#public_ptr_domain_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfig.__init__)
            check_type(argname="argument network_tier", value=network_tier, expected_type=type_hints["network_tier"])
            check_type(argname="argument public_ptr_domain_name", value=public_ptr_domain_name, expected_type=type_hints["public_ptr_domain_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "network_tier": network_tier,
        }
        if public_ptr_domain_name is not None:
            self._values["public_ptr_domain_name"] = public_ptr_domain_name

    @builtins.property
    def network_tier(self) -> builtins.str:
        '''The service-level to be provided for IPv6 traffic when the subnet has an external subnet.

        Only PREMIUM tier is valid for IPv6

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#network_tier GoogleComputeInstanceFromTemplate#network_tier}
        '''
        result = self._values.get("network_tier")
        assert result is not None, "Required property 'network_tier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def public_ptr_domain_name(self) -> typing.Optional[builtins.str]:
        '''The domain name to be used when creating DNSv6 records for the external IPv6 ranges.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#public_ptr_domain_name GoogleComputeInstanceFromTemplate#public_ptr_domain_name}
        '''
        result = self._values.get("public_ptr_domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigList",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPublicPtrDomainName")
    def reset_public_ptr_domain_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicPtrDomainName", []))

    @builtins.property
    @jsii.member(jsii_name="externalIpv6")
    def external_ipv6(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalIpv6"))

    @builtins.property
    @jsii.member(jsii_name="externalIpv6PrefixLength")
    def external_ipv6_prefix_length(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalIpv6PrefixLength"))

    @builtins.property
    @jsii.member(jsii_name="networkTierInput")
    def network_tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkTierInput"))

    @builtins.property
    @jsii.member(jsii_name="publicPtrDomainNameInput")
    def public_ptr_domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicPtrDomainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkTier")
    def network_tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkTier"))

    @network_tier.setter
    def network_tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigOutputReference, "network_tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkTier", value)

    @builtins.property
    @jsii.member(jsii_name="publicPtrDomainName")
    def public_ptr_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicPtrDomainName"))

    @public_ptr_domain_name.setter
    def public_ptr_domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigOutputReference, "public_ptr_domain_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicPtrDomainName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfig, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfig, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfig, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceFromTemplateNetworkInterfaceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateNetworkInterfaceList",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterfaceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeInstanceFromTemplateNetworkInterfaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterfaceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeInstanceFromTemplateNetworkInterfaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateNetworkInterface]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateNetworkInterface]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateNetworkInterface]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceFromTemplateNetworkInterfaceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateNetworkInterfaceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterfaceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAccessConfig")
    def put_access_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfig, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterfaceOutputReference.put_access_config)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccessConfig", [value]))

    @jsii.member(jsii_name="putAliasIpRange")
    def put_alias_ip_range(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRange, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterfaceOutputReference.put_alias_ip_range)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAliasIpRange", [value]))

    @jsii.member(jsii_name="putIpv6AccessConfig")
    def put_ipv6_access_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfig, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkInterfaceOutputReference.put_ipv6_access_config)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpv6AccessConfig", [value]))

    @jsii.member(jsii_name="resetAccessConfig")
    def reset_access_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessConfig", []))

    @jsii.member(jsii_name="resetAliasIpRange")
    def reset_alias_ip_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAliasIpRange", []))

    @jsii.member(jsii_name="resetIpv6AccessConfig")
    def reset_ipv6_access_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6AccessConfig", []))

    @jsii.member(jsii_name="resetNetwork")
    def reset_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetwork", []))

    @jsii.member(jsii_name="resetNetworkIp")
    def reset_network_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkIp", []))

    @jsii.member(jsii_name="resetNicType")
    def reset_nic_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNicType", []))

    @jsii.member(jsii_name="resetQueueCount")
    def reset_queue_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueueCount", []))

    @jsii.member(jsii_name="resetStackType")
    def reset_stack_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStackType", []))

    @jsii.member(jsii_name="resetSubnetwork")
    def reset_subnetwork(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetwork", []))

    @jsii.member(jsii_name="resetSubnetworkProject")
    def reset_subnetwork_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetworkProject", []))

    @builtins.property
    @jsii.member(jsii_name="accessConfig")
    def access_config(
        self,
    ) -> GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigList:
        return typing.cast(GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigList, jsii.get(self, "accessConfig"))

    @builtins.property
    @jsii.member(jsii_name="aliasIpRange")
    def alias_ip_range(
        self,
    ) -> GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeList:
        return typing.cast(GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeList, jsii.get(self, "aliasIpRange"))

    @builtins.property
    @jsii.member(jsii_name="ipv6AccessConfig")
    def ipv6_access_config(
        self,
    ) -> GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigList:
        return typing.cast(GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigList, jsii.get(self, "ipv6AccessConfig"))

    @builtins.property
    @jsii.member(jsii_name="ipv6AccessType")
    def ipv6_access_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv6AccessType"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="accessConfigInput")
    def access_config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfig]]], jsii.get(self, "accessConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasIpRangeInput")
    def alias_ip_range_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRange]]], jsii.get(self, "aliasIpRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6AccessConfigInput")
    def ipv6_access_config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfig]]], jsii.get(self, "ipv6AccessConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="networkIpInput")
    def network_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkIpInput"))

    @builtins.property
    @jsii.member(jsii_name="nicTypeInput")
    def nic_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nicTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="queueCountInput")
    def queue_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "queueCountInput"))

    @builtins.property
    @jsii.member(jsii_name="stackTypeInput")
    def stack_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stackTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetworkInput")
    def subnetwork_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetworkProjectInput")
    def subnetwork_project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetworkProjectInput"))

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceOutputReference, "network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="networkIp")
    def network_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkIp"))

    @network_ip.setter
    def network_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceOutputReference, "network_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkIp", value)

    @builtins.property
    @jsii.member(jsii_name="nicType")
    def nic_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nicType"))

    @nic_type.setter
    def nic_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceOutputReference, "nic_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nicType", value)

    @builtins.property
    @jsii.member(jsii_name="queueCount")
    def queue_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "queueCount"))

    @queue_count.setter
    def queue_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceOutputReference, "queue_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queueCount", value)

    @builtins.property
    @jsii.member(jsii_name="stackType")
    def stack_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stackType"))

    @stack_type.setter
    def stack_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceOutputReference, "stack_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackType", value)

    @builtins.property
    @jsii.member(jsii_name="subnetwork")
    def subnetwork(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetwork"))

    @subnetwork.setter
    def subnetwork(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceOutputReference, "subnetwork").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetwork", value)

    @builtins.property
    @jsii.member(jsii_name="subnetworkProject")
    def subnetwork_project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetworkProject"))

    @subnetwork_project.setter
    def subnetwork_project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceOutputReference, "subnetwork_project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetworkProject", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateNetworkInterface, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateNetworkInterface, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateNetworkInterface, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkInterfaceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateNetworkPerformanceConfig",
    jsii_struct_bases=[],
    name_mapping={"total_egress_bandwidth_tier": "totalEgressBandwidthTier"},
)
class GoogleComputeInstanceFromTemplateNetworkPerformanceConfig:
    def __init__(self, *, total_egress_bandwidth_tier: builtins.str) -> None:
        '''
        :param total_egress_bandwidth_tier: The egress bandwidth tier to enable. Possible values:TIER_1, DEFAULT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#total_egress_bandwidth_tier GoogleComputeInstanceFromTemplate#total_egress_bandwidth_tier}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkPerformanceConfig.__init__)
            check_type(argname="argument total_egress_bandwidth_tier", value=total_egress_bandwidth_tier, expected_type=type_hints["total_egress_bandwidth_tier"])
        self._values: typing.Dict[str, typing.Any] = {
            "total_egress_bandwidth_tier": total_egress_bandwidth_tier,
        }

    @builtins.property
    def total_egress_bandwidth_tier(self) -> builtins.str:
        '''The egress bandwidth tier to enable. Possible values:TIER_1, DEFAULT.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#total_egress_bandwidth_tier GoogleComputeInstanceFromTemplate#total_egress_bandwidth_tier}
        '''
        result = self._values.get("total_egress_bandwidth_tier")
        assert result is not None, "Required property 'total_egress_bandwidth_tier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateNetworkPerformanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceFromTemplateNetworkPerformanceConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateNetworkPerformanceConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateNetworkPerformanceConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="totalEgressBandwidthTierInput")
    def total_egress_bandwidth_tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "totalEgressBandwidthTierInput"))

    @builtins.property
    @jsii.member(jsii_name="totalEgressBandwidthTier")
    def total_egress_bandwidth_tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "totalEgressBandwidthTier"))

    @total_egress_bandwidth_tier.setter
    def total_egress_bandwidth_tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkPerformanceConfigOutputReference, "total_egress_bandwidth_tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "totalEgressBandwidthTier", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInstanceFromTemplateNetworkPerformanceConfig]:
        return typing.cast(typing.Optional[GoogleComputeInstanceFromTemplateNetworkPerformanceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInstanceFromTemplateNetworkPerformanceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateNetworkPerformanceConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateReservationAffinity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "specific_reservation": "specificReservation"},
)
class GoogleComputeInstanceFromTemplateReservationAffinity:
    def __init__(
        self,
        *,
        type: builtins.str,
        specific_reservation: typing.Optional[typing.Union["GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservation", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: The type of reservation from which this instance can consume resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#type GoogleComputeInstanceFromTemplate#type}
        :param specific_reservation: specific_reservation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#specific_reservation GoogleComputeInstanceFromTemplate#specific_reservation}
        '''
        if isinstance(specific_reservation, dict):
            specific_reservation = GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservation(**specific_reservation)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateReservationAffinity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument specific_reservation", value=specific_reservation, expected_type=type_hints["specific_reservation"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if specific_reservation is not None:
            self._values["specific_reservation"] = specific_reservation

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of reservation from which this instance can consume resources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#type GoogleComputeInstanceFromTemplate#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def specific_reservation(
        self,
    ) -> typing.Optional["GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservation"]:
        '''specific_reservation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#specific_reservation GoogleComputeInstanceFromTemplate#specific_reservation}
        '''
        result = self._values.get("specific_reservation")
        return typing.cast(typing.Optional["GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateReservationAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceFromTemplateReservationAffinityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateReservationAffinityOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateReservationAffinityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSpecificReservation")
    def put_specific_reservation(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Corresponds to the label key of a reservation resource. To target a SPECIFIC_RESERVATION by name, specify compute.googleapis.com/reservation-name as the key and specify the name of your reservation as the only value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#key GoogleComputeInstanceFromTemplate#key}
        :param values: Corresponds to the label values of a reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#values GoogleComputeInstanceFromTemplate#values}
        '''
        value = GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservation(
            key=key, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putSpecificReservation", [value]))

    @jsii.member(jsii_name="resetSpecificReservation")
    def reset_specific_reservation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpecificReservation", []))

    @builtins.property
    @jsii.member(jsii_name="specificReservation")
    def specific_reservation(
        self,
    ) -> "GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservationOutputReference":
        return typing.cast("GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservationOutputReference", jsii.get(self, "specificReservation"))

    @builtins.property
    @jsii.member(jsii_name="specificReservationInput")
    def specific_reservation_input(
        self,
    ) -> typing.Optional["GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservation"]:
        return typing.cast(typing.Optional["GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservation"], jsii.get(self, "specificReservationInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateReservationAffinityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInstanceFromTemplateReservationAffinity]:
        return typing.cast(typing.Optional[GoogleComputeInstanceFromTemplateReservationAffinity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInstanceFromTemplateReservationAffinity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateReservationAffinityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservation",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservation:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Corresponds to the label key of a reservation resource. To target a SPECIFIC_RESERVATION by name, specify compute.googleapis.com/reservation-name as the key and specify the name of your reservation as the only value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#key GoogleComputeInstanceFromTemplate#key}
        :param values: Corresponds to the label values of a reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#values GoogleComputeInstanceFromTemplate#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservation.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Corresponds to the label key of a reservation resource.

        To target a SPECIFIC_RESERVATION by name, specify compute.googleapis.com/reservation-name as the key and specify the name of your reservation as the only value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#key GoogleComputeInstanceFromTemplate#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Corresponds to the label values of a reservation resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#values GoogleComputeInstanceFromTemplate#values}
        '''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservationOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservationOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservation]:
        return typing.cast(typing.Optional[GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateScheduling",
    jsii_struct_bases=[],
    name_mapping={
        "automatic_restart": "automaticRestart",
        "instance_termination_action": "instanceTerminationAction",
        "min_node_cpus": "minNodeCpus",
        "node_affinities": "nodeAffinities",
        "on_host_maintenance": "onHostMaintenance",
        "preemptible": "preemptible",
        "provisioning_model": "provisioningModel",
    },
)
class GoogleComputeInstanceFromTemplateScheduling:
    def __init__(
        self,
        *,
        automatic_restart: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        instance_termination_action: typing.Optional[builtins.str] = None,
        min_node_cpus: typing.Optional[jsii.Number] = None,
        node_affinities: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceFromTemplateSchedulingNodeAffinities", typing.Dict[str, typing.Any]]]]] = None,
        on_host_maintenance: typing.Optional[builtins.str] = None,
        preemptible: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        provisioning_model: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param automatic_restart: Specifies if the instance should be restarted if it was terminated by Compute Engine (not a user). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#automatic_restart GoogleComputeInstanceFromTemplate#automatic_restart}
        :param instance_termination_action: Specifies the action GCE should take when SPOT VM is preempted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#instance_termination_action GoogleComputeInstanceFromTemplate#instance_termination_action}
        :param min_node_cpus: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#min_node_cpus GoogleComputeInstanceFromTemplate#min_node_cpus}.
        :param node_affinities: node_affinities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#node_affinities GoogleComputeInstanceFromTemplate#node_affinities}
        :param on_host_maintenance: Describes maintenance behavior for the instance. One of MIGRATE or TERMINATE,. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#on_host_maintenance GoogleComputeInstanceFromTemplate#on_host_maintenance}
        :param preemptible: Whether the instance is preemptible. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#preemptible GoogleComputeInstanceFromTemplate#preemptible}
        :param provisioning_model: Whether the instance is spot. If this is set as SPOT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#provisioning_model GoogleComputeInstanceFromTemplate#provisioning_model}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateScheduling.__init__)
            check_type(argname="argument automatic_restart", value=automatic_restart, expected_type=type_hints["automatic_restart"])
            check_type(argname="argument instance_termination_action", value=instance_termination_action, expected_type=type_hints["instance_termination_action"])
            check_type(argname="argument min_node_cpus", value=min_node_cpus, expected_type=type_hints["min_node_cpus"])
            check_type(argname="argument node_affinities", value=node_affinities, expected_type=type_hints["node_affinities"])
            check_type(argname="argument on_host_maintenance", value=on_host_maintenance, expected_type=type_hints["on_host_maintenance"])
            check_type(argname="argument preemptible", value=preemptible, expected_type=type_hints["preemptible"])
            check_type(argname="argument provisioning_model", value=provisioning_model, expected_type=type_hints["provisioning_model"])
        self._values: typing.Dict[str, typing.Any] = {}
        if automatic_restart is not None:
            self._values["automatic_restart"] = automatic_restart
        if instance_termination_action is not None:
            self._values["instance_termination_action"] = instance_termination_action
        if min_node_cpus is not None:
            self._values["min_node_cpus"] = min_node_cpus
        if node_affinities is not None:
            self._values["node_affinities"] = node_affinities
        if on_host_maintenance is not None:
            self._values["on_host_maintenance"] = on_host_maintenance
        if preemptible is not None:
            self._values["preemptible"] = preemptible
        if provisioning_model is not None:
            self._values["provisioning_model"] = provisioning_model

    @builtins.property
    def automatic_restart(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the instance should be restarted if it was terminated by Compute Engine (not a user).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#automatic_restart GoogleComputeInstanceFromTemplate#automatic_restart}
        '''
        result = self._values.get("automatic_restart")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def instance_termination_action(self) -> typing.Optional[builtins.str]:
        '''Specifies the action GCE should take when SPOT VM is preempted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#instance_termination_action GoogleComputeInstanceFromTemplate#instance_termination_action}
        '''
        result = self._values.get("instance_termination_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_node_cpus(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#min_node_cpus GoogleComputeInstanceFromTemplate#min_node_cpus}.'''
        result = self._values.get("min_node_cpus")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def node_affinities(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateSchedulingNodeAffinities"]]]:
        '''node_affinities block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#node_affinities GoogleComputeInstanceFromTemplate#node_affinities}
        '''
        result = self._values.get("node_affinities")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceFromTemplateSchedulingNodeAffinities"]]], result)

    @builtins.property
    def on_host_maintenance(self) -> typing.Optional[builtins.str]:
        '''Describes maintenance behavior for the instance. One of MIGRATE or TERMINATE,.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#on_host_maintenance GoogleComputeInstanceFromTemplate#on_host_maintenance}
        '''
        result = self._values.get("on_host_maintenance")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preemptible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the instance is preemptible.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#preemptible GoogleComputeInstanceFromTemplate#preemptible}
        '''
        result = self._values.get("preemptible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def provisioning_model(self) -> typing.Optional[builtins.str]:
        '''Whether the instance is spot. If this is set as SPOT.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#provisioning_model GoogleComputeInstanceFromTemplate#provisioning_model}
        '''
        result = self._values.get("provisioning_model")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateScheduling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateSchedulingNodeAffinities",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class GoogleComputeInstanceFromTemplateSchedulingNodeAffinities:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#key GoogleComputeInstanceFromTemplate#key}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#operator GoogleComputeInstanceFromTemplate#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#values GoogleComputeInstanceFromTemplate#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateSchedulingNodeAffinities.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "operator": operator,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#key GoogleComputeInstanceFromTemplate#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#operator GoogleComputeInstanceFromTemplate#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#values GoogleComputeInstanceFromTemplate#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateSchedulingNodeAffinities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesList",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateSchedulingNodeAffinities]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateSchedulingNodeAffinities]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateSchedulingNodeAffinities]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateSchedulingNodeAffinities, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateSchedulingNodeAffinities, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateSchedulingNodeAffinities, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceFromTemplateSchedulingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateSchedulingOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateSchedulingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNodeAffinities")
    def put_node_affinities(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeInstanceFromTemplateSchedulingNodeAffinities, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateSchedulingOutputReference.put_node_affinities)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNodeAffinities", [value]))

    @jsii.member(jsii_name="resetAutomaticRestart")
    def reset_automatic_restart(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticRestart", []))

    @jsii.member(jsii_name="resetInstanceTerminationAction")
    def reset_instance_termination_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceTerminationAction", []))

    @jsii.member(jsii_name="resetMinNodeCpus")
    def reset_min_node_cpus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinNodeCpus", []))

    @jsii.member(jsii_name="resetNodeAffinities")
    def reset_node_affinities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeAffinities", []))

    @jsii.member(jsii_name="resetOnHostMaintenance")
    def reset_on_host_maintenance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnHostMaintenance", []))

    @jsii.member(jsii_name="resetPreemptible")
    def reset_preemptible(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreemptible", []))

    @jsii.member(jsii_name="resetProvisioningModel")
    def reset_provisioning_model(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvisioningModel", []))

    @builtins.property
    @jsii.member(jsii_name="nodeAffinities")
    def node_affinities(
        self,
    ) -> GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesList:
        return typing.cast(GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesList, jsii.get(self, "nodeAffinities"))

    @builtins.property
    @jsii.member(jsii_name="automaticRestartInput")
    def automatic_restart_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "automaticRestartInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTerminationActionInput")
    def instance_termination_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTerminationActionInput"))

    @builtins.property
    @jsii.member(jsii_name="minNodeCpusInput")
    def min_node_cpus_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minNodeCpusInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeAffinitiesInput")
    def node_affinities_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateSchedulingNodeAffinities]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateSchedulingNodeAffinities]]], jsii.get(self, "nodeAffinitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="onHostMaintenanceInput")
    def on_host_maintenance_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "onHostMaintenanceInput"))

    @builtins.property
    @jsii.member(jsii_name="preemptibleInput")
    def preemptible_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preemptibleInput"))

    @builtins.property
    @jsii.member(jsii_name="provisioningModelInput")
    def provisioning_model_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "provisioningModelInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticRestart")
    def automatic_restart(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "automaticRestart"))

    @automatic_restart.setter
    def automatic_restart(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateSchedulingOutputReference, "automatic_restart").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticRestart", value)

    @builtins.property
    @jsii.member(jsii_name="instanceTerminationAction")
    def instance_termination_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceTerminationAction"))

    @instance_termination_action.setter
    def instance_termination_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateSchedulingOutputReference, "instance_termination_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceTerminationAction", value)

    @builtins.property
    @jsii.member(jsii_name="minNodeCpus")
    def min_node_cpus(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minNodeCpus"))

    @min_node_cpus.setter
    def min_node_cpus(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateSchedulingOutputReference, "min_node_cpus").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minNodeCpus", value)

    @builtins.property
    @jsii.member(jsii_name="onHostMaintenance")
    def on_host_maintenance(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onHostMaintenance"))

    @on_host_maintenance.setter
    def on_host_maintenance(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateSchedulingOutputReference, "on_host_maintenance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onHostMaintenance", value)

    @builtins.property
    @jsii.member(jsii_name="preemptible")
    def preemptible(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preemptible"))

    @preemptible.setter
    def preemptible(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateSchedulingOutputReference, "preemptible").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preemptible", value)

    @builtins.property
    @jsii.member(jsii_name="provisioningModel")
    def provisioning_model(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "provisioningModel"))

    @provisioning_model.setter
    def provisioning_model(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateSchedulingOutputReference, "provisioning_model").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisioningModel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInstanceFromTemplateScheduling]:
        return typing.cast(typing.Optional[GoogleComputeInstanceFromTemplateScheduling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInstanceFromTemplateScheduling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateSchedulingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateScratchDisk",
    jsii_struct_bases=[],
    name_mapping={"interface": "interface"},
)
class GoogleComputeInstanceFromTemplateScratchDisk:
    def __init__(self, *, interface: typing.Optional[builtins.str] = None) -> None:
        '''
        :param interface: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#interface GoogleComputeInstanceFromTemplate#interface}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateScratchDisk.__init__)
            check_type(argname="argument interface", value=interface, expected_type=type_hints["interface"])
        self._values: typing.Dict[str, typing.Any] = {}
        if interface is not None:
            self._values["interface"] = interface

    @builtins.property
    def interface(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#interface GoogleComputeInstanceFromTemplate#interface}.'''
        result = self._values.get("interface")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateScratchDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceFromTemplateScratchDiskList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateScratchDiskList",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateScratchDiskList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeInstanceFromTemplateScratchDiskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateScratchDiskList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeInstanceFromTemplateScratchDiskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateScratchDiskList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateScratchDiskList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateScratchDiskList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateScratchDisk]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateScratchDisk]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateScratchDisk]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateScratchDiskList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceFromTemplateScratchDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateScratchDiskOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateScratchDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetInterface")
    def reset_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterface", []))

    @builtins.property
    @jsii.member(jsii_name="interfaceInput")
    def interface_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="interface")
    def interface(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interface"))

    @interface.setter
    def interface(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateScratchDiskOutputReference, "interface").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interface", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateScratchDisk, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateScratchDisk, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateScratchDisk, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateScratchDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateServiceAccount",
    jsii_struct_bases=[],
    name_mapping={"email": "email", "scopes": "scopes"},
)
class GoogleComputeInstanceFromTemplateServiceAccount:
    def __init__(
        self,
        *,
        email: typing.Optional[builtins.str] = None,
        scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#email GoogleComputeInstanceFromTemplate#email}.
        :param scopes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#scopes GoogleComputeInstanceFromTemplate#scopes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateServiceAccount.__init__)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument scopes", value=scopes, expected_type=type_hints["scopes"])
        self._values: typing.Dict[str, typing.Any] = {}
        if email is not None:
            self._values["email"] = email
        if scopes is not None:
            self._values["scopes"] = scopes

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#email GoogleComputeInstanceFromTemplate#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#scopes GoogleComputeInstanceFromTemplate#scopes}.'''
        result = self._values.get("scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateServiceAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceFromTemplateServiceAccountList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateServiceAccountList",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateServiceAccountList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeInstanceFromTemplateServiceAccountOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateServiceAccountList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeInstanceFromTemplateServiceAccountOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateServiceAccountList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateServiceAccountList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateServiceAccountList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateServiceAccount]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateServiceAccount]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceFromTemplateServiceAccount]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateServiceAccountList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceFromTemplateServiceAccountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateServiceAccountOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateServiceAccountOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetScopes")
    def reset_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScopes", []))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="scopesInput")
    def scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "scopesInput"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateServiceAccountOutputReference, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="scopes")
    def scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "scopes"))

    @scopes.setter
    def scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateServiceAccountOutputReference, "scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateServiceAccount, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateServiceAccount, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateServiceAccount, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateServiceAccountOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateShieldedInstanceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "enable_integrity_monitoring": "enableIntegrityMonitoring",
        "enable_secure_boot": "enableSecureBoot",
        "enable_vtpm": "enableVtpm",
    },
)
class GoogleComputeInstanceFromTemplateShieldedInstanceConfig:
    def __init__(
        self,
        *,
        enable_integrity_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_secure_boot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_vtpm: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_integrity_monitoring: Whether integrity monitoring is enabled for the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#enable_integrity_monitoring GoogleComputeInstanceFromTemplate#enable_integrity_monitoring}
        :param enable_secure_boot: Whether secure boot is enabled for the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#enable_secure_boot GoogleComputeInstanceFromTemplate#enable_secure_boot}
        :param enable_vtpm: Whether the instance uses vTPM. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#enable_vtpm GoogleComputeInstanceFromTemplate#enable_vtpm}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateShieldedInstanceConfig.__init__)
            check_type(argname="argument enable_integrity_monitoring", value=enable_integrity_monitoring, expected_type=type_hints["enable_integrity_monitoring"])
            check_type(argname="argument enable_secure_boot", value=enable_secure_boot, expected_type=type_hints["enable_secure_boot"])
            check_type(argname="argument enable_vtpm", value=enable_vtpm, expected_type=type_hints["enable_vtpm"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enable_integrity_monitoring is not None:
            self._values["enable_integrity_monitoring"] = enable_integrity_monitoring
        if enable_secure_boot is not None:
            self._values["enable_secure_boot"] = enable_secure_boot
        if enable_vtpm is not None:
            self._values["enable_vtpm"] = enable_vtpm

    @builtins.property
    def enable_integrity_monitoring(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether integrity monitoring is enabled for the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#enable_integrity_monitoring GoogleComputeInstanceFromTemplate#enable_integrity_monitoring}
        '''
        result = self._values.get("enable_integrity_monitoring")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_secure_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether secure boot is enabled for the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#enable_secure_boot GoogleComputeInstanceFromTemplate#enable_secure_boot}
        '''
        result = self._values.get("enable_secure_boot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_vtpm(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the instance uses vTPM.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#enable_vtpm GoogleComputeInstanceFromTemplate#enable_vtpm}
        '''
        result = self._values.get("enable_vtpm")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateShieldedInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceFromTemplateShieldedInstanceConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateShieldedInstanceConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateShieldedInstanceConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnableIntegrityMonitoring")
    def reset_enable_integrity_monitoring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableIntegrityMonitoring", []))

    @jsii.member(jsii_name="resetEnableSecureBoot")
    def reset_enable_secure_boot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableSecureBoot", []))

    @jsii.member(jsii_name="resetEnableVtpm")
    def reset_enable_vtpm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableVtpm", []))

    @builtins.property
    @jsii.member(jsii_name="enableIntegrityMonitoringInput")
    def enable_integrity_monitoring_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableIntegrityMonitoringInput"))

    @builtins.property
    @jsii.member(jsii_name="enableSecureBootInput")
    def enable_secure_boot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableSecureBootInput"))

    @builtins.property
    @jsii.member(jsii_name="enableVtpmInput")
    def enable_vtpm_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableVtpmInput"))

    @builtins.property
    @jsii.member(jsii_name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableIntegrityMonitoring"))

    @enable_integrity_monitoring.setter
    def enable_integrity_monitoring(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateShieldedInstanceConfigOutputReference, "enable_integrity_monitoring").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableIntegrityMonitoring", value)

    @builtins.property
    @jsii.member(jsii_name="enableSecureBoot")
    def enable_secure_boot(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableSecureBoot"))

    @enable_secure_boot.setter
    def enable_secure_boot(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateShieldedInstanceConfigOutputReference, "enable_secure_boot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSecureBoot", value)

    @builtins.property
    @jsii.member(jsii_name="enableVtpm")
    def enable_vtpm(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableVtpm"))

    @enable_vtpm.setter
    def enable_vtpm(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateShieldedInstanceConfigOutputReference, "enable_vtpm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableVtpm", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInstanceFromTemplateShieldedInstanceConfig]:
        return typing.cast(typing.Optional[GoogleComputeInstanceFromTemplateShieldedInstanceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInstanceFromTemplateShieldedInstanceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateShieldedInstanceConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeInstanceFromTemplateTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#create GoogleComputeInstanceFromTemplate#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#delete GoogleComputeInstanceFromTemplate#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#update GoogleComputeInstanceFromTemplate#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#create GoogleComputeInstanceFromTemplate#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#delete GoogleComputeInstanceFromTemplate#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_from_template#update GoogleComputeInstanceFromTemplate#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceFromTemplateTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceFromTemplateTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceFromTemplate.GoogleComputeInstanceFromTemplateTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceFromTemplateTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInstanceFromTemplateTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceFromTemplateTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeInstanceFromTemplate",
    "GoogleComputeInstanceFromTemplateAdvancedMachineFeatures",
    "GoogleComputeInstanceFromTemplateAdvancedMachineFeaturesOutputReference",
    "GoogleComputeInstanceFromTemplateAttachedDisk",
    "GoogleComputeInstanceFromTemplateAttachedDiskList",
    "GoogleComputeInstanceFromTemplateAttachedDiskOutputReference",
    "GoogleComputeInstanceFromTemplateBootDisk",
    "GoogleComputeInstanceFromTemplateBootDiskInitializeParams",
    "GoogleComputeInstanceFromTemplateBootDiskInitializeParamsOutputReference",
    "GoogleComputeInstanceFromTemplateBootDiskOutputReference",
    "GoogleComputeInstanceFromTemplateConfidentialInstanceConfig",
    "GoogleComputeInstanceFromTemplateConfidentialInstanceConfigOutputReference",
    "GoogleComputeInstanceFromTemplateConfig",
    "GoogleComputeInstanceFromTemplateGuestAccelerator",
    "GoogleComputeInstanceFromTemplateGuestAcceleratorList",
    "GoogleComputeInstanceFromTemplateGuestAcceleratorOutputReference",
    "GoogleComputeInstanceFromTemplateNetworkInterface",
    "GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfig",
    "GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigList",
    "GoogleComputeInstanceFromTemplateNetworkInterfaceAccessConfigOutputReference",
    "GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRange",
    "GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeList",
    "GoogleComputeInstanceFromTemplateNetworkInterfaceAliasIpRangeOutputReference",
    "GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfig",
    "GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigList",
    "GoogleComputeInstanceFromTemplateNetworkInterfaceIpv6AccessConfigOutputReference",
    "GoogleComputeInstanceFromTemplateNetworkInterfaceList",
    "GoogleComputeInstanceFromTemplateNetworkInterfaceOutputReference",
    "GoogleComputeInstanceFromTemplateNetworkPerformanceConfig",
    "GoogleComputeInstanceFromTemplateNetworkPerformanceConfigOutputReference",
    "GoogleComputeInstanceFromTemplateReservationAffinity",
    "GoogleComputeInstanceFromTemplateReservationAffinityOutputReference",
    "GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservation",
    "GoogleComputeInstanceFromTemplateReservationAffinitySpecificReservationOutputReference",
    "GoogleComputeInstanceFromTemplateScheduling",
    "GoogleComputeInstanceFromTemplateSchedulingNodeAffinities",
    "GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesList",
    "GoogleComputeInstanceFromTemplateSchedulingNodeAffinitiesOutputReference",
    "GoogleComputeInstanceFromTemplateSchedulingOutputReference",
    "GoogleComputeInstanceFromTemplateScratchDisk",
    "GoogleComputeInstanceFromTemplateScratchDiskList",
    "GoogleComputeInstanceFromTemplateScratchDiskOutputReference",
    "GoogleComputeInstanceFromTemplateServiceAccount",
    "GoogleComputeInstanceFromTemplateServiceAccountList",
    "GoogleComputeInstanceFromTemplateServiceAccountOutputReference",
    "GoogleComputeInstanceFromTemplateShieldedInstanceConfig",
    "GoogleComputeInstanceFromTemplateShieldedInstanceConfigOutputReference",
    "GoogleComputeInstanceFromTemplateTimeouts",
    "GoogleComputeInstanceFromTemplateTimeoutsOutputReference",
]

publication.publish()
