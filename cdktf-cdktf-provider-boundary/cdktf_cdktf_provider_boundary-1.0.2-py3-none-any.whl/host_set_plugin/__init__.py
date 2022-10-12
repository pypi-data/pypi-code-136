'''
# `boundary_host_set_plugin`

Refer to the Terraform Registory for docs: [`boundary_host_set_plugin`](https://www.terraform.io/docs/providers/boundary/r/host_set_plugin).
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


class HostSetPlugin(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-boundary.hostSetPlugin.HostSetPlugin",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin boundary_host_set_plugin}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        host_catalog_id: builtins.str,
        attributes_json: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        preferred_endpoints: typing.Optional[typing.Sequence[builtins.str]] = None,
        sync_interval_seconds: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin boundary_host_set_plugin} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param host_catalog_id: The catalog for the host set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#host_catalog_id HostSetPlugin#host_catalog_id}
        :param attributes_json: The attributes for the host set. Either values encoded with the "jsonencode" function, pre-escaped JSON string, or a file:// or env:// path. Set to a string "null" or remove the block to clear all attributes in the host set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#attributes_json HostSetPlugin#attributes_json}
        :param description: The host set description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#description HostSetPlugin#description}
        :param name: The host set name. Defaults to the resource name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#name HostSetPlugin#name}
        :param preferred_endpoints: The ordered list of preferred endpoints. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#preferred_endpoints HostSetPlugin#preferred_endpoints}
        :param sync_interval_seconds: The value to set for the sync interval seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#sync_interval_seconds HostSetPlugin#sync_interval_seconds}
        :param type: The type of host set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#type HostSetPlugin#type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HostSetPlugin.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = HostSetPluginConfig(
            host_catalog_id=host_catalog_id,
            attributes_json=attributes_json,
            description=description,
            name=name,
            preferred_endpoints=preferred_endpoints,
            sync_interval_seconds=sync_interval_seconds,
            type=type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAttributesJson")
    def reset_attributes_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributesJson", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPreferredEndpoints")
    def reset_preferred_endpoints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredEndpoints", []))

    @jsii.member(jsii_name="resetSyncIntervalSeconds")
    def reset_sync_interval_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyncIntervalSeconds", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="attributesJsonInput")
    def attributes_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributesJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="hostCatalogIdInput")
    def host_catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostCatalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredEndpointsInput")
    def preferred_endpoints_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "preferredEndpointsInput"))

    @builtins.property
    @jsii.member(jsii_name="syncIntervalSecondsInput")
    def sync_interval_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "syncIntervalSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="attributesJson")
    def attributes_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributesJson"))

    @attributes_json.setter
    def attributes_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostSetPlugin, "attributes_json").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributesJson", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostSetPlugin, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="hostCatalogId")
    def host_catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostCatalogId"))

    @host_catalog_id.setter
    def host_catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostSetPlugin, "host_catalog_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostCatalogId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostSetPlugin, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="preferredEndpoints")
    def preferred_endpoints(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "preferredEndpoints"))

    @preferred_endpoints.setter
    def preferred_endpoints(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostSetPlugin, "preferred_endpoints").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredEndpoints", value)

    @builtins.property
    @jsii.member(jsii_name="syncIntervalSeconds")
    def sync_interval_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "syncIntervalSeconds"))

    @sync_interval_seconds.setter
    def sync_interval_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostSetPlugin, "sync_interval_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncIntervalSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostSetPlugin, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-boundary.hostSetPlugin.HostSetPluginConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "host_catalog_id": "hostCatalogId",
        "attributes_json": "attributesJson",
        "description": "description",
        "name": "name",
        "preferred_endpoints": "preferredEndpoints",
        "sync_interval_seconds": "syncIntervalSeconds",
        "type": "type",
    },
)
class HostSetPluginConfig(cdktf.TerraformMetaArguments):
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
        host_catalog_id: builtins.str,
        attributes_json: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        preferred_endpoints: typing.Optional[typing.Sequence[builtins.str]] = None,
        sync_interval_seconds: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param host_catalog_id: The catalog for the host set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#host_catalog_id HostSetPlugin#host_catalog_id}
        :param attributes_json: The attributes for the host set. Either values encoded with the "jsonencode" function, pre-escaped JSON string, or a file:// or env:// path. Set to a string "null" or remove the block to clear all attributes in the host set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#attributes_json HostSetPlugin#attributes_json}
        :param description: The host set description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#description HostSetPlugin#description}
        :param name: The host set name. Defaults to the resource name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#name HostSetPlugin#name}
        :param preferred_endpoints: The ordered list of preferred endpoints. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#preferred_endpoints HostSetPlugin#preferred_endpoints}
        :param sync_interval_seconds: The value to set for the sync interval seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#sync_interval_seconds HostSetPlugin#sync_interval_seconds}
        :param type: The type of host set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#type HostSetPlugin#type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(HostSetPluginConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument host_catalog_id", value=host_catalog_id, expected_type=type_hints["host_catalog_id"])
            check_type(argname="argument attributes_json", value=attributes_json, expected_type=type_hints["attributes_json"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument preferred_endpoints", value=preferred_endpoints, expected_type=type_hints["preferred_endpoints"])
            check_type(argname="argument sync_interval_seconds", value=sync_interval_seconds, expected_type=type_hints["sync_interval_seconds"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "host_catalog_id": host_catalog_id,
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
        if attributes_json is not None:
            self._values["attributes_json"] = attributes_json
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if preferred_endpoints is not None:
            self._values["preferred_endpoints"] = preferred_endpoints
        if sync_interval_seconds is not None:
            self._values["sync_interval_seconds"] = sync_interval_seconds
        if type is not None:
            self._values["type"] = type

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
    def host_catalog_id(self) -> builtins.str:
        '''The catalog for the host set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#host_catalog_id HostSetPlugin#host_catalog_id}
        '''
        result = self._values.get("host_catalog_id")
        assert result is not None, "Required property 'host_catalog_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attributes_json(self) -> typing.Optional[builtins.str]:
        '''The attributes for the host set.

        Either values encoded with the "jsonencode" function, pre-escaped JSON string, or a file:// or env:// path. Set to a string "null" or remove the block to clear all attributes in the host set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#attributes_json HostSetPlugin#attributes_json}
        '''
        result = self._values.get("attributes_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The host set description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#description HostSetPlugin#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The host set name. Defaults to the resource name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#name HostSetPlugin#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_endpoints(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ordered list of preferred endpoints.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#preferred_endpoints HostSetPlugin#preferred_endpoints}
        '''
        result = self._values.get("preferred_endpoints")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sync_interval_seconds(self) -> typing.Optional[jsii.Number]:
        '''The value to set for the sync interval seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#sync_interval_seconds HostSetPlugin#sync_interval_seconds}
        '''
        result = self._values.get("sync_interval_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of host set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_set_plugin#type HostSetPlugin#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostSetPluginConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "HostSetPlugin",
    "HostSetPluginConfig",
]

publication.publish()
