'''
# `datadog_integration_opsgenie_service_object`

Refer to the Terraform Registory for docs: [`datadog_integration_opsgenie_service_object`](https://www.terraform.io/docs/providers/datadog/r/integration_opsgenie_service_object).
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


class IntegrationOpsgenieServiceObject(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.integrationOpsgenieServiceObject.IntegrationOpsgenieServiceObject",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/datadog/r/integration_opsgenie_service_object datadog_integration_opsgenie_service_object}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        opsgenie_api_key: builtins.str,
        region: builtins.str,
        custom_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/datadog/r/integration_opsgenie_service_object datadog_integration_opsgenie_service_object} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name for the Opsgenie service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_opsgenie_service_object#name IntegrationOpsgenieServiceObject#name}
        :param opsgenie_api_key: The Opsgenie API key for the Opsgenie service. Note: Since the Datadog API never returns Opsgenie API keys, it is impossible to detect `drifts <https://www.hashicorp.com/blog/detecting-and-managing-drift-with-terraform>`_. The best way to solve a drift is to manually mark the Service Object resource with `terraform taint <https://www.terraform.io/docs/commands/taint.html>`_ to have it destroyed and recreated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_opsgenie_service_object#opsgenie_api_key IntegrationOpsgenieServiceObject#opsgenie_api_key}
        :param region: The region for the Opsgenie service. Valid values are ``us``, ``eu``, ``custom``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_opsgenie_service_object#region IntegrationOpsgenieServiceObject#region}
        :param custom_url: The custom url for a custom region. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_opsgenie_service_object#custom_url IntegrationOpsgenieServiceObject#custom_url}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_opsgenie_service_object#id IntegrationOpsgenieServiceObject#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IntegrationOpsgenieServiceObject.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IntegrationOpsgenieServiceObjectConfig(
            name=name,
            opsgenie_api_key=opsgenie_api_key,
            region=region,
            custom_url=custom_url,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCustomUrl")
    def reset_custom_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomUrl", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="customUrlInput")
    def custom_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="opsgenieApiKeyInput")
    def opsgenie_api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "opsgenieApiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="customUrl")
    def custom_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customUrl"))

    @custom_url.setter
    def custom_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IntegrationOpsgenieServiceObject, "custom_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customUrl", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IntegrationOpsgenieServiceObject, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IntegrationOpsgenieServiceObject, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="opsgenieApiKey")
    def opsgenie_api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "opsgenieApiKey"))

    @opsgenie_api_key.setter
    def opsgenie_api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IntegrationOpsgenieServiceObject, "opsgenie_api_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "opsgenieApiKey", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IntegrationOpsgenieServiceObject, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.integrationOpsgenieServiceObject.IntegrationOpsgenieServiceObjectConfig",
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
        "opsgenie_api_key": "opsgenieApiKey",
        "region": "region",
        "custom_url": "customUrl",
        "id": "id",
    },
)
class IntegrationOpsgenieServiceObjectConfig(cdktf.TerraformMetaArguments):
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
        opsgenie_api_key: builtins.str,
        region: builtins.str,
        custom_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name for the Opsgenie service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_opsgenie_service_object#name IntegrationOpsgenieServiceObject#name}
        :param opsgenie_api_key: The Opsgenie API key for the Opsgenie service. Note: Since the Datadog API never returns Opsgenie API keys, it is impossible to detect `drifts <https://www.hashicorp.com/blog/detecting-and-managing-drift-with-terraform>`_. The best way to solve a drift is to manually mark the Service Object resource with `terraform taint <https://www.terraform.io/docs/commands/taint.html>`_ to have it destroyed and recreated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_opsgenie_service_object#opsgenie_api_key IntegrationOpsgenieServiceObject#opsgenie_api_key}
        :param region: The region for the Opsgenie service. Valid values are ``us``, ``eu``, ``custom``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_opsgenie_service_object#region IntegrationOpsgenieServiceObject#region}
        :param custom_url: The custom url for a custom region. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_opsgenie_service_object#custom_url IntegrationOpsgenieServiceObject#custom_url}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_opsgenie_service_object#id IntegrationOpsgenieServiceObject#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(IntegrationOpsgenieServiceObjectConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument opsgenie_api_key", value=opsgenie_api_key, expected_type=type_hints["opsgenie_api_key"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument custom_url", value=custom_url, expected_type=type_hints["custom_url"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "opsgenie_api_key": opsgenie_api_key,
            "region": region,
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
        if custom_url is not None:
            self._values["custom_url"] = custom_url
        if id is not None:
            self._values["id"] = id

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
        '''The name for the Opsgenie service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_opsgenie_service_object#name IntegrationOpsgenieServiceObject#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def opsgenie_api_key(self) -> builtins.str:
        '''The Opsgenie API key for the Opsgenie service.

        Note: Since the Datadog API never returns Opsgenie API keys, it is impossible to detect `drifts <https://www.hashicorp.com/blog/detecting-and-managing-drift-with-terraform>`_. The best way to solve a drift is to manually mark the Service Object resource with `terraform taint <https://www.terraform.io/docs/commands/taint.html>`_ to have it destroyed and recreated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_opsgenie_service_object#opsgenie_api_key IntegrationOpsgenieServiceObject#opsgenie_api_key}
        '''
        result = self._values.get("opsgenie_api_key")
        assert result is not None, "Required property 'opsgenie_api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''The region for the Opsgenie service. Valid values are ``us``, ``eu``, ``custom``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_opsgenie_service_object#region IntegrationOpsgenieServiceObject#region}
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_url(self) -> typing.Optional[builtins.str]:
        '''The custom url for a custom region.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_opsgenie_service_object#custom_url IntegrationOpsgenieServiceObject#custom_url}
        '''
        result = self._values.get("custom_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_opsgenie_service_object#id IntegrationOpsgenieServiceObject#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntegrationOpsgenieServiceObjectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IntegrationOpsgenieServiceObject",
    "IntegrationOpsgenieServiceObjectConfig",
]

publication.publish()
