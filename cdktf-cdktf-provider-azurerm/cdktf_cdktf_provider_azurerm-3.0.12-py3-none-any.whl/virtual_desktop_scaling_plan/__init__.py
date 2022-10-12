'''
# `azurerm_virtual_desktop_scaling_plan`

Refer to the Terraform Registory for docs: [`azurerm_virtual_desktop_scaling_plan`](https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan).
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


class VirtualDesktopScalingPlan(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualDesktopScalingPlan.VirtualDesktopScalingPlan",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan azurerm_virtual_desktop_scaling_plan}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        schedule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualDesktopScalingPlanSchedule", typing.Dict[str, typing.Any]]]],
        time_zone: builtins.str,
        description: typing.Optional[builtins.str] = None,
        exclusion_tag: typing.Optional[builtins.str] = None,
        friendly_name: typing.Optional[builtins.str] = None,
        host_pool: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualDesktopScalingPlanHostPool", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VirtualDesktopScalingPlanTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan azurerm_virtual_desktop_scaling_plan} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#location VirtualDesktopScalingPlan#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#name VirtualDesktopScalingPlan#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#resource_group_name VirtualDesktopScalingPlan#resource_group_name}.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#schedule VirtualDesktopScalingPlan#schedule}
        :param time_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#time_zone VirtualDesktopScalingPlan#time_zone}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#description VirtualDesktopScalingPlan#description}.
        :param exclusion_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#exclusion_tag VirtualDesktopScalingPlan#exclusion_tag}.
        :param friendly_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#friendly_name VirtualDesktopScalingPlan#friendly_name}.
        :param host_pool: host_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#host_pool VirtualDesktopScalingPlan#host_pool}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#id VirtualDesktopScalingPlan#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#tags VirtualDesktopScalingPlan#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#timeouts VirtualDesktopScalingPlan#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualDesktopScalingPlan.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VirtualDesktopScalingPlanConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            schedule=schedule,
            time_zone=time_zone,
            description=description,
            exclusion_tag=exclusion_tag,
            friendly_name=friendly_name,
            host_pool=host_pool,
            id=id,
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

    @jsii.member(jsii_name="putHostPool")
    def put_host_pool(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualDesktopScalingPlanHostPool", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualDesktopScalingPlan.put_host_pool)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHostPool", [value]))

    @jsii.member(jsii_name="putSchedule")
    def put_schedule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualDesktopScalingPlanSchedule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualDesktopScalingPlan.put_schedule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSchedule", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#create VirtualDesktopScalingPlan#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#delete VirtualDesktopScalingPlan#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#read VirtualDesktopScalingPlan#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#update VirtualDesktopScalingPlan#update}.
        '''
        value = VirtualDesktopScalingPlanTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExclusionTag")
    def reset_exclusion_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusionTag", []))

    @jsii.member(jsii_name="resetFriendlyName")
    def reset_friendly_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFriendlyName", []))

    @jsii.member(jsii_name="resetHostPool")
    def reset_host_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPool", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="hostPool")
    def host_pool(self) -> "VirtualDesktopScalingPlanHostPoolList":
        return typing.cast("VirtualDesktopScalingPlanHostPoolList", jsii.get(self, "hostPool"))

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> "VirtualDesktopScalingPlanScheduleList":
        return typing.cast("VirtualDesktopScalingPlanScheduleList", jsii.get(self, "schedule"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "VirtualDesktopScalingPlanTimeoutsOutputReference":
        return typing.cast("VirtualDesktopScalingPlanTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusionTagInput")
    def exclusion_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exclusionTagInput"))

    @builtins.property
    @jsii.member(jsii_name="friendlyNameInput")
    def friendly_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "friendlyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPoolInput")
    def host_pool_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualDesktopScalingPlanHostPool"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualDesktopScalingPlanHostPool"]]], jsii.get(self, "hostPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualDesktopScalingPlanSchedule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualDesktopScalingPlanSchedule"]]], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["VirtualDesktopScalingPlanTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["VirtualDesktopScalingPlanTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeZoneInput")
    def time_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlan, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="exclusionTag")
    def exclusion_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exclusionTag"))

    @exclusion_tag.setter
    def exclusion_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlan, "exclusion_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusionTag", value)

    @builtins.property
    @jsii.member(jsii_name="friendlyName")
    def friendly_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "friendlyName"))

    @friendly_name.setter
    def friendly_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlan, "friendly_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "friendlyName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlan, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlan, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlan, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlan, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlan, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlan, "time_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualDesktopScalingPlan.VirtualDesktopScalingPlanConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "schedule": "schedule",
        "time_zone": "timeZone",
        "description": "description",
        "exclusion_tag": "exclusionTag",
        "friendly_name": "friendlyName",
        "host_pool": "hostPool",
        "id": "id",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class VirtualDesktopScalingPlanConfig(cdktf.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        schedule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualDesktopScalingPlanSchedule", typing.Dict[str, typing.Any]]]],
        time_zone: builtins.str,
        description: typing.Optional[builtins.str] = None,
        exclusion_tag: typing.Optional[builtins.str] = None,
        friendly_name: typing.Optional[builtins.str] = None,
        host_pool: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualDesktopScalingPlanHostPool", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VirtualDesktopScalingPlanTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#location VirtualDesktopScalingPlan#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#name VirtualDesktopScalingPlan#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#resource_group_name VirtualDesktopScalingPlan#resource_group_name}.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#schedule VirtualDesktopScalingPlan#schedule}
        :param time_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#time_zone VirtualDesktopScalingPlan#time_zone}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#description VirtualDesktopScalingPlan#description}.
        :param exclusion_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#exclusion_tag VirtualDesktopScalingPlan#exclusion_tag}.
        :param friendly_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#friendly_name VirtualDesktopScalingPlan#friendly_name}.
        :param host_pool: host_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#host_pool VirtualDesktopScalingPlan#host_pool}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#id VirtualDesktopScalingPlan#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#tags VirtualDesktopScalingPlan#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#timeouts VirtualDesktopScalingPlan#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = VirtualDesktopScalingPlanTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(VirtualDesktopScalingPlanConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument exclusion_tag", value=exclusion_tag, expected_type=type_hints["exclusion_tag"])
            check_type(argname="argument friendly_name", value=friendly_name, expected_type=type_hints["friendly_name"])
            check_type(argname="argument host_pool", value=host_pool, expected_type=type_hints["host_pool"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "schedule": schedule,
            "time_zone": time_zone,
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
        if description is not None:
            self._values["description"] = description
        if exclusion_tag is not None:
            self._values["exclusion_tag"] = exclusion_tag
        if friendly_name is not None:
            self._values["friendly_name"] = friendly_name
        if host_pool is not None:
            self._values["host_pool"] = host_pool
        if id is not None:
            self._values["id"] = id
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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#location VirtualDesktopScalingPlan#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#name VirtualDesktopScalingPlan#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#resource_group_name VirtualDesktopScalingPlan#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["VirtualDesktopScalingPlanSchedule"]]:
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#schedule VirtualDesktopScalingPlan#schedule}
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["VirtualDesktopScalingPlanSchedule"]], result)

    @builtins.property
    def time_zone(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#time_zone VirtualDesktopScalingPlan#time_zone}.'''
        result = self._values.get("time_zone")
        assert result is not None, "Required property 'time_zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#description VirtualDesktopScalingPlan#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exclusion_tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#exclusion_tag VirtualDesktopScalingPlan#exclusion_tag}.'''
        result = self._values.get("exclusion_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def friendly_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#friendly_name VirtualDesktopScalingPlan#friendly_name}.'''
        result = self._values.get("friendly_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_pool(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualDesktopScalingPlanHostPool"]]]:
        '''host_pool block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#host_pool VirtualDesktopScalingPlan#host_pool}
        '''
        result = self._values.get("host_pool")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualDesktopScalingPlanHostPool"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#id VirtualDesktopScalingPlan#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#tags VirtualDesktopScalingPlan#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["VirtualDesktopScalingPlanTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#timeouts VirtualDesktopScalingPlan#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["VirtualDesktopScalingPlanTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualDesktopScalingPlanConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualDesktopScalingPlan.VirtualDesktopScalingPlanHostPool",
    jsii_struct_bases=[],
    name_mapping={
        "hostpool_id": "hostpoolId",
        "scaling_plan_enabled": "scalingPlanEnabled",
    },
)
class VirtualDesktopScalingPlanHostPool:
    def __init__(
        self,
        *,
        hostpool_id: builtins.str,
        scaling_plan_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param hostpool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#hostpool_id VirtualDesktopScalingPlan#hostpool_id}.
        :param scaling_plan_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#scaling_plan_enabled VirtualDesktopScalingPlan#scaling_plan_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualDesktopScalingPlanHostPool.__init__)
            check_type(argname="argument hostpool_id", value=hostpool_id, expected_type=type_hints["hostpool_id"])
            check_type(argname="argument scaling_plan_enabled", value=scaling_plan_enabled, expected_type=type_hints["scaling_plan_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "hostpool_id": hostpool_id,
            "scaling_plan_enabled": scaling_plan_enabled,
        }

    @builtins.property
    def hostpool_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#hostpool_id VirtualDesktopScalingPlan#hostpool_id}.'''
        result = self._values.get("hostpool_id")
        assert result is not None, "Required property 'hostpool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scaling_plan_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#scaling_plan_enabled VirtualDesktopScalingPlan#scaling_plan_enabled}.'''
        result = self._values.get("scaling_plan_enabled")
        assert result is not None, "Required property 'scaling_plan_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualDesktopScalingPlanHostPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualDesktopScalingPlanHostPoolList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualDesktopScalingPlan.VirtualDesktopScalingPlanHostPoolList",
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
            type_hints = typing.get_type_hints(VirtualDesktopScalingPlanHostPoolList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualDesktopScalingPlanHostPoolOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualDesktopScalingPlanHostPoolList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualDesktopScalingPlanHostPoolOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanHostPoolList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanHostPoolList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanHostPoolList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualDesktopScalingPlanHostPool]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualDesktopScalingPlanHostPool]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualDesktopScalingPlanHostPool]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanHostPoolList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualDesktopScalingPlanHostPoolOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualDesktopScalingPlan.VirtualDesktopScalingPlanHostPoolOutputReference",
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
            type_hints = typing.get_type_hints(VirtualDesktopScalingPlanHostPoolOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="hostpoolIdInput")
    def hostpool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostpoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="scalingPlanEnabledInput")
    def scaling_plan_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "scalingPlanEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="hostpoolId")
    def hostpool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostpoolId"))

    @hostpool_id.setter
    def hostpool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanHostPoolOutputReference, "hostpool_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostpoolId", value)

    @builtins.property
    @jsii.member(jsii_name="scalingPlanEnabled")
    def scaling_plan_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "scalingPlanEnabled"))

    @scaling_plan_enabled.setter
    def scaling_plan_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanHostPoolOutputReference, "scaling_plan_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalingPlanEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualDesktopScalingPlanHostPool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualDesktopScalingPlanHostPool, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualDesktopScalingPlanHostPool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanHostPoolOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualDesktopScalingPlan.VirtualDesktopScalingPlanSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "days_of_week": "daysOfWeek",
        "name": "name",
        "off_peak_load_balancing_algorithm": "offPeakLoadBalancingAlgorithm",
        "off_peak_start_time": "offPeakStartTime",
        "peak_load_balancing_algorithm": "peakLoadBalancingAlgorithm",
        "peak_start_time": "peakStartTime",
        "ramp_down_capacity_threshold_percent": "rampDownCapacityThresholdPercent",
        "ramp_down_force_logoff_users": "rampDownForceLogoffUsers",
        "ramp_down_load_balancing_algorithm": "rampDownLoadBalancingAlgorithm",
        "ramp_down_minimum_hosts_percent": "rampDownMinimumHostsPercent",
        "ramp_down_notification_message": "rampDownNotificationMessage",
        "ramp_down_start_time": "rampDownStartTime",
        "ramp_down_stop_hosts_when": "rampDownStopHostsWhen",
        "ramp_down_wait_time_minutes": "rampDownWaitTimeMinutes",
        "ramp_up_load_balancing_algorithm": "rampUpLoadBalancingAlgorithm",
        "ramp_up_start_time": "rampUpStartTime",
        "ramp_up_capacity_threshold_percent": "rampUpCapacityThresholdPercent",
        "ramp_up_minimum_hosts_percent": "rampUpMinimumHostsPercent",
    },
)
class VirtualDesktopScalingPlanSchedule:
    def __init__(
        self,
        *,
        days_of_week: typing.Sequence[builtins.str],
        name: builtins.str,
        off_peak_load_balancing_algorithm: builtins.str,
        off_peak_start_time: builtins.str,
        peak_load_balancing_algorithm: builtins.str,
        peak_start_time: builtins.str,
        ramp_down_capacity_threshold_percent: jsii.Number,
        ramp_down_force_logoff_users: typing.Union[builtins.bool, cdktf.IResolvable],
        ramp_down_load_balancing_algorithm: builtins.str,
        ramp_down_minimum_hosts_percent: jsii.Number,
        ramp_down_notification_message: builtins.str,
        ramp_down_start_time: builtins.str,
        ramp_down_stop_hosts_when: builtins.str,
        ramp_down_wait_time_minutes: jsii.Number,
        ramp_up_load_balancing_algorithm: builtins.str,
        ramp_up_start_time: builtins.str,
        ramp_up_capacity_threshold_percent: typing.Optional[jsii.Number] = None,
        ramp_up_minimum_hosts_percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param days_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#days_of_week VirtualDesktopScalingPlan#days_of_week}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#name VirtualDesktopScalingPlan#name}.
        :param off_peak_load_balancing_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#off_peak_load_balancing_algorithm VirtualDesktopScalingPlan#off_peak_load_balancing_algorithm}.
        :param off_peak_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#off_peak_start_time VirtualDesktopScalingPlan#off_peak_start_time}.
        :param peak_load_balancing_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#peak_load_balancing_algorithm VirtualDesktopScalingPlan#peak_load_balancing_algorithm}.
        :param peak_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#peak_start_time VirtualDesktopScalingPlan#peak_start_time}.
        :param ramp_down_capacity_threshold_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_down_capacity_threshold_percent VirtualDesktopScalingPlan#ramp_down_capacity_threshold_percent}.
        :param ramp_down_force_logoff_users: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_down_force_logoff_users VirtualDesktopScalingPlan#ramp_down_force_logoff_users}.
        :param ramp_down_load_balancing_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_down_load_balancing_algorithm VirtualDesktopScalingPlan#ramp_down_load_balancing_algorithm}.
        :param ramp_down_minimum_hosts_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_down_minimum_hosts_percent VirtualDesktopScalingPlan#ramp_down_minimum_hosts_percent}.
        :param ramp_down_notification_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_down_notification_message VirtualDesktopScalingPlan#ramp_down_notification_message}.
        :param ramp_down_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_down_start_time VirtualDesktopScalingPlan#ramp_down_start_time}.
        :param ramp_down_stop_hosts_when: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_down_stop_hosts_when VirtualDesktopScalingPlan#ramp_down_stop_hosts_when}.
        :param ramp_down_wait_time_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_down_wait_time_minutes VirtualDesktopScalingPlan#ramp_down_wait_time_minutes}.
        :param ramp_up_load_balancing_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_up_load_balancing_algorithm VirtualDesktopScalingPlan#ramp_up_load_balancing_algorithm}.
        :param ramp_up_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_up_start_time VirtualDesktopScalingPlan#ramp_up_start_time}.
        :param ramp_up_capacity_threshold_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_up_capacity_threshold_percent VirtualDesktopScalingPlan#ramp_up_capacity_threshold_percent}.
        :param ramp_up_minimum_hosts_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_up_minimum_hosts_percent VirtualDesktopScalingPlan#ramp_up_minimum_hosts_percent}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualDesktopScalingPlanSchedule.__init__)
            check_type(argname="argument days_of_week", value=days_of_week, expected_type=type_hints["days_of_week"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument off_peak_load_balancing_algorithm", value=off_peak_load_balancing_algorithm, expected_type=type_hints["off_peak_load_balancing_algorithm"])
            check_type(argname="argument off_peak_start_time", value=off_peak_start_time, expected_type=type_hints["off_peak_start_time"])
            check_type(argname="argument peak_load_balancing_algorithm", value=peak_load_balancing_algorithm, expected_type=type_hints["peak_load_balancing_algorithm"])
            check_type(argname="argument peak_start_time", value=peak_start_time, expected_type=type_hints["peak_start_time"])
            check_type(argname="argument ramp_down_capacity_threshold_percent", value=ramp_down_capacity_threshold_percent, expected_type=type_hints["ramp_down_capacity_threshold_percent"])
            check_type(argname="argument ramp_down_force_logoff_users", value=ramp_down_force_logoff_users, expected_type=type_hints["ramp_down_force_logoff_users"])
            check_type(argname="argument ramp_down_load_balancing_algorithm", value=ramp_down_load_balancing_algorithm, expected_type=type_hints["ramp_down_load_balancing_algorithm"])
            check_type(argname="argument ramp_down_minimum_hosts_percent", value=ramp_down_minimum_hosts_percent, expected_type=type_hints["ramp_down_minimum_hosts_percent"])
            check_type(argname="argument ramp_down_notification_message", value=ramp_down_notification_message, expected_type=type_hints["ramp_down_notification_message"])
            check_type(argname="argument ramp_down_start_time", value=ramp_down_start_time, expected_type=type_hints["ramp_down_start_time"])
            check_type(argname="argument ramp_down_stop_hosts_when", value=ramp_down_stop_hosts_when, expected_type=type_hints["ramp_down_stop_hosts_when"])
            check_type(argname="argument ramp_down_wait_time_minutes", value=ramp_down_wait_time_minutes, expected_type=type_hints["ramp_down_wait_time_minutes"])
            check_type(argname="argument ramp_up_load_balancing_algorithm", value=ramp_up_load_balancing_algorithm, expected_type=type_hints["ramp_up_load_balancing_algorithm"])
            check_type(argname="argument ramp_up_start_time", value=ramp_up_start_time, expected_type=type_hints["ramp_up_start_time"])
            check_type(argname="argument ramp_up_capacity_threshold_percent", value=ramp_up_capacity_threshold_percent, expected_type=type_hints["ramp_up_capacity_threshold_percent"])
            check_type(argname="argument ramp_up_minimum_hosts_percent", value=ramp_up_minimum_hosts_percent, expected_type=type_hints["ramp_up_minimum_hosts_percent"])
        self._values: typing.Dict[str, typing.Any] = {
            "days_of_week": days_of_week,
            "name": name,
            "off_peak_load_balancing_algorithm": off_peak_load_balancing_algorithm,
            "off_peak_start_time": off_peak_start_time,
            "peak_load_balancing_algorithm": peak_load_balancing_algorithm,
            "peak_start_time": peak_start_time,
            "ramp_down_capacity_threshold_percent": ramp_down_capacity_threshold_percent,
            "ramp_down_force_logoff_users": ramp_down_force_logoff_users,
            "ramp_down_load_balancing_algorithm": ramp_down_load_balancing_algorithm,
            "ramp_down_minimum_hosts_percent": ramp_down_minimum_hosts_percent,
            "ramp_down_notification_message": ramp_down_notification_message,
            "ramp_down_start_time": ramp_down_start_time,
            "ramp_down_stop_hosts_when": ramp_down_stop_hosts_when,
            "ramp_down_wait_time_minutes": ramp_down_wait_time_minutes,
            "ramp_up_load_balancing_algorithm": ramp_up_load_balancing_algorithm,
            "ramp_up_start_time": ramp_up_start_time,
        }
        if ramp_up_capacity_threshold_percent is not None:
            self._values["ramp_up_capacity_threshold_percent"] = ramp_up_capacity_threshold_percent
        if ramp_up_minimum_hosts_percent is not None:
            self._values["ramp_up_minimum_hosts_percent"] = ramp_up_minimum_hosts_percent

    @builtins.property
    def days_of_week(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#days_of_week VirtualDesktopScalingPlan#days_of_week}.'''
        result = self._values.get("days_of_week")
        assert result is not None, "Required property 'days_of_week' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#name VirtualDesktopScalingPlan#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def off_peak_load_balancing_algorithm(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#off_peak_load_balancing_algorithm VirtualDesktopScalingPlan#off_peak_load_balancing_algorithm}.'''
        result = self._values.get("off_peak_load_balancing_algorithm")
        assert result is not None, "Required property 'off_peak_load_balancing_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def off_peak_start_time(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#off_peak_start_time VirtualDesktopScalingPlan#off_peak_start_time}.'''
        result = self._values.get("off_peak_start_time")
        assert result is not None, "Required property 'off_peak_start_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def peak_load_balancing_algorithm(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#peak_load_balancing_algorithm VirtualDesktopScalingPlan#peak_load_balancing_algorithm}.'''
        result = self._values.get("peak_load_balancing_algorithm")
        assert result is not None, "Required property 'peak_load_balancing_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def peak_start_time(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#peak_start_time VirtualDesktopScalingPlan#peak_start_time}.'''
        result = self._values.get("peak_start_time")
        assert result is not None, "Required property 'peak_start_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ramp_down_capacity_threshold_percent(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_down_capacity_threshold_percent VirtualDesktopScalingPlan#ramp_down_capacity_threshold_percent}.'''
        result = self._values.get("ramp_down_capacity_threshold_percent")
        assert result is not None, "Required property 'ramp_down_capacity_threshold_percent' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def ramp_down_force_logoff_users(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_down_force_logoff_users VirtualDesktopScalingPlan#ramp_down_force_logoff_users}.'''
        result = self._values.get("ramp_down_force_logoff_users")
        assert result is not None, "Required property 'ramp_down_force_logoff_users' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def ramp_down_load_balancing_algorithm(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_down_load_balancing_algorithm VirtualDesktopScalingPlan#ramp_down_load_balancing_algorithm}.'''
        result = self._values.get("ramp_down_load_balancing_algorithm")
        assert result is not None, "Required property 'ramp_down_load_balancing_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ramp_down_minimum_hosts_percent(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_down_minimum_hosts_percent VirtualDesktopScalingPlan#ramp_down_minimum_hosts_percent}.'''
        result = self._values.get("ramp_down_minimum_hosts_percent")
        assert result is not None, "Required property 'ramp_down_minimum_hosts_percent' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def ramp_down_notification_message(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_down_notification_message VirtualDesktopScalingPlan#ramp_down_notification_message}.'''
        result = self._values.get("ramp_down_notification_message")
        assert result is not None, "Required property 'ramp_down_notification_message' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ramp_down_start_time(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_down_start_time VirtualDesktopScalingPlan#ramp_down_start_time}.'''
        result = self._values.get("ramp_down_start_time")
        assert result is not None, "Required property 'ramp_down_start_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ramp_down_stop_hosts_when(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_down_stop_hosts_when VirtualDesktopScalingPlan#ramp_down_stop_hosts_when}.'''
        result = self._values.get("ramp_down_stop_hosts_when")
        assert result is not None, "Required property 'ramp_down_stop_hosts_when' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ramp_down_wait_time_minutes(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_down_wait_time_minutes VirtualDesktopScalingPlan#ramp_down_wait_time_minutes}.'''
        result = self._values.get("ramp_down_wait_time_minutes")
        assert result is not None, "Required property 'ramp_down_wait_time_minutes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def ramp_up_load_balancing_algorithm(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_up_load_balancing_algorithm VirtualDesktopScalingPlan#ramp_up_load_balancing_algorithm}.'''
        result = self._values.get("ramp_up_load_balancing_algorithm")
        assert result is not None, "Required property 'ramp_up_load_balancing_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ramp_up_start_time(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_up_start_time VirtualDesktopScalingPlan#ramp_up_start_time}.'''
        result = self._values.get("ramp_up_start_time")
        assert result is not None, "Required property 'ramp_up_start_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ramp_up_capacity_threshold_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_up_capacity_threshold_percent VirtualDesktopScalingPlan#ramp_up_capacity_threshold_percent}.'''
        result = self._values.get("ramp_up_capacity_threshold_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ramp_up_minimum_hosts_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#ramp_up_minimum_hosts_percent VirtualDesktopScalingPlan#ramp_up_minimum_hosts_percent}.'''
        result = self._values.get("ramp_up_minimum_hosts_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualDesktopScalingPlanSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualDesktopScalingPlanScheduleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualDesktopScalingPlan.VirtualDesktopScalingPlanScheduleList",
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
            type_hints = typing.get_type_hints(VirtualDesktopScalingPlanScheduleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualDesktopScalingPlanScheduleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualDesktopScalingPlanScheduleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualDesktopScalingPlanScheduleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualDesktopScalingPlanSchedule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualDesktopScalingPlanSchedule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualDesktopScalingPlanSchedule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualDesktopScalingPlanScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualDesktopScalingPlan.VirtualDesktopScalingPlanScheduleOutputReference",
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
            type_hints = typing.get_type_hints(VirtualDesktopScalingPlanScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetRampUpCapacityThresholdPercent")
    def reset_ramp_up_capacity_threshold_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRampUpCapacityThresholdPercent", []))

    @jsii.member(jsii_name="resetRampUpMinimumHostsPercent")
    def reset_ramp_up_minimum_hosts_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRampUpMinimumHostsPercent", []))

    @builtins.property
    @jsii.member(jsii_name="daysOfWeekInput")
    def days_of_week_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "daysOfWeekInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="offPeakLoadBalancingAlgorithmInput")
    def off_peak_load_balancing_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "offPeakLoadBalancingAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="offPeakStartTimeInput")
    def off_peak_start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "offPeakStartTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="peakLoadBalancingAlgorithmInput")
    def peak_load_balancing_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peakLoadBalancingAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="peakStartTimeInput")
    def peak_start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peakStartTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="rampDownCapacityThresholdPercentInput")
    def ramp_down_capacity_threshold_percent_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rampDownCapacityThresholdPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="rampDownForceLogoffUsersInput")
    def ramp_down_force_logoff_users_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "rampDownForceLogoffUsersInput"))

    @builtins.property
    @jsii.member(jsii_name="rampDownLoadBalancingAlgorithmInput")
    def ramp_down_load_balancing_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rampDownLoadBalancingAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="rampDownMinimumHostsPercentInput")
    def ramp_down_minimum_hosts_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rampDownMinimumHostsPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="rampDownNotificationMessageInput")
    def ramp_down_notification_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rampDownNotificationMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="rampDownStartTimeInput")
    def ramp_down_start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rampDownStartTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="rampDownStopHostsWhenInput")
    def ramp_down_stop_hosts_when_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rampDownStopHostsWhenInput"))

    @builtins.property
    @jsii.member(jsii_name="rampDownWaitTimeMinutesInput")
    def ramp_down_wait_time_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rampDownWaitTimeMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="rampUpCapacityThresholdPercentInput")
    def ramp_up_capacity_threshold_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rampUpCapacityThresholdPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="rampUpLoadBalancingAlgorithmInput")
    def ramp_up_load_balancing_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rampUpLoadBalancingAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="rampUpMinimumHostsPercentInput")
    def ramp_up_minimum_hosts_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rampUpMinimumHostsPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="rampUpStartTimeInput")
    def ramp_up_start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rampUpStartTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="daysOfWeek")
    def days_of_week(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "daysOfWeek"))

    @days_of_week.setter
    def days_of_week(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "days_of_week").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "daysOfWeek", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="offPeakLoadBalancingAlgorithm")
    def off_peak_load_balancing_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "offPeakLoadBalancingAlgorithm"))

    @off_peak_load_balancing_algorithm.setter
    def off_peak_load_balancing_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "off_peak_load_balancing_algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offPeakLoadBalancingAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="offPeakStartTime")
    def off_peak_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "offPeakStartTime"))

    @off_peak_start_time.setter
    def off_peak_start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "off_peak_start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offPeakStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="peakLoadBalancingAlgorithm")
    def peak_load_balancing_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peakLoadBalancingAlgorithm"))

    @peak_load_balancing_algorithm.setter
    def peak_load_balancing_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "peak_load_balancing_algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peakLoadBalancingAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="peakStartTime")
    def peak_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peakStartTime"))

    @peak_start_time.setter
    def peak_start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "peak_start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peakStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="rampDownCapacityThresholdPercent")
    def ramp_down_capacity_threshold_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rampDownCapacityThresholdPercent"))

    @ramp_down_capacity_threshold_percent.setter
    def ramp_down_capacity_threshold_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "ramp_down_capacity_threshold_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rampDownCapacityThresholdPercent", value)

    @builtins.property
    @jsii.member(jsii_name="rampDownForceLogoffUsers")
    def ramp_down_force_logoff_users(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "rampDownForceLogoffUsers"))

    @ramp_down_force_logoff_users.setter
    def ramp_down_force_logoff_users(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "ramp_down_force_logoff_users").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rampDownForceLogoffUsers", value)

    @builtins.property
    @jsii.member(jsii_name="rampDownLoadBalancingAlgorithm")
    def ramp_down_load_balancing_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rampDownLoadBalancingAlgorithm"))

    @ramp_down_load_balancing_algorithm.setter
    def ramp_down_load_balancing_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "ramp_down_load_balancing_algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rampDownLoadBalancingAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="rampDownMinimumHostsPercent")
    def ramp_down_minimum_hosts_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rampDownMinimumHostsPercent"))

    @ramp_down_minimum_hosts_percent.setter
    def ramp_down_minimum_hosts_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "ramp_down_minimum_hosts_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rampDownMinimumHostsPercent", value)

    @builtins.property
    @jsii.member(jsii_name="rampDownNotificationMessage")
    def ramp_down_notification_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rampDownNotificationMessage"))

    @ramp_down_notification_message.setter
    def ramp_down_notification_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "ramp_down_notification_message").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rampDownNotificationMessage", value)

    @builtins.property
    @jsii.member(jsii_name="rampDownStartTime")
    def ramp_down_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rampDownStartTime"))

    @ramp_down_start_time.setter
    def ramp_down_start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "ramp_down_start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rampDownStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="rampDownStopHostsWhen")
    def ramp_down_stop_hosts_when(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rampDownStopHostsWhen"))

    @ramp_down_stop_hosts_when.setter
    def ramp_down_stop_hosts_when(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "ramp_down_stop_hosts_when").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rampDownStopHostsWhen", value)

    @builtins.property
    @jsii.member(jsii_name="rampDownWaitTimeMinutes")
    def ramp_down_wait_time_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rampDownWaitTimeMinutes"))

    @ramp_down_wait_time_minutes.setter
    def ramp_down_wait_time_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "ramp_down_wait_time_minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rampDownWaitTimeMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="rampUpCapacityThresholdPercent")
    def ramp_up_capacity_threshold_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rampUpCapacityThresholdPercent"))

    @ramp_up_capacity_threshold_percent.setter
    def ramp_up_capacity_threshold_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "ramp_up_capacity_threshold_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rampUpCapacityThresholdPercent", value)

    @builtins.property
    @jsii.member(jsii_name="rampUpLoadBalancingAlgorithm")
    def ramp_up_load_balancing_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rampUpLoadBalancingAlgorithm"))

    @ramp_up_load_balancing_algorithm.setter
    def ramp_up_load_balancing_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "ramp_up_load_balancing_algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rampUpLoadBalancingAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="rampUpMinimumHostsPercent")
    def ramp_up_minimum_hosts_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rampUpMinimumHostsPercent"))

    @ramp_up_minimum_hosts_percent.setter
    def ramp_up_minimum_hosts_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "ramp_up_minimum_hosts_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rampUpMinimumHostsPercent", value)

    @builtins.property
    @jsii.member(jsii_name="rampUpStartTime")
    def ramp_up_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rampUpStartTime"))

    @ramp_up_start_time.setter
    def ramp_up_start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "ramp_up_start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rampUpStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualDesktopScalingPlanSchedule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualDesktopScalingPlanSchedule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualDesktopScalingPlanSchedule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualDesktopScalingPlan.VirtualDesktopScalingPlanTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class VirtualDesktopScalingPlanTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#create VirtualDesktopScalingPlan#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#delete VirtualDesktopScalingPlan#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#read VirtualDesktopScalingPlan#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#update VirtualDesktopScalingPlan#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualDesktopScalingPlanTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#create VirtualDesktopScalingPlan#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#delete VirtualDesktopScalingPlan#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#read VirtualDesktopScalingPlan#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_desktop_scaling_plan#update VirtualDesktopScalingPlan#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualDesktopScalingPlanTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualDesktopScalingPlanTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualDesktopScalingPlan.VirtualDesktopScalingPlanTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(VirtualDesktopScalingPlanTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

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
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

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
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualDesktopScalingPlanTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualDesktopScalingPlanTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualDesktopScalingPlanTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualDesktopScalingPlanTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VirtualDesktopScalingPlan",
    "VirtualDesktopScalingPlanConfig",
    "VirtualDesktopScalingPlanHostPool",
    "VirtualDesktopScalingPlanHostPoolList",
    "VirtualDesktopScalingPlanHostPoolOutputReference",
    "VirtualDesktopScalingPlanSchedule",
    "VirtualDesktopScalingPlanScheduleList",
    "VirtualDesktopScalingPlanScheduleOutputReference",
    "VirtualDesktopScalingPlanTimeouts",
    "VirtualDesktopScalingPlanTimeoutsOutputReference",
]

publication.publish()
