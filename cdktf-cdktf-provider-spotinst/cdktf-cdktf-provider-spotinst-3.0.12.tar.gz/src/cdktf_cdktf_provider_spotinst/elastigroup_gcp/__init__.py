'''
# `spotinst_elastigroup_gcp`

Refer to the Terraform Registory for docs: [`spotinst_elastigroup_gcp`](https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp).
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


class ElastigroupGcp(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcp",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp spotinst_elastigroup_gcp}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        desired_capacity: jsii.Number,
        name: builtins.str,
        auto_healing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        backend_services: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpBackendServices", typing.Dict[str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        disk: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpDisk", typing.Dict[str, typing.Any]]]]] = None,
        draining_timeout: typing.Optional[jsii.Number] = None,
        fallback_to_ondemand: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        gpu: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpGpu", typing.Dict[str, typing.Any]]]]] = None,
        health_check_grace_period: typing.Optional[jsii.Number] = None,
        health_check_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        instance_types_custom: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpInstanceTypesCustom", typing.Dict[str, typing.Any]]]]] = None,
        instance_types_ondemand: typing.Optional[builtins.str] = None,
        instance_types_preemptible: typing.Optional[typing.Sequence[builtins.str]] = None,
        integration_docker_swarm: typing.Optional[typing.Union["ElastigroupGcpIntegrationDockerSwarm", typing.Dict[str, typing.Any]]] = None,
        integration_gke: typing.Optional[typing.Union["ElastigroupGcpIntegrationGke", typing.Dict[str, typing.Any]]] = None,
        ip_forwarding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        labels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpLabels", typing.Dict[str, typing.Any]]]]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpMetadata", typing.Dict[str, typing.Any]]]]] = None,
        min_size: typing.Optional[jsii.Number] = None,
        network_interface: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpNetworkInterface", typing.Dict[str, typing.Any]]]]] = None,
        ondemand_count: typing.Optional[jsii.Number] = None,
        preemptible_percentage: typing.Optional[jsii.Number] = None,
        provisioning_model: typing.Optional[builtins.str] = None,
        scaling_down_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpScalingDownPolicy", typing.Dict[str, typing.Any]]]]] = None,
        scaling_up_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpScalingUpPolicy", typing.Dict[str, typing.Any]]]]] = None,
        scheduled_task: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpScheduledTask", typing.Dict[str, typing.Any]]]]] = None,
        service_account: typing.Optional[builtins.str] = None,
        shutdown_script: typing.Optional[builtins.str] = None,
        startup_script: typing.Optional[builtins.str] = None,
        subnets: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpSubnets", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        unhealthy_duration: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp spotinst_elastigroup_gcp} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#desired_capacity ElastigroupGcp#desired_capacity}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#name ElastigroupGcp#name}.
        :param auto_healing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#auto_healing ElastigroupGcp#auto_healing}.
        :param availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#availability_zones ElastigroupGcp#availability_zones}.
        :param backend_services: backend_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#backend_services ElastigroupGcp#backend_services}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#description ElastigroupGcp#description}.
        :param disk: disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#disk ElastigroupGcp#disk}
        :param draining_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#draining_timeout ElastigroupGcp#draining_timeout}.
        :param fallback_to_ondemand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#fallback_to_ondemand ElastigroupGcp#fallback_to_ondemand}.
        :param gpu: gpu block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#gpu ElastigroupGcp#gpu}
        :param health_check_grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#health_check_grace_period ElastigroupGcp#health_check_grace_period}.
        :param health_check_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#health_check_type ElastigroupGcp#health_check_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#id ElastigroupGcp#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_types_custom: instance_types_custom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#instance_types_custom ElastigroupGcp#instance_types_custom}
        :param instance_types_ondemand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#instance_types_ondemand ElastigroupGcp#instance_types_ondemand}.
        :param instance_types_preemptible: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#instance_types_preemptible ElastigroupGcp#instance_types_preemptible}.
        :param integration_docker_swarm: integration_docker_swarm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#integration_docker_swarm ElastigroupGcp#integration_docker_swarm}
        :param integration_gke: integration_gke block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#integration_gke ElastigroupGcp#integration_gke}
        :param ip_forwarding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#ip_forwarding ElastigroupGcp#ip_forwarding}.
        :param labels: labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#labels ElastigroupGcp#labels}
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#max_size ElastigroupGcp#max_size}.
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#metadata ElastigroupGcp#metadata}
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#min_size ElastigroupGcp#min_size}.
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#network_interface ElastigroupGcp#network_interface}
        :param ondemand_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#ondemand_count ElastigroupGcp#ondemand_count}.
        :param preemptible_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#preemptible_percentage ElastigroupGcp#preemptible_percentage}.
        :param provisioning_model: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#provisioning_model ElastigroupGcp#provisioning_model}.
        :param scaling_down_policy: scaling_down_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#scaling_down_policy ElastigroupGcp#scaling_down_policy}
        :param scaling_up_policy: scaling_up_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#scaling_up_policy ElastigroupGcp#scaling_up_policy}
        :param scheduled_task: scheduled_task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#scheduled_task ElastigroupGcp#scheduled_task}
        :param service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#service_account ElastigroupGcp#service_account}.
        :param shutdown_script: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#shutdown_script ElastigroupGcp#shutdown_script}.
        :param startup_script: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#startup_script ElastigroupGcp#startup_script}.
        :param subnets: subnets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#subnets ElastigroupGcp#subnets}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#tags ElastigroupGcp#tags}.
        :param unhealthy_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#unhealthy_duration ElastigroupGcp#unhealthy_duration}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcp.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ElastigroupGcpConfig(
            desired_capacity=desired_capacity,
            name=name,
            auto_healing=auto_healing,
            availability_zones=availability_zones,
            backend_services=backend_services,
            description=description,
            disk=disk,
            draining_timeout=draining_timeout,
            fallback_to_ondemand=fallback_to_ondemand,
            gpu=gpu,
            health_check_grace_period=health_check_grace_period,
            health_check_type=health_check_type,
            id=id,
            instance_types_custom=instance_types_custom,
            instance_types_ondemand=instance_types_ondemand,
            instance_types_preemptible=instance_types_preemptible,
            integration_docker_swarm=integration_docker_swarm,
            integration_gke=integration_gke,
            ip_forwarding=ip_forwarding,
            labels=labels,
            max_size=max_size,
            metadata=metadata,
            min_size=min_size,
            network_interface=network_interface,
            ondemand_count=ondemand_count,
            preemptible_percentage=preemptible_percentage,
            provisioning_model=provisioning_model,
            scaling_down_policy=scaling_down_policy,
            scaling_up_policy=scaling_up_policy,
            scheduled_task=scheduled_task,
            service_account=service_account,
            shutdown_script=shutdown_script,
            startup_script=startup_script,
            subnets=subnets,
            tags=tags,
            unhealthy_duration=unhealthy_duration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBackendServices")
    def put_backend_services(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpBackendServices", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcp.put_backend_services)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBackendServices", [value]))

    @jsii.member(jsii_name="putDisk")
    def put_disk(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpDisk", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcp.put_disk)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDisk", [value]))

    @jsii.member(jsii_name="putGpu")
    def put_gpu(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpGpu", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcp.put_gpu)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGpu", [value]))

    @jsii.member(jsii_name="putInstanceTypesCustom")
    def put_instance_types_custom(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpInstanceTypesCustom", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcp.put_instance_types_custom)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInstanceTypesCustom", [value]))

    @jsii.member(jsii_name="putIntegrationDockerSwarm")
    def put_integration_docker_swarm(
        self,
        *,
        master_host: builtins.str,
        master_port: jsii.Number,
    ) -> None:
        '''
        :param master_host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#master_host ElastigroupGcp#master_host}.
        :param master_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#master_port ElastigroupGcp#master_port}.
        '''
        value = ElastigroupGcpIntegrationDockerSwarm(
            master_host=master_host, master_port=master_port
        )

        return typing.cast(None, jsii.invoke(self, "putIntegrationDockerSwarm", [value]))

    @jsii.member(jsii_name="putIntegrationGke")
    def put_integration_gke(
        self,
        *,
        autoscale_cooldown: typing.Optional[jsii.Number] = None,
        autoscale_down: typing.Optional[typing.Union["ElastigroupGcpIntegrationGkeAutoscaleDown", typing.Dict[str, typing.Any]]] = None,
        autoscale_headroom: typing.Optional[typing.Union["ElastigroupGcpIntegrationGkeAutoscaleHeadroom", typing.Dict[str, typing.Any]]] = None,
        autoscale_is_auto_config: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        autoscale_is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        autoscale_labels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpIntegrationGkeAutoscaleLabels", typing.Dict[str, typing.Any]]]]] = None,
        auto_update: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param autoscale_cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#autoscale_cooldown ElastigroupGcp#autoscale_cooldown}.
        :param autoscale_down: autoscale_down block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#autoscale_down ElastigroupGcp#autoscale_down}
        :param autoscale_headroom: autoscale_headroom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#autoscale_headroom ElastigroupGcp#autoscale_headroom}
        :param autoscale_is_auto_config: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#autoscale_is_auto_config ElastigroupGcp#autoscale_is_auto_config}.
        :param autoscale_is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#autoscale_is_enabled ElastigroupGcp#autoscale_is_enabled}.
        :param autoscale_labels: autoscale_labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#autoscale_labels ElastigroupGcp#autoscale_labels}
        :param auto_update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#auto_update ElastigroupGcp#auto_update}.
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#cluster_id ElastigroupGcp#cluster_id}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#location ElastigroupGcp#location}.
        '''
        value = ElastigroupGcpIntegrationGke(
            autoscale_cooldown=autoscale_cooldown,
            autoscale_down=autoscale_down,
            autoscale_headroom=autoscale_headroom,
            autoscale_is_auto_config=autoscale_is_auto_config,
            autoscale_is_enabled=autoscale_is_enabled,
            autoscale_labels=autoscale_labels,
            auto_update=auto_update,
            cluster_id=cluster_id,
            location=location,
        )

        return typing.cast(None, jsii.invoke(self, "putIntegrationGke", [value]))

    @jsii.member(jsii_name="putLabels")
    def put_labels(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpLabels", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcp.put_labels)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLabels", [value]))

    @jsii.member(jsii_name="putMetadata")
    def put_metadata(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpMetadata", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcp.put_metadata)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putNetworkInterface")
    def put_network_interface(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpNetworkInterface", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcp.put_network_interface)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkInterface", [value]))

    @jsii.member(jsii_name="putScalingDownPolicy")
    def put_scaling_down_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpScalingDownPolicy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcp.put_scaling_down_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScalingDownPolicy", [value]))

    @jsii.member(jsii_name="putScalingUpPolicy")
    def put_scaling_up_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpScalingUpPolicy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcp.put_scaling_up_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScalingUpPolicy", [value]))

    @jsii.member(jsii_name="putScheduledTask")
    def put_scheduled_task(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpScheduledTask", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcp.put_scheduled_task)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScheduledTask", [value]))

    @jsii.member(jsii_name="putSubnets")
    def put_subnets(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpSubnets", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcp.put_subnets)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSubnets", [value]))

    @jsii.member(jsii_name="resetAutoHealing")
    def reset_auto_healing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoHealing", []))

    @jsii.member(jsii_name="resetAvailabilityZones")
    def reset_availability_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityZones", []))

    @jsii.member(jsii_name="resetBackendServices")
    def reset_backend_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendServices", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisk")
    def reset_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisk", []))

    @jsii.member(jsii_name="resetDrainingTimeout")
    def reset_draining_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDrainingTimeout", []))

    @jsii.member(jsii_name="resetFallbackToOndemand")
    def reset_fallback_to_ondemand(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFallbackToOndemand", []))

    @jsii.member(jsii_name="resetGpu")
    def reset_gpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGpu", []))

    @jsii.member(jsii_name="resetHealthCheckGracePeriod")
    def reset_health_check_grace_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckGracePeriod", []))

    @jsii.member(jsii_name="resetHealthCheckType")
    def reset_health_check_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckType", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInstanceTypesCustom")
    def reset_instance_types_custom(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceTypesCustom", []))

    @jsii.member(jsii_name="resetInstanceTypesOndemand")
    def reset_instance_types_ondemand(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceTypesOndemand", []))

    @jsii.member(jsii_name="resetInstanceTypesPreemptible")
    def reset_instance_types_preemptible(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceTypesPreemptible", []))

    @jsii.member(jsii_name="resetIntegrationDockerSwarm")
    def reset_integration_docker_swarm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntegrationDockerSwarm", []))

    @jsii.member(jsii_name="resetIntegrationGke")
    def reset_integration_gke(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntegrationGke", []))

    @jsii.member(jsii_name="resetIpForwarding")
    def reset_ip_forwarding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpForwarding", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetMaxSize")
    def reset_max_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxSize", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetMinSize")
    def reset_min_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinSize", []))

    @jsii.member(jsii_name="resetNetworkInterface")
    def reset_network_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkInterface", []))

    @jsii.member(jsii_name="resetOndemandCount")
    def reset_ondemand_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOndemandCount", []))

    @jsii.member(jsii_name="resetPreemptiblePercentage")
    def reset_preemptible_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreemptiblePercentage", []))

    @jsii.member(jsii_name="resetProvisioningModel")
    def reset_provisioning_model(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvisioningModel", []))

    @jsii.member(jsii_name="resetScalingDownPolicy")
    def reset_scaling_down_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScalingDownPolicy", []))

    @jsii.member(jsii_name="resetScalingUpPolicy")
    def reset_scaling_up_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScalingUpPolicy", []))

    @jsii.member(jsii_name="resetScheduledTask")
    def reset_scheduled_task(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduledTask", []))

    @jsii.member(jsii_name="resetServiceAccount")
    def reset_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccount", []))

    @jsii.member(jsii_name="resetShutdownScript")
    def reset_shutdown_script(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShutdownScript", []))

    @jsii.member(jsii_name="resetStartupScript")
    def reset_startup_script(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartupScript", []))

    @jsii.member(jsii_name="resetSubnets")
    def reset_subnets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnets", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetUnhealthyDuration")
    def reset_unhealthy_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnhealthyDuration", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="backendServices")
    def backend_services(self) -> "ElastigroupGcpBackendServicesList":
        return typing.cast("ElastigroupGcpBackendServicesList", jsii.get(self, "backendServices"))

    @builtins.property
    @jsii.member(jsii_name="disk")
    def disk(self) -> "ElastigroupGcpDiskList":
        return typing.cast("ElastigroupGcpDiskList", jsii.get(self, "disk"))

    @builtins.property
    @jsii.member(jsii_name="gpu")
    def gpu(self) -> "ElastigroupGcpGpuList":
        return typing.cast("ElastigroupGcpGpuList", jsii.get(self, "gpu"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypesCustom")
    def instance_types_custom(self) -> "ElastigroupGcpInstanceTypesCustomList":
        return typing.cast("ElastigroupGcpInstanceTypesCustomList", jsii.get(self, "instanceTypesCustom"))

    @builtins.property
    @jsii.member(jsii_name="integrationDockerSwarm")
    def integration_docker_swarm(
        self,
    ) -> "ElastigroupGcpIntegrationDockerSwarmOutputReference":
        return typing.cast("ElastigroupGcpIntegrationDockerSwarmOutputReference", jsii.get(self, "integrationDockerSwarm"))

    @builtins.property
    @jsii.member(jsii_name="integrationGke")
    def integration_gke(self) -> "ElastigroupGcpIntegrationGkeOutputReference":
        return typing.cast("ElastigroupGcpIntegrationGkeOutputReference", jsii.get(self, "integrationGke"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> "ElastigroupGcpLabelsList":
        return typing.cast("ElastigroupGcpLabelsList", jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "ElastigroupGcpMetadataList":
        return typing.cast("ElastigroupGcpMetadataList", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="networkInterface")
    def network_interface(self) -> "ElastigroupGcpNetworkInterfaceList":
        return typing.cast("ElastigroupGcpNetworkInterfaceList", jsii.get(self, "networkInterface"))

    @builtins.property
    @jsii.member(jsii_name="scalingDownPolicy")
    def scaling_down_policy(self) -> "ElastigroupGcpScalingDownPolicyList":
        return typing.cast("ElastigroupGcpScalingDownPolicyList", jsii.get(self, "scalingDownPolicy"))

    @builtins.property
    @jsii.member(jsii_name="scalingUpPolicy")
    def scaling_up_policy(self) -> "ElastigroupGcpScalingUpPolicyList":
        return typing.cast("ElastigroupGcpScalingUpPolicyList", jsii.get(self, "scalingUpPolicy"))

    @builtins.property
    @jsii.member(jsii_name="scheduledTask")
    def scheduled_task(self) -> "ElastigroupGcpScheduledTaskList":
        return typing.cast("ElastigroupGcpScheduledTaskList", jsii.get(self, "scheduledTask"))

    @builtins.property
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> "ElastigroupGcpSubnetsList":
        return typing.cast("ElastigroupGcpSubnetsList", jsii.get(self, "subnets"))

    @builtins.property
    @jsii.member(jsii_name="autoHealingInput")
    def auto_healing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoHealingInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZonesInput")
    def availability_zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "availabilityZonesInput"))

    @builtins.property
    @jsii.member(jsii_name="backendServicesInput")
    def backend_services_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpBackendServices"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpBackendServices"]]], jsii.get(self, "backendServicesInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredCapacityInput")
    def desired_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "desiredCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="diskInput")
    def disk_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpDisk"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpDisk"]]], jsii.get(self, "diskInput"))

    @builtins.property
    @jsii.member(jsii_name="drainingTimeoutInput")
    def draining_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "drainingTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="fallbackToOndemandInput")
    def fallback_to_ondemand_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fallbackToOndemandInput"))

    @builtins.property
    @jsii.member(jsii_name="gpuInput")
    def gpu_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpGpu"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpGpu"]]], jsii.get(self, "gpuInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckGracePeriodInput")
    def health_check_grace_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthCheckGracePeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckTypeInput")
    def health_check_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypesCustomInput")
    def instance_types_custom_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpInstanceTypesCustom"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpInstanceTypesCustom"]]], jsii.get(self, "instanceTypesCustomInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypesOndemandInput")
    def instance_types_ondemand_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypesOndemandInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypesPreemptibleInput")
    def instance_types_preemptible_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instanceTypesPreemptibleInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationDockerSwarmInput")
    def integration_docker_swarm_input(
        self,
    ) -> typing.Optional["ElastigroupGcpIntegrationDockerSwarm"]:
        return typing.cast(typing.Optional["ElastigroupGcpIntegrationDockerSwarm"], jsii.get(self, "integrationDockerSwarmInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationGkeInput")
    def integration_gke_input(self) -> typing.Optional["ElastigroupGcpIntegrationGke"]:
        return typing.cast(typing.Optional["ElastigroupGcpIntegrationGke"], jsii.get(self, "integrationGkeInput"))

    @builtins.property
    @jsii.member(jsii_name="ipForwardingInput")
    def ip_forwarding_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ipForwardingInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpLabels"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpLabels"]]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSizeInput")
    def max_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpMetadata"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpMetadata"]]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="minSizeInput")
    def min_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceInput")
    def network_interface_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpNetworkInterface"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpNetworkInterface"]]], jsii.get(self, "networkInterfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="ondemandCountInput")
    def ondemand_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ondemandCountInput"))

    @builtins.property
    @jsii.member(jsii_name="preemptiblePercentageInput")
    def preemptible_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "preemptiblePercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="provisioningModelInput")
    def provisioning_model_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "provisioningModelInput"))

    @builtins.property
    @jsii.member(jsii_name="scalingDownPolicyInput")
    def scaling_down_policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpScalingDownPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpScalingDownPolicy"]]], jsii.get(self, "scalingDownPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="scalingUpPolicyInput")
    def scaling_up_policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpScalingUpPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpScalingUpPolicy"]]], jsii.get(self, "scalingUpPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduledTaskInput")
    def scheduled_task_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpScheduledTask"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpScheduledTask"]]], jsii.get(self, "scheduledTaskInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountInput")
    def service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="shutdownScriptInput")
    def shutdown_script_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shutdownScriptInput"))

    @builtins.property
    @jsii.member(jsii_name="startupScriptInput")
    def startup_script_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startupScriptInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetsInput")
    def subnets_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpSubnets"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpSubnets"]]], jsii.get(self, "subnetsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="unhealthyDurationInput")
    def unhealthy_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "unhealthyDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="autoHealing")
    def auto_healing(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoHealing"))

    @auto_healing.setter
    def auto_healing(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "auto_healing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoHealing", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "availabilityZones"))

    @availability_zones.setter
    def availability_zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "availability_zones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZones", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="desiredCapacity")
    def desired_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredCapacity"))

    @desired_capacity.setter
    def desired_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "desired_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="drainingTimeout")
    def draining_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "drainingTimeout"))

    @draining_timeout.setter
    def draining_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "draining_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "drainingTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="fallbackToOndemand")
    def fallback_to_ondemand(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fallbackToOndemand"))

    @fallback_to_ondemand.setter
    def fallback_to_ondemand(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "fallback_to_ondemand").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fallbackToOndemand", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckGracePeriod")
    def health_check_grace_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthCheckGracePeriod"))

    @health_check_grace_period.setter
    def health_check_grace_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "health_check_grace_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckGracePeriod", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckType")
    def health_check_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckType"))

    @health_check_type.setter
    def health_check_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "health_check_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instanceTypesOndemand")
    def instance_types_ondemand(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceTypesOndemand"))

    @instance_types_ondemand.setter
    def instance_types_ondemand(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "instance_types_ondemand").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceTypesOndemand", value)

    @builtins.property
    @jsii.member(jsii_name="instanceTypesPreemptible")
    def instance_types_preemptible(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceTypesPreemptible"))

    @instance_types_preemptible.setter
    def instance_types_preemptible(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "instance_types_preemptible").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceTypesPreemptible", value)

    @builtins.property
    @jsii.member(jsii_name="ipForwarding")
    def ip_forwarding(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ipForwarding"))

    @ip_forwarding.setter
    def ip_forwarding(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "ip_forwarding").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipForwarding", value)

    @builtins.property
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSize"))

    @max_size.setter
    def max_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "max_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSize", value)

    @builtins.property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minSize"))

    @min_size.setter
    def min_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "min_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minSize", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ondemandCount")
    def ondemand_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ondemandCount"))

    @ondemand_count.setter
    def ondemand_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "ondemand_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ondemandCount", value)

    @builtins.property
    @jsii.member(jsii_name="preemptiblePercentage")
    def preemptible_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "preemptiblePercentage"))

    @preemptible_percentage.setter
    def preemptible_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "preemptible_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preemptiblePercentage", value)

    @builtins.property
    @jsii.member(jsii_name="provisioningModel")
    def provisioning_model(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "provisioningModel"))

    @provisioning_model.setter
    def provisioning_model(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "provisioning_model").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisioningModel", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccount"))

    @service_account.setter
    def service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "service_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="shutdownScript")
    def shutdown_script(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shutdownScript"))

    @shutdown_script.setter
    def shutdown_script(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "shutdown_script").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shutdownScript", value)

    @builtins.property
    @jsii.member(jsii_name="startupScript")
    def startup_script(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startupScript"))

    @startup_script.setter
    def startup_script(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "startup_script").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startupScript", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="unhealthyDuration")
    def unhealthy_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unhealthyDuration"))

    @unhealthy_duration.setter
    def unhealthy_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcp, "unhealthy_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unhealthyDuration", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpBackendServices",
    jsii_struct_bases=[],
    name_mapping={
        "service_name": "serviceName",
        "location_type": "locationType",
        "named_ports": "namedPorts",
        "scheme": "scheme",
    },
)
class ElastigroupGcpBackendServices:
    def __init__(
        self,
        *,
        service_name: builtins.str,
        location_type: typing.Optional[builtins.str] = None,
        named_ports: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpBackendServicesNamedPorts", typing.Dict[str, typing.Any]]]]] = None,
        scheme: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#service_name ElastigroupGcp#service_name}.
        :param location_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#location_type ElastigroupGcp#location_type}.
        :param named_ports: named_ports block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#named_ports ElastigroupGcp#named_ports}
        :param scheme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#scheme ElastigroupGcp#scheme}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpBackendServices.__init__)
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument location_type", value=location_type, expected_type=type_hints["location_type"])
            check_type(argname="argument named_ports", value=named_ports, expected_type=type_hints["named_ports"])
            check_type(argname="argument scheme", value=scheme, expected_type=type_hints["scheme"])
        self._values: typing.Dict[str, typing.Any] = {
            "service_name": service_name,
        }
        if location_type is not None:
            self._values["location_type"] = location_type
        if named_ports is not None:
            self._values["named_ports"] = named_ports
        if scheme is not None:
            self._values["scheme"] = scheme

    @builtins.property
    def service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#service_name ElastigroupGcp#service_name}.'''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#location_type ElastigroupGcp#location_type}.'''
        result = self._values.get("location_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def named_ports(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpBackendServicesNamedPorts"]]]:
        '''named_ports block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#named_ports ElastigroupGcp#named_ports}
        '''
        result = self._values.get("named_ports")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpBackendServicesNamedPorts"]]], result)

    @builtins.property
    def scheme(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#scheme ElastigroupGcp#scheme}.'''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpBackendServices(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupGcpBackendServicesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpBackendServicesList",
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
            type_hints = typing.get_type_hints(ElastigroupGcpBackendServicesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ElastigroupGcpBackendServicesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpBackendServicesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupGcpBackendServicesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpBackendServicesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpBackendServicesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpBackendServicesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpBackendServices]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpBackendServices]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpBackendServices]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpBackendServicesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpBackendServicesNamedPorts",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "ports": "ports"},
)
class ElastigroupGcpBackendServicesNamedPorts:
    def __init__(
        self,
        *,
        name: builtins.str,
        ports: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#name ElastigroupGcp#name}.
        :param ports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#ports ElastigroupGcp#ports}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpBackendServicesNamedPorts.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "ports": ports,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#name ElastigroupGcp#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ports(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#ports ElastigroupGcp#ports}.'''
        result = self._values.get("ports")
        assert result is not None, "Required property 'ports' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpBackendServicesNamedPorts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupGcpBackendServicesNamedPortsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpBackendServicesNamedPortsList",
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
            type_hints = typing.get_type_hints(ElastigroupGcpBackendServicesNamedPortsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupGcpBackendServicesNamedPortsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpBackendServicesNamedPortsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupGcpBackendServicesNamedPortsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpBackendServicesNamedPortsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpBackendServicesNamedPortsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpBackendServicesNamedPortsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpBackendServicesNamedPorts]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpBackendServicesNamedPorts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpBackendServicesNamedPorts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpBackendServicesNamedPortsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpBackendServicesNamedPortsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpBackendServicesNamedPortsOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpBackendServicesNamedPortsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="portsInput")
    def ports_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "portsInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpBackendServicesNamedPortsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ports"))

    @ports.setter
    def ports(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpBackendServicesNamedPortsOutputReference, "ports").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ports", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupGcpBackendServicesNamedPorts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupGcpBackendServicesNamedPorts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupGcpBackendServicesNamedPorts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpBackendServicesNamedPortsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpBackendServicesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpBackendServicesOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpBackendServicesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNamedPorts")
    def put_named_ports(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastigroupGcpBackendServicesNamedPorts, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpBackendServicesOutputReference.put_named_ports)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNamedPorts", [value]))

    @jsii.member(jsii_name="resetLocationType")
    def reset_location_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocationType", []))

    @jsii.member(jsii_name="resetNamedPorts")
    def reset_named_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamedPorts", []))

    @jsii.member(jsii_name="resetScheme")
    def reset_scheme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheme", []))

    @builtins.property
    @jsii.member(jsii_name="namedPorts")
    def named_ports(self) -> ElastigroupGcpBackendServicesNamedPortsList:
        return typing.cast(ElastigroupGcpBackendServicesNamedPortsList, jsii.get(self, "namedPorts"))

    @builtins.property
    @jsii.member(jsii_name="locationTypeInput")
    def location_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="namedPortsInput")
    def named_ports_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpBackendServicesNamedPorts]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpBackendServicesNamedPorts]]], jsii.get(self, "namedPortsInput"))

    @builtins.property
    @jsii.member(jsii_name="schemeInput")
    def scheme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemeInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="locationType")
    def location_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locationType"))

    @location_type.setter
    def location_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpBackendServicesOutputReference, "location_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationType", value)

    @builtins.property
    @jsii.member(jsii_name="scheme")
    def scheme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheme"))

    @scheme.setter
    def scheme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpBackendServicesOutputReference, "scheme").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheme", value)

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpBackendServicesOutputReference, "service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupGcpBackendServices, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupGcpBackendServices, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupGcpBackendServices, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpBackendServicesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "desired_capacity": "desiredCapacity",
        "name": "name",
        "auto_healing": "autoHealing",
        "availability_zones": "availabilityZones",
        "backend_services": "backendServices",
        "description": "description",
        "disk": "disk",
        "draining_timeout": "drainingTimeout",
        "fallback_to_ondemand": "fallbackToOndemand",
        "gpu": "gpu",
        "health_check_grace_period": "healthCheckGracePeriod",
        "health_check_type": "healthCheckType",
        "id": "id",
        "instance_types_custom": "instanceTypesCustom",
        "instance_types_ondemand": "instanceTypesOndemand",
        "instance_types_preemptible": "instanceTypesPreemptible",
        "integration_docker_swarm": "integrationDockerSwarm",
        "integration_gke": "integrationGke",
        "ip_forwarding": "ipForwarding",
        "labels": "labels",
        "max_size": "maxSize",
        "metadata": "metadata",
        "min_size": "minSize",
        "network_interface": "networkInterface",
        "ondemand_count": "ondemandCount",
        "preemptible_percentage": "preemptiblePercentage",
        "provisioning_model": "provisioningModel",
        "scaling_down_policy": "scalingDownPolicy",
        "scaling_up_policy": "scalingUpPolicy",
        "scheduled_task": "scheduledTask",
        "service_account": "serviceAccount",
        "shutdown_script": "shutdownScript",
        "startup_script": "startupScript",
        "subnets": "subnets",
        "tags": "tags",
        "unhealthy_duration": "unhealthyDuration",
    },
)
class ElastigroupGcpConfig(cdktf.TerraformMetaArguments):
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
        desired_capacity: jsii.Number,
        name: builtins.str,
        auto_healing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        backend_services: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastigroupGcpBackendServices, typing.Dict[str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        disk: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpDisk", typing.Dict[str, typing.Any]]]]] = None,
        draining_timeout: typing.Optional[jsii.Number] = None,
        fallback_to_ondemand: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        gpu: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpGpu", typing.Dict[str, typing.Any]]]]] = None,
        health_check_grace_period: typing.Optional[jsii.Number] = None,
        health_check_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        instance_types_custom: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpInstanceTypesCustom", typing.Dict[str, typing.Any]]]]] = None,
        instance_types_ondemand: typing.Optional[builtins.str] = None,
        instance_types_preemptible: typing.Optional[typing.Sequence[builtins.str]] = None,
        integration_docker_swarm: typing.Optional[typing.Union["ElastigroupGcpIntegrationDockerSwarm", typing.Dict[str, typing.Any]]] = None,
        integration_gke: typing.Optional[typing.Union["ElastigroupGcpIntegrationGke", typing.Dict[str, typing.Any]]] = None,
        ip_forwarding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        labels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpLabels", typing.Dict[str, typing.Any]]]]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpMetadata", typing.Dict[str, typing.Any]]]]] = None,
        min_size: typing.Optional[jsii.Number] = None,
        network_interface: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpNetworkInterface", typing.Dict[str, typing.Any]]]]] = None,
        ondemand_count: typing.Optional[jsii.Number] = None,
        preemptible_percentage: typing.Optional[jsii.Number] = None,
        provisioning_model: typing.Optional[builtins.str] = None,
        scaling_down_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpScalingDownPolicy", typing.Dict[str, typing.Any]]]]] = None,
        scaling_up_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpScalingUpPolicy", typing.Dict[str, typing.Any]]]]] = None,
        scheduled_task: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpScheduledTask", typing.Dict[str, typing.Any]]]]] = None,
        service_account: typing.Optional[builtins.str] = None,
        shutdown_script: typing.Optional[builtins.str] = None,
        startup_script: typing.Optional[builtins.str] = None,
        subnets: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpSubnets", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        unhealthy_duration: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#desired_capacity ElastigroupGcp#desired_capacity}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#name ElastigroupGcp#name}.
        :param auto_healing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#auto_healing ElastigroupGcp#auto_healing}.
        :param availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#availability_zones ElastigroupGcp#availability_zones}.
        :param backend_services: backend_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#backend_services ElastigroupGcp#backend_services}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#description ElastigroupGcp#description}.
        :param disk: disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#disk ElastigroupGcp#disk}
        :param draining_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#draining_timeout ElastigroupGcp#draining_timeout}.
        :param fallback_to_ondemand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#fallback_to_ondemand ElastigroupGcp#fallback_to_ondemand}.
        :param gpu: gpu block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#gpu ElastigroupGcp#gpu}
        :param health_check_grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#health_check_grace_period ElastigroupGcp#health_check_grace_period}.
        :param health_check_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#health_check_type ElastigroupGcp#health_check_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#id ElastigroupGcp#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_types_custom: instance_types_custom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#instance_types_custom ElastigroupGcp#instance_types_custom}
        :param instance_types_ondemand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#instance_types_ondemand ElastigroupGcp#instance_types_ondemand}.
        :param instance_types_preemptible: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#instance_types_preemptible ElastigroupGcp#instance_types_preemptible}.
        :param integration_docker_swarm: integration_docker_swarm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#integration_docker_swarm ElastigroupGcp#integration_docker_swarm}
        :param integration_gke: integration_gke block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#integration_gke ElastigroupGcp#integration_gke}
        :param ip_forwarding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#ip_forwarding ElastigroupGcp#ip_forwarding}.
        :param labels: labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#labels ElastigroupGcp#labels}
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#max_size ElastigroupGcp#max_size}.
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#metadata ElastigroupGcp#metadata}
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#min_size ElastigroupGcp#min_size}.
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#network_interface ElastigroupGcp#network_interface}
        :param ondemand_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#ondemand_count ElastigroupGcp#ondemand_count}.
        :param preemptible_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#preemptible_percentage ElastigroupGcp#preemptible_percentage}.
        :param provisioning_model: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#provisioning_model ElastigroupGcp#provisioning_model}.
        :param scaling_down_policy: scaling_down_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#scaling_down_policy ElastigroupGcp#scaling_down_policy}
        :param scaling_up_policy: scaling_up_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#scaling_up_policy ElastigroupGcp#scaling_up_policy}
        :param scheduled_task: scheduled_task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#scheduled_task ElastigroupGcp#scheduled_task}
        :param service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#service_account ElastigroupGcp#service_account}.
        :param shutdown_script: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#shutdown_script ElastigroupGcp#shutdown_script}.
        :param startup_script: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#startup_script ElastigroupGcp#startup_script}.
        :param subnets: subnets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#subnets ElastigroupGcp#subnets}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#tags ElastigroupGcp#tags}.
        :param unhealthy_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#unhealthy_duration ElastigroupGcp#unhealthy_duration}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(integration_docker_swarm, dict):
            integration_docker_swarm = ElastigroupGcpIntegrationDockerSwarm(**integration_docker_swarm)
        if isinstance(integration_gke, dict):
            integration_gke = ElastigroupGcpIntegrationGke(**integration_gke)
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument desired_capacity", value=desired_capacity, expected_type=type_hints["desired_capacity"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument auto_healing", value=auto_healing, expected_type=type_hints["auto_healing"])
            check_type(argname="argument availability_zones", value=availability_zones, expected_type=type_hints["availability_zones"])
            check_type(argname="argument backend_services", value=backend_services, expected_type=type_hints["backend_services"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disk", value=disk, expected_type=type_hints["disk"])
            check_type(argname="argument draining_timeout", value=draining_timeout, expected_type=type_hints["draining_timeout"])
            check_type(argname="argument fallback_to_ondemand", value=fallback_to_ondemand, expected_type=type_hints["fallback_to_ondemand"])
            check_type(argname="argument gpu", value=gpu, expected_type=type_hints["gpu"])
            check_type(argname="argument health_check_grace_period", value=health_check_grace_period, expected_type=type_hints["health_check_grace_period"])
            check_type(argname="argument health_check_type", value=health_check_type, expected_type=type_hints["health_check_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instance_types_custom", value=instance_types_custom, expected_type=type_hints["instance_types_custom"])
            check_type(argname="argument instance_types_ondemand", value=instance_types_ondemand, expected_type=type_hints["instance_types_ondemand"])
            check_type(argname="argument instance_types_preemptible", value=instance_types_preemptible, expected_type=type_hints["instance_types_preemptible"])
            check_type(argname="argument integration_docker_swarm", value=integration_docker_swarm, expected_type=type_hints["integration_docker_swarm"])
            check_type(argname="argument integration_gke", value=integration_gke, expected_type=type_hints["integration_gke"])
            check_type(argname="argument ip_forwarding", value=ip_forwarding, expected_type=type_hints["ip_forwarding"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            check_type(argname="argument network_interface", value=network_interface, expected_type=type_hints["network_interface"])
            check_type(argname="argument ondemand_count", value=ondemand_count, expected_type=type_hints["ondemand_count"])
            check_type(argname="argument preemptible_percentage", value=preemptible_percentage, expected_type=type_hints["preemptible_percentage"])
            check_type(argname="argument provisioning_model", value=provisioning_model, expected_type=type_hints["provisioning_model"])
            check_type(argname="argument scaling_down_policy", value=scaling_down_policy, expected_type=type_hints["scaling_down_policy"])
            check_type(argname="argument scaling_up_policy", value=scaling_up_policy, expected_type=type_hints["scaling_up_policy"])
            check_type(argname="argument scheduled_task", value=scheduled_task, expected_type=type_hints["scheduled_task"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument shutdown_script", value=shutdown_script, expected_type=type_hints["shutdown_script"])
            check_type(argname="argument startup_script", value=startup_script, expected_type=type_hints["startup_script"])
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument unhealthy_duration", value=unhealthy_duration, expected_type=type_hints["unhealthy_duration"])
        self._values: typing.Dict[str, typing.Any] = {
            "desired_capacity": desired_capacity,
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
        if auto_healing is not None:
            self._values["auto_healing"] = auto_healing
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if backend_services is not None:
            self._values["backend_services"] = backend_services
        if description is not None:
            self._values["description"] = description
        if disk is not None:
            self._values["disk"] = disk
        if draining_timeout is not None:
            self._values["draining_timeout"] = draining_timeout
        if fallback_to_ondemand is not None:
            self._values["fallback_to_ondemand"] = fallback_to_ondemand
        if gpu is not None:
            self._values["gpu"] = gpu
        if health_check_grace_period is not None:
            self._values["health_check_grace_period"] = health_check_grace_period
        if health_check_type is not None:
            self._values["health_check_type"] = health_check_type
        if id is not None:
            self._values["id"] = id
        if instance_types_custom is not None:
            self._values["instance_types_custom"] = instance_types_custom
        if instance_types_ondemand is not None:
            self._values["instance_types_ondemand"] = instance_types_ondemand
        if instance_types_preemptible is not None:
            self._values["instance_types_preemptible"] = instance_types_preemptible
        if integration_docker_swarm is not None:
            self._values["integration_docker_swarm"] = integration_docker_swarm
        if integration_gke is not None:
            self._values["integration_gke"] = integration_gke
        if ip_forwarding is not None:
            self._values["ip_forwarding"] = ip_forwarding
        if labels is not None:
            self._values["labels"] = labels
        if max_size is not None:
            self._values["max_size"] = max_size
        if metadata is not None:
            self._values["metadata"] = metadata
        if min_size is not None:
            self._values["min_size"] = min_size
        if network_interface is not None:
            self._values["network_interface"] = network_interface
        if ondemand_count is not None:
            self._values["ondemand_count"] = ondemand_count
        if preemptible_percentage is not None:
            self._values["preemptible_percentage"] = preemptible_percentage
        if provisioning_model is not None:
            self._values["provisioning_model"] = provisioning_model
        if scaling_down_policy is not None:
            self._values["scaling_down_policy"] = scaling_down_policy
        if scaling_up_policy is not None:
            self._values["scaling_up_policy"] = scaling_up_policy
        if scheduled_task is not None:
            self._values["scheduled_task"] = scheduled_task
        if service_account is not None:
            self._values["service_account"] = service_account
        if shutdown_script is not None:
            self._values["shutdown_script"] = shutdown_script
        if startup_script is not None:
            self._values["startup_script"] = startup_script
        if subnets is not None:
            self._values["subnets"] = subnets
        if tags is not None:
            self._values["tags"] = tags
        if unhealthy_duration is not None:
            self._values["unhealthy_duration"] = unhealthy_duration

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
    def desired_capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#desired_capacity ElastigroupGcp#desired_capacity}.'''
        result = self._values.get("desired_capacity")
        assert result is not None, "Required property 'desired_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#name ElastigroupGcp#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_healing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#auto_healing ElastigroupGcp#auto_healing}.'''
        result = self._values.get("auto_healing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#availability_zones ElastigroupGcp#availability_zones}.'''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def backend_services(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpBackendServices]]]:
        '''backend_services block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#backend_services ElastigroupGcp#backend_services}
        '''
        result = self._values.get("backend_services")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpBackendServices]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#description ElastigroupGcp#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpDisk"]]]:
        '''disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#disk ElastigroupGcp#disk}
        '''
        result = self._values.get("disk")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpDisk"]]], result)

    @builtins.property
    def draining_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#draining_timeout ElastigroupGcp#draining_timeout}.'''
        result = self._values.get("draining_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def fallback_to_ondemand(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#fallback_to_ondemand ElastigroupGcp#fallback_to_ondemand}.'''
        result = self._values.get("fallback_to_ondemand")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def gpu(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpGpu"]]]:
        '''gpu block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#gpu ElastigroupGcp#gpu}
        '''
        result = self._values.get("gpu")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpGpu"]]], result)

    @builtins.property
    def health_check_grace_period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#health_check_grace_period ElastigroupGcp#health_check_grace_period}.'''
        result = self._values.get("health_check_grace_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#health_check_type ElastigroupGcp#health_check_type}.'''
        result = self._values.get("health_check_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#id ElastigroupGcp#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_types_custom(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpInstanceTypesCustom"]]]:
        '''instance_types_custom block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#instance_types_custom ElastigroupGcp#instance_types_custom}
        '''
        result = self._values.get("instance_types_custom")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpInstanceTypesCustom"]]], result)

    @builtins.property
    def instance_types_ondemand(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#instance_types_ondemand ElastigroupGcp#instance_types_ondemand}.'''
        result = self._values.get("instance_types_ondemand")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_types_preemptible(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#instance_types_preemptible ElastigroupGcp#instance_types_preemptible}.'''
        result = self._values.get("instance_types_preemptible")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def integration_docker_swarm(
        self,
    ) -> typing.Optional["ElastigroupGcpIntegrationDockerSwarm"]:
        '''integration_docker_swarm block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#integration_docker_swarm ElastigroupGcp#integration_docker_swarm}
        '''
        result = self._values.get("integration_docker_swarm")
        return typing.cast(typing.Optional["ElastigroupGcpIntegrationDockerSwarm"], result)

    @builtins.property
    def integration_gke(self) -> typing.Optional["ElastigroupGcpIntegrationGke"]:
        '''integration_gke block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#integration_gke ElastigroupGcp#integration_gke}
        '''
        result = self._values.get("integration_gke")
        return typing.cast(typing.Optional["ElastigroupGcpIntegrationGke"], result)

    @builtins.property
    def ip_forwarding(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#ip_forwarding ElastigroupGcp#ip_forwarding}.'''
        result = self._values.get("ip_forwarding")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def labels(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpLabels"]]]:
        '''labels block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#labels ElastigroupGcp#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpLabels"]]], result)

    @builtins.property
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#max_size ElastigroupGcp#max_size}.'''
        result = self._values.get("max_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metadata(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpMetadata"]]]:
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#metadata ElastigroupGcp#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpMetadata"]]], result)

    @builtins.property
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#min_size ElastigroupGcp#min_size}.'''
        result = self._values.get("min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def network_interface(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpNetworkInterface"]]]:
        '''network_interface block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#network_interface ElastigroupGcp#network_interface}
        '''
        result = self._values.get("network_interface")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpNetworkInterface"]]], result)

    @builtins.property
    def ondemand_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#ondemand_count ElastigroupGcp#ondemand_count}.'''
        result = self._values.get("ondemand_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preemptible_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#preemptible_percentage ElastigroupGcp#preemptible_percentage}.'''
        result = self._values.get("preemptible_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def provisioning_model(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#provisioning_model ElastigroupGcp#provisioning_model}.'''
        result = self._values.get("provisioning_model")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scaling_down_policy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpScalingDownPolicy"]]]:
        '''scaling_down_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#scaling_down_policy ElastigroupGcp#scaling_down_policy}
        '''
        result = self._values.get("scaling_down_policy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpScalingDownPolicy"]]], result)

    @builtins.property
    def scaling_up_policy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpScalingUpPolicy"]]]:
        '''scaling_up_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#scaling_up_policy ElastigroupGcp#scaling_up_policy}
        '''
        result = self._values.get("scaling_up_policy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpScalingUpPolicy"]]], result)

    @builtins.property
    def scheduled_task(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpScheduledTask"]]]:
        '''scheduled_task block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#scheduled_task ElastigroupGcp#scheduled_task}
        '''
        result = self._values.get("scheduled_task")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpScheduledTask"]]], result)

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#service_account ElastigroupGcp#service_account}.'''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shutdown_script(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#shutdown_script ElastigroupGcp#shutdown_script}.'''
        result = self._values.get("shutdown_script")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def startup_script(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#startup_script ElastigroupGcp#startup_script}.'''
        result = self._values.get("startup_script")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnets(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpSubnets"]]]:
        '''subnets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#subnets ElastigroupGcp#subnets}
        '''
        result = self._values.get("subnets")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpSubnets"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#tags ElastigroupGcp#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def unhealthy_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#unhealthy_duration ElastigroupGcp#unhealthy_duration}.'''
        result = self._values.get("unhealthy_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpDisk",
    jsii_struct_bases=[],
    name_mapping={
        "auto_delete": "autoDelete",
        "boot": "boot",
        "device_name": "deviceName",
        "initialize_params": "initializeParams",
        "interface": "interface",
        "mode": "mode",
        "source": "source",
        "type": "type",
    },
)
class ElastigroupGcpDisk:
    def __init__(
        self,
        *,
        auto_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        boot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        device_name: typing.Optional[builtins.str] = None,
        initialize_params: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpDiskInitializeParams", typing.Dict[str, typing.Any]]]]] = None,
        interface: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#auto_delete ElastigroupGcp#auto_delete}.
        :param boot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#boot ElastigroupGcp#boot}.
        :param device_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#device_name ElastigroupGcp#device_name}.
        :param initialize_params: initialize_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#initialize_params ElastigroupGcp#initialize_params}
        :param interface: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#interface ElastigroupGcp#interface}.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#mode ElastigroupGcp#mode}.
        :param source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#source ElastigroupGcp#source}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#type ElastigroupGcp#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpDisk.__init__)
            check_type(argname="argument auto_delete", value=auto_delete, expected_type=type_hints["auto_delete"])
            check_type(argname="argument boot", value=boot, expected_type=type_hints["boot"])
            check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
            check_type(argname="argument initialize_params", value=initialize_params, expected_type=type_hints["initialize_params"])
            check_type(argname="argument interface", value=interface, expected_type=type_hints["interface"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_delete is not None:
            self._values["auto_delete"] = auto_delete
        if boot is not None:
            self._values["boot"] = boot
        if device_name is not None:
            self._values["device_name"] = device_name
        if initialize_params is not None:
            self._values["initialize_params"] = initialize_params
        if interface is not None:
            self._values["interface"] = interface
        if mode is not None:
            self._values["mode"] = mode
        if source is not None:
            self._values["source"] = source
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def auto_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#auto_delete ElastigroupGcp#auto_delete}.'''
        result = self._values.get("auto_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def boot(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#boot ElastigroupGcp#boot}.'''
        result = self._values.get("boot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def device_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#device_name ElastigroupGcp#device_name}.'''
        result = self._values.get("device_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initialize_params(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpDiskInitializeParams"]]]:
        '''initialize_params block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#initialize_params ElastigroupGcp#initialize_params}
        '''
        result = self._values.get("initialize_params")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpDiskInitializeParams"]]], result)

    @builtins.property
    def interface(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#interface ElastigroupGcp#interface}.'''
        result = self._values.get("interface")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#mode ElastigroupGcp#mode}.'''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#source ElastigroupGcp#source}.'''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#type ElastigroupGcp#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpDiskInitializeParams",
    jsii_struct_bases=[],
    name_mapping={
        "source_image": "sourceImage",
        "disk_size_gb": "diskSizeGb",
        "disk_type": "diskType",
    },
)
class ElastigroupGcpDiskInitializeParams:
    def __init__(
        self,
        *,
        source_image: builtins.str,
        disk_size_gb: typing.Optional[builtins.str] = None,
        disk_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source_image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#source_image ElastigroupGcp#source_image}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#disk_size_gb ElastigroupGcp#disk_size_gb}.
        :param disk_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#disk_type ElastigroupGcp#disk_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpDiskInitializeParams.__init__)
            check_type(argname="argument source_image", value=source_image, expected_type=type_hints["source_image"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument disk_type", value=disk_type, expected_type=type_hints["disk_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "source_image": source_image,
        }
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if disk_type is not None:
            self._values["disk_type"] = disk_type

    @builtins.property
    def source_image(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#source_image ElastigroupGcp#source_image}.'''
        result = self._values.get("source_image")
        assert result is not None, "Required property 'source_image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#disk_size_gb ElastigroupGcp#disk_size_gb}.'''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#disk_type ElastigroupGcp#disk_type}.'''
        result = self._values.get("disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpDiskInitializeParams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupGcpDiskInitializeParamsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpDiskInitializeParamsList",
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
            type_hints = typing.get_type_hints(ElastigroupGcpDiskInitializeParamsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupGcpDiskInitializeParamsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpDiskInitializeParamsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupGcpDiskInitializeParamsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskInitializeParamsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskInitializeParamsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskInitializeParamsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpDiskInitializeParams]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpDiskInitializeParams]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpDiskInitializeParams]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskInitializeParamsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpDiskInitializeParamsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpDiskInitializeParamsOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpDiskInitializeParamsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDiskSizeGb")
    def reset_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSizeGb", []))

    @jsii.member(jsii_name="resetDiskType")
    def reset_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskType", []))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="diskTypeInput")
    def disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceImageInput")
    def source_image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceImageInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskInitializeParamsOutputReference, "disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="diskType")
    def disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskType"))

    @disk_type.setter
    def disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskInitializeParamsOutputReference, "disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskType", value)

    @builtins.property
    @jsii.member(jsii_name="sourceImage")
    def source_image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceImage"))

    @source_image.setter
    def source_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskInitializeParamsOutputReference, "source_image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceImage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupGcpDiskInitializeParams, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupGcpDiskInitializeParams, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupGcpDiskInitializeParams, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskInitializeParamsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpDiskList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpDiskList",
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
            type_hints = typing.get_type_hints(ElastigroupGcpDiskList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ElastigroupGcpDiskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpDiskList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupGcpDiskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpDisk]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpDisk]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpDisk]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpDiskOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putInitializeParams")
    def put_initialize_params(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastigroupGcpDiskInitializeParams, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpDiskOutputReference.put_initialize_params)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInitializeParams", [value]))

    @jsii.member(jsii_name="resetAutoDelete")
    def reset_auto_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoDelete", []))

    @jsii.member(jsii_name="resetBoot")
    def reset_boot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBoot", []))

    @jsii.member(jsii_name="resetDeviceName")
    def reset_device_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceName", []))

    @jsii.member(jsii_name="resetInitializeParams")
    def reset_initialize_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitializeParams", []))

    @jsii.member(jsii_name="resetInterface")
    def reset_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterface", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="initializeParams")
    def initialize_params(self) -> ElastigroupGcpDiskInitializeParamsList:
        return typing.cast(ElastigroupGcpDiskInitializeParamsList, jsii.get(self, "initializeParams"))

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
    @jsii.member(jsii_name="initializeParamsInput")
    def initialize_params_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpDiskInitializeParams]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpDiskInitializeParams]]], jsii.get(self, "initializeParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="interfaceInput")
    def interface_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskOutputReference, "auto_delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoDelete", value)

    @builtins.property
    @jsii.member(jsii_name="boot")
    def boot(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "boot"))

    @boot.setter
    def boot(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskOutputReference, "boot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "boot", value)

    @builtins.property
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceName"))

    @device_name.setter
    def device_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskOutputReference, "device_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceName", value)

    @builtins.property
    @jsii.member(jsii_name="interface")
    def interface(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interface"))

    @interface.setter
    def interface(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskOutputReference, "interface").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interface", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupGcpDisk, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupGcpDisk, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupGcpDisk, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpGpu",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "type": "type"},
)
class ElastigroupGcpGpu:
    def __init__(self, *, count: jsii.Number, type: builtins.str) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#count ElastigroupGcp#count}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#type ElastigroupGcp#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpGpu.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
            "type": type,
        }

    @builtins.property
    def count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#count ElastigroupGcp#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#type ElastigroupGcp#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpGpu(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupGcpGpuList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpGpuList",
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
            type_hints = typing.get_type_hints(ElastigroupGcpGpuList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ElastigroupGcpGpuOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpGpuList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupGcpGpuOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpGpuList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpGpuList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpGpuList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpGpu]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpGpu]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpGpu]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpGpuList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpGpuOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpGpuOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpGpuOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpGpuOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpGpuOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupGcpGpu, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupGcpGpu, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupGcpGpu, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpGpuOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpInstanceTypesCustom",
    jsii_struct_bases=[],
    name_mapping={"memory_gib": "memoryGib", "vcpu": "vcpu"},
)
class ElastigroupGcpInstanceTypesCustom:
    def __init__(self, *, memory_gib: jsii.Number, vcpu: jsii.Number) -> None:
        '''
        :param memory_gib: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#memory_gib ElastigroupGcp#memory_gib}.
        :param vcpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#vcpu ElastigroupGcp#vcpu}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpInstanceTypesCustom.__init__)
            check_type(argname="argument memory_gib", value=memory_gib, expected_type=type_hints["memory_gib"])
            check_type(argname="argument vcpu", value=vcpu, expected_type=type_hints["vcpu"])
        self._values: typing.Dict[str, typing.Any] = {
            "memory_gib": memory_gib,
            "vcpu": vcpu,
        }

    @builtins.property
    def memory_gib(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#memory_gib ElastigroupGcp#memory_gib}.'''
        result = self._values.get("memory_gib")
        assert result is not None, "Required property 'memory_gib' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def vcpu(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#vcpu ElastigroupGcp#vcpu}.'''
        result = self._values.get("vcpu")
        assert result is not None, "Required property 'vcpu' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpInstanceTypesCustom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupGcpInstanceTypesCustomList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpInstanceTypesCustomList",
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
            type_hints = typing.get_type_hints(ElastigroupGcpInstanceTypesCustomList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupGcpInstanceTypesCustomOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpInstanceTypesCustomList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupGcpInstanceTypesCustomOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpInstanceTypesCustomList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpInstanceTypesCustomList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpInstanceTypesCustomList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpInstanceTypesCustom]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpInstanceTypesCustom]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpInstanceTypesCustom]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpInstanceTypesCustomList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpInstanceTypesCustomOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpInstanceTypesCustomOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpInstanceTypesCustomOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="memoryGibInput")
    def memory_gib_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryGibInput"))

    @builtins.property
    @jsii.member(jsii_name="vcpuInput")
    def vcpu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vcpuInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryGib")
    def memory_gib(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryGib"))

    @memory_gib.setter
    def memory_gib(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpInstanceTypesCustomOutputReference, "memory_gib").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryGib", value)

    @builtins.property
    @jsii.member(jsii_name="vcpu")
    def vcpu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vcpu"))

    @vcpu.setter
    def vcpu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpInstanceTypesCustomOutputReference, "vcpu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vcpu", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupGcpInstanceTypesCustom, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupGcpInstanceTypesCustom, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupGcpInstanceTypesCustom, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpInstanceTypesCustomOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpIntegrationDockerSwarm",
    jsii_struct_bases=[],
    name_mapping={"master_host": "masterHost", "master_port": "masterPort"},
)
class ElastigroupGcpIntegrationDockerSwarm:
    def __init__(self, *, master_host: builtins.str, master_port: jsii.Number) -> None:
        '''
        :param master_host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#master_host ElastigroupGcp#master_host}.
        :param master_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#master_port ElastigroupGcp#master_port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpIntegrationDockerSwarm.__init__)
            check_type(argname="argument master_host", value=master_host, expected_type=type_hints["master_host"])
            check_type(argname="argument master_port", value=master_port, expected_type=type_hints["master_port"])
        self._values: typing.Dict[str, typing.Any] = {
            "master_host": master_host,
            "master_port": master_port,
        }

    @builtins.property
    def master_host(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#master_host ElastigroupGcp#master_host}.'''
        result = self._values.get("master_host")
        assert result is not None, "Required property 'master_host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def master_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#master_port ElastigroupGcp#master_port}.'''
        result = self._values.get("master_port")
        assert result is not None, "Required property 'master_port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpIntegrationDockerSwarm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupGcpIntegrationDockerSwarmOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpIntegrationDockerSwarmOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpIntegrationDockerSwarmOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="masterHostInput")
    def master_host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterHostInput"))

    @builtins.property
    @jsii.member(jsii_name="masterPortInput")
    def master_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "masterPortInput"))

    @builtins.property
    @jsii.member(jsii_name="masterHost")
    def master_host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterHost"))

    @master_host.setter
    def master_host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationDockerSwarmOutputReference, "master_host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterHost", value)

    @builtins.property
    @jsii.member(jsii_name="masterPort")
    def master_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "masterPort"))

    @master_port.setter
    def master_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationDockerSwarmOutputReference, "master_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterPort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastigroupGcpIntegrationDockerSwarm]:
        return typing.cast(typing.Optional[ElastigroupGcpIntegrationDockerSwarm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastigroupGcpIntegrationDockerSwarm],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationDockerSwarmOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpIntegrationGke",
    jsii_struct_bases=[],
    name_mapping={
        "autoscale_cooldown": "autoscaleCooldown",
        "autoscale_down": "autoscaleDown",
        "autoscale_headroom": "autoscaleHeadroom",
        "autoscale_is_auto_config": "autoscaleIsAutoConfig",
        "autoscale_is_enabled": "autoscaleIsEnabled",
        "autoscale_labels": "autoscaleLabels",
        "auto_update": "autoUpdate",
        "cluster_id": "clusterId",
        "location": "location",
    },
)
class ElastigroupGcpIntegrationGke:
    def __init__(
        self,
        *,
        autoscale_cooldown: typing.Optional[jsii.Number] = None,
        autoscale_down: typing.Optional[typing.Union["ElastigroupGcpIntegrationGkeAutoscaleDown", typing.Dict[str, typing.Any]]] = None,
        autoscale_headroom: typing.Optional[typing.Union["ElastigroupGcpIntegrationGkeAutoscaleHeadroom", typing.Dict[str, typing.Any]]] = None,
        autoscale_is_auto_config: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        autoscale_is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        autoscale_labels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpIntegrationGkeAutoscaleLabels", typing.Dict[str, typing.Any]]]]] = None,
        auto_update: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param autoscale_cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#autoscale_cooldown ElastigroupGcp#autoscale_cooldown}.
        :param autoscale_down: autoscale_down block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#autoscale_down ElastigroupGcp#autoscale_down}
        :param autoscale_headroom: autoscale_headroom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#autoscale_headroom ElastigroupGcp#autoscale_headroom}
        :param autoscale_is_auto_config: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#autoscale_is_auto_config ElastigroupGcp#autoscale_is_auto_config}.
        :param autoscale_is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#autoscale_is_enabled ElastigroupGcp#autoscale_is_enabled}.
        :param autoscale_labels: autoscale_labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#autoscale_labels ElastigroupGcp#autoscale_labels}
        :param auto_update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#auto_update ElastigroupGcp#auto_update}.
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#cluster_id ElastigroupGcp#cluster_id}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#location ElastigroupGcp#location}.
        '''
        if isinstance(autoscale_down, dict):
            autoscale_down = ElastigroupGcpIntegrationGkeAutoscaleDown(**autoscale_down)
        if isinstance(autoscale_headroom, dict):
            autoscale_headroom = ElastigroupGcpIntegrationGkeAutoscaleHeadroom(**autoscale_headroom)
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpIntegrationGke.__init__)
            check_type(argname="argument autoscale_cooldown", value=autoscale_cooldown, expected_type=type_hints["autoscale_cooldown"])
            check_type(argname="argument autoscale_down", value=autoscale_down, expected_type=type_hints["autoscale_down"])
            check_type(argname="argument autoscale_headroom", value=autoscale_headroom, expected_type=type_hints["autoscale_headroom"])
            check_type(argname="argument autoscale_is_auto_config", value=autoscale_is_auto_config, expected_type=type_hints["autoscale_is_auto_config"])
            check_type(argname="argument autoscale_is_enabled", value=autoscale_is_enabled, expected_type=type_hints["autoscale_is_enabled"])
            check_type(argname="argument autoscale_labels", value=autoscale_labels, expected_type=type_hints["autoscale_labels"])
            check_type(argname="argument auto_update", value=auto_update, expected_type=type_hints["auto_update"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
        self._values: typing.Dict[str, typing.Any] = {}
        if autoscale_cooldown is not None:
            self._values["autoscale_cooldown"] = autoscale_cooldown
        if autoscale_down is not None:
            self._values["autoscale_down"] = autoscale_down
        if autoscale_headroom is not None:
            self._values["autoscale_headroom"] = autoscale_headroom
        if autoscale_is_auto_config is not None:
            self._values["autoscale_is_auto_config"] = autoscale_is_auto_config
        if autoscale_is_enabled is not None:
            self._values["autoscale_is_enabled"] = autoscale_is_enabled
        if autoscale_labels is not None:
            self._values["autoscale_labels"] = autoscale_labels
        if auto_update is not None:
            self._values["auto_update"] = auto_update
        if cluster_id is not None:
            self._values["cluster_id"] = cluster_id
        if location is not None:
            self._values["location"] = location

    @builtins.property
    def autoscale_cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#autoscale_cooldown ElastigroupGcp#autoscale_cooldown}.'''
        result = self._values.get("autoscale_cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def autoscale_down(
        self,
    ) -> typing.Optional["ElastigroupGcpIntegrationGkeAutoscaleDown"]:
        '''autoscale_down block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#autoscale_down ElastigroupGcp#autoscale_down}
        '''
        result = self._values.get("autoscale_down")
        return typing.cast(typing.Optional["ElastigroupGcpIntegrationGkeAutoscaleDown"], result)

    @builtins.property
    def autoscale_headroom(
        self,
    ) -> typing.Optional["ElastigroupGcpIntegrationGkeAutoscaleHeadroom"]:
        '''autoscale_headroom block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#autoscale_headroom ElastigroupGcp#autoscale_headroom}
        '''
        result = self._values.get("autoscale_headroom")
        return typing.cast(typing.Optional["ElastigroupGcpIntegrationGkeAutoscaleHeadroom"], result)

    @builtins.property
    def autoscale_is_auto_config(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#autoscale_is_auto_config ElastigroupGcp#autoscale_is_auto_config}.'''
        result = self._values.get("autoscale_is_auto_config")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def autoscale_is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#autoscale_is_enabled ElastigroupGcp#autoscale_is_enabled}.'''
        result = self._values.get("autoscale_is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def autoscale_labels(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpIntegrationGkeAutoscaleLabels"]]]:
        '''autoscale_labels block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#autoscale_labels ElastigroupGcp#autoscale_labels}
        '''
        result = self._values.get("autoscale_labels")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpIntegrationGkeAutoscaleLabels"]]], result)

    @builtins.property
    def auto_update(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#auto_update ElastigroupGcp#auto_update}.'''
        result = self._values.get("auto_update")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#cluster_id ElastigroupGcp#cluster_id}.'''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#location ElastigroupGcp#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpIntegrationGke(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpIntegrationGkeAutoscaleDown",
    jsii_struct_bases=[],
    name_mapping={"evaluation_periods": "evaluationPeriods"},
)
class ElastigroupGcpIntegrationGkeAutoscaleDown:
    def __init__(
        self,
        *,
        evaluation_periods: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param evaluation_periods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#evaluation_periods ElastigroupGcp#evaluation_periods}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpIntegrationGkeAutoscaleDown.__init__)
            check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
        self._values: typing.Dict[str, typing.Any] = {}
        if evaluation_periods is not None:
            self._values["evaluation_periods"] = evaluation_periods

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#evaluation_periods ElastigroupGcp#evaluation_periods}.'''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpIntegrationGkeAutoscaleDown(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupGcpIntegrationGkeAutoscaleDownOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpIntegrationGkeAutoscaleDownOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpIntegrationGkeAutoscaleDownOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEvaluationPeriods")
    def reset_evaluation_periods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluationPeriods", []))

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriodsInput")
    def evaluation_periods_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "evaluationPeriodsInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriods")
    def evaluation_periods(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "evaluationPeriods"))

    @evaluation_periods.setter
    def evaluation_periods(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeAutoscaleDownOutputReference, "evaluation_periods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationPeriods", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElastigroupGcpIntegrationGkeAutoscaleDown]:
        return typing.cast(typing.Optional[ElastigroupGcpIntegrationGkeAutoscaleDown], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastigroupGcpIntegrationGkeAutoscaleDown],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeAutoscaleDownOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpIntegrationGkeAutoscaleHeadroom",
    jsii_struct_bases=[],
    name_mapping={
        "cpu_per_unit": "cpuPerUnit",
        "memory_per_unit": "memoryPerUnit",
        "num_of_units": "numOfUnits",
    },
)
class ElastigroupGcpIntegrationGkeAutoscaleHeadroom:
    def __init__(
        self,
        *,
        cpu_per_unit: typing.Optional[jsii.Number] = None,
        memory_per_unit: typing.Optional[jsii.Number] = None,
        num_of_units: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#cpu_per_unit ElastigroupGcp#cpu_per_unit}.
        :param memory_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#memory_per_unit ElastigroupGcp#memory_per_unit}.
        :param num_of_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#num_of_units ElastigroupGcp#num_of_units}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpIntegrationGkeAutoscaleHeadroom.__init__)
            check_type(argname="argument cpu_per_unit", value=cpu_per_unit, expected_type=type_hints["cpu_per_unit"])
            check_type(argname="argument memory_per_unit", value=memory_per_unit, expected_type=type_hints["memory_per_unit"])
            check_type(argname="argument num_of_units", value=num_of_units, expected_type=type_hints["num_of_units"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cpu_per_unit is not None:
            self._values["cpu_per_unit"] = cpu_per_unit
        if memory_per_unit is not None:
            self._values["memory_per_unit"] = memory_per_unit
        if num_of_units is not None:
            self._values["num_of_units"] = num_of_units

    @builtins.property
    def cpu_per_unit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#cpu_per_unit ElastigroupGcp#cpu_per_unit}.'''
        result = self._values.get("cpu_per_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_per_unit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#memory_per_unit ElastigroupGcp#memory_per_unit}.'''
        result = self._values.get("memory_per_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def num_of_units(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#num_of_units ElastigroupGcp#num_of_units}.'''
        result = self._values.get("num_of_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpIntegrationGkeAutoscaleHeadroom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupGcpIntegrationGkeAutoscaleHeadroomOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpIntegrationGkeAutoscaleHeadroomOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpIntegrationGkeAutoscaleHeadroomOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCpuPerUnit")
    def reset_cpu_per_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuPerUnit", []))

    @jsii.member(jsii_name="resetMemoryPerUnit")
    def reset_memory_per_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryPerUnit", []))

    @jsii.member(jsii_name="resetNumOfUnits")
    def reset_num_of_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumOfUnits", []))

    @builtins.property
    @jsii.member(jsii_name="cpuPerUnitInput")
    def cpu_per_unit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuPerUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryPerUnitInput")
    def memory_per_unit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryPerUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="numOfUnitsInput")
    def num_of_units_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numOfUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuPerUnit")
    def cpu_per_unit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuPerUnit"))

    @cpu_per_unit.setter
    def cpu_per_unit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeAutoscaleHeadroomOutputReference, "cpu_per_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuPerUnit", value)

    @builtins.property
    @jsii.member(jsii_name="memoryPerUnit")
    def memory_per_unit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryPerUnit"))

    @memory_per_unit.setter
    def memory_per_unit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeAutoscaleHeadroomOutputReference, "memory_per_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryPerUnit", value)

    @builtins.property
    @jsii.member(jsii_name="numOfUnits")
    def num_of_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numOfUnits"))

    @num_of_units.setter
    def num_of_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeAutoscaleHeadroomOutputReference, "num_of_units").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numOfUnits", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElastigroupGcpIntegrationGkeAutoscaleHeadroom]:
        return typing.cast(typing.Optional[ElastigroupGcpIntegrationGkeAutoscaleHeadroom], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastigroupGcpIntegrationGkeAutoscaleHeadroom],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeAutoscaleHeadroomOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpIntegrationGkeAutoscaleLabels",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class ElastigroupGcpIntegrationGkeAutoscaleLabels:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#key ElastigroupGcp#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#value ElastigroupGcp#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpIntegrationGkeAutoscaleLabels.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#key ElastigroupGcp#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#value ElastigroupGcp#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpIntegrationGkeAutoscaleLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupGcpIntegrationGkeAutoscaleLabelsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpIntegrationGkeAutoscaleLabelsList",
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
            type_hints = typing.get_type_hints(ElastigroupGcpIntegrationGkeAutoscaleLabelsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupGcpIntegrationGkeAutoscaleLabelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpIntegrationGkeAutoscaleLabelsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupGcpIntegrationGkeAutoscaleLabelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeAutoscaleLabelsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeAutoscaleLabelsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeAutoscaleLabelsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpIntegrationGkeAutoscaleLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpIntegrationGkeAutoscaleLabels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpIntegrationGkeAutoscaleLabels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeAutoscaleLabelsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpIntegrationGkeAutoscaleLabelsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpIntegrationGkeAutoscaleLabelsOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpIntegrationGkeAutoscaleLabelsOutputReference.__init__)
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
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeAutoscaleLabelsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeAutoscaleLabelsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupGcpIntegrationGkeAutoscaleLabels, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupGcpIntegrationGkeAutoscaleLabels, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupGcpIntegrationGkeAutoscaleLabels, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeAutoscaleLabelsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpIntegrationGkeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpIntegrationGkeOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpIntegrationGkeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutoscaleDown")
    def put_autoscale_down(
        self,
        *,
        evaluation_periods: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param evaluation_periods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#evaluation_periods ElastigroupGcp#evaluation_periods}.
        '''
        value = ElastigroupGcpIntegrationGkeAutoscaleDown(
            evaluation_periods=evaluation_periods
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscaleDown", [value]))

    @jsii.member(jsii_name="putAutoscaleHeadroom")
    def put_autoscale_headroom(
        self,
        *,
        cpu_per_unit: typing.Optional[jsii.Number] = None,
        memory_per_unit: typing.Optional[jsii.Number] = None,
        num_of_units: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#cpu_per_unit ElastigroupGcp#cpu_per_unit}.
        :param memory_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#memory_per_unit ElastigroupGcp#memory_per_unit}.
        :param num_of_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#num_of_units ElastigroupGcp#num_of_units}.
        '''
        value = ElastigroupGcpIntegrationGkeAutoscaleHeadroom(
            cpu_per_unit=cpu_per_unit,
            memory_per_unit=memory_per_unit,
            num_of_units=num_of_units,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscaleHeadroom", [value]))

    @jsii.member(jsii_name="putAutoscaleLabels")
    def put_autoscale_labels(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastigroupGcpIntegrationGkeAutoscaleLabels, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpIntegrationGkeOutputReference.put_autoscale_labels)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAutoscaleLabels", [value]))

    @jsii.member(jsii_name="resetAutoscaleCooldown")
    def reset_autoscale_cooldown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaleCooldown", []))

    @jsii.member(jsii_name="resetAutoscaleDown")
    def reset_autoscale_down(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaleDown", []))

    @jsii.member(jsii_name="resetAutoscaleHeadroom")
    def reset_autoscale_headroom(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaleHeadroom", []))

    @jsii.member(jsii_name="resetAutoscaleIsAutoConfig")
    def reset_autoscale_is_auto_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaleIsAutoConfig", []))

    @jsii.member(jsii_name="resetAutoscaleIsEnabled")
    def reset_autoscale_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaleIsEnabled", []))

    @jsii.member(jsii_name="resetAutoscaleLabels")
    def reset_autoscale_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaleLabels", []))

    @jsii.member(jsii_name="resetAutoUpdate")
    def reset_auto_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoUpdate", []))

    @jsii.member(jsii_name="resetClusterId")
    def reset_cluster_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterId", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @builtins.property
    @jsii.member(jsii_name="autoscaleDown")
    def autoscale_down(
        self,
    ) -> ElastigroupGcpIntegrationGkeAutoscaleDownOutputReference:
        return typing.cast(ElastigroupGcpIntegrationGkeAutoscaleDownOutputReference, jsii.get(self, "autoscaleDown"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleHeadroom")
    def autoscale_headroom(
        self,
    ) -> ElastigroupGcpIntegrationGkeAutoscaleHeadroomOutputReference:
        return typing.cast(ElastigroupGcpIntegrationGkeAutoscaleHeadroomOutputReference, jsii.get(self, "autoscaleHeadroom"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleLabels")
    def autoscale_labels(self) -> ElastigroupGcpIntegrationGkeAutoscaleLabelsList:
        return typing.cast(ElastigroupGcpIntegrationGkeAutoscaleLabelsList, jsii.get(self, "autoscaleLabels"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleCooldownInput")
    def autoscale_cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autoscaleCooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleDownInput")
    def autoscale_down_input(
        self,
    ) -> typing.Optional[ElastigroupGcpIntegrationGkeAutoscaleDown]:
        return typing.cast(typing.Optional[ElastigroupGcpIntegrationGkeAutoscaleDown], jsii.get(self, "autoscaleDownInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleHeadroomInput")
    def autoscale_headroom_input(
        self,
    ) -> typing.Optional[ElastigroupGcpIntegrationGkeAutoscaleHeadroom]:
        return typing.cast(typing.Optional[ElastigroupGcpIntegrationGkeAutoscaleHeadroom], jsii.get(self, "autoscaleHeadroomInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleIsAutoConfigInput")
    def autoscale_is_auto_config_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoscaleIsAutoConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleIsEnabledInput")
    def autoscale_is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoscaleIsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleLabelsInput")
    def autoscale_labels_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpIntegrationGkeAutoscaleLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpIntegrationGkeAutoscaleLabels]]], jsii.get(self, "autoscaleLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoUpdateInput")
    def auto_update_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoUpdateInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleCooldown")
    def autoscale_cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autoscaleCooldown"))

    @autoscale_cooldown.setter
    def autoscale_cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeOutputReference, "autoscale_cooldown").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoscaleCooldown", value)

    @builtins.property
    @jsii.member(jsii_name="autoscaleIsAutoConfig")
    def autoscale_is_auto_config(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoscaleIsAutoConfig"))

    @autoscale_is_auto_config.setter
    def autoscale_is_auto_config(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeOutputReference, "autoscale_is_auto_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoscaleIsAutoConfig", value)

    @builtins.property
    @jsii.member(jsii_name="autoscaleIsEnabled")
    def autoscale_is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoscaleIsEnabled"))

    @autoscale_is_enabled.setter
    def autoscale_is_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeOutputReference, "autoscale_is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoscaleIsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="autoUpdate")
    def auto_update(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoUpdate"))

    @auto_update.setter
    def auto_update(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeOutputReference, "auto_update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoUpdate", value)

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeOutputReference, "cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeOutputReference, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastigroupGcpIntegrationGke]:
        return typing.cast(typing.Optional[ElastigroupGcpIntegrationGke], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastigroupGcpIntegrationGke],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpIntegrationGkeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpLabels",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class ElastigroupGcpLabels:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#key ElastigroupGcp#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#value ElastigroupGcp#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpLabels.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#key ElastigroupGcp#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#value ElastigroupGcp#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupGcpLabelsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpLabelsList",
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
            type_hints = typing.get_type_hints(ElastigroupGcpLabelsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ElastigroupGcpLabelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpLabelsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupGcpLabelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpLabelsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpLabelsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpLabelsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpLabels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpLabels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpLabelsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpLabelsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpLabelsOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpLabelsOutputReference.__init__)
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
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpLabelsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpLabelsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupGcpLabels, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupGcpLabels, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupGcpLabels, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpLabelsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpMetadata",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class ElastigroupGcpMetadata:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#key ElastigroupGcp#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#value ElastigroupGcp#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpMetadata.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#key ElastigroupGcp#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#value ElastigroupGcp#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupGcpMetadataList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpMetadataList",
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
            type_hints = typing.get_type_hints(ElastigroupGcpMetadataList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ElastigroupGcpMetadataOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpMetadataList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupGcpMetadataOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpMetadataList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpMetadataList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpMetadataList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpMetadata]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpMetadata]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpMetadata]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpMetadataList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpMetadataOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpMetadataOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpMetadataOutputReference.__init__)
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
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpMetadataOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpMetadataOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupGcpMetadata, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupGcpMetadata, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupGcpMetadata, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpMetadataOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpNetworkInterface",
    jsii_struct_bases=[],
    name_mapping={
        "network": "network",
        "access_configs": "accessConfigs",
        "alias_ip_ranges": "aliasIpRanges",
    },
)
class ElastigroupGcpNetworkInterface:
    def __init__(
        self,
        *,
        network: builtins.str,
        access_configs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpNetworkInterfaceAccessConfigs", typing.Dict[str, typing.Any]]]]] = None,
        alias_ip_ranges: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpNetworkInterfaceAliasIpRanges", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#network ElastigroupGcp#network}.
        :param access_configs: access_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#access_configs ElastigroupGcp#access_configs}
        :param alias_ip_ranges: alias_ip_ranges block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#alias_ip_ranges ElastigroupGcp#alias_ip_ranges}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpNetworkInterface.__init__)
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument access_configs", value=access_configs, expected_type=type_hints["access_configs"])
            check_type(argname="argument alias_ip_ranges", value=alias_ip_ranges, expected_type=type_hints["alias_ip_ranges"])
        self._values: typing.Dict[str, typing.Any] = {
            "network": network,
        }
        if access_configs is not None:
            self._values["access_configs"] = access_configs
        if alias_ip_ranges is not None:
            self._values["alias_ip_ranges"] = alias_ip_ranges

    @builtins.property
    def network(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#network ElastigroupGcp#network}.'''
        result = self._values.get("network")
        assert result is not None, "Required property 'network' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_configs(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpNetworkInterfaceAccessConfigs"]]]:
        '''access_configs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#access_configs ElastigroupGcp#access_configs}
        '''
        result = self._values.get("access_configs")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpNetworkInterfaceAccessConfigs"]]], result)

    @builtins.property
    def alias_ip_ranges(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpNetworkInterfaceAliasIpRanges"]]]:
        '''alias_ip_ranges block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#alias_ip_ranges ElastigroupGcp#alias_ip_ranges}
        '''
        result = self._values.get("alias_ip_ranges")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpNetworkInterfaceAliasIpRanges"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpNetworkInterface(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpNetworkInterfaceAccessConfigs",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class ElastigroupGcpNetworkInterfaceAccessConfigs:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#name ElastigroupGcp#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#type ElastigroupGcp#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpNetworkInterfaceAccessConfigs.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#name ElastigroupGcp#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#type ElastigroupGcp#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpNetworkInterfaceAccessConfigs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupGcpNetworkInterfaceAccessConfigsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpNetworkInterfaceAccessConfigsList",
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
            type_hints = typing.get_type_hints(ElastigroupGcpNetworkInterfaceAccessConfigsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupGcpNetworkInterfaceAccessConfigsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpNetworkInterfaceAccessConfigsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupGcpNetworkInterfaceAccessConfigsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceAccessConfigsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceAccessConfigsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceAccessConfigsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpNetworkInterfaceAccessConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpNetworkInterfaceAccessConfigs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpNetworkInterfaceAccessConfigs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceAccessConfigsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpNetworkInterfaceAccessConfigsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpNetworkInterfaceAccessConfigsOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpNetworkInterfaceAccessConfigsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceAccessConfigsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceAccessConfigsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupGcpNetworkInterfaceAccessConfigs, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupGcpNetworkInterfaceAccessConfigs, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupGcpNetworkInterfaceAccessConfigs, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceAccessConfigsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpNetworkInterfaceAliasIpRanges",
    jsii_struct_bases=[],
    name_mapping={
        "ip_cidr_range": "ipCidrRange",
        "subnetwork_range_name": "subnetworkRangeName",
    },
)
class ElastigroupGcpNetworkInterfaceAliasIpRanges:
    def __init__(
        self,
        *,
        ip_cidr_range: builtins.str,
        subnetwork_range_name: builtins.str,
    ) -> None:
        '''
        :param ip_cidr_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#ip_cidr_range ElastigroupGcp#ip_cidr_range}.
        :param subnetwork_range_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#subnetwork_range_name ElastigroupGcp#subnetwork_range_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpNetworkInterfaceAliasIpRanges.__init__)
            check_type(argname="argument ip_cidr_range", value=ip_cidr_range, expected_type=type_hints["ip_cidr_range"])
            check_type(argname="argument subnetwork_range_name", value=subnetwork_range_name, expected_type=type_hints["subnetwork_range_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "ip_cidr_range": ip_cidr_range,
            "subnetwork_range_name": subnetwork_range_name,
        }

    @builtins.property
    def ip_cidr_range(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#ip_cidr_range ElastigroupGcp#ip_cidr_range}.'''
        result = self._values.get("ip_cidr_range")
        assert result is not None, "Required property 'ip_cidr_range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnetwork_range_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#subnetwork_range_name ElastigroupGcp#subnetwork_range_name}.'''
        result = self._values.get("subnetwork_range_name")
        assert result is not None, "Required property 'subnetwork_range_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpNetworkInterfaceAliasIpRanges(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupGcpNetworkInterfaceAliasIpRangesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpNetworkInterfaceAliasIpRangesList",
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
            type_hints = typing.get_type_hints(ElastigroupGcpNetworkInterfaceAliasIpRangesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupGcpNetworkInterfaceAliasIpRangesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpNetworkInterfaceAliasIpRangesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupGcpNetworkInterfaceAliasIpRangesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceAliasIpRangesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceAliasIpRangesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceAliasIpRangesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpNetworkInterfaceAliasIpRanges]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpNetworkInterfaceAliasIpRanges]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpNetworkInterfaceAliasIpRanges]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceAliasIpRangesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpNetworkInterfaceAliasIpRangesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpNetworkInterfaceAliasIpRangesOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpNetworkInterfaceAliasIpRangesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceAliasIpRangesOutputReference, "ip_cidr_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipCidrRange", value)

    @builtins.property
    @jsii.member(jsii_name="subnetworkRangeName")
    def subnetwork_range_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetworkRangeName"))

    @subnetwork_range_name.setter
    def subnetwork_range_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceAliasIpRangesOutputReference, "subnetwork_range_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetworkRangeName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupGcpNetworkInterfaceAliasIpRanges, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupGcpNetworkInterfaceAliasIpRanges, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupGcpNetworkInterfaceAliasIpRanges, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceAliasIpRangesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpNetworkInterfaceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpNetworkInterfaceList",
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
            type_hints = typing.get_type_hints(ElastigroupGcpNetworkInterfaceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupGcpNetworkInterfaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpNetworkInterfaceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupGcpNetworkInterfaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpNetworkInterface]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpNetworkInterface]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpNetworkInterface]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpNetworkInterfaceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpNetworkInterfaceOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpNetworkInterfaceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAccessConfigs")
    def put_access_configs(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastigroupGcpNetworkInterfaceAccessConfigs, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpNetworkInterfaceOutputReference.put_access_configs)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccessConfigs", [value]))

    @jsii.member(jsii_name="putAliasIpRanges")
    def put_alias_ip_ranges(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastigroupGcpNetworkInterfaceAliasIpRanges, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpNetworkInterfaceOutputReference.put_alias_ip_ranges)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAliasIpRanges", [value]))

    @jsii.member(jsii_name="resetAccessConfigs")
    def reset_access_configs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessConfigs", []))

    @jsii.member(jsii_name="resetAliasIpRanges")
    def reset_alias_ip_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAliasIpRanges", []))

    @builtins.property
    @jsii.member(jsii_name="accessConfigs")
    def access_configs(self) -> ElastigroupGcpNetworkInterfaceAccessConfigsList:
        return typing.cast(ElastigroupGcpNetworkInterfaceAccessConfigsList, jsii.get(self, "accessConfigs"))

    @builtins.property
    @jsii.member(jsii_name="aliasIpRanges")
    def alias_ip_ranges(self) -> ElastigroupGcpNetworkInterfaceAliasIpRangesList:
        return typing.cast(ElastigroupGcpNetworkInterfaceAliasIpRangesList, jsii.get(self, "aliasIpRanges"))

    @builtins.property
    @jsii.member(jsii_name="accessConfigsInput")
    def access_configs_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpNetworkInterfaceAccessConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpNetworkInterfaceAccessConfigs]]], jsii.get(self, "accessConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasIpRangesInput")
    def alias_ip_ranges_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpNetworkInterfaceAliasIpRanges]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpNetworkInterfaceAliasIpRanges]]], jsii.get(self, "aliasIpRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceOutputReference, "network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupGcpNetworkInterface, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupGcpNetworkInterface, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupGcpNetworkInterface, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpNetworkInterfaceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpScalingDownPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "policy_name": "policyName",
        "threshold": "threshold",
        "unit": "unit",
        "action_type": "actionType",
        "adjustment": "adjustment",
        "cooldown": "cooldown",
        "dimensions": "dimensions",
        "evaluation_periods": "evaluationPeriods",
        "operator": "operator",
        "period": "period",
        "source": "source",
        "statistic": "statistic",
    },
)
class ElastigroupGcpScalingDownPolicy:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        policy_name: builtins.str,
        threshold: jsii.Number,
        unit: builtins.str,
        action_type: typing.Optional[builtins.str] = None,
        adjustment: typing.Optional[jsii.Number] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpScalingDownPolicyDimensions", typing.Dict[str, typing.Any]]]]] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        operator: typing.Optional[builtins.str] = None,
        period: typing.Optional[jsii.Number] = None,
        source: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#metric_name ElastigroupGcp#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#namespace ElastigroupGcp#namespace}.
        :param policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#policy_name ElastigroupGcp#policy_name}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#threshold ElastigroupGcp#threshold}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#unit ElastigroupGcp#unit}.
        :param action_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#action_type ElastigroupGcp#action_type}.
        :param adjustment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#adjustment ElastigroupGcp#adjustment}.
        :param cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#cooldown ElastigroupGcp#cooldown}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#dimensions ElastigroupGcp#dimensions}
        :param evaluation_periods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#evaluation_periods ElastigroupGcp#evaluation_periods}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#operator ElastigroupGcp#operator}.
        :param period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#period ElastigroupGcp#period}.
        :param source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#source ElastigroupGcp#source}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#statistic ElastigroupGcp#statistic}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpScalingDownPolicy.__init__)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument action_type", value=action_type, expected_type=type_hints["action_type"])
            check_type(argname="argument adjustment", value=adjustment, expected_type=type_hints["adjustment"])
            check_type(argname="argument cooldown", value=cooldown, expected_type=type_hints["cooldown"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
            "policy_name": policy_name,
            "threshold": threshold,
            "unit": unit,
        }
        if action_type is not None:
            self._values["action_type"] = action_type
        if adjustment is not None:
            self._values["adjustment"] = adjustment
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if evaluation_periods is not None:
            self._values["evaluation_periods"] = evaluation_periods
        if operator is not None:
            self._values["operator"] = operator
        if period is not None:
            self._values["period"] = period
        if source is not None:
            self._values["source"] = source
        if statistic is not None:
            self._values["statistic"] = statistic

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#metric_name ElastigroupGcp#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#namespace ElastigroupGcp#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#policy_name ElastigroupGcp#policy_name}.'''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#threshold ElastigroupGcp#threshold}.'''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#unit ElastigroupGcp#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#action_type ElastigroupGcp#action_type}.'''
        result = self._values.get("action_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def adjustment(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#adjustment ElastigroupGcp#adjustment}.'''
        result = self._values.get("adjustment")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#cooldown ElastigroupGcp#cooldown}.'''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpScalingDownPolicyDimensions"]]]:
        '''dimensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#dimensions ElastigroupGcp#dimensions}
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpScalingDownPolicyDimensions"]]], result)

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#evaluation_periods ElastigroupGcp#evaluation_periods}.'''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#operator ElastigroupGcp#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#period ElastigroupGcp#period}.'''
        result = self._values.get("period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#source ElastigroupGcp#source}.'''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#statistic ElastigroupGcp#statistic}.'''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpScalingDownPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpScalingDownPolicyDimensions",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class ElastigroupGcpScalingDownPolicyDimensions:
    def __init__(
        self,
        *,
        name: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#name ElastigroupGcp#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#value ElastigroupGcp#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpScalingDownPolicyDimensions.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#name ElastigroupGcp#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#value ElastigroupGcp#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpScalingDownPolicyDimensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupGcpScalingDownPolicyDimensionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpScalingDownPolicyDimensionsList",
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
            type_hints = typing.get_type_hints(ElastigroupGcpScalingDownPolicyDimensionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupGcpScalingDownPolicyDimensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpScalingDownPolicyDimensionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupGcpScalingDownPolicyDimensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyDimensionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyDimensionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyDimensionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScalingDownPolicyDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScalingDownPolicyDimensions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScalingDownPolicyDimensions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyDimensionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpScalingDownPolicyDimensionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpScalingDownPolicyDimensionsOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpScalingDownPolicyDimensionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyDimensionsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyDimensionsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupGcpScalingDownPolicyDimensions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupGcpScalingDownPolicyDimensions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupGcpScalingDownPolicyDimensions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyDimensionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpScalingDownPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpScalingDownPolicyList",
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
            type_hints = typing.get_type_hints(ElastigroupGcpScalingDownPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupGcpScalingDownPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpScalingDownPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupGcpScalingDownPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScalingDownPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScalingDownPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScalingDownPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpScalingDownPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpScalingDownPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpScalingDownPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDimensions")
    def put_dimensions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastigroupGcpScalingDownPolicyDimensions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpScalingDownPolicyOutputReference.put_dimensions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDimensions", [value]))

    @jsii.member(jsii_name="resetActionType")
    def reset_action_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActionType", []))

    @jsii.member(jsii_name="resetAdjustment")
    def reset_adjustment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdjustment", []))

    @jsii.member(jsii_name="resetCooldown")
    def reset_cooldown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCooldown", []))

    @jsii.member(jsii_name="resetDimensions")
    def reset_dimensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimensions", []))

    @jsii.member(jsii_name="resetEvaluationPeriods")
    def reset_evaluation_periods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluationPeriods", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="resetStatistic")
    def reset_statistic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatistic", []))

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(self) -> ElastigroupGcpScalingDownPolicyDimensionsList:
        return typing.cast(ElastigroupGcpScalingDownPolicyDimensionsList, jsii.get(self, "dimensions"))

    @builtins.property
    @jsii.member(jsii_name="actionTypeInput")
    def action_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="adjustmentInput")
    def adjustment_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "adjustmentInput"))

    @builtins.property
    @jsii.member(jsii_name="cooldownInput")
    def cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionsInput")
    def dimensions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScalingDownPolicyDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScalingDownPolicyDimensions]]], jsii.get(self, "dimensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriodsInput")
    def evaluation_periods_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "evaluationPeriodsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="periodInput")
    def period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "periodInput"))

    @builtins.property
    @jsii.member(jsii_name="policyNameInput")
    def policy_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="statisticInput")
    def statistic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statisticInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="actionType")
    def action_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionType"))

    @action_type.setter
    def action_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyOutputReference, "action_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionType", value)

    @builtins.property
    @jsii.member(jsii_name="adjustment")
    def adjustment(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "adjustment"))

    @adjustment.setter
    def adjustment(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyOutputReference, "adjustment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adjustment", value)

    @builtins.property
    @jsii.member(jsii_name="cooldown")
    def cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cooldown"))

    @cooldown.setter
    def cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyOutputReference, "cooldown").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cooldown", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriods")
    def evaluation_periods(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "evaluationPeriods"))

    @evaluation_periods.setter
    def evaluation_periods(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyOutputReference, "evaluation_periods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationPeriods", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyOutputReference, "metric_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "period"))

    @period.setter
    def period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyOutputReference, "period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyOutputReference, "policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyOutputReference, "statistic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statistic", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyOutputReference, "unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupGcpScalingDownPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupGcpScalingDownPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupGcpScalingDownPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingDownPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpScalingUpPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "policy_name": "policyName",
        "threshold": "threshold",
        "unit": "unit",
        "action_type": "actionType",
        "adjustment": "adjustment",
        "cooldown": "cooldown",
        "dimensions": "dimensions",
        "evaluation_periods": "evaluationPeriods",
        "operator": "operator",
        "period": "period",
        "source": "source",
        "statistic": "statistic",
    },
)
class ElastigroupGcpScalingUpPolicy:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        policy_name: builtins.str,
        threshold: jsii.Number,
        unit: builtins.str,
        action_type: typing.Optional[builtins.str] = None,
        adjustment: typing.Optional[jsii.Number] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastigroupGcpScalingUpPolicyDimensions", typing.Dict[str, typing.Any]]]]] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        operator: typing.Optional[builtins.str] = None,
        period: typing.Optional[jsii.Number] = None,
        source: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#metric_name ElastigroupGcp#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#namespace ElastigroupGcp#namespace}.
        :param policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#policy_name ElastigroupGcp#policy_name}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#threshold ElastigroupGcp#threshold}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#unit ElastigroupGcp#unit}.
        :param action_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#action_type ElastigroupGcp#action_type}.
        :param adjustment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#adjustment ElastigroupGcp#adjustment}.
        :param cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#cooldown ElastigroupGcp#cooldown}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#dimensions ElastigroupGcp#dimensions}
        :param evaluation_periods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#evaluation_periods ElastigroupGcp#evaluation_periods}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#operator ElastigroupGcp#operator}.
        :param period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#period ElastigroupGcp#period}.
        :param source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#source ElastigroupGcp#source}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#statistic ElastigroupGcp#statistic}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpScalingUpPolicy.__init__)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument action_type", value=action_type, expected_type=type_hints["action_type"])
            check_type(argname="argument adjustment", value=adjustment, expected_type=type_hints["adjustment"])
            check_type(argname="argument cooldown", value=cooldown, expected_type=type_hints["cooldown"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
            "policy_name": policy_name,
            "threshold": threshold,
            "unit": unit,
        }
        if action_type is not None:
            self._values["action_type"] = action_type
        if adjustment is not None:
            self._values["adjustment"] = adjustment
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if evaluation_periods is not None:
            self._values["evaluation_periods"] = evaluation_periods
        if operator is not None:
            self._values["operator"] = operator
        if period is not None:
            self._values["period"] = period
        if source is not None:
            self._values["source"] = source
        if statistic is not None:
            self._values["statistic"] = statistic

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#metric_name ElastigroupGcp#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#namespace ElastigroupGcp#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#policy_name ElastigroupGcp#policy_name}.'''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#threshold ElastigroupGcp#threshold}.'''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#unit ElastigroupGcp#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#action_type ElastigroupGcp#action_type}.'''
        result = self._values.get("action_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def adjustment(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#adjustment ElastigroupGcp#adjustment}.'''
        result = self._values.get("adjustment")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#cooldown ElastigroupGcp#cooldown}.'''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpScalingUpPolicyDimensions"]]]:
        '''dimensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#dimensions ElastigroupGcp#dimensions}
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastigroupGcpScalingUpPolicyDimensions"]]], result)

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#evaluation_periods ElastigroupGcp#evaluation_periods}.'''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#operator ElastigroupGcp#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#period ElastigroupGcp#period}.'''
        result = self._values.get("period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#source ElastigroupGcp#source}.'''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#statistic ElastigroupGcp#statistic}.'''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpScalingUpPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpScalingUpPolicyDimensions",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class ElastigroupGcpScalingUpPolicyDimensions:
    def __init__(
        self,
        *,
        name: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#name ElastigroupGcp#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#value ElastigroupGcp#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpScalingUpPolicyDimensions.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#name ElastigroupGcp#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#value ElastigroupGcp#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpScalingUpPolicyDimensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupGcpScalingUpPolicyDimensionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpScalingUpPolicyDimensionsList",
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
            type_hints = typing.get_type_hints(ElastigroupGcpScalingUpPolicyDimensionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastigroupGcpScalingUpPolicyDimensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpScalingUpPolicyDimensionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupGcpScalingUpPolicyDimensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyDimensionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyDimensionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyDimensionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScalingUpPolicyDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScalingUpPolicyDimensions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScalingUpPolicyDimensions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyDimensionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpScalingUpPolicyDimensionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpScalingUpPolicyDimensionsOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpScalingUpPolicyDimensionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyDimensionsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyDimensionsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupGcpScalingUpPolicyDimensions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupGcpScalingUpPolicyDimensions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupGcpScalingUpPolicyDimensions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyDimensionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpScalingUpPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpScalingUpPolicyList",
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
            type_hints = typing.get_type_hints(ElastigroupGcpScalingUpPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ElastigroupGcpScalingUpPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpScalingUpPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupGcpScalingUpPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScalingUpPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScalingUpPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScalingUpPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpScalingUpPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpScalingUpPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpScalingUpPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDimensions")
    def put_dimensions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastigroupGcpScalingUpPolicyDimensions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpScalingUpPolicyOutputReference.put_dimensions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDimensions", [value]))

    @jsii.member(jsii_name="resetActionType")
    def reset_action_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActionType", []))

    @jsii.member(jsii_name="resetAdjustment")
    def reset_adjustment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdjustment", []))

    @jsii.member(jsii_name="resetCooldown")
    def reset_cooldown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCooldown", []))

    @jsii.member(jsii_name="resetDimensions")
    def reset_dimensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimensions", []))

    @jsii.member(jsii_name="resetEvaluationPeriods")
    def reset_evaluation_periods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluationPeriods", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="resetStatistic")
    def reset_statistic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatistic", []))

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(self) -> ElastigroupGcpScalingUpPolicyDimensionsList:
        return typing.cast(ElastigroupGcpScalingUpPolicyDimensionsList, jsii.get(self, "dimensions"))

    @builtins.property
    @jsii.member(jsii_name="actionTypeInput")
    def action_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="adjustmentInput")
    def adjustment_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "adjustmentInput"))

    @builtins.property
    @jsii.member(jsii_name="cooldownInput")
    def cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionsInput")
    def dimensions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScalingUpPolicyDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScalingUpPolicyDimensions]]], jsii.get(self, "dimensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriodsInput")
    def evaluation_periods_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "evaluationPeriodsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="periodInput")
    def period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "periodInput"))

    @builtins.property
    @jsii.member(jsii_name="policyNameInput")
    def policy_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="statisticInput")
    def statistic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statisticInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="actionType")
    def action_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionType"))

    @action_type.setter
    def action_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyOutputReference, "action_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionType", value)

    @builtins.property
    @jsii.member(jsii_name="adjustment")
    def adjustment(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "adjustment"))

    @adjustment.setter
    def adjustment(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyOutputReference, "adjustment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adjustment", value)

    @builtins.property
    @jsii.member(jsii_name="cooldown")
    def cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cooldown"))

    @cooldown.setter
    def cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyOutputReference, "cooldown").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cooldown", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriods")
    def evaluation_periods(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "evaluationPeriods"))

    @evaluation_periods.setter
    def evaluation_periods(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyOutputReference, "evaluation_periods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationPeriods", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyOutputReference, "metric_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "period"))

    @period.setter
    def period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyOutputReference, "period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyOutputReference, "policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyOutputReference, "statistic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statistic", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyOutputReference, "unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupGcpScalingUpPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupGcpScalingUpPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupGcpScalingUpPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScalingUpPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpScheduledTask",
    jsii_struct_bases=[],
    name_mapping={
        "task_type": "taskType",
        "cron_expression": "cronExpression",
        "is_enabled": "isEnabled",
        "max_capacity": "maxCapacity",
        "min_capacity": "minCapacity",
        "target_capacity": "targetCapacity",
    },
)
class ElastigroupGcpScheduledTask:
    def __init__(
        self,
        *,
        task_type: builtins.str,
        cron_expression: typing.Optional[builtins.str] = None,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_capacity: typing.Optional[builtins.str] = None,
        min_capacity: typing.Optional[builtins.str] = None,
        target_capacity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param task_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#task_type ElastigroupGcp#task_type}.
        :param cron_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#cron_expression ElastigroupGcp#cron_expression}.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#is_enabled ElastigroupGcp#is_enabled}.
        :param max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#max_capacity ElastigroupGcp#max_capacity}.
        :param min_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#min_capacity ElastigroupGcp#min_capacity}.
        :param target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#target_capacity ElastigroupGcp#target_capacity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpScheduledTask.__init__)
            check_type(argname="argument task_type", value=task_type, expected_type=type_hints["task_type"])
            check_type(argname="argument cron_expression", value=cron_expression, expected_type=type_hints["cron_expression"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
            check_type(argname="argument target_capacity", value=target_capacity, expected_type=type_hints["target_capacity"])
        self._values: typing.Dict[str, typing.Any] = {
            "task_type": task_type,
        }
        if cron_expression is not None:
            self._values["cron_expression"] = cron_expression
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if max_capacity is not None:
            self._values["max_capacity"] = max_capacity
        if min_capacity is not None:
            self._values["min_capacity"] = min_capacity
        if target_capacity is not None:
            self._values["target_capacity"] = target_capacity

    @builtins.property
    def task_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#task_type ElastigroupGcp#task_type}.'''
        result = self._values.get("task_type")
        assert result is not None, "Required property 'task_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cron_expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#cron_expression ElastigroupGcp#cron_expression}.'''
        result = self._values.get("cron_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#is_enabled ElastigroupGcp#is_enabled}.'''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#max_capacity ElastigroupGcp#max_capacity}.'''
        result = self._values.get("max_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#min_capacity ElastigroupGcp#min_capacity}.'''
        result = self._values.get("min_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#target_capacity ElastigroupGcp#target_capacity}.'''
        result = self._values.get("target_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpScheduledTask(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupGcpScheduledTaskList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpScheduledTaskList",
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
            type_hints = typing.get_type_hints(ElastigroupGcpScheduledTaskList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ElastigroupGcpScheduledTaskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpScheduledTaskList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupGcpScheduledTaskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScheduledTaskList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScheduledTaskList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScheduledTaskList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScheduledTask]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScheduledTask]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpScheduledTask]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScheduledTaskList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpScheduledTaskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpScheduledTaskOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpScheduledTaskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCronExpression")
    def reset_cron_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCronExpression", []))

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetMaxCapacity")
    def reset_max_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxCapacity", []))

    @jsii.member(jsii_name="resetMinCapacity")
    def reset_min_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCapacity", []))

    @jsii.member(jsii_name="resetTargetCapacity")
    def reset_target_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="cronExpressionInput")
    def cron_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cronExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="maxCapacityInput")
    def max_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="minCapacityInput")
    def min_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="targetCapacityInput")
    def target_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="taskTypeInput")
    def task_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="cronExpression")
    def cron_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cronExpression"))

    @cron_expression.setter
    def cron_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScheduledTaskOutputReference, "cron_expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cronExpression", value)

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScheduledTaskOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxCapacity"))

    @max_capacity.setter
    def max_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScheduledTaskOutputReference, "max_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="minCapacity")
    def min_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minCapacity"))

    @min_capacity.setter
    def min_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScheduledTaskOutputReference, "min_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="targetCapacity")
    def target_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetCapacity"))

    @target_capacity.setter
    def target_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScheduledTaskOutputReference, "target_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="taskType")
    def task_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskType"))

    @task_type.setter
    def task_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScheduledTaskOutputReference, "task_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupGcpScheduledTask, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupGcpScheduledTask, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupGcpScheduledTask, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpScheduledTaskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpSubnets",
    jsii_struct_bases=[],
    name_mapping={"region": "region", "subnet_names": "subnetNames"},
)
class ElastigroupGcpSubnets:
    def __init__(
        self,
        *,
        region: builtins.str,
        subnet_names: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#region ElastigroupGcp#region}.
        :param subnet_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#subnet_names ElastigroupGcp#subnet_names}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpSubnets.__init__)
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument subnet_names", value=subnet_names, expected_type=type_hints["subnet_names"])
        self._values: typing.Dict[str, typing.Any] = {
            "region": region,
            "subnet_names": subnet_names,
        }

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#region ElastigroupGcp#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_names(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp#subnet_names ElastigroupGcp#subnet_names}.'''
        result = self._values.get("subnet_names")
        assert result is not None, "Required property 'subnet_names' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastigroupGcpSubnets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastigroupGcpSubnetsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpSubnetsList",
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
            type_hints = typing.get_type_hints(ElastigroupGcpSubnetsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ElastigroupGcpSubnetsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastigroupGcpSubnetsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastigroupGcpSubnetsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpSubnetsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpSubnetsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpSubnetsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpSubnets]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpSubnets]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastigroupGcpSubnets]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpSubnetsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastigroupGcpSubnetsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.elastigroupGcp.ElastigroupGcpSubnetsOutputReference",
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
            type_hints = typing.get_type_hints(ElastigroupGcpSubnetsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetNamesInput")
    def subnet_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpSubnetsOutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="subnetNames")
    def subnet_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetNames"))

    @subnet_names.setter
    def subnet_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpSubnetsOutputReference, "subnet_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetNames", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastigroupGcpSubnets, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastigroupGcpSubnets, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastigroupGcpSubnets, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastigroupGcpSubnetsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ElastigroupGcp",
    "ElastigroupGcpBackendServices",
    "ElastigroupGcpBackendServicesList",
    "ElastigroupGcpBackendServicesNamedPorts",
    "ElastigroupGcpBackendServicesNamedPortsList",
    "ElastigroupGcpBackendServicesNamedPortsOutputReference",
    "ElastigroupGcpBackendServicesOutputReference",
    "ElastigroupGcpConfig",
    "ElastigroupGcpDisk",
    "ElastigroupGcpDiskInitializeParams",
    "ElastigroupGcpDiskInitializeParamsList",
    "ElastigroupGcpDiskInitializeParamsOutputReference",
    "ElastigroupGcpDiskList",
    "ElastigroupGcpDiskOutputReference",
    "ElastigroupGcpGpu",
    "ElastigroupGcpGpuList",
    "ElastigroupGcpGpuOutputReference",
    "ElastigroupGcpInstanceTypesCustom",
    "ElastigroupGcpInstanceTypesCustomList",
    "ElastigroupGcpInstanceTypesCustomOutputReference",
    "ElastigroupGcpIntegrationDockerSwarm",
    "ElastigroupGcpIntegrationDockerSwarmOutputReference",
    "ElastigroupGcpIntegrationGke",
    "ElastigroupGcpIntegrationGkeAutoscaleDown",
    "ElastigroupGcpIntegrationGkeAutoscaleDownOutputReference",
    "ElastigroupGcpIntegrationGkeAutoscaleHeadroom",
    "ElastigroupGcpIntegrationGkeAutoscaleHeadroomOutputReference",
    "ElastigroupGcpIntegrationGkeAutoscaleLabels",
    "ElastigroupGcpIntegrationGkeAutoscaleLabelsList",
    "ElastigroupGcpIntegrationGkeAutoscaleLabelsOutputReference",
    "ElastigroupGcpIntegrationGkeOutputReference",
    "ElastigroupGcpLabels",
    "ElastigroupGcpLabelsList",
    "ElastigroupGcpLabelsOutputReference",
    "ElastigroupGcpMetadata",
    "ElastigroupGcpMetadataList",
    "ElastigroupGcpMetadataOutputReference",
    "ElastigroupGcpNetworkInterface",
    "ElastigroupGcpNetworkInterfaceAccessConfigs",
    "ElastigroupGcpNetworkInterfaceAccessConfigsList",
    "ElastigroupGcpNetworkInterfaceAccessConfigsOutputReference",
    "ElastigroupGcpNetworkInterfaceAliasIpRanges",
    "ElastigroupGcpNetworkInterfaceAliasIpRangesList",
    "ElastigroupGcpNetworkInterfaceAliasIpRangesOutputReference",
    "ElastigroupGcpNetworkInterfaceList",
    "ElastigroupGcpNetworkInterfaceOutputReference",
    "ElastigroupGcpScalingDownPolicy",
    "ElastigroupGcpScalingDownPolicyDimensions",
    "ElastigroupGcpScalingDownPolicyDimensionsList",
    "ElastigroupGcpScalingDownPolicyDimensionsOutputReference",
    "ElastigroupGcpScalingDownPolicyList",
    "ElastigroupGcpScalingDownPolicyOutputReference",
    "ElastigroupGcpScalingUpPolicy",
    "ElastigroupGcpScalingUpPolicyDimensions",
    "ElastigroupGcpScalingUpPolicyDimensionsList",
    "ElastigroupGcpScalingUpPolicyDimensionsOutputReference",
    "ElastigroupGcpScalingUpPolicyList",
    "ElastigroupGcpScalingUpPolicyOutputReference",
    "ElastigroupGcpScheduledTask",
    "ElastigroupGcpScheduledTaskList",
    "ElastigroupGcpScheduledTaskOutputReference",
    "ElastigroupGcpSubnets",
    "ElastigroupGcpSubnetsList",
    "ElastigroupGcpSubnetsOutputReference",
]

publication.publish()
