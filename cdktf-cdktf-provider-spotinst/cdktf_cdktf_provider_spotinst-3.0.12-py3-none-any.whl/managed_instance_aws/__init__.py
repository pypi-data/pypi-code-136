'''
# `spotinst_managed_instance_aws`

Refer to the Terraform Registory for docs: [`spotinst_managed_instance_aws`](https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws).
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


class ManagedInstanceAws(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAws",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws spotinst_managed_instance_aws}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        image_id: builtins.str,
        instance_types: typing.Sequence[builtins.str],
        name: builtins.str,
        persist_block_devices: typing.Union[builtins.bool, cdktf.IResolvable],
        product: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        auto_healing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        block_device_mappings: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsBlockDeviceMappings", typing.Dict[str, typing.Any]]]]] = None,
        block_devices_mode: typing.Optional[builtins.str] = None,
        cpu_credits: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        draining_timeout: typing.Optional[jsii.Number] = None,
        ebs_optimized: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        elastic_ip: typing.Optional[builtins.str] = None,
        enable_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fall_back_to_od: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        grace_period: typing.Optional[jsii.Number] = None,
        health_check_type: typing.Optional[builtins.str] = None,
        iam_instance_profile: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        integration_route53: typing.Optional[typing.Union["ManagedInstanceAwsIntegrationRoute53", typing.Dict[str, typing.Any]]] = None,
        key_pair: typing.Optional[builtins.str] = None,
        life_cycle: typing.Optional[builtins.str] = None,
        load_balancers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsLoadBalancers", typing.Dict[str, typing.Any]]]]] = None,
        managed_instance_action: typing.Optional[typing.Union["ManagedInstanceAwsManagedInstanceAction", typing.Dict[str, typing.Any]]] = None,
        minimum_instance_lifetime: typing.Optional[jsii.Number] = None,
        network_interface: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsNetworkInterface", typing.Dict[str, typing.Any]]]]] = None,
        optimization_windows: typing.Optional[typing.Sequence[builtins.str]] = None,
        orientation: typing.Optional[builtins.str] = None,
        persist_private_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        persist_root_device: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        placement_tenancy: typing.Optional[builtins.str] = None,
        preferred_type: typing.Optional[builtins.str] = None,
        private_ip: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        resource_tag_specification: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsResourceTagSpecification", typing.Dict[str, typing.Any]]]]] = None,
        revert_to_spot: typing.Optional[typing.Union["ManagedInstanceAwsRevertToSpot", typing.Dict[str, typing.Any]]] = None,
        scheduled_task: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsScheduledTask", typing.Dict[str, typing.Any]]]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        shutdown_script: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsTags", typing.Dict[str, typing.Any]]]]] = None,
        unhealthy_duration: typing.Optional[jsii.Number] = None,
        user_data: typing.Optional[builtins.str] = None,
        utilize_reserved_instances: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws spotinst_managed_instance_aws} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#image_id ManagedInstanceAws#image_id}.
        :param instance_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#instance_types ManagedInstanceAws#instance_types}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#name ManagedInstanceAws#name}.
        :param persist_block_devices: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#persist_block_devices ManagedInstanceAws#persist_block_devices}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#product ManagedInstanceAws#product}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#subnet_ids ManagedInstanceAws#subnet_ids}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#vpc_id ManagedInstanceAws#vpc_id}.
        :param auto_healing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#auto_healing ManagedInstanceAws#auto_healing}.
        :param block_device_mappings: block_device_mappings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#block_device_mappings ManagedInstanceAws#block_device_mappings}
        :param block_devices_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#block_devices_mode ManagedInstanceAws#block_devices_mode}.
        :param cpu_credits: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#cpu_credits ManagedInstanceAws#cpu_credits}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#description ManagedInstanceAws#description}.
        :param draining_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#draining_timeout ManagedInstanceAws#draining_timeout}.
        :param ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#ebs_optimized ManagedInstanceAws#ebs_optimized}.
        :param elastic_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#elastic_ip ManagedInstanceAws#elastic_ip}.
        :param enable_monitoring: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#enable_monitoring ManagedInstanceAws#enable_monitoring}.
        :param fall_back_to_od: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#fall_back_to_od ManagedInstanceAws#fall_back_to_od}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#grace_period ManagedInstanceAws#grace_period}.
        :param health_check_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#health_check_type ManagedInstanceAws#health_check_type}.
        :param iam_instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#iam_instance_profile ManagedInstanceAws#iam_instance_profile}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#id ManagedInstanceAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param integration_route53: integration_route53 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#integration_route53 ManagedInstanceAws#integration_route53}
        :param key_pair: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#key_pair ManagedInstanceAws#key_pair}.
        :param life_cycle: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#life_cycle ManagedInstanceAws#life_cycle}.
        :param load_balancers: load_balancers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#load_balancers ManagedInstanceAws#load_balancers}
        :param managed_instance_action: managed_instance_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#managed_instance_action ManagedInstanceAws#managed_instance_action}
        :param minimum_instance_lifetime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#minimum_instance_lifetime ManagedInstanceAws#minimum_instance_lifetime}.
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#network_interface ManagedInstanceAws#network_interface}
        :param optimization_windows: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#optimization_windows ManagedInstanceAws#optimization_windows}.
        :param orientation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#orientation ManagedInstanceAws#orientation}.
        :param persist_private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#persist_private_ip ManagedInstanceAws#persist_private_ip}.
        :param persist_root_device: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#persist_root_device ManagedInstanceAws#persist_root_device}.
        :param placement_tenancy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#placement_tenancy ManagedInstanceAws#placement_tenancy}.
        :param preferred_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#preferred_type ManagedInstanceAws#preferred_type}.
        :param private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#private_ip ManagedInstanceAws#private_ip}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#region ManagedInstanceAws#region}.
        :param resource_tag_specification: resource_tag_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#resource_tag_specification ManagedInstanceAws#resource_tag_specification}
        :param revert_to_spot: revert_to_spot block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#revert_to_spot ManagedInstanceAws#revert_to_spot}
        :param scheduled_task: scheduled_task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#scheduled_task ManagedInstanceAws#scheduled_task}
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#security_group_ids ManagedInstanceAws#security_group_ids}.
        :param shutdown_script: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#shutdown_script ManagedInstanceAws#shutdown_script}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#tags ManagedInstanceAws#tags}
        :param unhealthy_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#unhealthy_duration ManagedInstanceAws#unhealthy_duration}.
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#user_data ManagedInstanceAws#user_data}.
        :param utilize_reserved_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#utilize_reserved_instances ManagedInstanceAws#utilize_reserved_instances}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAws.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ManagedInstanceAwsConfig(
            image_id=image_id,
            instance_types=instance_types,
            name=name,
            persist_block_devices=persist_block_devices,
            product=product,
            subnet_ids=subnet_ids,
            vpc_id=vpc_id,
            auto_healing=auto_healing,
            block_device_mappings=block_device_mappings,
            block_devices_mode=block_devices_mode,
            cpu_credits=cpu_credits,
            description=description,
            draining_timeout=draining_timeout,
            ebs_optimized=ebs_optimized,
            elastic_ip=elastic_ip,
            enable_monitoring=enable_monitoring,
            fall_back_to_od=fall_back_to_od,
            grace_period=grace_period,
            health_check_type=health_check_type,
            iam_instance_profile=iam_instance_profile,
            id=id,
            integration_route53=integration_route53,
            key_pair=key_pair,
            life_cycle=life_cycle,
            load_balancers=load_balancers,
            managed_instance_action=managed_instance_action,
            minimum_instance_lifetime=minimum_instance_lifetime,
            network_interface=network_interface,
            optimization_windows=optimization_windows,
            orientation=orientation,
            persist_private_ip=persist_private_ip,
            persist_root_device=persist_root_device,
            placement_tenancy=placement_tenancy,
            preferred_type=preferred_type,
            private_ip=private_ip,
            region=region,
            resource_tag_specification=resource_tag_specification,
            revert_to_spot=revert_to_spot,
            scheduled_task=scheduled_task,
            security_group_ids=security_group_ids,
            shutdown_script=shutdown_script,
            tags=tags,
            unhealthy_duration=unhealthy_duration,
            user_data=user_data,
            utilize_reserved_instances=utilize_reserved_instances,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBlockDeviceMappings")
    def put_block_device_mappings(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsBlockDeviceMappings", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAws.put_block_device_mappings)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBlockDeviceMappings", [value]))

    @jsii.member(jsii_name="putIntegrationRoute53")
    def put_integration_route53(
        self,
        *,
        domains: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsIntegrationRoute53Domains", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param domains: domains block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#domains ManagedInstanceAws#domains}
        '''
        value = ManagedInstanceAwsIntegrationRoute53(domains=domains)

        return typing.cast(None, jsii.invoke(self, "putIntegrationRoute53", [value]))

    @jsii.member(jsii_name="putLoadBalancers")
    def put_load_balancers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsLoadBalancers", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAws.put_load_balancers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLoadBalancers", [value]))

    @jsii.member(jsii_name="putManagedInstanceAction")
    def put_managed_instance_action(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#type ManagedInstanceAws#type}.
        '''
        value = ManagedInstanceAwsManagedInstanceAction(type=type)

        return typing.cast(None, jsii.invoke(self, "putManagedInstanceAction", [value]))

    @jsii.member(jsii_name="putNetworkInterface")
    def put_network_interface(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsNetworkInterface", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAws.put_network_interface)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkInterface", [value]))

    @jsii.member(jsii_name="putResourceTagSpecification")
    def put_resource_tag_specification(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsResourceTagSpecification", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAws.put_resource_tag_specification)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResourceTagSpecification", [value]))

    @jsii.member(jsii_name="putRevertToSpot")
    def put_revert_to_spot(self, *, perform_at: builtins.str) -> None:
        '''
        :param perform_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#perform_at ManagedInstanceAws#perform_at}.
        '''
        value = ManagedInstanceAwsRevertToSpot(perform_at=perform_at)

        return typing.cast(None, jsii.invoke(self, "putRevertToSpot", [value]))

    @jsii.member(jsii_name="putScheduledTask")
    def put_scheduled_task(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsScheduledTask", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAws.put_scheduled_task)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScheduledTask", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsTags", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAws.put_tags)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetAutoHealing")
    def reset_auto_healing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoHealing", []))

    @jsii.member(jsii_name="resetBlockDeviceMappings")
    def reset_block_device_mappings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockDeviceMappings", []))

    @jsii.member(jsii_name="resetBlockDevicesMode")
    def reset_block_devices_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockDevicesMode", []))

    @jsii.member(jsii_name="resetCpuCredits")
    def reset_cpu_credits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuCredits", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDrainingTimeout")
    def reset_draining_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDrainingTimeout", []))

    @jsii.member(jsii_name="resetEbsOptimized")
    def reset_ebs_optimized(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsOptimized", []))

    @jsii.member(jsii_name="resetElasticIp")
    def reset_elastic_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticIp", []))

    @jsii.member(jsii_name="resetEnableMonitoring")
    def reset_enable_monitoring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableMonitoring", []))

    @jsii.member(jsii_name="resetFallBackToOd")
    def reset_fall_back_to_od(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFallBackToOd", []))

    @jsii.member(jsii_name="resetGracePeriod")
    def reset_grace_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGracePeriod", []))

    @jsii.member(jsii_name="resetHealthCheckType")
    def reset_health_check_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckType", []))

    @jsii.member(jsii_name="resetIamInstanceProfile")
    def reset_iam_instance_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamInstanceProfile", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIntegrationRoute53")
    def reset_integration_route53(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntegrationRoute53", []))

    @jsii.member(jsii_name="resetKeyPair")
    def reset_key_pair(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyPair", []))

    @jsii.member(jsii_name="resetLifeCycle")
    def reset_life_cycle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifeCycle", []))

    @jsii.member(jsii_name="resetLoadBalancers")
    def reset_load_balancers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancers", []))

    @jsii.member(jsii_name="resetManagedInstanceAction")
    def reset_managed_instance_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedInstanceAction", []))

    @jsii.member(jsii_name="resetMinimumInstanceLifetime")
    def reset_minimum_instance_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumInstanceLifetime", []))

    @jsii.member(jsii_name="resetNetworkInterface")
    def reset_network_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkInterface", []))

    @jsii.member(jsii_name="resetOptimizationWindows")
    def reset_optimization_windows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptimizationWindows", []))

    @jsii.member(jsii_name="resetOrientation")
    def reset_orientation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrientation", []))

    @jsii.member(jsii_name="resetPersistPrivateIp")
    def reset_persist_private_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPersistPrivateIp", []))

    @jsii.member(jsii_name="resetPersistRootDevice")
    def reset_persist_root_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPersistRootDevice", []))

    @jsii.member(jsii_name="resetPlacementTenancy")
    def reset_placement_tenancy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacementTenancy", []))

    @jsii.member(jsii_name="resetPreferredType")
    def reset_preferred_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredType", []))

    @jsii.member(jsii_name="resetPrivateIp")
    def reset_private_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIp", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetResourceTagSpecification")
    def reset_resource_tag_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceTagSpecification", []))

    @jsii.member(jsii_name="resetRevertToSpot")
    def reset_revert_to_spot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRevertToSpot", []))

    @jsii.member(jsii_name="resetScheduledTask")
    def reset_scheduled_task(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduledTask", []))

    @jsii.member(jsii_name="resetSecurityGroupIds")
    def reset_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroupIds", []))

    @jsii.member(jsii_name="resetShutdownScript")
    def reset_shutdown_script(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShutdownScript", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetUnhealthyDuration")
    def reset_unhealthy_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnhealthyDuration", []))

    @jsii.member(jsii_name="resetUserData")
    def reset_user_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserData", []))

    @jsii.member(jsii_name="resetUtilizeReservedInstances")
    def reset_utilize_reserved_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUtilizeReservedInstances", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="blockDeviceMappings")
    def block_device_mappings(self) -> "ManagedInstanceAwsBlockDeviceMappingsList":
        return typing.cast("ManagedInstanceAwsBlockDeviceMappingsList", jsii.get(self, "blockDeviceMappings"))

    @builtins.property
    @jsii.member(jsii_name="integrationRoute53")
    def integration_route53(
        self,
    ) -> "ManagedInstanceAwsIntegrationRoute53OutputReference":
        return typing.cast("ManagedInstanceAwsIntegrationRoute53OutputReference", jsii.get(self, "integrationRoute53"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancers")
    def load_balancers(self) -> "ManagedInstanceAwsLoadBalancersList":
        return typing.cast("ManagedInstanceAwsLoadBalancersList", jsii.get(self, "loadBalancers"))

    @builtins.property
    @jsii.member(jsii_name="managedInstanceAction")
    def managed_instance_action(
        self,
    ) -> "ManagedInstanceAwsManagedInstanceActionOutputReference":
        return typing.cast("ManagedInstanceAwsManagedInstanceActionOutputReference", jsii.get(self, "managedInstanceAction"))

    @builtins.property
    @jsii.member(jsii_name="networkInterface")
    def network_interface(self) -> "ManagedInstanceAwsNetworkInterfaceList":
        return typing.cast("ManagedInstanceAwsNetworkInterfaceList", jsii.get(self, "networkInterface"))

    @builtins.property
    @jsii.member(jsii_name="resourceTagSpecification")
    def resource_tag_specification(
        self,
    ) -> "ManagedInstanceAwsResourceTagSpecificationList":
        return typing.cast("ManagedInstanceAwsResourceTagSpecificationList", jsii.get(self, "resourceTagSpecification"))

    @builtins.property
    @jsii.member(jsii_name="revertToSpot")
    def revert_to_spot(self) -> "ManagedInstanceAwsRevertToSpotOutputReference":
        return typing.cast("ManagedInstanceAwsRevertToSpotOutputReference", jsii.get(self, "revertToSpot"))

    @builtins.property
    @jsii.member(jsii_name="scheduledTask")
    def scheduled_task(self) -> "ManagedInstanceAwsScheduledTaskList":
        return typing.cast("ManagedInstanceAwsScheduledTaskList", jsii.get(self, "scheduledTask"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "ManagedInstanceAwsTagsList":
        return typing.cast("ManagedInstanceAwsTagsList", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="autoHealingInput")
    def auto_healing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoHealingInput"))

    @builtins.property
    @jsii.member(jsii_name="blockDeviceMappingsInput")
    def block_device_mappings_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsBlockDeviceMappings"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsBlockDeviceMappings"]]], jsii.get(self, "blockDeviceMappingsInput"))

    @builtins.property
    @jsii.member(jsii_name="blockDevicesModeInput")
    def block_devices_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blockDevicesModeInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuCreditsInput")
    def cpu_credits_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuCreditsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="drainingTimeoutInput")
    def draining_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "drainingTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsOptimizedInput")
    def ebs_optimized_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ebsOptimizedInput"))

    @builtins.property
    @jsii.member(jsii_name="elasticIpInput")
    def elastic_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elasticIpInput"))

    @builtins.property
    @jsii.member(jsii_name="enableMonitoringInput")
    def enable_monitoring_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableMonitoringInput"))

    @builtins.property
    @jsii.member(jsii_name="fallBackToOdInput")
    def fall_back_to_od_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fallBackToOdInput"))

    @builtins.property
    @jsii.member(jsii_name="gracePeriodInput")
    def grace_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gracePeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckTypeInput")
    def health_check_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfileInput")
    def iam_instance_profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamInstanceProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="imageIdInput")
    def image_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageIdInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypesInput")
    def instance_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instanceTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationRoute53Input")
    def integration_route53_input(
        self,
    ) -> typing.Optional["ManagedInstanceAwsIntegrationRoute53"]:
        return typing.cast(typing.Optional["ManagedInstanceAwsIntegrationRoute53"], jsii.get(self, "integrationRoute53Input"))

    @builtins.property
    @jsii.member(jsii_name="keyPairInput")
    def key_pair_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyPairInput"))

    @builtins.property
    @jsii.member(jsii_name="lifeCycleInput")
    def life_cycle_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifeCycleInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancersInput")
    def load_balancers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsLoadBalancers"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsLoadBalancers"]]], jsii.get(self, "loadBalancersInput"))

    @builtins.property
    @jsii.member(jsii_name="managedInstanceActionInput")
    def managed_instance_action_input(
        self,
    ) -> typing.Optional["ManagedInstanceAwsManagedInstanceAction"]:
        return typing.cast(typing.Optional["ManagedInstanceAwsManagedInstanceAction"], jsii.get(self, "managedInstanceActionInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumInstanceLifetimeInput")
    def minimum_instance_lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumInstanceLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceInput")
    def network_interface_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsNetworkInterface"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsNetworkInterface"]]], jsii.get(self, "networkInterfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="optimizationWindowsInput")
    def optimization_windows_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "optimizationWindowsInput"))

    @builtins.property
    @jsii.member(jsii_name="orientationInput")
    def orientation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "orientationInput"))

    @builtins.property
    @jsii.member(jsii_name="persistBlockDevicesInput")
    def persist_block_devices_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "persistBlockDevicesInput"))

    @builtins.property
    @jsii.member(jsii_name="persistPrivateIpInput")
    def persist_private_ip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "persistPrivateIpInput"))

    @builtins.property
    @jsii.member(jsii_name="persistRootDeviceInput")
    def persist_root_device_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "persistRootDeviceInput"))

    @builtins.property
    @jsii.member(jsii_name="placementTenancyInput")
    def placement_tenancy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "placementTenancyInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredTypeInput")
    def preferred_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpInput")
    def private_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpInput"))

    @builtins.property
    @jsii.member(jsii_name="productInput")
    def product_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "productInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceTagSpecificationInput")
    def resource_tag_specification_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsResourceTagSpecification"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsResourceTagSpecification"]]], jsii.get(self, "resourceTagSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="revertToSpotInput")
    def revert_to_spot_input(self) -> typing.Optional["ManagedInstanceAwsRevertToSpot"]:
        return typing.cast(typing.Optional["ManagedInstanceAwsRevertToSpot"], jsii.get(self, "revertToSpotInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduledTaskInput")
    def scheduled_task_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsScheduledTask"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsScheduledTask"]]], jsii.get(self, "scheduledTaskInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="shutdownScriptInput")
    def shutdown_script_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shutdownScriptInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsTags"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsTags"]]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="unhealthyDurationInput")
    def unhealthy_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "unhealthyDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="userDataInput")
    def user_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userDataInput"))

    @builtins.property
    @jsii.member(jsii_name="utilizeReservedInstancesInput")
    def utilize_reserved_instances_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "utilizeReservedInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcIdInput")
    def vpc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcIdInput"))

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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "auto_healing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoHealing", value)

    @builtins.property
    @jsii.member(jsii_name="blockDevicesMode")
    def block_devices_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "blockDevicesMode"))

    @block_devices_mode.setter
    def block_devices_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "block_devices_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockDevicesMode", value)

    @builtins.property
    @jsii.member(jsii_name="cpuCredits")
    def cpu_credits(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpuCredits"))

    @cpu_credits.setter
    def cpu_credits(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "cpu_credits").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuCredits", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="drainingTimeout")
    def draining_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "drainingTimeout"))

    @draining_timeout.setter
    def draining_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "draining_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "drainingTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="ebsOptimized")
    def ebs_optimized(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ebsOptimized"))

    @ebs_optimized.setter
    def ebs_optimized(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "ebs_optimized").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsOptimized", value)

    @builtins.property
    @jsii.member(jsii_name="elasticIp")
    def elastic_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticIp"))

    @elastic_ip.setter
    def elastic_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "elastic_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticIp", value)

    @builtins.property
    @jsii.member(jsii_name="enableMonitoring")
    def enable_monitoring(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableMonitoring"))

    @enable_monitoring.setter
    def enable_monitoring(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "enable_monitoring").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableMonitoring", value)

    @builtins.property
    @jsii.member(jsii_name="fallBackToOd")
    def fall_back_to_od(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fallBackToOd"))

    @fall_back_to_od.setter
    def fall_back_to_od(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "fall_back_to_od").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fallBackToOd", value)

    @builtins.property
    @jsii.member(jsii_name="gracePeriod")
    def grace_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gracePeriod"))

    @grace_period.setter
    def grace_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "grace_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gracePeriod", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckType")
    def health_check_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckType"))

    @health_check_type.setter
    def health_check_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "health_check_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckType", value)

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfile")
    def iam_instance_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamInstanceProfile"))

    @iam_instance_profile.setter
    def iam_instance_profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "iam_instance_profile").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamInstanceProfile", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="imageId")
    def image_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageId"))

    @image_id.setter
    def image_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "image_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageId", value)

    @builtins.property
    @jsii.member(jsii_name="instanceTypes")
    def instance_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceTypes"))

    @instance_types.setter
    def instance_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "instance_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceTypes", value)

    @builtins.property
    @jsii.member(jsii_name="keyPair")
    def key_pair(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyPair"))

    @key_pair.setter
    def key_pair(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "key_pair").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyPair", value)

    @builtins.property
    @jsii.member(jsii_name="lifeCycle")
    def life_cycle(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifeCycle"))

    @life_cycle.setter
    def life_cycle(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "life_cycle").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifeCycle", value)

    @builtins.property
    @jsii.member(jsii_name="minimumInstanceLifetime")
    def minimum_instance_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumInstanceLifetime"))

    @minimum_instance_lifetime.setter
    def minimum_instance_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "minimum_instance_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumInstanceLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="optimizationWindows")
    def optimization_windows(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "optimizationWindows"))

    @optimization_windows.setter
    def optimization_windows(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "optimization_windows").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optimizationWindows", value)

    @builtins.property
    @jsii.member(jsii_name="orientation")
    def orientation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "orientation"))

    @orientation.setter
    def orientation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "orientation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "orientation", value)

    @builtins.property
    @jsii.member(jsii_name="persistBlockDevices")
    def persist_block_devices(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "persistBlockDevices"))

    @persist_block_devices.setter
    def persist_block_devices(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "persist_block_devices").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "persistBlockDevices", value)

    @builtins.property
    @jsii.member(jsii_name="persistPrivateIp")
    def persist_private_ip(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "persistPrivateIp"))

    @persist_private_ip.setter
    def persist_private_ip(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "persist_private_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "persistPrivateIp", value)

    @builtins.property
    @jsii.member(jsii_name="persistRootDevice")
    def persist_root_device(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "persistRootDevice"))

    @persist_root_device.setter
    def persist_root_device(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "persist_root_device").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "persistRootDevice", value)

    @builtins.property
    @jsii.member(jsii_name="placementTenancy")
    def placement_tenancy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "placementTenancy"))

    @placement_tenancy.setter
    def placement_tenancy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "placement_tenancy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placementTenancy", value)

    @builtins.property
    @jsii.member(jsii_name="preferredType")
    def preferred_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferredType"))

    @preferred_type.setter
    def preferred_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "preferred_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredType", value)

    @builtins.property
    @jsii.member(jsii_name="privateIp")
    def private_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIp"))

    @private_ip.setter
    def private_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "private_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIp", value)

    @builtins.property
    @jsii.member(jsii_name="product")
    def product(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "product"))

    @product.setter
    def product(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "product").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "product", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "security_group_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="shutdownScript")
    def shutdown_script(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shutdownScript"))

    @shutdown_script.setter
    def shutdown_script(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "shutdown_script").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shutdownScript", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "subnet_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="unhealthyDuration")
    def unhealthy_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unhealthyDuration"))

    @unhealthy_duration.setter
    def unhealthy_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "unhealthy_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unhealthyDuration", value)

    @builtins.property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userData"))

    @user_data.setter
    def user_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "user_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userData", value)

    @builtins.property
    @jsii.member(jsii_name="utilizeReservedInstances")
    def utilize_reserved_instances(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "utilizeReservedInstances"))

    @utilize_reserved_instances.setter
    def utilize_reserved_instances(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "utilize_reserved_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "utilizeReservedInstances", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAws, "vpc_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsBlockDeviceMappings",
    jsii_struct_bases=[],
    name_mapping={"device_name": "deviceName", "ebs": "ebs"},
)
class ManagedInstanceAwsBlockDeviceMappings:
    def __init__(
        self,
        *,
        device_name: builtins.str,
        ebs: typing.Optional[typing.Union["ManagedInstanceAwsBlockDeviceMappingsEbs", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param device_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#device_name ManagedInstanceAws#device_name}.
        :param ebs: ebs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#ebs ManagedInstanceAws#ebs}
        '''
        if isinstance(ebs, dict):
            ebs = ManagedInstanceAwsBlockDeviceMappingsEbs(**ebs)
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsBlockDeviceMappings.__init__)
            check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
            check_type(argname="argument ebs", value=ebs, expected_type=type_hints["ebs"])
        self._values: typing.Dict[str, typing.Any] = {
            "device_name": device_name,
        }
        if ebs is not None:
            self._values["ebs"] = ebs

    @builtins.property
    def device_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#device_name ManagedInstanceAws#device_name}.'''
        result = self._values.get("device_name")
        assert result is not None, "Required property 'device_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ebs(self) -> typing.Optional["ManagedInstanceAwsBlockDeviceMappingsEbs"]:
        '''ebs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#ebs ManagedInstanceAws#ebs}
        '''
        result = self._values.get("ebs")
        return typing.cast(typing.Optional["ManagedInstanceAwsBlockDeviceMappingsEbs"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedInstanceAwsBlockDeviceMappings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsBlockDeviceMappingsEbs",
    jsii_struct_bases=[],
    name_mapping={
        "delete_on_termination": "deleteOnTermination",
        "iops": "iops",
        "throughput": "throughput",
        "volume_size": "volumeSize",
        "volume_type": "volumeType",
    },
)
class ManagedInstanceAwsBlockDeviceMappingsEbs:
    def __init__(
        self,
        *,
        delete_on_termination: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        iops: typing.Optional[jsii.Number] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#delete_on_termination ManagedInstanceAws#delete_on_termination}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#iops ManagedInstanceAws#iops}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#throughput ManagedInstanceAws#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#volume_size ManagedInstanceAws#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#volume_type ManagedInstanceAws#volume_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsBlockDeviceMappingsEbs.__init__)
            check_type(argname="argument delete_on_termination", value=delete_on_termination, expected_type=type_hints["delete_on_termination"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if delete_on_termination is not None:
            self._values["delete_on_termination"] = delete_on_termination
        if iops is not None:
            self._values["iops"] = iops
        if throughput is not None:
            self._values["throughput"] = throughput
        if volume_size is not None:
            self._values["volume_size"] = volume_size
        if volume_type is not None:
            self._values["volume_type"] = volume_type

    @builtins.property
    def delete_on_termination(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#delete_on_termination ManagedInstanceAws#delete_on_termination}.'''
        result = self._values.get("delete_on_termination")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#iops ManagedInstanceAws#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#throughput ManagedInstanceAws#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#volume_size ManagedInstanceAws#volume_size}.'''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#volume_type ManagedInstanceAws#volume_type}.'''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedInstanceAwsBlockDeviceMappingsEbs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedInstanceAwsBlockDeviceMappingsEbsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsBlockDeviceMappingsEbsOutputReference",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsBlockDeviceMappingsEbsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDeleteOnTermination")
    def reset_delete_on_termination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteOnTermination", []))

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetThroughput")
    def reset_throughput(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThroughput", []))

    @jsii.member(jsii_name="resetVolumeSize")
    def reset_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeSize", []))

    @jsii.member(jsii_name="resetVolumeType")
    def reset_volume_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeType", []))

    @builtins.property
    @jsii.member(jsii_name="deleteOnTerminationInput")
    def delete_on_termination_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deleteOnTerminationInput"))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="throughputInput")
    def throughput_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "throughputInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeSizeInput")
    def volume_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeTypeInput")
    def volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteOnTermination")
    def delete_on_termination(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deleteOnTermination"))

    @delete_on_termination.setter
    def delete_on_termination(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsBlockDeviceMappingsEbsOutputReference, "delete_on_termination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteOnTermination", value)

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsBlockDeviceMappingsEbsOutputReference, "iops").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsBlockDeviceMappingsEbsOutputReference, "throughput").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value)

    @builtins.property
    @jsii.member(jsii_name="volumeSize")
    def volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumeSize"))

    @volume_size.setter
    def volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsBlockDeviceMappingsEbsOutputReference, "volume_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsBlockDeviceMappingsEbsOutputReference, "volume_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ManagedInstanceAwsBlockDeviceMappingsEbs]:
        return typing.cast(typing.Optional[ManagedInstanceAwsBlockDeviceMappingsEbs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedInstanceAwsBlockDeviceMappingsEbs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsBlockDeviceMappingsEbsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManagedInstanceAwsBlockDeviceMappingsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsBlockDeviceMappingsList",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsBlockDeviceMappingsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ManagedInstanceAwsBlockDeviceMappingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsBlockDeviceMappingsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ManagedInstanceAwsBlockDeviceMappingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsBlockDeviceMappingsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsBlockDeviceMappingsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsBlockDeviceMappingsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsBlockDeviceMappings]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsBlockDeviceMappings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsBlockDeviceMappings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsBlockDeviceMappingsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManagedInstanceAwsBlockDeviceMappingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsBlockDeviceMappingsOutputReference",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsBlockDeviceMappingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putEbs")
    def put_ebs(
        self,
        *,
        delete_on_termination: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        iops: typing.Optional[jsii.Number] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#delete_on_termination ManagedInstanceAws#delete_on_termination}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#iops ManagedInstanceAws#iops}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#throughput ManagedInstanceAws#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#volume_size ManagedInstanceAws#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#volume_type ManagedInstanceAws#volume_type}.
        '''
        value = ManagedInstanceAwsBlockDeviceMappingsEbs(
            delete_on_termination=delete_on_termination,
            iops=iops,
            throughput=throughput,
            volume_size=volume_size,
            volume_type=volume_type,
        )

        return typing.cast(None, jsii.invoke(self, "putEbs", [value]))

    @jsii.member(jsii_name="resetEbs")
    def reset_ebs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbs", []))

    @builtins.property
    @jsii.member(jsii_name="ebs")
    def ebs(self) -> ManagedInstanceAwsBlockDeviceMappingsEbsOutputReference:
        return typing.cast(ManagedInstanceAwsBlockDeviceMappingsEbsOutputReference, jsii.get(self, "ebs"))

    @builtins.property
    @jsii.member(jsii_name="deviceNameInput")
    def device_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsInput")
    def ebs_input(self) -> typing.Optional[ManagedInstanceAwsBlockDeviceMappingsEbs]:
        return typing.cast(typing.Optional[ManagedInstanceAwsBlockDeviceMappingsEbs], jsii.get(self, "ebsInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceName"))

    @device_name.setter
    def device_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsBlockDeviceMappingsOutputReference, "device_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ManagedInstanceAwsBlockDeviceMappings, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ManagedInstanceAwsBlockDeviceMappings, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ManagedInstanceAwsBlockDeviceMappings, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsBlockDeviceMappingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "image_id": "imageId",
        "instance_types": "instanceTypes",
        "name": "name",
        "persist_block_devices": "persistBlockDevices",
        "product": "product",
        "subnet_ids": "subnetIds",
        "vpc_id": "vpcId",
        "auto_healing": "autoHealing",
        "block_device_mappings": "blockDeviceMappings",
        "block_devices_mode": "blockDevicesMode",
        "cpu_credits": "cpuCredits",
        "description": "description",
        "draining_timeout": "drainingTimeout",
        "ebs_optimized": "ebsOptimized",
        "elastic_ip": "elasticIp",
        "enable_monitoring": "enableMonitoring",
        "fall_back_to_od": "fallBackToOd",
        "grace_period": "gracePeriod",
        "health_check_type": "healthCheckType",
        "iam_instance_profile": "iamInstanceProfile",
        "id": "id",
        "integration_route53": "integrationRoute53",
        "key_pair": "keyPair",
        "life_cycle": "lifeCycle",
        "load_balancers": "loadBalancers",
        "managed_instance_action": "managedInstanceAction",
        "minimum_instance_lifetime": "minimumInstanceLifetime",
        "network_interface": "networkInterface",
        "optimization_windows": "optimizationWindows",
        "orientation": "orientation",
        "persist_private_ip": "persistPrivateIp",
        "persist_root_device": "persistRootDevice",
        "placement_tenancy": "placementTenancy",
        "preferred_type": "preferredType",
        "private_ip": "privateIp",
        "region": "region",
        "resource_tag_specification": "resourceTagSpecification",
        "revert_to_spot": "revertToSpot",
        "scheduled_task": "scheduledTask",
        "security_group_ids": "securityGroupIds",
        "shutdown_script": "shutdownScript",
        "tags": "tags",
        "unhealthy_duration": "unhealthyDuration",
        "user_data": "userData",
        "utilize_reserved_instances": "utilizeReservedInstances",
    },
)
class ManagedInstanceAwsConfig(cdktf.TerraformMetaArguments):
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
        image_id: builtins.str,
        instance_types: typing.Sequence[builtins.str],
        name: builtins.str,
        persist_block_devices: typing.Union[builtins.bool, cdktf.IResolvable],
        product: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        auto_healing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        block_device_mappings: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ManagedInstanceAwsBlockDeviceMappings, typing.Dict[str, typing.Any]]]]] = None,
        block_devices_mode: typing.Optional[builtins.str] = None,
        cpu_credits: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        draining_timeout: typing.Optional[jsii.Number] = None,
        ebs_optimized: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        elastic_ip: typing.Optional[builtins.str] = None,
        enable_monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fall_back_to_od: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        grace_period: typing.Optional[jsii.Number] = None,
        health_check_type: typing.Optional[builtins.str] = None,
        iam_instance_profile: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        integration_route53: typing.Optional[typing.Union["ManagedInstanceAwsIntegrationRoute53", typing.Dict[str, typing.Any]]] = None,
        key_pair: typing.Optional[builtins.str] = None,
        life_cycle: typing.Optional[builtins.str] = None,
        load_balancers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsLoadBalancers", typing.Dict[str, typing.Any]]]]] = None,
        managed_instance_action: typing.Optional[typing.Union["ManagedInstanceAwsManagedInstanceAction", typing.Dict[str, typing.Any]]] = None,
        minimum_instance_lifetime: typing.Optional[jsii.Number] = None,
        network_interface: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsNetworkInterface", typing.Dict[str, typing.Any]]]]] = None,
        optimization_windows: typing.Optional[typing.Sequence[builtins.str]] = None,
        orientation: typing.Optional[builtins.str] = None,
        persist_private_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        persist_root_device: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        placement_tenancy: typing.Optional[builtins.str] = None,
        preferred_type: typing.Optional[builtins.str] = None,
        private_ip: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        resource_tag_specification: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsResourceTagSpecification", typing.Dict[str, typing.Any]]]]] = None,
        revert_to_spot: typing.Optional[typing.Union["ManagedInstanceAwsRevertToSpot", typing.Dict[str, typing.Any]]] = None,
        scheduled_task: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsScheduledTask", typing.Dict[str, typing.Any]]]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        shutdown_script: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsTags", typing.Dict[str, typing.Any]]]]] = None,
        unhealthy_duration: typing.Optional[jsii.Number] = None,
        user_data: typing.Optional[builtins.str] = None,
        utilize_reserved_instances: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#image_id ManagedInstanceAws#image_id}.
        :param instance_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#instance_types ManagedInstanceAws#instance_types}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#name ManagedInstanceAws#name}.
        :param persist_block_devices: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#persist_block_devices ManagedInstanceAws#persist_block_devices}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#product ManagedInstanceAws#product}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#subnet_ids ManagedInstanceAws#subnet_ids}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#vpc_id ManagedInstanceAws#vpc_id}.
        :param auto_healing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#auto_healing ManagedInstanceAws#auto_healing}.
        :param block_device_mappings: block_device_mappings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#block_device_mappings ManagedInstanceAws#block_device_mappings}
        :param block_devices_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#block_devices_mode ManagedInstanceAws#block_devices_mode}.
        :param cpu_credits: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#cpu_credits ManagedInstanceAws#cpu_credits}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#description ManagedInstanceAws#description}.
        :param draining_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#draining_timeout ManagedInstanceAws#draining_timeout}.
        :param ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#ebs_optimized ManagedInstanceAws#ebs_optimized}.
        :param elastic_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#elastic_ip ManagedInstanceAws#elastic_ip}.
        :param enable_monitoring: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#enable_monitoring ManagedInstanceAws#enable_monitoring}.
        :param fall_back_to_od: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#fall_back_to_od ManagedInstanceAws#fall_back_to_od}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#grace_period ManagedInstanceAws#grace_period}.
        :param health_check_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#health_check_type ManagedInstanceAws#health_check_type}.
        :param iam_instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#iam_instance_profile ManagedInstanceAws#iam_instance_profile}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#id ManagedInstanceAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param integration_route53: integration_route53 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#integration_route53 ManagedInstanceAws#integration_route53}
        :param key_pair: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#key_pair ManagedInstanceAws#key_pair}.
        :param life_cycle: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#life_cycle ManagedInstanceAws#life_cycle}.
        :param load_balancers: load_balancers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#load_balancers ManagedInstanceAws#load_balancers}
        :param managed_instance_action: managed_instance_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#managed_instance_action ManagedInstanceAws#managed_instance_action}
        :param minimum_instance_lifetime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#minimum_instance_lifetime ManagedInstanceAws#minimum_instance_lifetime}.
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#network_interface ManagedInstanceAws#network_interface}
        :param optimization_windows: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#optimization_windows ManagedInstanceAws#optimization_windows}.
        :param orientation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#orientation ManagedInstanceAws#orientation}.
        :param persist_private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#persist_private_ip ManagedInstanceAws#persist_private_ip}.
        :param persist_root_device: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#persist_root_device ManagedInstanceAws#persist_root_device}.
        :param placement_tenancy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#placement_tenancy ManagedInstanceAws#placement_tenancy}.
        :param preferred_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#preferred_type ManagedInstanceAws#preferred_type}.
        :param private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#private_ip ManagedInstanceAws#private_ip}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#region ManagedInstanceAws#region}.
        :param resource_tag_specification: resource_tag_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#resource_tag_specification ManagedInstanceAws#resource_tag_specification}
        :param revert_to_spot: revert_to_spot block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#revert_to_spot ManagedInstanceAws#revert_to_spot}
        :param scheduled_task: scheduled_task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#scheduled_task ManagedInstanceAws#scheduled_task}
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#security_group_ids ManagedInstanceAws#security_group_ids}.
        :param shutdown_script: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#shutdown_script ManagedInstanceAws#shutdown_script}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#tags ManagedInstanceAws#tags}
        :param unhealthy_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#unhealthy_duration ManagedInstanceAws#unhealthy_duration}.
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#user_data ManagedInstanceAws#user_data}.
        :param utilize_reserved_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#utilize_reserved_instances ManagedInstanceAws#utilize_reserved_instances}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(integration_route53, dict):
            integration_route53 = ManagedInstanceAwsIntegrationRoute53(**integration_route53)
        if isinstance(managed_instance_action, dict):
            managed_instance_action = ManagedInstanceAwsManagedInstanceAction(**managed_instance_action)
        if isinstance(revert_to_spot, dict):
            revert_to_spot = ManagedInstanceAwsRevertToSpot(**revert_to_spot)
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument image_id", value=image_id, expected_type=type_hints["image_id"])
            check_type(argname="argument instance_types", value=instance_types, expected_type=type_hints["instance_types"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument persist_block_devices", value=persist_block_devices, expected_type=type_hints["persist_block_devices"])
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument auto_healing", value=auto_healing, expected_type=type_hints["auto_healing"])
            check_type(argname="argument block_device_mappings", value=block_device_mappings, expected_type=type_hints["block_device_mappings"])
            check_type(argname="argument block_devices_mode", value=block_devices_mode, expected_type=type_hints["block_devices_mode"])
            check_type(argname="argument cpu_credits", value=cpu_credits, expected_type=type_hints["cpu_credits"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument draining_timeout", value=draining_timeout, expected_type=type_hints["draining_timeout"])
            check_type(argname="argument ebs_optimized", value=ebs_optimized, expected_type=type_hints["ebs_optimized"])
            check_type(argname="argument elastic_ip", value=elastic_ip, expected_type=type_hints["elastic_ip"])
            check_type(argname="argument enable_monitoring", value=enable_monitoring, expected_type=type_hints["enable_monitoring"])
            check_type(argname="argument fall_back_to_od", value=fall_back_to_od, expected_type=type_hints["fall_back_to_od"])
            check_type(argname="argument grace_period", value=grace_period, expected_type=type_hints["grace_period"])
            check_type(argname="argument health_check_type", value=health_check_type, expected_type=type_hints["health_check_type"])
            check_type(argname="argument iam_instance_profile", value=iam_instance_profile, expected_type=type_hints["iam_instance_profile"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument integration_route53", value=integration_route53, expected_type=type_hints["integration_route53"])
            check_type(argname="argument key_pair", value=key_pair, expected_type=type_hints["key_pair"])
            check_type(argname="argument life_cycle", value=life_cycle, expected_type=type_hints["life_cycle"])
            check_type(argname="argument load_balancers", value=load_balancers, expected_type=type_hints["load_balancers"])
            check_type(argname="argument managed_instance_action", value=managed_instance_action, expected_type=type_hints["managed_instance_action"])
            check_type(argname="argument minimum_instance_lifetime", value=minimum_instance_lifetime, expected_type=type_hints["minimum_instance_lifetime"])
            check_type(argname="argument network_interface", value=network_interface, expected_type=type_hints["network_interface"])
            check_type(argname="argument optimization_windows", value=optimization_windows, expected_type=type_hints["optimization_windows"])
            check_type(argname="argument orientation", value=orientation, expected_type=type_hints["orientation"])
            check_type(argname="argument persist_private_ip", value=persist_private_ip, expected_type=type_hints["persist_private_ip"])
            check_type(argname="argument persist_root_device", value=persist_root_device, expected_type=type_hints["persist_root_device"])
            check_type(argname="argument placement_tenancy", value=placement_tenancy, expected_type=type_hints["placement_tenancy"])
            check_type(argname="argument preferred_type", value=preferred_type, expected_type=type_hints["preferred_type"])
            check_type(argname="argument private_ip", value=private_ip, expected_type=type_hints["private_ip"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument resource_tag_specification", value=resource_tag_specification, expected_type=type_hints["resource_tag_specification"])
            check_type(argname="argument revert_to_spot", value=revert_to_spot, expected_type=type_hints["revert_to_spot"])
            check_type(argname="argument scheduled_task", value=scheduled_task, expected_type=type_hints["scheduled_task"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument shutdown_script", value=shutdown_script, expected_type=type_hints["shutdown_script"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument unhealthy_duration", value=unhealthy_duration, expected_type=type_hints["unhealthy_duration"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
            check_type(argname="argument utilize_reserved_instances", value=utilize_reserved_instances, expected_type=type_hints["utilize_reserved_instances"])
        self._values: typing.Dict[str, typing.Any] = {
            "image_id": image_id,
            "instance_types": instance_types,
            "name": name,
            "persist_block_devices": persist_block_devices,
            "product": product,
            "subnet_ids": subnet_ids,
            "vpc_id": vpc_id,
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
        if block_device_mappings is not None:
            self._values["block_device_mappings"] = block_device_mappings
        if block_devices_mode is not None:
            self._values["block_devices_mode"] = block_devices_mode
        if cpu_credits is not None:
            self._values["cpu_credits"] = cpu_credits
        if description is not None:
            self._values["description"] = description
        if draining_timeout is not None:
            self._values["draining_timeout"] = draining_timeout
        if ebs_optimized is not None:
            self._values["ebs_optimized"] = ebs_optimized
        if elastic_ip is not None:
            self._values["elastic_ip"] = elastic_ip
        if enable_monitoring is not None:
            self._values["enable_monitoring"] = enable_monitoring
        if fall_back_to_od is not None:
            self._values["fall_back_to_od"] = fall_back_to_od
        if grace_period is not None:
            self._values["grace_period"] = grace_period
        if health_check_type is not None:
            self._values["health_check_type"] = health_check_type
        if iam_instance_profile is not None:
            self._values["iam_instance_profile"] = iam_instance_profile
        if id is not None:
            self._values["id"] = id
        if integration_route53 is not None:
            self._values["integration_route53"] = integration_route53
        if key_pair is not None:
            self._values["key_pair"] = key_pair
        if life_cycle is not None:
            self._values["life_cycle"] = life_cycle
        if load_balancers is not None:
            self._values["load_balancers"] = load_balancers
        if managed_instance_action is not None:
            self._values["managed_instance_action"] = managed_instance_action
        if minimum_instance_lifetime is not None:
            self._values["minimum_instance_lifetime"] = minimum_instance_lifetime
        if network_interface is not None:
            self._values["network_interface"] = network_interface
        if optimization_windows is not None:
            self._values["optimization_windows"] = optimization_windows
        if orientation is not None:
            self._values["orientation"] = orientation
        if persist_private_ip is not None:
            self._values["persist_private_ip"] = persist_private_ip
        if persist_root_device is not None:
            self._values["persist_root_device"] = persist_root_device
        if placement_tenancy is not None:
            self._values["placement_tenancy"] = placement_tenancy
        if preferred_type is not None:
            self._values["preferred_type"] = preferred_type
        if private_ip is not None:
            self._values["private_ip"] = private_ip
        if region is not None:
            self._values["region"] = region
        if resource_tag_specification is not None:
            self._values["resource_tag_specification"] = resource_tag_specification
        if revert_to_spot is not None:
            self._values["revert_to_spot"] = revert_to_spot
        if scheduled_task is not None:
            self._values["scheduled_task"] = scheduled_task
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if shutdown_script is not None:
            self._values["shutdown_script"] = shutdown_script
        if tags is not None:
            self._values["tags"] = tags
        if unhealthy_duration is not None:
            self._values["unhealthy_duration"] = unhealthy_duration
        if user_data is not None:
            self._values["user_data"] = user_data
        if utilize_reserved_instances is not None:
            self._values["utilize_reserved_instances"] = utilize_reserved_instances

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
    def image_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#image_id ManagedInstanceAws#image_id}.'''
        result = self._values.get("image_id")
        assert result is not None, "Required property 'image_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_types(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#instance_types ManagedInstanceAws#instance_types}.'''
        result = self._values.get("instance_types")
        assert result is not None, "Required property 'instance_types' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#name ManagedInstanceAws#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def persist_block_devices(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#persist_block_devices ManagedInstanceAws#persist_block_devices}.'''
        result = self._values.get("persist_block_devices")
        assert result is not None, "Required property 'persist_block_devices' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def product(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#product ManagedInstanceAws#product}.'''
        result = self._values.get("product")
        assert result is not None, "Required property 'product' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#subnet_ids ManagedInstanceAws#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#vpc_id ManagedInstanceAws#vpc_id}.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_healing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#auto_healing ManagedInstanceAws#auto_healing}.'''
        result = self._values.get("auto_healing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def block_device_mappings(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsBlockDeviceMappings]]]:
        '''block_device_mappings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#block_device_mappings ManagedInstanceAws#block_device_mappings}
        '''
        result = self._values.get("block_device_mappings")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsBlockDeviceMappings]]], result)

    @builtins.property
    def block_devices_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#block_devices_mode ManagedInstanceAws#block_devices_mode}.'''
        result = self._values.get("block_devices_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cpu_credits(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#cpu_credits ManagedInstanceAws#cpu_credits}.'''
        result = self._values.get("cpu_credits")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#description ManagedInstanceAws#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def draining_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#draining_timeout ManagedInstanceAws#draining_timeout}.'''
        result = self._values.get("draining_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ebs_optimized(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#ebs_optimized ManagedInstanceAws#ebs_optimized}.'''
        result = self._values.get("ebs_optimized")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def elastic_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#elastic_ip ManagedInstanceAws#elastic_ip}.'''
        result = self._values.get("elastic_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_monitoring(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#enable_monitoring ManagedInstanceAws#enable_monitoring}.'''
        result = self._values.get("enable_monitoring")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def fall_back_to_od(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#fall_back_to_od ManagedInstanceAws#fall_back_to_od}.'''
        result = self._values.get("fall_back_to_od")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def grace_period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#grace_period ManagedInstanceAws#grace_period}.'''
        result = self._values.get("grace_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#health_check_type ManagedInstanceAws#health_check_type}.'''
        result = self._values.get("health_check_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_instance_profile(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#iam_instance_profile ManagedInstanceAws#iam_instance_profile}.'''
        result = self._values.get("iam_instance_profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#id ManagedInstanceAws#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_route53(
        self,
    ) -> typing.Optional["ManagedInstanceAwsIntegrationRoute53"]:
        '''integration_route53 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#integration_route53 ManagedInstanceAws#integration_route53}
        '''
        result = self._values.get("integration_route53")
        return typing.cast(typing.Optional["ManagedInstanceAwsIntegrationRoute53"], result)

    @builtins.property
    def key_pair(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#key_pair ManagedInstanceAws#key_pair}.'''
        result = self._values.get("key_pair")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def life_cycle(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#life_cycle ManagedInstanceAws#life_cycle}.'''
        result = self._values.get("life_cycle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsLoadBalancers"]]]:
        '''load_balancers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#load_balancers ManagedInstanceAws#load_balancers}
        '''
        result = self._values.get("load_balancers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsLoadBalancers"]]], result)

    @builtins.property
    def managed_instance_action(
        self,
    ) -> typing.Optional["ManagedInstanceAwsManagedInstanceAction"]:
        '''managed_instance_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#managed_instance_action ManagedInstanceAws#managed_instance_action}
        '''
        result = self._values.get("managed_instance_action")
        return typing.cast(typing.Optional["ManagedInstanceAwsManagedInstanceAction"], result)

    @builtins.property
    def minimum_instance_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#minimum_instance_lifetime ManagedInstanceAws#minimum_instance_lifetime}.'''
        result = self._values.get("minimum_instance_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def network_interface(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsNetworkInterface"]]]:
        '''network_interface block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#network_interface ManagedInstanceAws#network_interface}
        '''
        result = self._values.get("network_interface")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsNetworkInterface"]]], result)

    @builtins.property
    def optimization_windows(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#optimization_windows ManagedInstanceAws#optimization_windows}.'''
        result = self._values.get("optimization_windows")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def orientation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#orientation ManagedInstanceAws#orientation}.'''
        result = self._values.get("orientation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def persist_private_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#persist_private_ip ManagedInstanceAws#persist_private_ip}.'''
        result = self._values.get("persist_private_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def persist_root_device(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#persist_root_device ManagedInstanceAws#persist_root_device}.'''
        result = self._values.get("persist_root_device")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def placement_tenancy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#placement_tenancy ManagedInstanceAws#placement_tenancy}.'''
        result = self._values.get("placement_tenancy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#preferred_type ManagedInstanceAws#preferred_type}.'''
        result = self._values.get("preferred_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#private_ip ManagedInstanceAws#private_ip}.'''
        result = self._values.get("private_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#region ManagedInstanceAws#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_tag_specification(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsResourceTagSpecification"]]]:
        '''resource_tag_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#resource_tag_specification ManagedInstanceAws#resource_tag_specification}
        '''
        result = self._values.get("resource_tag_specification")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsResourceTagSpecification"]]], result)

    @builtins.property
    def revert_to_spot(self) -> typing.Optional["ManagedInstanceAwsRevertToSpot"]:
        '''revert_to_spot block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#revert_to_spot ManagedInstanceAws#revert_to_spot}
        '''
        result = self._values.get("revert_to_spot")
        return typing.cast(typing.Optional["ManagedInstanceAwsRevertToSpot"], result)

    @builtins.property
    def scheduled_task(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsScheduledTask"]]]:
        '''scheduled_task block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#scheduled_task ManagedInstanceAws#scheduled_task}
        '''
        result = self._values.get("scheduled_task")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsScheduledTask"]]], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#security_group_ids ManagedInstanceAws#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def shutdown_script(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#shutdown_script ManagedInstanceAws#shutdown_script}.'''
        result = self._values.get("shutdown_script")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsTags"]]]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#tags ManagedInstanceAws#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsTags"]]], result)

    @builtins.property
    def unhealthy_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#unhealthy_duration ManagedInstanceAws#unhealthy_duration}.'''
        result = self._values.get("unhealthy_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#user_data ManagedInstanceAws#user_data}.'''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def utilize_reserved_instances(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#utilize_reserved_instances ManagedInstanceAws#utilize_reserved_instances}.'''
        result = self._values.get("utilize_reserved_instances")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedInstanceAwsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsIntegrationRoute53",
    jsii_struct_bases=[],
    name_mapping={"domains": "domains"},
)
class ManagedInstanceAwsIntegrationRoute53:
    def __init__(
        self,
        *,
        domains: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsIntegrationRoute53Domains", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param domains: domains block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#domains ManagedInstanceAws#domains}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsIntegrationRoute53.__init__)
            check_type(argname="argument domains", value=domains, expected_type=type_hints["domains"])
        self._values: typing.Dict[str, typing.Any] = {
            "domains": domains,
        }

    @builtins.property
    def domains(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsIntegrationRoute53Domains"]]:
        '''domains block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#domains ManagedInstanceAws#domains}
        '''
        result = self._values.get("domains")
        assert result is not None, "Required property 'domains' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsIntegrationRoute53Domains"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedInstanceAwsIntegrationRoute53(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsIntegrationRoute53Domains",
    jsii_struct_bases=[],
    name_mapping={
        "hosted_zone_id": "hostedZoneId",
        "record_sets": "recordSets",
        "record_set_type": "recordSetType",
        "spotinst_acct_id": "spotinstAcctId",
    },
)
class ManagedInstanceAwsIntegrationRoute53Domains:
    def __init__(
        self,
        *,
        hosted_zone_id: builtins.str,
        record_sets: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsIntegrationRoute53DomainsRecordSets", typing.Dict[str, typing.Any]]]],
        record_set_type: typing.Optional[builtins.str] = None,
        spotinst_acct_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hosted_zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#hosted_zone_id ManagedInstanceAws#hosted_zone_id}.
        :param record_sets: record_sets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#record_sets ManagedInstanceAws#record_sets}
        :param record_set_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#record_set_type ManagedInstanceAws#record_set_type}.
        :param spotinst_acct_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#spotinst_acct_id ManagedInstanceAws#spotinst_acct_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsIntegrationRoute53Domains.__init__)
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
            check_type(argname="argument record_sets", value=record_sets, expected_type=type_hints["record_sets"])
            check_type(argname="argument record_set_type", value=record_set_type, expected_type=type_hints["record_set_type"])
            check_type(argname="argument spotinst_acct_id", value=spotinst_acct_id, expected_type=type_hints["spotinst_acct_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "hosted_zone_id": hosted_zone_id,
            "record_sets": record_sets,
        }
        if record_set_type is not None:
            self._values["record_set_type"] = record_set_type
        if spotinst_acct_id is not None:
            self._values["spotinst_acct_id"] = spotinst_acct_id

    @builtins.property
    def hosted_zone_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#hosted_zone_id ManagedInstanceAws#hosted_zone_id}.'''
        result = self._values.get("hosted_zone_id")
        assert result is not None, "Required property 'hosted_zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def record_sets(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsIntegrationRoute53DomainsRecordSets"]]:
        '''record_sets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#record_sets ManagedInstanceAws#record_sets}
        '''
        result = self._values.get("record_sets")
        assert result is not None, "Required property 'record_sets' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsIntegrationRoute53DomainsRecordSets"]], result)

    @builtins.property
    def record_set_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#record_set_type ManagedInstanceAws#record_set_type}.'''
        result = self._values.get("record_set_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spotinst_acct_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#spotinst_acct_id ManagedInstanceAws#spotinst_acct_id}.'''
        result = self._values.get("spotinst_acct_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedInstanceAwsIntegrationRoute53Domains(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedInstanceAwsIntegrationRoute53DomainsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsIntegrationRoute53DomainsList",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsIntegrationRoute53DomainsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ManagedInstanceAwsIntegrationRoute53DomainsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsIntegrationRoute53DomainsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ManagedInstanceAwsIntegrationRoute53DomainsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsIntegrationRoute53DomainsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsIntegrationRoute53DomainsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsIntegrationRoute53DomainsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsIntegrationRoute53Domains]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsIntegrationRoute53Domains]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsIntegrationRoute53Domains]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsIntegrationRoute53DomainsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManagedInstanceAwsIntegrationRoute53DomainsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsIntegrationRoute53DomainsOutputReference",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsIntegrationRoute53DomainsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRecordSets")
    def put_record_sets(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedInstanceAwsIntegrationRoute53DomainsRecordSets", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsIntegrationRoute53DomainsOutputReference.put_record_sets)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRecordSets", [value]))

    @jsii.member(jsii_name="resetRecordSetType")
    def reset_record_set_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordSetType", []))

    @jsii.member(jsii_name="resetSpotinstAcctId")
    def reset_spotinst_acct_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotinstAcctId", []))

    @builtins.property
    @jsii.member(jsii_name="recordSets")
    def record_sets(
        self,
    ) -> "ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsList":
        return typing.cast("ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsList", jsii.get(self, "recordSets"))

    @builtins.property
    @jsii.member(jsii_name="hostedZoneIdInput")
    def hosted_zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostedZoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="recordSetsInput")
    def record_sets_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsIntegrationRoute53DomainsRecordSets"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedInstanceAwsIntegrationRoute53DomainsRecordSets"]]], jsii.get(self, "recordSetsInput"))

    @builtins.property
    @jsii.member(jsii_name="recordSetTypeInput")
    def record_set_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordSetTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="spotinstAcctIdInput")
    def spotinst_acct_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spotinstAcctIdInput"))

    @builtins.property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostedZoneId"))

    @hosted_zone_id.setter
    def hosted_zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsIntegrationRoute53DomainsOutputReference, "hosted_zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostedZoneId", value)

    @builtins.property
    @jsii.member(jsii_name="recordSetType")
    def record_set_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordSetType"))

    @record_set_type.setter
    def record_set_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsIntegrationRoute53DomainsOutputReference, "record_set_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordSetType", value)

    @builtins.property
    @jsii.member(jsii_name="spotinstAcctId")
    def spotinst_acct_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spotinstAcctId"))

    @spotinst_acct_id.setter
    def spotinst_acct_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsIntegrationRoute53DomainsOutputReference, "spotinst_acct_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotinstAcctId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ManagedInstanceAwsIntegrationRoute53Domains, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ManagedInstanceAwsIntegrationRoute53Domains, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ManagedInstanceAwsIntegrationRoute53Domains, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsIntegrationRoute53DomainsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsIntegrationRoute53DomainsRecordSets",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "use_public_dns": "usePublicDns",
        "use_public_ip": "usePublicIp",
    },
)
class ManagedInstanceAwsIntegrationRoute53DomainsRecordSets:
    def __init__(
        self,
        *,
        name: builtins.str,
        use_public_dns: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#name ManagedInstanceAws#name}.
        :param use_public_dns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#use_public_dns ManagedInstanceAws#use_public_dns}.
        :param use_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#use_public_ip ManagedInstanceAws#use_public_ip}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsIntegrationRoute53DomainsRecordSets.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument use_public_dns", value=use_public_dns, expected_type=type_hints["use_public_dns"])
            check_type(argname="argument use_public_ip", value=use_public_ip, expected_type=type_hints["use_public_ip"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if use_public_dns is not None:
            self._values["use_public_dns"] = use_public_dns
        if use_public_ip is not None:
            self._values["use_public_ip"] = use_public_ip

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#name ManagedInstanceAws#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_public_dns(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#use_public_dns ManagedInstanceAws#use_public_dns}.'''
        result = self._values.get("use_public_dns")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def use_public_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#use_public_ip ManagedInstanceAws#use_public_ip}.'''
        result = self._values.get("use_public_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedInstanceAwsIntegrationRoute53DomainsRecordSets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsList",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsIntegrationRoute53DomainsRecordSets]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsIntegrationRoute53DomainsRecordSets]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsIntegrationRoute53DomainsRecordSets]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsOutputReference",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetUsePublicDns")
    def reset_use_public_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsePublicDns", []))

    @jsii.member(jsii_name="resetUsePublicIp")
    def reset_use_public_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsePublicIp", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="usePublicDnsInput")
    def use_public_dns_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "usePublicDnsInput"))

    @builtins.property
    @jsii.member(jsii_name="usePublicIpInput")
    def use_public_ip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "usePublicIpInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="usePublicDns")
    def use_public_dns(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "usePublicDns"))

    @use_public_dns.setter
    def use_public_dns(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsOutputReference, "use_public_dns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usePublicDns", value)

    @builtins.property
    @jsii.member(jsii_name="usePublicIp")
    def use_public_ip(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "usePublicIp"))

    @use_public_ip.setter
    def use_public_ip(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsOutputReference, "use_public_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usePublicIp", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ManagedInstanceAwsIntegrationRoute53DomainsRecordSets, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ManagedInstanceAwsIntegrationRoute53DomainsRecordSets, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ManagedInstanceAwsIntegrationRoute53DomainsRecordSets, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManagedInstanceAwsIntegrationRoute53OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsIntegrationRoute53OutputReference",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsIntegrationRoute53OutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDomains")
    def put_domains(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ManagedInstanceAwsIntegrationRoute53Domains, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsIntegrationRoute53OutputReference.put_domains)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDomains", [value]))

    @builtins.property
    @jsii.member(jsii_name="domains")
    def domains(self) -> ManagedInstanceAwsIntegrationRoute53DomainsList:
        return typing.cast(ManagedInstanceAwsIntegrationRoute53DomainsList, jsii.get(self, "domains"))

    @builtins.property
    @jsii.member(jsii_name="domainsInput")
    def domains_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsIntegrationRoute53Domains]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsIntegrationRoute53Domains]]], jsii.get(self, "domainsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ManagedInstanceAwsIntegrationRoute53]:
        return typing.cast(typing.Optional[ManagedInstanceAwsIntegrationRoute53], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedInstanceAwsIntegrationRoute53],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsIntegrationRoute53OutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsLoadBalancers",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "arn": "arn",
        "auto_weight": "autoWeight",
        "az_awareness": "azAwareness",
        "balancer_id": "balancerId",
        "name": "name",
        "target_set_id": "targetSetId",
    },
)
class ManagedInstanceAwsLoadBalancers:
    def __init__(
        self,
        *,
        type: builtins.str,
        arn: typing.Optional[builtins.str] = None,
        auto_weight: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        az_awareness: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        balancer_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        target_set_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#type ManagedInstanceAws#type}.
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#arn ManagedInstanceAws#arn}.
        :param auto_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#auto_weight ManagedInstanceAws#auto_weight}.
        :param az_awareness: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#az_awareness ManagedInstanceAws#az_awareness}.
        :param balancer_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#balancer_id ManagedInstanceAws#balancer_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#name ManagedInstanceAws#name}.
        :param target_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#target_set_id ManagedInstanceAws#target_set_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsLoadBalancers.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument auto_weight", value=auto_weight, expected_type=type_hints["auto_weight"])
            check_type(argname="argument az_awareness", value=az_awareness, expected_type=type_hints["az_awareness"])
            check_type(argname="argument balancer_id", value=balancer_id, expected_type=type_hints["balancer_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target_set_id", value=target_set_id, expected_type=type_hints["target_set_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if arn is not None:
            self._values["arn"] = arn
        if auto_weight is not None:
            self._values["auto_weight"] = auto_weight
        if az_awareness is not None:
            self._values["az_awareness"] = az_awareness
        if balancer_id is not None:
            self._values["balancer_id"] = balancer_id
        if name is not None:
            self._values["name"] = name
        if target_set_id is not None:
            self._values["target_set_id"] = target_set_id

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#type ManagedInstanceAws#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#arn ManagedInstanceAws#arn}.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_weight(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#auto_weight ManagedInstanceAws#auto_weight}.'''
        result = self._values.get("auto_weight")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def az_awareness(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#az_awareness ManagedInstanceAws#az_awareness}.'''
        result = self._values.get("az_awareness")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def balancer_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#balancer_id ManagedInstanceAws#balancer_id}.'''
        result = self._values.get("balancer_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#name ManagedInstanceAws#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#target_set_id ManagedInstanceAws#target_set_id}.'''
        result = self._values.get("target_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedInstanceAwsLoadBalancers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedInstanceAwsLoadBalancersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsLoadBalancersList",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsLoadBalancersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ManagedInstanceAwsLoadBalancersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsLoadBalancersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ManagedInstanceAwsLoadBalancersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsLoadBalancersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsLoadBalancersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsLoadBalancersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsLoadBalancers]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsLoadBalancers]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsLoadBalancers]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsLoadBalancersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManagedInstanceAwsLoadBalancersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsLoadBalancersOutputReference",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsLoadBalancersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetArn")
    def reset_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArn", []))

    @jsii.member(jsii_name="resetAutoWeight")
    def reset_auto_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoWeight", []))

    @jsii.member(jsii_name="resetAzAwareness")
    def reset_az_awareness(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzAwareness", []))

    @jsii.member(jsii_name="resetBalancerId")
    def reset_balancer_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBalancerId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetTargetSetId")
    def reset_target_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetSetId", []))

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="autoWeightInput")
    def auto_weight_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoWeightInput"))

    @builtins.property
    @jsii.member(jsii_name="azAwarenessInput")
    def az_awareness_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "azAwarenessInput"))

    @builtins.property
    @jsii.member(jsii_name="balancerIdInput")
    def balancer_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "balancerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetSetIdInput")
    def target_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsLoadBalancersOutputReference, "arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="autoWeight")
    def auto_weight(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoWeight"))

    @auto_weight.setter
    def auto_weight(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsLoadBalancersOutputReference, "auto_weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoWeight", value)

    @builtins.property
    @jsii.member(jsii_name="azAwareness")
    def az_awareness(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "azAwareness"))

    @az_awareness.setter
    def az_awareness(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsLoadBalancersOutputReference, "az_awareness").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azAwareness", value)

    @builtins.property
    @jsii.member(jsii_name="balancerId")
    def balancer_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "balancerId"))

    @balancer_id.setter
    def balancer_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsLoadBalancersOutputReference, "balancer_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "balancerId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsLoadBalancersOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="targetSetId")
    def target_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetSetId"))

    @target_set_id.setter
    def target_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsLoadBalancersOutputReference, "target_set_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetSetId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsLoadBalancersOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ManagedInstanceAwsLoadBalancers, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ManagedInstanceAwsLoadBalancers, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ManagedInstanceAwsLoadBalancers, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsLoadBalancersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsManagedInstanceAction",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class ManagedInstanceAwsManagedInstanceAction:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#type ManagedInstanceAws#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsManagedInstanceAction.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#type ManagedInstanceAws#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedInstanceAwsManagedInstanceAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedInstanceAwsManagedInstanceActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsManagedInstanceActionOutputReference",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsManagedInstanceActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsManagedInstanceActionOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ManagedInstanceAwsManagedInstanceAction]:
        return typing.cast(typing.Optional[ManagedInstanceAwsManagedInstanceAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedInstanceAwsManagedInstanceAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsManagedInstanceActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsNetworkInterface",
    jsii_struct_bases=[],
    name_mapping={
        "device_index": "deviceIndex",
        "associate_ipv6_address": "associateIpv6Address",
        "associate_public_ip_address": "associatePublicIpAddress",
    },
)
class ManagedInstanceAwsNetworkInterface:
    def __init__(
        self,
        *,
        device_index: builtins.str,
        associate_ipv6_address: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param device_index: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#device_index ManagedInstanceAws#device_index}.
        :param associate_ipv6_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#associate_ipv6_address ManagedInstanceAws#associate_ipv6_address}.
        :param associate_public_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#associate_public_ip_address ManagedInstanceAws#associate_public_ip_address}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsNetworkInterface.__init__)
            check_type(argname="argument device_index", value=device_index, expected_type=type_hints["device_index"])
            check_type(argname="argument associate_ipv6_address", value=associate_ipv6_address, expected_type=type_hints["associate_ipv6_address"])
            check_type(argname="argument associate_public_ip_address", value=associate_public_ip_address, expected_type=type_hints["associate_public_ip_address"])
        self._values: typing.Dict[str, typing.Any] = {
            "device_index": device_index,
        }
        if associate_ipv6_address is not None:
            self._values["associate_ipv6_address"] = associate_ipv6_address
        if associate_public_ip_address is not None:
            self._values["associate_public_ip_address"] = associate_public_ip_address

    @builtins.property
    def device_index(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#device_index ManagedInstanceAws#device_index}.'''
        result = self._values.get("device_index")
        assert result is not None, "Required property 'device_index' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def associate_ipv6_address(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#associate_ipv6_address ManagedInstanceAws#associate_ipv6_address}.'''
        result = self._values.get("associate_ipv6_address")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def associate_public_ip_address(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#associate_public_ip_address ManagedInstanceAws#associate_public_ip_address}.'''
        result = self._values.get("associate_public_ip_address")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedInstanceAwsNetworkInterface(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedInstanceAwsNetworkInterfaceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsNetworkInterfaceList",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsNetworkInterfaceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ManagedInstanceAwsNetworkInterfaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsNetworkInterfaceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ManagedInstanceAwsNetworkInterfaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsNetworkInterfaceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsNetworkInterfaceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsNetworkInterfaceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsNetworkInterface]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsNetworkInterface]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsNetworkInterface]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsNetworkInterfaceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManagedInstanceAwsNetworkInterfaceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsNetworkInterfaceOutputReference",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsNetworkInterfaceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAssociateIpv6Address")
    def reset_associate_ipv6_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssociateIpv6Address", []))

    @jsii.member(jsii_name="resetAssociatePublicIpAddress")
    def reset_associate_public_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssociatePublicIpAddress", []))

    @builtins.property
    @jsii.member(jsii_name="associateIpv6AddressInput")
    def associate_ipv6_address_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "associateIpv6AddressInput"))

    @builtins.property
    @jsii.member(jsii_name="associatePublicIpAddressInput")
    def associate_public_ip_address_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "associatePublicIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceIndexInput")
    def device_index_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceIndexInput"))

    @builtins.property
    @jsii.member(jsii_name="associateIpv6Address")
    def associate_ipv6_address(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "associateIpv6Address"))

    @associate_ipv6_address.setter
    def associate_ipv6_address(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsNetworkInterfaceOutputReference, "associate_ipv6_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associateIpv6Address", value)

    @builtins.property
    @jsii.member(jsii_name="associatePublicIpAddress")
    def associate_public_ip_address(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "associatePublicIpAddress"))

    @associate_public_ip_address.setter
    def associate_public_ip_address(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsNetworkInterfaceOutputReference, "associate_public_ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatePublicIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="deviceIndex")
    def device_index(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceIndex"))

    @device_index.setter
    def device_index(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsNetworkInterfaceOutputReference, "device_index").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceIndex", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ManagedInstanceAwsNetworkInterface, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ManagedInstanceAwsNetworkInterface, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ManagedInstanceAwsNetworkInterface, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsNetworkInterfaceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsResourceTagSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "should_tag_amis": "shouldTagAmis",
        "should_tag_enis": "shouldTagEnis",
        "should_tag_snapshots": "shouldTagSnapshots",
        "should_tag_volumes": "shouldTagVolumes",
    },
)
class ManagedInstanceAwsResourceTagSpecification:
    def __init__(
        self,
        *,
        should_tag_amis: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        should_tag_enis: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        should_tag_snapshots: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        should_tag_volumes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param should_tag_amis: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#should_tag_amis ManagedInstanceAws#should_tag_amis}.
        :param should_tag_enis: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#should_tag_enis ManagedInstanceAws#should_tag_enis}.
        :param should_tag_snapshots: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#should_tag_snapshots ManagedInstanceAws#should_tag_snapshots}.
        :param should_tag_volumes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#should_tag_volumes ManagedInstanceAws#should_tag_volumes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsResourceTagSpecification.__init__)
            check_type(argname="argument should_tag_amis", value=should_tag_amis, expected_type=type_hints["should_tag_amis"])
            check_type(argname="argument should_tag_enis", value=should_tag_enis, expected_type=type_hints["should_tag_enis"])
            check_type(argname="argument should_tag_snapshots", value=should_tag_snapshots, expected_type=type_hints["should_tag_snapshots"])
            check_type(argname="argument should_tag_volumes", value=should_tag_volumes, expected_type=type_hints["should_tag_volumes"])
        self._values: typing.Dict[str, typing.Any] = {}
        if should_tag_amis is not None:
            self._values["should_tag_amis"] = should_tag_amis
        if should_tag_enis is not None:
            self._values["should_tag_enis"] = should_tag_enis
        if should_tag_snapshots is not None:
            self._values["should_tag_snapshots"] = should_tag_snapshots
        if should_tag_volumes is not None:
            self._values["should_tag_volumes"] = should_tag_volumes

    @builtins.property
    def should_tag_amis(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#should_tag_amis ManagedInstanceAws#should_tag_amis}.'''
        result = self._values.get("should_tag_amis")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def should_tag_enis(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#should_tag_enis ManagedInstanceAws#should_tag_enis}.'''
        result = self._values.get("should_tag_enis")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def should_tag_snapshots(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#should_tag_snapshots ManagedInstanceAws#should_tag_snapshots}.'''
        result = self._values.get("should_tag_snapshots")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def should_tag_volumes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#should_tag_volumes ManagedInstanceAws#should_tag_volumes}.'''
        result = self._values.get("should_tag_volumes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedInstanceAwsResourceTagSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedInstanceAwsResourceTagSpecificationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsResourceTagSpecificationList",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsResourceTagSpecificationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ManagedInstanceAwsResourceTagSpecificationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsResourceTagSpecificationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ManagedInstanceAwsResourceTagSpecificationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsResourceTagSpecificationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsResourceTagSpecificationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsResourceTagSpecificationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsResourceTagSpecification]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsResourceTagSpecification]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsResourceTagSpecification]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsResourceTagSpecificationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManagedInstanceAwsResourceTagSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsResourceTagSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsResourceTagSpecificationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetShouldTagAmis")
    def reset_should_tag_amis(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShouldTagAmis", []))

    @jsii.member(jsii_name="resetShouldTagEnis")
    def reset_should_tag_enis(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShouldTagEnis", []))

    @jsii.member(jsii_name="resetShouldTagSnapshots")
    def reset_should_tag_snapshots(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShouldTagSnapshots", []))

    @jsii.member(jsii_name="resetShouldTagVolumes")
    def reset_should_tag_volumes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShouldTagVolumes", []))

    @builtins.property
    @jsii.member(jsii_name="shouldTagAmisInput")
    def should_tag_amis_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "shouldTagAmisInput"))

    @builtins.property
    @jsii.member(jsii_name="shouldTagEnisInput")
    def should_tag_enis_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "shouldTagEnisInput"))

    @builtins.property
    @jsii.member(jsii_name="shouldTagSnapshotsInput")
    def should_tag_snapshots_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "shouldTagSnapshotsInput"))

    @builtins.property
    @jsii.member(jsii_name="shouldTagVolumesInput")
    def should_tag_volumes_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "shouldTagVolumesInput"))

    @builtins.property
    @jsii.member(jsii_name="shouldTagAmis")
    def should_tag_amis(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "shouldTagAmis"))

    @should_tag_amis.setter
    def should_tag_amis(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsResourceTagSpecificationOutputReference, "should_tag_amis").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shouldTagAmis", value)

    @builtins.property
    @jsii.member(jsii_name="shouldTagEnis")
    def should_tag_enis(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "shouldTagEnis"))

    @should_tag_enis.setter
    def should_tag_enis(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsResourceTagSpecificationOutputReference, "should_tag_enis").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shouldTagEnis", value)

    @builtins.property
    @jsii.member(jsii_name="shouldTagSnapshots")
    def should_tag_snapshots(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "shouldTagSnapshots"))

    @should_tag_snapshots.setter
    def should_tag_snapshots(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsResourceTagSpecificationOutputReference, "should_tag_snapshots").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shouldTagSnapshots", value)

    @builtins.property
    @jsii.member(jsii_name="shouldTagVolumes")
    def should_tag_volumes(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "shouldTagVolumes"))

    @should_tag_volumes.setter
    def should_tag_volumes(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsResourceTagSpecificationOutputReference, "should_tag_volumes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shouldTagVolumes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ManagedInstanceAwsResourceTagSpecification, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ManagedInstanceAwsResourceTagSpecification, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ManagedInstanceAwsResourceTagSpecification, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsResourceTagSpecificationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsRevertToSpot",
    jsii_struct_bases=[],
    name_mapping={"perform_at": "performAt"},
)
class ManagedInstanceAwsRevertToSpot:
    def __init__(self, *, perform_at: builtins.str) -> None:
        '''
        :param perform_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#perform_at ManagedInstanceAws#perform_at}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsRevertToSpot.__init__)
            check_type(argname="argument perform_at", value=perform_at, expected_type=type_hints["perform_at"])
        self._values: typing.Dict[str, typing.Any] = {
            "perform_at": perform_at,
        }

    @builtins.property
    def perform_at(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#perform_at ManagedInstanceAws#perform_at}.'''
        result = self._values.get("perform_at")
        assert result is not None, "Required property 'perform_at' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedInstanceAwsRevertToSpot(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedInstanceAwsRevertToSpotOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsRevertToSpotOutputReference",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsRevertToSpotOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="performAtInput")
    def perform_at_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "performAtInput"))

    @builtins.property
    @jsii.member(jsii_name="performAt")
    def perform_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "performAt"))

    @perform_at.setter
    def perform_at(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsRevertToSpotOutputReference, "perform_at").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "performAt", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ManagedInstanceAwsRevertToSpot]:
        return typing.cast(typing.Optional[ManagedInstanceAwsRevertToSpot], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedInstanceAwsRevertToSpot],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsRevertToSpotOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsScheduledTask",
    jsii_struct_bases=[],
    name_mapping={
        "task_type": "taskType",
        "cron_expression": "cronExpression",
        "frequency": "frequency",
        "is_enabled": "isEnabled",
        "start_time": "startTime",
    },
)
class ManagedInstanceAwsScheduledTask:
    def __init__(
        self,
        *,
        task_type: builtins.str,
        cron_expression: typing.Optional[builtins.str] = None,
        frequency: typing.Optional[builtins.str] = None,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        start_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param task_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#task_type ManagedInstanceAws#task_type}.
        :param cron_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#cron_expression ManagedInstanceAws#cron_expression}.
        :param frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#frequency ManagedInstanceAws#frequency}.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#is_enabled ManagedInstanceAws#is_enabled}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#start_time ManagedInstanceAws#start_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsScheduledTask.__init__)
            check_type(argname="argument task_type", value=task_type, expected_type=type_hints["task_type"])
            check_type(argname="argument cron_expression", value=cron_expression, expected_type=type_hints["cron_expression"])
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "task_type": task_type,
        }
        if cron_expression is not None:
            self._values["cron_expression"] = cron_expression
        if frequency is not None:
            self._values["frequency"] = frequency
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if start_time is not None:
            self._values["start_time"] = start_time

    @builtins.property
    def task_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#task_type ManagedInstanceAws#task_type}.'''
        result = self._values.get("task_type")
        assert result is not None, "Required property 'task_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cron_expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#cron_expression ManagedInstanceAws#cron_expression}.'''
        result = self._values.get("cron_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def frequency(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#frequency ManagedInstanceAws#frequency}.'''
        result = self._values.get("frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#is_enabled ManagedInstanceAws#is_enabled}.'''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#start_time ManagedInstanceAws#start_time}.'''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedInstanceAwsScheduledTask(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedInstanceAwsScheduledTaskList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsScheduledTaskList",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsScheduledTaskList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ManagedInstanceAwsScheduledTaskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsScheduledTaskList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ManagedInstanceAwsScheduledTaskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsScheduledTaskList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsScheduledTaskList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsScheduledTaskList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsScheduledTask]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsScheduledTask]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsScheduledTask]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsScheduledTaskList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManagedInstanceAwsScheduledTaskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsScheduledTaskOutputReference",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsScheduledTaskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCronExpression")
    def reset_cron_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCronExpression", []))

    @jsii.member(jsii_name="resetFrequency")
    def reset_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrequency", []))

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

    @builtins.property
    @jsii.member(jsii_name="cronExpressionInput")
    def cron_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cronExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="frequencyInput")
    def frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsScheduledTaskOutputReference, "cron_expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cronExpression", value)

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsScheduledTaskOutputReference, "frequency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsScheduledTaskOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsScheduledTaskOutputReference, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="taskType")
    def task_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskType"))

    @task_type.setter
    def task_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsScheduledTaskOutputReference, "task_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ManagedInstanceAwsScheduledTask, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ManagedInstanceAwsScheduledTask, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ManagedInstanceAwsScheduledTask, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsScheduledTaskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class ManagedInstanceAwsTags:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#key ManagedInstanceAws#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#value ManagedInstanceAws#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsTags.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#key ManagedInstanceAws#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/managed_instance_aws#value ManagedInstanceAws#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedInstanceAwsTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedInstanceAwsTagsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsTagsList",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsTagsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ManagedInstanceAwsTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedInstanceAwsTagsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ManagedInstanceAwsTagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsTagsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsTagsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsTagsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsTags]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedInstanceAwsTags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsTagsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManagedInstanceAwsTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.managedInstanceAws.ManagedInstanceAwsTagsOutputReference",
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
            type_hints = typing.get_type_hints(ManagedInstanceAwsTagsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

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
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsTagsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsTagsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ManagedInstanceAwsTags, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ManagedInstanceAwsTags, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ManagedInstanceAwsTags, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedInstanceAwsTagsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ManagedInstanceAws",
    "ManagedInstanceAwsBlockDeviceMappings",
    "ManagedInstanceAwsBlockDeviceMappingsEbs",
    "ManagedInstanceAwsBlockDeviceMappingsEbsOutputReference",
    "ManagedInstanceAwsBlockDeviceMappingsList",
    "ManagedInstanceAwsBlockDeviceMappingsOutputReference",
    "ManagedInstanceAwsConfig",
    "ManagedInstanceAwsIntegrationRoute53",
    "ManagedInstanceAwsIntegrationRoute53Domains",
    "ManagedInstanceAwsIntegrationRoute53DomainsList",
    "ManagedInstanceAwsIntegrationRoute53DomainsOutputReference",
    "ManagedInstanceAwsIntegrationRoute53DomainsRecordSets",
    "ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsList",
    "ManagedInstanceAwsIntegrationRoute53DomainsRecordSetsOutputReference",
    "ManagedInstanceAwsIntegrationRoute53OutputReference",
    "ManagedInstanceAwsLoadBalancers",
    "ManagedInstanceAwsLoadBalancersList",
    "ManagedInstanceAwsLoadBalancersOutputReference",
    "ManagedInstanceAwsManagedInstanceAction",
    "ManagedInstanceAwsManagedInstanceActionOutputReference",
    "ManagedInstanceAwsNetworkInterface",
    "ManagedInstanceAwsNetworkInterfaceList",
    "ManagedInstanceAwsNetworkInterfaceOutputReference",
    "ManagedInstanceAwsResourceTagSpecification",
    "ManagedInstanceAwsResourceTagSpecificationList",
    "ManagedInstanceAwsResourceTagSpecificationOutputReference",
    "ManagedInstanceAwsRevertToSpot",
    "ManagedInstanceAwsRevertToSpotOutputReference",
    "ManagedInstanceAwsScheduledTask",
    "ManagedInstanceAwsScheduledTaskList",
    "ManagedInstanceAwsScheduledTaskOutputReference",
    "ManagedInstanceAwsTags",
    "ManagedInstanceAwsTagsList",
    "ManagedInstanceAwsTagsOutputReference",
]

publication.publish()
