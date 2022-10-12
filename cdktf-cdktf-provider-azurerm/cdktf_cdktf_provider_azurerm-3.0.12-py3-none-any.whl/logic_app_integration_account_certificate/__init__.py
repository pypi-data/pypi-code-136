'''
# `azurerm_logic_app_integration_account_certificate`

Refer to the Terraform Registory for docs: [`azurerm_logic_app_integration_account_certificate`](https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate).
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


class LogicAppIntegrationAccountCertificate(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppIntegrationAccountCertificate.LogicAppIntegrationAccountCertificate",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate azurerm_logic_app_integration_account_certificate}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        integration_account_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        key_vault_key: typing.Optional[typing.Union["LogicAppIntegrationAccountCertificateKeyVaultKey", typing.Dict[str, typing.Any]]] = None,
        metadata: typing.Optional[builtins.str] = None,
        public_certificate: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["LogicAppIntegrationAccountCertificateTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate azurerm_logic_app_integration_account_certificate} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param integration_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#integration_account_name LogicAppIntegrationAccountCertificate#integration_account_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#name LogicAppIntegrationAccountCertificate#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#resource_group_name LogicAppIntegrationAccountCertificate#resource_group_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#id LogicAppIntegrationAccountCertificate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param key_vault_key: key_vault_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#key_vault_key LogicAppIntegrationAccountCertificate#key_vault_key}
        :param metadata: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#metadata LogicAppIntegrationAccountCertificate#metadata}.
        :param public_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#public_certificate LogicAppIntegrationAccountCertificate#public_certificate}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#timeouts LogicAppIntegrationAccountCertificate#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppIntegrationAccountCertificate.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LogicAppIntegrationAccountCertificateConfig(
            integration_account_name=integration_account_name,
            name=name,
            resource_group_name=resource_group_name,
            id=id,
            key_vault_key=key_vault_key,
            metadata=metadata,
            public_certificate=public_certificate,
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

    @jsii.member(jsii_name="putKeyVaultKey")
    def put_key_vault_key(
        self,
        *,
        key_name: builtins.str,
        key_vault_id: builtins.str,
        key_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#key_name LogicAppIntegrationAccountCertificate#key_name}.
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#key_vault_id LogicAppIntegrationAccountCertificate#key_vault_id}.
        :param key_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#key_version LogicAppIntegrationAccountCertificate#key_version}.
        '''
        value = LogicAppIntegrationAccountCertificateKeyVaultKey(
            key_name=key_name, key_vault_id=key_vault_id, key_version=key_version
        )

        return typing.cast(None, jsii.invoke(self, "putKeyVaultKey", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#create LogicAppIntegrationAccountCertificate#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#delete LogicAppIntegrationAccountCertificate#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#read LogicAppIntegrationAccountCertificate#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#update LogicAppIntegrationAccountCertificate#update}.
        '''
        value = LogicAppIntegrationAccountCertificateTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKeyVaultKey")
    def reset_key_vault_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultKey", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetPublicCertificate")
    def reset_public_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicCertificate", []))

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
    @jsii.member(jsii_name="keyVaultKey")
    def key_vault_key(
        self,
    ) -> "LogicAppIntegrationAccountCertificateKeyVaultKeyOutputReference":
        return typing.cast("LogicAppIntegrationAccountCertificateKeyVaultKeyOutputReference", jsii.get(self, "keyVaultKey"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "LogicAppIntegrationAccountCertificateTimeoutsOutputReference":
        return typing.cast("LogicAppIntegrationAccountCertificateTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationAccountNameInput")
    def integration_account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationAccountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultKeyInput")
    def key_vault_key_input(
        self,
    ) -> typing.Optional["LogicAppIntegrationAccountCertificateKeyVaultKey"]:
        return typing.cast(typing.Optional["LogicAppIntegrationAccountCertificateKeyVaultKey"], jsii.get(self, "keyVaultKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicCertificateInput")
    def public_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LogicAppIntegrationAccountCertificateTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LogicAppIntegrationAccountCertificateTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountCertificate, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="integrationAccountName")
    def integration_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "integrationAccountName"))

    @integration_account_name.setter
    def integration_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountCertificate, "integration_account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountCertificate, "metadata").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountCertificate, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="publicCertificate")
    def public_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicCertificate"))

    @public_certificate.setter
    def public_certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountCertificate, "public_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountCertificate, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppIntegrationAccountCertificate.LogicAppIntegrationAccountCertificateConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "integration_account_name": "integrationAccountName",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "id": "id",
        "key_vault_key": "keyVaultKey",
        "metadata": "metadata",
        "public_certificate": "publicCertificate",
        "timeouts": "timeouts",
    },
)
class LogicAppIntegrationAccountCertificateConfig(cdktf.TerraformMetaArguments):
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
        integration_account_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        key_vault_key: typing.Optional[typing.Union["LogicAppIntegrationAccountCertificateKeyVaultKey", typing.Dict[str, typing.Any]]] = None,
        metadata: typing.Optional[builtins.str] = None,
        public_certificate: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["LogicAppIntegrationAccountCertificateTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param integration_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#integration_account_name LogicAppIntegrationAccountCertificate#integration_account_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#name LogicAppIntegrationAccountCertificate#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#resource_group_name LogicAppIntegrationAccountCertificate#resource_group_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#id LogicAppIntegrationAccountCertificate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param key_vault_key: key_vault_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#key_vault_key LogicAppIntegrationAccountCertificate#key_vault_key}
        :param metadata: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#metadata LogicAppIntegrationAccountCertificate#metadata}.
        :param public_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#public_certificate LogicAppIntegrationAccountCertificate#public_certificate}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#timeouts LogicAppIntegrationAccountCertificate#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(key_vault_key, dict):
            key_vault_key = LogicAppIntegrationAccountCertificateKeyVaultKey(**key_vault_key)
        if isinstance(timeouts, dict):
            timeouts = LogicAppIntegrationAccountCertificateTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppIntegrationAccountCertificateConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument integration_account_name", value=integration_account_name, expected_type=type_hints["integration_account_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument key_vault_key", value=key_vault_key, expected_type=type_hints["key_vault_key"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument public_certificate", value=public_certificate, expected_type=type_hints["public_certificate"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "integration_account_name": integration_account_name,
            "name": name,
            "resource_group_name": resource_group_name,
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
        if key_vault_key is not None:
            self._values["key_vault_key"] = key_vault_key
        if metadata is not None:
            self._values["metadata"] = metadata
        if public_certificate is not None:
            self._values["public_certificate"] = public_certificate
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
    def integration_account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#integration_account_name LogicAppIntegrationAccountCertificate#integration_account_name}.'''
        result = self._values.get("integration_account_name")
        assert result is not None, "Required property 'integration_account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#name LogicAppIntegrationAccountCertificate#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#resource_group_name LogicAppIntegrationAccountCertificate#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#id LogicAppIntegrationAccountCertificate#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_vault_key(
        self,
    ) -> typing.Optional["LogicAppIntegrationAccountCertificateKeyVaultKey"]:
        '''key_vault_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#key_vault_key LogicAppIntegrationAccountCertificate#key_vault_key}
        '''
        result = self._values.get("key_vault_key")
        return typing.cast(typing.Optional["LogicAppIntegrationAccountCertificateKeyVaultKey"], result)

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#metadata LogicAppIntegrationAccountCertificate#metadata}.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#public_certificate LogicAppIntegrationAccountCertificate#public_certificate}.'''
        result = self._values.get("public_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["LogicAppIntegrationAccountCertificateTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#timeouts LogicAppIntegrationAccountCertificate#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LogicAppIntegrationAccountCertificateTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppIntegrationAccountCertificateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppIntegrationAccountCertificate.LogicAppIntegrationAccountCertificateKeyVaultKey",
    jsii_struct_bases=[],
    name_mapping={
        "key_name": "keyName",
        "key_vault_id": "keyVaultId",
        "key_version": "keyVersion",
    },
)
class LogicAppIntegrationAccountCertificateKeyVaultKey:
    def __init__(
        self,
        *,
        key_name: builtins.str,
        key_vault_id: builtins.str,
        key_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#key_name LogicAppIntegrationAccountCertificate#key_name}.
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#key_vault_id LogicAppIntegrationAccountCertificate#key_vault_id}.
        :param key_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#key_version LogicAppIntegrationAccountCertificate#key_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppIntegrationAccountCertificateKeyVaultKey.__init__)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
            check_type(argname="argument key_version", value=key_version, expected_type=type_hints["key_version"])
        self._values: typing.Dict[str, typing.Any] = {
            "key_name": key_name,
            "key_vault_id": key_vault_id,
        }
        if key_version is not None:
            self._values["key_version"] = key_version

    @builtins.property
    def key_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#key_name LogicAppIntegrationAccountCertificate#key_name}.'''
        result = self._values.get("key_name")
        assert result is not None, "Required property 'key_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_vault_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#key_vault_id LogicAppIntegrationAccountCertificate#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        assert result is not None, "Required property 'key_vault_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#key_version LogicAppIntegrationAccountCertificate#key_version}.'''
        result = self._values.get("key_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppIntegrationAccountCertificateKeyVaultKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogicAppIntegrationAccountCertificateKeyVaultKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppIntegrationAccountCertificate.LogicAppIntegrationAccountCertificateKeyVaultKeyOutputReference",
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
            type_hints = typing.get_type_hints(LogicAppIntegrationAccountCertificateKeyVaultKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKeyVersion")
    def reset_key_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVersion", []))

    @builtins.property
    @jsii.member(jsii_name="keyNameInput")
    def key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultIdInput")
    def key_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVersionInput")
    def key_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyName"))

    @key_name.setter
    def key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountCertificateKeyVaultKeyOutputReference, "key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyName", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultId")
    def key_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultId"))

    @key_vault_id.setter
    def key_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountCertificateKeyVaultKeyOutputReference, "key_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="keyVersion")
    def key_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVersion"))

    @key_version.setter
    def key_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountCertificateKeyVaultKeyOutputReference, "key_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogicAppIntegrationAccountCertificateKeyVaultKey]:
        return typing.cast(typing.Optional[LogicAppIntegrationAccountCertificateKeyVaultKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogicAppIntegrationAccountCertificateKeyVaultKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountCertificateKeyVaultKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppIntegrationAccountCertificate.LogicAppIntegrationAccountCertificateTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class LogicAppIntegrationAccountCertificateTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#create LogicAppIntegrationAccountCertificate#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#delete LogicAppIntegrationAccountCertificate#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#read LogicAppIntegrationAccountCertificate#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#update LogicAppIntegrationAccountCertificate#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppIntegrationAccountCertificateTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#create LogicAppIntegrationAccountCertificate#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#delete LogicAppIntegrationAccountCertificate#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#read LogicAppIntegrationAccountCertificate#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_certificate#update LogicAppIntegrationAccountCertificate#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppIntegrationAccountCertificateTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogicAppIntegrationAccountCertificateTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppIntegrationAccountCertificate.LogicAppIntegrationAccountCertificateTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(LogicAppIntegrationAccountCertificateTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountCertificateTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountCertificateTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountCertificateTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountCertificateTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LogicAppIntegrationAccountCertificateTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LogicAppIntegrationAccountCertificateTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LogicAppIntegrationAccountCertificateTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountCertificateTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LogicAppIntegrationAccountCertificate",
    "LogicAppIntegrationAccountCertificateConfig",
    "LogicAppIntegrationAccountCertificateKeyVaultKey",
    "LogicAppIntegrationAccountCertificateKeyVaultKeyOutputReference",
    "LogicAppIntegrationAccountCertificateTimeouts",
    "LogicAppIntegrationAccountCertificateTimeoutsOutputReference",
]

publication.publish()
