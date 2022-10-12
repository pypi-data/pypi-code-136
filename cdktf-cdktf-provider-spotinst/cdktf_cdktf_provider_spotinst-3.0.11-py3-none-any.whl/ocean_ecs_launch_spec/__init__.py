'''
# `spotinst_ocean_ecs_launch_spec`

Refer to the Terraform Registory for docs: [`spotinst_ocean_ecs_launch_spec`](https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec).
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


class OceanEcsLaunchSpec(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpec",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec spotinst_ocean_ecs_launch_spec}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        ocean_id: builtins.str,
        attributes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsLaunchSpecAttributes", typing.Dict[str, typing.Any]]]]] = None,
        autoscale_headrooms: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsLaunchSpecAutoscaleHeadrooms", typing.Dict[str, typing.Any]]]]] = None,
        block_device_mappings: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsLaunchSpecBlockDeviceMappings", typing.Dict[str, typing.Any]]]]] = None,
        iam_instance_profile: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        image_id: typing.Optional[builtins.str] = None,
        instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        preferred_spot_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        restrict_scale_down: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        scheduling_task: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsLaunchSpecSchedulingTask", typing.Dict[str, typing.Any]]]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsLaunchSpecTags", typing.Dict[str, typing.Any]]]]] = None,
        user_data: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec spotinst_ocean_ecs_launch_spec} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#name OceanEcsLaunchSpec#name}.
        :param ocean_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#ocean_id OceanEcsLaunchSpec#ocean_id}.
        :param attributes: attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#attributes OceanEcsLaunchSpec#attributes}
        :param autoscale_headrooms: autoscale_headrooms block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#autoscale_headrooms OceanEcsLaunchSpec#autoscale_headrooms}
        :param block_device_mappings: block_device_mappings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#block_device_mappings OceanEcsLaunchSpec#block_device_mappings}
        :param iam_instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#iam_instance_profile OceanEcsLaunchSpec#iam_instance_profile}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#id OceanEcsLaunchSpec#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#image_id OceanEcsLaunchSpec#image_id}.
        :param instance_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#instance_types OceanEcsLaunchSpec#instance_types}.
        :param preferred_spot_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#preferred_spot_types OceanEcsLaunchSpec#preferred_spot_types}.
        :param restrict_scale_down: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#restrict_scale_down OceanEcsLaunchSpec#restrict_scale_down}.
        :param scheduling_task: scheduling_task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#scheduling_task OceanEcsLaunchSpec#scheduling_task}
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#security_group_ids OceanEcsLaunchSpec#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#subnet_ids OceanEcsLaunchSpec#subnet_ids}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#tags OceanEcsLaunchSpec#tags}
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#user_data OceanEcsLaunchSpec#user_data}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpec.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OceanEcsLaunchSpecConfig(
            name=name,
            ocean_id=ocean_id,
            attributes=attributes,
            autoscale_headrooms=autoscale_headrooms,
            block_device_mappings=block_device_mappings,
            iam_instance_profile=iam_instance_profile,
            id=id,
            image_id=image_id,
            instance_types=instance_types,
            preferred_spot_types=preferred_spot_types,
            restrict_scale_down=restrict_scale_down,
            scheduling_task=scheduling_task,
            security_group_ids=security_group_ids,
            subnet_ids=subnet_ids,
            tags=tags,
            user_data=user_data,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAttributes")
    def put_attributes(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsLaunchSpecAttributes", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpec.put_attributes)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAttributes", [value]))

    @jsii.member(jsii_name="putAutoscaleHeadrooms")
    def put_autoscale_headrooms(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsLaunchSpecAutoscaleHeadrooms", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpec.put_autoscale_headrooms)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAutoscaleHeadrooms", [value]))

    @jsii.member(jsii_name="putBlockDeviceMappings")
    def put_block_device_mappings(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsLaunchSpecBlockDeviceMappings", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpec.put_block_device_mappings)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBlockDeviceMappings", [value]))

    @jsii.member(jsii_name="putSchedulingTask")
    def put_scheduling_task(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsLaunchSpecSchedulingTask", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpec.put_scheduling_task)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSchedulingTask", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsLaunchSpecTags", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpec.put_tags)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetAttributes")
    def reset_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributes", []))

    @jsii.member(jsii_name="resetAutoscaleHeadrooms")
    def reset_autoscale_headrooms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaleHeadrooms", []))

    @jsii.member(jsii_name="resetBlockDeviceMappings")
    def reset_block_device_mappings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockDeviceMappings", []))

    @jsii.member(jsii_name="resetIamInstanceProfile")
    def reset_iam_instance_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamInstanceProfile", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImageId")
    def reset_image_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageId", []))

    @jsii.member(jsii_name="resetInstanceTypes")
    def reset_instance_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceTypes", []))

    @jsii.member(jsii_name="resetPreferredSpotTypes")
    def reset_preferred_spot_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredSpotTypes", []))

    @jsii.member(jsii_name="resetRestrictScaleDown")
    def reset_restrict_scale_down(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestrictScaleDown", []))

    @jsii.member(jsii_name="resetSchedulingTask")
    def reset_scheduling_task(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedulingTask", []))

    @jsii.member(jsii_name="resetSecurityGroupIds")
    def reset_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroupIds", []))

    @jsii.member(jsii_name="resetSubnetIds")
    def reset_subnet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetIds", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetUserData")
    def reset_user_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserData", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> "OceanEcsLaunchSpecAttributesList":
        return typing.cast("OceanEcsLaunchSpecAttributesList", jsii.get(self, "attributes"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleHeadrooms")
    def autoscale_headrooms(self) -> "OceanEcsLaunchSpecAutoscaleHeadroomsList":
        return typing.cast("OceanEcsLaunchSpecAutoscaleHeadroomsList", jsii.get(self, "autoscaleHeadrooms"))

    @builtins.property
    @jsii.member(jsii_name="blockDeviceMappings")
    def block_device_mappings(self) -> "OceanEcsLaunchSpecBlockDeviceMappingsList":
        return typing.cast("OceanEcsLaunchSpecBlockDeviceMappingsList", jsii.get(self, "blockDeviceMappings"))

    @builtins.property
    @jsii.member(jsii_name="schedulingTask")
    def scheduling_task(self) -> "OceanEcsLaunchSpecSchedulingTaskList":
        return typing.cast("OceanEcsLaunchSpecSchedulingTaskList", jsii.get(self, "schedulingTask"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "OceanEcsLaunchSpecTagsList":
        return typing.cast("OceanEcsLaunchSpecTagsList", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="attributesInput")
    def attributes_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLaunchSpecAttributes"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLaunchSpecAttributes"]]], jsii.get(self, "attributesInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleHeadroomsInput")
    def autoscale_headrooms_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLaunchSpecAutoscaleHeadrooms"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLaunchSpecAutoscaleHeadrooms"]]], jsii.get(self, "autoscaleHeadroomsInput"))

    @builtins.property
    @jsii.member(jsii_name="blockDeviceMappingsInput")
    def block_device_mappings_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLaunchSpecBlockDeviceMappings"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLaunchSpecBlockDeviceMappings"]]], jsii.get(self, "blockDeviceMappingsInput"))

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
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="oceanIdInput")
    def ocean_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oceanIdInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredSpotTypesInput")
    def preferred_spot_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "preferredSpotTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="restrictScaleDownInput")
    def restrict_scale_down_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "restrictScaleDownInput"))

    @builtins.property
    @jsii.member(jsii_name="schedulingTaskInput")
    def scheduling_task_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLaunchSpecSchedulingTask"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLaunchSpecSchedulingTask"]]], jsii.get(self, "schedulingTaskInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLaunchSpecTags"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLaunchSpecTags"]]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="userDataInput")
    def user_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userDataInput"))

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfile")
    def iam_instance_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamInstanceProfile"))

    @iam_instance_profile.setter
    def iam_instance_profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpec, "iam_instance_profile").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamInstanceProfile", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpec, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="imageId")
    def image_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageId"))

    @image_id.setter
    def image_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpec, "image_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageId", value)

    @builtins.property
    @jsii.member(jsii_name="instanceTypes")
    def instance_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceTypes"))

    @instance_types.setter
    def instance_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpec, "instance_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceTypes", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpec, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="oceanId")
    def ocean_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oceanId"))

    @ocean_id.setter
    def ocean_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpec, "ocean_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oceanId", value)

    @builtins.property
    @jsii.member(jsii_name="preferredSpotTypes")
    def preferred_spot_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "preferredSpotTypes"))

    @preferred_spot_types.setter
    def preferred_spot_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpec, "preferred_spot_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredSpotTypes", value)

    @builtins.property
    @jsii.member(jsii_name="restrictScaleDown")
    def restrict_scale_down(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "restrictScaleDown"))

    @restrict_scale_down.setter
    def restrict_scale_down(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpec, "restrict_scale_down").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restrictScaleDown", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpec, "security_group_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpec, "subnet_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userData"))

    @user_data.setter
    def user_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpec, "user_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userData", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecAttributes",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class OceanEcsLaunchSpecAttributes:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#key OceanEcsLaunchSpec#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#value OceanEcsLaunchSpec#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecAttributes.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#key OceanEcsLaunchSpec#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#value OceanEcsLaunchSpec#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsLaunchSpecAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsLaunchSpecAttributesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecAttributesList",
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
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecAttributesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanEcsLaunchSpecAttributesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecAttributesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanEcsLaunchSpecAttributesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecAttributesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecAttributesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecAttributesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecAttributes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecAttributes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecAttributes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecAttributesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanEcsLaunchSpecAttributesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecAttributesOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecAttributesOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecAttributesOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecAttributesOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanEcsLaunchSpecAttributes, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanEcsLaunchSpecAttributes, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanEcsLaunchSpecAttributes, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecAttributesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecAutoscaleHeadrooms",
    jsii_struct_bases=[],
    name_mapping={
        "num_of_units": "numOfUnits",
        "cpu_per_unit": "cpuPerUnit",
        "memory_per_unit": "memoryPerUnit",
    },
)
class OceanEcsLaunchSpecAutoscaleHeadrooms:
    def __init__(
        self,
        *,
        num_of_units: jsii.Number,
        cpu_per_unit: typing.Optional[jsii.Number] = None,
        memory_per_unit: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param num_of_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#num_of_units OceanEcsLaunchSpec#num_of_units}.
        :param cpu_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#cpu_per_unit OceanEcsLaunchSpec#cpu_per_unit}.
        :param memory_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#memory_per_unit OceanEcsLaunchSpec#memory_per_unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecAutoscaleHeadrooms.__init__)
            check_type(argname="argument num_of_units", value=num_of_units, expected_type=type_hints["num_of_units"])
            check_type(argname="argument cpu_per_unit", value=cpu_per_unit, expected_type=type_hints["cpu_per_unit"])
            check_type(argname="argument memory_per_unit", value=memory_per_unit, expected_type=type_hints["memory_per_unit"])
        self._values: typing.Dict[str, typing.Any] = {
            "num_of_units": num_of_units,
        }
        if cpu_per_unit is not None:
            self._values["cpu_per_unit"] = cpu_per_unit
        if memory_per_unit is not None:
            self._values["memory_per_unit"] = memory_per_unit

    @builtins.property
    def num_of_units(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#num_of_units OceanEcsLaunchSpec#num_of_units}.'''
        result = self._values.get("num_of_units")
        assert result is not None, "Required property 'num_of_units' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def cpu_per_unit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#cpu_per_unit OceanEcsLaunchSpec#cpu_per_unit}.'''
        result = self._values.get("cpu_per_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_per_unit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#memory_per_unit OceanEcsLaunchSpec#memory_per_unit}.'''
        result = self._values.get("memory_per_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsLaunchSpecAutoscaleHeadrooms(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsLaunchSpecAutoscaleHeadroomsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecAutoscaleHeadroomsList",
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
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecAutoscaleHeadroomsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OceanEcsLaunchSpecAutoscaleHeadroomsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecAutoscaleHeadroomsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanEcsLaunchSpecAutoscaleHeadroomsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecAutoscaleHeadroomsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecAutoscaleHeadroomsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecAutoscaleHeadroomsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecAutoscaleHeadrooms]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecAutoscaleHeadrooms]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecAutoscaleHeadrooms]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecAutoscaleHeadroomsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanEcsLaunchSpecAutoscaleHeadroomsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecAutoscaleHeadroomsOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecAutoscaleHeadroomsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCpuPerUnit")
    def reset_cpu_per_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuPerUnit", []))

    @jsii.member(jsii_name="resetMemoryPerUnit")
    def reset_memory_per_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryPerUnit", []))

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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecAutoscaleHeadroomsOutputReference, "cpu_per_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuPerUnit", value)

    @builtins.property
    @jsii.member(jsii_name="memoryPerUnit")
    def memory_per_unit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryPerUnit"))

    @memory_per_unit.setter
    def memory_per_unit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecAutoscaleHeadroomsOutputReference, "memory_per_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryPerUnit", value)

    @builtins.property
    @jsii.member(jsii_name="numOfUnits")
    def num_of_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numOfUnits"))

    @num_of_units.setter
    def num_of_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecAutoscaleHeadroomsOutputReference, "num_of_units").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numOfUnits", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanEcsLaunchSpecAutoscaleHeadrooms, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanEcsLaunchSpecAutoscaleHeadrooms, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanEcsLaunchSpecAutoscaleHeadrooms, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecAutoscaleHeadroomsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecBlockDeviceMappings",
    jsii_struct_bases=[],
    name_mapping={
        "device_name": "deviceName",
        "ebs": "ebs",
        "no_device": "noDevice",
        "virtual_name": "virtualName",
    },
)
class OceanEcsLaunchSpecBlockDeviceMappings:
    def __init__(
        self,
        *,
        device_name: builtins.str,
        ebs: typing.Optional[typing.Union["OceanEcsLaunchSpecBlockDeviceMappingsEbs", typing.Dict[str, typing.Any]]] = None,
        no_device: typing.Optional[builtins.str] = None,
        virtual_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param device_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#device_name OceanEcsLaunchSpec#device_name}.
        :param ebs: ebs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#ebs OceanEcsLaunchSpec#ebs}
        :param no_device: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#no_device OceanEcsLaunchSpec#no_device}.
        :param virtual_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#virtual_name OceanEcsLaunchSpec#virtual_name}.
        '''
        if isinstance(ebs, dict):
            ebs = OceanEcsLaunchSpecBlockDeviceMappingsEbs(**ebs)
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecBlockDeviceMappings.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#device_name OceanEcsLaunchSpec#device_name}.'''
        result = self._values.get("device_name")
        assert result is not None, "Required property 'device_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ebs(self) -> typing.Optional["OceanEcsLaunchSpecBlockDeviceMappingsEbs"]:
        '''ebs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#ebs OceanEcsLaunchSpec#ebs}
        '''
        result = self._values.get("ebs")
        return typing.cast(typing.Optional["OceanEcsLaunchSpecBlockDeviceMappingsEbs"], result)

    @builtins.property
    def no_device(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#no_device OceanEcsLaunchSpec#no_device}.'''
        result = self._values.get("no_device")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#virtual_name OceanEcsLaunchSpec#virtual_name}.'''
        result = self._values.get("virtual_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsLaunchSpecBlockDeviceMappings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecBlockDeviceMappingsEbs",
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
class OceanEcsLaunchSpecBlockDeviceMappingsEbs:
    def __init__(
        self,
        *,
        delete_on_termination: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        dynamic_volume_size: typing.Optional[typing.Union["OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSize", typing.Dict[str, typing.Any]]] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#delete_on_termination OceanEcsLaunchSpec#delete_on_termination}.
        :param dynamic_volume_size: dynamic_volume_size block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#dynamic_volume_size OceanEcsLaunchSpec#dynamic_volume_size}
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#encrypted OceanEcsLaunchSpec#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#iops OceanEcsLaunchSpec#iops}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#kms_key_id OceanEcsLaunchSpec#kms_key_id}.
        :param snapshot_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#snapshot_id OceanEcsLaunchSpec#snapshot_id}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#throughput OceanEcsLaunchSpec#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#volume_size OceanEcsLaunchSpec#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#volume_type OceanEcsLaunchSpec#volume_type}.
        '''
        if isinstance(dynamic_volume_size, dict):
            dynamic_volume_size = OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSize(**dynamic_volume_size)
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecBlockDeviceMappingsEbs.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#delete_on_termination OceanEcsLaunchSpec#delete_on_termination}.'''
        result = self._values.get("delete_on_termination")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def dynamic_volume_size(
        self,
    ) -> typing.Optional["OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSize"]:
        '''dynamic_volume_size block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#dynamic_volume_size OceanEcsLaunchSpec#dynamic_volume_size}
        '''
        result = self._values.get("dynamic_volume_size")
        return typing.cast(typing.Optional["OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSize"], result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#encrypted OceanEcsLaunchSpec#encrypted}.'''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#iops OceanEcsLaunchSpec#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#kms_key_id OceanEcsLaunchSpec#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#snapshot_id OceanEcsLaunchSpec#snapshot_id}.'''
        result = self._values.get("snapshot_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#throughput OceanEcsLaunchSpec#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#volume_size OceanEcsLaunchSpec#volume_size}.'''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#volume_type OceanEcsLaunchSpec#volume_type}.'''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsLaunchSpecBlockDeviceMappingsEbs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSize",
    jsii_struct_bases=[],
    name_mapping={
        "base_size": "baseSize",
        "resource": "resource",
        "size_per_resource_unit": "sizePerResourceUnit",
    },
)
class OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSize:
    def __init__(
        self,
        *,
        base_size: jsii.Number,
        resource: builtins.str,
        size_per_resource_unit: jsii.Number,
    ) -> None:
        '''
        :param base_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#base_size OceanEcsLaunchSpec#base_size}.
        :param resource: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#resource OceanEcsLaunchSpec#resource}.
        :param size_per_resource_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#size_per_resource_unit OceanEcsLaunchSpec#size_per_resource_unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSize.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#base_size OceanEcsLaunchSpec#base_size}.'''
        result = self._values.get("base_size")
        assert result is not None, "Required property 'base_size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def resource(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#resource OceanEcsLaunchSpec#resource}.'''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size_per_resource_unit(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#size_per_resource_unit OceanEcsLaunchSpec#size_per_resource_unit}.'''
        result = self._values.get("size_per_resource_unit")
        assert result is not None, "Required property 'size_per_resource_unit' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference, "base_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseSize", value)

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @resource.setter
    def resource(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference, "resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @builtins.property
    @jsii.member(jsii_name="sizePerResourceUnit")
    def size_per_resource_unit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizePerResourceUnit"))

    @size_per_resource_unit.setter
    def size_per_resource_unit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference, "size_per_resource_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizePerResourceUnit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSize]:
        return typing.cast(typing.Optional[OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSize], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSize],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanEcsLaunchSpecBlockDeviceMappingsEbsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecBlockDeviceMappingsEbsOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecBlockDeviceMappingsEbsOutputReference.__init__)
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
        :param base_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#base_size OceanEcsLaunchSpec#base_size}.
        :param resource: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#resource OceanEcsLaunchSpec#resource}.
        :param size_per_resource_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#size_per_resource_unit OceanEcsLaunchSpec#size_per_resource_unit}.
        '''
        value = OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSize(
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
    ) -> OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference:
        return typing.cast(OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference, jsii.get(self, "dynamicVolumeSize"))

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
    ) -> typing.Optional[OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSize]:
        return typing.cast(typing.Optional[OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSize], jsii.get(self, "dynamicVolumeSizeInput"))

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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsEbsOutputReference, "delete_on_termination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteOnTermination", value)

    @builtins.property
    @jsii.member(jsii_name="encrypted")
    def encrypted(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "encrypted"))

    @encrypted.setter
    def encrypted(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsEbsOutputReference, "encrypted").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsEbsOutputReference, "iops").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsEbsOutputReference, "kms_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotId")
    def snapshot_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotId"))

    @snapshot_id.setter
    def snapshot_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsEbsOutputReference, "snapshot_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotId", value)

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsEbsOutputReference, "throughput").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value)

    @builtins.property
    @jsii.member(jsii_name="volumeSize")
    def volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumeSize"))

    @volume_size.setter
    def volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsEbsOutputReference, "volume_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsEbsOutputReference, "volume_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OceanEcsLaunchSpecBlockDeviceMappingsEbs]:
        return typing.cast(typing.Optional[OceanEcsLaunchSpecBlockDeviceMappingsEbs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanEcsLaunchSpecBlockDeviceMappingsEbs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsEbsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanEcsLaunchSpecBlockDeviceMappingsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecBlockDeviceMappingsList",
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
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecBlockDeviceMappingsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OceanEcsLaunchSpecBlockDeviceMappingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecBlockDeviceMappingsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanEcsLaunchSpecBlockDeviceMappingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecBlockDeviceMappings]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecBlockDeviceMappings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecBlockDeviceMappings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanEcsLaunchSpecBlockDeviceMappingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecBlockDeviceMappingsOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecBlockDeviceMappingsOutputReference.__init__)
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
        dynamic_volume_size: typing.Optional[typing.Union[OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSize, typing.Dict[str, typing.Any]]] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#delete_on_termination OceanEcsLaunchSpec#delete_on_termination}.
        :param dynamic_volume_size: dynamic_volume_size block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#dynamic_volume_size OceanEcsLaunchSpec#dynamic_volume_size}
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#encrypted OceanEcsLaunchSpec#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#iops OceanEcsLaunchSpec#iops}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#kms_key_id OceanEcsLaunchSpec#kms_key_id}.
        :param snapshot_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#snapshot_id OceanEcsLaunchSpec#snapshot_id}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#throughput OceanEcsLaunchSpec#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#volume_size OceanEcsLaunchSpec#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#volume_type OceanEcsLaunchSpec#volume_type}.
        '''
        value = OceanEcsLaunchSpecBlockDeviceMappingsEbs(
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
    def ebs(self) -> OceanEcsLaunchSpecBlockDeviceMappingsEbsOutputReference:
        return typing.cast(OceanEcsLaunchSpecBlockDeviceMappingsEbsOutputReference, jsii.get(self, "ebs"))

    @builtins.property
    @jsii.member(jsii_name="deviceNameInput")
    def device_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsInput")
    def ebs_input(self) -> typing.Optional[OceanEcsLaunchSpecBlockDeviceMappingsEbs]:
        return typing.cast(typing.Optional[OceanEcsLaunchSpecBlockDeviceMappingsEbs], jsii.get(self, "ebsInput"))

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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsOutputReference, "device_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceName", value)

    @builtins.property
    @jsii.member(jsii_name="noDevice")
    def no_device(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "noDevice"))

    @no_device.setter
    def no_device(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsOutputReference, "no_device").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noDevice", value)

    @builtins.property
    @jsii.member(jsii_name="virtualName")
    def virtual_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualName"))

    @virtual_name.setter
    def virtual_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsOutputReference, "virtual_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanEcsLaunchSpecBlockDeviceMappings, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanEcsLaunchSpecBlockDeviceMappings, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanEcsLaunchSpecBlockDeviceMappings, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecBlockDeviceMappingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecConfig",
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
        "ocean_id": "oceanId",
        "attributes": "attributes",
        "autoscale_headrooms": "autoscaleHeadrooms",
        "block_device_mappings": "blockDeviceMappings",
        "iam_instance_profile": "iamInstanceProfile",
        "id": "id",
        "image_id": "imageId",
        "instance_types": "instanceTypes",
        "preferred_spot_types": "preferredSpotTypes",
        "restrict_scale_down": "restrictScaleDown",
        "scheduling_task": "schedulingTask",
        "security_group_ids": "securityGroupIds",
        "subnet_ids": "subnetIds",
        "tags": "tags",
        "user_data": "userData",
    },
)
class OceanEcsLaunchSpecConfig(cdktf.TerraformMetaArguments):
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
        ocean_id: builtins.str,
        attributes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OceanEcsLaunchSpecAttributes, typing.Dict[str, typing.Any]]]]] = None,
        autoscale_headrooms: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OceanEcsLaunchSpecAutoscaleHeadrooms, typing.Dict[str, typing.Any]]]]] = None,
        block_device_mappings: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OceanEcsLaunchSpecBlockDeviceMappings, typing.Dict[str, typing.Any]]]]] = None,
        iam_instance_profile: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        image_id: typing.Optional[builtins.str] = None,
        instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        preferred_spot_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        restrict_scale_down: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        scheduling_task: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsLaunchSpecSchedulingTask", typing.Dict[str, typing.Any]]]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsLaunchSpecTags", typing.Dict[str, typing.Any]]]]] = None,
        user_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#name OceanEcsLaunchSpec#name}.
        :param ocean_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#ocean_id OceanEcsLaunchSpec#ocean_id}.
        :param attributes: attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#attributes OceanEcsLaunchSpec#attributes}
        :param autoscale_headrooms: autoscale_headrooms block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#autoscale_headrooms OceanEcsLaunchSpec#autoscale_headrooms}
        :param block_device_mappings: block_device_mappings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#block_device_mappings OceanEcsLaunchSpec#block_device_mappings}
        :param iam_instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#iam_instance_profile OceanEcsLaunchSpec#iam_instance_profile}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#id OceanEcsLaunchSpec#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#image_id OceanEcsLaunchSpec#image_id}.
        :param instance_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#instance_types OceanEcsLaunchSpec#instance_types}.
        :param preferred_spot_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#preferred_spot_types OceanEcsLaunchSpec#preferred_spot_types}.
        :param restrict_scale_down: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#restrict_scale_down OceanEcsLaunchSpec#restrict_scale_down}.
        :param scheduling_task: scheduling_task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#scheduling_task OceanEcsLaunchSpec#scheduling_task}
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#security_group_ids OceanEcsLaunchSpec#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#subnet_ids OceanEcsLaunchSpec#subnet_ids}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#tags OceanEcsLaunchSpec#tags}
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#user_data OceanEcsLaunchSpec#user_data}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument ocean_id", value=ocean_id, expected_type=type_hints["ocean_id"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument autoscale_headrooms", value=autoscale_headrooms, expected_type=type_hints["autoscale_headrooms"])
            check_type(argname="argument block_device_mappings", value=block_device_mappings, expected_type=type_hints["block_device_mappings"])
            check_type(argname="argument iam_instance_profile", value=iam_instance_profile, expected_type=type_hints["iam_instance_profile"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument image_id", value=image_id, expected_type=type_hints["image_id"])
            check_type(argname="argument instance_types", value=instance_types, expected_type=type_hints["instance_types"])
            check_type(argname="argument preferred_spot_types", value=preferred_spot_types, expected_type=type_hints["preferred_spot_types"])
            check_type(argname="argument restrict_scale_down", value=restrict_scale_down, expected_type=type_hints["restrict_scale_down"])
            check_type(argname="argument scheduling_task", value=scheduling_task, expected_type=type_hints["scheduling_task"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "ocean_id": ocean_id,
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
        if attributes is not None:
            self._values["attributes"] = attributes
        if autoscale_headrooms is not None:
            self._values["autoscale_headrooms"] = autoscale_headrooms
        if block_device_mappings is not None:
            self._values["block_device_mappings"] = block_device_mappings
        if iam_instance_profile is not None:
            self._values["iam_instance_profile"] = iam_instance_profile
        if id is not None:
            self._values["id"] = id
        if image_id is not None:
            self._values["image_id"] = image_id
        if instance_types is not None:
            self._values["instance_types"] = instance_types
        if preferred_spot_types is not None:
            self._values["preferred_spot_types"] = preferred_spot_types
        if restrict_scale_down is not None:
            self._values["restrict_scale_down"] = restrict_scale_down
        if scheduling_task is not None:
            self._values["scheduling_task"] = scheduling_task
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids
        if tags is not None:
            self._values["tags"] = tags
        if user_data is not None:
            self._values["user_data"] = user_data

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#name OceanEcsLaunchSpec#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ocean_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#ocean_id OceanEcsLaunchSpec#ocean_id}.'''
        result = self._values.get("ocean_id")
        assert result is not None, "Required property 'ocean_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecAttributes]]]:
        '''attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#attributes OceanEcsLaunchSpec#attributes}
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecAttributes]]], result)

    @builtins.property
    def autoscale_headrooms(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecAutoscaleHeadrooms]]]:
        '''autoscale_headrooms block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#autoscale_headrooms OceanEcsLaunchSpec#autoscale_headrooms}
        '''
        result = self._values.get("autoscale_headrooms")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecAutoscaleHeadrooms]]], result)

    @builtins.property
    def block_device_mappings(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecBlockDeviceMappings]]]:
        '''block_device_mappings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#block_device_mappings OceanEcsLaunchSpec#block_device_mappings}
        '''
        result = self._values.get("block_device_mappings")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecBlockDeviceMappings]]], result)

    @builtins.property
    def iam_instance_profile(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#iam_instance_profile OceanEcsLaunchSpec#iam_instance_profile}.'''
        result = self._values.get("iam_instance_profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#id OceanEcsLaunchSpec#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#image_id OceanEcsLaunchSpec#image_id}.'''
        result = self._values.get("image_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#instance_types OceanEcsLaunchSpec#instance_types}.'''
        result = self._values.get("instance_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def preferred_spot_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#preferred_spot_types OceanEcsLaunchSpec#preferred_spot_types}.'''
        result = self._values.get("preferred_spot_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def restrict_scale_down(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#restrict_scale_down OceanEcsLaunchSpec#restrict_scale_down}.'''
        result = self._values.get("restrict_scale_down")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def scheduling_task(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLaunchSpecSchedulingTask"]]]:
        '''scheduling_task block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#scheduling_task OceanEcsLaunchSpec#scheduling_task}
        '''
        result = self._values.get("scheduling_task")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLaunchSpecSchedulingTask"]]], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#security_group_ids OceanEcsLaunchSpec#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#subnet_ids OceanEcsLaunchSpec#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLaunchSpecTags"]]]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#tags OceanEcsLaunchSpec#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLaunchSpecTags"]]], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#user_data OceanEcsLaunchSpec#user_data}.'''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsLaunchSpecConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecSchedulingTask",
    jsii_struct_bases=[],
    name_mapping={
        "cron_expression": "cronExpression",
        "is_enabled": "isEnabled",
        "task_type": "taskType",
        "task_headroom": "taskHeadroom",
    },
)
class OceanEcsLaunchSpecSchedulingTask:
    def __init__(
        self,
        *,
        cron_expression: builtins.str,
        is_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        task_type: builtins.str,
        task_headroom: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsLaunchSpecSchedulingTaskTaskHeadroom", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cron_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#cron_expression OceanEcsLaunchSpec#cron_expression}.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#is_enabled OceanEcsLaunchSpec#is_enabled}.
        :param task_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#task_type OceanEcsLaunchSpec#task_type}.
        :param task_headroom: task_headroom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#task_headroom OceanEcsLaunchSpec#task_headroom}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecSchedulingTask.__init__)
            check_type(argname="argument cron_expression", value=cron_expression, expected_type=type_hints["cron_expression"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument task_type", value=task_type, expected_type=type_hints["task_type"])
            check_type(argname="argument task_headroom", value=task_headroom, expected_type=type_hints["task_headroom"])
        self._values: typing.Dict[str, typing.Any] = {
            "cron_expression": cron_expression,
            "is_enabled": is_enabled,
            "task_type": task_type,
        }
        if task_headroom is not None:
            self._values["task_headroom"] = task_headroom

    @builtins.property
    def cron_expression(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#cron_expression OceanEcsLaunchSpec#cron_expression}.'''
        result = self._values.get("cron_expression")
        assert result is not None, "Required property 'cron_expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#is_enabled OceanEcsLaunchSpec#is_enabled}.'''
        result = self._values.get("is_enabled")
        assert result is not None, "Required property 'is_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def task_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#task_type OceanEcsLaunchSpec#task_type}.'''
        result = self._values.get("task_type")
        assert result is not None, "Required property 'task_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def task_headroom(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLaunchSpecSchedulingTaskTaskHeadroom"]]]:
        '''task_headroom block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#task_headroom OceanEcsLaunchSpec#task_headroom}
        '''
        result = self._values.get("task_headroom")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLaunchSpecSchedulingTaskTaskHeadroom"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsLaunchSpecSchedulingTask(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsLaunchSpecSchedulingTaskList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecSchedulingTaskList",
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
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecSchedulingTaskList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OceanEcsLaunchSpecSchedulingTaskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecSchedulingTaskList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanEcsLaunchSpecSchedulingTaskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecSchedulingTaskList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecSchedulingTaskList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecSchedulingTaskList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecSchedulingTask]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecSchedulingTask]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecSchedulingTask]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecSchedulingTaskList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanEcsLaunchSpecSchedulingTaskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecSchedulingTaskOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecSchedulingTaskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putTaskHeadroom")
    def put_task_headroom(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanEcsLaunchSpecSchedulingTaskTaskHeadroom", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecSchedulingTaskOutputReference.put_task_headroom)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTaskHeadroom", [value]))

    @jsii.member(jsii_name="resetTaskHeadroom")
    def reset_task_headroom(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskHeadroom", []))

    @builtins.property
    @jsii.member(jsii_name="taskHeadroom")
    def task_headroom(self) -> "OceanEcsLaunchSpecSchedulingTaskTaskHeadroomList":
        return typing.cast("OceanEcsLaunchSpecSchedulingTaskTaskHeadroomList", jsii.get(self, "taskHeadroom"))

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
    @jsii.member(jsii_name="taskHeadroomInput")
    def task_headroom_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLaunchSpecSchedulingTaskTaskHeadroom"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanEcsLaunchSpecSchedulingTaskTaskHeadroom"]]], jsii.get(self, "taskHeadroomInput"))

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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecSchedulingTaskOutputReference, "cron_expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cronExpression", value)

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecSchedulingTaskOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="taskType")
    def task_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskType"))

    @task_type.setter
    def task_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecSchedulingTaskOutputReference, "task_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanEcsLaunchSpecSchedulingTask, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanEcsLaunchSpecSchedulingTask, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanEcsLaunchSpecSchedulingTask, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecSchedulingTaskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecSchedulingTaskTaskHeadroom",
    jsii_struct_bases=[],
    name_mapping={
        "num_of_units": "numOfUnits",
        "cpu_per_unit": "cpuPerUnit",
        "memory_per_unit": "memoryPerUnit",
    },
)
class OceanEcsLaunchSpecSchedulingTaskTaskHeadroom:
    def __init__(
        self,
        *,
        num_of_units: jsii.Number,
        cpu_per_unit: typing.Optional[jsii.Number] = None,
        memory_per_unit: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param num_of_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#num_of_units OceanEcsLaunchSpec#num_of_units}.
        :param cpu_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#cpu_per_unit OceanEcsLaunchSpec#cpu_per_unit}.
        :param memory_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#memory_per_unit OceanEcsLaunchSpec#memory_per_unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecSchedulingTaskTaskHeadroom.__init__)
            check_type(argname="argument num_of_units", value=num_of_units, expected_type=type_hints["num_of_units"])
            check_type(argname="argument cpu_per_unit", value=cpu_per_unit, expected_type=type_hints["cpu_per_unit"])
            check_type(argname="argument memory_per_unit", value=memory_per_unit, expected_type=type_hints["memory_per_unit"])
        self._values: typing.Dict[str, typing.Any] = {
            "num_of_units": num_of_units,
        }
        if cpu_per_unit is not None:
            self._values["cpu_per_unit"] = cpu_per_unit
        if memory_per_unit is not None:
            self._values["memory_per_unit"] = memory_per_unit

    @builtins.property
    def num_of_units(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#num_of_units OceanEcsLaunchSpec#num_of_units}.'''
        result = self._values.get("num_of_units")
        assert result is not None, "Required property 'num_of_units' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def cpu_per_unit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#cpu_per_unit OceanEcsLaunchSpec#cpu_per_unit}.'''
        result = self._values.get("cpu_per_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_per_unit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#memory_per_unit OceanEcsLaunchSpec#memory_per_unit}.'''
        result = self._values.get("memory_per_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsLaunchSpecSchedulingTaskTaskHeadroom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsLaunchSpecSchedulingTaskTaskHeadroomList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecSchedulingTaskTaskHeadroomList",
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
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecSchedulingTaskTaskHeadroomList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OceanEcsLaunchSpecSchedulingTaskTaskHeadroomOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecSchedulingTaskTaskHeadroomList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanEcsLaunchSpecSchedulingTaskTaskHeadroomOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecSchedulingTaskTaskHeadroomList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecSchedulingTaskTaskHeadroomList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecSchedulingTaskTaskHeadroomList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecSchedulingTaskTaskHeadroom]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecSchedulingTaskTaskHeadroom]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecSchedulingTaskTaskHeadroom]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecSchedulingTaskTaskHeadroomList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanEcsLaunchSpecSchedulingTaskTaskHeadroomOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecSchedulingTaskTaskHeadroomOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecSchedulingTaskTaskHeadroomOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCpuPerUnit")
    def reset_cpu_per_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuPerUnit", []))

    @jsii.member(jsii_name="resetMemoryPerUnit")
    def reset_memory_per_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryPerUnit", []))

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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecSchedulingTaskTaskHeadroomOutputReference, "cpu_per_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuPerUnit", value)

    @builtins.property
    @jsii.member(jsii_name="memoryPerUnit")
    def memory_per_unit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryPerUnit"))

    @memory_per_unit.setter
    def memory_per_unit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecSchedulingTaskTaskHeadroomOutputReference, "memory_per_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryPerUnit", value)

    @builtins.property
    @jsii.member(jsii_name="numOfUnits")
    def num_of_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numOfUnits"))

    @num_of_units.setter
    def num_of_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecSchedulingTaskTaskHeadroomOutputReference, "num_of_units").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numOfUnits", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanEcsLaunchSpecSchedulingTaskTaskHeadroom, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanEcsLaunchSpecSchedulingTaskTaskHeadroom, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanEcsLaunchSpecSchedulingTaskTaskHeadroom, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecSchedulingTaskTaskHeadroomOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class OceanEcsLaunchSpecTags:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#key OceanEcsLaunchSpec#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#value OceanEcsLaunchSpec#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecTags.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#key OceanEcsLaunchSpec#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_ecs_launch_spec#value OceanEcsLaunchSpec#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanEcsLaunchSpecTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanEcsLaunchSpecTagsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecTagsList",
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
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecTagsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanEcsLaunchSpecTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecTagsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanEcsLaunchSpecTagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecTagsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecTagsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecTagsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecTags]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanEcsLaunchSpecTags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecTagsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanEcsLaunchSpecTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanEcsLaunchSpec.OceanEcsLaunchSpecTagsOutputReference",
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
            type_hints = typing.get_type_hints(OceanEcsLaunchSpecTagsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecTagsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecTagsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanEcsLaunchSpecTags, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanEcsLaunchSpecTags, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanEcsLaunchSpecTags, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanEcsLaunchSpecTagsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "OceanEcsLaunchSpec",
    "OceanEcsLaunchSpecAttributes",
    "OceanEcsLaunchSpecAttributesList",
    "OceanEcsLaunchSpecAttributesOutputReference",
    "OceanEcsLaunchSpecAutoscaleHeadrooms",
    "OceanEcsLaunchSpecAutoscaleHeadroomsList",
    "OceanEcsLaunchSpecAutoscaleHeadroomsOutputReference",
    "OceanEcsLaunchSpecBlockDeviceMappings",
    "OceanEcsLaunchSpecBlockDeviceMappingsEbs",
    "OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSize",
    "OceanEcsLaunchSpecBlockDeviceMappingsEbsDynamicVolumeSizeOutputReference",
    "OceanEcsLaunchSpecBlockDeviceMappingsEbsOutputReference",
    "OceanEcsLaunchSpecBlockDeviceMappingsList",
    "OceanEcsLaunchSpecBlockDeviceMappingsOutputReference",
    "OceanEcsLaunchSpecConfig",
    "OceanEcsLaunchSpecSchedulingTask",
    "OceanEcsLaunchSpecSchedulingTaskList",
    "OceanEcsLaunchSpecSchedulingTaskOutputReference",
    "OceanEcsLaunchSpecSchedulingTaskTaskHeadroom",
    "OceanEcsLaunchSpecSchedulingTaskTaskHeadroomList",
    "OceanEcsLaunchSpecSchedulingTaskTaskHeadroomOutputReference",
    "OceanEcsLaunchSpecTags",
    "OceanEcsLaunchSpecTagsList",
    "OceanEcsLaunchSpecTagsOutputReference",
]

publication.publish()
