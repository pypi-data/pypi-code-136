'''
# `ionoscloud_k8s_node_pool`

Refer to the Terraform Registory for docs: [`ionoscloud_k8s_node_pool`](https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool).
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


class K8SNodePool(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.k8SNodePool.K8SNodePool",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool ionoscloud_k8s_node_pool}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        availability_zone: builtins.str,
        cores_count: jsii.Number,
        cpu_family: builtins.str,
        datacenter_id: builtins.str,
        k8_s_cluster_id: builtins.str,
        k8_s_version: builtins.str,
        name: builtins.str,
        node_count: jsii.Number,
        ram_size: jsii.Number,
        storage_size: jsii.Number,
        storage_type: builtins.str,
        allow_replace: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        auto_scaling: typing.Optional[typing.Union["K8SNodePoolAutoScaling", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        lans: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["K8SNodePoolLans", typing.Dict[str, typing.Any]]]]] = None,
        maintenance_window: typing.Optional[typing.Union["K8SNodePoolMaintenanceWindow", typing.Dict[str, typing.Any]]] = None,
        public_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["K8SNodePoolTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool ionoscloud_k8s_node_pool} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param availability_zone: The compute availability zone in which the nodes should exist. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#availability_zone K8SNodePool#availability_zone}
        :param cores_count: CPU cores count. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#cores_count K8SNodePool#cores_count}
        :param cpu_family: CPU Family. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#cpu_family K8SNodePool#cpu_family}
        :param datacenter_id: The UUID of the VDC. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#datacenter_id K8SNodePool#datacenter_id}
        :param k8_s_cluster_id: The UUID of an existing kubernetes cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#k8s_cluster_id K8SNodePool#k8s_cluster_id}
        :param k8_s_version: The desired kubernetes version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#k8s_version K8SNodePool#k8s_version}
        :param name: The desired name for the node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#name K8SNodePool#name}
        :param node_count: The number of nodes in this node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#node_count K8SNodePool#node_count}
        :param ram_size: The amount of RAM in MB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#ram_size K8SNodePool#ram_size}
        :param storage_size: The total allocated storage capacity of a node in GB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#storage_size K8SNodePool#storage_size}
        :param storage_type: Storage type to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#storage_type K8SNodePool#storage_type}
        :param allow_replace: When set to true, allows the update of immutable fields by destroying and re-creating the node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#allow_replace K8SNodePool#allow_replace}
        :param annotations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#annotations K8SNodePool#annotations}.
        :param auto_scaling: auto_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#auto_scaling K8SNodePool#auto_scaling}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#id K8SNodePool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#labels K8SNodePool#labels}.
        :param lans: lans block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#lans K8SNodePool#lans}
        :param maintenance_window: maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#maintenance_window K8SNodePool#maintenance_window}
        :param public_ips: A list of fixed IPs. Cannot be set on private clusters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#public_ips K8SNodePool#public_ips}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#timeouts K8SNodePool#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(K8SNodePool.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = K8SNodePoolConfig(
            availability_zone=availability_zone,
            cores_count=cores_count,
            cpu_family=cpu_family,
            datacenter_id=datacenter_id,
            k8_s_cluster_id=k8_s_cluster_id,
            k8_s_version=k8_s_version,
            name=name,
            node_count=node_count,
            ram_size=ram_size,
            storage_size=storage_size,
            storage_type=storage_type,
            allow_replace=allow_replace,
            annotations=annotations,
            auto_scaling=auto_scaling,
            id=id,
            labels=labels,
            lans=lans,
            maintenance_window=maintenance_window,
            public_ips=public_ips,
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

    @jsii.member(jsii_name="putAutoScaling")
    def put_auto_scaling(
        self,
        *,
        max_node_count: jsii.Number,
        min_node_count: jsii.Number,
    ) -> None:
        '''
        :param max_node_count: The maximum number of worker nodes that the node pool can scale to. Should be greater than min_node_count. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#max_node_count K8SNodePool#max_node_count}
        :param min_node_count: The minimum number of worker nodes the node pool can scale down to. Should be less than max_node_count. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#min_node_count K8SNodePool#min_node_count}
        '''
        value = K8SNodePoolAutoScaling(
            max_node_count=max_node_count, min_node_count=min_node_count
        )

        return typing.cast(None, jsii.invoke(self, "putAutoScaling", [value]))

    @jsii.member(jsii_name="putLans")
    def put_lans(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["K8SNodePoolLans", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(K8SNodePool.put_lans)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLans", [value]))

    @jsii.member(jsii_name="putMaintenanceWindow")
    def put_maintenance_window(
        self,
        *,
        day_of_the_week: builtins.str,
        time: builtins.str,
    ) -> None:
        '''
        :param day_of_the_week: Day of the week when maintenance is allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#day_of_the_week K8SNodePool#day_of_the_week}
        :param time: A clock time in the day when maintenance is allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#time K8SNodePool#time}
        '''
        value = K8SNodePoolMaintenanceWindow(
            day_of_the_week=day_of_the_week, time=time
        )

        return typing.cast(None, jsii.invoke(self, "putMaintenanceWindow", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#create K8SNodePool#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#default K8SNodePool#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#delete K8SNodePool#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#update K8SNodePool#update}.
        '''
        value = K8SNodePoolTimeouts(
            create=create, default=default, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAllowReplace")
    def reset_allow_replace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowReplace", []))

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetAutoScaling")
    def reset_auto_scaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoScaling", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLans")
    def reset_lans(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLans", []))

    @jsii.member(jsii_name="resetMaintenanceWindow")
    def reset_maintenance_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceWindow", []))

    @jsii.member(jsii_name="resetPublicIps")
    def reset_public_ips(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicIps", []))

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
    @jsii.member(jsii_name="autoScaling")
    def auto_scaling(self) -> "K8SNodePoolAutoScalingOutputReference":
        return typing.cast("K8SNodePoolAutoScalingOutputReference", jsii.get(self, "autoScaling"))

    @builtins.property
    @jsii.member(jsii_name="lans")
    def lans(self) -> "K8SNodePoolLansList":
        return typing.cast("K8SNodePoolLansList", jsii.get(self, "lans"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindow")
    def maintenance_window(self) -> "K8SNodePoolMaintenanceWindowOutputReference":
        return typing.cast("K8SNodePoolMaintenanceWindowOutputReference", jsii.get(self, "maintenanceWindow"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "K8SNodePoolTimeoutsOutputReference":
        return typing.cast("K8SNodePoolTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="allowReplaceInput")
    def allow_replace_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowReplaceInput"))

    @builtins.property
    @jsii.member(jsii_name="annotationsInput")
    def annotations_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "annotationsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoScalingInput")
    def auto_scaling_input(self) -> typing.Optional["K8SNodePoolAutoScaling"]:
        return typing.cast(typing.Optional["K8SNodePoolAutoScaling"], jsii.get(self, "autoScalingInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneInput")
    def availability_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="coresCountInput")
    def cores_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "coresCountInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuFamilyInput")
    def cpu_family_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuFamilyInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterIdInput")
    def datacenter_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datacenterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="k8SClusterIdInput")
    def k8_s_cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "k8SClusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="k8SVersionInput")
    def k8_s_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "k8SVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="lansInput")
    def lans_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["K8SNodePoolLans"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["K8SNodePoolLans"]]], jsii.get(self, "lansInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowInput")
    def maintenance_window_input(
        self,
    ) -> typing.Optional["K8SNodePoolMaintenanceWindow"]:
        return typing.cast(typing.Optional["K8SNodePoolMaintenanceWindow"], jsii.get(self, "maintenanceWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeCountInput")
    def node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="publicIpsInput")
    def public_ips_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "publicIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="ramSizeInput")
    def ram_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ramSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="storageSizeInput")
    def storage_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="storageTypeInput")
    def storage_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["K8SNodePoolTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["K8SNodePoolTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowReplace")
    def allow_replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowReplace"))

    @allow_replace.setter
    def allow_replace(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePool, "allow_replace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowReplace", value)

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePool, "annotations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePool, "availability_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="coresCount")
    def cores_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "coresCount"))

    @cores_count.setter
    def cores_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePool, "cores_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coresCount", value)

    @builtins.property
    @jsii.member(jsii_name="cpuFamily")
    def cpu_family(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpuFamily"))

    @cpu_family.setter
    def cpu_family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePool, "cpu_family").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuFamily", value)

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datacenterId"))

    @datacenter_id.setter
    def datacenter_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePool, "datacenter_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenterId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePool, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="k8SClusterId")
    def k8_s_cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "k8SClusterId"))

    @k8_s_cluster_id.setter
    def k8_s_cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePool, "k8_s_cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "k8SClusterId", value)

    @builtins.property
    @jsii.member(jsii_name="k8SVersion")
    def k8_s_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "k8SVersion"))

    @k8_s_version.setter
    def k8_s_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePool, "k8_s_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "k8SVersion", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePool, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePool, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nodeCount")
    def node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nodeCount"))

    @node_count.setter
    def node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePool, "node_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="publicIps")
    def public_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "publicIps"))

    @public_ips.setter
    def public_ips(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePool, "public_ips").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicIps", value)

    @builtins.property
    @jsii.member(jsii_name="ramSize")
    def ram_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ramSize"))

    @ram_size.setter
    def ram_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePool, "ram_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ramSize", value)

    @builtins.property
    @jsii.member(jsii_name="storageSize")
    def storage_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storageSize"))

    @storage_size.setter
    def storage_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePool, "storage_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageSize", value)

    @builtins.property
    @jsii.member(jsii_name="storageType")
    def storage_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageType"))

    @storage_type.setter
    def storage_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePool, "storage_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.k8SNodePool.K8SNodePoolAutoScaling",
    jsii_struct_bases=[],
    name_mapping={"max_node_count": "maxNodeCount", "min_node_count": "minNodeCount"},
)
class K8SNodePoolAutoScaling:
    def __init__(
        self,
        *,
        max_node_count: jsii.Number,
        min_node_count: jsii.Number,
    ) -> None:
        '''
        :param max_node_count: The maximum number of worker nodes that the node pool can scale to. Should be greater than min_node_count. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#max_node_count K8SNodePool#max_node_count}
        :param min_node_count: The minimum number of worker nodes the node pool can scale down to. Should be less than max_node_count. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#min_node_count K8SNodePool#min_node_count}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(K8SNodePoolAutoScaling.__init__)
            check_type(argname="argument max_node_count", value=max_node_count, expected_type=type_hints["max_node_count"])
            check_type(argname="argument min_node_count", value=min_node_count, expected_type=type_hints["min_node_count"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_node_count": max_node_count,
            "min_node_count": min_node_count,
        }

    @builtins.property
    def max_node_count(self) -> jsii.Number:
        '''The maximum number of worker nodes that the node pool can scale to. Should be greater than min_node_count.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#max_node_count K8SNodePool#max_node_count}
        '''
        result = self._values.get("max_node_count")
        assert result is not None, "Required property 'max_node_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_node_count(self) -> jsii.Number:
        '''The minimum number of worker nodes the node pool can scale down to. Should be less than max_node_count.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#min_node_count K8SNodePool#min_node_count}
        '''
        result = self._values.get("min_node_count")
        assert result is not None, "Required property 'min_node_count' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "K8SNodePoolAutoScaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class K8SNodePoolAutoScalingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.k8SNodePool.K8SNodePoolAutoScalingOutputReference",
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
            type_hints = typing.get_type_hints(K8SNodePoolAutoScalingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maxNodeCountInput")
    def max_node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxNodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="minNodeCountInput")
    def min_node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minNodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="maxNodeCount")
    def max_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxNodeCount"))

    @max_node_count.setter
    def max_node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolAutoScalingOutputReference, "max_node_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxNodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="minNodeCount")
    def min_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minNodeCount"))

    @min_node_count.setter
    def min_node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolAutoScalingOutputReference, "min_node_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minNodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[K8SNodePoolAutoScaling]:
        return typing.cast(typing.Optional[K8SNodePoolAutoScaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[K8SNodePoolAutoScaling]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolAutoScalingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.k8SNodePool.K8SNodePoolConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "availability_zone": "availabilityZone",
        "cores_count": "coresCount",
        "cpu_family": "cpuFamily",
        "datacenter_id": "datacenterId",
        "k8_s_cluster_id": "k8SClusterId",
        "k8_s_version": "k8SVersion",
        "name": "name",
        "node_count": "nodeCount",
        "ram_size": "ramSize",
        "storage_size": "storageSize",
        "storage_type": "storageType",
        "allow_replace": "allowReplace",
        "annotations": "annotations",
        "auto_scaling": "autoScaling",
        "id": "id",
        "labels": "labels",
        "lans": "lans",
        "maintenance_window": "maintenanceWindow",
        "public_ips": "publicIps",
        "timeouts": "timeouts",
    },
)
class K8SNodePoolConfig(cdktf.TerraformMetaArguments):
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
        availability_zone: builtins.str,
        cores_count: jsii.Number,
        cpu_family: builtins.str,
        datacenter_id: builtins.str,
        k8_s_cluster_id: builtins.str,
        k8_s_version: builtins.str,
        name: builtins.str,
        node_count: jsii.Number,
        ram_size: jsii.Number,
        storage_size: jsii.Number,
        storage_type: builtins.str,
        allow_replace: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        auto_scaling: typing.Optional[typing.Union[K8SNodePoolAutoScaling, typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        lans: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["K8SNodePoolLans", typing.Dict[str, typing.Any]]]]] = None,
        maintenance_window: typing.Optional[typing.Union["K8SNodePoolMaintenanceWindow", typing.Dict[str, typing.Any]]] = None,
        public_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["K8SNodePoolTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param availability_zone: The compute availability zone in which the nodes should exist. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#availability_zone K8SNodePool#availability_zone}
        :param cores_count: CPU cores count. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#cores_count K8SNodePool#cores_count}
        :param cpu_family: CPU Family. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#cpu_family K8SNodePool#cpu_family}
        :param datacenter_id: The UUID of the VDC. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#datacenter_id K8SNodePool#datacenter_id}
        :param k8_s_cluster_id: The UUID of an existing kubernetes cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#k8s_cluster_id K8SNodePool#k8s_cluster_id}
        :param k8_s_version: The desired kubernetes version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#k8s_version K8SNodePool#k8s_version}
        :param name: The desired name for the node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#name K8SNodePool#name}
        :param node_count: The number of nodes in this node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#node_count K8SNodePool#node_count}
        :param ram_size: The amount of RAM in MB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#ram_size K8SNodePool#ram_size}
        :param storage_size: The total allocated storage capacity of a node in GB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#storage_size K8SNodePool#storage_size}
        :param storage_type: Storage type to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#storage_type K8SNodePool#storage_type}
        :param allow_replace: When set to true, allows the update of immutable fields by destroying and re-creating the node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#allow_replace K8SNodePool#allow_replace}
        :param annotations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#annotations K8SNodePool#annotations}.
        :param auto_scaling: auto_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#auto_scaling K8SNodePool#auto_scaling}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#id K8SNodePool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#labels K8SNodePool#labels}.
        :param lans: lans block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#lans K8SNodePool#lans}
        :param maintenance_window: maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#maintenance_window K8SNodePool#maintenance_window}
        :param public_ips: A list of fixed IPs. Cannot be set on private clusters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#public_ips K8SNodePool#public_ips}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#timeouts K8SNodePool#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(auto_scaling, dict):
            auto_scaling = K8SNodePoolAutoScaling(**auto_scaling)
        if isinstance(maintenance_window, dict):
            maintenance_window = K8SNodePoolMaintenanceWindow(**maintenance_window)
        if isinstance(timeouts, dict):
            timeouts = K8SNodePoolTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(K8SNodePoolConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument cores_count", value=cores_count, expected_type=type_hints["cores_count"])
            check_type(argname="argument cpu_family", value=cpu_family, expected_type=type_hints["cpu_family"])
            check_type(argname="argument datacenter_id", value=datacenter_id, expected_type=type_hints["datacenter_id"])
            check_type(argname="argument k8_s_cluster_id", value=k8_s_cluster_id, expected_type=type_hints["k8_s_cluster_id"])
            check_type(argname="argument k8_s_version", value=k8_s_version, expected_type=type_hints["k8_s_version"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument node_count", value=node_count, expected_type=type_hints["node_count"])
            check_type(argname="argument ram_size", value=ram_size, expected_type=type_hints["ram_size"])
            check_type(argname="argument storage_size", value=storage_size, expected_type=type_hints["storage_size"])
            check_type(argname="argument storage_type", value=storage_type, expected_type=type_hints["storage_type"])
            check_type(argname="argument allow_replace", value=allow_replace, expected_type=type_hints["allow_replace"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument auto_scaling", value=auto_scaling, expected_type=type_hints["auto_scaling"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument lans", value=lans, expected_type=type_hints["lans"])
            check_type(argname="argument maintenance_window", value=maintenance_window, expected_type=type_hints["maintenance_window"])
            check_type(argname="argument public_ips", value=public_ips, expected_type=type_hints["public_ips"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "availability_zone": availability_zone,
            "cores_count": cores_count,
            "cpu_family": cpu_family,
            "datacenter_id": datacenter_id,
            "k8_s_cluster_id": k8_s_cluster_id,
            "k8_s_version": k8_s_version,
            "name": name,
            "node_count": node_count,
            "ram_size": ram_size,
            "storage_size": storage_size,
            "storage_type": storage_type,
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
        if allow_replace is not None:
            self._values["allow_replace"] = allow_replace
        if annotations is not None:
            self._values["annotations"] = annotations
        if auto_scaling is not None:
            self._values["auto_scaling"] = auto_scaling
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if lans is not None:
            self._values["lans"] = lans
        if maintenance_window is not None:
            self._values["maintenance_window"] = maintenance_window
        if public_ips is not None:
            self._values["public_ips"] = public_ips
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
    def availability_zone(self) -> builtins.str:
        '''The compute availability zone in which the nodes should exist.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#availability_zone K8SNodePool#availability_zone}
        '''
        result = self._values.get("availability_zone")
        assert result is not None, "Required property 'availability_zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cores_count(self) -> jsii.Number:
        '''CPU cores count.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#cores_count K8SNodePool#cores_count}
        '''
        result = self._values.get("cores_count")
        assert result is not None, "Required property 'cores_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def cpu_family(self) -> builtins.str:
        '''CPU Family.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#cpu_family K8SNodePool#cpu_family}
        '''
        result = self._values.get("cpu_family")
        assert result is not None, "Required property 'cpu_family' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def datacenter_id(self) -> builtins.str:
        '''The UUID of the VDC.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#datacenter_id K8SNodePool#datacenter_id}
        '''
        result = self._values.get("datacenter_id")
        assert result is not None, "Required property 'datacenter_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def k8_s_cluster_id(self) -> builtins.str:
        '''The UUID of an existing kubernetes cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#k8s_cluster_id K8SNodePool#k8s_cluster_id}
        '''
        result = self._values.get("k8_s_cluster_id")
        assert result is not None, "Required property 'k8_s_cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def k8_s_version(self) -> builtins.str:
        '''The desired kubernetes version.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#k8s_version K8SNodePool#k8s_version}
        '''
        result = self._values.get("k8_s_version")
        assert result is not None, "Required property 'k8_s_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The desired name for the node pool.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#name K8SNodePool#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def node_count(self) -> jsii.Number:
        '''The number of nodes in this node pool.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#node_count K8SNodePool#node_count}
        '''
        result = self._values.get("node_count")
        assert result is not None, "Required property 'node_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def ram_size(self) -> jsii.Number:
        '''The amount of RAM in MB.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#ram_size K8SNodePool#ram_size}
        '''
        result = self._values.get("ram_size")
        assert result is not None, "Required property 'ram_size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def storage_size(self) -> jsii.Number:
        '''The total allocated storage capacity of a node in GB.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#storage_size K8SNodePool#storage_size}
        '''
        result = self._values.get("storage_size")
        assert result is not None, "Required property 'storage_size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def storage_type(self) -> builtins.str:
        '''Storage type to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#storage_type K8SNodePool#storage_type}
        '''
        result = self._values.get("storage_type")
        assert result is not None, "Required property 'storage_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_replace(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When set to true, allows the update of immutable fields by destroying and re-creating the node pool.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#allow_replace K8SNodePool#allow_replace}
        '''
        result = self._values.get("allow_replace")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#annotations K8SNodePool#annotations}.'''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def auto_scaling(self) -> typing.Optional[K8SNodePoolAutoScaling]:
        '''auto_scaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#auto_scaling K8SNodePool#auto_scaling}
        '''
        result = self._values.get("auto_scaling")
        return typing.cast(typing.Optional[K8SNodePoolAutoScaling], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#id K8SNodePool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#labels K8SNodePool#labels}.'''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def lans(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["K8SNodePoolLans"]]]:
        '''lans block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#lans K8SNodePool#lans}
        '''
        result = self._values.get("lans")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["K8SNodePoolLans"]]], result)

    @builtins.property
    def maintenance_window(self) -> typing.Optional["K8SNodePoolMaintenanceWindow"]:
        '''maintenance_window block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#maintenance_window K8SNodePool#maintenance_window}
        '''
        result = self._values.get("maintenance_window")
        return typing.cast(typing.Optional["K8SNodePoolMaintenanceWindow"], result)

    @builtins.property
    def public_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of fixed IPs. Cannot be set on private clusters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#public_ips K8SNodePool#public_ips}
        '''
        result = self._values.get("public_ips")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["K8SNodePoolTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#timeouts K8SNodePool#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["K8SNodePoolTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "K8SNodePoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.k8SNodePool.K8SNodePoolLans",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "dhcp": "dhcp", "routes": "routes"},
)
class K8SNodePoolLans:
    def __init__(
        self,
        *,
        id: jsii.Number,
        dhcp: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        routes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["K8SNodePoolLansRoutes", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param id: The LAN ID of an existing LAN at the related datacenter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#id K8SNodePool#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param dhcp: Indicates if the Kubernetes Node Pool LAN will reserve an IP using DHCP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#dhcp K8SNodePool#dhcp}
        :param routes: routes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#routes K8SNodePool#routes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(K8SNodePoolLans.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument dhcp", value=dhcp, expected_type=type_hints["dhcp"])
            check_type(argname="argument routes", value=routes, expected_type=type_hints["routes"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if dhcp is not None:
            self._values["dhcp"] = dhcp
        if routes is not None:
            self._values["routes"] = routes

    @builtins.property
    def id(self) -> jsii.Number:
        '''The LAN ID of an existing LAN at the related datacenter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#id K8SNodePool#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def dhcp(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates if the Kubernetes Node Pool LAN will reserve an IP using DHCP.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#dhcp K8SNodePool#dhcp}
        '''
        result = self._values.get("dhcp")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def routes(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["K8SNodePoolLansRoutes"]]]:
        '''routes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#routes K8SNodePool#routes}
        '''
        result = self._values.get("routes")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["K8SNodePoolLansRoutes"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "K8SNodePoolLans(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class K8SNodePoolLansList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.k8SNodePool.K8SNodePoolLansList",
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
            type_hints = typing.get_type_hints(K8SNodePoolLansList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "K8SNodePoolLansOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(K8SNodePoolLansList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("K8SNodePoolLansOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolLansList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(K8SNodePoolLansList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(K8SNodePoolLansList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[K8SNodePoolLans]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[K8SNodePoolLans]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[K8SNodePoolLans]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolLansList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class K8SNodePoolLansOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.k8SNodePool.K8SNodePoolLansOutputReference",
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
            type_hints = typing.get_type_hints(K8SNodePoolLansOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRoutes")
    def put_routes(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["K8SNodePoolLansRoutes", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(K8SNodePoolLansOutputReference.put_routes)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRoutes", [value]))

    @jsii.member(jsii_name="resetDhcp")
    def reset_dhcp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDhcp", []))

    @jsii.member(jsii_name="resetRoutes")
    def reset_routes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoutes", []))

    @builtins.property
    @jsii.member(jsii_name="routes")
    def routes(self) -> "K8SNodePoolLansRoutesList":
        return typing.cast("K8SNodePoolLansRoutesList", jsii.get(self, "routes"))

    @builtins.property
    @jsii.member(jsii_name="dhcpInput")
    def dhcp_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dhcpInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="routesInput")
    def routes_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["K8SNodePoolLansRoutes"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["K8SNodePoolLansRoutes"]]], jsii.get(self, "routesInput"))

    @builtins.property
    @jsii.member(jsii_name="dhcp")
    def dhcp(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dhcp"))

    @dhcp.setter
    def dhcp(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolLansOutputReference, "dhcp").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dhcp", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @id.setter
    def id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolLansOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[K8SNodePoolLans, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[K8SNodePoolLans, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[K8SNodePoolLans, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolLansOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.k8SNodePool.K8SNodePoolLansRoutes",
    jsii_struct_bases=[],
    name_mapping={"gateway_ip": "gatewayIp", "network": "network"},
)
class K8SNodePoolLansRoutes:
    def __init__(self, *, gateway_ip: builtins.str, network: builtins.str) -> None:
        '''
        :param gateway_ip: IPv4 or IPv6 Gateway IP for the route. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#gateway_ip K8SNodePool#gateway_ip}
        :param network: IPv4 or IPv6 CIDR to be routed via the interface. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#network K8SNodePool#network}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(K8SNodePoolLansRoutes.__init__)
            check_type(argname="argument gateway_ip", value=gateway_ip, expected_type=type_hints["gateway_ip"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
        self._values: typing.Dict[str, typing.Any] = {
            "gateway_ip": gateway_ip,
            "network": network,
        }

    @builtins.property
    def gateway_ip(self) -> builtins.str:
        '''IPv4 or IPv6 Gateway IP for the route.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#gateway_ip K8SNodePool#gateway_ip}
        '''
        result = self._values.get("gateway_ip")
        assert result is not None, "Required property 'gateway_ip' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network(self) -> builtins.str:
        '''IPv4 or IPv6 CIDR to be routed via the interface.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#network K8SNodePool#network}
        '''
        result = self._values.get("network")
        assert result is not None, "Required property 'network' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "K8SNodePoolLansRoutes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class K8SNodePoolLansRoutesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.k8SNodePool.K8SNodePoolLansRoutesList",
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
            type_hints = typing.get_type_hints(K8SNodePoolLansRoutesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "K8SNodePoolLansRoutesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(K8SNodePoolLansRoutesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("K8SNodePoolLansRoutesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolLansRoutesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(K8SNodePoolLansRoutesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(K8SNodePoolLansRoutesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[K8SNodePoolLansRoutes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[K8SNodePoolLansRoutes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[K8SNodePoolLansRoutes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolLansRoutesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class K8SNodePoolLansRoutesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.k8SNodePool.K8SNodePoolLansRoutesOutputReference",
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
            type_hints = typing.get_type_hints(K8SNodePoolLansRoutesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="gatewayIpInput")
    def gateway_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayIpInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayIp")
    def gateway_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayIp"))

    @gateway_ip.setter
    def gateway_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolLansRoutesOutputReference, "gateway_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayIp", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolLansRoutesOutputReference, "network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[K8SNodePoolLansRoutes, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[K8SNodePoolLansRoutes, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[K8SNodePoolLansRoutes, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolLansRoutesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.k8SNodePool.K8SNodePoolMaintenanceWindow",
    jsii_struct_bases=[],
    name_mapping={"day_of_the_week": "dayOfTheWeek", "time": "time"},
)
class K8SNodePoolMaintenanceWindow:
    def __init__(self, *, day_of_the_week: builtins.str, time: builtins.str) -> None:
        '''
        :param day_of_the_week: Day of the week when maintenance is allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#day_of_the_week K8SNodePool#day_of_the_week}
        :param time: A clock time in the day when maintenance is allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#time K8SNodePool#time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(K8SNodePoolMaintenanceWindow.__init__)
            check_type(argname="argument day_of_the_week", value=day_of_the_week, expected_type=type_hints["day_of_the_week"])
            check_type(argname="argument time", value=time, expected_type=type_hints["time"])
        self._values: typing.Dict[str, typing.Any] = {
            "day_of_the_week": day_of_the_week,
            "time": time,
        }

    @builtins.property
    def day_of_the_week(self) -> builtins.str:
        '''Day of the week when maintenance is allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#day_of_the_week K8SNodePool#day_of_the_week}
        '''
        result = self._values.get("day_of_the_week")
        assert result is not None, "Required property 'day_of_the_week' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time(self) -> builtins.str:
        '''A clock time in the day when maintenance is allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#time K8SNodePool#time}
        '''
        result = self._values.get("time")
        assert result is not None, "Required property 'time' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "K8SNodePoolMaintenanceWindow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class K8SNodePoolMaintenanceWindowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.k8SNodePool.K8SNodePoolMaintenanceWindowOutputReference",
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
            type_hints = typing.get_type_hints(K8SNodePoolMaintenanceWindowOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dayOfTheWeekInput")
    def day_of_the_week_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfTheWeekInput"))

    @builtins.property
    @jsii.member(jsii_name="timeInput")
    def time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeInput"))

    @builtins.property
    @jsii.member(jsii_name="dayOfTheWeek")
    def day_of_the_week(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayOfTheWeek"))

    @day_of_the_week.setter
    def day_of_the_week(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolMaintenanceWindowOutputReference, "day_of_the_week").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfTheWeek", value)

    @builtins.property
    @jsii.member(jsii_name="time")
    def time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "time"))

    @time.setter
    def time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolMaintenanceWindowOutputReference, "time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "time", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[K8SNodePoolMaintenanceWindow]:
        return typing.cast(typing.Optional[K8SNodePoolMaintenanceWindow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[K8SNodePoolMaintenanceWindow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolMaintenanceWindowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.k8SNodePool.K8SNodePoolTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "default": "default",
        "delete": "delete",
        "update": "update",
    },
)
class K8SNodePoolTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#create K8SNodePool#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#default K8SNodePool#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#delete K8SNodePool#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#update K8SNodePool#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(K8SNodePoolTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if default is not None:
            self._values["default"] = default
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#create K8SNodePool#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#default K8SNodePool#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#delete K8SNodePool#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_node_pool#update K8SNodePool#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "K8SNodePoolTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class K8SNodePoolTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.k8SNodePool.K8SNodePoolTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(K8SNodePoolTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

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
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

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
            type_hints = typing.get_type_hints(getattr(K8SNodePoolTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolTimeoutsOutputReference, "default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[K8SNodePoolTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[K8SNodePoolTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[K8SNodePoolTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SNodePoolTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "K8SNodePool",
    "K8SNodePoolAutoScaling",
    "K8SNodePoolAutoScalingOutputReference",
    "K8SNodePoolConfig",
    "K8SNodePoolLans",
    "K8SNodePoolLansList",
    "K8SNodePoolLansOutputReference",
    "K8SNodePoolLansRoutes",
    "K8SNodePoolLansRoutesList",
    "K8SNodePoolLansRoutesOutputReference",
    "K8SNodePoolMaintenanceWindow",
    "K8SNodePoolMaintenanceWindowOutputReference",
    "K8SNodePoolTimeouts",
    "K8SNodePoolTimeoutsOutputReference",
]

publication.publish()
