'''
# `spotinst_ocean_aks_virtual_node_group`

Refer to the Terraform Registory for docs: [`spotinst_ocean_aks_virtual_node_group`](https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group).
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


class OceanAksVirtualNodeGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group spotinst_ocean_aks_virtual_node_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        ocean_id: builtins.str,
        autoscale: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVirtualNodeGroupAutoscale", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVirtualNodeGroupLabel", typing.Dict[str, typing.Any]]]]] = None,
        launch_specification: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVirtualNodeGroupLaunchSpecification", typing.Dict[str, typing.Any]]]]] = None,
        resource_limits: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVirtualNodeGroupResourceLimits", typing.Dict[str, typing.Any]]]]] = None,
        taint: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVirtualNodeGroupTaint", typing.Dict[str, typing.Any]]]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group spotinst_ocean_aks_virtual_node_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#name OceanAksVirtualNodeGroup#name}.
        :param ocean_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#ocean_id OceanAksVirtualNodeGroup#ocean_id}.
        :param autoscale: autoscale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#autoscale OceanAksVirtualNodeGroup#autoscale}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#id OceanAksVirtualNodeGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param label: label block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#label OceanAksVirtualNodeGroup#label}
        :param launch_specification: launch_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#launch_specification OceanAksVirtualNodeGroup#launch_specification}
        :param resource_limits: resource_limits block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#resource_limits OceanAksVirtualNodeGroup#resource_limits}
        :param taint: taint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#taint OceanAksVirtualNodeGroup#taint}
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#zones OceanAksVirtualNodeGroup#zones}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OceanAksVirtualNodeGroupConfig(
            name=name,
            ocean_id=ocean_id,
            autoscale=autoscale,
            id=id,
            label=label,
            launch_specification=launch_specification,
            resource_limits=resource_limits,
            taint=taint,
            zones=zones,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAutoscale")
    def put_autoscale(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVirtualNodeGroupAutoscale", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroup.put_autoscale)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAutoscale", [value]))

    @jsii.member(jsii_name="putLabel")
    def put_label(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVirtualNodeGroupLabel", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroup.put_label)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLabel", [value]))

    @jsii.member(jsii_name="putLaunchSpecification")
    def put_launch_specification(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVirtualNodeGroupLaunchSpecification", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroup.put_launch_specification)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLaunchSpecification", [value]))

    @jsii.member(jsii_name="putResourceLimits")
    def put_resource_limits(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVirtualNodeGroupResourceLimits", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroup.put_resource_limits)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResourceLimits", [value]))

    @jsii.member(jsii_name="putTaint")
    def put_taint(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVirtualNodeGroupTaint", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroup.put_taint)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTaint", [value]))

    @jsii.member(jsii_name="resetAutoscale")
    def reset_autoscale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscale", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabel")
    def reset_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabel", []))

    @jsii.member(jsii_name="resetLaunchSpecification")
    def reset_launch_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchSpecification", []))

    @jsii.member(jsii_name="resetResourceLimits")
    def reset_resource_limits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceLimits", []))

    @jsii.member(jsii_name="resetTaint")
    def reset_taint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaint", []))

    @jsii.member(jsii_name="resetZones")
    def reset_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZones", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="autoscale")
    def autoscale(self) -> "OceanAksVirtualNodeGroupAutoscaleList":
        return typing.cast("OceanAksVirtualNodeGroupAutoscaleList", jsii.get(self, "autoscale"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> "OceanAksVirtualNodeGroupLabelList":
        return typing.cast("OceanAksVirtualNodeGroupLabelList", jsii.get(self, "label"))

    @builtins.property
    @jsii.member(jsii_name="launchSpecification")
    def launch_specification(self) -> "OceanAksVirtualNodeGroupLaunchSpecificationList":
        return typing.cast("OceanAksVirtualNodeGroupLaunchSpecificationList", jsii.get(self, "launchSpecification"))

    @builtins.property
    @jsii.member(jsii_name="resourceLimits")
    def resource_limits(self) -> "OceanAksVirtualNodeGroupResourceLimitsList":
        return typing.cast("OceanAksVirtualNodeGroupResourceLimitsList", jsii.get(self, "resourceLimits"))

    @builtins.property
    @jsii.member(jsii_name="taint")
    def taint(self) -> "OceanAksVirtualNodeGroupTaintList":
        return typing.cast("OceanAksVirtualNodeGroupTaintList", jsii.get(self, "taint"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleInput")
    def autoscale_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupAutoscale"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupAutoscale"]]], jsii.get(self, "autoscaleInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupLabel"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupLabel"]]], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="launchSpecificationInput")
    def launch_specification_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupLaunchSpecification"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupLaunchSpecification"]]], jsii.get(self, "launchSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="oceanIdInput")
    def ocean_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oceanIdInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLimitsInput")
    def resource_limits_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupResourceLimits"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupResourceLimits"]]], jsii.get(self, "resourceLimitsInput"))

    @builtins.property
    @jsii.member(jsii_name="taintInput")
    def taint_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupTaint"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupTaint"]]], jsii.get(self, "taintInput"))

    @builtins.property
    @jsii.member(jsii_name="zonesInput")
    def zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "zonesInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroup, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="oceanId")
    def ocean_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oceanId"))

    @ocean_id.setter
    def ocean_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroup, "ocean_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oceanId", value)

    @builtins.property
    @jsii.member(jsii_name="zones")
    def zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "zones"))

    @zones.setter
    def zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroup, "zones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zones", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupAutoscale",
    jsii_struct_bases=[],
    name_mapping={
        "auto_headroom_percentage": "autoHeadroomPercentage",
        "autoscale_headroom": "autoscaleHeadroom",
    },
)
class OceanAksVirtualNodeGroupAutoscale:
    def __init__(
        self,
        *,
        auto_headroom_percentage: typing.Optional[jsii.Number] = None,
        autoscale_headroom: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroom", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param auto_headroom_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#auto_headroom_percentage OceanAksVirtualNodeGroup#auto_headroom_percentage}.
        :param autoscale_headroom: autoscale_headroom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#autoscale_headroom OceanAksVirtualNodeGroup#autoscale_headroom}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupAutoscale.__init__)
            check_type(argname="argument auto_headroom_percentage", value=auto_headroom_percentage, expected_type=type_hints["auto_headroom_percentage"])
            check_type(argname="argument autoscale_headroom", value=autoscale_headroom, expected_type=type_hints["autoscale_headroom"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_headroom_percentage is not None:
            self._values["auto_headroom_percentage"] = auto_headroom_percentage
        if autoscale_headroom is not None:
            self._values["autoscale_headroom"] = autoscale_headroom

    @builtins.property
    def auto_headroom_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#auto_headroom_percentage OceanAksVirtualNodeGroup#auto_headroom_percentage}.'''
        result = self._values.get("auto_headroom_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def autoscale_headroom(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroom"]]]:
        '''autoscale_headroom block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#autoscale_headroom OceanAksVirtualNodeGroup#autoscale_headroom}
        '''
        result = self._values.get("autoscale_headroom")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroom"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksVirtualNodeGroupAutoscale(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroom",
    jsii_struct_bases=[],
    name_mapping={
        "num_of_units": "numOfUnits",
        "cpu_per_unit": "cpuPerUnit",
        "gpu_per_unit": "gpuPerUnit",
        "memory_per_unit": "memoryPerUnit",
    },
)
class OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroom:
    def __init__(
        self,
        *,
        num_of_units: jsii.Number,
        cpu_per_unit: typing.Optional[jsii.Number] = None,
        gpu_per_unit: typing.Optional[jsii.Number] = None,
        memory_per_unit: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param num_of_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#num_of_units OceanAksVirtualNodeGroup#num_of_units}.
        :param cpu_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#cpu_per_unit OceanAksVirtualNodeGroup#cpu_per_unit}.
        :param gpu_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#gpu_per_unit OceanAksVirtualNodeGroup#gpu_per_unit}.
        :param memory_per_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#memory_per_unit OceanAksVirtualNodeGroup#memory_per_unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroom.__init__)
            check_type(argname="argument num_of_units", value=num_of_units, expected_type=type_hints["num_of_units"])
            check_type(argname="argument cpu_per_unit", value=cpu_per_unit, expected_type=type_hints["cpu_per_unit"])
            check_type(argname="argument gpu_per_unit", value=gpu_per_unit, expected_type=type_hints["gpu_per_unit"])
            check_type(argname="argument memory_per_unit", value=memory_per_unit, expected_type=type_hints["memory_per_unit"])
        self._values: typing.Dict[str, typing.Any] = {
            "num_of_units": num_of_units,
        }
        if cpu_per_unit is not None:
            self._values["cpu_per_unit"] = cpu_per_unit
        if gpu_per_unit is not None:
            self._values["gpu_per_unit"] = gpu_per_unit
        if memory_per_unit is not None:
            self._values["memory_per_unit"] = memory_per_unit

    @builtins.property
    def num_of_units(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#num_of_units OceanAksVirtualNodeGroup#num_of_units}.'''
        result = self._values.get("num_of_units")
        assert result is not None, "Required property 'num_of_units' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def cpu_per_unit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#cpu_per_unit OceanAksVirtualNodeGroup#cpu_per_unit}.'''
        result = self._values.get("cpu_per_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def gpu_per_unit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#gpu_per_unit OceanAksVirtualNodeGroup#gpu_per_unit}.'''
        result = self._values.get("gpu_per_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_per_unit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#memory_per_unit OceanAksVirtualNodeGroup#memory_per_unit}.'''
        result = self._values.get("memory_per_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomList",
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
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroom]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroom]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroom]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCpuPerUnit")
    def reset_cpu_per_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuPerUnit", []))

    @jsii.member(jsii_name="resetGpuPerUnit")
    def reset_gpu_per_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGpuPerUnit", []))

    @jsii.member(jsii_name="resetMemoryPerUnit")
    def reset_memory_per_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryPerUnit", []))

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
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomOutputReference, "cpu_per_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuPerUnit", value)

    @builtins.property
    @jsii.member(jsii_name="gpuPerUnit")
    def gpu_per_unit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gpuPerUnit"))

    @gpu_per_unit.setter
    def gpu_per_unit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomOutputReference, "gpu_per_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gpuPerUnit", value)

    @builtins.property
    @jsii.member(jsii_name="memoryPerUnit")
    def memory_per_unit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryPerUnit"))

    @memory_per_unit.setter
    def memory_per_unit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomOutputReference, "memory_per_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryPerUnit", value)

    @builtins.property
    @jsii.member(jsii_name="numOfUnits")
    def num_of_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numOfUnits"))

    @num_of_units.setter
    def num_of_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomOutputReference, "num_of_units").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numOfUnits", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroom, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroom, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroom, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksVirtualNodeGroupAutoscaleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupAutoscaleList",
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
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupAutoscaleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OceanAksVirtualNodeGroupAutoscaleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupAutoscaleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAksVirtualNodeGroupAutoscaleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupAutoscaleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupAutoscaleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupAutoscaleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupAutoscale]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupAutoscale]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupAutoscale]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupAutoscaleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksVirtualNodeGroupAutoscaleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupAutoscaleOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupAutoscaleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAutoscaleHeadroom")
    def put_autoscale_headroom(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroom, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupAutoscaleOutputReference.put_autoscale_headroom)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAutoscaleHeadroom", [value]))

    @jsii.member(jsii_name="resetAutoHeadroomPercentage")
    def reset_auto_headroom_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoHeadroomPercentage", []))

    @jsii.member(jsii_name="resetAutoscaleHeadroom")
    def reset_autoscale_headroom(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaleHeadroom", []))

    @builtins.property
    @jsii.member(jsii_name="autoscaleHeadroom")
    def autoscale_headroom(
        self,
    ) -> OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomList:
        return typing.cast(OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomList, jsii.get(self, "autoscaleHeadroom"))

    @builtins.property
    @jsii.member(jsii_name="autoHeadroomPercentageInput")
    def auto_headroom_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autoHeadroomPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleHeadroomInput")
    def autoscale_headroom_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroom]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroom]]], jsii.get(self, "autoscaleHeadroomInput"))

    @builtins.property
    @jsii.member(jsii_name="autoHeadroomPercentage")
    def auto_headroom_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autoHeadroomPercentage"))

    @auto_headroom_percentage.setter
    def auto_headroom_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupAutoscaleOutputReference, "auto_headroom_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoHeadroomPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAksVirtualNodeGroupAutoscale, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAksVirtualNodeGroupAutoscale, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAksVirtualNodeGroupAutoscale, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupAutoscaleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupConfig",
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
        "autoscale": "autoscale",
        "id": "id",
        "label": "label",
        "launch_specification": "launchSpecification",
        "resource_limits": "resourceLimits",
        "taint": "taint",
        "zones": "zones",
    },
)
class OceanAksVirtualNodeGroupConfig(cdktf.TerraformMetaArguments):
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
        autoscale: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OceanAksVirtualNodeGroupAutoscale, typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVirtualNodeGroupLabel", typing.Dict[str, typing.Any]]]]] = None,
        launch_specification: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVirtualNodeGroupLaunchSpecification", typing.Dict[str, typing.Any]]]]] = None,
        resource_limits: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVirtualNodeGroupResourceLimits", typing.Dict[str, typing.Any]]]]] = None,
        taint: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVirtualNodeGroupTaint", typing.Dict[str, typing.Any]]]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#name OceanAksVirtualNodeGroup#name}.
        :param ocean_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#ocean_id OceanAksVirtualNodeGroup#ocean_id}.
        :param autoscale: autoscale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#autoscale OceanAksVirtualNodeGroup#autoscale}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#id OceanAksVirtualNodeGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param label: label block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#label OceanAksVirtualNodeGroup#label}
        :param launch_specification: launch_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#launch_specification OceanAksVirtualNodeGroup#launch_specification}
        :param resource_limits: resource_limits block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#resource_limits OceanAksVirtualNodeGroup#resource_limits}
        :param taint: taint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#taint OceanAksVirtualNodeGroup#taint}
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#zones OceanAksVirtualNodeGroup#zones}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument ocean_id", value=ocean_id, expected_type=type_hints["ocean_id"])
            check_type(argname="argument autoscale", value=autoscale, expected_type=type_hints["autoscale"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument launch_specification", value=launch_specification, expected_type=type_hints["launch_specification"])
            check_type(argname="argument resource_limits", value=resource_limits, expected_type=type_hints["resource_limits"])
            check_type(argname="argument taint", value=taint, expected_type=type_hints["taint"])
            check_type(argname="argument zones", value=zones, expected_type=type_hints["zones"])
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
        if autoscale is not None:
            self._values["autoscale"] = autoscale
        if id is not None:
            self._values["id"] = id
        if label is not None:
            self._values["label"] = label
        if launch_specification is not None:
            self._values["launch_specification"] = launch_specification
        if resource_limits is not None:
            self._values["resource_limits"] = resource_limits
        if taint is not None:
            self._values["taint"] = taint
        if zones is not None:
            self._values["zones"] = zones

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#name OceanAksVirtualNodeGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ocean_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#ocean_id OceanAksVirtualNodeGroup#ocean_id}.'''
        result = self._values.get("ocean_id")
        assert result is not None, "Required property 'ocean_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def autoscale(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupAutoscale]]]:
        '''autoscale block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#autoscale OceanAksVirtualNodeGroup#autoscale}
        '''
        result = self._values.get("autoscale")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupAutoscale]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#id OceanAksVirtualNodeGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupLabel"]]]:
        '''label block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#label OceanAksVirtualNodeGroup#label}
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupLabel"]]], result)

    @builtins.property
    def launch_specification(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupLaunchSpecification"]]]:
        '''launch_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#launch_specification OceanAksVirtualNodeGroup#launch_specification}
        '''
        result = self._values.get("launch_specification")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupLaunchSpecification"]]], result)

    @builtins.property
    def resource_limits(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupResourceLimits"]]]:
        '''resource_limits block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#resource_limits OceanAksVirtualNodeGroup#resource_limits}
        '''
        result = self._values.get("resource_limits")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupResourceLimits"]]], result)

    @builtins.property
    def taint(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupTaint"]]]:
        '''taint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#taint OceanAksVirtualNodeGroup#taint}
        '''
        result = self._values.get("taint")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupTaint"]]], result)

    @builtins.property
    def zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#zones OceanAksVirtualNodeGroup#zones}.'''
        result = self._values.get("zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksVirtualNodeGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupLabel",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class OceanAksVirtualNodeGroupLabel:
    def __init__(
        self,
        *,
        key: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#key OceanAksVirtualNodeGroup#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#value OceanAksVirtualNodeGroup#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupLabel.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
        }
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#key OceanAksVirtualNodeGroup#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#value OceanAksVirtualNodeGroup#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksVirtualNodeGroupLabel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksVirtualNodeGroupLabelList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupLabelList",
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
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupLabelList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanAksVirtualNodeGroupLabelOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupLabelList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAksVirtualNodeGroupLabelOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLabelList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLabelList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLabelList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupLabel]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupLabel]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupLabel]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLabelList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksVirtualNodeGroupLabelOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupLabelOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupLabelOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLabelOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLabelOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAksVirtualNodeGroupLabel, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAksVirtualNodeGroupLabel, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAksVirtualNodeGroupLabel, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLabelOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupLaunchSpecification",
    jsii_struct_bases=[],
    name_mapping={"max_pods": "maxPods", "os_disk": "osDisk", "tag": "tag"},
)
class OceanAksVirtualNodeGroupLaunchSpecification:
    def __init__(
        self,
        *,
        max_pods: typing.Optional[jsii.Number] = None,
        os_disk: typing.Optional[typing.Union["OceanAksVirtualNodeGroupLaunchSpecificationOsDisk", typing.Dict[str, typing.Any]]] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVirtualNodeGroupLaunchSpecificationTag", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param max_pods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#max_pods OceanAksVirtualNodeGroup#max_pods}.
        :param os_disk: os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#os_disk OceanAksVirtualNodeGroup#os_disk}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#tag OceanAksVirtualNodeGroup#tag}
        '''
        if isinstance(os_disk, dict):
            os_disk = OceanAksVirtualNodeGroupLaunchSpecificationOsDisk(**os_disk)
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupLaunchSpecification.__init__)
            check_type(argname="argument max_pods", value=max_pods, expected_type=type_hints["max_pods"])
            check_type(argname="argument os_disk", value=os_disk, expected_type=type_hints["os_disk"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_pods is not None:
            self._values["max_pods"] = max_pods
        if os_disk is not None:
            self._values["os_disk"] = os_disk
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def max_pods(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#max_pods OceanAksVirtualNodeGroup#max_pods}.'''
        result = self._values.get("max_pods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def os_disk(
        self,
    ) -> typing.Optional["OceanAksVirtualNodeGroupLaunchSpecificationOsDisk"]:
        '''os_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#os_disk OceanAksVirtualNodeGroup#os_disk}
        '''
        result = self._values.get("os_disk")
        return typing.cast(typing.Optional["OceanAksVirtualNodeGroupLaunchSpecificationOsDisk"], result)

    @builtins.property
    def tag(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupLaunchSpecificationTag"]]]:
        '''tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#tag OceanAksVirtualNodeGroup#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupLaunchSpecificationTag"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksVirtualNodeGroupLaunchSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksVirtualNodeGroupLaunchSpecificationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupLaunchSpecificationList",
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
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupLaunchSpecificationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OceanAksVirtualNodeGroupLaunchSpecificationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupLaunchSpecificationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAksVirtualNodeGroupLaunchSpecificationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLaunchSpecificationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLaunchSpecificationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLaunchSpecificationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupLaunchSpecification]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupLaunchSpecification]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupLaunchSpecification]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLaunchSpecificationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupLaunchSpecificationOsDisk",
    jsii_struct_bases=[],
    name_mapping={
        "size_gb": "sizeGb",
        "type": "type",
        "utilize_ephemeral_storage": "utilizeEphemeralStorage",
    },
)
class OceanAksVirtualNodeGroupLaunchSpecificationOsDisk:
    def __init__(
        self,
        *,
        size_gb: jsii.Number,
        type: typing.Optional[builtins.str] = None,
        utilize_ephemeral_storage: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#size_gb OceanAksVirtualNodeGroup#size_gb}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#type OceanAksVirtualNodeGroup#type}.
        :param utilize_ephemeral_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#utilize_ephemeral_storage OceanAksVirtualNodeGroup#utilize_ephemeral_storage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupLaunchSpecificationOsDisk.__init__)
            check_type(argname="argument size_gb", value=size_gb, expected_type=type_hints["size_gb"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument utilize_ephemeral_storage", value=utilize_ephemeral_storage, expected_type=type_hints["utilize_ephemeral_storage"])
        self._values: typing.Dict[str, typing.Any] = {
            "size_gb": size_gb,
        }
        if type is not None:
            self._values["type"] = type
        if utilize_ephemeral_storage is not None:
            self._values["utilize_ephemeral_storage"] = utilize_ephemeral_storage

    @builtins.property
    def size_gb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#size_gb OceanAksVirtualNodeGroup#size_gb}.'''
        result = self._values.get("size_gb")
        assert result is not None, "Required property 'size_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#type OceanAksVirtualNodeGroup#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def utilize_ephemeral_storage(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#utilize_ephemeral_storage OceanAksVirtualNodeGroup#utilize_ephemeral_storage}.'''
        result = self._values.get("utilize_ephemeral_storage")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksVirtualNodeGroupLaunchSpecificationOsDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksVirtualNodeGroupLaunchSpecificationOsDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupLaunchSpecificationOsDiskOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupLaunchSpecificationOsDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetUtilizeEphemeralStorage")
    def reset_utilize_ephemeral_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUtilizeEphemeralStorage", []))

    @builtins.property
    @jsii.member(jsii_name="sizeGbInput")
    def size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="utilizeEphemeralStorageInput")
    def utilize_ephemeral_storage_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "utilizeEphemeralStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeGb")
    def size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeGb"))

    @size_gb.setter
    def size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLaunchSpecificationOsDiskOutputReference, "size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLaunchSpecificationOsDiskOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="utilizeEphemeralStorage")
    def utilize_ephemeral_storage(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "utilizeEphemeralStorage"))

    @utilize_ephemeral_storage.setter
    def utilize_ephemeral_storage(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLaunchSpecificationOsDiskOutputReference, "utilize_ephemeral_storage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "utilizeEphemeralStorage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OceanAksVirtualNodeGroupLaunchSpecificationOsDisk]:
        return typing.cast(typing.Optional[OceanAksVirtualNodeGroupLaunchSpecificationOsDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OceanAksVirtualNodeGroupLaunchSpecificationOsDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLaunchSpecificationOsDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksVirtualNodeGroupLaunchSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupLaunchSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupLaunchSpecificationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putOsDisk")
    def put_os_disk(
        self,
        *,
        size_gb: jsii.Number,
        type: typing.Optional[builtins.str] = None,
        utilize_ephemeral_storage: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#size_gb OceanAksVirtualNodeGroup#size_gb}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#type OceanAksVirtualNodeGroup#type}.
        :param utilize_ephemeral_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#utilize_ephemeral_storage OceanAksVirtualNodeGroup#utilize_ephemeral_storage}.
        '''
        value = OceanAksVirtualNodeGroupLaunchSpecificationOsDisk(
            size_gb=size_gb,
            type=type,
            utilize_ephemeral_storage=utilize_ephemeral_storage,
        )

        return typing.cast(None, jsii.invoke(self, "putOsDisk", [value]))

    @jsii.member(jsii_name="putTag")
    def put_tag(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OceanAksVirtualNodeGroupLaunchSpecificationTag", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupLaunchSpecificationOutputReference.put_tag)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTag", [value]))

    @jsii.member(jsii_name="resetMaxPods")
    def reset_max_pods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxPods", []))

    @jsii.member(jsii_name="resetOsDisk")
    def reset_os_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsDisk", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @builtins.property
    @jsii.member(jsii_name="osDisk")
    def os_disk(
        self,
    ) -> OceanAksVirtualNodeGroupLaunchSpecificationOsDiskOutputReference:
        return typing.cast(OceanAksVirtualNodeGroupLaunchSpecificationOsDiskOutputReference, jsii.get(self, "osDisk"))

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> "OceanAksVirtualNodeGroupLaunchSpecificationTagList":
        return typing.cast("OceanAksVirtualNodeGroupLaunchSpecificationTagList", jsii.get(self, "tag"))

    @builtins.property
    @jsii.member(jsii_name="maxPodsInput")
    def max_pods_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxPodsInput"))

    @builtins.property
    @jsii.member(jsii_name="osDiskInput")
    def os_disk_input(
        self,
    ) -> typing.Optional[OceanAksVirtualNodeGroupLaunchSpecificationOsDisk]:
        return typing.cast(typing.Optional[OceanAksVirtualNodeGroupLaunchSpecificationOsDisk], jsii.get(self, "osDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupLaunchSpecificationTag"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OceanAksVirtualNodeGroupLaunchSpecificationTag"]]], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPods")
    def max_pods(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPods"))

    @max_pods.setter
    def max_pods(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLaunchSpecificationOutputReference, "max_pods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPods", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAksVirtualNodeGroupLaunchSpecification, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAksVirtualNodeGroupLaunchSpecification, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAksVirtualNodeGroupLaunchSpecification, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLaunchSpecificationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupLaunchSpecificationTag",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class OceanAksVirtualNodeGroupLaunchSpecificationTag:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#key OceanAksVirtualNodeGroup#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#value OceanAksVirtualNodeGroup#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupLaunchSpecificationTag.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#key OceanAksVirtualNodeGroup#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#value OceanAksVirtualNodeGroup#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksVirtualNodeGroupLaunchSpecificationTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksVirtualNodeGroupLaunchSpecificationTagList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupLaunchSpecificationTagList",
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
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupLaunchSpecificationTagList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OceanAksVirtualNodeGroupLaunchSpecificationTagOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupLaunchSpecificationTagList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAksVirtualNodeGroupLaunchSpecificationTagOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLaunchSpecificationTagList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLaunchSpecificationTagList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLaunchSpecificationTagList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupLaunchSpecificationTag]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupLaunchSpecificationTag]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupLaunchSpecificationTag]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLaunchSpecificationTagList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksVirtualNodeGroupLaunchSpecificationTagOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupLaunchSpecificationTagOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupLaunchSpecificationTagOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLaunchSpecificationTagOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLaunchSpecificationTagOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAksVirtualNodeGroupLaunchSpecificationTag, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAksVirtualNodeGroupLaunchSpecificationTag, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAksVirtualNodeGroupLaunchSpecificationTag, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupLaunchSpecificationTagOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupResourceLimits",
    jsii_struct_bases=[],
    name_mapping={"max_instance_count": "maxInstanceCount"},
)
class OceanAksVirtualNodeGroupResourceLimits:
    def __init__(
        self,
        *,
        max_instance_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#max_instance_count OceanAksVirtualNodeGroup#max_instance_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupResourceLimits.__init__)
            check_type(argname="argument max_instance_count", value=max_instance_count, expected_type=type_hints["max_instance_count"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_instance_count is not None:
            self._values["max_instance_count"] = max_instance_count

    @builtins.property
    def max_instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#max_instance_count OceanAksVirtualNodeGroup#max_instance_count}.'''
        result = self._values.get("max_instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksVirtualNodeGroupResourceLimits(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksVirtualNodeGroupResourceLimitsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupResourceLimitsList",
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
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupResourceLimitsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OceanAksVirtualNodeGroupResourceLimitsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupResourceLimitsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAksVirtualNodeGroupResourceLimitsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupResourceLimitsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupResourceLimitsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupResourceLimitsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupResourceLimits]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupResourceLimits]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupResourceLimits]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupResourceLimitsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksVirtualNodeGroupResourceLimitsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupResourceLimitsOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupResourceLimitsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMaxInstanceCount")
    def reset_max_instance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxInstanceCount", []))

    @builtins.property
    @jsii.member(jsii_name="maxInstanceCountInput")
    def max_instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInstanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="maxInstanceCount")
    def max_instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxInstanceCount"))

    @max_instance_count.setter
    def max_instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupResourceLimitsOutputReference, "max_instance_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxInstanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAksVirtualNodeGroupResourceLimits, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAksVirtualNodeGroupResourceLimits, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAksVirtualNodeGroupResourceLimits, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupResourceLimitsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupTaint",
    jsii_struct_bases=[],
    name_mapping={"effect": "effect", "key": "key", "value": "value"},
)
class OceanAksVirtualNodeGroupTaint:
    def __init__(
        self,
        *,
        effect: builtins.str,
        key: builtins.str,
        value: builtins.str,
    ) -> None:
        '''
        :param effect: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#effect OceanAksVirtualNodeGroup#effect}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#key OceanAksVirtualNodeGroup#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#value OceanAksVirtualNodeGroup#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupTaint.__init__)
            check_type(argname="argument effect", value=effect, expected_type=type_hints["effect"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "effect": effect,
            "key": key,
            "value": value,
        }

    @builtins.property
    def effect(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#effect OceanAksVirtualNodeGroup#effect}.'''
        result = self._values.get("effect")
        assert result is not None, "Required property 'effect' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#key OceanAksVirtualNodeGroup#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_aks_virtual_node_group#value OceanAksVirtualNodeGroup#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OceanAksVirtualNodeGroupTaint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OceanAksVirtualNodeGroupTaintList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupTaintList",
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
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupTaintList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OceanAksVirtualNodeGroupTaintOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupTaintList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OceanAksVirtualNodeGroupTaintOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupTaintList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupTaintList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupTaintList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupTaint]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupTaint]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OceanAksVirtualNodeGroupTaint]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupTaintList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OceanAksVirtualNodeGroupTaintOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.oceanAksVirtualNodeGroup.OceanAksVirtualNodeGroupTaintOutputReference",
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
            type_hints = typing.get_type_hints(OceanAksVirtualNodeGroupTaintOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="effectInput")
    def effect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "effectInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="effect")
    def effect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "effect"))

    @effect.setter
    def effect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupTaintOutputReference, "effect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "effect", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupTaintOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupTaintOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OceanAksVirtualNodeGroupTaint, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OceanAksVirtualNodeGroupTaint, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OceanAksVirtualNodeGroupTaint, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OceanAksVirtualNodeGroupTaintOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "OceanAksVirtualNodeGroup",
    "OceanAksVirtualNodeGroupAutoscale",
    "OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroom",
    "OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomList",
    "OceanAksVirtualNodeGroupAutoscaleAutoscaleHeadroomOutputReference",
    "OceanAksVirtualNodeGroupAutoscaleList",
    "OceanAksVirtualNodeGroupAutoscaleOutputReference",
    "OceanAksVirtualNodeGroupConfig",
    "OceanAksVirtualNodeGroupLabel",
    "OceanAksVirtualNodeGroupLabelList",
    "OceanAksVirtualNodeGroupLabelOutputReference",
    "OceanAksVirtualNodeGroupLaunchSpecification",
    "OceanAksVirtualNodeGroupLaunchSpecificationList",
    "OceanAksVirtualNodeGroupLaunchSpecificationOsDisk",
    "OceanAksVirtualNodeGroupLaunchSpecificationOsDiskOutputReference",
    "OceanAksVirtualNodeGroupLaunchSpecificationOutputReference",
    "OceanAksVirtualNodeGroupLaunchSpecificationTag",
    "OceanAksVirtualNodeGroupLaunchSpecificationTagList",
    "OceanAksVirtualNodeGroupLaunchSpecificationTagOutputReference",
    "OceanAksVirtualNodeGroupResourceLimits",
    "OceanAksVirtualNodeGroupResourceLimitsList",
    "OceanAksVirtualNodeGroupResourceLimitsOutputReference",
    "OceanAksVirtualNodeGroupTaint",
    "OceanAksVirtualNodeGroupTaintList",
    "OceanAksVirtualNodeGroupTaintOutputReference",
]

publication.publish()
