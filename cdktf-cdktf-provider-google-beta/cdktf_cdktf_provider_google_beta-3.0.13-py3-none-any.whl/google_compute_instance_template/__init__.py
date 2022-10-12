'''
# `google_compute_instance_template`

Refer to the Terraform Registory for docs: [`google_compute_instance_template`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template).
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


class GoogleComputeInstanceTemplate(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplate",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template google_compute_instance_template}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        disk: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceTemplateDisk", typing.Dict[str, typing.Any]]]],
        machine_type: builtins.str,
        advanced_machine_features: typing.Optional[typing.Union["GoogleComputeInstanceTemplateAdvancedMachineFeatures", typing.Dict[str, typing.Any]]] = None,
        can_ip_forward: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        confidential_instance_config: typing.Optional[typing.Union["GoogleComputeInstanceTemplateConfidentialInstanceConfig", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_display: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        guest_accelerator: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceTemplateGuestAccelerator", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        instance_description: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        metadata_startup_script: typing.Optional[builtins.str] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        network_interface: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceTemplateNetworkInterface", typing.Dict[str, typing.Any]]]]] = None,
        network_performance_config: typing.Optional[typing.Union["GoogleComputeInstanceTemplateNetworkPerformanceConfig", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        reservation_affinity: typing.Optional[typing.Union["GoogleComputeInstanceTemplateReservationAffinity", typing.Dict[str, typing.Any]]] = None,
        scheduling: typing.Optional[typing.Union["GoogleComputeInstanceTemplateScheduling", typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[typing.Union["GoogleComputeInstanceTemplateServiceAccount", typing.Dict[str, typing.Any]]] = None,
        shielded_instance_config: typing.Optional[typing.Union["GoogleComputeInstanceTemplateShieldedInstanceConfig", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeInstanceTemplateTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template google_compute_instance_template} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param disk: disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#disk GoogleComputeInstanceTemplate#disk}
        :param machine_type: The machine type to create. To create a machine with a custom type (such as extended memory), format the value like custom-VCPUS-MEM_IN_MB like custom-6-20480 for 6 vCPU and 20GB of RAM. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#machine_type GoogleComputeInstanceTemplate#machine_type}
        :param advanced_machine_features: advanced_machine_features block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#advanced_machine_features GoogleComputeInstanceTemplate#advanced_machine_features}
        :param can_ip_forward: Whether to allow sending and receiving of packets with non-matching source or destination IPs. This defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#can_ip_forward GoogleComputeInstanceTemplate#can_ip_forward}
        :param confidential_instance_config: confidential_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#confidential_instance_config GoogleComputeInstanceTemplate#confidential_instance_config}
        :param description: A brief description of this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#description GoogleComputeInstanceTemplate#description}
        :param enable_display: Enable Virtual Displays on this instance. Note: allow_stopping_for_update must be set to true in order to update this field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#enable_display GoogleComputeInstanceTemplate#enable_display}
        :param guest_accelerator: guest_accelerator block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#guest_accelerator GoogleComputeInstanceTemplate#guest_accelerator}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#id GoogleComputeInstanceTemplate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_description: A description of the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#instance_description GoogleComputeInstanceTemplate#instance_description}
        :param labels: A set of key/value label pairs to assign to instances created from this template,. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#labels GoogleComputeInstanceTemplate#labels}
        :param metadata: Metadata key/value pairs to make available from within instances created from this template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#metadata GoogleComputeInstanceTemplate#metadata}
        :param metadata_startup_script: An alternative to using the startup-script metadata key, mostly to match the compute_instance resource. This replaces the startup-script metadata key on the created instance and thus the two mechanisms are not allowed to be used simultaneously. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#metadata_startup_script GoogleComputeInstanceTemplate#metadata_startup_script}
        :param min_cpu_platform: Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as Intel Haswell or Intel Skylake. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#min_cpu_platform GoogleComputeInstanceTemplate#min_cpu_platform}
        :param name: The name of the instance template. If you leave this blank, Terraform will auto-generate a unique name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#name GoogleComputeInstanceTemplate#name}
        :param name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#name_prefix GoogleComputeInstanceTemplate#name_prefix}
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#network_interface GoogleComputeInstanceTemplate#network_interface}
        :param network_performance_config: network_performance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#network_performance_config GoogleComputeInstanceTemplate#network_performance_config}
        :param project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#project GoogleComputeInstanceTemplate#project}
        :param region: An instance template is a global resource that is not bound to a zone or a region. However, you can still specify some regional resources in an instance template, which restricts the template to the region where that resource resides. For example, a custom subnetwork resource is tied to a specific region. Defaults to the region of the Provider if no value is given. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#region GoogleComputeInstanceTemplate#region}
        :param reservation_affinity: reservation_affinity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#reservation_affinity GoogleComputeInstanceTemplate#reservation_affinity}
        :param scheduling: scheduling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#scheduling GoogleComputeInstanceTemplate#scheduling}
        :param service_account: service_account block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#service_account GoogleComputeInstanceTemplate#service_account}
        :param shielded_instance_config: shielded_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#shielded_instance_config GoogleComputeInstanceTemplate#shielded_instance_config}
        :param tags: Tags to attach to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#tags GoogleComputeInstanceTemplate#tags}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#timeouts GoogleComputeInstanceTemplate#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplate.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeInstanceTemplateConfig(
            disk=disk,
            machine_type=machine_type,
            advanced_machine_features=advanced_machine_features,
            can_ip_forward=can_ip_forward,
            confidential_instance_config=confidential_instance_config,
            description=description,
            enable_display=enable_display,
            guest_accelerator=guest_accelerator,
            id=id,
            instance_description=instance_description,
            labels=labels,
            metadata=metadata,
            metadata_startup_script=metadata_startup_script,
            min_cpu_platform=min_cpu_platform,
            name=name,
            name_prefix=name_prefix,
            network_interface=network_interface,
            network_performance_config=network_performance_config,
            project=project,
            region=region,
            reservation_affinity=reservation_affinity,
            scheduling=scheduling,
            service_account=service_account,
            shielded_instance_config=shielded_instance_config,
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

    @jsii.member(jsii_name="putAdvancedMachineFeatures")
    def put_advanced_machine_features(
        self,
        *,
        enable_nested_virtualization: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        threads_per_core: typing.Optional[jsii.Number] = None,
        visible_core_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enable_nested_virtualization: Whether to enable nested virtualization or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#enable_nested_virtualization GoogleComputeInstanceTemplate#enable_nested_virtualization}
        :param threads_per_core: The number of threads per physical core. To disable simultaneous multithreading (SMT) set this to 1. If unset, the maximum number of threads supported per core by the underlying processor is assumed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#threads_per_core GoogleComputeInstanceTemplate#threads_per_core}
        :param visible_core_count: The number of physical cores to expose to an instance. Multiply by the number of threads per core to compute the total number of virtual CPUs to expose to the instance. If unset, the number of cores is inferred from the instance's nominal CPU count and the underlying platform's SMT width. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#visible_core_count GoogleComputeInstanceTemplate#visible_core_count}
        '''
        value = GoogleComputeInstanceTemplateAdvancedMachineFeatures(
            enable_nested_virtualization=enable_nested_virtualization,
            threads_per_core=threads_per_core,
            visible_core_count=visible_core_count,
        )

        return typing.cast(None, jsii.invoke(self, "putAdvancedMachineFeatures", [value]))

    @jsii.member(jsii_name="putConfidentialInstanceConfig")
    def put_confidential_instance_config(
        self,
        *,
        enable_confidential_compute: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable_confidential_compute: Defines whether the instance should have confidential compute enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#enable_confidential_compute GoogleComputeInstanceTemplate#enable_confidential_compute}
        '''
        value = GoogleComputeInstanceTemplateConfidentialInstanceConfig(
            enable_confidential_compute=enable_confidential_compute
        )

        return typing.cast(None, jsii.invoke(self, "putConfidentialInstanceConfig", [value]))

    @jsii.member(jsii_name="putDisk")
    def put_disk(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceTemplateDisk", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplate.put_disk)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDisk", [value]))

    @jsii.member(jsii_name="putGuestAccelerator")
    def put_guest_accelerator(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceTemplateGuestAccelerator", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplate.put_guest_accelerator)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGuestAccelerator", [value]))

    @jsii.member(jsii_name="putNetworkInterface")
    def put_network_interface(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceTemplateNetworkInterface", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplate.put_network_interface)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkInterface", [value]))

    @jsii.member(jsii_name="putNetworkPerformanceConfig")
    def put_network_performance_config(
        self,
        *,
        total_egress_bandwidth_tier: builtins.str,
    ) -> None:
        '''
        :param total_egress_bandwidth_tier: The egress bandwidth tier to enable. Possible values:TIER_1, DEFAULT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#total_egress_bandwidth_tier GoogleComputeInstanceTemplate#total_egress_bandwidth_tier}
        '''
        value = GoogleComputeInstanceTemplateNetworkPerformanceConfig(
            total_egress_bandwidth_tier=total_egress_bandwidth_tier
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkPerformanceConfig", [value]))

    @jsii.member(jsii_name="putReservationAffinity")
    def put_reservation_affinity(
        self,
        *,
        type: builtins.str,
        specific_reservation: typing.Optional[typing.Union["GoogleComputeInstanceTemplateReservationAffinitySpecificReservation", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: The type of reservation from which this instance can consume resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#type GoogleComputeInstanceTemplate#type}
        :param specific_reservation: specific_reservation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#specific_reservation GoogleComputeInstanceTemplate#specific_reservation}
        '''
        value = GoogleComputeInstanceTemplateReservationAffinity(
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
        node_affinities: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceTemplateSchedulingNodeAffinities", typing.Dict[str, typing.Any]]]]] = None,
        on_host_maintenance: typing.Optional[builtins.str] = None,
        preemptible: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        provisioning_model: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param automatic_restart: Specifies whether the instance should be automatically restarted if it is terminated by Compute Engine (not terminated by a user). This defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#automatic_restart GoogleComputeInstanceTemplate#automatic_restart}
        :param instance_termination_action: Specifies the action GCE should take when SPOT VM is preempted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#instance_termination_action GoogleComputeInstanceTemplate#instance_termination_action}
        :param min_node_cpus: Minimum number of cpus for the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#min_node_cpus GoogleComputeInstanceTemplate#min_node_cpus}
        :param node_affinities: node_affinities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#node_affinities GoogleComputeInstanceTemplate#node_affinities}
        :param on_host_maintenance: Defines the maintenance behavior for this instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#on_host_maintenance GoogleComputeInstanceTemplate#on_host_maintenance}
        :param preemptible: Allows instance to be preempted. This defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#preemptible GoogleComputeInstanceTemplate#preemptible}
        :param provisioning_model: Whether the instance is spot. If this is set as SPOT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#provisioning_model GoogleComputeInstanceTemplate#provisioning_model}
        '''
        value = GoogleComputeInstanceTemplateScheduling(
            automatic_restart=automatic_restart,
            instance_termination_action=instance_termination_action,
            min_node_cpus=min_node_cpus,
            node_affinities=node_affinities,
            on_host_maintenance=on_host_maintenance,
            preemptible=preemptible,
            provisioning_model=provisioning_model,
        )

        return typing.cast(None, jsii.invoke(self, "putScheduling", [value]))

    @jsii.member(jsii_name="putServiceAccount")
    def put_service_account(
        self,
        *,
        scopes: typing.Sequence[builtins.str],
        email: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scopes: A list of service scopes. Both OAuth2 URLs and gcloud short names are supported. To allow full access to all Cloud APIs, use the cloud-platform scope. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#scopes GoogleComputeInstanceTemplate#scopes}
        :param email: The service account e-mail address. If not given, the default Google Compute Engine service account is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#email GoogleComputeInstanceTemplate#email}
        '''
        value = GoogleComputeInstanceTemplateServiceAccount(scopes=scopes, email=email)

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
        :param enable_integrity_monitoring: Compare the most recent boot measurements to the integrity policy baseline and return a pair of pass/fail results depending on whether they match or not. Defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#enable_integrity_monitoring GoogleComputeInstanceTemplate#enable_integrity_monitoring}
        :param enable_secure_boot: Verify the digital signature of all boot components, and halt the boot process if signature verification fails. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#enable_secure_boot GoogleComputeInstanceTemplate#enable_secure_boot}
        :param enable_vtpm: Use a virtualized trusted platform module, which is a specialized computer chip you can use to encrypt objects like keys and certificates. Defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#enable_vtpm GoogleComputeInstanceTemplate#enable_vtpm}
        '''
        value = GoogleComputeInstanceTemplateShieldedInstanceConfig(
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
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#create GoogleComputeInstanceTemplate#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#delete GoogleComputeInstanceTemplate#delete}.
        '''
        value = GoogleComputeInstanceTemplateTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAdvancedMachineFeatures")
    def reset_advanced_machine_features(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvancedMachineFeatures", []))

    @jsii.member(jsii_name="resetCanIpForward")
    def reset_can_ip_forward(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCanIpForward", []))

    @jsii.member(jsii_name="resetConfidentialInstanceConfig")
    def reset_confidential_instance_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfidentialInstanceConfig", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnableDisplay")
    def reset_enable_display(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableDisplay", []))

    @jsii.member(jsii_name="resetGuestAccelerator")
    def reset_guest_accelerator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGuestAccelerator", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInstanceDescription")
    def reset_instance_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceDescription", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetMetadataStartupScript")
    def reset_metadata_startup_script(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadataStartupScript", []))

    @jsii.member(jsii_name="resetMinCpuPlatform")
    def reset_min_cpu_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCpuPlatform", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="resetNetworkInterface")
    def reset_network_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkInterface", []))

    @jsii.member(jsii_name="resetNetworkPerformanceConfig")
    def reset_network_performance_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkPerformanceConfig", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetReservationAffinity")
    def reset_reservation_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReservationAffinity", []))

    @jsii.member(jsii_name="resetScheduling")
    def reset_scheduling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduling", []))

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
    ) -> "GoogleComputeInstanceTemplateAdvancedMachineFeaturesOutputReference":
        return typing.cast("GoogleComputeInstanceTemplateAdvancedMachineFeaturesOutputReference", jsii.get(self, "advancedMachineFeatures"))

    @builtins.property
    @jsii.member(jsii_name="confidentialInstanceConfig")
    def confidential_instance_config(
        self,
    ) -> "GoogleComputeInstanceTemplateConfidentialInstanceConfigOutputReference":
        return typing.cast("GoogleComputeInstanceTemplateConfidentialInstanceConfigOutputReference", jsii.get(self, "confidentialInstanceConfig"))

    @builtins.property
    @jsii.member(jsii_name="disk")
    def disk(self) -> "GoogleComputeInstanceTemplateDiskList":
        return typing.cast("GoogleComputeInstanceTemplateDiskList", jsii.get(self, "disk"))

    @builtins.property
    @jsii.member(jsii_name="guestAccelerator")
    def guest_accelerator(self) -> "GoogleComputeInstanceTemplateGuestAcceleratorList":
        return typing.cast("GoogleComputeInstanceTemplateGuestAcceleratorList", jsii.get(self, "guestAccelerator"))

    @builtins.property
    @jsii.member(jsii_name="metadataFingerprint")
    def metadata_fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metadataFingerprint"))

    @builtins.property
    @jsii.member(jsii_name="networkInterface")
    def network_interface(self) -> "GoogleComputeInstanceTemplateNetworkInterfaceList":
        return typing.cast("GoogleComputeInstanceTemplateNetworkInterfaceList", jsii.get(self, "networkInterface"))

    @builtins.property
    @jsii.member(jsii_name="networkPerformanceConfig")
    def network_performance_config(
        self,
    ) -> "GoogleComputeInstanceTemplateNetworkPerformanceConfigOutputReference":
        return typing.cast("GoogleComputeInstanceTemplateNetworkPerformanceConfigOutputReference", jsii.get(self, "networkPerformanceConfig"))

    @builtins.property
    @jsii.member(jsii_name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> "GoogleComputeInstanceTemplateReservationAffinityOutputReference":
        return typing.cast("GoogleComputeInstanceTemplateReservationAffinityOutputReference", jsii.get(self, "reservationAffinity"))

    @builtins.property
    @jsii.member(jsii_name="scheduling")
    def scheduling(self) -> "GoogleComputeInstanceTemplateSchedulingOutputReference":
        return typing.cast("GoogleComputeInstanceTemplateSchedulingOutputReference", jsii.get(self, "scheduling"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(
        self,
    ) -> "GoogleComputeInstanceTemplateServiceAccountOutputReference":
        return typing.cast("GoogleComputeInstanceTemplateServiceAccountOutputReference", jsii.get(self, "serviceAccount"))

    @builtins.property
    @jsii.member(jsii_name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> "GoogleComputeInstanceTemplateShieldedInstanceConfigOutputReference":
        return typing.cast("GoogleComputeInstanceTemplateShieldedInstanceConfigOutputReference", jsii.get(self, "shieldedInstanceConfig"))

    @builtins.property
    @jsii.member(jsii_name="tagsFingerprint")
    def tags_fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagsFingerprint"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeInstanceTemplateTimeoutsOutputReference":
        return typing.cast("GoogleComputeInstanceTemplateTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="advancedMachineFeaturesInput")
    def advanced_machine_features_input(
        self,
    ) -> typing.Optional["GoogleComputeInstanceTemplateAdvancedMachineFeatures"]:
        return typing.cast(typing.Optional["GoogleComputeInstanceTemplateAdvancedMachineFeatures"], jsii.get(self, "advancedMachineFeaturesInput"))

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
    ) -> typing.Optional["GoogleComputeInstanceTemplateConfidentialInstanceConfig"]:
        return typing.cast(typing.Optional["GoogleComputeInstanceTemplateConfidentialInstanceConfig"], jsii.get(self, "confidentialInstanceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="diskInput")
    def disk_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateDisk"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateDisk"]]], jsii.get(self, "diskInput"))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateGuestAccelerator"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateGuestAccelerator"]]], jsii.get(self, "guestAcceleratorInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceDescriptionInput")
    def instance_description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceDescriptionInput"))

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
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceInput")
    def network_interface_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateNetworkInterface"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateNetworkInterface"]]], jsii.get(self, "networkInterfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="networkPerformanceConfigInput")
    def network_performance_config_input(
        self,
    ) -> typing.Optional["GoogleComputeInstanceTemplateNetworkPerformanceConfig"]:
        return typing.cast(typing.Optional["GoogleComputeInstanceTemplateNetworkPerformanceConfig"], jsii.get(self, "networkPerformanceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="reservationAffinityInput")
    def reservation_affinity_input(
        self,
    ) -> typing.Optional["GoogleComputeInstanceTemplateReservationAffinity"]:
        return typing.cast(typing.Optional["GoogleComputeInstanceTemplateReservationAffinity"], jsii.get(self, "reservationAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="schedulingInput")
    def scheduling_input(
        self,
    ) -> typing.Optional["GoogleComputeInstanceTemplateScheduling"]:
        return typing.cast(typing.Optional["GoogleComputeInstanceTemplateScheduling"], jsii.get(self, "schedulingInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountInput")
    def service_account_input(
        self,
    ) -> typing.Optional["GoogleComputeInstanceTemplateServiceAccount"]:
        return typing.cast(typing.Optional["GoogleComputeInstanceTemplateServiceAccount"], jsii.get(self, "serviceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="shieldedInstanceConfigInput")
    def shielded_instance_config_input(
        self,
    ) -> typing.Optional["GoogleComputeInstanceTemplateShieldedInstanceConfig"]:
        return typing.cast(typing.Optional["GoogleComputeInstanceTemplateShieldedInstanceConfig"], jsii.get(self, "shieldedInstanceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeInstanceTemplateTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeInstanceTemplateTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplate, "can_ip_forward").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "canIpForward", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplate, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplate, "enable_display").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDisplay", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplate, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instanceDescription")
    def instance_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceDescription"))

    @instance_description.setter
    def instance_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplate, "instance_description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceDescription", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplate, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="machineType")
    def machine_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineType"))

    @machine_type.setter
    def machine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplate, "machine_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineType", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplate, "metadata").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="metadataStartupScript")
    def metadata_startup_script(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metadataStartupScript"))

    @metadata_startup_script.setter
    def metadata_startup_script(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplate, "metadata_startup_script").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadataStartupScript", value)

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatform")
    def min_cpu_platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minCpuPlatform"))

    @min_cpu_platform.setter
    def min_cpu_platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplate, "min_cpu_platform").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCpuPlatform", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplate, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplate, "name_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplate, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplate, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplate, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateAdvancedMachineFeatures",
    jsii_struct_bases=[],
    name_mapping={
        "enable_nested_virtualization": "enableNestedVirtualization",
        "threads_per_core": "threadsPerCore",
        "visible_core_count": "visibleCoreCount",
    },
)
class GoogleComputeInstanceTemplateAdvancedMachineFeatures:
    def __init__(
        self,
        *,
        enable_nested_virtualization: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        threads_per_core: typing.Optional[jsii.Number] = None,
        visible_core_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enable_nested_virtualization: Whether to enable nested virtualization or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#enable_nested_virtualization GoogleComputeInstanceTemplate#enable_nested_virtualization}
        :param threads_per_core: The number of threads per physical core. To disable simultaneous multithreading (SMT) set this to 1. If unset, the maximum number of threads supported per core by the underlying processor is assumed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#threads_per_core GoogleComputeInstanceTemplate#threads_per_core}
        :param visible_core_count: The number of physical cores to expose to an instance. Multiply by the number of threads per core to compute the total number of virtual CPUs to expose to the instance. If unset, the number of cores is inferred from the instance's nominal CPU count and the underlying platform's SMT width. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#visible_core_count GoogleComputeInstanceTemplate#visible_core_count}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateAdvancedMachineFeatures.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#enable_nested_virtualization GoogleComputeInstanceTemplate#enable_nested_virtualization}
        '''
        result = self._values.get("enable_nested_virtualization")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def threads_per_core(self) -> typing.Optional[jsii.Number]:
        '''The number of threads per physical core.

        To disable simultaneous multithreading (SMT) set this to 1. If unset, the maximum number of threads supported per core by the underlying processor is assumed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#threads_per_core GoogleComputeInstanceTemplate#threads_per_core}
        '''
        result = self._values.get("threads_per_core")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def visible_core_count(self) -> typing.Optional[jsii.Number]:
        '''The number of physical cores to expose to an instance.

        Multiply by the number of threads per core to compute the total number of virtual CPUs to expose to the instance. If unset, the number of cores is inferred from the instance's nominal CPU count and the underlying platform's SMT width.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#visible_core_count GoogleComputeInstanceTemplate#visible_core_count}
        '''
        result = self._values.get("visible_core_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceTemplateAdvancedMachineFeatures(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceTemplateAdvancedMachineFeaturesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateAdvancedMachineFeaturesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateAdvancedMachineFeaturesOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateAdvancedMachineFeaturesOutputReference, "enable_nested_virtualization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableNestedVirtualization", value)

    @builtins.property
    @jsii.member(jsii_name="threadsPerCore")
    def threads_per_core(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threadsPerCore"))

    @threads_per_core.setter
    def threads_per_core(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateAdvancedMachineFeaturesOutputReference, "threads_per_core").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threadsPerCore", value)

    @builtins.property
    @jsii.member(jsii_name="visibleCoreCount")
    def visible_core_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "visibleCoreCount"))

    @visible_core_count.setter
    def visible_core_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateAdvancedMachineFeaturesOutputReference, "visible_core_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibleCoreCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInstanceTemplateAdvancedMachineFeatures]:
        return typing.cast(typing.Optional[GoogleComputeInstanceTemplateAdvancedMachineFeatures], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInstanceTemplateAdvancedMachineFeatures],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateAdvancedMachineFeaturesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateConfidentialInstanceConfig",
    jsii_struct_bases=[],
    name_mapping={"enable_confidential_compute": "enableConfidentialCompute"},
)
class GoogleComputeInstanceTemplateConfidentialInstanceConfig:
    def __init__(
        self,
        *,
        enable_confidential_compute: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable_confidential_compute: Defines whether the instance should have confidential compute enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#enable_confidential_compute GoogleComputeInstanceTemplate#enable_confidential_compute}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateConfidentialInstanceConfig.__init__)
            check_type(argname="argument enable_confidential_compute", value=enable_confidential_compute, expected_type=type_hints["enable_confidential_compute"])
        self._values: typing.Dict[str, typing.Any] = {
            "enable_confidential_compute": enable_confidential_compute,
        }

    @builtins.property
    def enable_confidential_compute(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Defines whether the instance should have confidential compute enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#enable_confidential_compute GoogleComputeInstanceTemplate#enable_confidential_compute}
        '''
        result = self._values.get("enable_confidential_compute")
        assert result is not None, "Required property 'enable_confidential_compute' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceTemplateConfidentialInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceTemplateConfidentialInstanceConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateConfidentialInstanceConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateConfidentialInstanceConfigOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateConfidentialInstanceConfigOutputReference, "enable_confidential_compute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableConfidentialCompute", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInstanceTemplateConfidentialInstanceConfig]:
        return typing.cast(typing.Optional[GoogleComputeInstanceTemplateConfidentialInstanceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInstanceTemplateConfidentialInstanceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateConfidentialInstanceConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "disk": "disk",
        "machine_type": "machineType",
        "advanced_machine_features": "advancedMachineFeatures",
        "can_ip_forward": "canIpForward",
        "confidential_instance_config": "confidentialInstanceConfig",
        "description": "description",
        "enable_display": "enableDisplay",
        "guest_accelerator": "guestAccelerator",
        "id": "id",
        "instance_description": "instanceDescription",
        "labels": "labels",
        "metadata": "metadata",
        "metadata_startup_script": "metadataStartupScript",
        "min_cpu_platform": "minCpuPlatform",
        "name": "name",
        "name_prefix": "namePrefix",
        "network_interface": "networkInterface",
        "network_performance_config": "networkPerformanceConfig",
        "project": "project",
        "region": "region",
        "reservation_affinity": "reservationAffinity",
        "scheduling": "scheduling",
        "service_account": "serviceAccount",
        "shielded_instance_config": "shieldedInstanceConfig",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class GoogleComputeInstanceTemplateConfig(cdktf.TerraformMetaArguments):
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
        disk: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceTemplateDisk", typing.Dict[str, typing.Any]]]],
        machine_type: builtins.str,
        advanced_machine_features: typing.Optional[typing.Union[GoogleComputeInstanceTemplateAdvancedMachineFeatures, typing.Dict[str, typing.Any]]] = None,
        can_ip_forward: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        confidential_instance_config: typing.Optional[typing.Union[GoogleComputeInstanceTemplateConfidentialInstanceConfig, typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_display: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        guest_accelerator: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceTemplateGuestAccelerator", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        instance_description: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        metadata_startup_script: typing.Optional[builtins.str] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        network_interface: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceTemplateNetworkInterface", typing.Dict[str, typing.Any]]]]] = None,
        network_performance_config: typing.Optional[typing.Union["GoogleComputeInstanceTemplateNetworkPerformanceConfig", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        reservation_affinity: typing.Optional[typing.Union["GoogleComputeInstanceTemplateReservationAffinity", typing.Dict[str, typing.Any]]] = None,
        scheduling: typing.Optional[typing.Union["GoogleComputeInstanceTemplateScheduling", typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[typing.Union["GoogleComputeInstanceTemplateServiceAccount", typing.Dict[str, typing.Any]]] = None,
        shielded_instance_config: typing.Optional[typing.Union["GoogleComputeInstanceTemplateShieldedInstanceConfig", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeInstanceTemplateTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param disk: disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#disk GoogleComputeInstanceTemplate#disk}
        :param machine_type: The machine type to create. To create a machine with a custom type (such as extended memory), format the value like custom-VCPUS-MEM_IN_MB like custom-6-20480 for 6 vCPU and 20GB of RAM. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#machine_type GoogleComputeInstanceTemplate#machine_type}
        :param advanced_machine_features: advanced_machine_features block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#advanced_machine_features GoogleComputeInstanceTemplate#advanced_machine_features}
        :param can_ip_forward: Whether to allow sending and receiving of packets with non-matching source or destination IPs. This defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#can_ip_forward GoogleComputeInstanceTemplate#can_ip_forward}
        :param confidential_instance_config: confidential_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#confidential_instance_config GoogleComputeInstanceTemplate#confidential_instance_config}
        :param description: A brief description of this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#description GoogleComputeInstanceTemplate#description}
        :param enable_display: Enable Virtual Displays on this instance. Note: allow_stopping_for_update must be set to true in order to update this field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#enable_display GoogleComputeInstanceTemplate#enable_display}
        :param guest_accelerator: guest_accelerator block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#guest_accelerator GoogleComputeInstanceTemplate#guest_accelerator}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#id GoogleComputeInstanceTemplate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_description: A description of the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#instance_description GoogleComputeInstanceTemplate#instance_description}
        :param labels: A set of key/value label pairs to assign to instances created from this template,. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#labels GoogleComputeInstanceTemplate#labels}
        :param metadata: Metadata key/value pairs to make available from within instances created from this template. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#metadata GoogleComputeInstanceTemplate#metadata}
        :param metadata_startup_script: An alternative to using the startup-script metadata key, mostly to match the compute_instance resource. This replaces the startup-script metadata key on the created instance and thus the two mechanisms are not allowed to be used simultaneously. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#metadata_startup_script GoogleComputeInstanceTemplate#metadata_startup_script}
        :param min_cpu_platform: Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as Intel Haswell or Intel Skylake. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#min_cpu_platform GoogleComputeInstanceTemplate#min_cpu_platform}
        :param name: The name of the instance template. If you leave this blank, Terraform will auto-generate a unique name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#name GoogleComputeInstanceTemplate#name}
        :param name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#name_prefix GoogleComputeInstanceTemplate#name_prefix}
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#network_interface GoogleComputeInstanceTemplate#network_interface}
        :param network_performance_config: network_performance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#network_performance_config GoogleComputeInstanceTemplate#network_performance_config}
        :param project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#project GoogleComputeInstanceTemplate#project}
        :param region: An instance template is a global resource that is not bound to a zone or a region. However, you can still specify some regional resources in an instance template, which restricts the template to the region where that resource resides. For example, a custom subnetwork resource is tied to a specific region. Defaults to the region of the Provider if no value is given. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#region GoogleComputeInstanceTemplate#region}
        :param reservation_affinity: reservation_affinity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#reservation_affinity GoogleComputeInstanceTemplate#reservation_affinity}
        :param scheduling: scheduling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#scheduling GoogleComputeInstanceTemplate#scheduling}
        :param service_account: service_account block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#service_account GoogleComputeInstanceTemplate#service_account}
        :param shielded_instance_config: shielded_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#shielded_instance_config GoogleComputeInstanceTemplate#shielded_instance_config}
        :param tags: Tags to attach to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#tags GoogleComputeInstanceTemplate#tags}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#timeouts GoogleComputeInstanceTemplate#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(advanced_machine_features, dict):
            advanced_machine_features = GoogleComputeInstanceTemplateAdvancedMachineFeatures(**advanced_machine_features)
        if isinstance(confidential_instance_config, dict):
            confidential_instance_config = GoogleComputeInstanceTemplateConfidentialInstanceConfig(**confidential_instance_config)
        if isinstance(network_performance_config, dict):
            network_performance_config = GoogleComputeInstanceTemplateNetworkPerformanceConfig(**network_performance_config)
        if isinstance(reservation_affinity, dict):
            reservation_affinity = GoogleComputeInstanceTemplateReservationAffinity(**reservation_affinity)
        if isinstance(scheduling, dict):
            scheduling = GoogleComputeInstanceTemplateScheduling(**scheduling)
        if isinstance(service_account, dict):
            service_account = GoogleComputeInstanceTemplateServiceAccount(**service_account)
        if isinstance(shielded_instance_config, dict):
            shielded_instance_config = GoogleComputeInstanceTemplateShieldedInstanceConfig(**shielded_instance_config)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeInstanceTemplateTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument disk", value=disk, expected_type=type_hints["disk"])
            check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
            check_type(argname="argument advanced_machine_features", value=advanced_machine_features, expected_type=type_hints["advanced_machine_features"])
            check_type(argname="argument can_ip_forward", value=can_ip_forward, expected_type=type_hints["can_ip_forward"])
            check_type(argname="argument confidential_instance_config", value=confidential_instance_config, expected_type=type_hints["confidential_instance_config"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enable_display", value=enable_display, expected_type=type_hints["enable_display"])
            check_type(argname="argument guest_accelerator", value=guest_accelerator, expected_type=type_hints["guest_accelerator"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instance_description", value=instance_description, expected_type=type_hints["instance_description"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument metadata_startup_script", value=metadata_startup_script, expected_type=type_hints["metadata_startup_script"])
            check_type(argname="argument min_cpu_platform", value=min_cpu_platform, expected_type=type_hints["min_cpu_platform"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument network_interface", value=network_interface, expected_type=type_hints["network_interface"])
            check_type(argname="argument network_performance_config", value=network_performance_config, expected_type=type_hints["network_performance_config"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument reservation_affinity", value=reservation_affinity, expected_type=type_hints["reservation_affinity"])
            check_type(argname="argument scheduling", value=scheduling, expected_type=type_hints["scheduling"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument shielded_instance_config", value=shielded_instance_config, expected_type=type_hints["shielded_instance_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "disk": disk,
            "machine_type": machine_type,
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
        if can_ip_forward is not None:
            self._values["can_ip_forward"] = can_ip_forward
        if confidential_instance_config is not None:
            self._values["confidential_instance_config"] = confidential_instance_config
        if description is not None:
            self._values["description"] = description
        if enable_display is not None:
            self._values["enable_display"] = enable_display
        if guest_accelerator is not None:
            self._values["guest_accelerator"] = guest_accelerator
        if id is not None:
            self._values["id"] = id
        if instance_description is not None:
            self._values["instance_description"] = instance_description
        if labels is not None:
            self._values["labels"] = labels
        if metadata is not None:
            self._values["metadata"] = metadata
        if metadata_startup_script is not None:
            self._values["metadata_startup_script"] = metadata_startup_script
        if min_cpu_platform is not None:
            self._values["min_cpu_platform"] = min_cpu_platform
        if name is not None:
            self._values["name"] = name
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
        if network_interface is not None:
            self._values["network_interface"] = network_interface
        if network_performance_config is not None:
            self._values["network_performance_config"] = network_performance_config
        if project is not None:
            self._values["project"] = project
        if region is not None:
            self._values["region"] = region
        if reservation_affinity is not None:
            self._values["reservation_affinity"] = reservation_affinity
        if scheduling is not None:
            self._values["scheduling"] = scheduling
        if service_account is not None:
            self._values["service_account"] = service_account
        if shielded_instance_config is not None:
            self._values["shielded_instance_config"] = shielded_instance_config
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
    def disk(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateDisk"]]:
        '''disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#disk GoogleComputeInstanceTemplate#disk}
        '''
        result = self._values.get("disk")
        assert result is not None, "Required property 'disk' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateDisk"]], result)

    @builtins.property
    def machine_type(self) -> builtins.str:
        '''The machine type to create.

        To create a machine with a custom type (such as extended memory), format the value like custom-VCPUS-MEM_IN_MB like custom-6-20480 for 6 vCPU and 20GB of RAM.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#machine_type GoogleComputeInstanceTemplate#machine_type}
        '''
        result = self._values.get("machine_type")
        assert result is not None, "Required property 'machine_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def advanced_machine_features(
        self,
    ) -> typing.Optional[GoogleComputeInstanceTemplateAdvancedMachineFeatures]:
        '''advanced_machine_features block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#advanced_machine_features GoogleComputeInstanceTemplate#advanced_machine_features}
        '''
        result = self._values.get("advanced_machine_features")
        return typing.cast(typing.Optional[GoogleComputeInstanceTemplateAdvancedMachineFeatures], result)

    @builtins.property
    def can_ip_forward(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to allow sending and receiving of packets with non-matching source or destination IPs. This defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#can_ip_forward GoogleComputeInstanceTemplate#can_ip_forward}
        '''
        result = self._values.get("can_ip_forward")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def confidential_instance_config(
        self,
    ) -> typing.Optional[GoogleComputeInstanceTemplateConfidentialInstanceConfig]:
        '''confidential_instance_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#confidential_instance_config GoogleComputeInstanceTemplate#confidential_instance_config}
        '''
        result = self._values.get("confidential_instance_config")
        return typing.cast(typing.Optional[GoogleComputeInstanceTemplateConfidentialInstanceConfig], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A brief description of this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#description GoogleComputeInstanceTemplate#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_display(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable Virtual Displays on this instance. Note: allow_stopping_for_update must be set to true in order to update this field.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#enable_display GoogleComputeInstanceTemplate#enable_display}
        '''
        result = self._values.get("enable_display")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def guest_accelerator(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateGuestAccelerator"]]]:
        '''guest_accelerator block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#guest_accelerator GoogleComputeInstanceTemplate#guest_accelerator}
        '''
        result = self._values.get("guest_accelerator")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateGuestAccelerator"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#id GoogleComputeInstanceTemplate#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_description(self) -> typing.Optional[builtins.str]:
        '''A description of the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#instance_description GoogleComputeInstanceTemplate#instance_description}
        '''
        result = self._values.get("instance_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A set of key/value label pairs to assign to instances created from this template,.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#labels GoogleComputeInstanceTemplate#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Metadata key/value pairs to make available from within instances created from this template.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#metadata GoogleComputeInstanceTemplate#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def metadata_startup_script(self) -> typing.Optional[builtins.str]:
        '''An alternative to using the startup-script metadata key, mostly to match the compute_instance resource.

        This replaces the startup-script metadata key on the created instance and thus the two mechanisms are not allowed to be used simultaneously.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#metadata_startup_script GoogleComputeInstanceTemplate#metadata_startup_script}
        '''
        result = self._values.get("metadata_startup_script")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_cpu_platform(self) -> typing.Optional[builtins.str]:
        '''Specifies a minimum CPU platform.

        Applicable values are the friendly names of CPU platforms, such as Intel Haswell or Intel Skylake.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#min_cpu_platform GoogleComputeInstanceTemplate#min_cpu_platform}
        '''
        result = self._values.get("min_cpu_platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the instance template. If you leave this blank, Terraform will auto-generate a unique name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#name GoogleComputeInstanceTemplate#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Creates a unique name beginning with the specified prefix. Conflicts with name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#name_prefix GoogleComputeInstanceTemplate#name_prefix}
        '''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_interface(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateNetworkInterface"]]]:
        '''network_interface block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#network_interface GoogleComputeInstanceTemplate#network_interface}
        '''
        result = self._values.get("network_interface")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateNetworkInterface"]]], result)

    @builtins.property
    def network_performance_config(
        self,
    ) -> typing.Optional["GoogleComputeInstanceTemplateNetworkPerformanceConfig"]:
        '''network_performance_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#network_performance_config GoogleComputeInstanceTemplate#network_performance_config}
        '''
        result = self._values.get("network_performance_config")
        return typing.cast(typing.Optional["GoogleComputeInstanceTemplateNetworkPerformanceConfig"], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The ID of the project in which the resource belongs.

        If it is not provided, the provider project is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#project GoogleComputeInstanceTemplate#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''An instance template is a global resource that is not bound to a zone or a region.

        However, you can still specify some regional resources in an instance template, which restricts the template to the region where that resource resides. For example, a custom subnetwork resource is tied to a specific region. Defaults to the region of the Provider if no value is given.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#region GoogleComputeInstanceTemplate#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reservation_affinity(
        self,
    ) -> typing.Optional["GoogleComputeInstanceTemplateReservationAffinity"]:
        '''reservation_affinity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#reservation_affinity GoogleComputeInstanceTemplate#reservation_affinity}
        '''
        result = self._values.get("reservation_affinity")
        return typing.cast(typing.Optional["GoogleComputeInstanceTemplateReservationAffinity"], result)

    @builtins.property
    def scheduling(self) -> typing.Optional["GoogleComputeInstanceTemplateScheduling"]:
        '''scheduling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#scheduling GoogleComputeInstanceTemplate#scheduling}
        '''
        result = self._values.get("scheduling")
        return typing.cast(typing.Optional["GoogleComputeInstanceTemplateScheduling"], result)

    @builtins.property
    def service_account(
        self,
    ) -> typing.Optional["GoogleComputeInstanceTemplateServiceAccount"]:
        '''service_account block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#service_account GoogleComputeInstanceTemplate#service_account}
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional["GoogleComputeInstanceTemplateServiceAccount"], result)

    @builtins.property
    def shielded_instance_config(
        self,
    ) -> typing.Optional["GoogleComputeInstanceTemplateShieldedInstanceConfig"]:
        '''shielded_instance_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#shielded_instance_config GoogleComputeInstanceTemplate#shielded_instance_config}
        '''
        result = self._values.get("shielded_instance_config")
        return typing.cast(typing.Optional["GoogleComputeInstanceTemplateShieldedInstanceConfig"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Tags to attach to the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#tags GoogleComputeInstanceTemplate#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeInstanceTemplateTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#timeouts GoogleComputeInstanceTemplate#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeInstanceTemplateTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceTemplateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateDisk",
    jsii_struct_bases=[],
    name_mapping={
        "auto_delete": "autoDelete",
        "boot": "boot",
        "device_name": "deviceName",
        "disk_encryption_key": "diskEncryptionKey",
        "disk_name": "diskName",
        "disk_size_gb": "diskSizeGb",
        "disk_type": "diskType",
        "interface": "interface",
        "labels": "labels",
        "mode": "mode",
        "resource_policies": "resourcePolicies",
        "source": "source",
        "source_image": "sourceImage",
        "type": "type",
    },
)
class GoogleComputeInstanceTemplateDisk:
    def __init__(
        self,
        *,
        auto_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        boot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        device_name: typing.Optional[builtins.str] = None,
        disk_encryption_key: typing.Optional[typing.Union["GoogleComputeInstanceTemplateDiskDiskEncryptionKey", typing.Dict[str, typing.Any]]] = None,
        disk_name: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        disk_type: typing.Optional[builtins.str] = None,
        interface: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        mode: typing.Optional[builtins.str] = None,
        resource_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        source: typing.Optional[builtins.str] = None,
        source_image: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_delete: Whether or not the disk should be auto-deleted. This defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#auto_delete GoogleComputeInstanceTemplate#auto_delete}
        :param boot: Indicates that this is a boot disk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#boot GoogleComputeInstanceTemplate#boot}
        :param device_name: A unique device name that is reflected into the /dev/ tree of a Linux operating system running within the instance. If not specified, the server chooses a default device name to apply to this disk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#device_name GoogleComputeInstanceTemplate#device_name}
        :param disk_encryption_key: disk_encryption_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#disk_encryption_key GoogleComputeInstanceTemplate#disk_encryption_key}
        :param disk_name: Name of the disk. When not provided, this defaults to the name of the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#disk_name GoogleComputeInstanceTemplate#disk_name}
        :param disk_size_gb: The size of the image in gigabytes. If not specified, it will inherit the size of its base image. For SCRATCH disks, the size must be exactly 375GB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#disk_size_gb GoogleComputeInstanceTemplate#disk_size_gb}
        :param disk_type: The Google Compute Engine disk type. Such as "pd-ssd", "local-ssd", "pd-balanced" or "pd-standard". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#disk_type GoogleComputeInstanceTemplate#disk_type}
        :param interface: Specifies the disk interface to use for attaching this disk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#interface GoogleComputeInstanceTemplate#interface}
        :param labels: A set of key/value label pairs to assign to disks,. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#labels GoogleComputeInstanceTemplate#labels}
        :param mode: The mode in which to attach this disk, either READ_WRITE or READ_ONLY. If you are attaching or creating a boot disk, this must read-write mode. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#mode GoogleComputeInstanceTemplate#mode}
        :param resource_policies: A list (short name or id) of resource policies to attach to this disk. Currently a max of 1 resource policy is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#resource_policies GoogleComputeInstanceTemplate#resource_policies}
        :param source: The name (not self_link) of the disk (such as those managed by google_compute_disk) to attach. ~> Note: Either source or source_image is required when creating a new instance except for when creating a local SSD. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#source GoogleComputeInstanceTemplate#source}
        :param source_image: The image from which to initialize this disk. This can be one of: the image's self_link, projects/{project}/global/images/{image}, projects/{project}/global/images/family/{family}, global/images/{image}, global/images/family/{family}, family/{family}, {project}/{family}, {project}/{image}, {family}, or {image}. ~> Note: Either source or source_image is required when creating a new instance except for when creating a local SSD. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#source_image GoogleComputeInstanceTemplate#source_image}
        :param type: The type of Google Compute Engine disk, can be either "SCRATCH" or "PERSISTENT". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#type GoogleComputeInstanceTemplate#type}
        '''
        if isinstance(disk_encryption_key, dict):
            disk_encryption_key = GoogleComputeInstanceTemplateDiskDiskEncryptionKey(**disk_encryption_key)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateDisk.__init__)
            check_type(argname="argument auto_delete", value=auto_delete, expected_type=type_hints["auto_delete"])
            check_type(argname="argument boot", value=boot, expected_type=type_hints["boot"])
            check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
            check_type(argname="argument disk_encryption_key", value=disk_encryption_key, expected_type=type_hints["disk_encryption_key"])
            check_type(argname="argument disk_name", value=disk_name, expected_type=type_hints["disk_name"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument disk_type", value=disk_type, expected_type=type_hints["disk_type"])
            check_type(argname="argument interface", value=interface, expected_type=type_hints["interface"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument resource_policies", value=resource_policies, expected_type=type_hints["resource_policies"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument source_image", value=source_image, expected_type=type_hints["source_image"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_delete is not None:
            self._values["auto_delete"] = auto_delete
        if boot is not None:
            self._values["boot"] = boot
        if device_name is not None:
            self._values["device_name"] = device_name
        if disk_encryption_key is not None:
            self._values["disk_encryption_key"] = disk_encryption_key
        if disk_name is not None:
            self._values["disk_name"] = disk_name
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if disk_type is not None:
            self._values["disk_type"] = disk_type
        if interface is not None:
            self._values["interface"] = interface
        if labels is not None:
            self._values["labels"] = labels
        if mode is not None:
            self._values["mode"] = mode
        if resource_policies is not None:
            self._values["resource_policies"] = resource_policies
        if source is not None:
            self._values["source"] = source
        if source_image is not None:
            self._values["source_image"] = source_image
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def auto_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not the disk should be auto-deleted. This defaults to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#auto_delete GoogleComputeInstanceTemplate#auto_delete}
        '''
        result = self._values.get("auto_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def boot(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates that this is a boot disk.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#boot GoogleComputeInstanceTemplate#boot}
        '''
        result = self._values.get("boot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def device_name(self) -> typing.Optional[builtins.str]:
        '''A unique device name that is reflected into the /dev/ tree of a Linux operating system running within the instance.

        If not specified, the server chooses a default device name to apply to this disk.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#device_name GoogleComputeInstanceTemplate#device_name}
        '''
        result = self._values.get("device_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_encryption_key(
        self,
    ) -> typing.Optional["GoogleComputeInstanceTemplateDiskDiskEncryptionKey"]:
        '''disk_encryption_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#disk_encryption_key GoogleComputeInstanceTemplate#disk_encryption_key}
        '''
        result = self._values.get("disk_encryption_key")
        return typing.cast(typing.Optional["GoogleComputeInstanceTemplateDiskDiskEncryptionKey"], result)

    @builtins.property
    def disk_name(self) -> typing.Optional[builtins.str]:
        '''Name of the disk. When not provided, this defaults to the name of the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#disk_name GoogleComputeInstanceTemplate#disk_name}
        '''
        result = self._values.get("disk_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''The size of the image in gigabytes.

        If not specified, it will inherit the size of its base image. For SCRATCH disks, the size must be exactly 375GB.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#disk_size_gb GoogleComputeInstanceTemplate#disk_size_gb}
        '''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk_type(self) -> typing.Optional[builtins.str]:
        '''The Google Compute Engine disk type. Such as "pd-ssd", "local-ssd", "pd-balanced" or "pd-standard".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#disk_type GoogleComputeInstanceTemplate#disk_type}
        '''
        result = self._values.get("disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def interface(self) -> typing.Optional[builtins.str]:
        '''Specifies the disk interface to use for attaching this disk.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#interface GoogleComputeInstanceTemplate#interface}
        '''
        result = self._values.get("interface")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A set of key/value label pairs to assign to disks,.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#labels GoogleComputeInstanceTemplate#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''The mode in which to attach this disk, either READ_WRITE or READ_ONLY.

        If you are attaching or creating a boot disk, this must read-write mode.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#mode GoogleComputeInstanceTemplate#mode}
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list (short name or id) of resource policies to attach to this disk.

        Currently a max of 1 resource policy is supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#resource_policies GoogleComputeInstanceTemplate#resource_policies}
        '''
        result = self._values.get("resource_policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''The name (not self_link) of the disk (such as those managed by google_compute_disk) to attach.

        ~> Note: Either source or source_image is required when creating a new instance except for when creating a local SSD.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#source GoogleComputeInstanceTemplate#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_image(self) -> typing.Optional[builtins.str]:
        '''The image from which to initialize this disk.

        This can be one of: the image's self_link, projects/{project}/global/images/{image}, projects/{project}/global/images/family/{family}, global/images/{image}, global/images/family/{family}, family/{family}, {project}/{family}, {project}/{image}, {family}, or {image}. ~> Note: Either source or source_image is required when creating a new instance except for when creating a local SSD.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#source_image GoogleComputeInstanceTemplate#source_image}
        '''
        result = self._values.get("source_image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of Google Compute Engine disk, can be either "SCRATCH" or "PERSISTENT".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#type GoogleComputeInstanceTemplate#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceTemplateDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateDiskDiskEncryptionKey",
    jsii_struct_bases=[],
    name_mapping={"kms_key_self_link": "kmsKeySelfLink"},
)
class GoogleComputeInstanceTemplateDiskDiskEncryptionKey:
    def __init__(self, *, kms_key_self_link: builtins.str) -> None:
        '''
        :param kms_key_self_link: The self link of the encryption key that is stored in Google Cloud KMS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#kms_key_self_link GoogleComputeInstanceTemplate#kms_key_self_link}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateDiskDiskEncryptionKey.__init__)
            check_type(argname="argument kms_key_self_link", value=kms_key_self_link, expected_type=type_hints["kms_key_self_link"])
        self._values: typing.Dict[str, typing.Any] = {
            "kms_key_self_link": kms_key_self_link,
        }

    @builtins.property
    def kms_key_self_link(self) -> builtins.str:
        '''The self link of the encryption key that is stored in Google Cloud KMS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#kms_key_self_link GoogleComputeInstanceTemplate#kms_key_self_link}
        '''
        result = self._values.get("kms_key_self_link")
        assert result is not None, "Required property 'kms_key_self_link' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceTemplateDiskDiskEncryptionKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceTemplateDiskDiskEncryptionKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateDiskDiskEncryptionKeyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateDiskDiskEncryptionKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="kmsKeySelfLinkInput")
    def kms_key_self_link_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeySelfLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeySelfLink")
    def kms_key_self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeySelfLink"))

    @kms_key_self_link.setter
    def kms_key_self_link(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskDiskEncryptionKeyOutputReference, "kms_key_self_link").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeySelfLink", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInstanceTemplateDiskDiskEncryptionKey]:
        return typing.cast(typing.Optional[GoogleComputeInstanceTemplateDiskDiskEncryptionKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInstanceTemplateDiskDiskEncryptionKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskDiskEncryptionKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceTemplateDiskList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateDiskList",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateDiskList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeInstanceTemplateDiskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateDiskList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeInstanceTemplateDiskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateDisk]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateDisk]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateDisk]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceTemplateDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateDiskOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDiskEncryptionKey")
    def put_disk_encryption_key(self, *, kms_key_self_link: builtins.str) -> None:
        '''
        :param kms_key_self_link: The self link of the encryption key that is stored in Google Cloud KMS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#kms_key_self_link GoogleComputeInstanceTemplate#kms_key_self_link}
        '''
        value = GoogleComputeInstanceTemplateDiskDiskEncryptionKey(
            kms_key_self_link=kms_key_self_link
        )

        return typing.cast(None, jsii.invoke(self, "putDiskEncryptionKey", [value]))

    @jsii.member(jsii_name="resetAutoDelete")
    def reset_auto_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoDelete", []))

    @jsii.member(jsii_name="resetBoot")
    def reset_boot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBoot", []))

    @jsii.member(jsii_name="resetDeviceName")
    def reset_device_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceName", []))

    @jsii.member(jsii_name="resetDiskEncryptionKey")
    def reset_disk_encryption_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskEncryptionKey", []))

    @jsii.member(jsii_name="resetDiskName")
    def reset_disk_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskName", []))

    @jsii.member(jsii_name="resetDiskSizeGb")
    def reset_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSizeGb", []))

    @jsii.member(jsii_name="resetDiskType")
    def reset_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskType", []))

    @jsii.member(jsii_name="resetInterface")
    def reset_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterface", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetResourcePolicies")
    def reset_resource_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourcePolicies", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="resetSourceImage")
    def reset_source_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceImage", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKey")
    def disk_encryption_key(
        self,
    ) -> GoogleComputeInstanceTemplateDiskDiskEncryptionKeyOutputReference:
        return typing.cast(GoogleComputeInstanceTemplateDiskDiskEncryptionKeyOutputReference, jsii.get(self, "diskEncryptionKey"))

    @builtins.property
    @jsii.member(jsii_name="autoDeleteInput")
    def auto_delete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoDeleteInput"))

    @builtins.property
    @jsii.member(jsii_name="bootInput")
    def boot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "bootInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceNameInput")
    def device_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKeyInput")
    def disk_encryption_key_input(
        self,
    ) -> typing.Optional[GoogleComputeInstanceTemplateDiskDiskEncryptionKey]:
        return typing.cast(typing.Optional[GoogleComputeInstanceTemplateDiskDiskEncryptionKey], jsii.get(self, "diskEncryptionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="diskNameInput")
    def disk_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskNameInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="diskTypeInput")
    def disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="interfaceInput")
    def interface_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourcePoliciesInput")
    def resource_policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourcePoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceImageInput")
    def source_image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceImageInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskOutputReference, "auto_delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoDelete", value)

    @builtins.property
    @jsii.member(jsii_name="boot")
    def boot(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "boot"))

    @boot.setter
    def boot(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskOutputReference, "boot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "boot", value)

    @builtins.property
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceName"))

    @device_name.setter
    def device_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskOutputReference, "device_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceName", value)

    @builtins.property
    @jsii.member(jsii_name="diskName")
    def disk_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskName"))

    @disk_name.setter
    def disk_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskOutputReference, "disk_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskName", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskOutputReference, "disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="diskType")
    def disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskType"))

    @disk_type.setter
    def disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskOutputReference, "disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskType", value)

    @builtins.property
    @jsii.member(jsii_name="interface")
    def interface(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interface"))

    @interface.setter
    def interface(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskOutputReference, "interface").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interface", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="resourcePolicies")
    def resource_policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourcePolicies"))

    @resource_policies.setter
    def resource_policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskOutputReference, "resource_policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourcePolicies", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="sourceImage")
    def source_image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceImage"))

    @source_image.setter
    def source_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskOutputReference, "source_image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceImage", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInstanceTemplateDisk, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInstanceTemplateDisk, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInstanceTemplateDisk, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateGuestAccelerator",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "type": "type"},
)
class GoogleComputeInstanceTemplateGuestAccelerator:
    def __init__(self, *, count: jsii.Number, type: builtins.str) -> None:
        '''
        :param count: The number of the guest accelerator cards exposed to this instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#count GoogleComputeInstanceTemplate#count}
        :param type: The accelerator type resource to expose to this instance. E.g. nvidia-tesla-k80. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#type GoogleComputeInstanceTemplate#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateGuestAccelerator.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
            "type": type,
        }

    @builtins.property
    def count(self) -> jsii.Number:
        '''The number of the guest accelerator cards exposed to this instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#count GoogleComputeInstanceTemplate#count}
        '''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The accelerator type resource to expose to this instance. E.g. nvidia-tesla-k80.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#type GoogleComputeInstanceTemplate#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceTemplateGuestAccelerator(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceTemplateGuestAcceleratorList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateGuestAcceleratorList",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateGuestAcceleratorList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeInstanceTemplateGuestAcceleratorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateGuestAcceleratorList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeInstanceTemplateGuestAcceleratorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateGuestAcceleratorList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateGuestAcceleratorList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateGuestAcceleratorList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateGuestAccelerator]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateGuestAccelerator]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateGuestAccelerator]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateGuestAcceleratorList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceTemplateGuestAcceleratorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateGuestAcceleratorOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateGuestAcceleratorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateGuestAcceleratorOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateGuestAcceleratorOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInstanceTemplateGuestAccelerator, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInstanceTemplateGuestAccelerator, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInstanceTemplateGuestAccelerator, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateGuestAcceleratorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateNetworkInterface",
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
class GoogleComputeInstanceTemplateNetworkInterface:
    def __init__(
        self,
        *,
        access_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceTemplateNetworkInterfaceAccessConfig", typing.Dict[str, typing.Any]]]]] = None,
        alias_ip_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRange", typing.Dict[str, typing.Any]]]]] = None,
        ipv6_access_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfig", typing.Dict[str, typing.Any]]]]] = None,
        network: typing.Optional[builtins.str] = None,
        network_ip: typing.Optional[builtins.str] = None,
        nic_type: typing.Optional[builtins.str] = None,
        queue_count: typing.Optional[jsii.Number] = None,
        stack_type: typing.Optional[builtins.str] = None,
        subnetwork: typing.Optional[builtins.str] = None,
        subnetwork_project: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_config: access_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#access_config GoogleComputeInstanceTemplate#access_config}
        :param alias_ip_range: alias_ip_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#alias_ip_range GoogleComputeInstanceTemplate#alias_ip_range}
        :param ipv6_access_config: ipv6_access_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#ipv6_access_config GoogleComputeInstanceTemplate#ipv6_access_config}
        :param network: The name or self_link of the network to attach this interface to. Use network attribute for Legacy or Auto subnetted networks and subnetwork for custom subnetted networks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#network GoogleComputeInstanceTemplate#network}
        :param network_ip: The private IP address to assign to the instance. If empty, the address will be automatically assigned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#network_ip GoogleComputeInstanceTemplate#network_ip}
        :param nic_type: The type of vNIC to be used on this interface. Possible values:GVNIC, VIRTIO_NET. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#nic_type GoogleComputeInstanceTemplate#nic_type}
        :param queue_count: The networking queue count that's specified by users for the network interface. Both Rx and Tx queues will be set to this number. It will be empty if not specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#queue_count GoogleComputeInstanceTemplate#queue_count}
        :param stack_type: The stack type for this network interface to identify whether the IPv6 feature is enabled or not. If not specified, IPV4_ONLY will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#stack_type GoogleComputeInstanceTemplate#stack_type}
        :param subnetwork: The name of the subnetwork to attach this interface to. The subnetwork must exist in the same region this instance will be created in. Either network or subnetwork must be provided. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#subnetwork GoogleComputeInstanceTemplate#subnetwork}
        :param subnetwork_project: The ID of the project in which the subnetwork belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#subnetwork_project GoogleComputeInstanceTemplate#subnetwork_project}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterface.__init__)
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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateNetworkInterfaceAccessConfig"]]]:
        '''access_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#access_config GoogleComputeInstanceTemplate#access_config}
        '''
        result = self._values.get("access_config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateNetworkInterfaceAccessConfig"]]], result)

    @builtins.property
    def alias_ip_range(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRange"]]]:
        '''alias_ip_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#alias_ip_range GoogleComputeInstanceTemplate#alias_ip_range}
        '''
        result = self._values.get("alias_ip_range")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRange"]]], result)

    @builtins.property
    def ipv6_access_config(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfig"]]]:
        '''ipv6_access_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#ipv6_access_config GoogleComputeInstanceTemplate#ipv6_access_config}
        '''
        result = self._values.get("ipv6_access_config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfig"]]], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''The name or self_link of the network to attach this interface to.

        Use network attribute for Legacy or Auto subnetted networks and subnetwork for custom subnetted networks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#network GoogleComputeInstanceTemplate#network}
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_ip(self) -> typing.Optional[builtins.str]:
        '''The private IP address to assign to the instance. If empty, the address will be automatically assigned.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#network_ip GoogleComputeInstanceTemplate#network_ip}
        '''
        result = self._values.get("network_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nic_type(self) -> typing.Optional[builtins.str]:
        '''The type of vNIC to be used on this interface. Possible values:GVNIC, VIRTIO_NET.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#nic_type GoogleComputeInstanceTemplate#nic_type}
        '''
        result = self._values.get("nic_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def queue_count(self) -> typing.Optional[jsii.Number]:
        '''The networking queue count that's specified by users for the network interface.

        Both Rx and Tx queues will be set to this number. It will be empty if not specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#queue_count GoogleComputeInstanceTemplate#queue_count}
        '''
        result = self._values.get("queue_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stack_type(self) -> typing.Optional[builtins.str]:
        '''The stack type for this network interface to identify whether the IPv6 feature is enabled or not.

        If not specified, IPV4_ONLY will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#stack_type GoogleComputeInstanceTemplate#stack_type}
        '''
        result = self._values.get("stack_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnetwork(self) -> typing.Optional[builtins.str]:
        '''The name of the subnetwork to attach this interface to.

        The subnetwork must exist in the same region this instance will be created in. Either network or subnetwork must be provided.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#subnetwork GoogleComputeInstanceTemplate#subnetwork}
        '''
        result = self._values.get("subnetwork")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnetwork_project(self) -> typing.Optional[builtins.str]:
        '''The ID of the project in which the subnetwork belongs.

        If it is not provided, the provider project is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#subnetwork_project GoogleComputeInstanceTemplate#subnetwork_project}
        '''
        result = self._values.get("subnetwork_project")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceTemplateNetworkInterface(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateNetworkInterfaceAccessConfig",
    jsii_struct_bases=[],
    name_mapping={"nat_ip": "natIp", "network_tier": "networkTier"},
)
class GoogleComputeInstanceTemplateNetworkInterfaceAccessConfig:
    def __init__(
        self,
        *,
        nat_ip: typing.Optional[builtins.str] = None,
        network_tier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param nat_ip: The IP address that will be 1:1 mapped to the instance's network ip. If not given, one will be generated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#nat_ip GoogleComputeInstanceTemplate#nat_ip}
        :param network_tier: The networking tier used for configuring this instance template. This field can take the following values: PREMIUM, STANDARD, FIXED_STANDARD. If this field is not specified, it is assumed to be PREMIUM. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#network_tier GoogleComputeInstanceTemplate#network_tier}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterfaceAccessConfig.__init__)
            check_type(argname="argument nat_ip", value=nat_ip, expected_type=type_hints["nat_ip"])
            check_type(argname="argument network_tier", value=network_tier, expected_type=type_hints["network_tier"])
        self._values: typing.Dict[str, typing.Any] = {}
        if nat_ip is not None:
            self._values["nat_ip"] = nat_ip
        if network_tier is not None:
            self._values["network_tier"] = network_tier

    @builtins.property
    def nat_ip(self) -> typing.Optional[builtins.str]:
        '''The IP address that will be 1:1 mapped to the instance's network ip.

        If not given, one will be generated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#nat_ip GoogleComputeInstanceTemplate#nat_ip}
        '''
        result = self._values.get("nat_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_tier(self) -> typing.Optional[builtins.str]:
        '''The networking tier used for configuring this instance template.

        This field can take the following values: PREMIUM, STANDARD, FIXED_STANDARD. If this field is not specified, it is assumed to be PREMIUM.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#network_tier GoogleComputeInstanceTemplate#network_tier}
        '''
        result = self._values.get("network_tier")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceTemplateNetworkInterfaceAccessConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigList",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateNetworkInterfaceAccessConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateNetworkInterfaceAccessConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateNetworkInterfaceAccessConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigOutputReference.__init__)
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

    @builtins.property
    @jsii.member(jsii_name="publicPtrDomainName")
    def public_ptr_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicPtrDomainName"))

    @builtins.property
    @jsii.member(jsii_name="natIpInput")
    def nat_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "natIpInput"))

    @builtins.property
    @jsii.member(jsii_name="networkTierInput")
    def network_tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkTierInput"))

    @builtins.property
    @jsii.member(jsii_name="natIp")
    def nat_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "natIp"))

    @nat_ip.setter
    def nat_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigOutputReference, "nat_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "natIp", value)

    @builtins.property
    @jsii.member(jsii_name="networkTier")
    def network_tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkTier"))

    @network_tier.setter
    def network_tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigOutputReference, "network_tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkTier", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInstanceTemplateNetworkInterfaceAccessConfig, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInstanceTemplateNetworkInterfaceAccessConfig, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInstanceTemplateNetworkInterfaceAccessConfig, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRange",
    jsii_struct_bases=[],
    name_mapping={
        "ip_cidr_range": "ipCidrRange",
        "subnetwork_range_name": "subnetworkRangeName",
    },
)
class GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRange:
    def __init__(
        self,
        *,
        ip_cidr_range: builtins.str,
        subnetwork_range_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ip_cidr_range: The IP CIDR range represented by this alias IP range. This IP CIDR range must belong to the specified subnetwork and cannot contain IP addresses reserved by system or used by other network interfaces. At the time of writing only a netmask (e.g. /24) may be supplied, with a CIDR format resulting in an API error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#ip_cidr_range GoogleComputeInstanceTemplate#ip_cidr_range}
        :param subnetwork_range_name: The subnetwork secondary range name specifying the secondary range from which to allocate the IP CIDR range for this alias IP range. If left unspecified, the primary range of the subnetwork will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#subnetwork_range_name GoogleComputeInstanceTemplate#subnetwork_range_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRange.__init__)
            check_type(argname="argument ip_cidr_range", value=ip_cidr_range, expected_type=type_hints["ip_cidr_range"])
            check_type(argname="argument subnetwork_range_name", value=subnetwork_range_name, expected_type=type_hints["subnetwork_range_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "ip_cidr_range": ip_cidr_range,
        }
        if subnetwork_range_name is not None:
            self._values["subnetwork_range_name"] = subnetwork_range_name

    @builtins.property
    def ip_cidr_range(self) -> builtins.str:
        '''The IP CIDR range represented by this alias IP range.

        This IP CIDR range must belong to the specified subnetwork and cannot contain IP addresses reserved by system or used by other network interfaces. At the time of writing only a netmask (e.g. /24) may be supplied, with a CIDR format resulting in an API error.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#ip_cidr_range GoogleComputeInstanceTemplate#ip_cidr_range}
        '''
        result = self._values.get("ip_cidr_range")
        assert result is not None, "Required property 'ip_cidr_range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnetwork_range_name(self) -> typing.Optional[builtins.str]:
        '''The subnetwork secondary range name specifying the secondary range from which to allocate the IP CIDR range for this alias IP range.

        If left unspecified, the primary range of the subnetwork will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#subnetwork_range_name GoogleComputeInstanceTemplate#subnetwork_range_name}
        '''
        result = self._values.get("subnetwork_range_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeList",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeOutputReference, "ip_cidr_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipCidrRange", value)

    @builtins.property
    @jsii.member(jsii_name="subnetworkRangeName")
    def subnetwork_range_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetworkRangeName"))

    @subnetwork_range_name.setter
    def subnetwork_range_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeOutputReference, "subnetwork_range_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetworkRangeName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRange, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRange, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRange, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfig",
    jsii_struct_bases=[],
    name_mapping={"network_tier": "networkTier"},
)
class GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfig:
    def __init__(self, *, network_tier: builtins.str) -> None:
        '''
        :param network_tier: The service-level to be provided for IPv6 traffic when the subnet has an external subnet. Only PREMIUM tier is valid for IPv6 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#network_tier GoogleComputeInstanceTemplate#network_tier}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfig.__init__)
            check_type(argname="argument network_tier", value=network_tier, expected_type=type_hints["network_tier"])
        self._values: typing.Dict[str, typing.Any] = {
            "network_tier": network_tier,
        }

    @builtins.property
    def network_tier(self) -> builtins.str:
        '''The service-level to be provided for IPv6 traffic when the subnet has an external subnet.

        Only PREMIUM tier is valid for IPv6

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#network_tier GoogleComputeInstanceTemplate#network_tier}
        '''
        result = self._values.get("network_tier")
        assert result is not None, "Required property 'network_tier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigList",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="externalIpv6")
    def external_ipv6(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalIpv6"))

    @builtins.property
    @jsii.member(jsii_name="externalIpv6PrefixLength")
    def external_ipv6_prefix_length(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalIpv6PrefixLength"))

    @builtins.property
    @jsii.member(jsii_name="publicPtrDomainName")
    def public_ptr_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicPtrDomainName"))

    @builtins.property
    @jsii.member(jsii_name="networkTierInput")
    def network_tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkTierInput"))

    @builtins.property
    @jsii.member(jsii_name="networkTier")
    def network_tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkTier"))

    @network_tier.setter
    def network_tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigOutputReference, "network_tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkTier", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfig, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfig, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfig, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceTemplateNetworkInterfaceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateNetworkInterfaceList",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterfaceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeInstanceTemplateNetworkInterfaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterfaceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeInstanceTemplateNetworkInterfaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateNetworkInterface]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateNetworkInterface]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateNetworkInterface]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceTemplateNetworkInterfaceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateNetworkInterfaceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterfaceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAccessConfig")
    def put_access_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeInstanceTemplateNetworkInterfaceAccessConfig, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterfaceOutputReference.put_access_config)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccessConfig", [value]))

    @jsii.member(jsii_name="putAliasIpRange")
    def put_alias_ip_range(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRange, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterfaceOutputReference.put_alias_ip_range)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAliasIpRange", [value]))

    @jsii.member(jsii_name="putIpv6AccessConfig")
    def put_ipv6_access_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfig, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkInterfaceOutputReference.put_ipv6_access_config)
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
    ) -> GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigList:
        return typing.cast(GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigList, jsii.get(self, "accessConfig"))

    @builtins.property
    @jsii.member(jsii_name="aliasIpRange")
    def alias_ip_range(
        self,
    ) -> GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeList:
        return typing.cast(GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeList, jsii.get(self, "aliasIpRange"))

    @builtins.property
    @jsii.member(jsii_name="ipv6AccessConfig")
    def ipv6_access_config(
        self,
    ) -> GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigList:
        return typing.cast(GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigList, jsii.get(self, "ipv6AccessConfig"))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateNetworkInterfaceAccessConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateNetworkInterfaceAccessConfig]]], jsii.get(self, "accessConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasIpRangeInput")
    def alias_ip_range_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRange]]], jsii.get(self, "aliasIpRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6AccessConfigInput")
    def ipv6_access_config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfig]]], jsii.get(self, "ipv6AccessConfigInput"))

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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceOutputReference, "network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="networkIp")
    def network_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkIp"))

    @network_ip.setter
    def network_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceOutputReference, "network_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkIp", value)

    @builtins.property
    @jsii.member(jsii_name="nicType")
    def nic_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nicType"))

    @nic_type.setter
    def nic_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceOutputReference, "nic_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nicType", value)

    @builtins.property
    @jsii.member(jsii_name="queueCount")
    def queue_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "queueCount"))

    @queue_count.setter
    def queue_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceOutputReference, "queue_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queueCount", value)

    @builtins.property
    @jsii.member(jsii_name="stackType")
    def stack_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stackType"))

    @stack_type.setter
    def stack_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceOutputReference, "stack_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackType", value)

    @builtins.property
    @jsii.member(jsii_name="subnetwork")
    def subnetwork(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetwork"))

    @subnetwork.setter
    def subnetwork(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceOutputReference, "subnetwork").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetwork", value)

    @builtins.property
    @jsii.member(jsii_name="subnetworkProject")
    def subnetwork_project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetworkProject"))

    @subnetwork_project.setter
    def subnetwork_project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceOutputReference, "subnetwork_project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetworkProject", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInstanceTemplateNetworkInterface, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInstanceTemplateNetworkInterface, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInstanceTemplateNetworkInterface, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkInterfaceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateNetworkPerformanceConfig",
    jsii_struct_bases=[],
    name_mapping={"total_egress_bandwidth_tier": "totalEgressBandwidthTier"},
)
class GoogleComputeInstanceTemplateNetworkPerformanceConfig:
    def __init__(self, *, total_egress_bandwidth_tier: builtins.str) -> None:
        '''
        :param total_egress_bandwidth_tier: The egress bandwidth tier to enable. Possible values:TIER_1, DEFAULT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#total_egress_bandwidth_tier GoogleComputeInstanceTemplate#total_egress_bandwidth_tier}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkPerformanceConfig.__init__)
            check_type(argname="argument total_egress_bandwidth_tier", value=total_egress_bandwidth_tier, expected_type=type_hints["total_egress_bandwidth_tier"])
        self._values: typing.Dict[str, typing.Any] = {
            "total_egress_bandwidth_tier": total_egress_bandwidth_tier,
        }

    @builtins.property
    def total_egress_bandwidth_tier(self) -> builtins.str:
        '''The egress bandwidth tier to enable. Possible values:TIER_1, DEFAULT.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#total_egress_bandwidth_tier GoogleComputeInstanceTemplate#total_egress_bandwidth_tier}
        '''
        result = self._values.get("total_egress_bandwidth_tier")
        assert result is not None, "Required property 'total_egress_bandwidth_tier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceTemplateNetworkPerformanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceTemplateNetworkPerformanceConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateNetworkPerformanceConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateNetworkPerformanceConfigOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkPerformanceConfigOutputReference, "total_egress_bandwidth_tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "totalEgressBandwidthTier", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInstanceTemplateNetworkPerformanceConfig]:
        return typing.cast(typing.Optional[GoogleComputeInstanceTemplateNetworkPerformanceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInstanceTemplateNetworkPerformanceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateNetworkPerformanceConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateReservationAffinity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "specific_reservation": "specificReservation"},
)
class GoogleComputeInstanceTemplateReservationAffinity:
    def __init__(
        self,
        *,
        type: builtins.str,
        specific_reservation: typing.Optional[typing.Union["GoogleComputeInstanceTemplateReservationAffinitySpecificReservation", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: The type of reservation from which this instance can consume resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#type GoogleComputeInstanceTemplate#type}
        :param specific_reservation: specific_reservation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#specific_reservation GoogleComputeInstanceTemplate#specific_reservation}
        '''
        if isinstance(specific_reservation, dict):
            specific_reservation = GoogleComputeInstanceTemplateReservationAffinitySpecificReservation(**specific_reservation)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateReservationAffinity.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#type GoogleComputeInstanceTemplate#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def specific_reservation(
        self,
    ) -> typing.Optional["GoogleComputeInstanceTemplateReservationAffinitySpecificReservation"]:
        '''specific_reservation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#specific_reservation GoogleComputeInstanceTemplate#specific_reservation}
        '''
        result = self._values.get("specific_reservation")
        return typing.cast(typing.Optional["GoogleComputeInstanceTemplateReservationAffinitySpecificReservation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceTemplateReservationAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceTemplateReservationAffinityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateReservationAffinityOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateReservationAffinityOutputReference.__init__)
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
        :param key: Corresponds to the label key of a reservation resource. To target a SPECIFIC_RESERVATION by name, specify compute.googleapis.com/reservation-name as the key and specify the name of your reservation as the only value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#key GoogleComputeInstanceTemplate#key}
        :param values: Corresponds to the label values of a reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#values GoogleComputeInstanceTemplate#values}
        '''
        value = GoogleComputeInstanceTemplateReservationAffinitySpecificReservation(
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
    ) -> "GoogleComputeInstanceTemplateReservationAffinitySpecificReservationOutputReference":
        return typing.cast("GoogleComputeInstanceTemplateReservationAffinitySpecificReservationOutputReference", jsii.get(self, "specificReservation"))

    @builtins.property
    @jsii.member(jsii_name="specificReservationInput")
    def specific_reservation_input(
        self,
    ) -> typing.Optional["GoogleComputeInstanceTemplateReservationAffinitySpecificReservation"]:
        return typing.cast(typing.Optional["GoogleComputeInstanceTemplateReservationAffinitySpecificReservation"], jsii.get(self, "specificReservationInput"))

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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateReservationAffinityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInstanceTemplateReservationAffinity]:
        return typing.cast(typing.Optional[GoogleComputeInstanceTemplateReservationAffinity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInstanceTemplateReservationAffinity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateReservationAffinityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateReservationAffinitySpecificReservation",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class GoogleComputeInstanceTemplateReservationAffinitySpecificReservation:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Corresponds to the label key of a reservation resource. To target a SPECIFIC_RESERVATION by name, specify compute.googleapis.com/reservation-name as the key and specify the name of your reservation as the only value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#key GoogleComputeInstanceTemplate#key}
        :param values: Corresponds to the label values of a reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#values GoogleComputeInstanceTemplate#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateReservationAffinitySpecificReservation.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#key GoogleComputeInstanceTemplate#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Corresponds to the label values of a reservation resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#values GoogleComputeInstanceTemplate#values}
        '''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceTemplateReservationAffinitySpecificReservation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceTemplateReservationAffinitySpecificReservationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateReservationAffinitySpecificReservationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateReservationAffinitySpecificReservationOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateReservationAffinitySpecificReservationOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateReservationAffinitySpecificReservationOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInstanceTemplateReservationAffinitySpecificReservation]:
        return typing.cast(typing.Optional[GoogleComputeInstanceTemplateReservationAffinitySpecificReservation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInstanceTemplateReservationAffinitySpecificReservation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateReservationAffinitySpecificReservationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateScheduling",
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
class GoogleComputeInstanceTemplateScheduling:
    def __init__(
        self,
        *,
        automatic_restart: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        instance_termination_action: typing.Optional[builtins.str] = None,
        min_node_cpus: typing.Optional[jsii.Number] = None,
        node_affinities: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeInstanceTemplateSchedulingNodeAffinities", typing.Dict[str, typing.Any]]]]] = None,
        on_host_maintenance: typing.Optional[builtins.str] = None,
        preemptible: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        provisioning_model: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param automatic_restart: Specifies whether the instance should be automatically restarted if it is terminated by Compute Engine (not terminated by a user). This defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#automatic_restart GoogleComputeInstanceTemplate#automatic_restart}
        :param instance_termination_action: Specifies the action GCE should take when SPOT VM is preempted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#instance_termination_action GoogleComputeInstanceTemplate#instance_termination_action}
        :param min_node_cpus: Minimum number of cpus for the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#min_node_cpus GoogleComputeInstanceTemplate#min_node_cpus}
        :param node_affinities: node_affinities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#node_affinities GoogleComputeInstanceTemplate#node_affinities}
        :param on_host_maintenance: Defines the maintenance behavior for this instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#on_host_maintenance GoogleComputeInstanceTemplate#on_host_maintenance}
        :param preemptible: Allows instance to be preempted. This defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#preemptible GoogleComputeInstanceTemplate#preemptible}
        :param provisioning_model: Whether the instance is spot. If this is set as SPOT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#provisioning_model GoogleComputeInstanceTemplate#provisioning_model}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateScheduling.__init__)
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
        '''Specifies whether the instance should be automatically restarted if it is terminated by Compute Engine (not terminated by a user).

        This defaults to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#automatic_restart GoogleComputeInstanceTemplate#automatic_restart}
        '''
        result = self._values.get("automatic_restart")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def instance_termination_action(self) -> typing.Optional[builtins.str]:
        '''Specifies the action GCE should take when SPOT VM is preempted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#instance_termination_action GoogleComputeInstanceTemplate#instance_termination_action}
        '''
        result = self._values.get("instance_termination_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_node_cpus(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of cpus for the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#min_node_cpus GoogleComputeInstanceTemplate#min_node_cpus}
        '''
        result = self._values.get("min_node_cpus")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def node_affinities(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateSchedulingNodeAffinities"]]]:
        '''node_affinities block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#node_affinities GoogleComputeInstanceTemplate#node_affinities}
        '''
        result = self._values.get("node_affinities")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeInstanceTemplateSchedulingNodeAffinities"]]], result)

    @builtins.property
    def on_host_maintenance(self) -> typing.Optional[builtins.str]:
        '''Defines the maintenance behavior for this instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#on_host_maintenance GoogleComputeInstanceTemplate#on_host_maintenance}
        '''
        result = self._values.get("on_host_maintenance")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preemptible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allows instance to be preempted. This defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#preemptible GoogleComputeInstanceTemplate#preemptible}
        '''
        result = self._values.get("preemptible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def provisioning_model(self) -> typing.Optional[builtins.str]:
        '''Whether the instance is spot. If this is set as SPOT.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#provisioning_model GoogleComputeInstanceTemplate#provisioning_model}
        '''
        result = self._values.get("provisioning_model")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceTemplateScheduling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateSchedulingNodeAffinities",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class GoogleComputeInstanceTemplateSchedulingNodeAffinities:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#key GoogleComputeInstanceTemplate#key}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#operator GoogleComputeInstanceTemplate#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#values GoogleComputeInstanceTemplate#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateSchedulingNodeAffinities.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#key GoogleComputeInstanceTemplate#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#operator GoogleComputeInstanceTemplate#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#values GoogleComputeInstanceTemplate#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceTemplateSchedulingNodeAffinities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceTemplateSchedulingNodeAffinitiesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateSchedulingNodeAffinitiesList",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateSchedulingNodeAffinitiesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeInstanceTemplateSchedulingNodeAffinitiesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateSchedulingNodeAffinitiesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeInstanceTemplateSchedulingNodeAffinitiesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateSchedulingNodeAffinitiesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateSchedulingNodeAffinitiesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateSchedulingNodeAffinitiesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateSchedulingNodeAffinities]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateSchedulingNodeAffinities]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateSchedulingNodeAffinities]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateSchedulingNodeAffinitiesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceTemplateSchedulingNodeAffinitiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateSchedulingNodeAffinitiesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateSchedulingNodeAffinitiesOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateSchedulingNodeAffinitiesOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateSchedulingNodeAffinitiesOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateSchedulingNodeAffinitiesOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInstanceTemplateSchedulingNodeAffinities, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInstanceTemplateSchedulingNodeAffinities, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInstanceTemplateSchedulingNodeAffinities, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateSchedulingNodeAffinitiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeInstanceTemplateSchedulingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateSchedulingOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateSchedulingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNodeAffinities")
    def put_node_affinities(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeInstanceTemplateSchedulingNodeAffinities, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateSchedulingOutputReference.put_node_affinities)
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
    ) -> GoogleComputeInstanceTemplateSchedulingNodeAffinitiesList:
        return typing.cast(GoogleComputeInstanceTemplateSchedulingNodeAffinitiesList, jsii.get(self, "nodeAffinities"))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateSchedulingNodeAffinities]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeInstanceTemplateSchedulingNodeAffinities]]], jsii.get(self, "nodeAffinitiesInput"))

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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateSchedulingOutputReference, "automatic_restart").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticRestart", value)

    @builtins.property
    @jsii.member(jsii_name="instanceTerminationAction")
    def instance_termination_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceTerminationAction"))

    @instance_termination_action.setter
    def instance_termination_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateSchedulingOutputReference, "instance_termination_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceTerminationAction", value)

    @builtins.property
    @jsii.member(jsii_name="minNodeCpus")
    def min_node_cpus(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minNodeCpus"))

    @min_node_cpus.setter
    def min_node_cpus(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateSchedulingOutputReference, "min_node_cpus").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minNodeCpus", value)

    @builtins.property
    @jsii.member(jsii_name="onHostMaintenance")
    def on_host_maintenance(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onHostMaintenance"))

    @on_host_maintenance.setter
    def on_host_maintenance(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateSchedulingOutputReference, "on_host_maintenance").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateSchedulingOutputReference, "preemptible").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preemptible", value)

    @builtins.property
    @jsii.member(jsii_name="provisioningModel")
    def provisioning_model(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "provisioningModel"))

    @provisioning_model.setter
    def provisioning_model(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateSchedulingOutputReference, "provisioning_model").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisioningModel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInstanceTemplateScheduling]:
        return typing.cast(typing.Optional[GoogleComputeInstanceTemplateScheduling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInstanceTemplateScheduling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateSchedulingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateServiceAccount",
    jsii_struct_bases=[],
    name_mapping={"scopes": "scopes", "email": "email"},
)
class GoogleComputeInstanceTemplateServiceAccount:
    def __init__(
        self,
        *,
        scopes: typing.Sequence[builtins.str],
        email: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scopes: A list of service scopes. Both OAuth2 URLs and gcloud short names are supported. To allow full access to all Cloud APIs, use the cloud-platform scope. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#scopes GoogleComputeInstanceTemplate#scopes}
        :param email: The service account e-mail address. If not given, the default Google Compute Engine service account is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#email GoogleComputeInstanceTemplate#email}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateServiceAccount.__init__)
            check_type(argname="argument scopes", value=scopes, expected_type=type_hints["scopes"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
        self._values: typing.Dict[str, typing.Any] = {
            "scopes": scopes,
        }
        if email is not None:
            self._values["email"] = email

    @builtins.property
    def scopes(self) -> typing.List[builtins.str]:
        '''A list of service scopes.

        Both OAuth2 URLs and gcloud short names are supported. To allow full access to all Cloud APIs, use the cloud-platform scope.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#scopes GoogleComputeInstanceTemplate#scopes}
        '''
        result = self._values.get("scopes")
        assert result is not None, "Required property 'scopes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''The service account e-mail address. If not given, the default Google Compute Engine service account is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#email GoogleComputeInstanceTemplate#email}
        '''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceTemplateServiceAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceTemplateServiceAccountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateServiceAccountOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateServiceAccountOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateServiceAccountOutputReference, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="scopes")
    def scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "scopes"))

    @scopes.setter
    def scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateServiceAccountOutputReference, "scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInstanceTemplateServiceAccount]:
        return typing.cast(typing.Optional[GoogleComputeInstanceTemplateServiceAccount], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInstanceTemplateServiceAccount],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateServiceAccountOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateShieldedInstanceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "enable_integrity_monitoring": "enableIntegrityMonitoring",
        "enable_secure_boot": "enableSecureBoot",
        "enable_vtpm": "enableVtpm",
    },
)
class GoogleComputeInstanceTemplateShieldedInstanceConfig:
    def __init__(
        self,
        *,
        enable_integrity_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_secure_boot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_vtpm: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_integrity_monitoring: Compare the most recent boot measurements to the integrity policy baseline and return a pair of pass/fail results depending on whether they match or not. Defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#enable_integrity_monitoring GoogleComputeInstanceTemplate#enable_integrity_monitoring}
        :param enable_secure_boot: Verify the digital signature of all boot components, and halt the boot process if signature verification fails. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#enable_secure_boot GoogleComputeInstanceTemplate#enable_secure_boot}
        :param enable_vtpm: Use a virtualized trusted platform module, which is a specialized computer chip you can use to encrypt objects like keys and certificates. Defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#enable_vtpm GoogleComputeInstanceTemplate#enable_vtpm}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateShieldedInstanceConfig.__init__)
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
        '''Compare the most recent boot measurements to the integrity policy baseline and return a pair of pass/fail results depending on whether they match or not.

        Defaults to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#enable_integrity_monitoring GoogleComputeInstanceTemplate#enable_integrity_monitoring}
        '''
        result = self._values.get("enable_integrity_monitoring")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_secure_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Verify the digital signature of all boot components, and halt the boot process if signature verification fails.

        Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#enable_secure_boot GoogleComputeInstanceTemplate#enable_secure_boot}
        '''
        result = self._values.get("enable_secure_boot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_vtpm(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Use a virtualized trusted platform module, which is a specialized computer chip you can use to encrypt objects like keys and certificates.

        Defaults to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#enable_vtpm GoogleComputeInstanceTemplate#enable_vtpm}
        '''
        result = self._values.get("enable_vtpm")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceTemplateShieldedInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceTemplateShieldedInstanceConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateShieldedInstanceConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateShieldedInstanceConfigOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateShieldedInstanceConfigOutputReference, "enable_integrity_monitoring").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateShieldedInstanceConfigOutputReference, "enable_secure_boot").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateShieldedInstanceConfigOutputReference, "enable_vtpm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableVtpm", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInstanceTemplateShieldedInstanceConfig]:
        return typing.cast(typing.Optional[GoogleComputeInstanceTemplateShieldedInstanceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInstanceTemplateShieldedInstanceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateShieldedInstanceConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class GoogleComputeInstanceTemplateTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#create GoogleComputeInstanceTemplate#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#delete GoogleComputeInstanceTemplate#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#create GoogleComputeInstanceTemplate#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_instance_template#delete GoogleComputeInstanceTemplate#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInstanceTemplateTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInstanceTemplateTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInstanceTemplate.GoogleComputeInstanceTemplateTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInstanceTemplateTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInstanceTemplateTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInstanceTemplateTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInstanceTemplateTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInstanceTemplateTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeInstanceTemplate",
    "GoogleComputeInstanceTemplateAdvancedMachineFeatures",
    "GoogleComputeInstanceTemplateAdvancedMachineFeaturesOutputReference",
    "GoogleComputeInstanceTemplateConfidentialInstanceConfig",
    "GoogleComputeInstanceTemplateConfidentialInstanceConfigOutputReference",
    "GoogleComputeInstanceTemplateConfig",
    "GoogleComputeInstanceTemplateDisk",
    "GoogleComputeInstanceTemplateDiskDiskEncryptionKey",
    "GoogleComputeInstanceTemplateDiskDiskEncryptionKeyOutputReference",
    "GoogleComputeInstanceTemplateDiskList",
    "GoogleComputeInstanceTemplateDiskOutputReference",
    "GoogleComputeInstanceTemplateGuestAccelerator",
    "GoogleComputeInstanceTemplateGuestAcceleratorList",
    "GoogleComputeInstanceTemplateGuestAcceleratorOutputReference",
    "GoogleComputeInstanceTemplateNetworkInterface",
    "GoogleComputeInstanceTemplateNetworkInterfaceAccessConfig",
    "GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigList",
    "GoogleComputeInstanceTemplateNetworkInterfaceAccessConfigOutputReference",
    "GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRange",
    "GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeList",
    "GoogleComputeInstanceTemplateNetworkInterfaceAliasIpRangeOutputReference",
    "GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfig",
    "GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigList",
    "GoogleComputeInstanceTemplateNetworkInterfaceIpv6AccessConfigOutputReference",
    "GoogleComputeInstanceTemplateNetworkInterfaceList",
    "GoogleComputeInstanceTemplateNetworkInterfaceOutputReference",
    "GoogleComputeInstanceTemplateNetworkPerformanceConfig",
    "GoogleComputeInstanceTemplateNetworkPerformanceConfigOutputReference",
    "GoogleComputeInstanceTemplateReservationAffinity",
    "GoogleComputeInstanceTemplateReservationAffinityOutputReference",
    "GoogleComputeInstanceTemplateReservationAffinitySpecificReservation",
    "GoogleComputeInstanceTemplateReservationAffinitySpecificReservationOutputReference",
    "GoogleComputeInstanceTemplateScheduling",
    "GoogleComputeInstanceTemplateSchedulingNodeAffinities",
    "GoogleComputeInstanceTemplateSchedulingNodeAffinitiesList",
    "GoogleComputeInstanceTemplateSchedulingNodeAffinitiesOutputReference",
    "GoogleComputeInstanceTemplateSchedulingOutputReference",
    "GoogleComputeInstanceTemplateServiceAccount",
    "GoogleComputeInstanceTemplateServiceAccountOutputReference",
    "GoogleComputeInstanceTemplateShieldedInstanceConfig",
    "GoogleComputeInstanceTemplateShieldedInstanceConfigOutputReference",
    "GoogleComputeInstanceTemplateTimeouts",
    "GoogleComputeInstanceTemplateTimeoutsOutputReference",
]

publication.publish()
