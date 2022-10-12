'''
# `spotinst_ocean_ecs`

Refer to the Terraform Registory for docs: [`spotinst_ocean_ecs`](https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs).
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


class OceanEcs(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcs",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs spotinst_ocean_ecs}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cluster_name: builtins.str,
        name: builtins.str,
        region: builtins.str,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
        associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        autoscaler: typing.Optional[typing.Union["OceanEcsAutoscaler", typing.Dict[str, typing.Any]]] = None,
        block_device_mappings: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsBlockDeviceMappings", typing.Dict[str, typing.Any]]]]] = None,
        desired_capacity: typing.Optional[jsii.Number] = None,
        draining_timeout: typing.Optional[jsii.Number] = None,
        ebs_optimized: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        iam_instance_profile: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        image_id: typing.Optional[builtins.str] = None,
        instance_metadata_options: typing.Optional[typing.Union["OceanEcsInstanceMetadataOptions", typing.Dict[str, typing.Any]]] = None,
        key_pair: typing.Optional[builtins.str] = None,
        logging: typing.Optional[typing.Union["OceanEcsLogging", typing.Dict[str, typing.Any]]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        optimize_images: typing.Optional[typing.Union["OceanEcsOptimizeImages", typing.Dict[str, typing.Any]]] = None,
        scheduled_task: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsScheduledTask", typing.Dict[str, typing.Any]]]]] = None,
        spot_percentage: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsTags", typing.Dict[str, typing.Any]]]]] = None,
        update_policy: typing.Optional[typing.Union["OceanEcsUpdatePolicy", typing.Dict[str, typing.Any]]] = None,
        use_as_template_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        user_data: typing.Optional[builtins.str] = None,
        utilize_commitments: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        utilize_reserved_instances: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs spotinst_ocean_ecs} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#cluster_name OceanEcs#cluster_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#name OceanEcs#name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#region OceanEcs#region}.
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#security_group_ids OceanEcs#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#subnet_ids OceanEcs#subnet_ids}.
        :param associate_public_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#associate_public_ip_address OceanEcs#associate_public_ip_address}.
        :param autoscaler: autoscaler block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#autoscaler OceanEcs#autoscaler}
        :param block_device_mappings: block_device_mappings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#block_device_mappings OceanEcs#block_device_mappings}
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#desired_capacity OceanEcs#desired_capacity}.
        :param draining_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#draining_timeout OceanEcs#draining_timeout}.
        :param ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#ebs_optimized OceanEcs#ebs_optimized}.
        :param iam_instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#iam_instance_profile OceanEcs#iam_instance_profile}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#id OceanEcs#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#image_id OceanEcs#image_id}.
        :param instance_metadata_options: instance_metadata_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#instance_metadata_options OceanEcs#instance_metadata_options}
        :param key_pair: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#key_pair OceanEcs#key_pair}.
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#logging OceanEcs#logging}
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#max_size OceanEcs#max_size}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#min_size OceanEcs#min_size}.
        :param monitoring: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#monitoring OceanEcs#monitoring}.
        :param optimize_images: optimize_images block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#optimize_images OceanEcs#optimize_images}
        :param scheduled_task: scheduled_task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#scheduled_task OceanEcs#scheduled_task}
        :param spot_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#spot_percentage OceanEcs#spot_percentage}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#tags OceanEcs#tags}
        :param update_policy: update_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#update_policy OceanEcs#update_policy}
        :param use_as_template_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#use_as_template_only OceanEcs#use_as_template_only}.
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#user_data OceanEcs#user_data}.
        :param utilize_commitments: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#utilize_commitments OceanEcs#utilize_commitments}.
        :param utilize_reserved_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#utilize_reserved_instances OceanEcs#utilize_reserved_instances}.
        :param whitelist: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#whitelist OceanEcs#whitelist}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcs.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OceanEcsConfig(
            cluster_name=cluster_name,
            name=name,
            region=region,
            security_group_ids=security_group_ids,
            subnet_ids=subnet_ids,
            associate_public_ip_address=associate_public_ip_address,
            autoscaler=autoscaler,
            block_device_mappings=block_device_mappings,
            desired_capacity=desired_capacity,
            draining_timeout=draining_timeout,
            ebs_optimized=ebs_optimized,
            iam_instance_profile=iam_instance_profile,
            id=id,
            image_id=image_id,
            instance_metadata_options=instance_metadata_options,
            key_pair=key_pair,
            logging=logging,
            max_size=max_size,
            min_size=min_size,
            monitoring=monitoring,
            optimize_images=optimize_images,
            scheduled_task=scheduled_task,
            spot_percentage=spot_percentage,
            tags=tags,
            update_policy=update_policy,
            use_as_template_only=use_as_template_only,
            user_data=user_data,
            utilize_commitments=utilize_commitments,
            utilize_reserved_instances=utilize_reserved_instances,
            whitelist=whitelist,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAutoscaler")
    def put_autoscaler(
        self,
        *,
        auto_headroom_percentage: typing.Optional[jsii.Number] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        down: typing.Optional[typing.Union["OceanEcsAutoscalerDown", typing.Dict[str, typing.Any]]] = None,
        headroom: typing.Optional[typing.Union["OceanEcsAutoscalerHeadroom", typing.Dict[str, typing.Any]]] = None,
        is_auto_config: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        resource_limits: typing.Optional[typing.Union["OceanEcsAutoscalerResourceLimits", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param auto_headroom_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#auto_headroom_percentage OceanEcs#auto_headroom_percentage}.
        :param cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#cooldown OceanEcs#cooldown}.
        :param down: down block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#down OceanEcs#down}
        :param headroom: headroom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#headroom OceanEcs#headroom}
        :param is_auto_config: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#is_auto_config OceanEcs#is_auto_config}.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#is_enabled OceanEcs#is_enabled}.
        :param resource_limits: resource_limits block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#resource_limits OceanEcs#resource_limits}
        '''
        value = OceanEcsAutoscaler(
            auto_headroom_percentage=auto_headroom_percentage,
            cooldown=cooldown,
            down=down,
            headroom=headroom,
            is_auto_config=is_auto_config,
            is_enabled=is_enabled,
            resource_limits=resource_limits,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscaler", [value]))

    @jsii.member(jsii_name="putBlockDeviceMappings")
    def put_block_device_mappings(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsBlockDeviceMappings", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcs.put_block_device_mappings)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBlockDeviceMappings", [value]))

    @jsii.member(jsii_name="putInstanceMetadataOptions")
    def put_instance_metadata_options(
        self,
        *,
        http_tokens: builtins.str,
        http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param http_tokens: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#http_tokens OceanEcs#http_tokens}.
        :param http_put_response_hop_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#http_put_response_hop_limit OceanEcs#http_put_response_hop_limit}.
        '''
        value = OceanEcsInstanceMetadataOptions(
            http_tokens=http_tokens,
            http_put_response_hop_limit=http_put_response_hop_limit,
        )

        return typing.cast(None, jsii.invoke(self, "putInstanceMetadataOptions", [value]))

    @jsii.member(jsii_name="putLogging")
    def put_logging(
        self,
        *,
        export: typing.Optional[typing.Union["OceanEcsLoggingExport", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param export: export block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#export OceanEcs#export}
        '''
        value = OceanEcsLogging(export=export)

        return typing.cast(None, jsii.invoke(self, "putLogging", [value]))

    @jsii.member(jsii_name="putOptimizeImages")
    def put_optimize_images(
        self,
        *,
        perform_at: builtins.str,
        should_optimize_ecs_ami: typing.Union[builtins.bool, cdktf.IResolvable],
        time_windows: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param perform_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#perform_at OceanEcs#perform_at}.
        :param should_optimize_ecs_ami: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#should_optimize_ecs_ami OceanEcs#should_optimize_ecs_ami}.
        :param time_windows: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#time_windows OceanEcs#time_windows}.
        '''
        value = OceanEcsOptimizeImages(
            perform_at=perform_at,
            should_optimize_ecs_ami=should_optimize_ecs_ami,
            time_windows=time_windows,
        )

        return typing.cast(None, jsii.invoke(self, "putOptimizeImages", [value]))

    @jsii.member(jsii_name="putScheduledTask")
    def put_scheduled_task(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsScheduledTask", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcs.put_scheduled_task)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScheduledTask", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsTags", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcs.put_tags)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="putUpdatePolicy")
    def put_update_policy(
        self,
        *,
        should_roll: typing.Union[builtins.bool, cdktf.IResolvable],
        auto_apply_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        conditioned_roll: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        roll_config: typing.Optional[typing.Union["OceanEcsUpdatePolicyRollConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param should_roll: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#should_roll OceanEcs#should_roll}.
        :param auto_apply_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#auto_apply_tags OceanEcs#auto_apply_tags}.
        :param conditioned_roll: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#conditioned_roll OceanEcs#conditioned_roll}.
        :param roll_config: roll_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#roll_config OceanEcs#roll_config}
        '''
        value = OceanEcsUpdatePolicy(
            should_roll=should_roll,
            auto_apply_tags=auto_apply_tags,
            conditioned_roll=conditioned_roll,
            roll_config=roll_config,
        )

        return typing.cast(None, jsii.invoke(self, "putUpdatePolicy", [value]))

    @jsii.member(jsii_name="resetAssociatePublicIpAddress")
    def reset_associate_public_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssociatePublicIpAddress", []))

    @jsii.member(jsii_name="resetAutoscaler")
    def reset_autoscaler(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaler", []))

    @jsii.member(jsii_name="resetBlockDeviceMappings")
    def reset_block_device_mappings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockDeviceMappings", []))

    @jsii.member(jsii_name="resetDesiredCapacity")
    def reset_desired_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredCapacity", []))

    @jsii.member(jsii_name="resetDrainingTimeout")
    def reset_draining_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDrainingTimeout", []))

    @jsii.member(jsii_name="resetEbsOptimized")
    def reset_ebs_optimized(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsOptimized", []))

    @jsii.member(jsii_name="resetIamInstanceProfile")
    def reset_iam_instance_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamInstanceProfile", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImageId")
    def reset_image_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageId", []))

    @jsii.member(jsii_name="resetInstanceMetadataOptions")
    def reset_instance_metadata_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceMetadataOptions", []))

    @jsii.member(jsii_name="resetKeyPair")
    def reset_key_pair(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyPair", []))

    @jsii.member(jsii_name="resetLogging")
    def reset_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogging", []))

    @jsii.member(jsii_name="resetMaxSize")
    def reset_max_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxSize", []))

    @jsii.member(jsii_name="resetMinSize")
    def reset_min_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinSize", []))

    @jsii.member(jsii_name="resetMonitoring")
    def reset_monitoring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitoring", []))

    @jsii.member(jsii_name="resetOptimizeImages")
    def reset_optimize_images(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptimizeImages", []))

    @jsii.member(jsii_name="resetScheduledTask")
    def reset_scheduled_task(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduledTask", []))

    @jsii.member(jsii_name="resetSpotPercentage")
    def reset_spot_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotPercentage", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetUpdatePolicy")
    def reset_update_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdatePolicy", []))

    @jsii.member(jsii_name="resetUseAsTemplateOnly")
    def reset_use_as_template_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseAsTemplateOnly", []))

    @jsii.member(jsii_name="resetUserData")
    def reset_user_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserData", []))

    @jsii.member(jsii_name="resetUtilizeCommitments")
    def reset_utilize_commitments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUtilizeCommitments", []))

    @jsii.member(jsii_name="resetUtilizeReservedInstances")
    def reset_utilize_reserved_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUtilizeReservedInstances", []))

    @jsii.member(jsii_name="resetWhitelist")
    def reset_whitelist(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhitelist", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="autoscaler")
    def autoscaler(self) -> "OceanEcsAutoscalerOutputReference":
        return typing.cast("OceanEcsAutoscalerOutputReference", jsii.get(self, "autoscaler"))

    @builtins.property
    @jsii.member(jsii_name="blockDeviceMappings")
    def block_device_mappings(self) -> "OceanEcsBlockDeviceMappingsList":
        return typing.cast("OceanEcsBlockDeviceMappingsList", jsii.get(self, "blockDeviceMappings"))

    @builtins.property
    @jsii.member(jsii_name="instanceMetadataOptions")
    def instance_metadata_options(
        self,
    ) -> "OceanEcsInstanceMetadataOptionsOutputReference":
        return typing.cast("OceanEcsInstanceMetadataOptionsOutputReference", jsii.get(self, "instanceMetadataOptions"))

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> "OceanEcsLoggingOutputReference":
        return typing.cast("OceanEcsLoggingOutputReference", jsii.get(self, "logging"))

    @builtins.property
    @jsii.member(jsii_name="optimizeImages")
    def optimize_images(self) -> "OceanEcsOptimizeImagesOutputReference":
        return typing.cast("OceanEcsOptimizeImagesOutputReference", jsii.get(self, "optimizeImages"))

    @builtins.property
    @jsii.member(jsii_name="scheduledTask")
    def scheduled_task(self) -> "OceanEcsScheduledTaskList":
        return typing.cast("OceanEcsScheduledTaskList", jsii.get(self, "scheduledTask"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "OceanEcsTagsList":
        return typing.cast("OceanEcsTagsList", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="updatePolicy")
    def update_policy(self) -> "OceanEcsUpdatePolicyOutputReference":
        return typing.cast("OceanEcsUpdatePolicyOutputReference", jsii.get(self, "updatePolicy"))

    @builtins.property
    @jsii.member(jsii_name="associatePublicIpAddressInput")
    def associate_public_ip_address_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "associatePublicIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscalerInput")
    def autoscaler_input(self) -> typing.Optional["OceanEcsAutoscaler"]:
        return typing.cast(typing.Optional["OceanEcsAutoscaler"], jsii.get(self, "autoscalerInput"))

    @builtins.property
    @jsii.member(jsii_name="blockDeviceMappingsInput")
    def block_device_mappings_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsBlockDeviceMappings"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsBlockDeviceMappings"]]], jsii.get(self, "blockDeviceMappingsInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterNameInput")
    def cluster_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredCapacityInput")
    def desired_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "desiredCapacityInput"))

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
    @jsii.member(jsii_name="instanceMetadataOptionsInput")
    def instance_metadata_options_input(
        self,
    ) -> typing.Optional["OceanEcsInstanceMetadataOptions"]:
        return typing.cast(typing.Optional["OceanEcsInstanceMetadataOptions"], jsii.get(self, "instanceMetadataOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="keyPairInput")
    def key_pair_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyPairInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingInput")
    def logging_input(self) -> typing.Optional["OceanEcsLogging"]:
        return typing.cast(typing.Optional["OceanEcsLogging"], jsii.get(self, "loggingInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSizeInput")
    def max_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="minSizeInput")
    def min_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="monitoringInput")
    def monitoring_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "monitoringInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="optimizeImagesInput")
    def optimize_images_input(self) -> typing.Optional["OceanEcsOptimizeImages"]:
        return typing.cast(typing.Optional["OceanEcsOptimizeImages"], jsii.get(self, "optimizeImagesInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduledTaskInput")
    def scheduled_task_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsScheduledTask"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsScheduledTask"]]], jsii.get(self, "scheduledTaskInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="spotPercentageInput")
    def spot_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "spotPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsTags"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsTags"]]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="updatePolicyInput")
    def update_policy_input(self) -> typing.Optional["OceanEcsUpdatePolicy"]:
        return typing.cast(typing.Optional["OceanEcsUpdatePolicy"], jsii.get(self, "updatePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="useAsTemplateOnlyInput")
    def use_as_template_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useAsTemplateOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="userDataInput")
    def user_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userDataInput"))

    @builtins.property
    @jsii.member(jsii_name="utilizeCommitmentsInput")
    def utilize_commitments_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "utilizeCommitmentsInput"))

    @builtins.property
    @jsii.member(jsii_name="utilizeReservedInstancesInput")
    def utilize_reserved_instances_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "utilizeReservedInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="whitelistInput")
    def whitelist_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "whitelistInput"))

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
            type_hints = typing.get_type_hints(getattr(OceanEcs, "associate_public_ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatePublicIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "cluster_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="desiredCapacity")
    def desired_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredCapacity"))

    @desired_capacity.setter
    def desired_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "desired_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="drainingTimeout")
    def draining_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "drainingTimeout"))

    @draining_timeout.setter
    def draining_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "draining_timeout").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcs, "ebs_optimized").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsOptimized", value)

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfile")
    def iam_instance_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamInstanceProfile"))

    @iam_instance_profile.setter
    def iam_instance_profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "iam_instance_profile").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamInstanceProfile", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="imageId")
    def image_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageId"))

    @image_id.setter
    def image_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "image_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageId", value)

    @builtins.property
    @jsii.member(jsii_name="keyPair")
    def key_pair(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyPair"))

    @key_pair.setter
    def key_pair(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "key_pair").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyPair", value)

    @builtins.property
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSize"))

    @max_size.setter
    def max_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "max_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSize", value)

    @builtins.property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minSize"))

    @min_size.setter
    def min_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "min_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minSize", value)

    @builtins.property
    @jsii.member(jsii_name="monitoring")
    def monitoring(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "monitoring"))

    @monitoring.setter
    def monitoring(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "monitoring").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitoring", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "security_group_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="spotPercentage")
    def spot_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotPercentage"))

    @spot_percentage.setter
    def spot_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "spot_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "subnet_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="useAsTemplateOnly")
    def use_as_template_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useAsTemplateOnly"))

    @use_as_template_only.setter
    def use_as_template_only(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "use_as_template_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useAsTemplateOnly", value)

    @builtins.property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userData"))

    @user_data.setter
    def user_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "user_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userData", value)

    @builtins.property
    @jsii.member(jsii_name="utilizeCommitments")
    def utilize_commitments(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "utilizeCommitments"))

    @utilize_commitments.setter
    def utilize_commitments(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "utilize_commitments").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "utilizeCommitments", value)

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
            type_hints = typing.get_type_hints(getattr(OceanEcs, "utilize_reserved_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "utilizeReservedInstances", value)

    @builtins.property
    @jsii.member(jsii_name="whitelist")
    def whitelist(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "whitelist"))

    @whitelist.setter
    def whitelist(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcs, "whitelist").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whitelist", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsAutoscaler",
    jsii_struct_bases=[],
    name_mapping={
        "auto_headroom_percentage": "autoHeadroomPercentage",
        "cooldown": "cooldown",
        "down": "down",
        "headroom": "headroom",
        "is_auto_config": "isAutoConfig",
        "is_enabled": "isEnabled",
        "resource_limits": "resourceLimits",
    },
)
class OceanEcsAutoscaler:
    def __init__(
        self,
        *,
        auto_headroom_percentage: typing.Optional[jsii.Number] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        down: typing.Optional[typing.Union["OceanEcsAutoscalerDown", typing.Dict[str, typing.Any]]] = None,
        headroom: typing.Optional[typing.Union["OceanEcsAutoscalerHeadroom", typing.Dict[str, typing.Any]]] = None,
        is_auto_config: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        resource_limits: typing.Optional[typing.Union["OceanEcsAutoscalerResourceLimits", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param auto_headroom_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#auto_headroom_percentage OceanEcs#auto_headroom_percentage}.
        :param cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#cooldown OceanEcs#cooldown}.
        :param down: down block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#down OceanEcs#down}
        :param headroom: headroom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#headroom OceanEcs#headroom}
        :param is_auto_config: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#is_auto_config OceanEcs#is_auto_config}.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#is_enabled OceanEcs#is_enabled}.
        :param resource_limits: resource_limits block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#resource_limits OceanEcs#resource_limits}
        '''
        if isinstance(down, dict):
            down = OceanEcsAutoscalerDown(**down)
        if isinstance(headroom, dict):
            headroom = OceanEcsAutoscalerHeadroom(**headroom)
        if isinstance(resource_limits, dict):
            resource_limits = OceanEcsAutoscalerResourceLimits(**resource_limits)
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsAutoscaler.__init__)
            check_type(argname="argument auto_headroom_percentage", value=auto_headroom_percentage, expected_type=type_hints["auto_headroom_percentage"])
            check_type(argname="argument cooldown", value=cooldown, expected_type=type_hints["cooldown"])
            check_type(argname="argument down", value=down, expected_type=type_hints["down"])
            check_type(argname="argument headroom", value=headroom, expected_type=type_hints["headroom"])
            check_type(argname="argument is_auto_config", value=is_auto_config, expected_type=type_hints["is_auto_config"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument resource_limits", value=resource_limits, expected_type=type_hints["resource_limits"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_headroom_percentage is not None:
            self._values["auto_headroom_percentage"] = auto_headroom_percentage
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if down is not None:
            self._values["down"] = down
        if headroom is not None:
            self._values["headroom"] = headroom
        if is_auto_config is not None:
            self._values["is_auto_config"] = is_auto_config
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if resource_limits is not None:
            self._values["resource_limits"] = resource_limits

    @builtins.property
    def auto_headroom_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#auto_headroom_percentage OceanEcs#auto_headroom_percentage}.'''
        result = self._values.get("auto_headroom_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#cooldown OceanEcs#cooldown}.'''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def down(self) -> typing.Optional["OceanEcsAutoscalerDown"]:
        '''down block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#down OceanEcs#down}
        '''
        result = self._values.get("down")
        return typing.cast(typing.Optional["OceanEcsAutoscalerDown"], result)

    @builtins.property
    def headroom(self) -> typing.Optional["OceanEcsAutoscalerHeadroom"]:
        '''headroom block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#headroom OceanEcs#headroom}
        '''
        result = self._values.get("headroom")
        return typing.cast(typing.Optional["OceanEcsAutoscalerHeadroom"], result)

    @builtins.property
    def is_auto_config(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#is_auto_config OceanEcs#is_auto_config}.'''
        result = self._values.get("is_auto_config")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#is_enabled OceanEcs#is_enabled}.'''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def resource_limits(self) -> typing.Optional["OceanEcsAutoscalerResourceLimits"]:
        '''resource_limits block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#resource_limits OceanEcs#resource_limits}
        '''
        result = self._values.get("resource_limits")
        return typing.cast(typing.Optional["OceanEcsAutoscalerResourceLimits"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsAutoscaler(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsAutoscalerDown",
    jsii_struct_bases=[],
    name_mapping={"max_scale_down_percentage": "maxScaleDownPercentage"},
)
class OceanEcsAutoscalerDown:
    def __init__(
        self,
        *,
        max_scale_down_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_scale_down_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#max_scale_down_percentage OceanEcs#max_scale_down_percentage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsAutoscalerDown.__init__)
            check_type(argname="argument max_scale_down_percentage", value=max_scale_down_percentage, expected_type=type_hints["max_scale_down_percentage"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_scale_down_percentage is not None:
            self._values["max_scale_down_percentage"] = max_scale_down_percentage

    @builtins.property
    def max_scale_down_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#max_scale_down_percentage OceanEcs#max_scale_down_percentage}.'''
        result = self._values.get("max_scale_down_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsAutoscalerDown(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsAutoscalerDownOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsAutoscalerDownOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsAutoscalerDownOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxScaleDownPercentage")
    def reset_max_scale_down_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxScaleDownPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="maxScaleDownPercentageInput")
    def max_scale_down_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxScaleDownPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="maxScaleDownPercentage")
    def max_scale_down_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxScaleDownPercentage"))

    @max_scale_down_percentage.setter
    def max_scale_down_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsAutoscalerDownOutputReference, "max_scale_down_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxScaleDownPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanEcsAutoscalerDown]:
        return typing.cast(typing.Optional[OceanEcsAutoscalerDown], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OceanEcsAutoscalerDown]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsAutoscalerDownOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsAutoscalerHeadroom",
    jsii_struct_bases=[],
    name_mapping={
        "cpu_per_unit": "cpuPerUnit",
        "memory_per_unit": "memoryPerUnit",
        "num_of_units": "numOfUnits",
    },
)
class OceanEcsAutoscalerHeadroom:
    def __init__(
        self,
        *,
        cpu_per_unit: typing.Optional[jsii.Number] = None,
        memory_per_unit: typing.Optional[jsii.Number] = None,
        num_of_units: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#cpu_per_unit OceanEcs#cpu_per_unit}.
        :param memory_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#memory_per_unit OceanEcs#memory_per_unit}.
        :param num_of_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#num_of_units OceanEcs#num_of_units}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsAutoscalerHeadroom.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#cpu_per_unit OceanEcs#cpu_per_unit}.'''
        result = self._values.get("cpu_per_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_per_unit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#memory_per_unit OceanEcs#memory_per_unit}.'''
        result = self._values.get("memory_per_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def num_of_units(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#num_of_units OceanEcs#num_of_units}.'''
        result = self._values.get("num_of_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsAutoscalerHeadroom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsAutoscalerHeadroomOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsAutoscalerHeadroomOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsAutoscalerHeadroomOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsAutoscalerHeadroomOutputReference, "cpu_per_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuPerUnit", value)

    @builtins.property
    @jsii.member(jsii_name="memoryPerUnit")
    def memory_per_unit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryPerUnit"))

    @memory_per_unit.setter
    def memory_per_unit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsAutoscalerHeadroomOutputReference, "memory_per_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryPerUnit", value)

    @builtins.property
    @jsii.member(jsii_name="numOfUnits")
    def num_of_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numOfUnits"))

    @num_of_units.setter
    def num_of_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsAutoscalerHeadroomOutputReference, "num_of_units").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numOfUnits", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanEcsAutoscalerHeadroom]:
        return typing.cast(typing.Optional[OceanEcsAutoscalerHeadroom], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanEcsAutoscalerHeadroom],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsAutoscalerHeadroomOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanEcsAutoscalerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsAutoscalerOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsAutoscalerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDown")
    def put_down(
        self,
        *,
        max_scale_down_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_scale_down_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#max_scale_down_percentage OceanEcs#max_scale_down_percentage}.
        '''
        value = OceanEcsAutoscalerDown(
            max_scale_down_percentage=max_scale_down_percentage
        )

        return typing.cast(None, jsii.invoke(self, "putDown", [value]))

    @jsii.member(jsii_name="putHeadroom")
    def put_headroom(
        self,
        *,
        cpu_per_unit: typing.Optional[jsii.Number] = None,
        memory_per_unit: typing.Optional[jsii.Number] = None,
        num_of_units: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#cpu_per_unit OceanEcs#cpu_per_unit}.
        :param memory_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#memory_per_unit OceanEcs#memory_per_unit}.
        :param num_of_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#num_of_units OceanEcs#num_of_units}.
        '''
        value = OceanEcsAutoscalerHeadroom(
            cpu_per_unit=cpu_per_unit,
            memory_per_unit=memory_per_unit,
            num_of_units=num_of_units,
        )

        return typing.cast(None, jsii.invoke(self, "putHeadroom", [value]))

    @jsii.member(jsii_name="putResourceLimits")
    def put_resource_limits(
        self,
        *,
        max_memory_gib: typing.Optional[jsii.Number] = None,
        max_vcpu: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_memory_gib: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#max_memory_gib OceanEcs#max_memory_gib}.
        :param max_vcpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#max_vcpu OceanEcs#max_vcpu}.
        '''
        value = OceanEcsAutoscalerResourceLimits(
            max_memory_gib=max_memory_gib, max_vcpu=max_vcpu
        )

        return typing.cast(None, jsii.invoke(self, "putResourceLimits", [value]))

    @jsii.member(jsii_name="resetAutoHeadroomPercentage")
    def reset_auto_headroom_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoHeadroomPercentage", []))

    @jsii.member(jsii_name="resetCooldown")
    def reset_cooldown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCooldown", []))

    @jsii.member(jsii_name="resetDown")
    def reset_down(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDown", []))

    @jsii.member(jsii_name="resetHeadroom")
    def reset_headroom(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeadroom", []))

    @jsii.member(jsii_name="resetIsAutoConfig")
    def reset_is_auto_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsAutoConfig", []))

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetResourceLimits")
    def reset_resource_limits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceLimits", []))

    @builtins.property
    @jsii.member(jsii_name="down")
    def down(self) -> OceanEcsAutoscalerDownOutputReference:
        return typing.cast(OceanEcsAutoscalerDownOutputReference, jsii.get(self, "down"))

    @builtins.property
    @jsii.member(jsii_name="headroom")
    def headroom(self) -> OceanEcsAutoscalerHeadroomOutputReference:
        return typing.cast(OceanEcsAutoscalerHeadroomOutputReference, jsii.get(self, "headroom"))

    @builtins.property
    @jsii.member(jsii_name="resourceLimits")
    def resource_limits(self) -> "OceanEcsAutoscalerResourceLimitsOutputReference":
        return typing.cast("OceanEcsAutoscalerResourceLimitsOutputReference", jsii.get(self, "resourceLimits"))

    @builtins.property
    @jsii.member(jsii_name="autoHeadroomPercentageInput")
    def auto_headroom_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autoHeadroomPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="cooldownInput")
    def cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="downInput")
    def down_input(self) -> typing.Optional[OceanEcsAutoscalerDown]:
        return typing.cast(typing.Optional[OceanEcsAutoscalerDown], jsii.get(self, "downInput"))

    @builtins.property
    @jsii.member(jsii_name="headroomInput")
    def headroom_input(self) -> typing.Optional[OceanEcsAutoscalerHeadroom]:
        return typing.cast(typing.Optional[OceanEcsAutoscalerHeadroom], jsii.get(self, "headroomInput"))

    @builtins.property
    @jsii.member(jsii_name="isAutoConfigInput")
    def is_auto_config_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isAutoConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLimitsInput")
    def resource_limits_input(
        self,
    ) -> typing.Optional["OceanEcsAutoscalerResourceLimits"]:
        return typing.cast(typing.Optional["OceanEcsAutoscalerResourceLimits"], jsii.get(self, "resourceLimitsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoHeadroomPercentage")
    def auto_headroom_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autoHeadroomPercentage"))

    @auto_headroom_percentage.setter
    def auto_headroom_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsAutoscalerOutputReference, "auto_headroom_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoHeadroomPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="cooldown")
    def cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cooldown"))

    @cooldown.setter
    def cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsAutoscalerOutputReference, "cooldown").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cooldown", value)

    @builtins.property
    @jsii.member(jsii_name="isAutoConfig")
    def is_auto_config(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isAutoConfig"))

    @is_auto_config.setter
    def is_auto_config(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsAutoscalerOutputReference, "is_auto_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isAutoConfig", value)

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsAutoscalerOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanEcsAutoscaler]:
        return typing.cast(typing.Optional[OceanEcsAutoscaler], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OceanEcsAutoscaler]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsAutoscalerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsAutoscalerResourceLimits",
    jsii_struct_bases=[],
    name_mapping={"max_memory_gib": "maxMemoryGib", "max_vcpu": "maxVcpu"},
)
class OceanEcsAutoscalerResourceLimits:
    def __init__(
        self,
        *,
        max_memory_gib: typing.Optional[jsii.Number] = None,
        max_vcpu: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_memory_gib: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#max_memory_gib OceanEcs#max_memory_gib}.
        :param max_vcpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#max_vcpu OceanEcs#max_vcpu}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsAutoscalerResourceLimits.__init__)
            check_type(argname="argument max_memory_gib", value=max_memory_gib, expected_type=type_hints["max_memory_gib"])
            check_type(argname="argument max_vcpu", value=max_vcpu, expected_type=type_hints["max_vcpu"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_memory_gib is not None:
            self._values["max_memory_gib"] = max_memory_gib
        if max_vcpu is not None:
            self._values["max_vcpu"] = max_vcpu

    @builtins.property
    def max_memory_gib(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#max_memory_gib OceanEcs#max_memory_gib}.'''
        result = self._values.get("max_memory_gib")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_vcpu(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#max_vcpu OceanEcs#max_vcpu}.'''
        result = self._values.get("max_vcpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsAutoscalerResourceLimits(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsAutoscalerResourceLimitsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsAutoscalerResourceLimitsOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsAutoscalerResourceLimitsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxMemoryGib")
    def reset_max_memory_gib(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxMemoryGib", []))

    @jsii.member(jsii_name="resetMaxVcpu")
    def reset_max_vcpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxVcpu", []))

    @builtins.property
    @jsii.member(jsii_name="maxMemoryGibInput")
    def max_memory_gib_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxMemoryGibInput"))

    @builtins.property
    @jsii.member(jsii_name="maxVcpuInput")
    def max_vcpu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxVcpuInput"))

    @builtins.property
    @jsii.member(jsii_name="maxMemoryGib")
    def max_memory_gib(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxMemoryGib"))

    @max_memory_gib.setter
    def max_memory_gib(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsAutoscalerResourceLimitsOutputReference, "max_memory_gib").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxMemoryGib", value)

    @builtins.property
    @jsii.member(jsii_name="maxVcpu")
    def max_vcpu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxVcpu"))

    @max_vcpu.setter
    def max_vcpu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsAutoscalerResourceLimitsOutputReference, "max_vcpu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxVcpu", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanEcsAutoscalerResourceLimits]:
        return typing.cast(typing.Optional[OceanEcsAutoscalerResourceLimits], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanEcsAutoscalerResourceLimits],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsAutoscalerResourceLimitsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsBlockDeviceMappings",
    jsii_struct_bases=[],
    name_mapping={
        "device_name": "deviceName",
        "ebs": "ebs",
        "no_device": "noDevice",
        "virtual_name": "virtualName",
    },
)
class OceanEcsBlockDeviceMappings:
    def __init__(
        self,
        *,
        device_name: builtins.str,
        ebs: typing.Optional[typing.Union["OceanEcsBlockDeviceMappingsEbs", typing.Dict[str, typing.Any]]] = None,
        no_device: typing.Optional[builtins.str] = None,
        virtual_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param device_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#device_name OceanEcs#device_name}.
        :param ebs: ebs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#ebs OceanEcs#ebs}
        :param no_device: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#no_device OceanEcs#no_device}.
        :param virtual_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#virtual_name OceanEcs#virtual_name}.
        '''
        if isinstance(ebs, dict):
            ebs = OceanEcsBlockDeviceMappingsEbs(**ebs)
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsBlockDeviceMappings.__init__)
            check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
            check_type(argname="argument ebs", value=ebs, expected_type=type_hints["ebs"])
            check_type(argname="argument no_device", value=no_device, expected_type=type_hints["no_device"])
            check_type(argname="argument virtual_name", value=virtual_name, expected_type=type_hints["virtual_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "device_name": device_name,
        }
        if ebs is not None:
            self._values["ebs"] = ebs
        if no_device is not None:
            self._values["no_device"] = no_device
        if virtual_name is not None:
            self._values["virtual_name"] = virtual_name

    @builtins.property
    def device_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#device_name OceanEcs#device_name}.'''
        result = self._values.get("device_name")
        assert result is not None, "Required property 'device_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ebs(self) -> typing.Optional["OceanEcsBlockDeviceMappingsEbs"]:
        '''ebs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#ebs OceanEcs#ebs}
        '''
        result = self._values.get("ebs")
        return typing.cast(typing.Optional["OceanEcsBlockDeviceMappingsEbs"], result)

    @builtins.property
    def no_device(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#no_device OceanEcs#no_device}.'''
        result = self._values.get("no_device")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#virtual_name OceanEcs#virtual_name}.'''
        result = self._values.get("virtual_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsBlockDeviceMappings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsBlockDeviceMappingsEbs",
    jsii_struct_bases=[],
    name_mapping={
        "delete_on_termination": "deleteOnTermination",
        "dynamic_volume_size": "dynamicVolumeSize",
        "encrypted": "encrypted",
        "iops": "iops",
        "kms_key_id": "kmsKeyId",
        "snapshot_id": "snapshotId",
        "throughput": "throughput",
        "volume_size": "volumeSize",
        "volume_type": "volumeType",
    },
)
class OceanEcsBlockDeviceMappingsEbs:
    def __init__(
        self,
        *,
        delete_on_termination: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        dynamic_volume_size: typing.Optional[typing.Union["OceanEcsBlockDeviceMappingsEbsDynamicVolumeSize", typing.Dict[str, typing.Any]]] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#delete_on_termination OceanEcs#delete_on_termination}.
        :param dynamic_volume_size: dynamic_volume_size block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#dynamic_volume_size OceanEcs#dynamic_volume_size}
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#encrypted OceanEcs#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#iops OceanEcs#iops}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#kms_key_id OceanEcs#kms_key_id}.
        :param snapshot_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#snapshot_id OceanEcs#snapshot_id}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#throughput OceanEcs#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#volume_size OceanEcs#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#volume_type OceanEcs#volume_type}.
        '''
        if isinstance(dynamic_volume_size, dict):
            dynamic_volume_size = OceanEcsBlockDeviceMappingsEbsDynamicVolumeSize(**dynamic_volume_size)
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsBlockDeviceMappingsEbs.__init__)
            check_type(argname="argument delete_on_termination", value=delete_on_termination, expected_type=type_hints["delete_on_termination"])
            check_type(argname="argument dynamic_volume_size", value=dynamic_volume_size, expected_type=type_hints["dynamic_volume_size"])
            check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument snapshot_id", value=snapshot_id, expected_type=type_hints["snapshot_id"])
            check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if delete_on_termination is not None:
            self._values["delete_on_termination"] = delete_on_termination
        if dynamic_volume_size is not None:
            self._values["dynamic_volume_size"] = dynamic_volume_size
        if encrypted is not None:
            self._values["encrypted"] = encrypted
        if iops is not None:
            self._values["iops"] = iops
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if snapshot_id is not None:
            self._values["snapshot_id"] = snapshot_id
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#delete_on_termination OceanEcs#delete_on_termination}.'''
        result = self._values.get("delete_on_termination")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def dynamic_volume_size(
        self,
    ) -> typing.Optional["OceanEcsBlockDeviceMappingsEbsDynamicVolumeSize"]:
        '''dynamic_volume_size block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#dynamic_volume_size OceanEcs#dynamic_volume_size}
        '''
        result = self._values.get("dynamic_volume_size")
        return typing.cast(typing.Optional["OceanEcsBlockDeviceMappingsEbsDynamicVolumeSize"], result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#encrypted OceanEcs#encrypted}.'''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#iops OceanEcs#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#kms_key_id OceanEcs#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#snapshot_id OceanEcs#snapshot_id}.'''
        result = self._values.get("snapshot_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#throughput OceanEcs#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#volume_size OceanEcs#volume_size}.'''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#volume_type OceanEcs#volume_type}.'''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsBlockDeviceMappingsEbs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsBlockDeviceMappingsEbsDynamicVolumeSize",
    jsii_struct_bases=[],
    name_mapping={
        "base_size": "baseSize",
        "resource": "resource",
        "size_per_resource_unit": "sizePerResourceUnit",
    },
)
class OceanEcsBlockDeviceMappingsEbsDynamicVolumeSize:
    def __init__(
        self,
        *,
        base_size: jsii.Number,
        resource: builtins.str,
        size_per_resource_unit: jsii.Number,
    ) -> None:
        '''
        :param base_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#base_size OceanEcs#base_size}.
        :param resource: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#resource OceanEcs#resource}.
        :param size_per_resource_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#size_per_resource_unit OceanEcs#size_per_resource_unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsBlockDeviceMappingsEbsDynamicVolumeSize.__init__)
            check_type(argname="argument base_size", value=base_size, expected_type=type_hints["base_size"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument size_per_resource_unit", value=size_per_resource_unit, expected_type=type_hints["size_per_resource_unit"])
        self._values: typing.Dict[str, typing.Any] = {
            "base_size": base_size,
            "resource": resource,
            "size_per_resource_unit": size_per_resource_unit,
        }

    @builtins.property
    def base_size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#base_size OceanEcs#base_size}.'''
        result = self._values.get("base_size")
        assert result is not None, "Required property 'base_size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def resource(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#resource OceanEcs#resource}.'''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size_per_resource_unit(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#size_per_resource_unit OceanEcs#size_per_resource_unit}.'''
        result = self._values.get("size_per_resource_unit")
        assert result is not None, "Required property 'size_per_resource_unit' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsBlockDeviceMappingsEbsDynamicVolumeSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="baseSizeInput")
    def base_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "baseSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceInput")
    def resource_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceInput"))

    @builtins.property
    @jsii.member(jsii_name="sizePerResourceUnitInput")
    def size_per_resource_unit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizePerResourceUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="baseSize")
    def base_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "baseSize"))

    @base_size.setter
    def base_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference, "base_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseSize", value)

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @resource.setter
    def resource(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference, "resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @builtins.property
    @jsii.member(jsii_name="sizePerResourceUnit")
    def size_per_resource_unit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizePerResourceUnit"))

    @size_per_resource_unit.setter
    def size_per_resource_unit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference, "size_per_resource_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizePerResourceUnit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OceanEcsBlockDeviceMappingsEbsDynamicVolumeSize]:
        return typing.cast(typing.Optional[OceanEcsBlockDeviceMappingsEbsDynamicVolumeSize], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanEcsBlockDeviceMappingsEbsDynamicVolumeSize],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanEcsBlockDeviceMappingsEbsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsBlockDeviceMappingsEbsOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsBlockDeviceMappingsEbsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDynamicVolumeSize")
    def put_dynamic_volume_size(
        self,
        *,
        base_size: jsii.Number,
        resource: builtins.str,
        size_per_resource_unit: jsii.Number,
    ) -> None:
        '''
        :param base_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#base_size OceanEcs#base_size}.
        :param resource: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#resource OceanEcs#resource}.
        :param size_per_resource_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#size_per_resource_unit OceanEcs#size_per_resource_unit}.
        '''
        value = OceanEcsBlockDeviceMappingsEbsDynamicVolumeSize(
            base_size=base_size,
            resource=resource,
            size_per_resource_unit=size_per_resource_unit,
        )

        return typing.cast(None, jsii.invoke(self, "putDynamicVolumeSize", [value]))

    @jsii.member(jsii_name="resetDeleteOnTermination")
    def reset_delete_on_termination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteOnTermination", []))

    @jsii.member(jsii_name="resetDynamicVolumeSize")
    def reset_dynamic_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamicVolumeSize", []))

    @jsii.member(jsii_name="resetEncrypted")
    def reset_encrypted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncrypted", []))

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetSnapshotId")
    def reset_snapshot_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotId", []))

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
    @jsii.member(jsii_name="dynamicVolumeSize")
    def dynamic_volume_size(
        self,
    ) -> OceanEcsBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference:
        return typing.cast(OceanEcsBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference, jsii.get(self, "dynamicVolumeSize"))

    @builtins.property
    @jsii.member(jsii_name="deleteOnTerminationInput")
    def delete_on_termination_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deleteOnTerminationInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamicVolumeSizeInput")
    def dynamic_volume_size_input(
        self,
    ) -> typing.Optional[OceanEcsBlockDeviceMappingsEbsDynamicVolumeSize]:
        return typing.cast(typing.Optional[OceanEcsBlockDeviceMappingsEbsDynamicVolumeSize], jsii.get(self, "dynamicVolumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptedInput")
    def encrypted_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "encryptedInput"))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotIdInput")
    def snapshot_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotIdInput"))

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
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsEbsOutputReference, "delete_on_termination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteOnTermination", value)

    @builtins.property
    @jsii.member(jsii_name="encrypted")
    def encrypted(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "encrypted"))

    @encrypted.setter
    def encrypted(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsEbsOutputReference, "encrypted").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsEbsOutputReference, "iops").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsEbsOutputReference, "kms_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotId")
    def snapshot_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotId"))

    @snapshot_id.setter
    def snapshot_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsEbsOutputReference, "snapshot_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotId", value)

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsEbsOutputReference, "throughput").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value)

    @builtins.property
    @jsii.member(jsii_name="volumeSize")
    def volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumeSize"))

    @volume_size.setter
    def volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsEbsOutputReference, "volume_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsEbsOutputReference, "volume_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanEcsBlockDeviceMappingsEbs]:
        return typing.cast(typing.Optional[OceanEcsBlockDeviceMappingsEbs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanEcsBlockDeviceMappingsEbs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsEbsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanEcsBlockDeviceMappingsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsBlockDeviceMappingsList",
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
            type_hints = typing.get_type_hints(OceanEcsBlockDeviceMappingsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanEcsBlockDeviceMappingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsBlockDeviceMappingsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanEcsBlockDeviceMappingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsBlockDeviceMappings]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsBlockDeviceMappings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsBlockDeviceMappings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanEcsBlockDeviceMappingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsBlockDeviceMappingsOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsBlockDeviceMappingsOutputReference.__init__)
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
        dynamic_volume_size: typing.Optional[typing.Union[OceanEcsBlockDeviceMappingsEbsDynamicVolumeSize, typing.Dict[str, typing.Any]]] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#delete_on_termination OceanEcs#delete_on_termination}.
        :param dynamic_volume_size: dynamic_volume_size block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#dynamic_volume_size OceanEcs#dynamic_volume_size}
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#encrypted OceanEcs#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#iops OceanEcs#iops}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#kms_key_id OceanEcs#kms_key_id}.
        :param snapshot_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#snapshot_id OceanEcs#snapshot_id}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#throughput OceanEcs#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#volume_size OceanEcs#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#volume_type OceanEcs#volume_type}.
        '''
        value = OceanEcsBlockDeviceMappingsEbs(
            delete_on_termination=delete_on_termination,
            dynamic_volume_size=dynamic_volume_size,
            encrypted=encrypted,
            iops=iops,
            kms_key_id=kms_key_id,
            snapshot_id=snapshot_id,
            throughput=throughput,
            volume_size=volume_size,
            volume_type=volume_type,
        )

        return typing.cast(None, jsii.invoke(self, "putEbs", [value]))

    @jsii.member(jsii_name="resetEbs")
    def reset_ebs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbs", []))

    @jsii.member(jsii_name="resetNoDevice")
    def reset_no_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoDevice", []))

    @jsii.member(jsii_name="resetVirtualName")
    def reset_virtual_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualName", []))

    @builtins.property
    @jsii.member(jsii_name="ebs")
    def ebs(self) -> OceanEcsBlockDeviceMappingsEbsOutputReference:
        return typing.cast(OceanEcsBlockDeviceMappingsEbsOutputReference, jsii.get(self, "ebs"))

    @builtins.property
    @jsii.member(jsii_name="deviceNameInput")
    def device_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsInput")
    def ebs_input(self) -> typing.Optional[OceanEcsBlockDeviceMappingsEbs]:
        return typing.cast(typing.Optional[OceanEcsBlockDeviceMappingsEbs], jsii.get(self, "ebsInput"))

    @builtins.property
    @jsii.member(jsii_name="noDeviceInput")
    def no_device_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "noDeviceInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNameInput")
    def virtual_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceName"))

    @device_name.setter
    def device_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsOutputReference, "device_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceName", value)

    @builtins.property
    @jsii.member(jsii_name="noDevice")
    def no_device(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "noDevice"))

    @no_device.setter
    def no_device(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsOutputReference, "no_device").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noDevice", value)

    @builtins.property
    @jsii.member(jsii_name="virtualName")
    def virtual_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualName"))

    @virtual_name.setter
    def virtual_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsOutputReference, "virtual_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanEcsBlockDeviceMappings, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanEcsBlockDeviceMappings, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanEcsBlockDeviceMappings, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsBlockDeviceMappingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster_name": "clusterName",
        "name": "name",
        "region": "region",
        "security_group_ids": "securityGroupIds",
        "subnet_ids": "subnetIds",
        "associate_public_ip_address": "associatePublicIpAddress",
        "autoscaler": "autoscaler",
        "block_device_mappings": "blockDeviceMappings",
        "desired_capacity": "desiredCapacity",
        "draining_timeout": "drainingTimeout",
        "ebs_optimized": "ebsOptimized",
        "iam_instance_profile": "iamInstanceProfile",
        "id": "id",
        "image_id": "imageId",
        "instance_metadata_options": "instanceMetadataOptions",
        "key_pair": "keyPair",
        "logging": "logging",
        "max_size": "maxSize",
        "min_size": "minSize",
        "monitoring": "monitoring",
        "optimize_images": "optimizeImages",
        "scheduled_task": "scheduledTask",
        "spot_percentage": "spotPercentage",
        "tags": "tags",
        "update_policy": "updatePolicy",
        "use_as_template_only": "useAsTemplateOnly",
        "user_data": "userData",
        "utilize_commitments": "utilizeCommitments",
        "utilize_reserved_instances": "utilizeReservedInstances",
        "whitelist": "whitelist",
    },
)
class OceanEcsConfig(cdktf.TerraformMetaArguments):
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
        cluster_name: builtins.str,
        name: builtins.str,
        region: builtins.str,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
        associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        autoscaler: typing.Optional[typing.Union[OceanEcsAutoscaler, typing.Dict[str, typing.Any]]] = None,
        block_device_mappings: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OceanEcsBlockDeviceMappings, typing.Dict[str, typing.Any]]]]] = None,
        desired_capacity: typing.Optional[jsii.Number] = None,
        draining_timeout: typing.Optional[jsii.Number] = None,
        ebs_optimized: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        iam_instance_profile: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        image_id: typing.Optional[builtins.str] = None,
        instance_metadata_options: typing.Optional[typing.Union["OceanEcsInstanceMetadataOptions", typing.Dict[str, typing.Any]]] = None,
        key_pair: typing.Optional[builtins.str] = None,
        logging: typing.Optional[typing.Union["OceanEcsLogging", typing.Dict[str, typing.Any]]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        optimize_images: typing.Optional[typing.Union["OceanEcsOptimizeImages", typing.Dict[str, typing.Any]]] = None,
        scheduled_task: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsScheduledTask", typing.Dict[str, typing.Any]]]]] = None,
        spot_percentage: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsTags", typing.Dict[str, typing.Any]]]]] = None,
        update_policy: typing.Optional[typing.Union["OceanEcsUpdatePolicy", typing.Dict[str, typing.Any]]] = None,
        use_as_template_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        user_data: typing.Optional[builtins.str] = None,
        utilize_commitments: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        utilize_reserved_instances: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#cluster_name OceanEcs#cluster_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#name OceanEcs#name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#region OceanEcs#region}.
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#security_group_ids OceanEcs#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#subnet_ids OceanEcs#subnet_ids}.
        :param associate_public_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#associate_public_ip_address OceanEcs#associate_public_ip_address}.
        :param autoscaler: autoscaler block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#autoscaler OceanEcs#autoscaler}
        :param block_device_mappings: block_device_mappings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#block_device_mappings OceanEcs#block_device_mappings}
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#desired_capacity OceanEcs#desired_capacity}.
        :param draining_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#draining_timeout OceanEcs#draining_timeout}.
        :param ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#ebs_optimized OceanEcs#ebs_optimized}.
        :param iam_instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#iam_instance_profile OceanEcs#iam_instance_profile}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#id OceanEcs#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#image_id OceanEcs#image_id}.
        :param instance_metadata_options: instance_metadata_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#instance_metadata_options OceanEcs#instance_metadata_options}
        :param key_pair: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#key_pair OceanEcs#key_pair}.
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#logging OceanEcs#logging}
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#max_size OceanEcs#max_size}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#min_size OceanEcs#min_size}.
        :param monitoring: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#monitoring OceanEcs#monitoring}.
        :param optimize_images: optimize_images block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#optimize_images OceanEcs#optimize_images}
        :param scheduled_task: scheduled_task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#scheduled_task OceanEcs#scheduled_task}
        :param spot_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#spot_percentage OceanEcs#spot_percentage}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#tags OceanEcs#tags}
        :param update_policy: update_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#update_policy OceanEcs#update_policy}
        :param use_as_template_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#use_as_template_only OceanEcs#use_as_template_only}.
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#user_data OceanEcs#user_data}.
        :param utilize_commitments: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#utilize_commitments OceanEcs#utilize_commitments}.
        :param utilize_reserved_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#utilize_reserved_instances OceanEcs#utilize_reserved_instances}.
        :param whitelist: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#whitelist OceanEcs#whitelist}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(autoscaler, dict):
            autoscaler = OceanEcsAutoscaler(**autoscaler)
        if isinstance(instance_metadata_options, dict):
            instance_metadata_options = OceanEcsInstanceMetadataOptions(**instance_metadata_options)
        if isinstance(logging, dict):
            logging = OceanEcsLogging(**logging)
        if isinstance(optimize_images, dict):
            optimize_images = OceanEcsOptimizeImages(**optimize_images)
        if isinstance(update_policy, dict):
            update_policy = OceanEcsUpdatePolicy(**update_policy)
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument associate_public_ip_address", value=associate_public_ip_address, expected_type=type_hints["associate_public_ip_address"])
            check_type(argname="argument autoscaler", value=autoscaler, expected_type=type_hints["autoscaler"])
            check_type(argname="argument block_device_mappings", value=block_device_mappings, expected_type=type_hints["block_device_mappings"])
            check_type(argname="argument desired_capacity", value=desired_capacity, expected_type=type_hints["desired_capacity"])
            check_type(argname="argument draining_timeout", value=draining_timeout, expected_type=type_hints["draining_timeout"])
            check_type(argname="argument ebs_optimized", value=ebs_optimized, expected_type=type_hints["ebs_optimized"])
            check_type(argname="argument iam_instance_profile", value=iam_instance_profile, expected_type=type_hints["iam_instance_profile"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument image_id", value=image_id, expected_type=type_hints["image_id"])
            check_type(argname="argument instance_metadata_options", value=instance_metadata_options, expected_type=type_hints["instance_metadata_options"])
            check_type(argname="argument key_pair", value=key_pair, expected_type=type_hints["key_pair"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
            check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            check_type(argname="argument monitoring", value=monitoring, expected_type=type_hints["monitoring"])
            check_type(argname="argument optimize_images", value=optimize_images, expected_type=type_hints["optimize_images"])
            check_type(argname="argument scheduled_task", value=scheduled_task, expected_type=type_hints["scheduled_task"])
            check_type(argname="argument spot_percentage", value=spot_percentage, expected_type=type_hints["spot_percentage"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument update_policy", value=update_policy, expected_type=type_hints["update_policy"])
            check_type(argname="argument use_as_template_only", value=use_as_template_only, expected_type=type_hints["use_as_template_only"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
            check_type(argname="argument utilize_commitments", value=utilize_commitments, expected_type=type_hints["utilize_commitments"])
            check_type(argname="argument utilize_reserved_instances", value=utilize_reserved_instances, expected_type=type_hints["utilize_reserved_instances"])
            check_type(argname="argument whitelist", value=whitelist, expected_type=type_hints["whitelist"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_name": cluster_name,
            "name": name,
            "region": region,
            "security_group_ids": security_group_ids,
            "subnet_ids": subnet_ids,
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
        if associate_public_ip_address is not None:
            self._values["associate_public_ip_address"] = associate_public_ip_address
        if autoscaler is not None:
            self._values["autoscaler"] = autoscaler
        if block_device_mappings is not None:
            self._values["block_device_mappings"] = block_device_mappings
        if desired_capacity is not None:
            self._values["desired_capacity"] = desired_capacity
        if draining_timeout is not None:
            self._values["draining_timeout"] = draining_timeout
        if ebs_optimized is not None:
            self._values["ebs_optimized"] = ebs_optimized
        if iam_instance_profile is not None:
            self._values["iam_instance_profile"] = iam_instance_profile
        if id is not None:
            self._values["id"] = id
        if image_id is not None:
            self._values["image_id"] = image_id
        if instance_metadata_options is not None:
            self._values["instance_metadata_options"] = instance_metadata_options
        if key_pair is not None:
            self._values["key_pair"] = key_pair
        if logging is not None:
            self._values["logging"] = logging
        if max_size is not None:
            self._values["max_size"] = max_size
        if min_size is not None:
            self._values["min_size"] = min_size
        if monitoring is not None:
            self._values["monitoring"] = monitoring
        if optimize_images is not None:
            self._values["optimize_images"] = optimize_images
        if scheduled_task is not None:
            self._values["scheduled_task"] = scheduled_task
        if spot_percentage is not None:
            self._values["spot_percentage"] = spot_percentage
        if tags is not None:
            self._values["tags"] = tags
        if update_policy is not None:
            self._values["update_policy"] = update_policy
        if use_as_template_only is not None:
            self._values["use_as_template_only"] = use_as_template_only
        if user_data is not None:
            self._values["user_data"] = user_data
        if utilize_commitments is not None:
            self._values["utilize_commitments"] = utilize_commitments
        if utilize_reserved_instances is not None:
            self._values["utilize_reserved_instances"] = utilize_reserved_instances
        if whitelist is not None:
            self._values["whitelist"] = whitelist

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
    def cluster_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#cluster_name OceanEcs#cluster_name}.'''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#name OceanEcs#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#region OceanEcs#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#security_group_ids OceanEcs#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#subnet_ids OceanEcs#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def associate_public_ip_address(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#associate_public_ip_address OceanEcs#associate_public_ip_address}.'''
        result = self._values.get("associate_public_ip_address")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def autoscaler(self) -> typing.Optional[OceanEcsAutoscaler]:
        '''autoscaler block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#autoscaler OceanEcs#autoscaler}
        '''
        result = self._values.get("autoscaler")
        return typing.cast(typing.Optional[OceanEcsAutoscaler], result)

    @builtins.property
    def block_device_mappings(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsBlockDeviceMappings]]]:
        '''block_device_mappings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#block_device_mappings OceanEcs#block_device_mappings}
        '''
        result = self._values.get("block_device_mappings")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsBlockDeviceMappings]]], result)

    @builtins.property
    def desired_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#desired_capacity OceanEcs#desired_capacity}.'''
        result = self._values.get("desired_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def draining_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#draining_timeout OceanEcs#draining_timeout}.'''
        result = self._values.get("draining_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ebs_optimized(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#ebs_optimized OceanEcs#ebs_optimized}.'''
        result = self._values.get("ebs_optimized")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def iam_instance_profile(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#iam_instance_profile OceanEcs#iam_instance_profile}.'''
        result = self._values.get("iam_instance_profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#id OceanEcs#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#image_id OceanEcs#image_id}.'''
        result = self._values.get("image_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_metadata_options(
        self,
    ) -> typing.Optional["OceanEcsInstanceMetadataOptions"]:
        '''instance_metadata_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#instance_metadata_options OceanEcs#instance_metadata_options}
        '''
        result = self._values.get("instance_metadata_options")
        return typing.cast(typing.Optional["OceanEcsInstanceMetadataOptions"], result)

    @builtins.property
    def key_pair(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#key_pair OceanEcs#key_pair}.'''
        result = self._values.get("key_pair")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging(self) -> typing.Optional["OceanEcsLogging"]:
        '''logging block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#logging OceanEcs#logging}
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional["OceanEcsLogging"], result)

    @builtins.property
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#max_size OceanEcs#max_size}.'''
        result = self._values.get("max_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#min_size OceanEcs#min_size}.'''
        result = self._values.get("min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def monitoring(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#monitoring OceanEcs#monitoring}.'''
        result = self._values.get("monitoring")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def optimize_images(self) -> typing.Optional["OceanEcsOptimizeImages"]:
        '''optimize_images block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#optimize_images OceanEcs#optimize_images}
        '''
        result = self._values.get("optimize_images")
        return typing.cast(typing.Optional["OceanEcsOptimizeImages"], result)

    @builtins.property
    def scheduled_task(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsScheduledTask"]]]:
        '''scheduled_task block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#scheduled_task OceanEcs#scheduled_task}
        '''
        result = self._values.get("scheduled_task")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsScheduledTask"]]], result)

    @builtins.property
    def spot_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#spot_percentage OceanEcs#spot_percentage}.'''
        result = self._values.get("spot_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsTags"]]]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#tags OceanEcs#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsTags"]]], result)

    @builtins.property
    def update_policy(self) -> typing.Optional["OceanEcsUpdatePolicy"]:
        '''update_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#update_policy OceanEcs#update_policy}
        '''
        result = self._values.get("update_policy")
        return typing.cast(typing.Optional["OceanEcsUpdatePolicy"], result)

    @builtins.property
    def use_as_template_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#use_as_template_only OceanEcs#use_as_template_only}.'''
        result = self._values.get("use_as_template_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#user_data OceanEcs#user_data}.'''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def utilize_commitments(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#utilize_commitments OceanEcs#utilize_commitments}.'''
        result = self._values.get("utilize_commitments")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def utilize_reserved_instances(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#utilize_reserved_instances OceanEcs#utilize_reserved_instances}.'''
        result = self._values.get("utilize_reserved_instances")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def whitelist(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#whitelist OceanEcs#whitelist}.'''
        result = self._values.get("whitelist")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsInstanceMetadataOptions",
    jsii_struct_bases=[],
    name_mapping={
        "http_tokens": "httpTokens",
        "http_put_response_hop_limit": "httpPutResponseHopLimit",
    },
)
class OceanEcsInstanceMetadataOptions:
    def __init__(
        self,
        *,
        http_tokens: builtins.str,
        http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param http_tokens: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#http_tokens OceanEcs#http_tokens}.
        :param http_put_response_hop_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#http_put_response_hop_limit OceanEcs#http_put_response_hop_limit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsInstanceMetadataOptions.__init__)
            check_type(argname="argument http_tokens", value=http_tokens, expected_type=type_hints["http_tokens"])
            check_type(argname="argument http_put_response_hop_limit", value=http_put_response_hop_limit, expected_type=type_hints["http_put_response_hop_limit"])
        self._values: typing.Dict[str, typing.Any] = {
            "http_tokens": http_tokens,
        }
        if http_put_response_hop_limit is not None:
            self._values["http_put_response_hop_limit"] = http_put_response_hop_limit

    @builtins.property
    def http_tokens(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#http_tokens OceanEcs#http_tokens}.'''
        result = self._values.get("http_tokens")
        assert result is not None, "Required property 'http_tokens' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def http_put_response_hop_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#http_put_response_hop_limit OceanEcs#http_put_response_hop_limit}.'''
        result = self._values.get("http_put_response_hop_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsInstanceMetadataOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsInstanceMetadataOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsInstanceMetadataOptionsOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsInstanceMetadataOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHttpPutResponseHopLimit")
    def reset_http_put_response_hop_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpPutResponseHopLimit", []))

    @builtins.property
    @jsii.member(jsii_name="httpPutResponseHopLimitInput")
    def http_put_response_hop_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpPutResponseHopLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="httpTokensInput")
    def http_tokens_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpTokensInput"))

    @builtins.property
    @jsii.member(jsii_name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpPutResponseHopLimit"))

    @http_put_response_hop_limit.setter
    def http_put_response_hop_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsInstanceMetadataOptionsOutputReference, "http_put_response_hop_limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpPutResponseHopLimit", value)

    @builtins.property
    @jsii.member(jsii_name="httpTokens")
    def http_tokens(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpTokens"))

    @http_tokens.setter
    def http_tokens(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsInstanceMetadataOptionsOutputReference, "http_tokens").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpTokens", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanEcsInstanceMetadataOptions]:
        return typing.cast(typing.Optional[OceanEcsInstanceMetadataOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanEcsInstanceMetadataOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsInstanceMetadataOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsLogging",
    jsii_struct_bases=[],
    name_mapping={"export": "export"},
)
class OceanEcsLogging:
    def __init__(
        self,
        *,
        export: typing.Optional[typing.Union["OceanEcsLoggingExport", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param export: export block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#export OceanEcs#export}
        '''
        if isinstance(export, dict):
            export = OceanEcsLoggingExport(**export)
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLogging.__init__)
            check_type(argname="argument export", value=export, expected_type=type_hints["export"])
        self._values: typing.Dict[str, typing.Any] = {}
        if export is not None:
            self._values["export"] = export

    @builtins.property
    def export(self) -> typing.Optional["OceanEcsLoggingExport"]:
        '''export block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#export OceanEcs#export}
        '''
        result = self._values.get("export")
        return typing.cast(typing.Optional["OceanEcsLoggingExport"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsLogging(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsLoggingExport",
    jsii_struct_bases=[],
    name_mapping={"s3": "s3"},
)
class OceanEcsLoggingExport:
    def __init__(
        self,
        *,
        s3: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsLoggingExportS3", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#s3 OceanEcs#s3}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLoggingExport.__init__)
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
        self._values: typing.Dict[str, typing.Any] = {}
        if s3 is not None:
            self._values["s3"] = s3

    @builtins.property
    def s3(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLoggingExportS3"]]]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#s3 OceanEcs#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLoggingExportS3"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsLoggingExport(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsLoggingExportOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsLoggingExportOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsLoggingExportOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsLoggingExportS3", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLoggingExportOutputReference.put_s3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "OceanEcsLoggingExportS3List":
        return typing.cast("OceanEcsLoggingExportS3List", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLoggingExportS3"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLoggingExportS3"]]], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanEcsLoggingExport]:
        return typing.cast(typing.Optional[OceanEcsLoggingExport], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OceanEcsLoggingExport]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLoggingExportOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsLoggingExportS3",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class OceanEcsLoggingExportS3:
    def __init__(self, *, id: builtins.str) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#id OceanEcs#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLoggingExportS3.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#id OceanEcs#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsLoggingExportS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsLoggingExportS3List(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsLoggingExportS3List",
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
            type_hints = typing.get_type_hints(OceanEcsLoggingExportS3List.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanEcsLoggingExportS3OutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLoggingExportS3List.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanEcsLoggingExportS3OutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLoggingExportS3List, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsLoggingExportS3List, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsLoggingExportS3List, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLoggingExportS3]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLoggingExportS3]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLoggingExportS3]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLoggingExportS3List, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanEcsLoggingExportS3OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsLoggingExportS3OutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsLoggingExportS3OutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLoggingExportS3OutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanEcsLoggingExportS3, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanEcsLoggingExportS3, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanEcsLoggingExportS3, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLoggingExportS3OutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanEcsLoggingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsLoggingOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsLoggingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putExport")
    def put_export(
        self,
        *,
        s3: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OceanEcsLoggingExportS3, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#s3 OceanEcs#s3}
        '''
        value = OceanEcsLoggingExport(s3=s3)

        return typing.cast(None, jsii.invoke(self, "putExport", [value]))

    @jsii.member(jsii_name="resetExport")
    def reset_export(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExport", []))

    @builtins.property
    @jsii.member(jsii_name="export")
    def export(self) -> OceanEcsLoggingExportOutputReference:
        return typing.cast(OceanEcsLoggingExportOutputReference, jsii.get(self, "export"))

    @builtins.property
    @jsii.member(jsii_name="exportInput")
    def export_input(self) -> typing.Optional[OceanEcsLoggingExport]:
        return typing.cast(typing.Optional[OceanEcsLoggingExport], jsii.get(self, "exportInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanEcsLogging]:
        return typing.cast(typing.Optional[OceanEcsLogging], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OceanEcsLogging]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLoggingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsOptimizeImages",
    jsii_struct_bases=[],
    name_mapping={
        "perform_at": "performAt",
        "should_optimize_ecs_ami": "shouldOptimizeEcsAmi",
        "time_windows": "timeWindows",
    },
)
class OceanEcsOptimizeImages:
    def __init__(
        self,
        *,
        perform_at: builtins.str,
        should_optimize_ecs_ami: typing.Union[builtins.bool, cdktf.IResolvable],
        time_windows: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param perform_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#perform_at OceanEcs#perform_at}.
        :param should_optimize_ecs_ami: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#should_optimize_ecs_ami OceanEcs#should_optimize_ecs_ami}.
        :param time_windows: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#time_windows OceanEcs#time_windows}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsOptimizeImages.__init__)
            check_type(argname="argument perform_at", value=perform_at, expected_type=type_hints["perform_at"])
            check_type(argname="argument should_optimize_ecs_ami", value=should_optimize_ecs_ami, expected_type=type_hints["should_optimize_ecs_ami"])
            check_type(argname="argument time_windows", value=time_windows, expected_type=type_hints["time_windows"])
        self._values: typing.Dict[str, typing.Any] = {
            "perform_at": perform_at,
            "should_optimize_ecs_ami": should_optimize_ecs_ami,
        }
        if time_windows is not None:
            self._values["time_windows"] = time_windows

    @builtins.property
    def perform_at(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#perform_at OceanEcs#perform_at}.'''
        result = self._values.get("perform_at")
        assert result is not None, "Required property 'perform_at' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def should_optimize_ecs_ami(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#should_optimize_ecs_ami OceanEcs#should_optimize_ecs_ami}.'''
        result = self._values.get("should_optimize_ecs_ami")
        assert result is not None, "Required property 'should_optimize_ecs_ami' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def time_windows(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#time_windows OceanEcs#time_windows}.'''
        result = self._values.get("time_windows")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsOptimizeImages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsOptimizeImagesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsOptimizeImagesOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsOptimizeImagesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTimeWindows")
    def reset_time_windows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeWindows", []))

    @builtins.property
    @jsii.member(jsii_name="performAtInput")
    def perform_at_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "performAtInput"))

    @builtins.property
    @jsii.member(jsii_name="shouldOptimizeEcsAmiInput")
    def should_optimize_ecs_ami_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "shouldOptimizeEcsAmiInput"))

    @builtins.property
    @jsii.member(jsii_name="timeWindowsInput")
    def time_windows_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "timeWindowsInput"))

    @builtins.property
    @jsii.member(jsii_name="performAt")
    def perform_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "performAt"))

    @perform_at.setter
    def perform_at(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsOptimizeImagesOutputReference, "perform_at").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "performAt", value)

    @builtins.property
    @jsii.member(jsii_name="shouldOptimizeEcsAmi")
    def should_optimize_ecs_ami(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "shouldOptimizeEcsAmi"))

    @should_optimize_ecs_ami.setter
    def should_optimize_ecs_ami(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsOptimizeImagesOutputReference, "should_optimize_ecs_ami").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shouldOptimizeEcsAmi", value)

    @builtins.property
    @jsii.member(jsii_name="timeWindows")
    def time_windows(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "timeWindows"))

    @time_windows.setter
    def time_windows(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsOptimizeImagesOutputReference, "time_windows").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeWindows", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanEcsOptimizeImages]:
        return typing.cast(typing.Optional[OceanEcsOptimizeImages], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OceanEcsOptimizeImages]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsOptimizeImagesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsScheduledTask",
    jsii_struct_bases=[],
    name_mapping={"shutdown_hours": "shutdownHours", "tasks": "tasks"},
)
class OceanEcsScheduledTask:
    def __init__(
        self,
        *,
        shutdown_hours: typing.Optional[typing.Union["OceanEcsScheduledTaskShutdownHours", typing.Dict[str, typing.Any]]] = None,
        tasks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsScheduledTaskTasks", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param shutdown_hours: shutdown_hours block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#shutdown_hours OceanEcs#shutdown_hours}
        :param tasks: tasks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#tasks OceanEcs#tasks}
        '''
        if isinstance(shutdown_hours, dict):
            shutdown_hours = OceanEcsScheduledTaskShutdownHours(**shutdown_hours)
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsScheduledTask.__init__)
            check_type(argname="argument shutdown_hours", value=shutdown_hours, expected_type=type_hints["shutdown_hours"])
            check_type(argname="argument tasks", value=tasks, expected_type=type_hints["tasks"])
        self._values: typing.Dict[str, typing.Any] = {}
        if shutdown_hours is not None:
            self._values["shutdown_hours"] = shutdown_hours
        if tasks is not None:
            self._values["tasks"] = tasks

    @builtins.property
    def shutdown_hours(self) -> typing.Optional["OceanEcsScheduledTaskShutdownHours"]:
        '''shutdown_hours block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#shutdown_hours OceanEcs#shutdown_hours}
        '''
        result = self._values.get("shutdown_hours")
        return typing.cast(typing.Optional["OceanEcsScheduledTaskShutdownHours"], result)

    @builtins.property
    def tasks(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsScheduledTaskTasks"]]]:
        '''tasks block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#tasks OceanEcs#tasks}
        '''
        result = self._values.get("tasks")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsScheduledTaskTasks"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsScheduledTask(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsScheduledTaskList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsScheduledTaskList",
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
            type_hints = typing.get_type_hints(OceanEcsScheduledTaskList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanEcsScheduledTaskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsScheduledTaskList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanEcsScheduledTaskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsScheduledTaskList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsScheduledTaskList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsScheduledTaskList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsScheduledTask]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsScheduledTask]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsScheduledTask]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsScheduledTaskList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanEcsScheduledTaskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsScheduledTaskOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsScheduledTaskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putShutdownHours")
    def put_shutdown_hours(
        self,
        *,
        time_windows: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param time_windows: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#time_windows OceanEcs#time_windows}.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#is_enabled OceanEcs#is_enabled}.
        '''
        value = OceanEcsScheduledTaskShutdownHours(
            time_windows=time_windows, is_enabled=is_enabled
        )

        return typing.cast(None, jsii.invoke(self, "putShutdownHours", [value]))

    @jsii.member(jsii_name="putTasks")
    def put_tasks(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsScheduledTaskTasks", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsScheduledTaskOutputReference.put_tasks)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTasks", [value]))

    @jsii.member(jsii_name="resetShutdownHours")
    def reset_shutdown_hours(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShutdownHours", []))

    @jsii.member(jsii_name="resetTasks")
    def reset_tasks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTasks", []))

    @builtins.property
    @jsii.member(jsii_name="shutdownHours")
    def shutdown_hours(self) -> "OceanEcsScheduledTaskShutdownHoursOutputReference":
        return typing.cast("OceanEcsScheduledTaskShutdownHoursOutputReference", jsii.get(self, "shutdownHours"))

    @builtins.property
    @jsii.member(jsii_name="tasks")
    def tasks(self) -> "OceanEcsScheduledTaskTasksList":
        return typing.cast("OceanEcsScheduledTaskTasksList", jsii.get(self, "tasks"))

    @builtins.property
    @jsii.member(jsii_name="shutdownHoursInput")
    def shutdown_hours_input(
        self,
    ) -> typing.Optional["OceanEcsScheduledTaskShutdownHours"]:
        return typing.cast(typing.Optional["OceanEcsScheduledTaskShutdownHours"], jsii.get(self, "shutdownHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="tasksInput")
    def tasks_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsScheduledTaskTasks"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsScheduledTaskTasks"]]], jsii.get(self, "tasksInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanEcsScheduledTask, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanEcsScheduledTask, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanEcsScheduledTask, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsScheduledTaskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsScheduledTaskShutdownHours",
    jsii_struct_bases=[],
    name_mapping={"time_windows": "timeWindows", "is_enabled": "isEnabled"},
)
class OceanEcsScheduledTaskShutdownHours:
    def __init__(
        self,
        *,
        time_windows: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param time_windows: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#time_windows OceanEcs#time_windows}.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#is_enabled OceanEcs#is_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsScheduledTaskShutdownHours.__init__)
            check_type(argname="argument time_windows", value=time_windows, expected_type=type_hints["time_windows"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "time_windows": time_windows,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled

    @builtins.property
    def time_windows(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#time_windows OceanEcs#time_windows}.'''
        result = self._values.get("time_windows")
        assert result is not None, "Required property 'time_windows' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#is_enabled OceanEcs#is_enabled}.'''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsScheduledTaskShutdownHours(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsScheduledTaskShutdownHoursOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsScheduledTaskShutdownHoursOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsScheduledTaskShutdownHoursOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="timeWindowsInput")
    def time_windows_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "timeWindowsInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsScheduledTaskShutdownHoursOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="timeWindows")
    def time_windows(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "timeWindows"))

    @time_windows.setter
    def time_windows(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsScheduledTaskShutdownHoursOutputReference, "time_windows").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeWindows", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanEcsScheduledTaskShutdownHours]:
        return typing.cast(typing.Optional[OceanEcsScheduledTaskShutdownHours], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanEcsScheduledTaskShutdownHours],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsScheduledTaskShutdownHoursOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsScheduledTaskTasks",
    jsii_struct_bases=[],
    name_mapping={
        "cron_expression": "cronExpression",
        "is_enabled": "isEnabled",
        "task_type": "taskType",
    },
)
class OceanEcsScheduledTaskTasks:
    def __init__(
        self,
        *,
        cron_expression: builtins.str,
        is_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        task_type: builtins.str,
    ) -> None:
        '''
        :param cron_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#cron_expression OceanEcs#cron_expression}.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#is_enabled OceanEcs#is_enabled}.
        :param task_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#task_type OceanEcs#task_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsScheduledTaskTasks.__init__)
            check_type(argname="argument cron_expression", value=cron_expression, expected_type=type_hints["cron_expression"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument task_type", value=task_type, expected_type=type_hints["task_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "cron_expression": cron_expression,
            "is_enabled": is_enabled,
            "task_type": task_type,
        }

    @builtins.property
    def cron_expression(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#cron_expression OceanEcs#cron_expression}.'''
        result = self._values.get("cron_expression")
        assert result is not None, "Required property 'cron_expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#is_enabled OceanEcs#is_enabled}.'''
        result = self._values.get("is_enabled")
        assert result is not None, "Required property 'is_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def task_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#task_type OceanEcs#task_type}.'''
        result = self._values.get("task_type")
        assert result is not None, "Required property 'task_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsScheduledTaskTasks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsScheduledTaskTasksList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsScheduledTaskTasksList",
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
            type_hints = typing.get_type_hints(OceanEcsScheduledTaskTasksList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanEcsScheduledTaskTasksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsScheduledTaskTasksList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanEcsScheduledTaskTasksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsScheduledTaskTasksList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsScheduledTaskTasksList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsScheduledTaskTasksList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsScheduledTaskTasks]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsScheduledTaskTasks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsScheduledTaskTasks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsScheduledTaskTasksList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanEcsScheduledTaskTasksOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsScheduledTaskTasksOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsScheduledTaskTasksOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(getattr(OceanEcsScheduledTaskTasksOutputReference, "cron_expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cronExpression", value)

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsScheduledTaskTasksOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="taskType")
    def task_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskType"))

    @task_type.setter
    def task_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsScheduledTaskTasksOutputReference, "task_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanEcsScheduledTaskTasks, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanEcsScheduledTaskTasks, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanEcsScheduledTaskTasks, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsScheduledTaskTasksOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class OceanEcsTags:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#key OceanEcs#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#value OceanEcs#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsTags.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#key OceanEcs#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#value OceanEcs#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsTagsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsTagsList",
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
            type_hints = typing.get_type_hints(OceanEcsTagsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanEcsTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsTagsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanEcsTagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsTagsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsTagsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsTagsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsTags]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsTags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsTagsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanEcsTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsTagsOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsTagsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsTagsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsTagsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanEcsTags, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanEcsTags, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanEcsTags, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsTagsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsUpdatePolicy",
    jsii_struct_bases=[],
    name_mapping={
        "should_roll": "shouldRoll",
        "auto_apply_tags": "autoApplyTags",
        "conditioned_roll": "conditionedRoll",
        "roll_config": "rollConfig",
    },
)
class OceanEcsUpdatePolicy:
    def __init__(
        self,
        *,
        should_roll: typing.Union[builtins.bool, cdktf.IResolvable],
        auto_apply_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        conditioned_roll: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        roll_config: typing.Optional[typing.Union["OceanEcsUpdatePolicyRollConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param should_roll: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#should_roll OceanEcs#should_roll}.
        :param auto_apply_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#auto_apply_tags OceanEcs#auto_apply_tags}.
        :param conditioned_roll: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#conditioned_roll OceanEcs#conditioned_roll}.
        :param roll_config: roll_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#roll_config OceanEcs#roll_config}
        '''
        if isinstance(roll_config, dict):
            roll_config = OceanEcsUpdatePolicyRollConfig(**roll_config)
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsUpdatePolicy.__init__)
            check_type(argname="argument should_roll", value=should_roll, expected_type=type_hints["should_roll"])
            check_type(argname="argument auto_apply_tags", value=auto_apply_tags, expected_type=type_hints["auto_apply_tags"])
            check_type(argname="argument conditioned_roll", value=conditioned_roll, expected_type=type_hints["conditioned_roll"])
            check_type(argname="argument roll_config", value=roll_config, expected_type=type_hints["roll_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "should_roll": should_roll,
        }
        if auto_apply_tags is not None:
            self._values["auto_apply_tags"] = auto_apply_tags
        if conditioned_roll is not None:
            self._values["conditioned_roll"] = conditioned_roll
        if roll_config is not None:
            self._values["roll_config"] = roll_config

    @builtins.property
    def should_roll(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#should_roll OceanEcs#should_roll}.'''
        result = self._values.get("should_roll")
        assert result is not None, "Required property 'should_roll' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def auto_apply_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#auto_apply_tags OceanEcs#auto_apply_tags}.'''
        result = self._values.get("auto_apply_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def conditioned_roll(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#conditioned_roll OceanEcs#conditioned_roll}.'''
        result = self._values.get("conditioned_roll")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def roll_config(self) -> typing.Optional["OceanEcsUpdatePolicyRollConfig"]:
        '''roll_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#roll_config OceanEcs#roll_config}
        '''
        result = self._values.get("roll_config")
        return typing.cast(typing.Optional["OceanEcsUpdatePolicyRollConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsUpdatePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsUpdatePolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsUpdatePolicyOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsUpdatePolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRollConfig")
    def put_roll_config(
        self,
        *,
        batch_size_percentage: jsii.Number,
        batch_min_healthy_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param batch_size_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#batch_size_percentage OceanEcs#batch_size_percentage}.
        :param batch_min_healthy_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#batch_min_healthy_percentage OceanEcs#batch_min_healthy_percentage}.
        '''
        value = OceanEcsUpdatePolicyRollConfig(
            batch_size_percentage=batch_size_percentage,
            batch_min_healthy_percentage=batch_min_healthy_percentage,
        )

        return typing.cast(None, jsii.invoke(self, "putRollConfig", [value]))

    @jsii.member(jsii_name="resetAutoApplyTags")
    def reset_auto_apply_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoApplyTags", []))

    @jsii.member(jsii_name="resetConditionedRoll")
    def reset_conditioned_roll(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionedRoll", []))

    @jsii.member(jsii_name="resetRollConfig")
    def reset_roll_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRollConfig", []))

    @builtins.property
    @jsii.member(jsii_name="rollConfig")
    def roll_config(self) -> "OceanEcsUpdatePolicyRollConfigOutputReference":
        return typing.cast("OceanEcsUpdatePolicyRollConfigOutputReference", jsii.get(self, "rollConfig"))

    @builtins.property
    @jsii.member(jsii_name="autoApplyTagsInput")
    def auto_apply_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoApplyTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionedRollInput")
    def conditioned_roll_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "conditionedRollInput"))

    @builtins.property
    @jsii.member(jsii_name="rollConfigInput")
    def roll_config_input(self) -> typing.Optional["OceanEcsUpdatePolicyRollConfig"]:
        return typing.cast(typing.Optional["OceanEcsUpdatePolicyRollConfig"], jsii.get(self, "rollConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="shouldRollInput")
    def should_roll_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "shouldRollInput"))

    @builtins.property
    @jsii.member(jsii_name="autoApplyTags")
    def auto_apply_tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoApplyTags"))

    @auto_apply_tags.setter
    def auto_apply_tags(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsUpdatePolicyOutputReference, "auto_apply_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoApplyTags", value)

    @builtins.property
    @jsii.member(jsii_name="conditionedRoll")
    def conditioned_roll(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "conditionedRoll"))

    @conditioned_roll.setter
    def conditioned_roll(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsUpdatePolicyOutputReference, "conditioned_roll").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conditionedRoll", value)

    @builtins.property
    @jsii.member(jsii_name="shouldRoll")
    def should_roll(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "shouldRoll"))

    @should_roll.setter
    def should_roll(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsUpdatePolicyOutputReference, "should_roll").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shouldRoll", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanEcsUpdatePolicy]:
        return typing.cast(typing.Optional[OceanEcsUpdatePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OceanEcsUpdatePolicy]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsUpdatePolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsUpdatePolicyRollConfig",
    jsii_struct_bases=[],
    name_mapping={
        "batch_size_percentage": "batchSizePercentage",
        "batch_min_healthy_percentage": "batchMinHealthyPercentage",
    },
)
class OceanEcsUpdatePolicyRollConfig:
    def __init__(
        self,
        *,
        batch_size_percentage: jsii.Number,
        batch_min_healthy_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param batch_size_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#batch_size_percentage OceanEcs#batch_size_percentage}.
        :param batch_min_healthy_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#batch_min_healthy_percentage OceanEcs#batch_min_healthy_percentage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsUpdatePolicyRollConfig.__init__)
            check_type(argname="argument batch_size_percentage", value=batch_size_percentage, expected_type=type_hints["batch_size_percentage"])
            check_type(argname="argument batch_min_healthy_percentage", value=batch_min_healthy_percentage, expected_type=type_hints["batch_min_healthy_percentage"])
        self._values: typing.Dict[str, typing.Any] = {
            "batch_size_percentage": batch_size_percentage,
        }
        if batch_min_healthy_percentage is not None:
            self._values["batch_min_healthy_percentage"] = batch_min_healthy_percentage

    @builtins.property
    def batch_size_percentage(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#batch_size_percentage OceanEcs#batch_size_percentage}.'''
        result = self._values.get("batch_size_percentage")
        assert result is not None, "Required property 'batch_size_percentage' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def batch_min_healthy_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs#batch_min_healthy_percentage OceanEcs#batch_min_healthy_percentage}.'''
        result = self._values.get("batch_min_healthy_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsUpdatePolicyRollConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsUpdatePolicyRollConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcs.OceanEcsUpdatePolicyRollConfigOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsUpdatePolicyRollConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBatchMinHealthyPercentage")
    def reset_batch_min_healthy_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBatchMinHealthyPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="batchMinHealthyPercentageInput")
    def batch_min_healthy_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "batchMinHealthyPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="batchSizePercentageInput")
    def batch_size_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "batchSizePercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="batchMinHealthyPercentage")
    def batch_min_healthy_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "batchMinHealthyPercentage"))

    @batch_min_healthy_percentage.setter
    def batch_min_healthy_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsUpdatePolicyRollConfigOutputReference, "batch_min_healthy_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchMinHealthyPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="batchSizePercentage")
    def batch_size_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "batchSizePercentage"))

    @batch_size_percentage.setter
    def batch_size_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsUpdatePolicyRollConfigOutputReference, "batch_size_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchSizePercentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanEcsUpdatePolicyRollConfig]:
        return typing.cast(typing.Optional[OceanEcsUpdatePolicyRollConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanEcsUpdatePolicyRollConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsUpdatePolicyRollConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "OceanEcs",
    "OceanEcsAutoscaler",
    "OceanEcsAutoscalerDown",
    "OceanEcsAutoscalerDownOutputReference",
    "OceanEcsAutoscalerHeadroom",
    "OceanEcsAutoscalerHeadroomOutputReference",
    "OceanEcsAutoscalerOutputReference",
    "OceanEcsAutoscalerResourceLimits",
    "OceanEcsAutoscalerResourceLimitsOutputReference",
    "OceanEcsBlockDeviceMappings",
    "OceanEcsBlockDeviceMappingsEbs",
    "OceanEcsBlockDeviceMappingsEbsDynamicVolumeSize",
    "OceanEcsBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference",
    "OceanEcsBlockDeviceMappingsEbsOutputReference",
    "OceanEcsBlockDeviceMappingsList",
    "OceanEcsBlockDeviceMappingsOutputReference",
    "OceanEcsConfig",
    "OceanEcsInstanceMetadataOptions",
    "OceanEcsInstanceMetadataOptionsOutputReference",
    "OceanEcsLogging",
    "OceanEcsLoggingExport",
    "OceanEcsLoggingExportOutputReference",
    "OceanEcsLoggingExportS3",
    "OceanEcsLoggingExportS3List",
    "OceanEcsLoggingExportS3OutputReference",
    "OceanEcsLoggingOutputReference",
    "OceanEcsOptimizeImages",
    "OceanEcsOptimizeImagesOutputReference",
    "OceanEcsScheduledTask",
    "OceanEcsScheduledTaskList",
    "OceanEcsScheduledTaskOutputReference",
    "OceanEcsScheduledTaskShutdownHours",
    "OceanEcsScheduledTaskShutdownHoursOutputReference",
    "OceanEcsScheduledTaskTasks",
    "OceanEcsScheduledTaskTasksList",
    "OceanEcsScheduledTaskTasksOutputReference",
    "OceanEcsTags",
    "OceanEcsTagsList",
    "OceanEcsTagsOutputReference",
    "OceanEcsUpdatePolicy",
    "OceanEcsUpdatePolicyOutputReference",
    "OceanEcsUpdatePolicyRollConfig",
    "OceanEcsUpdatePolicyRollConfigOutputReference",
]

publication.publish()
