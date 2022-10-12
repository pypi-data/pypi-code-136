'''
# `data_databricks_node_type`

Refer to the Terraform Registory for docs: [`data_databricks_node_type`](https://www.terraform.io/docs/providers/databricks/d/node_type).
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


class DataDatabricksNodeType(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.dataDatabricksNodeType.DataDatabricksNodeType",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/d/node_type databricks_node_type}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        category: typing.Optional[builtins.str] = None,
        gb_per_core: typing.Optional[jsii.Number] = None,
        graviton: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        is_io_cache_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        local_disk: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        min_cores: typing.Optional[jsii.Number] = None,
        min_gpus: typing.Optional[jsii.Number] = None,
        min_memory_gb: typing.Optional[jsii.Number] = None,
        photon_driver_capable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        photon_worker_capable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        support_port_forwarding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        vcpu: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/d/node_type databricks_node_type} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param category: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#category DataDatabricksNodeType#category}.
        :param gb_per_core: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#gb_per_core DataDatabricksNodeType#gb_per_core}.
        :param graviton: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#graviton DataDatabricksNodeType#graviton}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#id DataDatabricksNodeType#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_io_cache_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#is_io_cache_enabled DataDatabricksNodeType#is_io_cache_enabled}.
        :param local_disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#local_disk DataDatabricksNodeType#local_disk}.
        :param min_cores: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#min_cores DataDatabricksNodeType#min_cores}.
        :param min_gpus: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#min_gpus DataDatabricksNodeType#min_gpus}.
        :param min_memory_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#min_memory_gb DataDatabricksNodeType#min_memory_gb}.
        :param photon_driver_capable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#photon_driver_capable DataDatabricksNodeType#photon_driver_capable}.
        :param photon_worker_capable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#photon_worker_capable DataDatabricksNodeType#photon_worker_capable}.
        :param support_port_forwarding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#support_port_forwarding DataDatabricksNodeType#support_port_forwarding}.
        :param vcpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#vcpu DataDatabricksNodeType#vcpu}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksNodeType.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataDatabricksNodeTypeConfig(
            category=category,
            gb_per_core=gb_per_core,
            graviton=graviton,
            id=id,
            is_io_cache_enabled=is_io_cache_enabled,
            local_disk=local_disk,
            min_cores=min_cores,
            min_gpus=min_gpus,
            min_memory_gb=min_memory_gb,
            photon_driver_capable=photon_driver_capable,
            photon_worker_capable=photon_worker_capable,
            support_port_forwarding=support_port_forwarding,
            vcpu=vcpu,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCategory")
    def reset_category(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCategory", []))

    @jsii.member(jsii_name="resetGbPerCore")
    def reset_gb_per_core(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGbPerCore", []))

    @jsii.member(jsii_name="resetGraviton")
    def reset_graviton(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGraviton", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsIoCacheEnabled")
    def reset_is_io_cache_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsIoCacheEnabled", []))

    @jsii.member(jsii_name="resetLocalDisk")
    def reset_local_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalDisk", []))

    @jsii.member(jsii_name="resetMinCores")
    def reset_min_cores(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCores", []))

    @jsii.member(jsii_name="resetMinGpus")
    def reset_min_gpus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinGpus", []))

    @jsii.member(jsii_name="resetMinMemoryGb")
    def reset_min_memory_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinMemoryGb", []))

    @jsii.member(jsii_name="resetPhotonDriverCapable")
    def reset_photon_driver_capable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhotonDriverCapable", []))

    @jsii.member(jsii_name="resetPhotonWorkerCapable")
    def reset_photon_worker_capable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhotonWorkerCapable", []))

    @jsii.member(jsii_name="resetSupportPortForwarding")
    def reset_support_port_forwarding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSupportPortForwarding", []))

    @jsii.member(jsii_name="resetVcpu")
    def reset_vcpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVcpu", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="categoryInput")
    def category_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "categoryInput"))

    @builtins.property
    @jsii.member(jsii_name="gbPerCoreInput")
    def gb_per_core_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gbPerCoreInput"))

    @builtins.property
    @jsii.member(jsii_name="gravitonInput")
    def graviton_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "gravitonInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isIoCacheEnabledInput")
    def is_io_cache_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isIoCacheEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="localDiskInput")
    def local_disk_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "localDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="minCoresInput")
    def min_cores_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minCoresInput"))

    @builtins.property
    @jsii.member(jsii_name="minGpusInput")
    def min_gpus_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minGpusInput"))

    @builtins.property
    @jsii.member(jsii_name="minMemoryGbInput")
    def min_memory_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minMemoryGbInput"))

    @builtins.property
    @jsii.member(jsii_name="photonDriverCapableInput")
    def photon_driver_capable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "photonDriverCapableInput"))

    @builtins.property
    @jsii.member(jsii_name="photonWorkerCapableInput")
    def photon_worker_capable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "photonWorkerCapableInput"))

    @builtins.property
    @jsii.member(jsii_name="supportPortForwardingInput")
    def support_port_forwarding_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "supportPortForwardingInput"))

    @builtins.property
    @jsii.member(jsii_name="vcpuInput")
    def vcpu_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "vcpuInput"))

    @builtins.property
    @jsii.member(jsii_name="category")
    def category(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "category"))

    @category.setter
    def category(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksNodeType, "category").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "category", value)

    @builtins.property
    @jsii.member(jsii_name="gbPerCore")
    def gb_per_core(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gbPerCore"))

    @gb_per_core.setter
    def gb_per_core(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksNodeType, "gb_per_core").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gbPerCore", value)

    @builtins.property
    @jsii.member(jsii_name="graviton")
    def graviton(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "graviton"))

    @graviton.setter
    def graviton(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksNodeType, "graviton").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "graviton", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksNodeType, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isIoCacheEnabled")
    def is_io_cache_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isIoCacheEnabled"))

    @is_io_cache_enabled.setter
    def is_io_cache_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksNodeType, "is_io_cache_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isIoCacheEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="localDisk")
    def local_disk(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "localDisk"))

    @local_disk.setter
    def local_disk(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksNodeType, "local_disk").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localDisk", value)

    @builtins.property
    @jsii.member(jsii_name="minCores")
    def min_cores(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minCores"))

    @min_cores.setter
    def min_cores(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksNodeType, "min_cores").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCores", value)

    @builtins.property
    @jsii.member(jsii_name="minGpus")
    def min_gpus(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minGpus"))

    @min_gpus.setter
    def min_gpus(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksNodeType, "min_gpus").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minGpus", value)

    @builtins.property
    @jsii.member(jsii_name="minMemoryGb")
    def min_memory_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minMemoryGb"))

    @min_memory_gb.setter
    def min_memory_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksNodeType, "min_memory_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minMemoryGb", value)

    @builtins.property
    @jsii.member(jsii_name="photonDriverCapable")
    def photon_driver_capable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "photonDriverCapable"))

    @photon_driver_capable.setter
    def photon_driver_capable(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksNodeType, "photon_driver_capable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "photonDriverCapable", value)

    @builtins.property
    @jsii.member(jsii_name="photonWorkerCapable")
    def photon_worker_capable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "photonWorkerCapable"))

    @photon_worker_capable.setter
    def photon_worker_capable(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksNodeType, "photon_worker_capable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "photonWorkerCapable", value)

    @builtins.property
    @jsii.member(jsii_name="supportPortForwarding")
    def support_port_forwarding(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "supportPortForwarding"))

    @support_port_forwarding.setter
    def support_port_forwarding(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksNodeType, "support_port_forwarding").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportPortForwarding", value)

    @builtins.property
    @jsii.member(jsii_name="vcpu")
    def vcpu(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "vcpu"))

    @vcpu.setter
    def vcpu(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataDatabricksNodeType, "vcpu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vcpu", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.dataDatabricksNodeType.DataDatabricksNodeTypeConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "category": "category",
        "gb_per_core": "gbPerCore",
        "graviton": "graviton",
        "id": "id",
        "is_io_cache_enabled": "isIoCacheEnabled",
        "local_disk": "localDisk",
        "min_cores": "minCores",
        "min_gpus": "minGpus",
        "min_memory_gb": "minMemoryGb",
        "photon_driver_capable": "photonDriverCapable",
        "photon_worker_capable": "photonWorkerCapable",
        "support_port_forwarding": "supportPortForwarding",
        "vcpu": "vcpu",
    },
)
class DataDatabricksNodeTypeConfig(cdktf.TerraformMetaArguments):
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
        category: typing.Optional[builtins.str] = None,
        gb_per_core: typing.Optional[jsii.Number] = None,
        graviton: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        is_io_cache_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        local_disk: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        min_cores: typing.Optional[jsii.Number] = None,
        min_gpus: typing.Optional[jsii.Number] = None,
        min_memory_gb: typing.Optional[jsii.Number] = None,
        photon_driver_capable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        photon_worker_capable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        support_port_forwarding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        vcpu: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param category: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#category DataDatabricksNodeType#category}.
        :param gb_per_core: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#gb_per_core DataDatabricksNodeType#gb_per_core}.
        :param graviton: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#graviton DataDatabricksNodeType#graviton}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#id DataDatabricksNodeType#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_io_cache_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#is_io_cache_enabled DataDatabricksNodeType#is_io_cache_enabled}.
        :param local_disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#local_disk DataDatabricksNodeType#local_disk}.
        :param min_cores: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#min_cores DataDatabricksNodeType#min_cores}.
        :param min_gpus: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#min_gpus DataDatabricksNodeType#min_gpus}.
        :param min_memory_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#min_memory_gb DataDatabricksNodeType#min_memory_gb}.
        :param photon_driver_capable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#photon_driver_capable DataDatabricksNodeType#photon_driver_capable}.
        :param photon_worker_capable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#photon_worker_capable DataDatabricksNodeType#photon_worker_capable}.
        :param support_port_forwarding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#support_port_forwarding DataDatabricksNodeType#support_port_forwarding}.
        :param vcpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#vcpu DataDatabricksNodeType#vcpu}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataDatabricksNodeTypeConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument category", value=category, expected_type=type_hints["category"])
            check_type(argname="argument gb_per_core", value=gb_per_core, expected_type=type_hints["gb_per_core"])
            check_type(argname="argument graviton", value=graviton, expected_type=type_hints["graviton"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_io_cache_enabled", value=is_io_cache_enabled, expected_type=type_hints["is_io_cache_enabled"])
            check_type(argname="argument local_disk", value=local_disk, expected_type=type_hints["local_disk"])
            check_type(argname="argument min_cores", value=min_cores, expected_type=type_hints["min_cores"])
            check_type(argname="argument min_gpus", value=min_gpus, expected_type=type_hints["min_gpus"])
            check_type(argname="argument min_memory_gb", value=min_memory_gb, expected_type=type_hints["min_memory_gb"])
            check_type(argname="argument photon_driver_capable", value=photon_driver_capable, expected_type=type_hints["photon_driver_capable"])
            check_type(argname="argument photon_worker_capable", value=photon_worker_capable, expected_type=type_hints["photon_worker_capable"])
            check_type(argname="argument support_port_forwarding", value=support_port_forwarding, expected_type=type_hints["support_port_forwarding"])
            check_type(argname="argument vcpu", value=vcpu, expected_type=type_hints["vcpu"])
        self._values: typing.Dict[str, typing.Any] = {}
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
        if category is not None:
            self._values["category"] = category
        if gb_per_core is not None:
            self._values["gb_per_core"] = gb_per_core
        if graviton is not None:
            self._values["graviton"] = graviton
        if id is not None:
            self._values["id"] = id
        if is_io_cache_enabled is not None:
            self._values["is_io_cache_enabled"] = is_io_cache_enabled
        if local_disk is not None:
            self._values["local_disk"] = local_disk
        if min_cores is not None:
            self._values["min_cores"] = min_cores
        if min_gpus is not None:
            self._values["min_gpus"] = min_gpus
        if min_memory_gb is not None:
            self._values["min_memory_gb"] = min_memory_gb
        if photon_driver_capable is not None:
            self._values["photon_driver_capable"] = photon_driver_capable
        if photon_worker_capable is not None:
            self._values["photon_worker_capable"] = photon_worker_capable
        if support_port_forwarding is not None:
            self._values["support_port_forwarding"] = support_port_forwarding
        if vcpu is not None:
            self._values["vcpu"] = vcpu

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
    def category(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#category DataDatabricksNodeType#category}.'''
        result = self._values.get("category")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gb_per_core(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#gb_per_core DataDatabricksNodeType#gb_per_core}.'''
        result = self._values.get("gb_per_core")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def graviton(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#graviton DataDatabricksNodeType#graviton}.'''
        result = self._values.get("graviton")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#id DataDatabricksNodeType#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_io_cache_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#is_io_cache_enabled DataDatabricksNodeType#is_io_cache_enabled}.'''
        result = self._values.get("is_io_cache_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def local_disk(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#local_disk DataDatabricksNodeType#local_disk}.'''
        result = self._values.get("local_disk")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def min_cores(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#min_cores DataDatabricksNodeType#min_cores}.'''
        result = self._values.get("min_cores")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_gpus(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#min_gpus DataDatabricksNodeType#min_gpus}.'''
        result = self._values.get("min_gpus")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_memory_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#min_memory_gb DataDatabricksNodeType#min_memory_gb}.'''
        result = self._values.get("min_memory_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def photon_driver_capable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#photon_driver_capable DataDatabricksNodeType#photon_driver_capable}.'''
        result = self._values.get("photon_driver_capable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def photon_worker_capable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#photon_worker_capable DataDatabricksNodeType#photon_worker_capable}.'''
        result = self._values.get("photon_worker_capable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def support_port_forwarding(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#support_port_forwarding DataDatabricksNodeType#support_port_forwarding}.'''
        result = self._values.get("support_port_forwarding")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def vcpu(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#vcpu DataDatabricksNodeType#vcpu}.'''
        result = self._values.get("vcpu")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksNodeTypeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataDatabricksNodeType",
    "DataDatabricksNodeTypeConfig",
]

publication.publish()
