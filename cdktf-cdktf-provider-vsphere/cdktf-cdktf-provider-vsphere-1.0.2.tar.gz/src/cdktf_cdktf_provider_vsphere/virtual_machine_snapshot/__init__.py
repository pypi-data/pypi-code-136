'''
# `vsphere_virtual_machine_snapshot`

Refer to the Terraform Registory for docs: [`vsphere_virtual_machine_snapshot`](https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot).
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


class VirtualMachineSnapshot(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.virtualMachineSnapshot.VirtualMachineSnapshot",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot vsphere_virtual_machine_snapshot}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        description: builtins.str,
        memory: typing.Union[builtins.bool, cdktf.IResolvable],
        quiesce: typing.Union[builtins.bool, cdktf.IResolvable],
        snapshot_name: builtins.str,
        virtual_machine_uuid: builtins.str,
        consolidate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        remove_children: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot vsphere_virtual_machine_snapshot} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#description VirtualMachineSnapshot#description}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#memory VirtualMachineSnapshot#memory}.
        :param quiesce: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#quiesce VirtualMachineSnapshot#quiesce}.
        :param snapshot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#snapshot_name VirtualMachineSnapshot#snapshot_name}.
        :param virtual_machine_uuid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#virtual_machine_uuid VirtualMachineSnapshot#virtual_machine_uuid}.
        :param consolidate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#consolidate VirtualMachineSnapshot#consolidate}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#id VirtualMachineSnapshot#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param remove_children: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#remove_children VirtualMachineSnapshot#remove_children}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineSnapshot.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VirtualMachineSnapshotConfig(
            description=description,
            memory=memory,
            quiesce=quiesce,
            snapshot_name=snapshot_name,
            virtual_machine_uuid=virtual_machine_uuid,
            consolidate=consolidate,
            id=id,
            remove_children=remove_children,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetConsolidate")
    def reset_consolidate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsolidate", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRemoveChildren")
    def reset_remove_children(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoveChildren", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="consolidateInput")
    def consolidate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "consolidateInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryInput")
    def memory_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "memoryInput"))

    @builtins.property
    @jsii.member(jsii_name="quiesceInput")
    def quiesce_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "quiesceInput"))

    @builtins.property
    @jsii.member(jsii_name="removeChildrenInput")
    def remove_children_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "removeChildrenInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotNameInput")
    def snapshot_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotNameInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineUuidInput")
    def virtual_machine_uuid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualMachineUuidInput"))

    @builtins.property
    @jsii.member(jsii_name="consolidate")
    def consolidate(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "consolidate"))

    @consolidate.setter
    def consolidate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineSnapshot, "consolidate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consolidate", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineSnapshot, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineSnapshot, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="memory")
    def memory(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "memory"))

    @memory.setter
    def memory(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineSnapshot, "memory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memory", value)

    @builtins.property
    @jsii.member(jsii_name="quiesce")
    def quiesce(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "quiesce"))

    @quiesce.setter
    def quiesce(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineSnapshot, "quiesce").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "quiesce", value)

    @builtins.property
    @jsii.member(jsii_name="removeChildren")
    def remove_children(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "removeChildren"))

    @remove_children.setter
    def remove_children(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineSnapshot, "remove_children").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "removeChildren", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotName")
    def snapshot_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotName"))

    @snapshot_name.setter
    def snapshot_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineSnapshot, "snapshot_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotName", value)

    @builtins.property
    @jsii.member(jsii_name="virtualMachineUuid")
    def virtual_machine_uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualMachineUuid"))

    @virtual_machine_uuid.setter
    def virtual_machine_uuid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineSnapshot, "virtual_machine_uuid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualMachineUuid", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.virtualMachineSnapshot.VirtualMachineSnapshotConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "description": "description",
        "memory": "memory",
        "quiesce": "quiesce",
        "snapshot_name": "snapshotName",
        "virtual_machine_uuid": "virtualMachineUuid",
        "consolidate": "consolidate",
        "id": "id",
        "remove_children": "removeChildren",
    },
)
class VirtualMachineSnapshotConfig(cdktf.TerraformMetaArguments):
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
        description: builtins.str,
        memory: typing.Union[builtins.bool, cdktf.IResolvable],
        quiesce: typing.Union[builtins.bool, cdktf.IResolvable],
        snapshot_name: builtins.str,
        virtual_machine_uuid: builtins.str,
        consolidate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        remove_children: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#description VirtualMachineSnapshot#description}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#memory VirtualMachineSnapshot#memory}.
        :param quiesce: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#quiesce VirtualMachineSnapshot#quiesce}.
        :param snapshot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#snapshot_name VirtualMachineSnapshot#snapshot_name}.
        :param virtual_machine_uuid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#virtual_machine_uuid VirtualMachineSnapshot#virtual_machine_uuid}.
        :param consolidate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#consolidate VirtualMachineSnapshot#consolidate}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#id VirtualMachineSnapshot#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param remove_children: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#remove_children VirtualMachineSnapshot#remove_children}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineSnapshotConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
            check_type(argname="argument quiesce", value=quiesce, expected_type=type_hints["quiesce"])
            check_type(argname="argument snapshot_name", value=snapshot_name, expected_type=type_hints["snapshot_name"])
            check_type(argname="argument virtual_machine_uuid", value=virtual_machine_uuid, expected_type=type_hints["virtual_machine_uuid"])
            check_type(argname="argument consolidate", value=consolidate, expected_type=type_hints["consolidate"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument remove_children", value=remove_children, expected_type=type_hints["remove_children"])
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "memory": memory,
            "quiesce": quiesce,
            "snapshot_name": snapshot_name,
            "virtual_machine_uuid": virtual_machine_uuid,
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
        if consolidate is not None:
            self._values["consolidate"] = consolidate
        if id is not None:
            self._values["id"] = id
        if remove_children is not None:
            self._values["remove_children"] = remove_children

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
    def description(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#description VirtualMachineSnapshot#description}.'''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def memory(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#memory VirtualMachineSnapshot#memory}.'''
        result = self._values.get("memory")
        assert result is not None, "Required property 'memory' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def quiesce(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#quiesce VirtualMachineSnapshot#quiesce}.'''
        result = self._values.get("quiesce")
        assert result is not None, "Required property 'quiesce' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def snapshot_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#snapshot_name VirtualMachineSnapshot#snapshot_name}.'''
        result = self._values.get("snapshot_name")
        assert result is not None, "Required property 'snapshot_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_machine_uuid(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#virtual_machine_uuid VirtualMachineSnapshot#virtual_machine_uuid}.'''
        result = self._values.get("virtual_machine_uuid")
        assert result is not None, "Required property 'virtual_machine_uuid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def consolidate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#consolidate VirtualMachineSnapshot#consolidate}.'''
        result = self._values.get("consolidate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#id VirtualMachineSnapshot#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remove_children(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot#remove_children VirtualMachineSnapshot#remove_children}.'''
        result = self._values.get("remove_children")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineSnapshotConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "VirtualMachineSnapshot",
    "VirtualMachineSnapshotConfig",
]

publication.publish()
