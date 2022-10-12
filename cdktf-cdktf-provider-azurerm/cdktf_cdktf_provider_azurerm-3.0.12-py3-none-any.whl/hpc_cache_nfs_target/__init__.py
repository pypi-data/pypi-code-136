'''
# `azurerm_hpc_cache_nfs_target`

Refer to the Terraform Registory for docs: [`azurerm_hpc_cache_nfs_target`](https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target).
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


class HpcCacheNfsTarget(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hpcCacheNfsTarget.HpcCacheNfsTarget",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target azurerm_hpc_cache_nfs_target}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cache_name: builtins.str,
        name: builtins.str,
        namespace_junction: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HpcCacheNfsTargetNamespaceJunction", typing.Dict[str, typing.Any]]]],
        resource_group_name: builtins.str,
        target_host_name: builtins.str,
        usage_model: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["HpcCacheNfsTargetTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target azurerm_hpc_cache_nfs_target} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cache_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#cache_name HpcCacheNfsTarget#cache_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#name HpcCacheNfsTarget#name}.
        :param namespace_junction: namespace_junction block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#namespace_junction HpcCacheNfsTarget#namespace_junction}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#resource_group_name HpcCacheNfsTarget#resource_group_name}.
        :param target_host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#target_host_name HpcCacheNfsTarget#target_host_name}.
        :param usage_model: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#usage_model HpcCacheNfsTarget#usage_model}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#id HpcCacheNfsTarget#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#timeouts HpcCacheNfsTarget#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HpcCacheNfsTarget.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = HpcCacheNfsTargetConfig(
            cache_name=cache_name,
            name=name,
            namespace_junction=namespace_junction,
            resource_group_name=resource_group_name,
            target_host_name=target_host_name,
            usage_model=usage_model,
            id=id,
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

    @jsii.member(jsii_name="putNamespaceJunction")
    def put_namespace_junction(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HpcCacheNfsTargetNamespaceJunction", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HpcCacheNfsTarget.put_namespace_junction)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNamespaceJunction", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#create HpcCacheNfsTarget#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#delete HpcCacheNfsTarget#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#read HpcCacheNfsTarget#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#update HpcCacheNfsTarget#update}.
        '''
        value = HpcCacheNfsTargetTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="namespaceJunction")
    def namespace_junction(self) -> "HpcCacheNfsTargetNamespaceJunctionList":
        return typing.cast("HpcCacheNfsTargetNamespaceJunctionList", jsii.get(self, "namespaceJunction"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "HpcCacheNfsTargetTimeoutsOutputReference":
        return typing.cast("HpcCacheNfsTargetTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="cacheNameInput")
    def cache_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceJunctionInput")
    def namespace_junction_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HpcCacheNfsTargetNamespaceJunction"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HpcCacheNfsTargetNamespaceJunction"]]], jsii.get(self, "namespaceJunctionInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetHostNameInput")
    def target_host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetHostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["HpcCacheNfsTargetTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["HpcCacheNfsTargetTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="usageModelInput")
    def usage_model_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usageModelInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheName")
    def cache_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheName"))

    @cache_name.setter
    def cache_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTarget, "cache_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTarget, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTarget, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTarget, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="targetHostName")
    def target_host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetHostName"))

    @target_host_name.setter
    def target_host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTarget, "target_host_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetHostName", value)

    @builtins.property
    @jsii.member(jsii_name="usageModel")
    def usage_model(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usageModel"))

    @usage_model.setter
    def usage_model(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTarget, "usage_model").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usageModel", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hpcCacheNfsTarget.HpcCacheNfsTargetConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cache_name": "cacheName",
        "name": "name",
        "namespace_junction": "namespaceJunction",
        "resource_group_name": "resourceGroupName",
        "target_host_name": "targetHostName",
        "usage_model": "usageModel",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class HpcCacheNfsTargetConfig(cdktf.TerraformMetaArguments):
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
        cache_name: builtins.str,
        name: builtins.str,
        namespace_junction: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HpcCacheNfsTargetNamespaceJunction", typing.Dict[str, typing.Any]]]],
        resource_group_name: builtins.str,
        target_host_name: builtins.str,
        usage_model: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["HpcCacheNfsTargetTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cache_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#cache_name HpcCacheNfsTarget#cache_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#name HpcCacheNfsTarget#name}.
        :param namespace_junction: namespace_junction block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#namespace_junction HpcCacheNfsTarget#namespace_junction}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#resource_group_name HpcCacheNfsTarget#resource_group_name}.
        :param target_host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#target_host_name HpcCacheNfsTarget#target_host_name}.
        :param usage_model: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#usage_model HpcCacheNfsTarget#usage_model}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#id HpcCacheNfsTarget#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#timeouts HpcCacheNfsTarget#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = HpcCacheNfsTargetTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(HpcCacheNfsTargetConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cache_name", value=cache_name, expected_type=type_hints["cache_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace_junction", value=namespace_junction, expected_type=type_hints["namespace_junction"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument target_host_name", value=target_host_name, expected_type=type_hints["target_host_name"])
            check_type(argname="argument usage_model", value=usage_model, expected_type=type_hints["usage_model"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "cache_name": cache_name,
            "name": name,
            "namespace_junction": namespace_junction,
            "resource_group_name": resource_group_name,
            "target_host_name": target_host_name,
            "usage_model": usage_model,
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
    def cache_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#cache_name HpcCacheNfsTarget#cache_name}.'''
        result = self._values.get("cache_name")
        assert result is not None, "Required property 'cache_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#name HpcCacheNfsTarget#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace_junction(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["HpcCacheNfsTargetNamespaceJunction"]]:
        '''namespace_junction block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#namespace_junction HpcCacheNfsTarget#namespace_junction}
        '''
        result = self._values.get("namespace_junction")
        assert result is not None, "Required property 'namespace_junction' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["HpcCacheNfsTargetNamespaceJunction"]], result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#resource_group_name HpcCacheNfsTarget#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_host_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#target_host_name HpcCacheNfsTarget#target_host_name}.'''
        result = self._values.get("target_host_name")
        assert result is not None, "Required property 'target_host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def usage_model(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#usage_model HpcCacheNfsTarget#usage_model}.'''
        result = self._values.get("usage_model")
        assert result is not None, "Required property 'usage_model' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#id HpcCacheNfsTarget#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["HpcCacheNfsTargetTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#timeouts HpcCacheNfsTarget#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["HpcCacheNfsTargetTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HpcCacheNfsTargetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hpcCacheNfsTarget.HpcCacheNfsTargetNamespaceJunction",
    jsii_struct_bases=[],
    name_mapping={
        "namespace_path": "namespacePath",
        "nfs_export": "nfsExport",
        "access_policy_name": "accessPolicyName",
        "target_path": "targetPath",
    },
)
class HpcCacheNfsTargetNamespaceJunction:
    def __init__(
        self,
        *,
        namespace_path: builtins.str,
        nfs_export: builtins.str,
        access_policy_name: typing.Optional[builtins.str] = None,
        target_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param namespace_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#namespace_path HpcCacheNfsTarget#namespace_path}.
        :param nfs_export: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#nfs_export HpcCacheNfsTarget#nfs_export}.
        :param access_policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#access_policy_name HpcCacheNfsTarget#access_policy_name}.
        :param target_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#target_path HpcCacheNfsTarget#target_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HpcCacheNfsTargetNamespaceJunction.__init__)
            check_type(argname="argument namespace_path", value=namespace_path, expected_type=type_hints["namespace_path"])
            check_type(argname="argument nfs_export", value=nfs_export, expected_type=type_hints["nfs_export"])
            check_type(argname="argument access_policy_name", value=access_policy_name, expected_type=type_hints["access_policy_name"])
            check_type(argname="argument target_path", value=target_path, expected_type=type_hints["target_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "namespace_path": namespace_path,
            "nfs_export": nfs_export,
        }
        if access_policy_name is not None:
            self._values["access_policy_name"] = access_policy_name
        if target_path is not None:
            self._values["target_path"] = target_path

    @builtins.property
    def namespace_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#namespace_path HpcCacheNfsTarget#namespace_path}.'''
        result = self._values.get("namespace_path")
        assert result is not None, "Required property 'namespace_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def nfs_export(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#nfs_export HpcCacheNfsTarget#nfs_export}.'''
        result = self._values.get("nfs_export")
        assert result is not None, "Required property 'nfs_export' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_policy_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#access_policy_name HpcCacheNfsTarget#access_policy_name}.'''
        result = self._values.get("access_policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#target_path HpcCacheNfsTarget#target_path}.'''
        result = self._values.get("target_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HpcCacheNfsTargetNamespaceJunction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HpcCacheNfsTargetNamespaceJunctionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hpcCacheNfsTarget.HpcCacheNfsTargetNamespaceJunctionList",
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
            type_hints = typing.get_type_hints(HpcCacheNfsTargetNamespaceJunctionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HpcCacheNfsTargetNamespaceJunctionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HpcCacheNfsTargetNamespaceJunctionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HpcCacheNfsTargetNamespaceJunctionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTargetNamespaceJunctionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTargetNamespaceJunctionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTargetNamespaceJunctionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HpcCacheNfsTargetNamespaceJunction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HpcCacheNfsTargetNamespaceJunction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HpcCacheNfsTargetNamespaceJunction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTargetNamespaceJunctionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HpcCacheNfsTargetNamespaceJunctionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hpcCacheNfsTarget.HpcCacheNfsTargetNamespaceJunctionOutputReference",
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
            type_hints = typing.get_type_hints(HpcCacheNfsTargetNamespaceJunctionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccessPolicyName")
    def reset_access_policy_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessPolicyName", []))

    @jsii.member(jsii_name="resetTargetPath")
    def reset_target_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetPath", []))

    @builtins.property
    @jsii.member(jsii_name="accessPolicyNameInput")
    def access_policy_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessPolicyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespacePathInput")
    def namespace_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespacePathInput"))

    @builtins.property
    @jsii.member(jsii_name="nfsExportInput")
    def nfs_export_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nfsExportInput"))

    @builtins.property
    @jsii.member(jsii_name="targetPathInput")
    def target_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetPathInput"))

    @builtins.property
    @jsii.member(jsii_name="accessPolicyName")
    def access_policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessPolicyName"))

    @access_policy_name.setter
    def access_policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTargetNamespaceJunctionOutputReference, "access_policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessPolicyName", value)

    @builtins.property
    @jsii.member(jsii_name="namespacePath")
    def namespace_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespacePath"))

    @namespace_path.setter
    def namespace_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTargetNamespaceJunctionOutputReference, "namespace_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespacePath", value)

    @builtins.property
    @jsii.member(jsii_name="nfsExport")
    def nfs_export(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nfsExport"))

    @nfs_export.setter
    def nfs_export(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTargetNamespaceJunctionOutputReference, "nfs_export").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nfsExport", value)

    @builtins.property
    @jsii.member(jsii_name="targetPath")
    def target_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetPath"))

    @target_path.setter
    def target_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTargetNamespaceJunctionOutputReference, "target_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HpcCacheNfsTargetNamespaceJunction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HpcCacheNfsTargetNamespaceJunction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HpcCacheNfsTargetNamespaceJunction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTargetNamespaceJunctionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hpcCacheNfsTarget.HpcCacheNfsTargetTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class HpcCacheNfsTargetTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#create HpcCacheNfsTarget#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#delete HpcCacheNfsTarget#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#read HpcCacheNfsTarget#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#update HpcCacheNfsTarget#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HpcCacheNfsTargetTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#create HpcCacheNfsTarget#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#delete HpcCacheNfsTarget#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#read HpcCacheNfsTarget#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache_nfs_target#update HpcCacheNfsTarget#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HpcCacheNfsTargetTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HpcCacheNfsTargetTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hpcCacheNfsTarget.HpcCacheNfsTargetTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(HpcCacheNfsTargetTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTargetTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTargetTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTargetTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTargetTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HpcCacheNfsTargetTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HpcCacheNfsTargetTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HpcCacheNfsTargetTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheNfsTargetTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "HpcCacheNfsTarget",
    "HpcCacheNfsTargetConfig",
    "HpcCacheNfsTargetNamespaceJunction",
    "HpcCacheNfsTargetNamespaceJunctionList",
    "HpcCacheNfsTargetNamespaceJunctionOutputReference",
    "HpcCacheNfsTargetTimeouts",
    "HpcCacheNfsTargetTimeoutsOutputReference",
]

publication.publish()
