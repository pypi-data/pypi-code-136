'''
# `vsphere_datastore_cluster_vm_anti_affinity_rule`

Refer to the Terraform Registory for docs: [`vsphere_datastore_cluster_vm_anti_affinity_rule`](https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule).
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


class DatastoreClusterVmAntiAffinityRule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.datastoreClusterVmAntiAffinityRule.DatastoreClusterVmAntiAffinityRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule vsphere_datastore_cluster_vm_anti_affinity_rule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        datastore_cluster_id: builtins.str,
        name: builtins.str,
        virtual_machine_ids: typing.Sequence[builtins.str],
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        mandatory: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule vsphere_datastore_cluster_vm_anti_affinity_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param datastore_cluster_id: The managed object ID of the datastore cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule#datastore_cluster_id DatastoreClusterVmAntiAffinityRule#datastore_cluster_id}
        :param name: The unique name of the virtual machine group in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule#name DatastoreClusterVmAntiAffinityRule#name}
        :param virtual_machine_ids: The UUIDs of the virtual machines to run on different datastores from each other. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule#virtual_machine_ids DatastoreClusterVmAntiAffinityRule#virtual_machine_ids}
        :param enabled: Enable this rule in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule#enabled DatastoreClusterVmAntiAffinityRule#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule#id DatastoreClusterVmAntiAffinityRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mandatory: When true, prevents any virtual machine operations that may violate this rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule#mandatory DatastoreClusterVmAntiAffinityRule#mandatory}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatastoreClusterVmAntiAffinityRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DatastoreClusterVmAntiAffinityRuleConfig(
            datastore_cluster_id=datastore_cluster_id,
            name=name,
            virtual_machine_ids=virtual_machine_ids,
            enabled=enabled,
            id=id,
            mandatory=mandatory,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMandatory")
    def reset_mandatory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMandatory", []))

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
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="mandatoryInput")
    def mandatory_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "mandatoryInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineIdsInput")
    def virtual_machine_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "virtualMachineIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="datastoreClusterId")
    def datastore_cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datastoreClusterId"))

    @datastore_cluster_id.setter
    def datastore_cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreClusterVmAntiAffinityRule, "datastore_cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datastoreClusterId", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreClusterVmAntiAffinityRule, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreClusterVmAntiAffinityRule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mandatory")
    def mandatory(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "mandatory"))

    @mandatory.setter
    def mandatory(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreClusterVmAntiAffinityRule, "mandatory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mandatory", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreClusterVmAntiAffinityRule, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="virtualMachineIds")
    def virtual_machine_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "virtualMachineIds"))

    @virtual_machine_ids.setter
    def virtual_machine_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreClusterVmAntiAffinityRule, "virtual_machine_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualMachineIds", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.datastoreClusterVmAntiAffinityRule.DatastoreClusterVmAntiAffinityRuleConfig",
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
        "name": "name",
        "virtual_machine_ids": "virtualMachineIds",
        "enabled": "enabled",
        "id": "id",
        "mandatory": "mandatory",
    },
)
class DatastoreClusterVmAntiAffinityRuleConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        virtual_machine_ids: typing.Sequence[builtins.str],
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        mandatory: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param datastore_cluster_id: The managed object ID of the datastore cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule#datastore_cluster_id DatastoreClusterVmAntiAffinityRule#datastore_cluster_id}
        :param name: The unique name of the virtual machine group in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule#name DatastoreClusterVmAntiAffinityRule#name}
        :param virtual_machine_ids: The UUIDs of the virtual machines to run on different datastores from each other. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule#virtual_machine_ids DatastoreClusterVmAntiAffinityRule#virtual_machine_ids}
        :param enabled: Enable this rule in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule#enabled DatastoreClusterVmAntiAffinityRule#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule#id DatastoreClusterVmAntiAffinityRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mandatory: When true, prevents any virtual machine operations that may violate this rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule#mandatory DatastoreClusterVmAntiAffinityRule#mandatory}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DatastoreClusterVmAntiAffinityRuleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument datastore_cluster_id", value=datastore_cluster_id, expected_type=type_hints["datastore_cluster_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument virtual_machine_ids", value=virtual_machine_ids, expected_type=type_hints["virtual_machine_ids"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mandatory", value=mandatory, expected_type=type_hints["mandatory"])
        self._values: typing.Dict[str, typing.Any] = {
            "datastore_cluster_id": datastore_cluster_id,
            "name": name,
            "virtual_machine_ids": virtual_machine_ids,
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
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if mandatory is not None:
            self._values["mandatory"] = mandatory

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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule#datastore_cluster_id DatastoreClusterVmAntiAffinityRule#datastore_cluster_id}
        '''
        result = self._values.get("datastore_cluster_id")
        assert result is not None, "Required property 'datastore_cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The unique name of the virtual machine group in the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule#name DatastoreClusterVmAntiAffinityRule#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_machine_ids(self) -> typing.List[builtins.str]:
        '''The UUIDs of the virtual machines to run on different datastores from each other.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule#virtual_machine_ids DatastoreClusterVmAntiAffinityRule#virtual_machine_ids}
        '''
        result = self._values.get("virtual_machine_ids")
        assert result is not None, "Required property 'virtual_machine_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable this rule in the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule#enabled DatastoreClusterVmAntiAffinityRule#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule#id DatastoreClusterVmAntiAffinityRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mandatory(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When true, prevents any virtual machine operations that may violate this rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule#mandatory DatastoreClusterVmAntiAffinityRule#mandatory}
        '''
        result = self._values.get("mandatory")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastoreClusterVmAntiAffinityRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DatastoreClusterVmAntiAffinityRule",
    "DatastoreClusterVmAntiAffinityRuleConfig",
]

publication.publish()
