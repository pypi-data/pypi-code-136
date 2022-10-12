'''
# `spotinst_mrscaler_aws`

Refer to the Terraform Registory for docs: [`spotinst_mrscaler_aws`](https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws).
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


class MrscalerAws(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAws",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws spotinst_mrscaler_aws}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        strategy: builtins.str,
        additional_info: typing.Optional[builtins.str] = None,
        additional_primary_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        additional_replica_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        applications: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsApplications", typing.Dict[str, typing.Any]]]]] = None,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        bootstrap_actions_file: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsBootstrapActionsFile", typing.Dict[str, typing.Any]]]]] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        configurations_file: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsConfigurationsFile", typing.Dict[str, typing.Any]]]]] = None,
        core_desired_capacity: typing.Optional[jsii.Number] = None,
        core_ebs_block_device: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsCoreEbsBlockDevice", typing.Dict[str, typing.Any]]]]] = None,
        core_ebs_optimized: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        core_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        core_lifecycle: typing.Optional[builtins.str] = None,
        core_max_size: typing.Optional[jsii.Number] = None,
        core_min_size: typing.Optional[jsii.Number] = None,
        core_scaling_down_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsCoreScalingDownPolicy", typing.Dict[str, typing.Any]]]]] = None,
        core_scaling_up_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsCoreScalingUpPolicy", typing.Dict[str, typing.Any]]]]] = None,
        core_unit: typing.Optional[builtins.str] = None,
        custom_ami_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        ebs_root_volume_size: typing.Optional[jsii.Number] = None,
        ec2_key_name: typing.Optional[builtins.str] = None,
        expose_cluster_id: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        instance_weights: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsInstanceWeights", typing.Dict[str, typing.Any]]]]] = None,
        job_flow_role: typing.Optional[builtins.str] = None,
        keep_job_flow_alive: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_uri: typing.Optional[builtins.str] = None,
        managed_primary_security_group: typing.Optional[builtins.str] = None,
        managed_replica_security_group: typing.Optional[builtins.str] = None,
        master_ebs_block_device: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsMasterEbsBlockDevice", typing.Dict[str, typing.Any]]]]] = None,
        master_ebs_optimized: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        master_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        master_lifecycle: typing.Optional[builtins.str] = None,
        master_target: typing.Optional[jsii.Number] = None,
        provisioning_timeout: typing.Optional[typing.Union["MrscalerAwsProvisioningTimeout", typing.Dict[str, typing.Any]]] = None,
        region: typing.Optional[builtins.str] = None,
        release_label: typing.Optional[builtins.str] = None,
        repo_upgrade_on_boot: typing.Optional[builtins.str] = None,
        retries: typing.Optional[jsii.Number] = None,
        scheduled_task: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsScheduledTask", typing.Dict[str, typing.Any]]]]] = None,
        security_config: typing.Optional[builtins.str] = None,
        service_access_security_group: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[builtins.str] = None,
        steps_file: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsStepsFile", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsTags", typing.Dict[str, typing.Any]]]]] = None,
        task_desired_capacity: typing.Optional[jsii.Number] = None,
        task_ebs_block_device: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsTaskEbsBlockDevice", typing.Dict[str, typing.Any]]]]] = None,
        task_ebs_optimized: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        task_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        task_lifecycle: typing.Optional[builtins.str] = None,
        task_max_size: typing.Optional[jsii.Number] = None,
        task_min_size: typing.Optional[jsii.Number] = None,
        task_scaling_down_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsTaskScalingDownPolicy", typing.Dict[str, typing.Any]]]]] = None,
        task_scaling_up_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsTaskScalingUpPolicy", typing.Dict[str, typing.Any]]]]] = None,
        task_unit: typing.Optional[builtins.str] = None,
        termination_policies: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsTerminationPolicies", typing.Dict[str, typing.Any]]]]] = None,
        termination_protected: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        visible_to_all_users: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws spotinst_mrscaler_aws} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#name MrscalerAws#name}.
        :param strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#strategy MrscalerAws#strategy}.
        :param additional_info: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#additional_info MrscalerAws#additional_info}.
        :param additional_primary_security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#additional_primary_security_groups MrscalerAws#additional_primary_security_groups}.
        :param additional_replica_security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#additional_replica_security_groups MrscalerAws#additional_replica_security_groups}.
        :param applications: applications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#applications MrscalerAws#applications}
        :param availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#availability_zones MrscalerAws#availability_zones}.
        :param bootstrap_actions_file: bootstrap_actions_file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#bootstrap_actions_file MrscalerAws#bootstrap_actions_file}
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#cluster_id MrscalerAws#cluster_id}.
        :param configurations_file: configurations_file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#configurations_file MrscalerAws#configurations_file}
        :param core_desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_desired_capacity MrscalerAws#core_desired_capacity}.
        :param core_ebs_block_device: core_ebs_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_ebs_block_device MrscalerAws#core_ebs_block_device}
        :param core_ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_ebs_optimized MrscalerAws#core_ebs_optimized}.
        :param core_instance_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_instance_types MrscalerAws#core_instance_types}.
        :param core_lifecycle: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_lifecycle MrscalerAws#core_lifecycle}.
        :param core_max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_max_size MrscalerAws#core_max_size}.
        :param core_min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_min_size MrscalerAws#core_min_size}.
        :param core_scaling_down_policy: core_scaling_down_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_scaling_down_policy MrscalerAws#core_scaling_down_policy}
        :param core_scaling_up_policy: core_scaling_up_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_scaling_up_policy MrscalerAws#core_scaling_up_policy}
        :param core_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_unit MrscalerAws#core_unit}.
        :param custom_ami_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#custom_ami_id MrscalerAws#custom_ami_id}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#description MrscalerAws#description}.
        :param ebs_root_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#ebs_root_volume_size MrscalerAws#ebs_root_volume_size}.
        :param ec2_key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#ec2_key_name MrscalerAws#ec2_key_name}.
        :param expose_cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#expose_cluster_id MrscalerAws#expose_cluster_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#id MrscalerAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_weights: instance_weights block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#instance_weights MrscalerAws#instance_weights}
        :param job_flow_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#job_flow_role MrscalerAws#job_flow_role}.
        :param keep_job_flow_alive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#keep_job_flow_alive MrscalerAws#keep_job_flow_alive}.
        :param log_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#log_uri MrscalerAws#log_uri}.
        :param managed_primary_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#managed_primary_security_group MrscalerAws#managed_primary_security_group}.
        :param managed_replica_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#managed_replica_security_group MrscalerAws#managed_replica_security_group}.
        :param master_ebs_block_device: master_ebs_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#master_ebs_block_device MrscalerAws#master_ebs_block_device}
        :param master_ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#master_ebs_optimized MrscalerAws#master_ebs_optimized}.
        :param master_instance_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#master_instance_types MrscalerAws#master_instance_types}.
        :param master_lifecycle: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#master_lifecycle MrscalerAws#master_lifecycle}.
        :param master_target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#master_target MrscalerAws#master_target}.
        :param provisioning_timeout: provisioning_timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#provisioning_timeout MrscalerAws#provisioning_timeout}
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#region MrscalerAws#region}.
        :param release_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#release_label MrscalerAws#release_label}.
        :param repo_upgrade_on_boot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#repo_upgrade_on_boot MrscalerAws#repo_upgrade_on_boot}.
        :param retries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#retries MrscalerAws#retries}.
        :param scheduled_task: scheduled_task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#scheduled_task MrscalerAws#scheduled_task}
        :param security_config: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#security_config MrscalerAws#security_config}.
        :param service_access_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#service_access_security_group MrscalerAws#service_access_security_group}.
        :param service_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#service_role MrscalerAws#service_role}.
        :param steps_file: steps_file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#steps_file MrscalerAws#steps_file}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#tags MrscalerAws#tags}
        :param task_desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_desired_capacity MrscalerAws#task_desired_capacity}.
        :param task_ebs_block_device: task_ebs_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_ebs_block_device MrscalerAws#task_ebs_block_device}
        :param task_ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_ebs_optimized MrscalerAws#task_ebs_optimized}.
        :param task_instance_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_instance_types MrscalerAws#task_instance_types}.
        :param task_lifecycle: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_lifecycle MrscalerAws#task_lifecycle}.
        :param task_max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_max_size MrscalerAws#task_max_size}.
        :param task_min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_min_size MrscalerAws#task_min_size}.
        :param task_scaling_down_policy: task_scaling_down_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_scaling_down_policy MrscalerAws#task_scaling_down_policy}
        :param task_scaling_up_policy: task_scaling_up_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_scaling_up_policy MrscalerAws#task_scaling_up_policy}
        :param task_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_unit MrscalerAws#task_unit}.
        :param termination_policies: termination_policies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#termination_policies MrscalerAws#termination_policies}
        :param termination_protected: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#termination_protected MrscalerAws#termination_protected}.
        :param visible_to_all_users: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#visible_to_all_users MrscalerAws#visible_to_all_users}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAws.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MrscalerAwsConfig(
            name=name,
            strategy=strategy,
            additional_info=additional_info,
            additional_primary_security_groups=additional_primary_security_groups,
            additional_replica_security_groups=additional_replica_security_groups,
            applications=applications,
            availability_zones=availability_zones,
            bootstrap_actions_file=bootstrap_actions_file,
            cluster_id=cluster_id,
            configurations_file=configurations_file,
            core_desired_capacity=core_desired_capacity,
            core_ebs_block_device=core_ebs_block_device,
            core_ebs_optimized=core_ebs_optimized,
            core_instance_types=core_instance_types,
            core_lifecycle=core_lifecycle,
            core_max_size=core_max_size,
            core_min_size=core_min_size,
            core_scaling_down_policy=core_scaling_down_policy,
            core_scaling_up_policy=core_scaling_up_policy,
            core_unit=core_unit,
            custom_ami_id=custom_ami_id,
            description=description,
            ebs_root_volume_size=ebs_root_volume_size,
            ec2_key_name=ec2_key_name,
            expose_cluster_id=expose_cluster_id,
            id=id,
            instance_weights=instance_weights,
            job_flow_role=job_flow_role,
            keep_job_flow_alive=keep_job_flow_alive,
            log_uri=log_uri,
            managed_primary_security_group=managed_primary_security_group,
            managed_replica_security_group=managed_replica_security_group,
            master_ebs_block_device=master_ebs_block_device,
            master_ebs_optimized=master_ebs_optimized,
            master_instance_types=master_instance_types,
            master_lifecycle=master_lifecycle,
            master_target=master_target,
            provisioning_timeout=provisioning_timeout,
            region=region,
            release_label=release_label,
            repo_upgrade_on_boot=repo_upgrade_on_boot,
            retries=retries,
            scheduled_task=scheduled_task,
            security_config=security_config,
            service_access_security_group=service_access_security_group,
            service_role=service_role,
            steps_file=steps_file,
            tags=tags,
            task_desired_capacity=task_desired_capacity,
            task_ebs_block_device=task_ebs_block_device,
            task_ebs_optimized=task_ebs_optimized,
            task_instance_types=task_instance_types,
            task_lifecycle=task_lifecycle,
            task_max_size=task_max_size,
            task_min_size=task_min_size,
            task_scaling_down_policy=task_scaling_down_policy,
            task_scaling_up_policy=task_scaling_up_policy,
            task_unit=task_unit,
            termination_policies=termination_policies,
            termination_protected=termination_protected,
            visible_to_all_users=visible_to_all_users,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putApplications")
    def put_applications(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsApplications", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAws.put_applications)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putApplications", [value]))

    @jsii.member(jsii_name="putBootstrapActionsFile")
    def put_bootstrap_actions_file(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsBootstrapActionsFile", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAws.put_bootstrap_actions_file)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBootstrapActionsFile", [value]))

    @jsii.member(jsii_name="putConfigurationsFile")
    def put_configurations_file(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsConfigurationsFile", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAws.put_configurations_file)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConfigurationsFile", [value]))

    @jsii.member(jsii_name="putCoreEbsBlockDevice")
    def put_core_ebs_block_device(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsCoreEbsBlockDevice", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAws.put_core_ebs_block_device)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCoreEbsBlockDevice", [value]))

    @jsii.member(jsii_name="putCoreScalingDownPolicy")
    def put_core_scaling_down_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsCoreScalingDownPolicy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAws.put_core_scaling_down_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCoreScalingDownPolicy", [value]))

    @jsii.member(jsii_name="putCoreScalingUpPolicy")
    def put_core_scaling_up_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsCoreScalingUpPolicy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAws.put_core_scaling_up_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCoreScalingUpPolicy", [value]))

    @jsii.member(jsii_name="putInstanceWeights")
    def put_instance_weights(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsInstanceWeights", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAws.put_instance_weights)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInstanceWeights", [value]))

    @jsii.member(jsii_name="putMasterEbsBlockDevice")
    def put_master_ebs_block_device(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsMasterEbsBlockDevice", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAws.put_master_ebs_block_device)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMasterEbsBlockDevice", [value]))

    @jsii.member(jsii_name="putProvisioningTimeout")
    def put_provisioning_timeout(
        self,
        *,
        timeout: jsii.Number,
        timeout_action: builtins.str,
    ) -> None:
        '''
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#timeout MrscalerAws#timeout}.
        :param timeout_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#timeout_action MrscalerAws#timeout_action}.
        '''
        value = MrscalerAwsProvisioningTimeout(
            timeout=timeout, timeout_action=timeout_action
        )

        return typing.cast(None, jsii.invoke(self, "putProvisioningTimeout", [value]))

    @jsii.member(jsii_name="putScheduledTask")
    def put_scheduled_task(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsScheduledTask", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAws.put_scheduled_task)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScheduledTask", [value]))

    @jsii.member(jsii_name="putStepsFile")
    def put_steps_file(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsStepsFile", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAws.put_steps_file)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStepsFile", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsTags", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAws.put_tags)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="putTaskEbsBlockDevice")
    def put_task_ebs_block_device(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsTaskEbsBlockDevice", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAws.put_task_ebs_block_device)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTaskEbsBlockDevice", [value]))

    @jsii.member(jsii_name="putTaskScalingDownPolicy")
    def put_task_scaling_down_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsTaskScalingDownPolicy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAws.put_task_scaling_down_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTaskScalingDownPolicy", [value]))

    @jsii.member(jsii_name="putTaskScalingUpPolicy")
    def put_task_scaling_up_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsTaskScalingUpPolicy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAws.put_task_scaling_up_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTaskScalingUpPolicy", [value]))

    @jsii.member(jsii_name="putTerminationPolicies")
    def put_termination_policies(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsTerminationPolicies", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAws.put_termination_policies)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTerminationPolicies", [value]))

    @jsii.member(jsii_name="resetAdditionalInfo")
    def reset_additional_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalInfo", []))

    @jsii.member(jsii_name="resetAdditionalPrimarySecurityGroups")
    def reset_additional_primary_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalPrimarySecurityGroups", []))

    @jsii.member(jsii_name="resetAdditionalReplicaSecurityGroups")
    def reset_additional_replica_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalReplicaSecurityGroups", []))

    @jsii.member(jsii_name="resetApplications")
    def reset_applications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplications", []))

    @jsii.member(jsii_name="resetAvailabilityZones")
    def reset_availability_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityZones", []))

    @jsii.member(jsii_name="resetBootstrapActionsFile")
    def reset_bootstrap_actions_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootstrapActionsFile", []))

    @jsii.member(jsii_name="resetClusterId")
    def reset_cluster_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterId", []))

    @jsii.member(jsii_name="resetConfigurationsFile")
    def reset_configurations_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurationsFile", []))

    @jsii.member(jsii_name="resetCoreDesiredCapacity")
    def reset_core_desired_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreDesiredCapacity", []))

    @jsii.member(jsii_name="resetCoreEbsBlockDevice")
    def reset_core_ebs_block_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreEbsBlockDevice", []))

    @jsii.member(jsii_name="resetCoreEbsOptimized")
    def reset_core_ebs_optimized(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreEbsOptimized", []))

    @jsii.member(jsii_name="resetCoreInstanceTypes")
    def reset_core_instance_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreInstanceTypes", []))

    @jsii.member(jsii_name="resetCoreLifecycle")
    def reset_core_lifecycle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreLifecycle", []))

    @jsii.member(jsii_name="resetCoreMaxSize")
    def reset_core_max_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreMaxSize", []))

    @jsii.member(jsii_name="resetCoreMinSize")
    def reset_core_min_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreMinSize", []))

    @jsii.member(jsii_name="resetCoreScalingDownPolicy")
    def reset_core_scaling_down_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreScalingDownPolicy", []))

    @jsii.member(jsii_name="resetCoreScalingUpPolicy")
    def reset_core_scaling_up_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreScalingUpPolicy", []))

    @jsii.member(jsii_name="resetCoreUnit")
    def reset_core_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreUnit", []))

    @jsii.member(jsii_name="resetCustomAmiId")
    def reset_custom_ami_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomAmiId", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEbsRootVolumeSize")
    def reset_ebs_root_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsRootVolumeSize", []))

    @jsii.member(jsii_name="resetEc2KeyName")
    def reset_ec2_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEc2KeyName", []))

    @jsii.member(jsii_name="resetExposeClusterId")
    def reset_expose_cluster_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExposeClusterId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInstanceWeights")
    def reset_instance_weights(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceWeights", []))

    @jsii.member(jsii_name="resetJobFlowRole")
    def reset_job_flow_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobFlowRole", []))

    @jsii.member(jsii_name="resetKeepJobFlowAlive")
    def reset_keep_job_flow_alive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeepJobFlowAlive", []))

    @jsii.member(jsii_name="resetLogUri")
    def reset_log_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogUri", []))

    @jsii.member(jsii_name="resetManagedPrimarySecurityGroup")
    def reset_managed_primary_security_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedPrimarySecurityGroup", []))

    @jsii.member(jsii_name="resetManagedReplicaSecurityGroup")
    def reset_managed_replica_security_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedReplicaSecurityGroup", []))

    @jsii.member(jsii_name="resetMasterEbsBlockDevice")
    def reset_master_ebs_block_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterEbsBlockDevice", []))

    @jsii.member(jsii_name="resetMasterEbsOptimized")
    def reset_master_ebs_optimized(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterEbsOptimized", []))

    @jsii.member(jsii_name="resetMasterInstanceTypes")
    def reset_master_instance_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterInstanceTypes", []))

    @jsii.member(jsii_name="resetMasterLifecycle")
    def reset_master_lifecycle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterLifecycle", []))

    @jsii.member(jsii_name="resetMasterTarget")
    def reset_master_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterTarget", []))

    @jsii.member(jsii_name="resetProvisioningTimeout")
    def reset_provisioning_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvisioningTimeout", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetReleaseLabel")
    def reset_release_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReleaseLabel", []))

    @jsii.member(jsii_name="resetRepoUpgradeOnBoot")
    def reset_repo_upgrade_on_boot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepoUpgradeOnBoot", []))

    @jsii.member(jsii_name="resetRetries")
    def reset_retries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetries", []))

    @jsii.member(jsii_name="resetScheduledTask")
    def reset_scheduled_task(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduledTask", []))

    @jsii.member(jsii_name="resetSecurityConfig")
    def reset_security_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityConfig", []))

    @jsii.member(jsii_name="resetServiceAccessSecurityGroup")
    def reset_service_access_security_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccessSecurityGroup", []))

    @jsii.member(jsii_name="resetServiceRole")
    def reset_service_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRole", []))

    @jsii.member(jsii_name="resetStepsFile")
    def reset_steps_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStepsFile", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTaskDesiredCapacity")
    def reset_task_desired_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskDesiredCapacity", []))

    @jsii.member(jsii_name="resetTaskEbsBlockDevice")
    def reset_task_ebs_block_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskEbsBlockDevice", []))

    @jsii.member(jsii_name="resetTaskEbsOptimized")
    def reset_task_ebs_optimized(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskEbsOptimized", []))

    @jsii.member(jsii_name="resetTaskInstanceTypes")
    def reset_task_instance_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskInstanceTypes", []))

    @jsii.member(jsii_name="resetTaskLifecycle")
    def reset_task_lifecycle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskLifecycle", []))

    @jsii.member(jsii_name="resetTaskMaxSize")
    def reset_task_max_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskMaxSize", []))

    @jsii.member(jsii_name="resetTaskMinSize")
    def reset_task_min_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskMinSize", []))

    @jsii.member(jsii_name="resetTaskScalingDownPolicy")
    def reset_task_scaling_down_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskScalingDownPolicy", []))

    @jsii.member(jsii_name="resetTaskScalingUpPolicy")
    def reset_task_scaling_up_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskScalingUpPolicy", []))

    @jsii.member(jsii_name="resetTaskUnit")
    def reset_task_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskUnit", []))

    @jsii.member(jsii_name="resetTerminationPolicies")
    def reset_termination_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminationPolicies", []))

    @jsii.member(jsii_name="resetTerminationProtected")
    def reset_termination_protected(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminationProtected", []))

    @jsii.member(jsii_name="resetVisibleToAllUsers")
    def reset_visible_to_all_users(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVisibleToAllUsers", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="applications")
    def applications(self) -> "MrscalerAwsApplicationsList":
        return typing.cast("MrscalerAwsApplicationsList", jsii.get(self, "applications"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapActionsFile")
    def bootstrap_actions_file(self) -> "MrscalerAwsBootstrapActionsFileList":
        return typing.cast("MrscalerAwsBootstrapActionsFileList", jsii.get(self, "bootstrapActionsFile"))

    @builtins.property
    @jsii.member(jsii_name="configurationsFile")
    def configurations_file(self) -> "MrscalerAwsConfigurationsFileList":
        return typing.cast("MrscalerAwsConfigurationsFileList", jsii.get(self, "configurationsFile"))

    @builtins.property
    @jsii.member(jsii_name="coreEbsBlockDevice")
    def core_ebs_block_device(self) -> "MrscalerAwsCoreEbsBlockDeviceList":
        return typing.cast("MrscalerAwsCoreEbsBlockDeviceList", jsii.get(self, "coreEbsBlockDevice"))

    @builtins.property
    @jsii.member(jsii_name="coreScalingDownPolicy")
    def core_scaling_down_policy(self) -> "MrscalerAwsCoreScalingDownPolicyList":
        return typing.cast("MrscalerAwsCoreScalingDownPolicyList", jsii.get(self, "coreScalingDownPolicy"))

    @builtins.property
    @jsii.member(jsii_name="coreScalingUpPolicy")
    def core_scaling_up_policy(self) -> "MrscalerAwsCoreScalingUpPolicyList":
        return typing.cast("MrscalerAwsCoreScalingUpPolicyList", jsii.get(self, "coreScalingUpPolicy"))

    @builtins.property
    @jsii.member(jsii_name="instanceWeights")
    def instance_weights(self) -> "MrscalerAwsInstanceWeightsList":
        return typing.cast("MrscalerAwsInstanceWeightsList", jsii.get(self, "instanceWeights"))

    @builtins.property
    @jsii.member(jsii_name="masterEbsBlockDevice")
    def master_ebs_block_device(self) -> "MrscalerAwsMasterEbsBlockDeviceList":
        return typing.cast("MrscalerAwsMasterEbsBlockDeviceList", jsii.get(self, "masterEbsBlockDevice"))

    @builtins.property
    @jsii.member(jsii_name="outputClusterId")
    def output_cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputClusterId"))

    @builtins.property
    @jsii.member(jsii_name="provisioningTimeout")
    def provisioning_timeout(self) -> "MrscalerAwsProvisioningTimeoutOutputReference":
        return typing.cast("MrscalerAwsProvisioningTimeoutOutputReference", jsii.get(self, "provisioningTimeout"))

    @builtins.property
    @jsii.member(jsii_name="scheduledTask")
    def scheduled_task(self) -> "MrscalerAwsScheduledTaskList":
        return typing.cast("MrscalerAwsScheduledTaskList", jsii.get(self, "scheduledTask"))

    @builtins.property
    @jsii.member(jsii_name="stepsFile")
    def steps_file(self) -> "MrscalerAwsStepsFileList":
        return typing.cast("MrscalerAwsStepsFileList", jsii.get(self, "stepsFile"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "MrscalerAwsTagsList":
        return typing.cast("MrscalerAwsTagsList", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="taskEbsBlockDevice")
    def task_ebs_block_device(self) -> "MrscalerAwsTaskEbsBlockDeviceList":
        return typing.cast("MrscalerAwsTaskEbsBlockDeviceList", jsii.get(self, "taskEbsBlockDevice"))

    @builtins.property
    @jsii.member(jsii_name="taskScalingDownPolicy")
    def task_scaling_down_policy(self) -> "MrscalerAwsTaskScalingDownPolicyList":
        return typing.cast("MrscalerAwsTaskScalingDownPolicyList", jsii.get(self, "taskScalingDownPolicy"))

    @builtins.property
    @jsii.member(jsii_name="taskScalingUpPolicy")
    def task_scaling_up_policy(self) -> "MrscalerAwsTaskScalingUpPolicyList":
        return typing.cast("MrscalerAwsTaskScalingUpPolicyList", jsii.get(self, "taskScalingUpPolicy"))

    @builtins.property
    @jsii.member(jsii_name="terminationPolicies")
    def termination_policies(self) -> "MrscalerAwsTerminationPoliciesList":
        return typing.cast("MrscalerAwsTerminationPoliciesList", jsii.get(self, "terminationPolicies"))

    @builtins.property
    @jsii.member(jsii_name="additionalInfoInput")
    def additional_info_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "additionalInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalPrimarySecurityGroupsInput")
    def additional_primary_security_groups_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "additionalPrimarySecurityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalReplicaSecurityGroupsInput")
    def additional_replica_security_groups_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "additionalReplicaSecurityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationsInput")
    def applications_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsApplications"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsApplications"]]], jsii.get(self, "applicationsInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZonesInput")
    def availability_zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "availabilityZonesInput"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapActionsFileInput")
    def bootstrap_actions_file_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsBootstrapActionsFile"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsBootstrapActionsFile"]]], jsii.get(self, "bootstrapActionsFileInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationsFileInput")
    def configurations_file_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsConfigurationsFile"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsConfigurationsFile"]]], jsii.get(self, "configurationsFileInput"))

    @builtins.property
    @jsii.member(jsii_name="coreDesiredCapacityInput")
    def core_desired_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "coreDesiredCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="coreEbsBlockDeviceInput")
    def core_ebs_block_device_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsCoreEbsBlockDevice"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsCoreEbsBlockDevice"]]], jsii.get(self, "coreEbsBlockDeviceInput"))

    @builtins.property
    @jsii.member(jsii_name="coreEbsOptimizedInput")
    def core_ebs_optimized_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "coreEbsOptimizedInput"))

    @builtins.property
    @jsii.member(jsii_name="coreInstanceTypesInput")
    def core_instance_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "coreInstanceTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="coreLifecycleInput")
    def core_lifecycle_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "coreLifecycleInput"))

    @builtins.property
    @jsii.member(jsii_name="coreMaxSizeInput")
    def core_max_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "coreMaxSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="coreMinSizeInput")
    def core_min_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "coreMinSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="coreScalingDownPolicyInput")
    def core_scaling_down_policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsCoreScalingDownPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsCoreScalingDownPolicy"]]], jsii.get(self, "coreScalingDownPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="coreScalingUpPolicyInput")
    def core_scaling_up_policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsCoreScalingUpPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsCoreScalingUpPolicy"]]], jsii.get(self, "coreScalingUpPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="coreUnitInput")
    def core_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "coreUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="customAmiIdInput")
    def custom_ami_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customAmiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsRootVolumeSizeInput")
    def ebs_root_volume_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ebsRootVolumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="ec2KeyNameInput")
    def ec2_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ec2KeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="exposeClusterIdInput")
    def expose_cluster_id_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "exposeClusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceWeightsInput")
    def instance_weights_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsInstanceWeights"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsInstanceWeights"]]], jsii.get(self, "instanceWeightsInput"))

    @builtins.property
    @jsii.member(jsii_name="jobFlowRoleInput")
    def job_flow_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobFlowRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="keepJobFlowAliveInput")
    def keep_job_flow_alive_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "keepJobFlowAliveInput"))

    @builtins.property
    @jsii.member(jsii_name="logUriInput")
    def log_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logUriInput"))

    @builtins.property
    @jsii.member(jsii_name="managedPrimarySecurityGroupInput")
    def managed_primary_security_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedPrimarySecurityGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="managedReplicaSecurityGroupInput")
    def managed_replica_security_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedReplicaSecurityGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="masterEbsBlockDeviceInput")
    def master_ebs_block_device_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsMasterEbsBlockDevice"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsMasterEbsBlockDevice"]]], jsii.get(self, "masterEbsBlockDeviceInput"))

    @builtins.property
    @jsii.member(jsii_name="masterEbsOptimizedInput")
    def master_ebs_optimized_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "masterEbsOptimizedInput"))

    @builtins.property
    @jsii.member(jsii_name="masterInstanceTypesInput")
    def master_instance_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "masterInstanceTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="masterLifecycleInput")
    def master_lifecycle_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterLifecycleInput"))

    @builtins.property
    @jsii.member(jsii_name="masterTargetInput")
    def master_target_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "masterTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="provisioningTimeoutInput")
    def provisioning_timeout_input(
        self,
    ) -> typing.Optional["MrscalerAwsProvisioningTimeout"]:
        return typing.cast(typing.Optional["MrscalerAwsProvisioningTimeout"], jsii.get(self, "provisioningTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="releaseLabelInput")
    def release_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "releaseLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="repoUpgradeOnBootInput")
    def repo_upgrade_on_boot_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoUpgradeOnBootInput"))

    @builtins.property
    @jsii.member(jsii_name="retriesInput")
    def retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retriesInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduledTaskInput")
    def scheduled_task_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsScheduledTask"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsScheduledTask"]]], jsii.get(self, "scheduledTaskInput"))

    @builtins.property
    @jsii.member(jsii_name="securityConfigInput")
    def security_config_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccessSecurityGroupInput")
    def service_access_security_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccessSecurityGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleInput")
    def service_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="stepsFileInput")
    def steps_file_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsStepsFile"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsStepsFile"]]], jsii.get(self, "stepsFileInput"))

    @builtins.property
    @jsii.member(jsii_name="strategyInput")
    def strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "strategyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTags"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTags"]]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="taskDesiredCapacityInput")
    def task_desired_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "taskDesiredCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="taskEbsBlockDeviceInput")
    def task_ebs_block_device_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTaskEbsBlockDevice"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTaskEbsBlockDevice"]]], jsii.get(self, "taskEbsBlockDeviceInput"))

    @builtins.property
    @jsii.member(jsii_name="taskEbsOptimizedInput")
    def task_ebs_optimized_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "taskEbsOptimizedInput"))

    @builtins.property
    @jsii.member(jsii_name="taskInstanceTypesInput")
    def task_instance_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "taskInstanceTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="taskLifecycleInput")
    def task_lifecycle_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskLifecycleInput"))

    @builtins.property
    @jsii.member(jsii_name="taskMaxSizeInput")
    def task_max_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "taskMaxSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="taskMinSizeInput")
    def task_min_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "taskMinSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="taskScalingDownPolicyInput")
    def task_scaling_down_policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTaskScalingDownPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTaskScalingDownPolicy"]]], jsii.get(self, "taskScalingDownPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="taskScalingUpPolicyInput")
    def task_scaling_up_policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTaskScalingUpPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTaskScalingUpPolicy"]]], jsii.get(self, "taskScalingUpPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="taskUnitInput")
    def task_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="terminationPoliciesInput")
    def termination_policies_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTerminationPolicies"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTerminationPolicies"]]], jsii.get(self, "terminationPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="terminationProtectedInput")
    def termination_protected_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "terminationProtectedInput"))

    @builtins.property
    @jsii.member(jsii_name="visibleToAllUsersInput")
    def visible_to_all_users_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "visibleToAllUsersInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalInfo")
    def additional_info(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "additionalInfo"))

    @additional_info.setter
    def additional_info(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "additional_info").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalInfo", value)

    @builtins.property
    @jsii.member(jsii_name="additionalPrimarySecurityGroups")
    def additional_primary_security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "additionalPrimarySecurityGroups"))

    @additional_primary_security_groups.setter
    def additional_primary_security_groups(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "additional_primary_security_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalPrimarySecurityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="additionalReplicaSecurityGroups")
    def additional_replica_security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "additionalReplicaSecurityGroups"))

    @additional_replica_security_groups.setter
    def additional_replica_security_groups(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "additional_replica_security_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalReplicaSecurityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "availabilityZones"))

    @availability_zones.setter
    def availability_zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "availability_zones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZones", value)

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="coreDesiredCapacity")
    def core_desired_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "coreDesiredCapacity"))

    @core_desired_capacity.setter
    def core_desired_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "core_desired_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreDesiredCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="coreEbsOptimized")
    def core_ebs_optimized(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "coreEbsOptimized"))

    @core_ebs_optimized.setter
    def core_ebs_optimized(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "core_ebs_optimized").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreEbsOptimized", value)

    @builtins.property
    @jsii.member(jsii_name="coreInstanceTypes")
    def core_instance_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "coreInstanceTypes"))

    @core_instance_types.setter
    def core_instance_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "core_instance_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreInstanceTypes", value)

    @builtins.property
    @jsii.member(jsii_name="coreLifecycle")
    def core_lifecycle(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "coreLifecycle"))

    @core_lifecycle.setter
    def core_lifecycle(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "core_lifecycle").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreLifecycle", value)

    @builtins.property
    @jsii.member(jsii_name="coreMaxSize")
    def core_max_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "coreMaxSize"))

    @core_max_size.setter
    def core_max_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "core_max_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreMaxSize", value)

    @builtins.property
    @jsii.member(jsii_name="coreMinSize")
    def core_min_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "coreMinSize"))

    @core_min_size.setter
    def core_min_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "core_min_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreMinSize", value)

    @builtins.property
    @jsii.member(jsii_name="coreUnit")
    def core_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "coreUnit"))

    @core_unit.setter
    def core_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "core_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreUnit", value)

    @builtins.property
    @jsii.member(jsii_name="customAmiId")
    def custom_ami_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customAmiId"))

    @custom_ami_id.setter
    def custom_ami_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "custom_ami_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customAmiId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="ebsRootVolumeSize")
    def ebs_root_volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsRootVolumeSize"))

    @ebs_root_volume_size.setter
    def ebs_root_volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "ebs_root_volume_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsRootVolumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="ec2KeyName")
    def ec2_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ec2KeyName"))

    @ec2_key_name.setter
    def ec2_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "ec2_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2KeyName", value)

    @builtins.property
    @jsii.member(jsii_name="exposeClusterId")
    def expose_cluster_id(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "exposeClusterId"))

    @expose_cluster_id.setter
    def expose_cluster_id(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "expose_cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exposeClusterId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="jobFlowRole")
    def job_flow_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobFlowRole"))

    @job_flow_role.setter
    def job_flow_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "job_flow_role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobFlowRole", value)

    @builtins.property
    @jsii.member(jsii_name="keepJobFlowAlive")
    def keep_job_flow_alive(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "keepJobFlowAlive"))

    @keep_job_flow_alive.setter
    def keep_job_flow_alive(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "keep_job_flow_alive").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keepJobFlowAlive", value)

    @builtins.property
    @jsii.member(jsii_name="logUri")
    def log_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logUri"))

    @log_uri.setter
    def log_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "log_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logUri", value)

    @builtins.property
    @jsii.member(jsii_name="managedPrimarySecurityGroup")
    def managed_primary_security_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedPrimarySecurityGroup"))

    @managed_primary_security_group.setter
    def managed_primary_security_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "managed_primary_security_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedPrimarySecurityGroup", value)

    @builtins.property
    @jsii.member(jsii_name="managedReplicaSecurityGroup")
    def managed_replica_security_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedReplicaSecurityGroup"))

    @managed_replica_security_group.setter
    def managed_replica_security_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "managed_replica_security_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedReplicaSecurityGroup", value)

    @builtins.property
    @jsii.member(jsii_name="masterEbsOptimized")
    def master_ebs_optimized(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "masterEbsOptimized"))

    @master_ebs_optimized.setter
    def master_ebs_optimized(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "master_ebs_optimized").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterEbsOptimized", value)

    @builtins.property
    @jsii.member(jsii_name="masterInstanceTypes")
    def master_instance_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "masterInstanceTypes"))

    @master_instance_types.setter
    def master_instance_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "master_instance_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterInstanceTypes", value)

    @builtins.property
    @jsii.member(jsii_name="masterLifecycle")
    def master_lifecycle(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterLifecycle"))

    @master_lifecycle.setter
    def master_lifecycle(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "master_lifecycle").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterLifecycle", value)

    @builtins.property
    @jsii.member(jsii_name="masterTarget")
    def master_target(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "masterTarget"))

    @master_target.setter
    def master_target(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "master_target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterTarget", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="releaseLabel")
    def release_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "releaseLabel"))

    @release_label.setter
    def release_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "release_label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "releaseLabel", value)

    @builtins.property
    @jsii.member(jsii_name="repoUpgradeOnBoot")
    def repo_upgrade_on_boot(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repoUpgradeOnBoot"))

    @repo_upgrade_on_boot.setter
    def repo_upgrade_on_boot(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "repo_upgrade_on_boot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repoUpgradeOnBoot", value)

    @builtins.property
    @jsii.member(jsii_name="retries")
    def retries(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retries"))

    @retries.setter
    def retries(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "retries").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retries", value)

    @builtins.property
    @jsii.member(jsii_name="securityConfig")
    def security_config(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityConfig"))

    @security_config.setter
    def security_config(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "security_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityConfig", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccessSecurityGroup")
    def service_access_security_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessSecurityGroup"))

    @service_access_security_group.setter
    def service_access_security_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "service_access_security_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccessSecurityGroup", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRole"))

    @service_role.setter
    def service_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "service_role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRole", value)

    @builtins.property
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "strategy"))

    @strategy.setter
    def strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "strategy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "strategy", value)

    @builtins.property
    @jsii.member(jsii_name="taskDesiredCapacity")
    def task_desired_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "taskDesiredCapacity"))

    @task_desired_capacity.setter
    def task_desired_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "task_desired_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskDesiredCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="taskEbsOptimized")
    def task_ebs_optimized(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "taskEbsOptimized"))

    @task_ebs_optimized.setter
    def task_ebs_optimized(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "task_ebs_optimized").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskEbsOptimized", value)

    @builtins.property
    @jsii.member(jsii_name="taskInstanceTypes")
    def task_instance_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "taskInstanceTypes"))

    @task_instance_types.setter
    def task_instance_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "task_instance_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskInstanceTypes", value)

    @builtins.property
    @jsii.member(jsii_name="taskLifecycle")
    def task_lifecycle(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskLifecycle"))

    @task_lifecycle.setter
    def task_lifecycle(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "task_lifecycle").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskLifecycle", value)

    @builtins.property
    @jsii.member(jsii_name="taskMaxSize")
    def task_max_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "taskMaxSize"))

    @task_max_size.setter
    def task_max_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "task_max_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskMaxSize", value)

    @builtins.property
    @jsii.member(jsii_name="taskMinSize")
    def task_min_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "taskMinSize"))

    @task_min_size.setter
    def task_min_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "task_min_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskMinSize", value)

    @builtins.property
    @jsii.member(jsii_name="taskUnit")
    def task_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskUnit"))

    @task_unit.setter
    def task_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "task_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskUnit", value)

    @builtins.property
    @jsii.member(jsii_name="terminationProtected")
    def termination_protected(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "terminationProtected"))

    @termination_protected.setter
    def termination_protected(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "termination_protected").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terminationProtected", value)

    @builtins.property
    @jsii.member(jsii_name="visibleToAllUsers")
    def visible_to_all_users(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "visibleToAllUsers"))

    @visible_to_all_users.setter
    def visible_to_all_users(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAws, "visible_to_all_users").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibleToAllUsers", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsApplications",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "args": "args", "version": "version"},
)
class MrscalerAwsApplications:
    def __init__(
        self,
        *,
        name: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#name MrscalerAws#name}.
        :param args: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#args MrscalerAws#args}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#version MrscalerAws#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsApplications.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if args is not None:
            self._values["args"] = args
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#name MrscalerAws#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#args MrscalerAws#args}.'''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#version MrscalerAws#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MrscalerAwsApplications(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MrscalerAwsApplicationsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsApplicationsList",
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
            type_hints = typing.get_type_hints(MrscalerAwsApplicationsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MrscalerAwsApplicationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsApplicationsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MrscalerAwsApplicationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsApplicationsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsApplicationsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsApplicationsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsApplications]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsApplications]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsApplications]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsApplicationsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MrscalerAwsApplicationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsApplicationsOutputReference",
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
            type_hints = typing.get_type_hints(MrscalerAwsApplicationsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetArgs")
    def reset_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgs", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="argsInput")
    def args_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="args")
    def args(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "args"))

    @args.setter
    def args(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsApplicationsOutputReference, "args").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "args", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsApplicationsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsApplicationsOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MrscalerAwsApplications, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MrscalerAwsApplications, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MrscalerAwsApplications, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsApplicationsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsBootstrapActionsFile",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "key": "key"},
)
class MrscalerAwsBootstrapActionsFile:
    def __init__(self, *, bucket: builtins.str, key: builtins.str) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#bucket MrscalerAws#bucket}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#key MrscalerAws#key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsBootstrapActionsFile.__init__)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "key": key,
        }

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#bucket MrscalerAws#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#key MrscalerAws#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MrscalerAwsBootstrapActionsFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MrscalerAwsBootstrapActionsFileList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsBootstrapActionsFileList",
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
            type_hints = typing.get_type_hints(MrscalerAwsBootstrapActionsFileList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MrscalerAwsBootstrapActionsFileOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsBootstrapActionsFileList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MrscalerAwsBootstrapActionsFileOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsBootstrapActionsFileList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsBootstrapActionsFileList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsBootstrapActionsFileList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsBootstrapActionsFile]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsBootstrapActionsFile]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsBootstrapActionsFile]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsBootstrapActionsFileList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MrscalerAwsBootstrapActionsFileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsBootstrapActionsFileOutputReference",
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
            type_hints = typing.get_type_hints(MrscalerAwsBootstrapActionsFileOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsBootstrapActionsFileOutputReference, "bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsBootstrapActionsFileOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MrscalerAwsBootstrapActionsFile, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MrscalerAwsBootstrapActionsFile, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MrscalerAwsBootstrapActionsFile, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsBootstrapActionsFileOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsConfig",
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
        "strategy": "strategy",
        "additional_info": "additionalInfo",
        "additional_primary_security_groups": "additionalPrimarySecurityGroups",
        "additional_replica_security_groups": "additionalReplicaSecurityGroups",
        "applications": "applications",
        "availability_zones": "availabilityZones",
        "bootstrap_actions_file": "bootstrapActionsFile",
        "cluster_id": "clusterId",
        "configurations_file": "configurationsFile",
        "core_desired_capacity": "coreDesiredCapacity",
        "core_ebs_block_device": "coreEbsBlockDevice",
        "core_ebs_optimized": "coreEbsOptimized",
        "core_instance_types": "coreInstanceTypes",
        "core_lifecycle": "coreLifecycle",
        "core_max_size": "coreMaxSize",
        "core_min_size": "coreMinSize",
        "core_scaling_down_policy": "coreScalingDownPolicy",
        "core_scaling_up_policy": "coreScalingUpPolicy",
        "core_unit": "coreUnit",
        "custom_ami_id": "customAmiId",
        "description": "description",
        "ebs_root_volume_size": "ebsRootVolumeSize",
        "ec2_key_name": "ec2KeyName",
        "expose_cluster_id": "exposeClusterId",
        "id": "id",
        "instance_weights": "instanceWeights",
        "job_flow_role": "jobFlowRole",
        "keep_job_flow_alive": "keepJobFlowAlive",
        "log_uri": "logUri",
        "managed_primary_security_group": "managedPrimarySecurityGroup",
        "managed_replica_security_group": "managedReplicaSecurityGroup",
        "master_ebs_block_device": "masterEbsBlockDevice",
        "master_ebs_optimized": "masterEbsOptimized",
        "master_instance_types": "masterInstanceTypes",
        "master_lifecycle": "masterLifecycle",
        "master_target": "masterTarget",
        "provisioning_timeout": "provisioningTimeout",
        "region": "region",
        "release_label": "releaseLabel",
        "repo_upgrade_on_boot": "repoUpgradeOnBoot",
        "retries": "retries",
        "scheduled_task": "scheduledTask",
        "security_config": "securityConfig",
        "service_access_security_group": "serviceAccessSecurityGroup",
        "service_role": "serviceRole",
        "steps_file": "stepsFile",
        "tags": "tags",
        "task_desired_capacity": "taskDesiredCapacity",
        "task_ebs_block_device": "taskEbsBlockDevice",
        "task_ebs_optimized": "taskEbsOptimized",
        "task_instance_types": "taskInstanceTypes",
        "task_lifecycle": "taskLifecycle",
        "task_max_size": "taskMaxSize",
        "task_min_size": "taskMinSize",
        "task_scaling_down_policy": "taskScalingDownPolicy",
        "task_scaling_up_policy": "taskScalingUpPolicy",
        "task_unit": "taskUnit",
        "termination_policies": "terminationPolicies",
        "termination_protected": "terminationProtected",
        "visible_to_all_users": "visibleToAllUsers",
    },
)
class MrscalerAwsConfig(cdktf.TerraformMetaArguments):
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
        strategy: builtins.str,
        additional_info: typing.Optional[builtins.str] = None,
        additional_primary_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        additional_replica_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        applications: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MrscalerAwsApplications, typing.Dict[str, typing.Any]]]]] = None,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        bootstrap_actions_file: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MrscalerAwsBootstrapActionsFile, typing.Dict[str, typing.Any]]]]] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        configurations_file: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsConfigurationsFile", typing.Dict[str, typing.Any]]]]] = None,
        core_desired_capacity: typing.Optional[jsii.Number] = None,
        core_ebs_block_device: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsCoreEbsBlockDevice", typing.Dict[str, typing.Any]]]]] = None,
        core_ebs_optimized: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        core_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        core_lifecycle: typing.Optional[builtins.str] = None,
        core_max_size: typing.Optional[jsii.Number] = None,
        core_min_size: typing.Optional[jsii.Number] = None,
        core_scaling_down_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsCoreScalingDownPolicy", typing.Dict[str, typing.Any]]]]] = None,
        core_scaling_up_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsCoreScalingUpPolicy", typing.Dict[str, typing.Any]]]]] = None,
        core_unit: typing.Optional[builtins.str] = None,
        custom_ami_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        ebs_root_volume_size: typing.Optional[jsii.Number] = None,
        ec2_key_name: typing.Optional[builtins.str] = None,
        expose_cluster_id: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        instance_weights: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsInstanceWeights", typing.Dict[str, typing.Any]]]]] = None,
        job_flow_role: typing.Optional[builtins.str] = None,
        keep_job_flow_alive: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_uri: typing.Optional[builtins.str] = None,
        managed_primary_security_group: typing.Optional[builtins.str] = None,
        managed_replica_security_group: typing.Optional[builtins.str] = None,
        master_ebs_block_device: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsMasterEbsBlockDevice", typing.Dict[str, typing.Any]]]]] = None,
        master_ebs_optimized: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        master_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        master_lifecycle: typing.Optional[builtins.str] = None,
        master_target: typing.Optional[jsii.Number] = None,
        provisioning_timeout: typing.Optional[typing.Union["MrscalerAwsProvisioningTimeout", typing.Dict[str, typing.Any]]] = None,
        region: typing.Optional[builtins.str] = None,
        release_label: typing.Optional[builtins.str] = None,
        repo_upgrade_on_boot: typing.Optional[builtins.str] = None,
        retries: typing.Optional[jsii.Number] = None,
        scheduled_task: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsScheduledTask", typing.Dict[str, typing.Any]]]]] = None,
        security_config: typing.Optional[builtins.str] = None,
        service_access_security_group: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[builtins.str] = None,
        steps_file: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsStepsFile", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsTags", typing.Dict[str, typing.Any]]]]] = None,
        task_desired_capacity: typing.Optional[jsii.Number] = None,
        task_ebs_block_device: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsTaskEbsBlockDevice", typing.Dict[str, typing.Any]]]]] = None,
        task_ebs_optimized: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        task_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        task_lifecycle: typing.Optional[builtins.str] = None,
        task_max_size: typing.Optional[jsii.Number] = None,
        task_min_size: typing.Optional[jsii.Number] = None,
        task_scaling_down_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsTaskScalingDownPolicy", typing.Dict[str, typing.Any]]]]] = None,
        task_scaling_up_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsTaskScalingUpPolicy", typing.Dict[str, typing.Any]]]]] = None,
        task_unit: typing.Optional[builtins.str] = None,
        termination_policies: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsTerminationPolicies", typing.Dict[str, typing.Any]]]]] = None,
        termination_protected: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        visible_to_all_users: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#name MrscalerAws#name}.
        :param strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#strategy MrscalerAws#strategy}.
        :param additional_info: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#additional_info MrscalerAws#additional_info}.
        :param additional_primary_security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#additional_primary_security_groups MrscalerAws#additional_primary_security_groups}.
        :param additional_replica_security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#additional_replica_security_groups MrscalerAws#additional_replica_security_groups}.
        :param applications: applications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#applications MrscalerAws#applications}
        :param availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#availability_zones MrscalerAws#availability_zones}.
        :param bootstrap_actions_file: bootstrap_actions_file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#bootstrap_actions_file MrscalerAws#bootstrap_actions_file}
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#cluster_id MrscalerAws#cluster_id}.
        :param configurations_file: configurations_file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#configurations_file MrscalerAws#configurations_file}
        :param core_desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_desired_capacity MrscalerAws#core_desired_capacity}.
        :param core_ebs_block_device: core_ebs_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_ebs_block_device MrscalerAws#core_ebs_block_device}
        :param core_ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_ebs_optimized MrscalerAws#core_ebs_optimized}.
        :param core_instance_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_instance_types MrscalerAws#core_instance_types}.
        :param core_lifecycle: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_lifecycle MrscalerAws#core_lifecycle}.
        :param core_max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_max_size MrscalerAws#core_max_size}.
        :param core_min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_min_size MrscalerAws#core_min_size}.
        :param core_scaling_down_policy: core_scaling_down_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_scaling_down_policy MrscalerAws#core_scaling_down_policy}
        :param core_scaling_up_policy: core_scaling_up_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_scaling_up_policy MrscalerAws#core_scaling_up_policy}
        :param core_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_unit MrscalerAws#core_unit}.
        :param custom_ami_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#custom_ami_id MrscalerAws#custom_ami_id}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#description MrscalerAws#description}.
        :param ebs_root_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#ebs_root_volume_size MrscalerAws#ebs_root_volume_size}.
        :param ec2_key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#ec2_key_name MrscalerAws#ec2_key_name}.
        :param expose_cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#expose_cluster_id MrscalerAws#expose_cluster_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#id MrscalerAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_weights: instance_weights block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#instance_weights MrscalerAws#instance_weights}
        :param job_flow_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#job_flow_role MrscalerAws#job_flow_role}.
        :param keep_job_flow_alive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#keep_job_flow_alive MrscalerAws#keep_job_flow_alive}.
        :param log_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#log_uri MrscalerAws#log_uri}.
        :param managed_primary_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#managed_primary_security_group MrscalerAws#managed_primary_security_group}.
        :param managed_replica_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#managed_replica_security_group MrscalerAws#managed_replica_security_group}.
        :param master_ebs_block_device: master_ebs_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#master_ebs_block_device MrscalerAws#master_ebs_block_device}
        :param master_ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#master_ebs_optimized MrscalerAws#master_ebs_optimized}.
        :param master_instance_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#master_instance_types MrscalerAws#master_instance_types}.
        :param master_lifecycle: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#master_lifecycle MrscalerAws#master_lifecycle}.
        :param master_target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#master_target MrscalerAws#master_target}.
        :param provisioning_timeout: provisioning_timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#provisioning_timeout MrscalerAws#provisioning_timeout}
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#region MrscalerAws#region}.
        :param release_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#release_label MrscalerAws#release_label}.
        :param repo_upgrade_on_boot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#repo_upgrade_on_boot MrscalerAws#repo_upgrade_on_boot}.
        :param retries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#retries MrscalerAws#retries}.
        :param scheduled_task: scheduled_task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#scheduled_task MrscalerAws#scheduled_task}
        :param security_config: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#security_config MrscalerAws#security_config}.
        :param service_access_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#service_access_security_group MrscalerAws#service_access_security_group}.
        :param service_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#service_role MrscalerAws#service_role}.
        :param steps_file: steps_file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#steps_file MrscalerAws#steps_file}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#tags MrscalerAws#tags}
        :param task_desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_desired_capacity MrscalerAws#task_desired_capacity}.
        :param task_ebs_block_device: task_ebs_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_ebs_block_device MrscalerAws#task_ebs_block_device}
        :param task_ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_ebs_optimized MrscalerAws#task_ebs_optimized}.
        :param task_instance_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_instance_types MrscalerAws#task_instance_types}.
        :param task_lifecycle: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_lifecycle MrscalerAws#task_lifecycle}.
        :param task_max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_max_size MrscalerAws#task_max_size}.
        :param task_min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_min_size MrscalerAws#task_min_size}.
        :param task_scaling_down_policy: task_scaling_down_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_scaling_down_policy MrscalerAws#task_scaling_down_policy}
        :param task_scaling_up_policy: task_scaling_up_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_scaling_up_policy MrscalerAws#task_scaling_up_policy}
        :param task_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_unit MrscalerAws#task_unit}.
        :param termination_policies: termination_policies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#termination_policies MrscalerAws#termination_policies}
        :param termination_protected: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#termination_protected MrscalerAws#termination_protected}.
        :param visible_to_all_users: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#visible_to_all_users MrscalerAws#visible_to_all_users}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(provisioning_timeout, dict):
            provisioning_timeout = MrscalerAwsProvisioningTimeout(**provisioning_timeout)
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument strategy", value=strategy, expected_type=type_hints["strategy"])
            check_type(argname="argument additional_info", value=additional_info, expected_type=type_hints["additional_info"])
            check_type(argname="argument additional_primary_security_groups", value=additional_primary_security_groups, expected_type=type_hints["additional_primary_security_groups"])
            check_type(argname="argument additional_replica_security_groups", value=additional_replica_security_groups, expected_type=type_hints["additional_replica_security_groups"])
            check_type(argname="argument applications", value=applications, expected_type=type_hints["applications"])
            check_type(argname="argument availability_zones", value=availability_zones, expected_type=type_hints["availability_zones"])
            check_type(argname="argument bootstrap_actions_file", value=bootstrap_actions_file, expected_type=type_hints["bootstrap_actions_file"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument configurations_file", value=configurations_file, expected_type=type_hints["configurations_file"])
            check_type(argname="argument core_desired_capacity", value=core_desired_capacity, expected_type=type_hints["core_desired_capacity"])
            check_type(argname="argument core_ebs_block_device", value=core_ebs_block_device, expected_type=type_hints["core_ebs_block_device"])
            check_type(argname="argument core_ebs_optimized", value=core_ebs_optimized, expected_type=type_hints["core_ebs_optimized"])
            check_type(argname="argument core_instance_types", value=core_instance_types, expected_type=type_hints["core_instance_types"])
            check_type(argname="argument core_lifecycle", value=core_lifecycle, expected_type=type_hints["core_lifecycle"])
            check_type(argname="argument core_max_size", value=core_max_size, expected_type=type_hints["core_max_size"])
            check_type(argname="argument core_min_size", value=core_min_size, expected_type=type_hints["core_min_size"])
            check_type(argname="argument core_scaling_down_policy", value=core_scaling_down_policy, expected_type=type_hints["core_scaling_down_policy"])
            check_type(argname="argument core_scaling_up_policy", value=core_scaling_up_policy, expected_type=type_hints["core_scaling_up_policy"])
            check_type(argname="argument core_unit", value=core_unit, expected_type=type_hints["core_unit"])
            check_type(argname="argument custom_ami_id", value=custom_ami_id, expected_type=type_hints["custom_ami_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument ebs_root_volume_size", value=ebs_root_volume_size, expected_type=type_hints["ebs_root_volume_size"])
            check_type(argname="argument ec2_key_name", value=ec2_key_name, expected_type=type_hints["ec2_key_name"])
            check_type(argname="argument expose_cluster_id", value=expose_cluster_id, expected_type=type_hints["expose_cluster_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instance_weights", value=instance_weights, expected_type=type_hints["instance_weights"])
            check_type(argname="argument job_flow_role", value=job_flow_role, expected_type=type_hints["job_flow_role"])
            check_type(argname="argument keep_job_flow_alive", value=keep_job_flow_alive, expected_type=type_hints["keep_job_flow_alive"])
            check_type(argname="argument log_uri", value=log_uri, expected_type=type_hints["log_uri"])
            check_type(argname="argument managed_primary_security_group", value=managed_primary_security_group, expected_type=type_hints["managed_primary_security_group"])
            check_type(argname="argument managed_replica_security_group", value=managed_replica_security_group, expected_type=type_hints["managed_replica_security_group"])
            check_type(argname="argument master_ebs_block_device", value=master_ebs_block_device, expected_type=type_hints["master_ebs_block_device"])
            check_type(argname="argument master_ebs_optimized", value=master_ebs_optimized, expected_type=type_hints["master_ebs_optimized"])
            check_type(argname="argument master_instance_types", value=master_instance_types, expected_type=type_hints["master_instance_types"])
            check_type(argname="argument master_lifecycle", value=master_lifecycle, expected_type=type_hints["master_lifecycle"])
            check_type(argname="argument master_target", value=master_target, expected_type=type_hints["master_target"])
            check_type(argname="argument provisioning_timeout", value=provisioning_timeout, expected_type=type_hints["provisioning_timeout"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument release_label", value=release_label, expected_type=type_hints["release_label"])
            check_type(argname="argument repo_upgrade_on_boot", value=repo_upgrade_on_boot, expected_type=type_hints["repo_upgrade_on_boot"])
            check_type(argname="argument retries", value=retries, expected_type=type_hints["retries"])
            check_type(argname="argument scheduled_task", value=scheduled_task, expected_type=type_hints["scheduled_task"])
            check_type(argname="argument security_config", value=security_config, expected_type=type_hints["security_config"])
            check_type(argname="argument service_access_security_group", value=service_access_security_group, expected_type=type_hints["service_access_security_group"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument steps_file", value=steps_file, expected_type=type_hints["steps_file"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument task_desired_capacity", value=task_desired_capacity, expected_type=type_hints["task_desired_capacity"])
            check_type(argname="argument task_ebs_block_device", value=task_ebs_block_device, expected_type=type_hints["task_ebs_block_device"])
            check_type(argname="argument task_ebs_optimized", value=task_ebs_optimized, expected_type=type_hints["task_ebs_optimized"])
            check_type(argname="argument task_instance_types", value=task_instance_types, expected_type=type_hints["task_instance_types"])
            check_type(argname="argument task_lifecycle", value=task_lifecycle, expected_type=type_hints["task_lifecycle"])
            check_type(argname="argument task_max_size", value=task_max_size, expected_type=type_hints["task_max_size"])
            check_type(argname="argument task_min_size", value=task_min_size, expected_type=type_hints["task_min_size"])
            check_type(argname="argument task_scaling_down_policy", value=task_scaling_down_policy, expected_type=type_hints["task_scaling_down_policy"])
            check_type(argname="argument task_scaling_up_policy", value=task_scaling_up_policy, expected_type=type_hints["task_scaling_up_policy"])
            check_type(argname="argument task_unit", value=task_unit, expected_type=type_hints["task_unit"])
            check_type(argname="argument termination_policies", value=termination_policies, expected_type=type_hints["termination_policies"])
            check_type(argname="argument termination_protected", value=termination_protected, expected_type=type_hints["termination_protected"])
            check_type(argname="argument visible_to_all_users", value=visible_to_all_users, expected_type=type_hints["visible_to_all_users"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "strategy": strategy,
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
        if additional_info is not None:
            self._values["additional_info"] = additional_info
        if additional_primary_security_groups is not None:
            self._values["additional_primary_security_groups"] = additional_primary_security_groups
        if additional_replica_security_groups is not None:
            self._values["additional_replica_security_groups"] = additional_replica_security_groups
        if applications is not None:
            self._values["applications"] = applications
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if bootstrap_actions_file is not None:
            self._values["bootstrap_actions_file"] = bootstrap_actions_file
        if cluster_id is not None:
            self._values["cluster_id"] = cluster_id
        if configurations_file is not None:
            self._values["configurations_file"] = configurations_file
        if core_desired_capacity is not None:
            self._values["core_desired_capacity"] = core_desired_capacity
        if core_ebs_block_device is not None:
            self._values["core_ebs_block_device"] = core_ebs_block_device
        if core_ebs_optimized is not None:
            self._values["core_ebs_optimized"] = core_ebs_optimized
        if core_instance_types is not None:
            self._values["core_instance_types"] = core_instance_types
        if core_lifecycle is not None:
            self._values["core_lifecycle"] = core_lifecycle
        if core_max_size is not None:
            self._values["core_max_size"] = core_max_size
        if core_min_size is not None:
            self._values["core_min_size"] = core_min_size
        if core_scaling_down_policy is not None:
            self._values["core_scaling_down_policy"] = core_scaling_down_policy
        if core_scaling_up_policy is not None:
            self._values["core_scaling_up_policy"] = core_scaling_up_policy
        if core_unit is not None:
            self._values["core_unit"] = core_unit
        if custom_ami_id is not None:
            self._values["custom_ami_id"] = custom_ami_id
        if description is not None:
            self._values["description"] = description
        if ebs_root_volume_size is not None:
            self._values["ebs_root_volume_size"] = ebs_root_volume_size
        if ec2_key_name is not None:
            self._values["ec2_key_name"] = ec2_key_name
        if expose_cluster_id is not None:
            self._values["expose_cluster_id"] = expose_cluster_id
        if id is not None:
            self._values["id"] = id
        if instance_weights is not None:
            self._values["instance_weights"] = instance_weights
        if job_flow_role is not None:
            self._values["job_flow_role"] = job_flow_role
        if keep_job_flow_alive is not None:
            self._values["keep_job_flow_alive"] = keep_job_flow_alive
        if log_uri is not None:
            self._values["log_uri"] = log_uri
        if managed_primary_security_group is not None:
            self._values["managed_primary_security_group"] = managed_primary_security_group
        if managed_replica_security_group is not None:
            self._values["managed_replica_security_group"] = managed_replica_security_group
        if master_ebs_block_device is not None:
            self._values["master_ebs_block_device"] = master_ebs_block_device
        if master_ebs_optimized is not None:
            self._values["master_ebs_optimized"] = master_ebs_optimized
        if master_instance_types is not None:
            self._values["master_instance_types"] = master_instance_types
        if master_lifecycle is not None:
            self._values["master_lifecycle"] = master_lifecycle
        if master_target is not None:
            self._values["master_target"] = master_target
        if provisioning_timeout is not None:
            self._values["provisioning_timeout"] = provisioning_timeout
        if region is not None:
            self._values["region"] = region
        if release_label is not None:
            self._values["release_label"] = release_label
        if repo_upgrade_on_boot is not None:
            self._values["repo_upgrade_on_boot"] = repo_upgrade_on_boot
        if retries is not None:
            self._values["retries"] = retries
        if scheduled_task is not None:
            self._values["scheduled_task"] = scheduled_task
        if security_config is not None:
            self._values["security_config"] = security_config
        if service_access_security_group is not None:
            self._values["service_access_security_group"] = service_access_security_group
        if service_role is not None:
            self._values["service_role"] = service_role
        if steps_file is not None:
            self._values["steps_file"] = steps_file
        if tags is not None:
            self._values["tags"] = tags
        if task_desired_capacity is not None:
            self._values["task_desired_capacity"] = task_desired_capacity
        if task_ebs_block_device is not None:
            self._values["task_ebs_block_device"] = task_ebs_block_device
        if task_ebs_optimized is not None:
            self._values["task_ebs_optimized"] = task_ebs_optimized
        if task_instance_types is not None:
            self._values["task_instance_types"] = task_instance_types
        if task_lifecycle is not None:
            self._values["task_lifecycle"] = task_lifecycle
        if task_max_size is not None:
            self._values["task_max_size"] = task_max_size
        if task_min_size is not None:
            self._values["task_min_size"] = task_min_size
        if task_scaling_down_policy is not None:
            self._values["task_scaling_down_policy"] = task_scaling_down_policy
        if task_scaling_up_policy is not None:
            self._values["task_scaling_up_policy"] = task_scaling_up_policy
        if task_unit is not None:
            self._values["task_unit"] = task_unit
        if termination_policies is not None:
            self._values["termination_policies"] = termination_policies
        if termination_protected is not None:
            self._values["termination_protected"] = termination_protected
        if visible_to_all_users is not None:
            self._values["visible_to_all_users"] = visible_to_all_users

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#name MrscalerAws#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def strategy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#strategy MrscalerAws#strategy}.'''
        result = self._values.get("strategy")
        assert result is not None, "Required property 'strategy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_info(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#additional_info MrscalerAws#additional_info}.'''
        result = self._values.get("additional_info")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def additional_primary_security_groups(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#additional_primary_security_groups MrscalerAws#additional_primary_security_groups}.'''
        result = self._values.get("additional_primary_security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def additional_replica_security_groups(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#additional_replica_security_groups MrscalerAws#additional_replica_security_groups}.'''
        result = self._values.get("additional_replica_security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def applications(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsApplications]]]:
        '''applications block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#applications MrscalerAws#applications}
        '''
        result = self._values.get("applications")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsApplications]]], result)

    @builtins.property
    def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#availability_zones MrscalerAws#availability_zones}.'''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def bootstrap_actions_file(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsBootstrapActionsFile]]]:
        '''bootstrap_actions_file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#bootstrap_actions_file MrscalerAws#bootstrap_actions_file}
        '''
        result = self._values.get("bootstrap_actions_file")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsBootstrapActionsFile]]], result)

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#cluster_id MrscalerAws#cluster_id}.'''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def configurations_file(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsConfigurationsFile"]]]:
        '''configurations_file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#configurations_file MrscalerAws#configurations_file}
        '''
        result = self._values.get("configurations_file")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsConfigurationsFile"]]], result)

    @builtins.property
    def core_desired_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_desired_capacity MrscalerAws#core_desired_capacity}.'''
        result = self._values.get("core_desired_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def core_ebs_block_device(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsCoreEbsBlockDevice"]]]:
        '''core_ebs_block_device block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_ebs_block_device MrscalerAws#core_ebs_block_device}
        '''
        result = self._values.get("core_ebs_block_device")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsCoreEbsBlockDevice"]]], result)

    @builtins.property
    def core_ebs_optimized(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_ebs_optimized MrscalerAws#core_ebs_optimized}.'''
        result = self._values.get("core_ebs_optimized")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def core_instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_instance_types MrscalerAws#core_instance_types}.'''
        result = self._values.get("core_instance_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def core_lifecycle(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_lifecycle MrscalerAws#core_lifecycle}.'''
        result = self._values.get("core_lifecycle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def core_max_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_max_size MrscalerAws#core_max_size}.'''
        result = self._values.get("core_max_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def core_min_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_min_size MrscalerAws#core_min_size}.'''
        result = self._values.get("core_min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def core_scaling_down_policy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsCoreScalingDownPolicy"]]]:
        '''core_scaling_down_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_scaling_down_policy MrscalerAws#core_scaling_down_policy}
        '''
        result = self._values.get("core_scaling_down_policy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsCoreScalingDownPolicy"]]], result)

    @builtins.property
    def core_scaling_up_policy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsCoreScalingUpPolicy"]]]:
        '''core_scaling_up_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_scaling_up_policy MrscalerAws#core_scaling_up_policy}
        '''
        result = self._values.get("core_scaling_up_policy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsCoreScalingUpPolicy"]]], result)

    @builtins.property
    def core_unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#core_unit MrscalerAws#core_unit}.'''
        result = self._values.get("core_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_ami_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#custom_ami_id MrscalerAws#custom_ami_id}.'''
        result = self._values.get("custom_ami_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#description MrscalerAws#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_root_volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#ebs_root_volume_size MrscalerAws#ebs_root_volume_size}.'''
        result = self._values.get("ebs_root_volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ec2_key_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#ec2_key_name MrscalerAws#ec2_key_name}.'''
        result = self._values.get("ec2_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expose_cluster_id(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#expose_cluster_id MrscalerAws#expose_cluster_id}.'''
        result = self._values.get("expose_cluster_id")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#id MrscalerAws#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_weights(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsInstanceWeights"]]]:
        '''instance_weights block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#instance_weights MrscalerAws#instance_weights}
        '''
        result = self._values.get("instance_weights")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsInstanceWeights"]]], result)

    @builtins.property
    def job_flow_role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#job_flow_role MrscalerAws#job_flow_role}.'''
        result = self._values.get("job_flow_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keep_job_flow_alive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#keep_job_flow_alive MrscalerAws#keep_job_flow_alive}.'''
        result = self._values.get("keep_job_flow_alive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def log_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#log_uri MrscalerAws#log_uri}.'''
        result = self._values.get("log_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_primary_security_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#managed_primary_security_group MrscalerAws#managed_primary_security_group}.'''
        result = self._values.get("managed_primary_security_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_replica_security_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#managed_replica_security_group MrscalerAws#managed_replica_security_group}.'''
        result = self._values.get("managed_replica_security_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_ebs_block_device(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsMasterEbsBlockDevice"]]]:
        '''master_ebs_block_device block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#master_ebs_block_device MrscalerAws#master_ebs_block_device}
        '''
        result = self._values.get("master_ebs_block_device")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsMasterEbsBlockDevice"]]], result)

    @builtins.property
    def master_ebs_optimized(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#master_ebs_optimized MrscalerAws#master_ebs_optimized}.'''
        result = self._values.get("master_ebs_optimized")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def master_instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#master_instance_types MrscalerAws#master_instance_types}.'''
        result = self._values.get("master_instance_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def master_lifecycle(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#master_lifecycle MrscalerAws#master_lifecycle}.'''
        result = self._values.get("master_lifecycle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_target(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#master_target MrscalerAws#master_target}.'''
        result = self._values.get("master_target")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def provisioning_timeout(self) -> typing.Optional["MrscalerAwsProvisioningTimeout"]:
        '''provisioning_timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#provisioning_timeout MrscalerAws#provisioning_timeout}
        '''
        result = self._values.get("provisioning_timeout")
        return typing.cast(typing.Optional["MrscalerAwsProvisioningTimeout"], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#region MrscalerAws#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def release_label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#release_label MrscalerAws#release_label}.'''
        result = self._values.get("release_label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repo_upgrade_on_boot(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#repo_upgrade_on_boot MrscalerAws#repo_upgrade_on_boot}.'''
        result = self._values.get("repo_upgrade_on_boot")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retries(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#retries MrscalerAws#retries}.'''
        result = self._values.get("retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scheduled_task(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsScheduledTask"]]]:
        '''scheduled_task block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#scheduled_task MrscalerAws#scheduled_task}
        '''
        result = self._values.get("scheduled_task")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsScheduledTask"]]], result)

    @builtins.property
    def security_config(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#security_config MrscalerAws#security_config}.'''
        result = self._values.get("security_config")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_access_security_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#service_access_security_group MrscalerAws#service_access_security_group}.'''
        result = self._values.get("service_access_security_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#service_role MrscalerAws#service_role}.'''
        result = self._values.get("service_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def steps_file(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsStepsFile"]]]:
        '''steps_file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#steps_file MrscalerAws#steps_file}
        '''
        result = self._values.get("steps_file")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsStepsFile"]]], result)

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTags"]]]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#tags MrscalerAws#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTags"]]], result)

    @builtins.property
    def task_desired_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_desired_capacity MrscalerAws#task_desired_capacity}.'''
        result = self._values.get("task_desired_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def task_ebs_block_device(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTaskEbsBlockDevice"]]]:
        '''task_ebs_block_device block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_ebs_block_device MrscalerAws#task_ebs_block_device}
        '''
        result = self._values.get("task_ebs_block_device")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTaskEbsBlockDevice"]]], result)

    @builtins.property
    def task_ebs_optimized(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_ebs_optimized MrscalerAws#task_ebs_optimized}.'''
        result = self._values.get("task_ebs_optimized")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def task_instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_instance_types MrscalerAws#task_instance_types}.'''
        result = self._values.get("task_instance_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def task_lifecycle(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_lifecycle MrscalerAws#task_lifecycle}.'''
        result = self._values.get("task_lifecycle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def task_max_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_max_size MrscalerAws#task_max_size}.'''
        result = self._values.get("task_max_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def task_min_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_min_size MrscalerAws#task_min_size}.'''
        result = self._values.get("task_min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def task_scaling_down_policy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTaskScalingDownPolicy"]]]:
        '''task_scaling_down_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_scaling_down_policy MrscalerAws#task_scaling_down_policy}
        '''
        result = self._values.get("task_scaling_down_policy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTaskScalingDownPolicy"]]], result)

    @builtins.property
    def task_scaling_up_policy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTaskScalingUpPolicy"]]]:
        '''task_scaling_up_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_scaling_up_policy MrscalerAws#task_scaling_up_policy}
        '''
        result = self._values.get("task_scaling_up_policy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTaskScalingUpPolicy"]]], result)

    @builtins.property
    def task_unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_unit MrscalerAws#task_unit}.'''
        result = self._values.get("task_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def termination_policies(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTerminationPolicies"]]]:
        '''termination_policies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#termination_policies MrscalerAws#termination_policies}
        '''
        result = self._values.get("termination_policies")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTerminationPolicies"]]], result)

    @builtins.property
    def termination_protected(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#termination_protected MrscalerAws#termination_protected}.'''
        result = self._values.get("termination_protected")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def visible_to_all_users(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#visible_to_all_users MrscalerAws#visible_to_all_users}.'''
        result = self._values.get("visible_to_all_users")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MrscalerAwsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsConfigurationsFile",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "key": "key"},
)
class MrscalerAwsConfigurationsFile:
    def __init__(self, *, bucket: builtins.str, key: builtins.str) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#bucket MrscalerAws#bucket}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#key MrscalerAws#key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsConfigurationsFile.__init__)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "key": key,
        }

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#bucket MrscalerAws#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#key MrscalerAws#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MrscalerAwsConfigurationsFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MrscalerAwsConfigurationsFileList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsConfigurationsFileList",
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
            type_hints = typing.get_type_hints(MrscalerAwsConfigurationsFileList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MrscalerAwsConfigurationsFileOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsConfigurationsFileList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MrscalerAwsConfigurationsFileOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsConfigurationsFileList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsConfigurationsFileList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsConfigurationsFileList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsConfigurationsFile]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsConfigurationsFile]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsConfigurationsFile]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsConfigurationsFileList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MrscalerAwsConfigurationsFileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsConfigurationsFileOutputReference",
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
            type_hints = typing.get_type_hints(MrscalerAwsConfigurationsFileOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsConfigurationsFileOutputReference, "bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsConfigurationsFileOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MrscalerAwsConfigurationsFile, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MrscalerAwsConfigurationsFile, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MrscalerAwsConfigurationsFile, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsConfigurationsFileOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsCoreEbsBlockDevice",
    jsii_struct_bases=[],
    name_mapping={
        "size_in_gb": "sizeInGb",
        "volume_type": "volumeType",
        "iops": "iops",
        "volumes_per_instance": "volumesPerInstance",
    },
)
class MrscalerAwsCoreEbsBlockDevice:
    def __init__(
        self,
        *,
        size_in_gb: jsii.Number,
        volume_type: builtins.str,
        iops: typing.Optional[jsii.Number] = None,
        volumes_per_instance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param size_in_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#size_in_gb MrscalerAws#size_in_gb}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#volume_type MrscalerAws#volume_type}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#iops MrscalerAws#iops}.
        :param volumes_per_instance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#volumes_per_instance MrscalerAws#volumes_per_instance}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsCoreEbsBlockDevice.__init__)
            check_type(argname="argument size_in_gb", value=size_in_gb, expected_type=type_hints["size_in_gb"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument volumes_per_instance", value=volumes_per_instance, expected_type=type_hints["volumes_per_instance"])
        self._values: typing.Dict[str, typing.Any] = {
            "size_in_gb": size_in_gb,
            "volume_type": volume_type,
        }
        if iops is not None:
            self._values["iops"] = iops
        if volumes_per_instance is not None:
            self._values["volumes_per_instance"] = volumes_per_instance

    @builtins.property
    def size_in_gb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#size_in_gb MrscalerAws#size_in_gb}.'''
        result = self._values.get("size_in_gb")
        assert result is not None, "Required property 'size_in_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def volume_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#volume_type MrscalerAws#volume_type}.'''
        result = self._values.get("volume_type")
        assert result is not None, "Required property 'volume_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#iops MrscalerAws#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volumes_per_instance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#volumes_per_instance MrscalerAws#volumes_per_instance}.'''
        result = self._values.get("volumes_per_instance")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MrscalerAwsCoreEbsBlockDevice(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MrscalerAwsCoreEbsBlockDeviceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsCoreEbsBlockDeviceList",
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
            type_hints = typing.get_type_hints(MrscalerAwsCoreEbsBlockDeviceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MrscalerAwsCoreEbsBlockDeviceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsCoreEbsBlockDeviceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MrscalerAwsCoreEbsBlockDeviceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreEbsBlockDeviceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreEbsBlockDeviceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreEbsBlockDeviceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsCoreEbsBlockDevice]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsCoreEbsBlockDevice]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsCoreEbsBlockDevice]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreEbsBlockDeviceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MrscalerAwsCoreEbsBlockDeviceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsCoreEbsBlockDeviceOutputReference",
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
            type_hints = typing.get_type_hints(MrscalerAwsCoreEbsBlockDeviceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetVolumesPerInstance")
    def reset_volumes_per_instance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumesPerInstance", []))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInGbInput")
    def size_in_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInGbInput"))

    @builtins.property
    @jsii.member(jsii_name="volumesPerInstanceInput")
    def volumes_per_instance_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumesPerInstanceInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeTypeInput")
    def volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreEbsBlockDeviceOutputReference, "iops").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="sizeInGb")
    def size_in_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeInGb"))

    @size_in_gb.setter
    def size_in_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreEbsBlockDeviceOutputReference, "size_in_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeInGb", value)

    @builtins.property
    @jsii.member(jsii_name="volumesPerInstance")
    def volumes_per_instance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumesPerInstance"))

    @volumes_per_instance.setter
    def volumes_per_instance(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreEbsBlockDeviceOutputReference, "volumes_per_instance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumesPerInstance", value)

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreEbsBlockDeviceOutputReference, "volume_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MrscalerAwsCoreEbsBlockDevice, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MrscalerAwsCoreEbsBlockDevice, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MrscalerAwsCoreEbsBlockDevice, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreEbsBlockDeviceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsCoreScalingDownPolicy",
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
        "maximum": "maximum",
        "max_target_capacity": "maxTargetCapacity",
        "minimum": "minimum",
        "min_target_capacity": "minTargetCapacity",
        "operator": "operator",
        "period": "period",
        "statistic": "statistic",
        "target": "target",
    },
)
class MrscalerAwsCoreScalingDownPolicy:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        policy_name: builtins.str,
        threshold: jsii.Number,
        unit: builtins.str,
        action_type: typing.Optional[builtins.str] = None,
        adjustment: typing.Optional[builtins.str] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        maximum: typing.Optional[builtins.str] = None,
        max_target_capacity: typing.Optional[builtins.str] = None,
        minimum: typing.Optional[builtins.str] = None,
        min_target_capacity: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        period: typing.Optional[jsii.Number] = None,
        statistic: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#metric_name MrscalerAws#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#namespace MrscalerAws#namespace}.
        :param policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#policy_name MrscalerAws#policy_name}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#threshold MrscalerAws#threshold}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#unit MrscalerAws#unit}.
        :param action_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#action_type MrscalerAws#action_type}.
        :param adjustment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#adjustment MrscalerAws#adjustment}.
        :param cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#cooldown MrscalerAws#cooldown}.
        :param dimensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#dimensions MrscalerAws#dimensions}.
        :param evaluation_periods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#evaluation_periods MrscalerAws#evaluation_periods}.
        :param maximum: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#maximum MrscalerAws#maximum}.
        :param max_target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#max_target_capacity MrscalerAws#max_target_capacity}.
        :param minimum: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#minimum MrscalerAws#minimum}.
        :param min_target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#min_target_capacity MrscalerAws#min_target_capacity}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#operator MrscalerAws#operator}.
        :param period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#period MrscalerAws#period}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#statistic MrscalerAws#statistic}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#target MrscalerAws#target}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsCoreScalingDownPolicy.__init__)
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
            check_type(argname="argument maximum", value=maximum, expected_type=type_hints["maximum"])
            check_type(argname="argument max_target_capacity", value=max_target_capacity, expected_type=type_hints["max_target_capacity"])
            check_type(argname="argument minimum", value=minimum, expected_type=type_hints["minimum"])
            check_type(argname="argument min_target_capacity", value=min_target_capacity, expected_type=type_hints["min_target_capacity"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
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
        if maximum is not None:
            self._values["maximum"] = maximum
        if max_target_capacity is not None:
            self._values["max_target_capacity"] = max_target_capacity
        if minimum is not None:
            self._values["minimum"] = minimum
        if min_target_capacity is not None:
            self._values["min_target_capacity"] = min_target_capacity
        if operator is not None:
            self._values["operator"] = operator
        if period is not None:
            self._values["period"] = period
        if statistic is not None:
            self._values["statistic"] = statistic
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#metric_name MrscalerAws#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#namespace MrscalerAws#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#policy_name MrscalerAws#policy_name}.'''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#threshold MrscalerAws#threshold}.'''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#unit MrscalerAws#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#action_type MrscalerAws#action_type}.'''
        result = self._values.get("action_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def adjustment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#adjustment MrscalerAws#adjustment}.'''
        result = self._values.get("adjustment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#cooldown MrscalerAws#cooldown}.'''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimensions(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#dimensions MrscalerAws#dimensions}.'''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#evaluation_periods MrscalerAws#evaluation_periods}.'''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#maximum MrscalerAws#maximum}.'''
        result = self._values.get("maximum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_target_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#max_target_capacity MrscalerAws#max_target_capacity}.'''
        result = self._values.get("max_target_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#minimum MrscalerAws#minimum}.'''
        result = self._values.get("minimum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_target_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#min_target_capacity MrscalerAws#min_target_capacity}.'''
        result = self._values.get("min_target_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#operator MrscalerAws#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#period MrscalerAws#period}.'''
        result = self._values.get("period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#statistic MrscalerAws#statistic}.'''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#target MrscalerAws#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MrscalerAwsCoreScalingDownPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MrscalerAwsCoreScalingDownPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsCoreScalingDownPolicyList",
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
            type_hints = typing.get_type_hints(MrscalerAwsCoreScalingDownPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MrscalerAwsCoreScalingDownPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsCoreScalingDownPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MrscalerAwsCoreScalingDownPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsCoreScalingDownPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsCoreScalingDownPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsCoreScalingDownPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MrscalerAwsCoreScalingDownPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsCoreScalingDownPolicyOutputReference",
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
            type_hints = typing.get_type_hints(MrscalerAwsCoreScalingDownPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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

    @jsii.member(jsii_name="resetMaximum")
    def reset_maximum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximum", []))

    @jsii.member(jsii_name="resetMaxTargetCapacity")
    def reset_max_target_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTargetCapacity", []))

    @jsii.member(jsii_name="resetMinimum")
    def reset_minimum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimum", []))

    @jsii.member(jsii_name="resetMinTargetCapacity")
    def reset_min_target_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinTargetCapacity", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @jsii.member(jsii_name="resetStatistic")
    def reset_statistic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatistic", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="actionTypeInput")
    def action_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="adjustmentInput")
    def adjustment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adjustmentInput"))

    @builtins.property
    @jsii.member(jsii_name="cooldownInput")
    def cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionsInput")
    def dimensions_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dimensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriodsInput")
    def evaluation_periods_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "evaluationPeriodsInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumInput")
    def maximum_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maximumInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTargetCapacityInput")
    def max_target_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxTargetCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumInput")
    def minimum_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumInput"))

    @builtins.property
    @jsii.member(jsii_name="minTargetCapacityInput")
    def min_target_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minTargetCapacityInput"))

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
    @jsii.member(jsii_name="statisticInput")
    def statistic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statisticInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "action_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionType", value)

    @builtins.property
    @jsii.member(jsii_name="adjustment")
    def adjustment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adjustment"))

    @adjustment.setter
    def adjustment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "adjustment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adjustment", value)

    @builtins.property
    @jsii.member(jsii_name="cooldown")
    def cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cooldown"))

    @cooldown.setter
    def cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "cooldown").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cooldown", value)

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "dimensions"))

    @dimensions.setter
    def dimensions(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "dimensions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dimensions", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriods")
    def evaluation_periods(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "evaluationPeriods"))

    @evaluation_periods.setter
    def evaluation_periods(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "evaluation_periods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationPeriods", value)

    @builtins.property
    @jsii.member(jsii_name="maximum")
    def maximum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maximum"))

    @maximum.setter
    def maximum(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "maximum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximum", value)

    @builtins.property
    @jsii.member(jsii_name="maxTargetCapacity")
    def max_target_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxTargetCapacity"))

    @max_target_capacity.setter
    def max_target_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "max_target_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTargetCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "metric_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="minimum")
    def minimum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimum"))

    @minimum.setter
    def minimum(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "minimum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimum", value)

    @builtins.property
    @jsii.member(jsii_name="minTargetCapacity")
    def min_target_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minTargetCapacity"))

    @min_target_capacity.setter
    def min_target_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "min_target_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minTargetCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "period"))

    @period.setter
    def period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "statistic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statistic", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MrscalerAwsCoreScalingDownPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MrscalerAwsCoreScalingDownPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MrscalerAwsCoreScalingDownPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingDownPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsCoreScalingUpPolicy",
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
        "maximum": "maximum",
        "max_target_capacity": "maxTargetCapacity",
        "minimum": "minimum",
        "min_target_capacity": "minTargetCapacity",
        "operator": "operator",
        "period": "period",
        "statistic": "statistic",
        "target": "target",
    },
)
class MrscalerAwsCoreScalingUpPolicy:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        policy_name: builtins.str,
        threshold: jsii.Number,
        unit: builtins.str,
        action_type: typing.Optional[builtins.str] = None,
        adjustment: typing.Optional[builtins.str] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        maximum: typing.Optional[builtins.str] = None,
        max_target_capacity: typing.Optional[builtins.str] = None,
        minimum: typing.Optional[builtins.str] = None,
        min_target_capacity: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        period: typing.Optional[jsii.Number] = None,
        statistic: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#metric_name MrscalerAws#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#namespace MrscalerAws#namespace}.
        :param policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#policy_name MrscalerAws#policy_name}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#threshold MrscalerAws#threshold}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#unit MrscalerAws#unit}.
        :param action_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#action_type MrscalerAws#action_type}.
        :param adjustment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#adjustment MrscalerAws#adjustment}.
        :param cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#cooldown MrscalerAws#cooldown}.
        :param dimensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#dimensions MrscalerAws#dimensions}.
        :param evaluation_periods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#evaluation_periods MrscalerAws#evaluation_periods}.
        :param maximum: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#maximum MrscalerAws#maximum}.
        :param max_target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#max_target_capacity MrscalerAws#max_target_capacity}.
        :param minimum: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#minimum MrscalerAws#minimum}.
        :param min_target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#min_target_capacity MrscalerAws#min_target_capacity}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#operator MrscalerAws#operator}.
        :param period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#period MrscalerAws#period}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#statistic MrscalerAws#statistic}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#target MrscalerAws#target}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsCoreScalingUpPolicy.__init__)
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
            check_type(argname="argument maximum", value=maximum, expected_type=type_hints["maximum"])
            check_type(argname="argument max_target_capacity", value=max_target_capacity, expected_type=type_hints["max_target_capacity"])
            check_type(argname="argument minimum", value=minimum, expected_type=type_hints["minimum"])
            check_type(argname="argument min_target_capacity", value=min_target_capacity, expected_type=type_hints["min_target_capacity"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
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
        if maximum is not None:
            self._values["maximum"] = maximum
        if max_target_capacity is not None:
            self._values["max_target_capacity"] = max_target_capacity
        if minimum is not None:
            self._values["minimum"] = minimum
        if min_target_capacity is not None:
            self._values["min_target_capacity"] = min_target_capacity
        if operator is not None:
            self._values["operator"] = operator
        if period is not None:
            self._values["period"] = period
        if statistic is not None:
            self._values["statistic"] = statistic
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#metric_name MrscalerAws#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#namespace MrscalerAws#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#policy_name MrscalerAws#policy_name}.'''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#threshold MrscalerAws#threshold}.'''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#unit MrscalerAws#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#action_type MrscalerAws#action_type}.'''
        result = self._values.get("action_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def adjustment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#adjustment MrscalerAws#adjustment}.'''
        result = self._values.get("adjustment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#cooldown MrscalerAws#cooldown}.'''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimensions(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#dimensions MrscalerAws#dimensions}.'''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#evaluation_periods MrscalerAws#evaluation_periods}.'''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#maximum MrscalerAws#maximum}.'''
        result = self._values.get("maximum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_target_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#max_target_capacity MrscalerAws#max_target_capacity}.'''
        result = self._values.get("max_target_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#minimum MrscalerAws#minimum}.'''
        result = self._values.get("minimum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_target_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#min_target_capacity MrscalerAws#min_target_capacity}.'''
        result = self._values.get("min_target_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#operator MrscalerAws#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#period MrscalerAws#period}.'''
        result = self._values.get("period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#statistic MrscalerAws#statistic}.'''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#target MrscalerAws#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MrscalerAwsCoreScalingUpPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MrscalerAwsCoreScalingUpPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsCoreScalingUpPolicyList",
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
            type_hints = typing.get_type_hints(MrscalerAwsCoreScalingUpPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MrscalerAwsCoreScalingUpPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsCoreScalingUpPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MrscalerAwsCoreScalingUpPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsCoreScalingUpPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsCoreScalingUpPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsCoreScalingUpPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MrscalerAwsCoreScalingUpPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsCoreScalingUpPolicyOutputReference",
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
            type_hints = typing.get_type_hints(MrscalerAwsCoreScalingUpPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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

    @jsii.member(jsii_name="resetMaximum")
    def reset_maximum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximum", []))

    @jsii.member(jsii_name="resetMaxTargetCapacity")
    def reset_max_target_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTargetCapacity", []))

    @jsii.member(jsii_name="resetMinimum")
    def reset_minimum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimum", []))

    @jsii.member(jsii_name="resetMinTargetCapacity")
    def reset_min_target_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinTargetCapacity", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @jsii.member(jsii_name="resetStatistic")
    def reset_statistic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatistic", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="actionTypeInput")
    def action_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="adjustmentInput")
    def adjustment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adjustmentInput"))

    @builtins.property
    @jsii.member(jsii_name="cooldownInput")
    def cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionsInput")
    def dimensions_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dimensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriodsInput")
    def evaluation_periods_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "evaluationPeriodsInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumInput")
    def maximum_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maximumInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTargetCapacityInput")
    def max_target_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxTargetCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumInput")
    def minimum_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumInput"))

    @builtins.property
    @jsii.member(jsii_name="minTargetCapacityInput")
    def min_target_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minTargetCapacityInput"))

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
    @jsii.member(jsii_name="statisticInput")
    def statistic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statisticInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "action_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionType", value)

    @builtins.property
    @jsii.member(jsii_name="adjustment")
    def adjustment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adjustment"))

    @adjustment.setter
    def adjustment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "adjustment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adjustment", value)

    @builtins.property
    @jsii.member(jsii_name="cooldown")
    def cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cooldown"))

    @cooldown.setter
    def cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "cooldown").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cooldown", value)

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "dimensions"))

    @dimensions.setter
    def dimensions(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "dimensions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dimensions", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriods")
    def evaluation_periods(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "evaluationPeriods"))

    @evaluation_periods.setter
    def evaluation_periods(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "evaluation_periods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationPeriods", value)

    @builtins.property
    @jsii.member(jsii_name="maximum")
    def maximum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maximum"))

    @maximum.setter
    def maximum(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "maximum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximum", value)

    @builtins.property
    @jsii.member(jsii_name="maxTargetCapacity")
    def max_target_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxTargetCapacity"))

    @max_target_capacity.setter
    def max_target_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "max_target_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTargetCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "metric_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="minimum")
    def minimum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimum"))

    @minimum.setter
    def minimum(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "minimum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimum", value)

    @builtins.property
    @jsii.member(jsii_name="minTargetCapacity")
    def min_target_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minTargetCapacity"))

    @min_target_capacity.setter
    def min_target_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "min_target_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minTargetCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "period"))

    @period.setter
    def period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "statistic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statistic", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MrscalerAwsCoreScalingUpPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MrscalerAwsCoreScalingUpPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MrscalerAwsCoreScalingUpPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsCoreScalingUpPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsInstanceWeights",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "weighted_capacity": "weightedCapacity",
    },
)
class MrscalerAwsInstanceWeights:
    def __init__(
        self,
        *,
        instance_type: builtins.str,
        weighted_capacity: jsii.Number,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#instance_type MrscalerAws#instance_type}.
        :param weighted_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#weighted_capacity MrscalerAws#weighted_capacity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsInstanceWeights.__init__)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument weighted_capacity", value=weighted_capacity, expected_type=type_hints["weighted_capacity"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_type": instance_type,
            "weighted_capacity": weighted_capacity,
        }

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#instance_type MrscalerAws#instance_type}.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def weighted_capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#weighted_capacity MrscalerAws#weighted_capacity}.'''
        result = self._values.get("weighted_capacity")
        assert result is not None, "Required property 'weighted_capacity' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MrscalerAwsInstanceWeights(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MrscalerAwsInstanceWeightsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsInstanceWeightsList",
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
            type_hints = typing.get_type_hints(MrscalerAwsInstanceWeightsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MrscalerAwsInstanceWeightsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsInstanceWeightsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MrscalerAwsInstanceWeightsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsInstanceWeightsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsInstanceWeightsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsInstanceWeightsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsInstanceWeights]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsInstanceWeights]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsInstanceWeights]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsInstanceWeightsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MrscalerAwsInstanceWeightsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsInstanceWeightsOutputReference",
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
            type_hints = typing.get_type_hints(MrscalerAwsInstanceWeightsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="weightedCapacityInput")
    def weighted_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightedCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsInstanceWeightsOutputReference, "instance_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="weightedCapacity")
    def weighted_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weightedCapacity"))

    @weighted_capacity.setter
    def weighted_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsInstanceWeightsOutputReference, "weighted_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weightedCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MrscalerAwsInstanceWeights, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MrscalerAwsInstanceWeights, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MrscalerAwsInstanceWeights, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsInstanceWeightsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsMasterEbsBlockDevice",
    jsii_struct_bases=[],
    name_mapping={
        "size_in_gb": "sizeInGb",
        "volume_type": "volumeType",
        "iops": "iops",
        "volumes_per_instance": "volumesPerInstance",
    },
)
class MrscalerAwsMasterEbsBlockDevice:
    def __init__(
        self,
        *,
        size_in_gb: jsii.Number,
        volume_type: builtins.str,
        iops: typing.Optional[jsii.Number] = None,
        volumes_per_instance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param size_in_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#size_in_gb MrscalerAws#size_in_gb}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#volume_type MrscalerAws#volume_type}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#iops MrscalerAws#iops}.
        :param volumes_per_instance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#volumes_per_instance MrscalerAws#volumes_per_instance}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsMasterEbsBlockDevice.__init__)
            check_type(argname="argument size_in_gb", value=size_in_gb, expected_type=type_hints["size_in_gb"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument volumes_per_instance", value=volumes_per_instance, expected_type=type_hints["volumes_per_instance"])
        self._values: typing.Dict[str, typing.Any] = {
            "size_in_gb": size_in_gb,
            "volume_type": volume_type,
        }
        if iops is not None:
            self._values["iops"] = iops
        if volumes_per_instance is not None:
            self._values["volumes_per_instance"] = volumes_per_instance

    @builtins.property
    def size_in_gb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#size_in_gb MrscalerAws#size_in_gb}.'''
        result = self._values.get("size_in_gb")
        assert result is not None, "Required property 'size_in_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def volume_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#volume_type MrscalerAws#volume_type}.'''
        result = self._values.get("volume_type")
        assert result is not None, "Required property 'volume_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#iops MrscalerAws#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volumes_per_instance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#volumes_per_instance MrscalerAws#volumes_per_instance}.'''
        result = self._values.get("volumes_per_instance")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MrscalerAwsMasterEbsBlockDevice(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MrscalerAwsMasterEbsBlockDeviceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsMasterEbsBlockDeviceList",
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
            type_hints = typing.get_type_hints(MrscalerAwsMasterEbsBlockDeviceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MrscalerAwsMasterEbsBlockDeviceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsMasterEbsBlockDeviceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MrscalerAwsMasterEbsBlockDeviceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsMasterEbsBlockDeviceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsMasterEbsBlockDeviceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsMasterEbsBlockDeviceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsMasterEbsBlockDevice]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsMasterEbsBlockDevice]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsMasterEbsBlockDevice]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsMasterEbsBlockDeviceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MrscalerAwsMasterEbsBlockDeviceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsMasterEbsBlockDeviceOutputReference",
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
            type_hints = typing.get_type_hints(MrscalerAwsMasterEbsBlockDeviceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetVolumesPerInstance")
    def reset_volumes_per_instance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumesPerInstance", []))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInGbInput")
    def size_in_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInGbInput"))

    @builtins.property
    @jsii.member(jsii_name="volumesPerInstanceInput")
    def volumes_per_instance_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumesPerInstanceInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeTypeInput")
    def volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsMasterEbsBlockDeviceOutputReference, "iops").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="sizeInGb")
    def size_in_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeInGb"))

    @size_in_gb.setter
    def size_in_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsMasterEbsBlockDeviceOutputReference, "size_in_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeInGb", value)

    @builtins.property
    @jsii.member(jsii_name="volumesPerInstance")
    def volumes_per_instance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumesPerInstance"))

    @volumes_per_instance.setter
    def volumes_per_instance(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsMasterEbsBlockDeviceOutputReference, "volumes_per_instance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumesPerInstance", value)

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsMasterEbsBlockDeviceOutputReference, "volume_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MrscalerAwsMasterEbsBlockDevice, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MrscalerAwsMasterEbsBlockDevice, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MrscalerAwsMasterEbsBlockDevice, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsMasterEbsBlockDeviceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsProvisioningTimeout",
    jsii_struct_bases=[],
    name_mapping={"timeout": "timeout", "timeout_action": "timeoutAction"},
)
class MrscalerAwsProvisioningTimeout:
    def __init__(self, *, timeout: jsii.Number, timeout_action: builtins.str) -> None:
        '''
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#timeout MrscalerAws#timeout}.
        :param timeout_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#timeout_action MrscalerAws#timeout_action}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsProvisioningTimeout.__init__)
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument timeout_action", value=timeout_action, expected_type=type_hints["timeout_action"])
        self._values: typing.Dict[str, typing.Any] = {
            "timeout": timeout,
            "timeout_action": timeout_action,
        }

    @builtins.property
    def timeout(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#timeout MrscalerAws#timeout}.'''
        result = self._values.get("timeout")
        assert result is not None, "Required property 'timeout' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def timeout_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#timeout_action MrscalerAws#timeout_action}.'''
        result = self._values.get("timeout_action")
        assert result is not None, "Required property 'timeout_action' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MrscalerAwsProvisioningTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MrscalerAwsProvisioningTimeoutOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsProvisioningTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(MrscalerAwsProvisioningTimeoutOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="timeoutActionInput")
    def timeout_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeoutActionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsProvisioningTimeoutOutputReference, "timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutAction")
    def timeout_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeoutAction"))

    @timeout_action.setter
    def timeout_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsProvisioningTimeoutOutputReference, "timeout_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutAction", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MrscalerAwsProvisioningTimeout]:
        return typing.cast(typing.Optional[MrscalerAwsProvisioningTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MrscalerAwsProvisioningTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsProvisioningTimeoutOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsScheduledTask",
    jsii_struct_bases=[],
    name_mapping={
        "cron": "cron",
        "instance_group_type": "instanceGroupType",
        "task_type": "taskType",
        "desired_capacity": "desiredCapacity",
        "is_enabled": "isEnabled",
        "max_capacity": "maxCapacity",
        "min_capacity": "minCapacity",
    },
)
class MrscalerAwsScheduledTask:
    def __init__(
        self,
        *,
        cron: builtins.str,
        instance_group_type: builtins.str,
        task_type: builtins.str,
        desired_capacity: typing.Optional[builtins.str] = None,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_capacity: typing.Optional[builtins.str] = None,
        min_capacity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cron: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#cron MrscalerAws#cron}.
        :param instance_group_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#instance_group_type MrscalerAws#instance_group_type}.
        :param task_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_type MrscalerAws#task_type}.
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#desired_capacity MrscalerAws#desired_capacity}.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#is_enabled MrscalerAws#is_enabled}.
        :param max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#max_capacity MrscalerAws#max_capacity}.
        :param min_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#min_capacity MrscalerAws#min_capacity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsScheduledTask.__init__)
            check_type(argname="argument cron", value=cron, expected_type=type_hints["cron"])
            check_type(argname="argument instance_group_type", value=instance_group_type, expected_type=type_hints["instance_group_type"])
            check_type(argname="argument task_type", value=task_type, expected_type=type_hints["task_type"])
            check_type(argname="argument desired_capacity", value=desired_capacity, expected_type=type_hints["desired_capacity"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
        self._values: typing.Dict[str, typing.Any] = {
            "cron": cron,
            "instance_group_type": instance_group_type,
            "task_type": task_type,
        }
        if desired_capacity is not None:
            self._values["desired_capacity"] = desired_capacity
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if max_capacity is not None:
            self._values["max_capacity"] = max_capacity
        if min_capacity is not None:
            self._values["min_capacity"] = min_capacity

    @builtins.property
    def cron(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#cron MrscalerAws#cron}.'''
        result = self._values.get("cron")
        assert result is not None, "Required property 'cron' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_group_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#instance_group_type MrscalerAws#instance_group_type}.'''
        result = self._values.get("instance_group_type")
        assert result is not None, "Required property 'instance_group_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def task_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#task_type MrscalerAws#task_type}.'''
        result = self._values.get("task_type")
        assert result is not None, "Required property 'task_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def desired_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#desired_capacity MrscalerAws#desired_capacity}.'''
        result = self._values.get("desired_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#is_enabled MrscalerAws#is_enabled}.'''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#max_capacity MrscalerAws#max_capacity}.'''
        result = self._values.get("max_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#min_capacity MrscalerAws#min_capacity}.'''
        result = self._values.get("min_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MrscalerAwsScheduledTask(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MrscalerAwsScheduledTaskList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsScheduledTaskList",
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
            type_hints = typing.get_type_hints(MrscalerAwsScheduledTaskList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MrscalerAwsScheduledTaskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsScheduledTaskList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MrscalerAwsScheduledTaskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsScheduledTaskList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsScheduledTaskList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsScheduledTaskList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsScheduledTask]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsScheduledTask]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsScheduledTask]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsScheduledTaskList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MrscalerAwsScheduledTaskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsScheduledTaskOutputReference",
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
            type_hints = typing.get_type_hints(MrscalerAwsScheduledTaskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDesiredCapacity")
    def reset_desired_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredCapacity", []))

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetMaxCapacity")
    def reset_max_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxCapacity", []))

    @jsii.member(jsii_name="resetMinCapacity")
    def reset_min_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="cronInput")
    def cron_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cronInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredCapacityInput")
    def desired_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desiredCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceGroupTypeInput")
    def instance_group_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceGroupTypeInput"))

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
    @jsii.member(jsii_name="taskTypeInput")
    def task_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="cron")
    def cron(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cron"))

    @cron.setter
    def cron(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsScheduledTaskOutputReference, "cron").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cron", value)

    @builtins.property
    @jsii.member(jsii_name="desiredCapacity")
    def desired_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "desiredCapacity"))

    @desired_capacity.setter
    def desired_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsScheduledTaskOutputReference, "desired_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="instanceGroupType")
    def instance_group_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceGroupType"))

    @instance_group_type.setter
    def instance_group_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsScheduledTaskOutputReference, "instance_group_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceGroupType", value)

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsScheduledTaskOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxCapacity"))

    @max_capacity.setter
    def max_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsScheduledTaskOutputReference, "max_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="minCapacity")
    def min_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minCapacity"))

    @min_capacity.setter
    def min_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsScheduledTaskOutputReference, "min_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="taskType")
    def task_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskType"))

    @task_type.setter
    def task_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsScheduledTaskOutputReference, "task_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MrscalerAwsScheduledTask, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MrscalerAwsScheduledTask, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MrscalerAwsScheduledTask, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsScheduledTaskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsStepsFile",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "key": "key"},
)
class MrscalerAwsStepsFile:
    def __init__(self, *, bucket: builtins.str, key: builtins.str) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#bucket MrscalerAws#bucket}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#key MrscalerAws#key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsStepsFile.__init__)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "key": key,
        }

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#bucket MrscalerAws#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#key MrscalerAws#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MrscalerAwsStepsFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MrscalerAwsStepsFileList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsStepsFileList",
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
            type_hints = typing.get_type_hints(MrscalerAwsStepsFileList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MrscalerAwsStepsFileOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsStepsFileList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MrscalerAwsStepsFileOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsStepsFileList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsStepsFileList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsStepsFileList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsStepsFile]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsStepsFile]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsStepsFile]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsStepsFileList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MrscalerAwsStepsFileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsStepsFileOutputReference",
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
            type_hints = typing.get_type_hints(MrscalerAwsStepsFileOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsStepsFileOutputReference, "bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsStepsFileOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MrscalerAwsStepsFile, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MrscalerAwsStepsFile, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MrscalerAwsStepsFile, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsStepsFileOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class MrscalerAwsTags:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#key MrscalerAws#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#value MrscalerAws#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsTags.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#key MrscalerAws#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#value MrscalerAws#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MrscalerAwsTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MrscalerAwsTagsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsTagsList",
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
            type_hints = typing.get_type_hints(MrscalerAwsTagsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MrscalerAwsTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsTagsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MrscalerAwsTagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTagsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTagsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTagsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsTags]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsTags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTagsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MrscalerAwsTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsTagsOutputReference",
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
            type_hints = typing.get_type_hints(MrscalerAwsTagsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTagsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTagsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MrscalerAwsTags, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MrscalerAwsTags, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MrscalerAwsTags, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTagsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsTaskEbsBlockDevice",
    jsii_struct_bases=[],
    name_mapping={
        "size_in_gb": "sizeInGb",
        "volume_type": "volumeType",
        "iops": "iops",
        "volumes_per_instance": "volumesPerInstance",
    },
)
class MrscalerAwsTaskEbsBlockDevice:
    def __init__(
        self,
        *,
        size_in_gb: jsii.Number,
        volume_type: builtins.str,
        iops: typing.Optional[jsii.Number] = None,
        volumes_per_instance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param size_in_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#size_in_gb MrscalerAws#size_in_gb}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#volume_type MrscalerAws#volume_type}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#iops MrscalerAws#iops}.
        :param volumes_per_instance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#volumes_per_instance MrscalerAws#volumes_per_instance}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsTaskEbsBlockDevice.__init__)
            check_type(argname="argument size_in_gb", value=size_in_gb, expected_type=type_hints["size_in_gb"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument volumes_per_instance", value=volumes_per_instance, expected_type=type_hints["volumes_per_instance"])
        self._values: typing.Dict[str, typing.Any] = {
            "size_in_gb": size_in_gb,
            "volume_type": volume_type,
        }
        if iops is not None:
            self._values["iops"] = iops
        if volumes_per_instance is not None:
            self._values["volumes_per_instance"] = volumes_per_instance

    @builtins.property
    def size_in_gb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#size_in_gb MrscalerAws#size_in_gb}.'''
        result = self._values.get("size_in_gb")
        assert result is not None, "Required property 'size_in_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def volume_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#volume_type MrscalerAws#volume_type}.'''
        result = self._values.get("volume_type")
        assert result is not None, "Required property 'volume_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#iops MrscalerAws#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volumes_per_instance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#volumes_per_instance MrscalerAws#volumes_per_instance}.'''
        result = self._values.get("volumes_per_instance")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MrscalerAwsTaskEbsBlockDevice(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MrscalerAwsTaskEbsBlockDeviceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsTaskEbsBlockDeviceList",
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
            type_hints = typing.get_type_hints(MrscalerAwsTaskEbsBlockDeviceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MrscalerAwsTaskEbsBlockDeviceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsTaskEbsBlockDeviceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MrscalerAwsTaskEbsBlockDeviceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskEbsBlockDeviceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskEbsBlockDeviceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskEbsBlockDeviceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsTaskEbsBlockDevice]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsTaskEbsBlockDevice]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsTaskEbsBlockDevice]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskEbsBlockDeviceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MrscalerAwsTaskEbsBlockDeviceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsTaskEbsBlockDeviceOutputReference",
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
            type_hints = typing.get_type_hints(MrscalerAwsTaskEbsBlockDeviceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetVolumesPerInstance")
    def reset_volumes_per_instance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumesPerInstance", []))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInGbInput")
    def size_in_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInGbInput"))

    @builtins.property
    @jsii.member(jsii_name="volumesPerInstanceInput")
    def volumes_per_instance_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumesPerInstanceInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeTypeInput")
    def volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskEbsBlockDeviceOutputReference, "iops").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="sizeInGb")
    def size_in_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeInGb"))

    @size_in_gb.setter
    def size_in_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskEbsBlockDeviceOutputReference, "size_in_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeInGb", value)

    @builtins.property
    @jsii.member(jsii_name="volumesPerInstance")
    def volumes_per_instance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumesPerInstance"))

    @volumes_per_instance.setter
    def volumes_per_instance(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskEbsBlockDeviceOutputReference, "volumes_per_instance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumesPerInstance", value)

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskEbsBlockDeviceOutputReference, "volume_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MrscalerAwsTaskEbsBlockDevice, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MrscalerAwsTaskEbsBlockDevice, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MrscalerAwsTaskEbsBlockDevice, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskEbsBlockDeviceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsTaskScalingDownPolicy",
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
        "maximum": "maximum",
        "max_target_capacity": "maxTargetCapacity",
        "minimum": "minimum",
        "min_target_capacity": "minTargetCapacity",
        "operator": "operator",
        "period": "period",
        "statistic": "statistic",
        "target": "target",
    },
)
class MrscalerAwsTaskScalingDownPolicy:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        policy_name: builtins.str,
        threshold: jsii.Number,
        unit: builtins.str,
        action_type: typing.Optional[builtins.str] = None,
        adjustment: typing.Optional[builtins.str] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        maximum: typing.Optional[builtins.str] = None,
        max_target_capacity: typing.Optional[builtins.str] = None,
        minimum: typing.Optional[builtins.str] = None,
        min_target_capacity: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        period: typing.Optional[jsii.Number] = None,
        statistic: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#metric_name MrscalerAws#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#namespace MrscalerAws#namespace}.
        :param policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#policy_name MrscalerAws#policy_name}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#threshold MrscalerAws#threshold}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#unit MrscalerAws#unit}.
        :param action_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#action_type MrscalerAws#action_type}.
        :param adjustment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#adjustment MrscalerAws#adjustment}.
        :param cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#cooldown MrscalerAws#cooldown}.
        :param dimensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#dimensions MrscalerAws#dimensions}.
        :param evaluation_periods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#evaluation_periods MrscalerAws#evaluation_periods}.
        :param maximum: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#maximum MrscalerAws#maximum}.
        :param max_target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#max_target_capacity MrscalerAws#max_target_capacity}.
        :param minimum: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#minimum MrscalerAws#minimum}.
        :param min_target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#min_target_capacity MrscalerAws#min_target_capacity}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#operator MrscalerAws#operator}.
        :param period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#period MrscalerAws#period}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#statistic MrscalerAws#statistic}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#target MrscalerAws#target}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsTaskScalingDownPolicy.__init__)
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
            check_type(argname="argument maximum", value=maximum, expected_type=type_hints["maximum"])
            check_type(argname="argument max_target_capacity", value=max_target_capacity, expected_type=type_hints["max_target_capacity"])
            check_type(argname="argument minimum", value=minimum, expected_type=type_hints["minimum"])
            check_type(argname="argument min_target_capacity", value=min_target_capacity, expected_type=type_hints["min_target_capacity"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
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
        if maximum is not None:
            self._values["maximum"] = maximum
        if max_target_capacity is not None:
            self._values["max_target_capacity"] = max_target_capacity
        if minimum is not None:
            self._values["minimum"] = minimum
        if min_target_capacity is not None:
            self._values["min_target_capacity"] = min_target_capacity
        if operator is not None:
            self._values["operator"] = operator
        if period is not None:
            self._values["period"] = period
        if statistic is not None:
            self._values["statistic"] = statistic
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#metric_name MrscalerAws#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#namespace MrscalerAws#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#policy_name MrscalerAws#policy_name}.'''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#threshold MrscalerAws#threshold}.'''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#unit MrscalerAws#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#action_type MrscalerAws#action_type}.'''
        result = self._values.get("action_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def adjustment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#adjustment MrscalerAws#adjustment}.'''
        result = self._values.get("adjustment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#cooldown MrscalerAws#cooldown}.'''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimensions(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#dimensions MrscalerAws#dimensions}.'''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#evaluation_periods MrscalerAws#evaluation_periods}.'''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#maximum MrscalerAws#maximum}.'''
        result = self._values.get("maximum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_target_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#max_target_capacity MrscalerAws#max_target_capacity}.'''
        result = self._values.get("max_target_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#minimum MrscalerAws#minimum}.'''
        result = self._values.get("minimum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_target_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#min_target_capacity MrscalerAws#min_target_capacity}.'''
        result = self._values.get("min_target_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#operator MrscalerAws#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#period MrscalerAws#period}.'''
        result = self._values.get("period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#statistic MrscalerAws#statistic}.'''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#target MrscalerAws#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MrscalerAwsTaskScalingDownPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MrscalerAwsTaskScalingDownPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsTaskScalingDownPolicyList",
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
            type_hints = typing.get_type_hints(MrscalerAwsTaskScalingDownPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MrscalerAwsTaskScalingDownPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsTaskScalingDownPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MrscalerAwsTaskScalingDownPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsTaskScalingDownPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsTaskScalingDownPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsTaskScalingDownPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MrscalerAwsTaskScalingDownPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsTaskScalingDownPolicyOutputReference",
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
            type_hints = typing.get_type_hints(MrscalerAwsTaskScalingDownPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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

    @jsii.member(jsii_name="resetMaximum")
    def reset_maximum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximum", []))

    @jsii.member(jsii_name="resetMaxTargetCapacity")
    def reset_max_target_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTargetCapacity", []))

    @jsii.member(jsii_name="resetMinimum")
    def reset_minimum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimum", []))

    @jsii.member(jsii_name="resetMinTargetCapacity")
    def reset_min_target_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinTargetCapacity", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @jsii.member(jsii_name="resetStatistic")
    def reset_statistic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatistic", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="actionTypeInput")
    def action_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="adjustmentInput")
    def adjustment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adjustmentInput"))

    @builtins.property
    @jsii.member(jsii_name="cooldownInput")
    def cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionsInput")
    def dimensions_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dimensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriodsInput")
    def evaluation_periods_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "evaluationPeriodsInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumInput")
    def maximum_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maximumInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTargetCapacityInput")
    def max_target_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxTargetCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumInput")
    def minimum_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumInput"))

    @builtins.property
    @jsii.member(jsii_name="minTargetCapacityInput")
    def min_target_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minTargetCapacityInput"))

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
    @jsii.member(jsii_name="statisticInput")
    def statistic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statisticInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "action_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionType", value)

    @builtins.property
    @jsii.member(jsii_name="adjustment")
    def adjustment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adjustment"))

    @adjustment.setter
    def adjustment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "adjustment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adjustment", value)

    @builtins.property
    @jsii.member(jsii_name="cooldown")
    def cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cooldown"))

    @cooldown.setter
    def cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "cooldown").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cooldown", value)

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "dimensions"))

    @dimensions.setter
    def dimensions(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "dimensions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dimensions", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriods")
    def evaluation_periods(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "evaluationPeriods"))

    @evaluation_periods.setter
    def evaluation_periods(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "evaluation_periods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationPeriods", value)

    @builtins.property
    @jsii.member(jsii_name="maximum")
    def maximum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maximum"))

    @maximum.setter
    def maximum(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "maximum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximum", value)

    @builtins.property
    @jsii.member(jsii_name="maxTargetCapacity")
    def max_target_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxTargetCapacity"))

    @max_target_capacity.setter
    def max_target_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "max_target_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTargetCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "metric_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="minimum")
    def minimum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimum"))

    @minimum.setter
    def minimum(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "minimum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimum", value)

    @builtins.property
    @jsii.member(jsii_name="minTargetCapacity")
    def min_target_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minTargetCapacity"))

    @min_target_capacity.setter
    def min_target_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "min_target_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minTargetCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "period"))

    @period.setter
    def period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "statistic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statistic", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MrscalerAwsTaskScalingDownPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MrscalerAwsTaskScalingDownPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MrscalerAwsTaskScalingDownPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingDownPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsTaskScalingUpPolicy",
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
        "maximum": "maximum",
        "max_target_capacity": "maxTargetCapacity",
        "minimum": "minimum",
        "min_target_capacity": "minTargetCapacity",
        "operator": "operator",
        "period": "period",
        "statistic": "statistic",
        "target": "target",
    },
)
class MrscalerAwsTaskScalingUpPolicy:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        policy_name: builtins.str,
        threshold: jsii.Number,
        unit: builtins.str,
        action_type: typing.Optional[builtins.str] = None,
        adjustment: typing.Optional[builtins.str] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        maximum: typing.Optional[builtins.str] = None,
        max_target_capacity: typing.Optional[builtins.str] = None,
        minimum: typing.Optional[builtins.str] = None,
        min_target_capacity: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        period: typing.Optional[jsii.Number] = None,
        statistic: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#metric_name MrscalerAws#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#namespace MrscalerAws#namespace}.
        :param policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#policy_name MrscalerAws#policy_name}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#threshold MrscalerAws#threshold}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#unit MrscalerAws#unit}.
        :param action_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#action_type MrscalerAws#action_type}.
        :param adjustment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#adjustment MrscalerAws#adjustment}.
        :param cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#cooldown MrscalerAws#cooldown}.
        :param dimensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#dimensions MrscalerAws#dimensions}.
        :param evaluation_periods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#evaluation_periods MrscalerAws#evaluation_periods}.
        :param maximum: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#maximum MrscalerAws#maximum}.
        :param max_target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#max_target_capacity MrscalerAws#max_target_capacity}.
        :param minimum: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#minimum MrscalerAws#minimum}.
        :param min_target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#min_target_capacity MrscalerAws#min_target_capacity}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#operator MrscalerAws#operator}.
        :param period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#period MrscalerAws#period}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#statistic MrscalerAws#statistic}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#target MrscalerAws#target}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsTaskScalingUpPolicy.__init__)
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
            check_type(argname="argument maximum", value=maximum, expected_type=type_hints["maximum"])
            check_type(argname="argument max_target_capacity", value=max_target_capacity, expected_type=type_hints["max_target_capacity"])
            check_type(argname="argument minimum", value=minimum, expected_type=type_hints["minimum"])
            check_type(argname="argument min_target_capacity", value=min_target_capacity, expected_type=type_hints["min_target_capacity"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
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
        if maximum is not None:
            self._values["maximum"] = maximum
        if max_target_capacity is not None:
            self._values["max_target_capacity"] = max_target_capacity
        if minimum is not None:
            self._values["minimum"] = minimum
        if min_target_capacity is not None:
            self._values["min_target_capacity"] = min_target_capacity
        if operator is not None:
            self._values["operator"] = operator
        if period is not None:
            self._values["period"] = period
        if statistic is not None:
            self._values["statistic"] = statistic
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#metric_name MrscalerAws#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#namespace MrscalerAws#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#policy_name MrscalerAws#policy_name}.'''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#threshold MrscalerAws#threshold}.'''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#unit MrscalerAws#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#action_type MrscalerAws#action_type}.'''
        result = self._values.get("action_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def adjustment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#adjustment MrscalerAws#adjustment}.'''
        result = self._values.get("adjustment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#cooldown MrscalerAws#cooldown}.'''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimensions(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#dimensions MrscalerAws#dimensions}.'''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#evaluation_periods MrscalerAws#evaluation_periods}.'''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#maximum MrscalerAws#maximum}.'''
        result = self._values.get("maximum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_target_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#max_target_capacity MrscalerAws#max_target_capacity}.'''
        result = self._values.get("max_target_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#minimum MrscalerAws#minimum}.'''
        result = self._values.get("minimum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_target_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#min_target_capacity MrscalerAws#min_target_capacity}.'''
        result = self._values.get("min_target_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#operator MrscalerAws#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#period MrscalerAws#period}.'''
        result = self._values.get("period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#statistic MrscalerAws#statistic}.'''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#target MrscalerAws#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MrscalerAwsTaskScalingUpPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MrscalerAwsTaskScalingUpPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsTaskScalingUpPolicyList",
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
            type_hints = typing.get_type_hints(MrscalerAwsTaskScalingUpPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MrscalerAwsTaskScalingUpPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsTaskScalingUpPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MrscalerAwsTaskScalingUpPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsTaskScalingUpPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsTaskScalingUpPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsTaskScalingUpPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MrscalerAwsTaskScalingUpPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsTaskScalingUpPolicyOutputReference",
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
            type_hints = typing.get_type_hints(MrscalerAwsTaskScalingUpPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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

    @jsii.member(jsii_name="resetMaximum")
    def reset_maximum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximum", []))

    @jsii.member(jsii_name="resetMaxTargetCapacity")
    def reset_max_target_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTargetCapacity", []))

    @jsii.member(jsii_name="resetMinimum")
    def reset_minimum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimum", []))

    @jsii.member(jsii_name="resetMinTargetCapacity")
    def reset_min_target_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinTargetCapacity", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @jsii.member(jsii_name="resetStatistic")
    def reset_statistic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatistic", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="actionTypeInput")
    def action_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="adjustmentInput")
    def adjustment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adjustmentInput"))

    @builtins.property
    @jsii.member(jsii_name="cooldownInput")
    def cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionsInput")
    def dimensions_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dimensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriodsInput")
    def evaluation_periods_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "evaluationPeriodsInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumInput")
    def maximum_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maximumInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTargetCapacityInput")
    def max_target_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxTargetCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumInput")
    def minimum_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumInput"))

    @builtins.property
    @jsii.member(jsii_name="minTargetCapacityInput")
    def min_target_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minTargetCapacityInput"))

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
    @jsii.member(jsii_name="statisticInput")
    def statistic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statisticInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "action_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionType", value)

    @builtins.property
    @jsii.member(jsii_name="adjustment")
    def adjustment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adjustment"))

    @adjustment.setter
    def adjustment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "adjustment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adjustment", value)

    @builtins.property
    @jsii.member(jsii_name="cooldown")
    def cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cooldown"))

    @cooldown.setter
    def cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "cooldown").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cooldown", value)

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "dimensions"))

    @dimensions.setter
    def dimensions(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "dimensions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dimensions", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriods")
    def evaluation_periods(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "evaluationPeriods"))

    @evaluation_periods.setter
    def evaluation_periods(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "evaluation_periods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationPeriods", value)

    @builtins.property
    @jsii.member(jsii_name="maximum")
    def maximum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maximum"))

    @maximum.setter
    def maximum(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "maximum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximum", value)

    @builtins.property
    @jsii.member(jsii_name="maxTargetCapacity")
    def max_target_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxTargetCapacity"))

    @max_target_capacity.setter
    def max_target_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "max_target_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTargetCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "metric_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="minimum")
    def minimum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimum"))

    @minimum.setter
    def minimum(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "minimum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimum", value)

    @builtins.property
    @jsii.member(jsii_name="minTargetCapacity")
    def min_target_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minTargetCapacity"))

    @min_target_capacity.setter
    def min_target_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "min_target_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minTargetCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "period"))

    @period.setter
    def period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "statistic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statistic", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MrscalerAwsTaskScalingUpPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MrscalerAwsTaskScalingUpPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MrscalerAwsTaskScalingUpPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTaskScalingUpPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsTerminationPolicies",
    jsii_struct_bases=[],
    name_mapping={"statements": "statements"},
)
class MrscalerAwsTerminationPolicies:
    def __init__(
        self,
        *,
        statements: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsTerminationPoliciesStatements", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param statements: statements block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#statements MrscalerAws#statements}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsTerminationPolicies.__init__)
            check_type(argname="argument statements", value=statements, expected_type=type_hints["statements"])
        self._values: typing.Dict[str, typing.Any] = {
            "statements": statements,
        }

    @builtins.property
    def statements(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTerminationPoliciesStatements"]]:
        '''statements block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#statements MrscalerAws#statements}
        '''
        result = self._values.get("statements")
        assert result is not None, "Required property 'statements' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTerminationPoliciesStatements"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MrscalerAwsTerminationPolicies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MrscalerAwsTerminationPoliciesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsTerminationPoliciesList",
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
            type_hints = typing.get_type_hints(MrscalerAwsTerminationPoliciesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MrscalerAwsTerminationPoliciesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsTerminationPoliciesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MrscalerAwsTerminationPoliciesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTerminationPoliciesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTerminationPoliciesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTerminationPoliciesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsTerminationPolicies]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsTerminationPolicies]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsTerminationPolicies]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTerminationPoliciesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MrscalerAwsTerminationPoliciesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsTerminationPoliciesOutputReference",
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
            type_hints = typing.get_type_hints(MrscalerAwsTerminationPoliciesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putStatements")
    def put_statements(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MrscalerAwsTerminationPoliciesStatements", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsTerminationPoliciesOutputReference.put_statements)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStatements", [value]))

    @builtins.property
    @jsii.member(jsii_name="statements")
    def statements(self) -> "MrscalerAwsTerminationPoliciesStatementsList":
        return typing.cast("MrscalerAwsTerminationPoliciesStatementsList", jsii.get(self, "statements"))

    @builtins.property
    @jsii.member(jsii_name="statementsInput")
    def statements_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTerminationPoliciesStatements"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MrscalerAwsTerminationPoliciesStatements"]]], jsii.get(self, "statementsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MrscalerAwsTerminationPolicies, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MrscalerAwsTerminationPolicies, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MrscalerAwsTerminationPolicies, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTerminationPoliciesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsTerminationPoliciesStatements",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "threshold": "threshold",
        "evaluation_periods": "evaluationPeriods",
        "operator": "operator",
        "period": "period",
        "statistic": "statistic",
        "unit": "unit",
    },
)
class MrscalerAwsTerminationPoliciesStatements:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        threshold: jsii.Number,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        operator: typing.Optional[builtins.str] = None,
        period: typing.Optional[jsii.Number] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#metric_name MrscalerAws#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#namespace MrscalerAws#namespace}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#threshold MrscalerAws#threshold}.
        :param evaluation_periods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#evaluation_periods MrscalerAws#evaluation_periods}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#operator MrscalerAws#operator}.
        :param period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#period MrscalerAws#period}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#statistic MrscalerAws#statistic}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#unit MrscalerAws#unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsTerminationPoliciesStatements.__init__)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
            "threshold": threshold,
        }
        if evaluation_periods is not None:
            self._values["evaluation_periods"] = evaluation_periods
        if operator is not None:
            self._values["operator"] = operator
        if period is not None:
            self._values["period"] = period
        if statistic is not None:
            self._values["statistic"] = statistic
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#metric_name MrscalerAws#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#namespace MrscalerAws#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#threshold MrscalerAws#threshold}.'''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#evaluation_periods MrscalerAws#evaluation_periods}.'''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#operator MrscalerAws#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#period MrscalerAws#period}.'''
        result = self._values.get("period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#statistic MrscalerAws#statistic}.'''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/mrscaler_aws#unit MrscalerAws#unit}.'''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MrscalerAwsTerminationPoliciesStatements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MrscalerAwsTerminationPoliciesStatementsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsTerminationPoliciesStatementsList",
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
            type_hints = typing.get_type_hints(MrscalerAwsTerminationPoliciesStatementsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MrscalerAwsTerminationPoliciesStatementsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MrscalerAwsTerminationPoliciesStatementsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MrscalerAwsTerminationPoliciesStatementsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTerminationPoliciesStatementsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTerminationPoliciesStatementsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTerminationPoliciesStatementsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsTerminationPoliciesStatements]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsTerminationPoliciesStatements]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MrscalerAwsTerminationPoliciesStatements]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTerminationPoliciesStatementsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MrscalerAwsTerminationPoliciesStatementsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.mrscalerAws.MrscalerAwsTerminationPoliciesStatementsOutputReference",
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
            type_hints = typing.get_type_hints(MrscalerAwsTerminationPoliciesStatementsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEvaluationPeriods")
    def reset_evaluation_periods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluationPeriods", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @jsii.member(jsii_name="resetStatistic")
    def reset_statistic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatistic", []))

    @jsii.member(jsii_name="resetUnit")
    def reset_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnit", []))

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
    @jsii.member(jsii_name="evaluationPeriods")
    def evaluation_periods(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "evaluationPeriods"))

    @evaluation_periods.setter
    def evaluation_periods(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTerminationPoliciesStatementsOutputReference, "evaluation_periods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationPeriods", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTerminationPoliciesStatementsOutputReference, "metric_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTerminationPoliciesStatementsOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTerminationPoliciesStatementsOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "period"))

    @period.setter
    def period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTerminationPoliciesStatementsOutputReference, "period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTerminationPoliciesStatementsOutputReference, "statistic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statistic", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTerminationPoliciesStatementsOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTerminationPoliciesStatementsOutputReference, "unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MrscalerAwsTerminationPoliciesStatements, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MrscalerAwsTerminationPoliciesStatements, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MrscalerAwsTerminationPoliciesStatements, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MrscalerAwsTerminationPoliciesStatementsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MrscalerAws",
    "MrscalerAwsApplications",
    "MrscalerAwsApplicationsList",
    "MrscalerAwsApplicationsOutputReference",
    "MrscalerAwsBootstrapActionsFile",
    "MrscalerAwsBootstrapActionsFileList",
    "MrscalerAwsBootstrapActionsFileOutputReference",
    "MrscalerAwsConfig",
    "MrscalerAwsConfigurationsFile",
    "MrscalerAwsConfigurationsFileList",
    "MrscalerAwsConfigurationsFileOutputReference",
    "MrscalerAwsCoreEbsBlockDevice",
    "MrscalerAwsCoreEbsBlockDeviceList",
    "MrscalerAwsCoreEbsBlockDeviceOutputReference",
    "MrscalerAwsCoreScalingDownPolicy",
    "MrscalerAwsCoreScalingDownPolicyList",
    "MrscalerAwsCoreScalingDownPolicyOutputReference",
    "MrscalerAwsCoreScalingUpPolicy",
    "MrscalerAwsCoreScalingUpPolicyList",
    "MrscalerAwsCoreScalingUpPolicyOutputReference",
    "MrscalerAwsInstanceWeights",
    "MrscalerAwsInstanceWeightsList",
    "MrscalerAwsInstanceWeightsOutputReference",
    "MrscalerAwsMasterEbsBlockDevice",
    "MrscalerAwsMasterEbsBlockDeviceList",
    "MrscalerAwsMasterEbsBlockDeviceOutputReference",
    "MrscalerAwsProvisioningTimeout",
    "MrscalerAwsProvisioningTimeoutOutputReference",
    "MrscalerAwsScheduledTask",
    "MrscalerAwsScheduledTaskList",
    "MrscalerAwsScheduledTaskOutputReference",
    "MrscalerAwsStepsFile",
    "MrscalerAwsStepsFileList",
    "MrscalerAwsStepsFileOutputReference",
    "MrscalerAwsTags",
    "MrscalerAwsTagsList",
    "MrscalerAwsTagsOutputReference",
    "MrscalerAwsTaskEbsBlockDevice",
    "MrscalerAwsTaskEbsBlockDeviceList",
    "MrscalerAwsTaskEbsBlockDeviceOutputReference",
    "MrscalerAwsTaskScalingDownPolicy",
    "MrscalerAwsTaskScalingDownPolicyList",
    "MrscalerAwsTaskScalingDownPolicyOutputReference",
    "MrscalerAwsTaskScalingUpPolicy",
    "MrscalerAwsTaskScalingUpPolicyList",
    "MrscalerAwsTaskScalingUpPolicyOutputReference",
    "MrscalerAwsTerminationPolicies",
    "MrscalerAwsTerminationPoliciesList",
    "MrscalerAwsTerminationPoliciesOutputReference",
    "MrscalerAwsTerminationPoliciesStatements",
    "MrscalerAwsTerminationPoliciesStatementsList",
    "MrscalerAwsTerminationPoliciesStatementsOutputReference",
]

publication.publish()
