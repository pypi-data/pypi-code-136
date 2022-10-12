'''
# `vault_generic_endpoint`

Refer to the Terraform Registory for docs: [`vault_generic_endpoint`](https://www.terraform.io/docs/providers/vault/r/generic_endpoint).
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


class GenericEndpoint(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.genericEndpoint.GenericEndpoint",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint vault_generic_endpoint}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        data_json: builtins.str,
        path: builtins.str,
        disable_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_read: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ignore_absent_fields: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        namespace: typing.Optional[builtins.str] = None,
        write_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint vault_generic_endpoint} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_json: JSON-encoded data to write. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#data_json GenericEndpoint#data_json}
        :param path: Full path where to the endpoint that will be written. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#path GenericEndpoint#path}
        :param disable_delete: Don't attempt to delete the path from Vault if true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#disable_delete GenericEndpoint#disable_delete}
        :param disable_read: Don't attempt to read the path from Vault if true; drift won't be detected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#disable_read GenericEndpoint#disable_read}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#id GenericEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignore_absent_fields: When reading, disregard fields not present in data_json. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#ignore_absent_fields GenericEndpoint#ignore_absent_fields}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#namespace GenericEndpoint#namespace}
        :param write_fields: Top-level fields returned by write to persist in state. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#write_fields GenericEndpoint#write_fields}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GenericEndpoint.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GenericEndpointConfig(
            data_json=data_json,
            path=path,
            disable_delete=disable_delete,
            disable_read=disable_read,
            id=id,
            ignore_absent_fields=ignore_absent_fields,
            namespace=namespace,
            write_fields=write_fields,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDisableDelete")
    def reset_disable_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableDelete", []))

    @jsii.member(jsii_name="resetDisableRead")
    def reset_disable_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableRead", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIgnoreAbsentFields")
    def reset_ignore_absent_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreAbsentFields", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetWriteFields")
    def reset_write_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteFields", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="writeData")
    def write_data(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "writeData"))

    @builtins.property
    @jsii.member(jsii_name="writeDataJson")
    def write_data_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "writeDataJson"))

    @builtins.property
    @jsii.member(jsii_name="dataJsonInput")
    def data_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="disableDeleteInput")
    def disable_delete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableDeleteInput"))

    @builtins.property
    @jsii.member(jsii_name="disableReadInput")
    def disable_read_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableReadInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreAbsentFieldsInput")
    def ignore_absent_fields_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreAbsentFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="writeFieldsInput")
    def write_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "writeFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataJson")
    def data_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataJson"))

    @data_json.setter
    def data_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GenericEndpoint, "data_json").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataJson", value)

    @builtins.property
    @jsii.member(jsii_name="disableDelete")
    def disable_delete(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableDelete"))

    @disable_delete.setter
    def disable_delete(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GenericEndpoint, "disable_delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableDelete", value)

    @builtins.property
    @jsii.member(jsii_name="disableRead")
    def disable_read(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableRead"))

    @disable_read.setter
    def disable_read(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GenericEndpoint, "disable_read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableRead", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GenericEndpoint, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreAbsentFields")
    def ignore_absent_fields(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreAbsentFields"))

    @ignore_absent_fields.setter
    def ignore_absent_fields(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GenericEndpoint, "ignore_absent_fields").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreAbsentFields", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GenericEndpoint, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GenericEndpoint, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="writeFields")
    def write_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "writeFields"))

    @write_fields.setter
    def write_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GenericEndpoint, "write_fields").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeFields", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.genericEndpoint.GenericEndpointConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "data_json": "dataJson",
        "path": "path",
        "disable_delete": "disableDelete",
        "disable_read": "disableRead",
        "id": "id",
        "ignore_absent_fields": "ignoreAbsentFields",
        "namespace": "namespace",
        "write_fields": "writeFields",
    },
)
class GenericEndpointConfig(cdktf.TerraformMetaArguments):
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
        data_json: builtins.str,
        path: builtins.str,
        disable_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_read: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ignore_absent_fields: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        namespace: typing.Optional[builtins.str] = None,
        write_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_json: JSON-encoded data to write. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#data_json GenericEndpoint#data_json}
        :param path: Full path where to the endpoint that will be written. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#path GenericEndpoint#path}
        :param disable_delete: Don't attempt to delete the path from Vault if true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#disable_delete GenericEndpoint#disable_delete}
        :param disable_read: Don't attempt to read the path from Vault if true; drift won't be detected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#disable_read GenericEndpoint#disable_read}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#id GenericEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignore_absent_fields: When reading, disregard fields not present in data_json. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#ignore_absent_fields GenericEndpoint#ignore_absent_fields}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#namespace GenericEndpoint#namespace}
        :param write_fields: Top-level fields returned by write to persist in state. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#write_fields GenericEndpoint#write_fields}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(GenericEndpointConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument data_json", value=data_json, expected_type=type_hints["data_json"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument disable_delete", value=disable_delete, expected_type=type_hints["disable_delete"])
            check_type(argname="argument disable_read", value=disable_read, expected_type=type_hints["disable_read"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ignore_absent_fields", value=ignore_absent_fields, expected_type=type_hints["ignore_absent_fields"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument write_fields", value=write_fields, expected_type=type_hints["write_fields"])
        self._values: typing.Dict[str, typing.Any] = {
            "data_json": data_json,
            "path": path,
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
        if disable_delete is not None:
            self._values["disable_delete"] = disable_delete
        if disable_read is not None:
            self._values["disable_read"] = disable_read
        if id is not None:
            self._values["id"] = id
        if ignore_absent_fields is not None:
            self._values["ignore_absent_fields"] = ignore_absent_fields
        if namespace is not None:
            self._values["namespace"] = namespace
        if write_fields is not None:
            self._values["write_fields"] = write_fields

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
    def data_json(self) -> builtins.str:
        '''JSON-encoded data to write.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#data_json GenericEndpoint#data_json}
        '''
        result = self._values.get("data_json")
        assert result is not None, "Required property 'data_json' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Full path where to the endpoint that will be written.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#path GenericEndpoint#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disable_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Don't attempt to delete the path from Vault if true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#disable_delete GenericEndpoint#disable_delete}
        '''
        result = self._values.get("disable_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def disable_read(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Don't attempt to read the path from Vault if true; drift won't be detected.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#disable_read GenericEndpoint#disable_read}
        '''
        result = self._values.get("disable_read")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#id GenericEndpoint#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_absent_fields(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When reading, disregard fields not present in data_json.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#ignore_absent_fields GenericEndpoint#ignore_absent_fields}
        '''
        result = self._values.get("ignore_absent_fields")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#namespace GenericEndpoint#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def write_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Top-level fields returned by write to persist in state.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/generic_endpoint#write_fields GenericEndpoint#write_fields}
        '''
        result = self._values.get("write_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GenericEndpointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GenericEndpoint",
    "GenericEndpointConfig",
]

publication.publish()
