'''
# `vsphere_storage_drs_vm_override`

Refer to the Terraform Registory for docs: [`vsphere_storage_drs_vm_override`](https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override).
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


class StorageDrsVmOverride(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.storageDrsVmOverride.StorageDrsVmOverride",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override vsphere_storage_drs_vm_override}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        datastore_cluster_id: builtins.str,
        virtual_machine_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        sdrs_automation_level: typing.Optional[builtins.str] = None,
        sdrs_enabled: typing.Optional[builtins.str] = None,
        sdrs_intra_vm_affinity: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override vsphere_storage_drs_vm_override} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param datastore_cluster_id: The managed object ID of the datastore cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override#datastore_cluster_id StorageDrsVmOverride#datastore_cluster_id}
        :param virtual_machine_id: The managed object ID of the virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override#virtual_machine_id StorageDrsVmOverride#virtual_machine_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override#id StorageDrsVmOverride#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param sdrs_automation_level: Overrides any Storage DRS automation levels for this virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override#sdrs_automation_level StorageDrsVmOverride#sdrs_automation_level}
        :param sdrs_enabled: Overrides the default Storage DRS setting for this virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override#sdrs_enabled StorageDrsVmOverride#sdrs_enabled}
        :param sdrs_intra_vm_affinity: Overrides the intra-VM affinity setting for this virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override#sdrs_intra_vm_affinity StorageDrsVmOverride#sdrs_intra_vm_affinity}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageDrsVmOverride.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StorageDrsVmOverrideConfig(
            datastore_cluster_id=datastore_cluster_id,
            virtual_machine_id=virtual_machine_id,
            id=id,
            sdrs_automation_level=sdrs_automation_level,
            sdrs_enabled=sdrs_enabled,
            sdrs_intra_vm_affinity=sdrs_intra_vm_affinity,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSdrsAutomationLevel")
    def reset_sdrs_automation_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsAutomationLevel", []))

    @jsii.member(jsii_name="resetSdrsEnabled")
    def reset_sdrs_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsEnabled", []))

    @jsii.member(jsii_name="resetSdrsIntraVmAffinity")
    def reset_sdrs_intra_vm_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsIntraVmAffinity", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="datastoreClusterIdInput")
    def datastore_cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datastoreClusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsAutomationLevelInput")
    def sdrs_automation_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sdrsAutomationLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsEnabledInput")
    def sdrs_enabled_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sdrsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsIntraVmAffinityInput")
    def sdrs_intra_vm_affinity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sdrsIntraVmAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineIdInput")
    def virtual_machine_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualMachineIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datastoreClusterId")
    def datastore_cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datastoreClusterId"))

    @datastore_cluster_id.setter
    def datastore_cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageDrsVmOverride, "datastore_cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datastoreClusterId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageDrsVmOverride, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsAutomationLevel")
    def sdrs_automation_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sdrsAutomationLevel"))

    @sdrs_automation_level.setter
    def sdrs_automation_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageDrsVmOverride, "sdrs_automation_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsAutomationLevel", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsEnabled")
    def sdrs_enabled(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sdrsEnabled"))

    @sdrs_enabled.setter
    def sdrs_enabled(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageDrsVmOverride, "sdrs_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsIntraVmAffinity")
    def sdrs_intra_vm_affinity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sdrsIntraVmAffinity"))

    @sdrs_intra_vm_affinity.setter
    def sdrs_intra_vm_affinity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageDrsVmOverride, "sdrs_intra_vm_affinity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsIntraVmAffinity", value)

    @builtins.property
    @jsii.member(jsii_name="virtualMachineId")
    def virtual_machine_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualMachineId"))

    @virtual_machine_id.setter
    def virtual_machine_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageDrsVmOverride, "virtual_machine_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualMachineId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.storageDrsVmOverride.StorageDrsVmOverrideConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "datastore_cluster_id": "datastoreClusterId",
        "virtual_machine_id": "virtualMachineId",
        "id": "id",
        "sdrs_automation_level": "sdrsAutomationLevel",
        "sdrs_enabled": "sdrsEnabled",
        "sdrs_intra_vm_affinity": "sdrsIntraVmAffinity",
    },
)
class StorageDrsVmOverrideConfig(cdktf.TerraformMetaArguments):
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
        datastore_cluster_id: builtins.str,
        virtual_machine_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        sdrs_automation_level: typing.Optional[builtins.str] = None,
        sdrs_enabled: typing.Optional[builtins.str] = None,
        sdrs_intra_vm_affinity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param datastore_cluster_id: The managed object ID of the datastore cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override#datastore_cluster_id StorageDrsVmOverride#datastore_cluster_id}
        :param virtual_machine_id: The managed object ID of the virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override#virtual_machine_id StorageDrsVmOverride#virtual_machine_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override#id StorageDrsVmOverride#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param sdrs_automation_level: Overrides any Storage DRS automation levels for this virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override#sdrs_automation_level StorageDrsVmOverride#sdrs_automation_level}
        :param sdrs_enabled: Overrides the default Storage DRS setting for this virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override#sdrs_enabled StorageDrsVmOverride#sdrs_enabled}
        :param sdrs_intra_vm_affinity: Overrides the intra-VM affinity setting for this virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override#sdrs_intra_vm_affinity StorageDrsVmOverride#sdrs_intra_vm_affinity}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(StorageDrsVmOverrideConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument datastore_cluster_id", value=datastore_cluster_id, expected_type=type_hints["datastore_cluster_id"])
            check_type(argname="argument virtual_machine_id", value=virtual_machine_id, expected_type=type_hints["virtual_machine_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument sdrs_automation_level", value=sdrs_automation_level, expected_type=type_hints["sdrs_automation_level"])
            check_type(argname="argument sdrs_enabled", value=sdrs_enabled, expected_type=type_hints["sdrs_enabled"])
            check_type(argname="argument sdrs_intra_vm_affinity", value=sdrs_intra_vm_affinity, expected_type=type_hints["sdrs_intra_vm_affinity"])
        self._values: typing.Dict[str, typing.Any] = {
            "datastore_cluster_id": datastore_cluster_id,
            "virtual_machine_id": virtual_machine_id,
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
        if id is not None:
            self._values["id"] = id
        if sdrs_automation_level is not None:
            self._values["sdrs_automation_level"] = sdrs_automation_level
        if sdrs_enabled is not None:
            self._values["sdrs_enabled"] = sdrs_enabled
        if sdrs_intra_vm_affinity is not None:
            self._values["sdrs_intra_vm_affinity"] = sdrs_intra_vm_affinity

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
    def datastore_cluster_id(self) -> builtins.str:
        '''The managed object ID of the datastore cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override#datastore_cluster_id StorageDrsVmOverride#datastore_cluster_id}
        '''
        result = self._values.get("datastore_cluster_id")
        assert result is not None, "Required property 'datastore_cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_machine_id(self) -> builtins.str:
        '''The managed object ID of the virtual machine.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override#virtual_machine_id StorageDrsVmOverride#virtual_machine_id}
        '''
        result = self._values.get("virtual_machine_id")
        assert result is not None, "Required property 'virtual_machine_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override#id StorageDrsVmOverride#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sdrs_automation_level(self) -> typing.Optional[builtins.str]:
        '''Overrides any Storage DRS automation levels for this virtual machine.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override#sdrs_automation_level StorageDrsVmOverride#sdrs_automation_level}
        '''
        result = self._values.get("sdrs_automation_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sdrs_enabled(self) -> typing.Optional[builtins.str]:
        '''Overrides the default Storage DRS setting for this virtual machine.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override#sdrs_enabled StorageDrsVmOverride#sdrs_enabled}
        '''
        result = self._values.get("sdrs_enabled")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sdrs_intra_vm_affinity(self) -> typing.Optional[builtins.str]:
        '''Overrides the intra-VM affinity setting for this virtual machine.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override#sdrs_intra_vm_affinity StorageDrsVmOverride#sdrs_intra_vm_affinity}
        '''
        result = self._values.get("sdrs_intra_vm_affinity")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageDrsVmOverrideConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "StorageDrsVmOverride",
    "StorageDrsVmOverrideConfig",
]

publication.publish()
