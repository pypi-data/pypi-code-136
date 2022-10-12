'''
# `spotinst_ocean_aws`

Refer to the Terraform Registory for docs: [`spotinst_ocean_aws`](https://www.terraform.io/docs/providers/spotinst/r/ocean_aws).
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


class OceanAws(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAws",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws spotinst_ocean_aws}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        security_groups: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
        associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        autoscaler: typing.Optional[typing.Union["OceanAwsAutoscaler", typing.Dict[str, typing.Any]]] = None,
        blacklist: typing.Optional[typing.Sequence[builtins.str]] = None,
        controller_id: typing.Optional[builtins.str] = None,
        desired_capacity: typing.Optional[jsii.Number] = None,
        draining_timeout: typing.Optional[jsii.Number] = None,
        ebs_optimized: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fallback_to_ondemand: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        grace_period: typing.Optional[jsii.Number] = None,
        iam_instance_profile: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        image_id: typing.Optional[builtins.str] = None,
        instance_metadata_options: typing.Optional[typing.Union["OceanAwsInstanceMetadataOptions", typing.Dict[str, typing.Any]]] = None,
        key_name: typing.Optional[builtins.str] = None,
        load_balancers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAwsLoadBalancers", typing.Dict[str, typing.Any]]]]] = None,
        logging: typing.Optional[typing.Union["OceanAwsLogging", typing.Dict[str, typing.Any]]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        root_volume_size: typing.Optional[jsii.Number] = None,
        scheduled_task: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAwsScheduledTask", typing.Dict[str, typing.Any]]]]] = None,
        spot_percentage: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAwsTags", typing.Dict[str, typing.Any]]]]] = None,
        update_policy: typing.Optional[typing.Union["OceanAwsUpdatePolicy", typing.Dict[str, typing.Any]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws spotinst_ocean_aws} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#security_groups OceanAws#security_groups}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#subnet_ids OceanAws#subnet_ids}.
        :param associate_public_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#associate_public_ip_address OceanAws#associate_public_ip_address}.
        :param autoscaler: autoscaler block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#autoscaler OceanAws#autoscaler}
        :param blacklist: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#blacklist OceanAws#blacklist}.
        :param controller_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#controller_id OceanAws#controller_id}.
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#desired_capacity OceanAws#desired_capacity}.
        :param draining_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#draining_timeout OceanAws#draining_timeout}.
        :param ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#ebs_optimized OceanAws#ebs_optimized}.
        :param fallback_to_ondemand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#fallback_to_ondemand OceanAws#fallback_to_ondemand}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#grace_period OceanAws#grace_period}.
        :param iam_instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#iam_instance_profile OceanAws#iam_instance_profile}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#id OceanAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#image_id OceanAws#image_id}.
        :param instance_metadata_options: instance_metadata_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#instance_metadata_options OceanAws#instance_metadata_options}
        :param key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#key_name OceanAws#key_name}.
        :param load_balancers: load_balancers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#load_balancers OceanAws#load_balancers}
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#logging OceanAws#logging}
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#max_size OceanAws#max_size}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#min_size OceanAws#min_size}.
        :param monitoring: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#monitoring OceanAws#monitoring}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#name OceanAws#name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#region OceanAws#region}.
        :param root_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#root_volume_size OceanAws#root_volume_size}.
        :param scheduled_task: scheduled_task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#scheduled_task OceanAws#scheduled_task}
        :param spot_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#spot_percentage OceanAws#spot_percentage}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#tags OceanAws#tags}
        :param update_policy: update_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#update_policy OceanAws#update_policy}
        :param use_as_template_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#use_as_template_only OceanAws#use_as_template_only}.
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#user_data OceanAws#user_data}.
        :param utilize_commitments: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#utilize_commitments OceanAws#utilize_commitments}.
        :param utilize_reserved_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#utilize_reserved_instances OceanAws#utilize_reserved_instances}.
        :param whitelist: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#whitelist OceanAws#whitelist}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAws.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OceanAwsConfig(
            security_groups=security_groups,
            subnet_ids=subnet_ids,
            associate_public_ip_address=associate_public_ip_address,
            autoscaler=autoscaler,
            blacklist=blacklist,
            controller_id=controller_id,
            desired_capacity=desired_capacity,
            draining_timeout=draining_timeout,
            ebs_optimized=ebs_optimized,
            fallback_to_ondemand=fallback_to_ondemand,
            grace_period=grace_period,
            iam_instance_profile=iam_instance_profile,
            id=id,
            image_id=image_id,
            instance_metadata_options=instance_metadata_options,
            key_name=key_name,
            load_balancers=load_balancers,
            logging=logging,
            max_size=max_size,
            min_size=min_size,
            monitoring=monitoring,
            name=name,
            region=region,
            root_volume_size=root_volume_size,
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
        autoscale_cooldown: typing.Optional[jsii.Number] = None,
        autoscale_down: typing.Optional[typing.Union["OceanAwsAutoscalerAutoscaleDown", typing.Dict[str, typing.Any]]] = None,
        autoscale_headroom: typing.Optional[typing.Union["OceanAwsAutoscalerAutoscaleHeadroom", typing.Dict[str, typing.Any]]] = None,
        autoscale_is_auto_config: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        autoscale_is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_automatic_and_manual_headroom: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        extended_resource_definitions: typing.Optional[typing.Sequence[builtins.str]] = None,
        resource_limits: typing.Optional[typing.Union["OceanAwsAutoscalerResourceLimits", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param auto_headroom_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#auto_headroom_percentage OceanAws#auto_headroom_percentage}.
        :param autoscale_cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#autoscale_cooldown OceanAws#autoscale_cooldown}.
        :param autoscale_down: autoscale_down block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#autoscale_down OceanAws#autoscale_down}
        :param autoscale_headroom: autoscale_headroom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#autoscale_headroom OceanAws#autoscale_headroom}
        :param autoscale_is_auto_config: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#autoscale_is_auto_config OceanAws#autoscale_is_auto_config}.
        :param autoscale_is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#autoscale_is_enabled OceanAws#autoscale_is_enabled}.
        :param enable_automatic_and_manual_headroom: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#enable_automatic_and_manual_headroom OceanAws#enable_automatic_and_manual_headroom}.
        :param extended_resource_definitions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#extended_resource_definitions OceanAws#extended_resource_definitions}.
        :param resource_limits: resource_limits block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#resource_limits OceanAws#resource_limits}
        '''
        value = OceanAwsAutoscaler(
            auto_headroom_percentage=auto_headroom_percentage,
            autoscale_cooldown=autoscale_cooldown,
            autoscale_down=autoscale_down,
            autoscale_headroom=autoscale_headroom,
            autoscale_is_auto_config=autoscale_is_auto_config,
            autoscale_is_enabled=autoscale_is_enabled,
            enable_automatic_and_manual_headroom=enable_automatic_and_manual_headroom,
            extended_resource_definitions=extended_resource_definitions,
            resource_limits=resource_limits,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscaler", [value]))

    @jsii.member(jsii_name="putInstanceMetadataOptions")
    def put_instance_metadata_options(
        self,
        *,
        http_tokens: builtins.str,
        http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param http_tokens: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#http_tokens OceanAws#http_tokens}.
        :param http_put_response_hop_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#http_put_response_hop_limit OceanAws#http_put_response_hop_limit}.
        '''
        value = OceanAwsInstanceMetadataOptions(
            http_tokens=http_tokens,
            http_put_response_hop_limit=http_put_response_hop_limit,
        )

        return typing.cast(None, jsii.invoke(self, "putInstanceMetadataOptions", [value]))

    @jsii.member(jsii_name="putLoadBalancers")
    def put_load_balancers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAwsLoadBalancers", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAws.put_load_balancers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLoadBalancers", [value]))

    @jsii.member(jsii_name="putLogging")
    def put_logging(
        self,
        *,
        export: typing.Optional[typing.Union["OceanAwsLoggingExport", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param export: export block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#export OceanAws#export}
        '''
        value = OceanAwsLogging(export=export)

        return typing.cast(None, jsii.invoke(self, "putLogging", [value]))

    @jsii.member(jsii_name="putScheduledTask")
    def put_scheduled_task(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAwsScheduledTask", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAws.put_scheduled_task)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScheduledTask", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAwsTags", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAws.put_tags)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="putUpdatePolicy")
    def put_update_policy(
        self,
        *,
        should_roll: typing.Union[builtins.bool, cdktf.IResolvable],
        auto_apply_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        conditioned_roll: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        roll_config: typing.Optional[typing.Union["OceanAwsUpdatePolicyRollConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param should_roll: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#should_roll OceanAws#should_roll}.
        :param auto_apply_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#auto_apply_tags OceanAws#auto_apply_tags}.
        :param conditioned_roll: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#conditioned_roll OceanAws#conditioned_roll}.
        :param roll_config: roll_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#roll_config OceanAws#roll_config}
        '''
        value = OceanAwsUpdatePolicy(
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

    @jsii.member(jsii_name="resetBlacklist")
    def reset_blacklist(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlacklist", []))

    @jsii.member(jsii_name="resetControllerId")
    def reset_controller_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetControllerId", []))

    @jsii.member(jsii_name="resetDesiredCapacity")
    def reset_desired_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredCapacity", []))

    @jsii.member(jsii_name="resetDrainingTimeout")
    def reset_draining_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDrainingTimeout", []))

    @jsii.member(jsii_name="resetEbsOptimized")
    def reset_ebs_optimized(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsOptimized", []))

    @jsii.member(jsii_name="resetFallbackToOndemand")
    def reset_fallback_to_ondemand(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFallbackToOndemand", []))

    @jsii.member(jsii_name="resetGracePeriod")
    def reset_grace_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGracePeriod", []))

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

    @jsii.member(jsii_name="resetKeyName")
    def reset_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyName", []))

    @jsii.member(jsii_name="resetLoadBalancers")
    def reset_load_balancers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancers", []))

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

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetRootVolumeSize")
    def reset_root_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootVolumeSize", []))

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
    def autoscaler(self) -> "OceanAwsAutoscalerOutputReference":
        return typing.cast("OceanAwsAutoscalerOutputReference", jsii.get(self, "autoscaler"))

    @builtins.property
    @jsii.member(jsii_name="instanceMetadataOptions")
    def instance_metadata_options(
        self,
    ) -> "OceanAwsInstanceMetadataOptionsOutputReference":
        return typing.cast("OceanAwsInstanceMetadataOptionsOutputReference", jsii.get(self, "instanceMetadataOptions"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancers")
    def load_balancers(self) -> "OceanAwsLoadBalancersList":
        return typing.cast("OceanAwsLoadBalancersList", jsii.get(self, "loadBalancers"))

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> "OceanAwsLoggingOutputReference":
        return typing.cast("OceanAwsLoggingOutputReference", jsii.get(self, "logging"))

    @builtins.property
    @jsii.member(jsii_name="scheduledTask")
    def scheduled_task(self) -> "OceanAwsScheduledTaskList":
        return typing.cast("OceanAwsScheduledTaskList", jsii.get(self, "scheduledTask"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "OceanAwsTagsList":
        return typing.cast("OceanAwsTagsList", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="updatePolicy")
    def update_policy(self) -> "OceanAwsUpdatePolicyOutputReference":
        return typing.cast("OceanAwsUpdatePolicyOutputReference", jsii.get(self, "updatePolicy"))

    @builtins.property
    @jsii.member(jsii_name="associatePublicIpAddressInput")
    def associate_public_ip_address_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "associatePublicIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscalerInput")
    def autoscaler_input(self) -> typing.Optional["OceanAwsAutoscaler"]:
        return typing.cast(typing.Optional["OceanAwsAutoscaler"], jsii.get(self, "autoscalerInput"))

    @builtins.property
    @jsii.member(jsii_name="blacklistInput")
    def blacklist_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "blacklistInput"))

    @builtins.property
    @jsii.member(jsii_name="controllerIdInput")
    def controller_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "controllerIdInput"))

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
    @jsii.member(jsii_name="fallbackToOndemandInput")
    def fallback_to_ondemand_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fallbackToOndemandInput"))

    @builtins.property
    @jsii.member(jsii_name="gracePeriodInput")
    def grace_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gracePeriodInput"))

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
    ) -> typing.Optional["OceanAwsInstanceMetadataOptions"]:
        return typing.cast(typing.Optional["OceanAwsInstanceMetadataOptions"], jsii.get(self, "instanceMetadataOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="keyNameInput")
    def key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancersInput")
    def load_balancers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsLoadBalancers"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsLoadBalancers"]]], jsii.get(self, "loadBalancersInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingInput")
    def logging_input(self) -> typing.Optional["OceanAwsLogging"]:
        return typing.cast(typing.Optional["OceanAwsLogging"], jsii.get(self, "loggingInput"))

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
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="rootVolumeSizeInput")
    def root_volume_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rootVolumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduledTaskInput")
    def scheduled_task_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsScheduledTask"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsScheduledTask"]]], jsii.get(self, "scheduledTaskInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsTags"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsTags"]]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="updatePolicyInput")
    def update_policy_input(self) -> typing.Optional["OceanAwsUpdatePolicy"]:
        return typing.cast(typing.Optional["OceanAwsUpdatePolicy"], jsii.get(self, "updatePolicyInput"))

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
            type_hints = typing.get_type_hints(getattr(OceanAws, "associate_public_ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatePublicIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="blacklist")
    def blacklist(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "blacklist"))

    @blacklist.setter
    def blacklist(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "blacklist").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blacklist", value)

    @builtins.property
    @jsii.member(jsii_name="controllerId")
    def controller_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "controllerId"))

    @controller_id.setter
    def controller_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "controller_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "controllerId", value)

    @builtins.property
    @jsii.member(jsii_name="desiredCapacity")
    def desired_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredCapacity"))

    @desired_capacity.setter
    def desired_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "desired_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="drainingTimeout")
    def draining_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "drainingTimeout"))

    @draining_timeout.setter
    def draining_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "draining_timeout").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAws, "ebs_optimized").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsOptimized", value)

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
            type_hints = typing.get_type_hints(getattr(OceanAws, "fallback_to_ondemand").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fallbackToOndemand", value)

    @builtins.property
    @jsii.member(jsii_name="gracePeriod")
    def grace_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gracePeriod"))

    @grace_period.setter
    def grace_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "grace_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gracePeriod", value)

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfile")
    def iam_instance_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamInstanceProfile"))

    @iam_instance_profile.setter
    def iam_instance_profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "iam_instance_profile").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamInstanceProfile", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="imageId")
    def image_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageId"))

    @image_id.setter
    def image_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "image_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageId", value)

    @builtins.property
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyName"))

    @key_name.setter
    def key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyName", value)

    @builtins.property
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSize"))

    @max_size.setter
    def max_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "max_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSize", value)

    @builtins.property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minSize"))

    @min_size.setter
    def min_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "min_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minSize", value)

    @builtins.property
    @jsii.member(jsii_name="monitoring")
    def monitoring(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "monitoring"))

    @monitoring.setter
    def monitoring(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "monitoring").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitoring", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="rootVolumeSize")
    def root_volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rootVolumeSize"))

    @root_volume_size.setter
    def root_volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "root_volume_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootVolumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "security_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="spotPercentage")
    def spot_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotPercentage"))

    @spot_percentage.setter
    def spot_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "spot_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "subnet_ids").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAws, "use_as_template_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useAsTemplateOnly", value)

    @builtins.property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userData"))

    @user_data.setter
    def user_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "user_data").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAws, "utilize_commitments").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAws, "utilize_reserved_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "utilizeReservedInstances", value)

    @builtins.property
    @jsii.member(jsii_name="whitelist")
    def whitelist(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "whitelist"))

    @whitelist.setter
    def whitelist(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAws, "whitelist").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whitelist", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsAutoscaler",
    jsii_struct_bases=[],
    name_mapping={
        "auto_headroom_percentage": "autoHeadroomPercentage",
        "autoscale_cooldown": "autoscaleCooldown",
        "autoscale_down": "autoscaleDown",
        "autoscale_headroom": "autoscaleHeadroom",
        "autoscale_is_auto_config": "autoscaleIsAutoConfig",
        "autoscale_is_enabled": "autoscaleIsEnabled",
        "enable_automatic_and_manual_headroom": "enableAutomaticAndManualHeadroom",
        "extended_resource_definitions": "extendedResourceDefinitions",
        "resource_limits": "resourceLimits",
    },
)
class OceanAwsAutoscaler:
    def __init__(
        self,
        *,
        auto_headroom_percentage: typing.Optional[jsii.Number] = None,
        autoscale_cooldown: typing.Optional[jsii.Number] = None,
        autoscale_down: typing.Optional[typing.Union["OceanAwsAutoscalerAutoscaleDown", typing.Dict[str, typing.Any]]] = None,
        autoscale_headroom: typing.Optional[typing.Union["OceanAwsAutoscalerAutoscaleHeadroom", typing.Dict[str, typing.Any]]] = None,
        autoscale_is_auto_config: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        autoscale_is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_automatic_and_manual_headroom: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        extended_resource_definitions: typing.Optional[typing.Sequence[builtins.str]] = None,
        resource_limits: typing.Optional[typing.Union["OceanAwsAutoscalerResourceLimits", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param auto_headroom_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#auto_headroom_percentage OceanAws#auto_headroom_percentage}.
        :param autoscale_cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#autoscale_cooldown OceanAws#autoscale_cooldown}.
        :param autoscale_down: autoscale_down block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#autoscale_down OceanAws#autoscale_down}
        :param autoscale_headroom: autoscale_headroom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#autoscale_headroom OceanAws#autoscale_headroom}
        :param autoscale_is_auto_config: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#autoscale_is_auto_config OceanAws#autoscale_is_auto_config}.
        :param autoscale_is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#autoscale_is_enabled OceanAws#autoscale_is_enabled}.
        :param enable_automatic_and_manual_headroom: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#enable_automatic_and_manual_headroom OceanAws#enable_automatic_and_manual_headroom}.
        :param extended_resource_definitions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#extended_resource_definitions OceanAws#extended_resource_definitions}.
        :param resource_limits: resource_limits block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#resource_limits OceanAws#resource_limits}
        '''
        if isinstance(autoscale_down, dict):
            autoscale_down = OceanAwsAutoscalerAutoscaleDown(**autoscale_down)
        if isinstance(autoscale_headroom, dict):
            autoscale_headroom = OceanAwsAutoscalerAutoscaleHeadroom(**autoscale_headroom)
        if isinstance(resource_limits, dict):
            resource_limits = OceanAwsAutoscalerResourceLimits(**resource_limits)
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsAutoscaler.__init__)
            check_type(argname="argument auto_headroom_percentage", value=auto_headroom_percentage, expected_type=type_hints["auto_headroom_percentage"])
            check_type(argname="argument autoscale_cooldown", value=autoscale_cooldown, expected_type=type_hints["autoscale_cooldown"])
            check_type(argname="argument autoscale_down", value=autoscale_down, expected_type=type_hints["autoscale_down"])
            check_type(argname="argument autoscale_headroom", value=autoscale_headroom, expected_type=type_hints["autoscale_headroom"])
            check_type(argname="argument autoscale_is_auto_config", value=autoscale_is_auto_config, expected_type=type_hints["autoscale_is_auto_config"])
            check_type(argname="argument autoscale_is_enabled", value=autoscale_is_enabled, expected_type=type_hints["autoscale_is_enabled"])
            check_type(argname="argument enable_automatic_and_manual_headroom", value=enable_automatic_and_manual_headroom, expected_type=type_hints["enable_automatic_and_manual_headroom"])
            check_type(argname="argument extended_resource_definitions", value=extended_resource_definitions, expected_type=type_hints["extended_resource_definitions"])
            check_type(argname="argument resource_limits", value=resource_limits, expected_type=type_hints["resource_limits"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_headroom_percentage is not None:
            self._values["auto_headroom_percentage"] = auto_headroom_percentage
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
        if enable_automatic_and_manual_headroom is not None:
            self._values["enable_automatic_and_manual_headroom"] = enable_automatic_and_manual_headroom
        if extended_resource_definitions is not None:
            self._values["extended_resource_definitions"] = extended_resource_definitions
        if resource_limits is not None:
            self._values["resource_limits"] = resource_limits

    @builtins.property
    def auto_headroom_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#auto_headroom_percentage OceanAws#auto_headroom_percentage}.'''
        result = self._values.get("auto_headroom_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def autoscale_cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#autoscale_cooldown OceanAws#autoscale_cooldown}.'''
        result = self._values.get("autoscale_cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def autoscale_down(self) -> typing.Optional["OceanAwsAutoscalerAutoscaleDown"]:
        '''autoscale_down block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#autoscale_down OceanAws#autoscale_down}
        '''
        result = self._values.get("autoscale_down")
        return typing.cast(typing.Optional["OceanAwsAutoscalerAutoscaleDown"], result)

    @builtins.property
    def autoscale_headroom(
        self,
    ) -> typing.Optional["OceanAwsAutoscalerAutoscaleHeadroom"]:
        '''autoscale_headroom block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#autoscale_headroom OceanAws#autoscale_headroom}
        '''
        result = self._values.get("autoscale_headroom")
        return typing.cast(typing.Optional["OceanAwsAutoscalerAutoscaleHeadroom"], result)

    @builtins.property
    def autoscale_is_auto_config(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#autoscale_is_auto_config OceanAws#autoscale_is_auto_config}.'''
        result = self._values.get("autoscale_is_auto_config")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def autoscale_is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#autoscale_is_enabled OceanAws#autoscale_is_enabled}.'''
        result = self._values.get("autoscale_is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_automatic_and_manual_headroom(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#enable_automatic_and_manual_headroom OceanAws#enable_automatic_and_manual_headroom}.'''
        result = self._values.get("enable_automatic_and_manual_headroom")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def extended_resource_definitions(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#extended_resource_definitions OceanAws#extended_resource_definitions}.'''
        result = self._values.get("extended_resource_definitions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def resource_limits(self) -> typing.Optional["OceanAwsAutoscalerResourceLimits"]:
        '''resource_limits block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#resource_limits OceanAws#resource_limits}
        '''
        result = self._values.get("resource_limits")
        return typing.cast(typing.Optional["OceanAwsAutoscalerResourceLimits"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAwsAutoscaler(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsAutoscalerAutoscaleDown",
    jsii_struct_bases=[],
    name_mapping={
        "evaluation_periods": "evaluationPeriods",
        "max_scale_down_percentage": "maxScaleDownPercentage",
    },
)
class OceanAwsAutoscalerAutoscaleDown:
    def __init__(
        self,
        *,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        max_scale_down_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param evaluation_periods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#evaluation_periods OceanAws#evaluation_periods}.
        :param max_scale_down_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#max_scale_down_percentage OceanAws#max_scale_down_percentage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsAutoscalerAutoscaleDown.__init__)
            check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
            check_type(argname="argument max_scale_down_percentage", value=max_scale_down_percentage, expected_type=type_hints["max_scale_down_percentage"])
        self._values: typing.Dict[str, typing.Any] = {}
        if evaluation_periods is not None:
            self._values["evaluation_periods"] = evaluation_periods
        if max_scale_down_percentage is not None:
            self._values["max_scale_down_percentage"] = max_scale_down_percentage

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#evaluation_periods OceanAws#evaluation_periods}.'''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_scale_down_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#max_scale_down_percentage OceanAws#max_scale_down_percentage}.'''
        result = self._values.get("max_scale_down_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAwsAutoscalerAutoscaleDown(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAwsAutoscalerAutoscaleDownOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsAutoscalerAutoscaleDownOutputReference",
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
            type_hints = typing.get_type_hints(OceanAwsAutoscalerAutoscaleDownOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEvaluationPeriods")
    def reset_evaluation_periods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluationPeriods", []))

    @jsii.member(jsii_name="resetMaxScaleDownPercentage")
    def reset_max_scale_down_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxScaleDownPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriodsInput")
    def evaluation_periods_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "evaluationPeriodsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxScaleDownPercentageInput")
    def max_scale_down_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxScaleDownPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriods")
    def evaluation_periods(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "evaluationPeriods"))

    @evaluation_periods.setter
    def evaluation_periods(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsAutoscalerAutoscaleDownOutputReference, "evaluation_periods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationPeriods", value)

    @builtins.property
    @jsii.member(jsii_name="maxScaleDownPercentage")
    def max_scale_down_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxScaleDownPercentage"))

    @max_scale_down_percentage.setter
    def max_scale_down_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsAutoscalerAutoscaleDownOutputReference, "max_scale_down_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxScaleDownPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanAwsAutoscalerAutoscaleDown]:
        return typing.cast(typing.Optional[OceanAwsAutoscalerAutoscaleDown], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanAwsAutoscalerAutoscaleDown],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsAutoscalerAutoscaleDownOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsAutoscalerAutoscaleHeadroom",
    jsii_struct_bases=[],
    name_mapping={
        "cpu_per_unit": "cpuPerUnit",
        "gpu_per_unit": "gpuPerUnit",
        "memory_per_unit": "memoryPerUnit",
        "num_of_units": "numOfUnits",
    },
)
class OceanAwsAutoscalerAutoscaleHeadroom:
    def __init__(
        self,
        *,
        cpu_per_unit: typing.Optional[jsii.Number] = None,
        gpu_per_unit: typing.Optional[jsii.Number] = None,
        memory_per_unit: typing.Optional[jsii.Number] = None,
        num_of_units: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#cpu_per_unit OceanAws#cpu_per_unit}.
        :param gpu_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#gpu_per_unit OceanAws#gpu_per_unit}.
        :param memory_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#memory_per_unit OceanAws#memory_per_unit}.
        :param num_of_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#num_of_units OceanAws#num_of_units}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsAutoscalerAutoscaleHeadroom.__init__)
            check_type(argname="argument cpu_per_unit", value=cpu_per_unit, expected_type=type_hints["cpu_per_unit"])
            check_type(argname="argument gpu_per_unit", value=gpu_per_unit, expected_type=type_hints["gpu_per_unit"])
            check_type(argname="argument memory_per_unit", value=memory_per_unit, expected_type=type_hints["memory_per_unit"])
            check_type(argname="argument num_of_units", value=num_of_units, expected_type=type_hints["num_of_units"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cpu_per_unit is not None:
            self._values["cpu_per_unit"] = cpu_per_unit
        if gpu_per_unit is not None:
            self._values["gpu_per_unit"] = gpu_per_unit
        if memory_per_unit is not None:
            self._values["memory_per_unit"] = memory_per_unit
        if num_of_units is not None:
            self._values["num_of_units"] = num_of_units

    @builtins.property
    def cpu_per_unit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#cpu_per_unit OceanAws#cpu_per_unit}.'''
        result = self._values.get("cpu_per_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def gpu_per_unit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#gpu_per_unit OceanAws#gpu_per_unit}.'''
        result = self._values.get("gpu_per_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_per_unit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#memory_per_unit OceanAws#memory_per_unit}.'''
        result = self._values.get("memory_per_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def num_of_units(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#num_of_units OceanAws#num_of_units}.'''
        result = self._values.get("num_of_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAwsAutoscalerAutoscaleHeadroom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAwsAutoscalerAutoscaleHeadroomOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsAutoscalerAutoscaleHeadroomOutputReference",
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
            type_hints = typing.get_type_hints(OceanAwsAutoscalerAutoscaleHeadroomOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCpuPerUnit")
    def reset_cpu_per_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuPerUnit", []))

    @jsii.member(jsii_name="resetGpuPerUnit")
    def reset_gpu_per_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGpuPerUnit", []))

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
    @jsii.member(jsii_name="gpuPerUnitInput")
    def gpu_per_unit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gpuPerUnitInput"))

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
            type_hints = typing.get_type_hints(getattr(OceanAwsAutoscalerAutoscaleHeadroomOutputReference, "cpu_per_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuPerUnit", value)

    @builtins.property
    @jsii.member(jsii_name="gpuPerUnit")
    def gpu_per_unit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gpuPerUnit"))

    @gpu_per_unit.setter
    def gpu_per_unit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsAutoscalerAutoscaleHeadroomOutputReference, "gpu_per_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gpuPerUnit", value)

    @builtins.property
    @jsii.member(jsii_name="memoryPerUnit")
    def memory_per_unit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryPerUnit"))

    @memory_per_unit.setter
    def memory_per_unit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsAutoscalerAutoscaleHeadroomOutputReference, "memory_per_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryPerUnit", value)

    @builtins.property
    @jsii.member(jsii_name="numOfUnits")
    def num_of_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numOfUnits"))

    @num_of_units.setter
    def num_of_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsAutoscalerAutoscaleHeadroomOutputReference, "num_of_units").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numOfUnits", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanAwsAutoscalerAutoscaleHeadroom]:
        return typing.cast(typing.Optional[OceanAwsAutoscalerAutoscaleHeadroom], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanAwsAutoscalerAutoscaleHeadroom],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsAutoscalerAutoscaleHeadroomOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAwsAutoscalerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsAutoscalerOutputReference",
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
            type_hints = typing.get_type_hints(OceanAwsAutoscalerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutoscaleDown")
    def put_autoscale_down(
        self,
        *,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        max_scale_down_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param evaluation_periods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#evaluation_periods OceanAws#evaluation_periods}.
        :param max_scale_down_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#max_scale_down_percentage OceanAws#max_scale_down_percentage}.
        '''
        value = OceanAwsAutoscalerAutoscaleDown(
            evaluation_periods=evaluation_periods,
            max_scale_down_percentage=max_scale_down_percentage,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscaleDown", [value]))

    @jsii.member(jsii_name="putAutoscaleHeadroom")
    def put_autoscale_headroom(
        self,
        *,
        cpu_per_unit: typing.Optional[jsii.Number] = None,
        gpu_per_unit: typing.Optional[jsii.Number] = None,
        memory_per_unit: typing.Optional[jsii.Number] = None,
        num_of_units: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#cpu_per_unit OceanAws#cpu_per_unit}.
        :param gpu_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#gpu_per_unit OceanAws#gpu_per_unit}.
        :param memory_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#memory_per_unit OceanAws#memory_per_unit}.
        :param num_of_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#num_of_units OceanAws#num_of_units}.
        '''
        value = OceanAwsAutoscalerAutoscaleHeadroom(
            cpu_per_unit=cpu_per_unit,
            gpu_per_unit=gpu_per_unit,
            memory_per_unit=memory_per_unit,
            num_of_units=num_of_units,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscaleHeadroom", [value]))

    @jsii.member(jsii_name="putResourceLimits")
    def put_resource_limits(
        self,
        *,
        max_memory_gib: typing.Optional[jsii.Number] = None,
        max_vcpu: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_memory_gib: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#max_memory_gib OceanAws#max_memory_gib}.
        :param max_vcpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#max_vcpu OceanAws#max_vcpu}.
        '''
        value = OceanAwsAutoscalerResourceLimits(
            max_memory_gib=max_memory_gib, max_vcpu=max_vcpu
        )

        return typing.cast(None, jsii.invoke(self, "putResourceLimits", [value]))

    @jsii.member(jsii_name="resetAutoHeadroomPercentage")
    def reset_auto_headroom_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoHeadroomPercentage", []))

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

    @jsii.member(jsii_name="resetEnableAutomaticAndManualHeadroom")
    def reset_enable_automatic_and_manual_headroom(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAutomaticAndManualHeadroom", []))

    @jsii.member(jsii_name="resetExtendedResourceDefinitions")
    def reset_extended_resource_definitions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtendedResourceDefinitions", []))

    @jsii.member(jsii_name="resetResourceLimits")
    def reset_resource_limits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceLimits", []))

    @builtins.property
    @jsii.member(jsii_name="autoscaleDown")
    def autoscale_down(self) -> OceanAwsAutoscalerAutoscaleDownOutputReference:
        return typing.cast(OceanAwsAutoscalerAutoscaleDownOutputReference, jsii.get(self, "autoscaleDown"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleHeadroom")
    def autoscale_headroom(self) -> OceanAwsAutoscalerAutoscaleHeadroomOutputReference:
        return typing.cast(OceanAwsAutoscalerAutoscaleHeadroomOutputReference, jsii.get(self, "autoscaleHeadroom"))

    @builtins.property
    @jsii.member(jsii_name="resourceLimits")
    def resource_limits(self) -> "OceanAwsAutoscalerResourceLimitsOutputReference":
        return typing.cast("OceanAwsAutoscalerResourceLimitsOutputReference", jsii.get(self, "resourceLimits"))

    @builtins.property
    @jsii.member(jsii_name="autoHeadroomPercentageInput")
    def auto_headroom_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autoHeadroomPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleCooldownInput")
    def autoscale_cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autoscaleCooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleDownInput")
    def autoscale_down_input(self) -> typing.Optional[OceanAwsAutoscalerAutoscaleDown]:
        return typing.cast(typing.Optional[OceanAwsAutoscalerAutoscaleDown], jsii.get(self, "autoscaleDownInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleHeadroomInput")
    def autoscale_headroom_input(
        self,
    ) -> typing.Optional[OceanAwsAutoscalerAutoscaleHeadroom]:
        return typing.cast(typing.Optional[OceanAwsAutoscalerAutoscaleHeadroom], jsii.get(self, "autoscaleHeadroomInput"))

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
    @jsii.member(jsii_name="enableAutomaticAndManualHeadroomInput")
    def enable_automatic_and_manual_headroom_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableAutomaticAndManualHeadroomInput"))

    @builtins.property
    @jsii.member(jsii_name="extendedResourceDefinitionsInput")
    def extended_resource_definitions_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "extendedResourceDefinitionsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLimitsInput")
    def resource_limits_input(
        self,
    ) -> typing.Optional["OceanAwsAutoscalerResourceLimits"]:
        return typing.cast(typing.Optional["OceanAwsAutoscalerResourceLimits"], jsii.get(self, "resourceLimitsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoHeadroomPercentage")
    def auto_headroom_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autoHeadroomPercentage"))

    @auto_headroom_percentage.setter
    def auto_headroom_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsAutoscalerOutputReference, "auto_headroom_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoHeadroomPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="autoscaleCooldown")
    def autoscale_cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autoscaleCooldown"))

    @autoscale_cooldown.setter
    def autoscale_cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsAutoscalerOutputReference, "autoscale_cooldown").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsAutoscalerOutputReference, "autoscale_is_auto_config").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsAutoscalerOutputReference, "autoscale_is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoscaleIsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="enableAutomaticAndManualHeadroom")
    def enable_automatic_and_manual_headroom(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableAutomaticAndManualHeadroom"))

    @enable_automatic_and_manual_headroom.setter
    def enable_automatic_and_manual_headroom(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsAutoscalerOutputReference, "enable_automatic_and_manual_headroom").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutomaticAndManualHeadroom", value)

    @builtins.property
    @jsii.member(jsii_name="extendedResourceDefinitions")
    def extended_resource_definitions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "extendedResourceDefinitions"))

    @extended_resource_definitions.setter
    def extended_resource_definitions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsAutoscalerOutputReference, "extended_resource_definitions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extendedResourceDefinitions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanAwsAutoscaler]:
        return typing.cast(typing.Optional[OceanAwsAutoscaler], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OceanAwsAutoscaler]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsAutoscalerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsAutoscalerResourceLimits",
    jsii_struct_bases=[],
    name_mapping={"max_memory_gib": "maxMemoryGib", "max_vcpu": "maxVcpu"},
)
class OceanAwsAutoscalerResourceLimits:
    def __init__(
        self,
        *,
        max_memory_gib: typing.Optional[jsii.Number] = None,
        max_vcpu: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_memory_gib: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#max_memory_gib OceanAws#max_memory_gib}.
        :param max_vcpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#max_vcpu OceanAws#max_vcpu}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsAutoscalerResourceLimits.__init__)
            check_type(argname="argument max_memory_gib", value=max_memory_gib, expected_type=type_hints["max_memory_gib"])
            check_type(argname="argument max_vcpu", value=max_vcpu, expected_type=type_hints["max_vcpu"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_memory_gib is not None:
            self._values["max_memory_gib"] = max_memory_gib
        if max_vcpu is not None:
            self._values["max_vcpu"] = max_vcpu

    @builtins.property
    def max_memory_gib(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#max_memory_gib OceanAws#max_memory_gib}.'''
        result = self._values.get("max_memory_gib")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_vcpu(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#max_vcpu OceanAws#max_vcpu}.'''
        result = self._values.get("max_vcpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAwsAutoscalerResourceLimits(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAwsAutoscalerResourceLimitsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsAutoscalerResourceLimitsOutputReference",
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
            type_hints = typing.get_type_hints(OceanAwsAutoscalerResourceLimitsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsAutoscalerResourceLimitsOutputReference, "max_memory_gib").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxMemoryGib", value)

    @builtins.property
    @jsii.member(jsii_name="maxVcpu")
    def max_vcpu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxVcpu"))

    @max_vcpu.setter
    def max_vcpu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsAutoscalerResourceLimitsOutputReference, "max_vcpu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxVcpu", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanAwsAutoscalerResourceLimits]:
        return typing.cast(typing.Optional[OceanAwsAutoscalerResourceLimits], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanAwsAutoscalerResourceLimits],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsAutoscalerResourceLimitsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "security_groups": "securityGroups",
        "subnet_ids": "subnetIds",
        "associate_public_ip_address": "associatePublicIpAddress",
        "autoscaler": "autoscaler",
        "blacklist": "blacklist",
        "controller_id": "controllerId",
        "desired_capacity": "desiredCapacity",
        "draining_timeout": "drainingTimeout",
        "ebs_optimized": "ebsOptimized",
        "fallback_to_ondemand": "fallbackToOndemand",
        "grace_period": "gracePeriod",
        "iam_instance_profile": "iamInstanceProfile",
        "id": "id",
        "image_id": "imageId",
        "instance_metadata_options": "instanceMetadataOptions",
        "key_name": "keyName",
        "load_balancers": "loadBalancers",
        "logging": "logging",
        "max_size": "maxSize",
        "min_size": "minSize",
        "monitoring": "monitoring",
        "name": "name",
        "region": "region",
        "root_volume_size": "rootVolumeSize",
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
class OceanAwsConfig(cdktf.TerraformMetaArguments):
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
        security_groups: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
        associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        autoscaler: typing.Optional[typing.Union[OceanAwsAutoscaler, typing.Dict[str, typing.Any]]] = None,
        blacklist: typing.Optional[typing.Sequence[builtins.str]] = None,
        controller_id: typing.Optional[builtins.str] = None,
        desired_capacity: typing.Optional[jsii.Number] = None,
        draining_timeout: typing.Optional[jsii.Number] = None,
        ebs_optimized: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fallback_to_ondemand: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        grace_period: typing.Optional[jsii.Number] = None,
        iam_instance_profile: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        image_id: typing.Optional[builtins.str] = None,
        instance_metadata_options: typing.Optional[typing.Union["OceanAwsInstanceMetadataOptions", typing.Dict[str, typing.Any]]] = None,
        key_name: typing.Optional[builtins.str] = None,
        load_balancers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAwsLoadBalancers", typing.Dict[str, typing.Any]]]]] = None,
        logging: typing.Optional[typing.Union["OceanAwsLogging", typing.Dict[str, typing.Any]]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        monitoring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        root_volume_size: typing.Optional[jsii.Number] = None,
        scheduled_task: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAwsScheduledTask", typing.Dict[str, typing.Any]]]]] = None,
        spot_percentage: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAwsTags", typing.Dict[str, typing.Any]]]]] = None,
        update_policy: typing.Optional[typing.Union["OceanAwsUpdatePolicy", typing.Dict[str, typing.Any]]] = None,
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
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#security_groups OceanAws#security_groups}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#subnet_ids OceanAws#subnet_ids}.
        :param associate_public_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#associate_public_ip_address OceanAws#associate_public_ip_address}.
        :param autoscaler: autoscaler block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#autoscaler OceanAws#autoscaler}
        :param blacklist: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#blacklist OceanAws#blacklist}.
        :param controller_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#controller_id OceanAws#controller_id}.
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#desired_capacity OceanAws#desired_capacity}.
        :param draining_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#draining_timeout OceanAws#draining_timeout}.
        :param ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#ebs_optimized OceanAws#ebs_optimized}.
        :param fallback_to_ondemand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#fallback_to_ondemand OceanAws#fallback_to_ondemand}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#grace_period OceanAws#grace_period}.
        :param iam_instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#iam_instance_profile OceanAws#iam_instance_profile}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#id OceanAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#image_id OceanAws#image_id}.
        :param instance_metadata_options: instance_metadata_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#instance_metadata_options OceanAws#instance_metadata_options}
        :param key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#key_name OceanAws#key_name}.
        :param load_balancers: load_balancers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#load_balancers OceanAws#load_balancers}
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#logging OceanAws#logging}
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#max_size OceanAws#max_size}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#min_size OceanAws#min_size}.
        :param monitoring: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#monitoring OceanAws#monitoring}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#name OceanAws#name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#region OceanAws#region}.
        :param root_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#root_volume_size OceanAws#root_volume_size}.
        :param scheduled_task: scheduled_task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#scheduled_task OceanAws#scheduled_task}
        :param spot_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#spot_percentage OceanAws#spot_percentage}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#tags OceanAws#tags}
        :param update_policy: update_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#update_policy OceanAws#update_policy}
        :param use_as_template_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#use_as_template_only OceanAws#use_as_template_only}.
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#user_data OceanAws#user_data}.
        :param utilize_commitments: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#utilize_commitments OceanAws#utilize_commitments}.
        :param utilize_reserved_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#utilize_reserved_instances OceanAws#utilize_reserved_instances}.
        :param whitelist: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#whitelist OceanAws#whitelist}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(autoscaler, dict):
            autoscaler = OceanAwsAutoscaler(**autoscaler)
        if isinstance(instance_metadata_options, dict):
            instance_metadata_options = OceanAwsInstanceMetadataOptions(**instance_metadata_options)
        if isinstance(logging, dict):
            logging = OceanAwsLogging(**logging)
        if isinstance(update_policy, dict):
            update_policy = OceanAwsUpdatePolicy(**update_policy)
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument associate_public_ip_address", value=associate_public_ip_address, expected_type=type_hints["associate_public_ip_address"])
            check_type(argname="argument autoscaler", value=autoscaler, expected_type=type_hints["autoscaler"])
            check_type(argname="argument blacklist", value=blacklist, expected_type=type_hints["blacklist"])
            check_type(argname="argument controller_id", value=controller_id, expected_type=type_hints["controller_id"])
            check_type(argname="argument desired_capacity", value=desired_capacity, expected_type=type_hints["desired_capacity"])
            check_type(argname="argument draining_timeout", value=draining_timeout, expected_type=type_hints["draining_timeout"])
            check_type(argname="argument ebs_optimized", value=ebs_optimized, expected_type=type_hints["ebs_optimized"])
            check_type(argname="argument fallback_to_ondemand", value=fallback_to_ondemand, expected_type=type_hints["fallback_to_ondemand"])
            check_type(argname="argument grace_period", value=grace_period, expected_type=type_hints["grace_period"])
            check_type(argname="argument iam_instance_profile", value=iam_instance_profile, expected_type=type_hints["iam_instance_profile"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument image_id", value=image_id, expected_type=type_hints["image_id"])
            check_type(argname="argument instance_metadata_options", value=instance_metadata_options, expected_type=type_hints["instance_metadata_options"])
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument load_balancers", value=load_balancers, expected_type=type_hints["load_balancers"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
            check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            check_type(argname="argument monitoring", value=monitoring, expected_type=type_hints["monitoring"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument root_volume_size", value=root_volume_size, expected_type=type_hints["root_volume_size"])
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
            "security_groups": security_groups,
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
        if blacklist is not None:
            self._values["blacklist"] = blacklist
        if controller_id is not None:
            self._values["controller_id"] = controller_id
        if desired_capacity is not None:
            self._values["desired_capacity"] = desired_capacity
        if draining_timeout is not None:
            self._values["draining_timeout"] = draining_timeout
        if ebs_optimized is not None:
            self._values["ebs_optimized"] = ebs_optimized
        if fallback_to_ondemand is not None:
            self._values["fallback_to_ondemand"] = fallback_to_ondemand
        if grace_period is not None:
            self._values["grace_period"] = grace_period
        if iam_instance_profile is not None:
            self._values["iam_instance_profile"] = iam_instance_profile
        if id is not None:
            self._values["id"] = id
        if image_id is not None:
            self._values["image_id"] = image_id
        if instance_metadata_options is not None:
            self._values["instance_metadata_options"] = instance_metadata_options
        if key_name is not None:
            self._values["key_name"] = key_name
        if load_balancers is not None:
            self._values["load_balancers"] = load_balancers
        if logging is not None:
            self._values["logging"] = logging
        if max_size is not None:
            self._values["max_size"] = max_size
        if min_size is not None:
            self._values["min_size"] = min_size
        if monitoring is not None:
            self._values["monitoring"] = monitoring
        if name is not None:
            self._values["name"] = name
        if region is not None:
            self._values["region"] = region
        if root_volume_size is not None:
            self._values["root_volume_size"] = root_volume_size
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
    def security_groups(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#security_groups OceanAws#security_groups}.'''
        result = self._values.get("security_groups")
        assert result is not None, "Required property 'security_groups' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#subnet_ids OceanAws#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def associate_public_ip_address(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#associate_public_ip_address OceanAws#associate_public_ip_address}.'''
        result = self._values.get("associate_public_ip_address")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def autoscaler(self) -> typing.Optional[OceanAwsAutoscaler]:
        '''autoscaler block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#autoscaler OceanAws#autoscaler}
        '''
        result = self._values.get("autoscaler")
        return typing.cast(typing.Optional[OceanAwsAutoscaler], result)

    @builtins.property
    def blacklist(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#blacklist OceanAws#blacklist}.'''
        result = self._values.get("blacklist")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def controller_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#controller_id OceanAws#controller_id}.'''
        result = self._values.get("controller_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def desired_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#desired_capacity OceanAws#desired_capacity}.'''
        result = self._values.get("desired_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def draining_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#draining_timeout OceanAws#draining_timeout}.'''
        result = self._values.get("draining_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ebs_optimized(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#ebs_optimized OceanAws#ebs_optimized}.'''
        result = self._values.get("ebs_optimized")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def fallback_to_ondemand(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#fallback_to_ondemand OceanAws#fallback_to_ondemand}.'''
        result = self._values.get("fallback_to_ondemand")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def grace_period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#grace_period OceanAws#grace_period}.'''
        result = self._values.get("grace_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def iam_instance_profile(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#iam_instance_profile OceanAws#iam_instance_profile}.'''
        result = self._values.get("iam_instance_profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#id OceanAws#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#image_id OceanAws#image_id}.'''
        result = self._values.get("image_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_metadata_options(
        self,
    ) -> typing.Optional["OceanAwsInstanceMetadataOptions"]:
        '''instance_metadata_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#instance_metadata_options OceanAws#instance_metadata_options}
        '''
        result = self._values.get("instance_metadata_options")
        return typing.cast(typing.Optional["OceanAwsInstanceMetadataOptions"], result)

    @builtins.property
    def key_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#key_name OceanAws#key_name}.'''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsLoadBalancers"]]]:
        '''load_balancers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#load_balancers OceanAws#load_balancers}
        '''
        result = self._values.get("load_balancers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsLoadBalancers"]]], result)

    @builtins.property
    def logging(self) -> typing.Optional["OceanAwsLogging"]:
        '''logging block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#logging OceanAws#logging}
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional["OceanAwsLogging"], result)

    @builtins.property
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#max_size OceanAws#max_size}.'''
        result = self._values.get("max_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#min_size OceanAws#min_size}.'''
        result = self._values.get("min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def monitoring(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#monitoring OceanAws#monitoring}.'''
        result = self._values.get("monitoring")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#name OceanAws#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#region OceanAws#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#root_volume_size OceanAws#root_volume_size}.'''
        result = self._values.get("root_volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scheduled_task(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsScheduledTask"]]]:
        '''scheduled_task block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#scheduled_task OceanAws#scheduled_task}
        '''
        result = self._values.get("scheduled_task")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsScheduledTask"]]], result)

    @builtins.property
    def spot_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#spot_percentage OceanAws#spot_percentage}.'''
        result = self._values.get("spot_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsTags"]]]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#tags OceanAws#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsTags"]]], result)

    @builtins.property
    def update_policy(self) -> typing.Optional["OceanAwsUpdatePolicy"]:
        '''update_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#update_policy OceanAws#update_policy}
        '''
        result = self._values.get("update_policy")
        return typing.cast(typing.Optional["OceanAwsUpdatePolicy"], result)

    @builtins.property
    def use_as_template_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#use_as_template_only OceanAws#use_as_template_only}.'''
        result = self._values.get("use_as_template_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#user_data OceanAws#user_data}.'''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def utilize_commitments(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#utilize_commitments OceanAws#utilize_commitments}.'''
        result = self._values.get("utilize_commitments")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def utilize_reserved_instances(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#utilize_reserved_instances OceanAws#utilize_reserved_instances}.'''
        result = self._values.get("utilize_reserved_instances")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def whitelist(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#whitelist OceanAws#whitelist}.'''
        result = self._values.get("whitelist")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAwsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsInstanceMetadataOptions",
    jsii_struct_bases=[],
    name_mapping={
        "http_tokens": "httpTokens",
        "http_put_response_hop_limit": "httpPutResponseHopLimit",
    },
)
class OceanAwsInstanceMetadataOptions:
    def __init__(
        self,
        *,
        http_tokens: builtins.str,
        http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param http_tokens: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#http_tokens OceanAws#http_tokens}.
        :param http_put_response_hop_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#http_put_response_hop_limit OceanAws#http_put_response_hop_limit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsInstanceMetadataOptions.__init__)
            check_type(argname="argument http_tokens", value=http_tokens, expected_type=type_hints["http_tokens"])
            check_type(argname="argument http_put_response_hop_limit", value=http_put_response_hop_limit, expected_type=type_hints["http_put_response_hop_limit"])
        self._values: typing.Dict[str, typing.Any] = {
            "http_tokens": http_tokens,
        }
        if http_put_response_hop_limit is not None:
            self._values["http_put_response_hop_limit"] = http_put_response_hop_limit

    @builtins.property
    def http_tokens(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#http_tokens OceanAws#http_tokens}.'''
        result = self._values.get("http_tokens")
        assert result is not None, "Required property 'http_tokens' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def http_put_response_hop_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#http_put_response_hop_limit OceanAws#http_put_response_hop_limit}.'''
        result = self._values.get("http_put_response_hop_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAwsInstanceMetadataOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAwsInstanceMetadataOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsInstanceMetadataOptionsOutputReference",
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
            type_hints = typing.get_type_hints(OceanAwsInstanceMetadataOptionsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsInstanceMetadataOptionsOutputReference, "http_put_response_hop_limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpPutResponseHopLimit", value)

    @builtins.property
    @jsii.member(jsii_name="httpTokens")
    def http_tokens(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpTokens"))

    @http_tokens.setter
    def http_tokens(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsInstanceMetadataOptionsOutputReference, "http_tokens").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpTokens", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanAwsInstanceMetadataOptions]:
        return typing.cast(typing.Optional[OceanAwsInstanceMetadataOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanAwsInstanceMetadataOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsInstanceMetadataOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsLoadBalancers",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "name": "name", "type": "type"},
)
class OceanAwsLoadBalancers:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#arn OceanAws#arn}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#name OceanAws#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#type OceanAws#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsLoadBalancers.__init__)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#arn OceanAws#arn}.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#name OceanAws#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#type OceanAws#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAwsLoadBalancers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAwsLoadBalancersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsLoadBalancersList",
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
            type_hints = typing.get_type_hints(OceanAwsLoadBalancersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanAwsLoadBalancersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsLoadBalancersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAwsLoadBalancersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsLoadBalancersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsLoadBalancersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsLoadBalancersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAwsLoadBalancers]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAwsLoadBalancers]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAwsLoadBalancers]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsLoadBalancersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAwsLoadBalancersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsLoadBalancersOutputReference",
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
            type_hints = typing.get_type_hints(OceanAwsLoadBalancersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetArn")
    def reset_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArn", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

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
            type_hints = typing.get_type_hints(getattr(OceanAwsLoadBalancersOutputReference, "arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsLoadBalancersOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsLoadBalancersOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAwsLoadBalancers, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAwsLoadBalancers, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAwsLoadBalancers, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsLoadBalancersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsLogging",
    jsii_struct_bases=[],
    name_mapping={"export": "export"},
)
class OceanAwsLogging:
    def __init__(
        self,
        *,
        export: typing.Optional[typing.Union["OceanAwsLoggingExport", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param export: export block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#export OceanAws#export}
        '''
        if isinstance(export, dict):
            export = OceanAwsLoggingExport(**export)
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsLogging.__init__)
            check_type(argname="argument export", value=export, expected_type=type_hints["export"])
        self._values: typing.Dict[str, typing.Any] = {}
        if export is not None:
            self._values["export"] = export

    @builtins.property
    def export(self) -> typing.Optional["OceanAwsLoggingExport"]:
        '''export block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#export OceanAws#export}
        '''
        result = self._values.get("export")
        return typing.cast(typing.Optional["OceanAwsLoggingExport"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAwsLogging(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsLoggingExport",
    jsii_struct_bases=[],
    name_mapping={"s3": "s3"},
)
class OceanAwsLoggingExport:
    def __init__(
        self,
        *,
        s3: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAwsLoggingExportS3", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#s3 OceanAws#s3}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsLoggingExport.__init__)
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
        self._values: typing.Dict[str, typing.Any] = {}
        if s3 is not None:
            self._values["s3"] = s3

    @builtins.property
    def s3(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsLoggingExportS3"]]]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#s3 OceanAws#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsLoggingExportS3"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAwsLoggingExport(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAwsLoggingExportOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsLoggingExportOutputReference",
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
            type_hints = typing.get_type_hints(OceanAwsLoggingExportOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAwsLoggingExportS3", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsLoggingExportOutputReference.put_s3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "OceanAwsLoggingExportS3List":
        return typing.cast("OceanAwsLoggingExportS3List", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsLoggingExportS3"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsLoggingExportS3"]]], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanAwsLoggingExport]:
        return typing.cast(typing.Optional[OceanAwsLoggingExport], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OceanAwsLoggingExport]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsLoggingExportOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsLoggingExportS3",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class OceanAwsLoggingExportS3:
    def __init__(self, *, id: builtins.str) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#id OceanAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsLoggingExportS3.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#id OceanAws#id}.

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
        return "OceanAwsLoggingExportS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAwsLoggingExportS3List(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsLoggingExportS3List",
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
            type_hints = typing.get_type_hints(OceanAwsLoggingExportS3List.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanAwsLoggingExportS3OutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsLoggingExportS3List.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAwsLoggingExportS3OutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsLoggingExportS3List, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsLoggingExportS3List, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsLoggingExportS3List, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAwsLoggingExportS3]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAwsLoggingExportS3]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAwsLoggingExportS3]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsLoggingExportS3List, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAwsLoggingExportS3OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsLoggingExportS3OutputReference",
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
            type_hints = typing.get_type_hints(OceanAwsLoggingExportS3OutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsLoggingExportS3OutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAwsLoggingExportS3, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAwsLoggingExportS3, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAwsLoggingExportS3, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsLoggingExportS3OutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAwsLoggingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsLoggingOutputReference",
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
            type_hints = typing.get_type_hints(OceanAwsLoggingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putExport")
    def put_export(
        self,
        *,
        s3: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OceanAwsLoggingExportS3, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#s3 OceanAws#s3}
        '''
        value = OceanAwsLoggingExport(s3=s3)

        return typing.cast(None, jsii.invoke(self, "putExport", [value]))

    @jsii.member(jsii_name="resetExport")
    def reset_export(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExport", []))

    @builtins.property
    @jsii.member(jsii_name="export")
    def export(self) -> OceanAwsLoggingExportOutputReference:
        return typing.cast(OceanAwsLoggingExportOutputReference, jsii.get(self, "export"))

    @builtins.property
    @jsii.member(jsii_name="exportInput")
    def export_input(self) -> typing.Optional[OceanAwsLoggingExport]:
        return typing.cast(typing.Optional[OceanAwsLoggingExport], jsii.get(self, "exportInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanAwsLogging]:
        return typing.cast(typing.Optional[OceanAwsLogging], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OceanAwsLogging]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsLoggingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsScheduledTask",
    jsii_struct_bases=[],
    name_mapping={"shutdown_hours": "shutdownHours", "tasks": "tasks"},
)
class OceanAwsScheduledTask:
    def __init__(
        self,
        *,
        shutdown_hours: typing.Optional[typing.Union["OceanAwsScheduledTaskShutdownHours", typing.Dict[str, typing.Any]]] = None,
        tasks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAwsScheduledTaskTasks", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param shutdown_hours: shutdown_hours block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#shutdown_hours OceanAws#shutdown_hours}
        :param tasks: tasks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#tasks OceanAws#tasks}
        '''
        if isinstance(shutdown_hours, dict):
            shutdown_hours = OceanAwsScheduledTaskShutdownHours(**shutdown_hours)
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsScheduledTask.__init__)
            check_type(argname="argument shutdown_hours", value=shutdown_hours, expected_type=type_hints["shutdown_hours"])
            check_type(argname="argument tasks", value=tasks, expected_type=type_hints["tasks"])
        self._values: typing.Dict[str, typing.Any] = {}
        if shutdown_hours is not None:
            self._values["shutdown_hours"] = shutdown_hours
        if tasks is not None:
            self._values["tasks"] = tasks

    @builtins.property
    def shutdown_hours(self) -> typing.Optional["OceanAwsScheduledTaskShutdownHours"]:
        '''shutdown_hours block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#shutdown_hours OceanAws#shutdown_hours}
        '''
        result = self._values.get("shutdown_hours")
        return typing.cast(typing.Optional["OceanAwsScheduledTaskShutdownHours"], result)

    @builtins.property
    def tasks(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsScheduledTaskTasks"]]]:
        '''tasks block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#tasks OceanAws#tasks}
        '''
        result = self._values.get("tasks")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsScheduledTaskTasks"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAwsScheduledTask(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAwsScheduledTaskList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsScheduledTaskList",
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
            type_hints = typing.get_type_hints(OceanAwsScheduledTaskList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanAwsScheduledTaskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsScheduledTaskList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAwsScheduledTaskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsScheduledTaskList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsScheduledTaskList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsScheduledTaskList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAwsScheduledTask]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAwsScheduledTask]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAwsScheduledTask]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsScheduledTaskList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAwsScheduledTaskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsScheduledTaskOutputReference",
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
            type_hints = typing.get_type_hints(OceanAwsScheduledTaskOutputReference.__init__)
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
        :param time_windows: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#time_windows OceanAws#time_windows}.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#is_enabled OceanAws#is_enabled}.
        '''
        value = OceanAwsScheduledTaskShutdownHours(
            time_windows=time_windows, is_enabled=is_enabled
        )

        return typing.cast(None, jsii.invoke(self, "putShutdownHours", [value]))

    @jsii.member(jsii_name="putTasks")
    def put_tasks(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAwsScheduledTaskTasks", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsScheduledTaskOutputReference.put_tasks)
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
    def shutdown_hours(self) -> "OceanAwsScheduledTaskShutdownHoursOutputReference":
        return typing.cast("OceanAwsScheduledTaskShutdownHoursOutputReference", jsii.get(self, "shutdownHours"))

    @builtins.property
    @jsii.member(jsii_name="tasks")
    def tasks(self) -> "OceanAwsScheduledTaskTasksList":
        return typing.cast("OceanAwsScheduledTaskTasksList", jsii.get(self, "tasks"))

    @builtins.property
    @jsii.member(jsii_name="shutdownHoursInput")
    def shutdown_hours_input(
        self,
    ) -> typing.Optional["OceanAwsScheduledTaskShutdownHours"]:
        return typing.cast(typing.Optional["OceanAwsScheduledTaskShutdownHours"], jsii.get(self, "shutdownHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="tasksInput")
    def tasks_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsScheduledTaskTasks"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAwsScheduledTaskTasks"]]], jsii.get(self, "tasksInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAwsScheduledTask, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAwsScheduledTask, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAwsScheduledTask, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsScheduledTaskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsScheduledTaskShutdownHours",
    jsii_struct_bases=[],
    name_mapping={"time_windows": "timeWindows", "is_enabled": "isEnabled"},
)
class OceanAwsScheduledTaskShutdownHours:
    def __init__(
        self,
        *,
        time_windows: typing.Sequence[builtins.str],
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param time_windows: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#time_windows OceanAws#time_windows}.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#is_enabled OceanAws#is_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsScheduledTaskShutdownHours.__init__)
            check_type(argname="argument time_windows", value=time_windows, expected_type=type_hints["time_windows"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "time_windows": time_windows,
        }
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled

    @builtins.property
    def time_windows(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#time_windows OceanAws#time_windows}.'''
        result = self._values.get("time_windows")
        assert result is not None, "Required property 'time_windows' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#is_enabled OceanAws#is_enabled}.'''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAwsScheduledTaskShutdownHours(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAwsScheduledTaskShutdownHoursOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsScheduledTaskShutdownHoursOutputReference",
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
            type_hints = typing.get_type_hints(OceanAwsScheduledTaskShutdownHoursOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsScheduledTaskShutdownHoursOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="timeWindows")
    def time_windows(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "timeWindows"))

    @time_windows.setter
    def time_windows(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsScheduledTaskShutdownHoursOutputReference, "time_windows").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeWindows", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanAwsScheduledTaskShutdownHours]:
        return typing.cast(typing.Optional[OceanAwsScheduledTaskShutdownHours], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanAwsScheduledTaskShutdownHours],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsScheduledTaskShutdownHoursOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsScheduledTaskTasks",
    jsii_struct_bases=[],
    name_mapping={
        "cron_expression": "cronExpression",
        "is_enabled": "isEnabled",
        "task_type": "taskType",
    },
)
class OceanAwsScheduledTaskTasks:
    def __init__(
        self,
        *,
        cron_expression: builtins.str,
        is_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        task_type: builtins.str,
    ) -> None:
        '''
        :param cron_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#cron_expression OceanAws#cron_expression}.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#is_enabled OceanAws#is_enabled}.
        :param task_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#task_type OceanAws#task_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsScheduledTaskTasks.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#cron_expression OceanAws#cron_expression}.'''
        result = self._values.get("cron_expression")
        assert result is not None, "Required property 'cron_expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#is_enabled OceanAws#is_enabled}.'''
        result = self._values.get("is_enabled")
        assert result is not None, "Required property 'is_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def task_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#task_type OceanAws#task_type}.'''
        result = self._values.get("task_type")
        assert result is not None, "Required property 'task_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAwsScheduledTaskTasks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAwsScheduledTaskTasksList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsScheduledTaskTasksList",
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
            type_hints = typing.get_type_hints(OceanAwsScheduledTaskTasksList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanAwsScheduledTaskTasksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsScheduledTaskTasksList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAwsScheduledTaskTasksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsScheduledTaskTasksList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsScheduledTaskTasksList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsScheduledTaskTasksList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAwsScheduledTaskTasks]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAwsScheduledTaskTasks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAwsScheduledTaskTasks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsScheduledTaskTasksList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAwsScheduledTaskTasksOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsScheduledTaskTasksOutputReference",
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
            type_hints = typing.get_type_hints(OceanAwsScheduledTaskTasksOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsScheduledTaskTasksOutputReference, "cron_expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cronExpression", value)

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsScheduledTaskTasksOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="taskType")
    def task_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskType"))

    @task_type.setter
    def task_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsScheduledTaskTasksOutputReference, "task_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAwsScheduledTaskTasks, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAwsScheduledTaskTasks, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAwsScheduledTaskTasks, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsScheduledTaskTasksOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class OceanAwsTags:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#key OceanAws#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#value OceanAws#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsTags.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#key OceanAws#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#value OceanAws#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAwsTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAwsTagsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsTagsList",
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
            type_hints = typing.get_type_hints(OceanAwsTagsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanAwsTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsTagsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAwsTagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsTagsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsTagsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsTagsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAwsTags]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAwsTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAwsTags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsTagsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAwsTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsTagsOutputReference",
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
            type_hints = typing.get_type_hints(OceanAwsTagsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsTagsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsTagsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAwsTags, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAwsTags, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAwsTags, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsTagsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsUpdatePolicy",
    jsii_struct_bases=[],
    name_mapping={
        "should_roll": "shouldRoll",
        "auto_apply_tags": "autoApplyTags",
        "conditioned_roll": "conditionedRoll",
        "roll_config": "rollConfig",
    },
)
class OceanAwsUpdatePolicy:
    def __init__(
        self,
        *,
        should_roll: typing.Union[builtins.bool, cdktf.IResolvable],
        auto_apply_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        conditioned_roll: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        roll_config: typing.Optional[typing.Union["OceanAwsUpdatePolicyRollConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param should_roll: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#should_roll OceanAws#should_roll}.
        :param auto_apply_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#auto_apply_tags OceanAws#auto_apply_tags}.
        :param conditioned_roll: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#conditioned_roll OceanAws#conditioned_roll}.
        :param roll_config: roll_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#roll_config OceanAws#roll_config}
        '''
        if isinstance(roll_config, dict):
            roll_config = OceanAwsUpdatePolicyRollConfig(**roll_config)
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsUpdatePolicy.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#should_roll OceanAws#should_roll}.'''
        result = self._values.get("should_roll")
        assert result is not None, "Required property 'should_roll' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def auto_apply_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#auto_apply_tags OceanAws#auto_apply_tags}.'''
        result = self._values.get("auto_apply_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def conditioned_roll(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#conditioned_roll OceanAws#conditioned_roll}.'''
        result = self._values.get("conditioned_roll")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def roll_config(self) -> typing.Optional["OceanAwsUpdatePolicyRollConfig"]:
        '''roll_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#roll_config OceanAws#roll_config}
        '''
        result = self._values.get("roll_config")
        return typing.cast(typing.Optional["OceanAwsUpdatePolicyRollConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAwsUpdatePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAwsUpdatePolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsUpdatePolicyOutputReference",
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
            type_hints = typing.get_type_hints(OceanAwsUpdatePolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRollConfig")
    def put_roll_config(
        self,
        *,
        batch_size_percentage: jsii.Number,
        batch_min_healthy_percentage: typing.Optional[jsii.Number] = None,
        launch_spec_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        respect_pdb: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param batch_size_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#batch_size_percentage OceanAws#batch_size_percentage}.
        :param batch_min_healthy_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#batch_min_healthy_percentage OceanAws#batch_min_healthy_percentage}.
        :param launch_spec_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#launch_spec_ids OceanAws#launch_spec_ids}.
        :param respect_pdb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#respect_pdb OceanAws#respect_pdb}.
        '''
        value = OceanAwsUpdatePolicyRollConfig(
            batch_size_percentage=batch_size_percentage,
            batch_min_healthy_percentage=batch_min_healthy_percentage,
            launch_spec_ids=launch_spec_ids,
            respect_pdb=respect_pdb,
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
    def roll_config(self) -> "OceanAwsUpdatePolicyRollConfigOutputReference":
        return typing.cast("OceanAwsUpdatePolicyRollConfigOutputReference", jsii.get(self, "rollConfig"))

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
    def roll_config_input(self) -> typing.Optional["OceanAwsUpdatePolicyRollConfig"]:
        return typing.cast(typing.Optional["OceanAwsUpdatePolicyRollConfig"], jsii.get(self, "rollConfigInput"))

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
            type_hints = typing.get_type_hints(getattr(OceanAwsUpdatePolicyOutputReference, "auto_apply_tags").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsUpdatePolicyOutputReference, "conditioned_roll").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAwsUpdatePolicyOutputReference, "should_roll").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shouldRoll", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanAwsUpdatePolicy]:
        return typing.cast(typing.Optional[OceanAwsUpdatePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OceanAwsUpdatePolicy]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsUpdatePolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsUpdatePolicyRollConfig",
    jsii_struct_bases=[],
    name_mapping={
        "batch_size_percentage": "batchSizePercentage",
        "batch_min_healthy_percentage": "batchMinHealthyPercentage",
        "launch_spec_ids": "launchSpecIds",
        "respect_pdb": "respectPdb",
    },
)
class OceanAwsUpdatePolicyRollConfig:
    def __init__(
        self,
        *,
        batch_size_percentage: jsii.Number,
        batch_min_healthy_percentage: typing.Optional[jsii.Number] = None,
        launch_spec_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        respect_pdb: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param batch_size_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#batch_size_percentage OceanAws#batch_size_percentage}.
        :param batch_min_healthy_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#batch_min_healthy_percentage OceanAws#batch_min_healthy_percentage}.
        :param launch_spec_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#launch_spec_ids OceanAws#launch_spec_ids}.
        :param respect_pdb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#respect_pdb OceanAws#respect_pdb}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAwsUpdatePolicyRollConfig.__init__)
            check_type(argname="argument batch_size_percentage", value=batch_size_percentage, expected_type=type_hints["batch_size_percentage"])
            check_type(argname="argument batch_min_healthy_percentage", value=batch_min_healthy_percentage, expected_type=type_hints["batch_min_healthy_percentage"])
            check_type(argname="argument launch_spec_ids", value=launch_spec_ids, expected_type=type_hints["launch_spec_ids"])
            check_type(argname="argument respect_pdb", value=respect_pdb, expected_type=type_hints["respect_pdb"])
        self._values: typing.Dict[str, typing.Any] = {
            "batch_size_percentage": batch_size_percentage,
        }
        if batch_min_healthy_percentage is not None:
            self._values["batch_min_healthy_percentage"] = batch_min_healthy_percentage
        if launch_spec_ids is not None:
            self._values["launch_spec_ids"] = launch_spec_ids
        if respect_pdb is not None:
            self._values["respect_pdb"] = respect_pdb

    @builtins.property
    def batch_size_percentage(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#batch_size_percentage OceanAws#batch_size_percentage}.'''
        result = self._values.get("batch_size_percentage")
        assert result is not None, "Required property 'batch_size_percentage' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def batch_min_healthy_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#batch_min_healthy_percentage OceanAws#batch_min_healthy_percentage}.'''
        result = self._values.get("batch_min_healthy_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def launch_spec_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#launch_spec_ids OceanAws#launch_spec_ids}.'''
        result = self._values.get("launch_spec_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def respect_pdb(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aws#respect_pdb OceanAws#respect_pdb}.'''
        result = self._values.get("respect_pdb")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAwsUpdatePolicyRollConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAwsUpdatePolicyRollConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAws.OceanAwsUpdatePolicyRollConfigOutputReference",
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
            type_hints = typing.get_type_hints(OceanAwsUpdatePolicyRollConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBatchMinHealthyPercentage")
    def reset_batch_min_healthy_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBatchMinHealthyPercentage", []))

    @jsii.member(jsii_name="resetLaunchSpecIds")
    def reset_launch_spec_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchSpecIds", []))

    @jsii.member(jsii_name="resetRespectPdb")
    def reset_respect_pdb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRespectPdb", []))

    @builtins.property
    @jsii.member(jsii_name="batchMinHealthyPercentageInput")
    def batch_min_healthy_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "batchMinHealthyPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="batchSizePercentageInput")
    def batch_size_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "batchSizePercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="launchSpecIdsInput")
    def launch_spec_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "launchSpecIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="respectPdbInput")
    def respect_pdb_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "respectPdbInput"))

    @builtins.property
    @jsii.member(jsii_name="batchMinHealthyPercentage")
    def batch_min_healthy_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "batchMinHealthyPercentage"))

    @batch_min_healthy_percentage.setter
    def batch_min_healthy_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsUpdatePolicyRollConfigOutputReference, "batch_min_healthy_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchMinHealthyPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="batchSizePercentage")
    def batch_size_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "batchSizePercentage"))

    @batch_size_percentage.setter
    def batch_size_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsUpdatePolicyRollConfigOutputReference, "batch_size_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchSizePercentage", value)

    @builtins.property
    @jsii.member(jsii_name="launchSpecIds")
    def launch_spec_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "launchSpecIds"))

    @launch_spec_ids.setter
    def launch_spec_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsUpdatePolicyRollConfigOutputReference, "launch_spec_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchSpecIds", value)

    @builtins.property
    @jsii.member(jsii_name="respectPdb")
    def respect_pdb(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "respectPdb"))

    @respect_pdb.setter
    def respect_pdb(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsUpdatePolicyRollConfigOutputReference, "respect_pdb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "respectPdb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OceanAwsUpdatePolicyRollConfig]:
        return typing.cast(typing.Optional[OceanAwsUpdatePolicyRollConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanAwsUpdatePolicyRollConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAwsUpdatePolicyRollConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "OceanAws",
    "OceanAwsAutoscaler",
    "OceanAwsAutoscalerAutoscaleDown",
    "OceanAwsAutoscalerAutoscaleDownOutputReference",
    "OceanAwsAutoscalerAutoscaleHeadroom",
    "OceanAwsAutoscalerAutoscaleHeadroomOutputReference",
    "OceanAwsAutoscalerOutputReference",
    "OceanAwsAutoscalerResourceLimits",
    "OceanAwsAutoscalerResourceLimitsOutputReference",
    "OceanAwsConfig",
    "OceanAwsInstanceMetadataOptions",
    "OceanAwsInstanceMetadataOptionsOutputReference",
    "OceanAwsLoadBalancers",
    "OceanAwsLoadBalancersList",
    "OceanAwsLoadBalancersOutputReference",
    "OceanAwsLogging",
    "OceanAwsLoggingExport",
    "OceanAwsLoggingExportOutputReference",
    "OceanAwsLoggingExportS3",
    "OceanAwsLoggingExportS3List",
    "OceanAwsLoggingExportS3OutputReference",
    "OceanAwsLoggingOutputReference",
    "OceanAwsScheduledTask",
    "OceanAwsScheduledTaskList",
    "OceanAwsScheduledTaskOutputReference",
    "OceanAwsScheduledTaskShutdownHours",
    "OceanAwsScheduledTaskShutdownHoursOutputReference",
    "OceanAwsScheduledTaskTasks",
    "OceanAwsScheduledTaskTasksList",
    "OceanAwsScheduledTaskTasksOutputReference",
    "OceanAwsTags",
    "OceanAwsTagsList",
    "OceanAwsTagsOutputReference",
    "OceanAwsUpdatePolicy",
    "OceanAwsUpdatePolicyOutputReference",
    "OceanAwsUpdatePolicyRollConfig",
    "OceanAwsUpdatePolicyRollConfigOutputReference",
]

publication.publish()
