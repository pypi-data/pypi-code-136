'''
# `azurerm_frontdoor_custom_https_configuration`

Refer to the Terraform Registory for docs: [`azurerm_frontdoor_custom_https_configuration`](https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration).
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


class FrontdoorCustomHttpsConfiguration(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoorCustomHttpsConfiguration.FrontdoorCustomHttpsConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration azurerm_frontdoor_custom_https_configuration}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        custom_https_provisioning_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        frontend_endpoint_id: builtins.str,
        custom_https_configuration: typing.Optional[typing.Union["FrontdoorCustomHttpsConfigurationCustomHttpsConfiguration", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["FrontdoorCustomHttpsConfigurationTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration azurerm_frontdoor_custom_https_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param custom_https_provisioning_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#custom_https_provisioning_enabled FrontdoorCustomHttpsConfiguration#custom_https_provisioning_enabled}.
        :param frontend_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#frontend_endpoint_id FrontdoorCustomHttpsConfiguration#frontend_endpoint_id}.
        :param custom_https_configuration: custom_https_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#custom_https_configuration FrontdoorCustomHttpsConfiguration#custom_https_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#id FrontdoorCustomHttpsConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#timeouts FrontdoorCustomHttpsConfiguration#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorCustomHttpsConfiguration.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = FrontdoorCustomHttpsConfigurationConfig(
            custom_https_provisioning_enabled=custom_https_provisioning_enabled,
            frontend_endpoint_id=frontend_endpoint_id,
            custom_https_configuration=custom_https_configuration,
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

    @jsii.member(jsii_name="putCustomHttpsConfiguration")
    def put_custom_https_configuration(
        self,
        *,
        azure_key_vault_certificate_secret_name: typing.Optional[builtins.str] = None,
        azure_key_vault_certificate_secret_version: typing.Optional[builtins.str] = None,
        azure_key_vault_certificate_vault_id: typing.Optional[builtins.str] = None,
        certificate_source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param azure_key_vault_certificate_secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#azure_key_vault_certificate_secret_name FrontdoorCustomHttpsConfiguration#azure_key_vault_certificate_secret_name}.
        :param azure_key_vault_certificate_secret_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#azure_key_vault_certificate_secret_version FrontdoorCustomHttpsConfiguration#azure_key_vault_certificate_secret_version}.
        :param azure_key_vault_certificate_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#azure_key_vault_certificate_vault_id FrontdoorCustomHttpsConfiguration#azure_key_vault_certificate_vault_id}.
        :param certificate_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#certificate_source FrontdoorCustomHttpsConfiguration#certificate_source}.
        '''
        value = FrontdoorCustomHttpsConfigurationCustomHttpsConfiguration(
            azure_key_vault_certificate_secret_name=azure_key_vault_certificate_secret_name,
            azure_key_vault_certificate_secret_version=azure_key_vault_certificate_secret_version,
            azure_key_vault_certificate_vault_id=azure_key_vault_certificate_vault_id,
            certificate_source=certificate_source,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomHttpsConfiguration", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#create FrontdoorCustomHttpsConfiguration#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#delete FrontdoorCustomHttpsConfiguration#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#read FrontdoorCustomHttpsConfiguration#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#update FrontdoorCustomHttpsConfiguration#update}.
        '''
        value = FrontdoorCustomHttpsConfigurationTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCustomHttpsConfiguration")
    def reset_custom_https_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomHttpsConfiguration", []))

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
    @jsii.member(jsii_name="customHttpsConfiguration")
    def custom_https_configuration(
        self,
    ) -> "FrontdoorCustomHttpsConfigurationCustomHttpsConfigurationOutputReference":
        return typing.cast("FrontdoorCustomHttpsConfigurationCustomHttpsConfigurationOutputReference", jsii.get(self, "customHttpsConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "FrontdoorCustomHttpsConfigurationTimeoutsOutputReference":
        return typing.cast("FrontdoorCustomHttpsConfigurationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="customHttpsConfigurationInput")
    def custom_https_configuration_input(
        self,
    ) -> typing.Optional["FrontdoorCustomHttpsConfigurationCustomHttpsConfiguration"]:
        return typing.cast(typing.Optional["FrontdoorCustomHttpsConfigurationCustomHttpsConfiguration"], jsii.get(self, "customHttpsConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="customHttpsProvisioningEnabledInput")
    def custom_https_provisioning_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "customHttpsProvisioningEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendEndpointIdInput")
    def frontend_endpoint_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frontendEndpointIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["FrontdoorCustomHttpsConfigurationTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["FrontdoorCustomHttpsConfigurationTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="customHttpsProvisioningEnabled")
    def custom_https_provisioning_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "customHttpsProvisioningEnabled"))

    @custom_https_provisioning_enabled.setter
    def custom_https_provisioning_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorCustomHttpsConfiguration, "custom_https_provisioning_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customHttpsProvisioningEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="frontendEndpointId")
    def frontend_endpoint_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frontendEndpointId"))

    @frontend_endpoint_id.setter
    def frontend_endpoint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorCustomHttpsConfiguration, "frontend_endpoint_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frontendEndpointId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorCustomHttpsConfiguration, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.frontdoorCustomHttpsConfiguration.FrontdoorCustomHttpsConfigurationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "custom_https_provisioning_enabled": "customHttpsProvisioningEnabled",
        "frontend_endpoint_id": "frontendEndpointId",
        "custom_https_configuration": "customHttpsConfiguration",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class FrontdoorCustomHttpsConfigurationConfig(cdktf.TerraformMetaArguments):
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
        custom_https_provisioning_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        frontend_endpoint_id: builtins.str,
        custom_https_configuration: typing.Optional[typing.Union["FrontdoorCustomHttpsConfigurationCustomHttpsConfiguration", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["FrontdoorCustomHttpsConfigurationTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param custom_https_provisioning_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#custom_https_provisioning_enabled FrontdoorCustomHttpsConfiguration#custom_https_provisioning_enabled}.
        :param frontend_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#frontend_endpoint_id FrontdoorCustomHttpsConfiguration#frontend_endpoint_id}.
        :param custom_https_configuration: custom_https_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#custom_https_configuration FrontdoorCustomHttpsConfiguration#custom_https_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#id FrontdoorCustomHttpsConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#timeouts FrontdoorCustomHttpsConfiguration#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(custom_https_configuration, dict):
            custom_https_configuration = FrontdoorCustomHttpsConfigurationCustomHttpsConfiguration(**custom_https_configuration)
        if isinstance(timeouts, dict):
            timeouts = FrontdoorCustomHttpsConfigurationTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorCustomHttpsConfigurationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument custom_https_provisioning_enabled", value=custom_https_provisioning_enabled, expected_type=type_hints["custom_https_provisioning_enabled"])
            check_type(argname="argument frontend_endpoint_id", value=frontend_endpoint_id, expected_type=type_hints["frontend_endpoint_id"])
            check_type(argname="argument custom_https_configuration", value=custom_https_configuration, expected_type=type_hints["custom_https_configuration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "custom_https_provisioning_enabled": custom_https_provisioning_enabled,
            "frontend_endpoint_id": frontend_endpoint_id,
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
        if custom_https_configuration is not None:
            self._values["custom_https_configuration"] = custom_https_configuration
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
    def custom_https_provisioning_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#custom_https_provisioning_enabled FrontdoorCustomHttpsConfiguration#custom_https_provisioning_enabled}.'''
        result = self._values.get("custom_https_provisioning_enabled")
        assert result is not None, "Required property 'custom_https_provisioning_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def frontend_endpoint_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#frontend_endpoint_id FrontdoorCustomHttpsConfiguration#frontend_endpoint_id}.'''
        result = self._values.get("frontend_endpoint_id")
        assert result is not None, "Required property 'frontend_endpoint_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_https_configuration(
        self,
    ) -> typing.Optional["FrontdoorCustomHttpsConfigurationCustomHttpsConfiguration"]:
        '''custom_https_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#custom_https_configuration FrontdoorCustomHttpsConfiguration#custom_https_configuration}
        '''
        result = self._values.get("custom_https_configuration")
        return typing.cast(typing.Optional["FrontdoorCustomHttpsConfigurationCustomHttpsConfiguration"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#id FrontdoorCustomHttpsConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["FrontdoorCustomHttpsConfigurationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#timeouts FrontdoorCustomHttpsConfiguration#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["FrontdoorCustomHttpsConfigurationTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FrontdoorCustomHttpsConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.frontdoorCustomHttpsConfiguration.FrontdoorCustomHttpsConfigurationCustomHttpsConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "azure_key_vault_certificate_secret_name": "azureKeyVaultCertificateSecretName",
        "azure_key_vault_certificate_secret_version": "azureKeyVaultCertificateSecretVersion",
        "azure_key_vault_certificate_vault_id": "azureKeyVaultCertificateVaultId",
        "certificate_source": "certificateSource",
    },
)
class FrontdoorCustomHttpsConfigurationCustomHttpsConfiguration:
    def __init__(
        self,
        *,
        azure_key_vault_certificate_secret_name: typing.Optional[builtins.str] = None,
        azure_key_vault_certificate_secret_version: typing.Optional[builtins.str] = None,
        azure_key_vault_certificate_vault_id: typing.Optional[builtins.str] = None,
        certificate_source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param azure_key_vault_certificate_secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#azure_key_vault_certificate_secret_name FrontdoorCustomHttpsConfiguration#azure_key_vault_certificate_secret_name}.
        :param azure_key_vault_certificate_secret_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#azure_key_vault_certificate_secret_version FrontdoorCustomHttpsConfiguration#azure_key_vault_certificate_secret_version}.
        :param azure_key_vault_certificate_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#azure_key_vault_certificate_vault_id FrontdoorCustomHttpsConfiguration#azure_key_vault_certificate_vault_id}.
        :param certificate_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#certificate_source FrontdoorCustomHttpsConfiguration#certificate_source}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorCustomHttpsConfigurationCustomHttpsConfiguration.__init__)
            check_type(argname="argument azure_key_vault_certificate_secret_name", value=azure_key_vault_certificate_secret_name, expected_type=type_hints["azure_key_vault_certificate_secret_name"])
            check_type(argname="argument azure_key_vault_certificate_secret_version", value=azure_key_vault_certificate_secret_version, expected_type=type_hints["azure_key_vault_certificate_secret_version"])
            check_type(argname="argument azure_key_vault_certificate_vault_id", value=azure_key_vault_certificate_vault_id, expected_type=type_hints["azure_key_vault_certificate_vault_id"])
            check_type(argname="argument certificate_source", value=certificate_source, expected_type=type_hints["certificate_source"])
        self._values: typing.Dict[str, typing.Any] = {}
        if azure_key_vault_certificate_secret_name is not None:
            self._values["azure_key_vault_certificate_secret_name"] = azure_key_vault_certificate_secret_name
        if azure_key_vault_certificate_secret_version is not None:
            self._values["azure_key_vault_certificate_secret_version"] = azure_key_vault_certificate_secret_version
        if azure_key_vault_certificate_vault_id is not None:
            self._values["azure_key_vault_certificate_vault_id"] = azure_key_vault_certificate_vault_id
        if certificate_source is not None:
            self._values["certificate_source"] = certificate_source

    @builtins.property
    def azure_key_vault_certificate_secret_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#azure_key_vault_certificate_secret_name FrontdoorCustomHttpsConfiguration#azure_key_vault_certificate_secret_name}.'''
        result = self._values.get("azure_key_vault_certificate_secret_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_key_vault_certificate_secret_version(
        self,
    ) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#azure_key_vault_certificate_secret_version FrontdoorCustomHttpsConfiguration#azure_key_vault_certificate_secret_version}.'''
        result = self._values.get("azure_key_vault_certificate_secret_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_key_vault_certificate_vault_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#azure_key_vault_certificate_vault_id FrontdoorCustomHttpsConfiguration#azure_key_vault_certificate_vault_id}.'''
        result = self._values.get("azure_key_vault_certificate_vault_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_source(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#certificate_source FrontdoorCustomHttpsConfiguration#certificate_source}.'''
        result = self._values.get("certificate_source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FrontdoorCustomHttpsConfigurationCustomHttpsConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FrontdoorCustomHttpsConfigurationCustomHttpsConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoorCustomHttpsConfiguration.FrontdoorCustomHttpsConfigurationCustomHttpsConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(FrontdoorCustomHttpsConfigurationCustomHttpsConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAzureKeyVaultCertificateSecretName")
    def reset_azure_key_vault_certificate_secret_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureKeyVaultCertificateSecretName", []))

    @jsii.member(jsii_name="resetAzureKeyVaultCertificateSecretVersion")
    def reset_azure_key_vault_certificate_secret_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureKeyVaultCertificateSecretVersion", []))

    @jsii.member(jsii_name="resetAzureKeyVaultCertificateVaultId")
    def reset_azure_key_vault_certificate_vault_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureKeyVaultCertificateVaultId", []))

    @jsii.member(jsii_name="resetCertificateSource")
    def reset_certificate_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateSource", []))

    @builtins.property
    @jsii.member(jsii_name="minimumTlsVersion")
    def minimum_tls_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimumTlsVersion"))

    @builtins.property
    @jsii.member(jsii_name="provisioningState")
    def provisioning_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "provisioningState"))

    @builtins.property
    @jsii.member(jsii_name="provisioningSubstate")
    def provisioning_substate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "provisioningSubstate"))

    @builtins.property
    @jsii.member(jsii_name="azureKeyVaultCertificateSecretNameInput")
    def azure_key_vault_certificate_secret_name_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureKeyVaultCertificateSecretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="azureKeyVaultCertificateSecretVersionInput")
    def azure_key_vault_certificate_secret_version_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureKeyVaultCertificateSecretVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="azureKeyVaultCertificateVaultIdInput")
    def azure_key_vault_certificate_vault_id_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureKeyVaultCertificateVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateSourceInput")
    def certificate_source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="azureKeyVaultCertificateSecretName")
    def azure_key_vault_certificate_secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azureKeyVaultCertificateSecretName"))

    @azure_key_vault_certificate_secret_name.setter
    def azure_key_vault_certificate_secret_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorCustomHttpsConfigurationCustomHttpsConfigurationOutputReference, "azure_key_vault_certificate_secret_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureKeyVaultCertificateSecretName", value)

    @builtins.property
    @jsii.member(jsii_name="azureKeyVaultCertificateSecretVersion")
    def azure_key_vault_certificate_secret_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azureKeyVaultCertificateSecretVersion"))

    @azure_key_vault_certificate_secret_version.setter
    def azure_key_vault_certificate_secret_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorCustomHttpsConfigurationCustomHttpsConfigurationOutputReference, "azure_key_vault_certificate_secret_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureKeyVaultCertificateSecretVersion", value)

    @builtins.property
    @jsii.member(jsii_name="azureKeyVaultCertificateVaultId")
    def azure_key_vault_certificate_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azureKeyVaultCertificateVaultId"))

    @azure_key_vault_certificate_vault_id.setter
    def azure_key_vault_certificate_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorCustomHttpsConfigurationCustomHttpsConfigurationOutputReference, "azure_key_vault_certificate_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureKeyVaultCertificateVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="certificateSource")
    def certificate_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateSource"))

    @certificate_source.setter
    def certificate_source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorCustomHttpsConfigurationCustomHttpsConfigurationOutputReference, "certificate_source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateSource", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[FrontdoorCustomHttpsConfigurationCustomHttpsConfiguration]:
        return typing.cast(typing.Optional[FrontdoorCustomHttpsConfigurationCustomHttpsConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FrontdoorCustomHttpsConfigurationCustomHttpsConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorCustomHttpsConfigurationCustomHttpsConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.frontdoorCustomHttpsConfiguration.FrontdoorCustomHttpsConfigurationTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class FrontdoorCustomHttpsConfigurationTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#create FrontdoorCustomHttpsConfiguration#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#delete FrontdoorCustomHttpsConfiguration#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#read FrontdoorCustomHttpsConfiguration#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#update FrontdoorCustomHttpsConfiguration#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorCustomHttpsConfigurationTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#create FrontdoorCustomHttpsConfiguration#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#delete FrontdoorCustomHttpsConfiguration#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#read FrontdoorCustomHttpsConfiguration#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor_custom_https_configuration#update FrontdoorCustomHttpsConfiguration#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FrontdoorCustomHttpsConfigurationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FrontdoorCustomHttpsConfigurationTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoorCustomHttpsConfiguration.FrontdoorCustomHttpsConfigurationTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(FrontdoorCustomHttpsConfigurationTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(FrontdoorCustomHttpsConfigurationTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorCustomHttpsConfigurationTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorCustomHttpsConfigurationTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorCustomHttpsConfigurationTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FrontdoorCustomHttpsConfigurationTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FrontdoorCustomHttpsConfigurationTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FrontdoorCustomHttpsConfigurationTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorCustomHttpsConfigurationTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "FrontdoorCustomHttpsConfiguration",
    "FrontdoorCustomHttpsConfigurationConfig",
    "FrontdoorCustomHttpsConfigurationCustomHttpsConfiguration",
    "FrontdoorCustomHttpsConfigurationCustomHttpsConfigurationOutputReference",
    "FrontdoorCustomHttpsConfigurationTimeouts",
    "FrontdoorCustomHttpsConfigurationTimeoutsOutputReference",
]

publication.publish()
