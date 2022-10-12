'''
# `cloudflare_access_identity_provider`

Refer to the Terraform Registory for docs: [`cloudflare_access_identity_provider`](https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider).
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


class AccessIdentityProvider(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessIdentityProvider.AccessIdentityProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider cloudflare_access_identity_provider}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessIdentityProviderConfigA", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        zone_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider cloudflare_access_identity_provider} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Friendly name of the Access Identity Provider configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#name AccessIdentityProvider#name}
        :param type: The provider type to use. Available values: ``centrify``, ``facebook``, ``google-apps``, ``oidc``, ``github``, ``google``, ``saml``, ``linkedin``, ``azureAD``, ``okta``, ``onetimepin``, ``onelogin``, ``yandex``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#type AccessIdentityProvider#type}
        :param account_id: The account identifier to target for the resource. Conflicts with ``zone_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#account_id AccessIdentityProvider#account_id}
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#config AccessIdentityProvider#config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#id AccessIdentityProvider#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param zone_id: The zone identifier to target for the resource. Conflicts with ``account_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#zone_id AccessIdentityProvider#zone_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessIdentityProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config_ = AccessIdentityProviderConfig(
            name=name,
            type=type,
            account_id=account_id,
            config=config,
            id=id,
            zone_id=zone_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config_])

    @jsii.member(jsii_name="putConfig")
    def put_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessIdentityProviderConfigA", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessIdentityProvider.put_config)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConfig", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetConfig")
    def reset_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetZoneId")
    def reset_zone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(self) -> "AccessIdentityProviderConfigAList":
        return typing.cast("AccessIdentityProviderConfigAList", jsii.get(self, "config"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="configInput")
    def config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessIdentityProviderConfigA"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessIdentityProviderConfigA"]]], jsii.get(self, "configInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProvider, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProvider, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProvider, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProvider, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProvider, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessIdentityProvider.AccessIdentityProviderConfig",
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
        "type": "type",
        "account_id": "accountId",
        "config": "config",
        "id": "id",
        "zone_id": "zoneId",
    },
)
class AccessIdentityProviderConfig(cdktf.TerraformMetaArguments):
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
        type: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessIdentityProviderConfigA", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Friendly name of the Access Identity Provider configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#name AccessIdentityProvider#name}
        :param type: The provider type to use. Available values: ``centrify``, ``facebook``, ``google-apps``, ``oidc``, ``github``, ``google``, ``saml``, ``linkedin``, ``azureAD``, ``okta``, ``onetimepin``, ``onelogin``, ``yandex``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#type AccessIdentityProvider#type}
        :param account_id: The account identifier to target for the resource. Conflicts with ``zone_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#account_id AccessIdentityProvider#account_id}
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#config AccessIdentityProvider#config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#id AccessIdentityProvider#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param zone_id: The zone identifier to target for the resource. Conflicts with ``account_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#zone_id AccessIdentityProvider#zone_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AccessIdentityProviderConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
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
        if account_id is not None:
            self._values["account_id"] = account_id
        if config is not None:
            self._values["config"] = config
        if id is not None:
            self._values["id"] = id
        if zone_id is not None:
            self._values["zone_id"] = zone_id

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
        '''Friendly name of the Access Identity Provider configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#name AccessIdentityProvider#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The provider type to use.

        Available values: ``centrify``, ``facebook``, ``google-apps``, ``oidc``, ``github``, ``google``, ``saml``, ``linkedin``, ``azureAD``, ``okta``, ``onetimepin``, ``onelogin``, ``yandex``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#type AccessIdentityProvider#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''The account identifier to target for the resource. Conflicts with ``zone_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#account_id AccessIdentityProvider#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessIdentityProviderConfigA"]]]:
        '''config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#config AccessIdentityProvider#config}
        '''
        result = self._values.get("config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessIdentityProviderConfigA"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#id AccessIdentityProvider#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''The zone identifier to target for the resource. Conflicts with ``account_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#zone_id AccessIdentityProvider#zone_id}
        '''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessIdentityProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessIdentityProvider.AccessIdentityProviderConfigA",
    jsii_struct_bases=[],
    name_mapping={
        "api_token": "apiToken",
        "apps_domain": "appsDomain",
        "attributes": "attributes",
        "auth_url": "authUrl",
        "centrify_account": "centrifyAccount",
        "centrify_app_id": "centrifyAppId",
        "certs_url": "certsUrl",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "directory_id": "directoryId",
        "email_attribute_name": "emailAttributeName",
        "idp_public_cert": "idpPublicCert",
        "issuer_url": "issuerUrl",
        "okta_account": "oktaAccount",
        "onelogin_account": "oneloginAccount",
        "pkce_enabled": "pkceEnabled",
        "redirect_url": "redirectUrl",
        "sign_request": "signRequest",
        "sso_target_url": "ssoTargetUrl",
        "support_groups": "supportGroups",
        "token_url": "tokenUrl",
    },
)
class AccessIdentityProviderConfigA:
    def __init__(
        self,
        *,
        api_token: typing.Optional[builtins.str] = None,
        apps_domain: typing.Optional[builtins.str] = None,
        attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        auth_url: typing.Optional[builtins.str] = None,
        centrify_account: typing.Optional[builtins.str] = None,
        centrify_app_id: typing.Optional[builtins.str] = None,
        certs_url: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        directory_id: typing.Optional[builtins.str] = None,
        email_attribute_name: typing.Optional[builtins.str] = None,
        idp_public_cert: typing.Optional[builtins.str] = None,
        issuer_url: typing.Optional[builtins.str] = None,
        okta_account: typing.Optional[builtins.str] = None,
        onelogin_account: typing.Optional[builtins.str] = None,
        pkce_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        redirect_url: typing.Optional[builtins.str] = None,
        sign_request: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sso_target_url: typing.Optional[builtins.str] = None,
        support_groups: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        token_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#api_token AccessIdentityProvider#api_token}.
        :param apps_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#apps_domain AccessIdentityProvider#apps_domain}.
        :param attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#attributes AccessIdentityProvider#attributes}.
        :param auth_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#auth_url AccessIdentityProvider#auth_url}.
        :param centrify_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#centrify_account AccessIdentityProvider#centrify_account}.
        :param centrify_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#centrify_app_id AccessIdentityProvider#centrify_app_id}.
        :param certs_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#certs_url AccessIdentityProvider#certs_url}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#client_id AccessIdentityProvider#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#client_secret AccessIdentityProvider#client_secret}.
        :param directory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#directory_id AccessIdentityProvider#directory_id}.
        :param email_attribute_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#email_attribute_name AccessIdentityProvider#email_attribute_name}.
        :param idp_public_cert: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#idp_public_cert AccessIdentityProvider#idp_public_cert}.
        :param issuer_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#issuer_url AccessIdentityProvider#issuer_url}.
        :param okta_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#okta_account AccessIdentityProvider#okta_account}.
        :param onelogin_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#onelogin_account AccessIdentityProvider#onelogin_account}.
        :param pkce_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#pkce_enabled AccessIdentityProvider#pkce_enabled}.
        :param redirect_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#redirect_url AccessIdentityProvider#redirect_url}.
        :param sign_request: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#sign_request AccessIdentityProvider#sign_request}.
        :param sso_target_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#sso_target_url AccessIdentityProvider#sso_target_url}.
        :param support_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#support_groups AccessIdentityProvider#support_groups}.
        :param token_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#token_url AccessIdentityProvider#token_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessIdentityProviderConfigA.__init__)
            check_type(argname="argument api_token", value=api_token, expected_type=type_hints["api_token"])
            check_type(argname="argument apps_domain", value=apps_domain, expected_type=type_hints["apps_domain"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument auth_url", value=auth_url, expected_type=type_hints["auth_url"])
            check_type(argname="argument centrify_account", value=centrify_account, expected_type=type_hints["centrify_account"])
            check_type(argname="argument centrify_app_id", value=centrify_app_id, expected_type=type_hints["centrify_app_id"])
            check_type(argname="argument certs_url", value=certs_url, expected_type=type_hints["certs_url"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument directory_id", value=directory_id, expected_type=type_hints["directory_id"])
            check_type(argname="argument email_attribute_name", value=email_attribute_name, expected_type=type_hints["email_attribute_name"])
            check_type(argname="argument idp_public_cert", value=idp_public_cert, expected_type=type_hints["idp_public_cert"])
            check_type(argname="argument issuer_url", value=issuer_url, expected_type=type_hints["issuer_url"])
            check_type(argname="argument okta_account", value=okta_account, expected_type=type_hints["okta_account"])
            check_type(argname="argument onelogin_account", value=onelogin_account, expected_type=type_hints["onelogin_account"])
            check_type(argname="argument pkce_enabled", value=pkce_enabled, expected_type=type_hints["pkce_enabled"])
            check_type(argname="argument redirect_url", value=redirect_url, expected_type=type_hints["redirect_url"])
            check_type(argname="argument sign_request", value=sign_request, expected_type=type_hints["sign_request"])
            check_type(argname="argument sso_target_url", value=sso_target_url, expected_type=type_hints["sso_target_url"])
            check_type(argname="argument support_groups", value=support_groups, expected_type=type_hints["support_groups"])
            check_type(argname="argument token_url", value=token_url, expected_type=type_hints["token_url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if api_token is not None:
            self._values["api_token"] = api_token
        if apps_domain is not None:
            self._values["apps_domain"] = apps_domain
        if attributes is not None:
            self._values["attributes"] = attributes
        if auth_url is not None:
            self._values["auth_url"] = auth_url
        if centrify_account is not None:
            self._values["centrify_account"] = centrify_account
        if centrify_app_id is not None:
            self._values["centrify_app_id"] = centrify_app_id
        if certs_url is not None:
            self._values["certs_url"] = certs_url
        if client_id is not None:
            self._values["client_id"] = client_id
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if directory_id is not None:
            self._values["directory_id"] = directory_id
        if email_attribute_name is not None:
            self._values["email_attribute_name"] = email_attribute_name
        if idp_public_cert is not None:
            self._values["idp_public_cert"] = idp_public_cert
        if issuer_url is not None:
            self._values["issuer_url"] = issuer_url
        if okta_account is not None:
            self._values["okta_account"] = okta_account
        if onelogin_account is not None:
            self._values["onelogin_account"] = onelogin_account
        if pkce_enabled is not None:
            self._values["pkce_enabled"] = pkce_enabled
        if redirect_url is not None:
            self._values["redirect_url"] = redirect_url
        if sign_request is not None:
            self._values["sign_request"] = sign_request
        if sso_target_url is not None:
            self._values["sso_target_url"] = sso_target_url
        if support_groups is not None:
            self._values["support_groups"] = support_groups
        if token_url is not None:
            self._values["token_url"] = token_url

    @builtins.property
    def api_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#api_token AccessIdentityProvider#api_token}.'''
        result = self._values.get("api_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def apps_domain(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#apps_domain AccessIdentityProvider#apps_domain}.'''
        result = self._values.get("apps_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attributes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#attributes AccessIdentityProvider#attributes}.'''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def auth_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#auth_url AccessIdentityProvider#auth_url}.'''
        result = self._values.get("auth_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def centrify_account(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#centrify_account AccessIdentityProvider#centrify_account}.'''
        result = self._values.get("centrify_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def centrify_app_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#centrify_app_id AccessIdentityProvider#centrify_app_id}.'''
        result = self._values.get("centrify_app_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certs_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#certs_url AccessIdentityProvider#certs_url}.'''
        result = self._values.get("certs_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#client_id AccessIdentityProvider#client_id}.'''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#client_secret AccessIdentityProvider#client_secret}.'''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#directory_id AccessIdentityProvider#directory_id}.'''
        result = self._values.get("directory_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_attribute_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#email_attribute_name AccessIdentityProvider#email_attribute_name}.'''
        result = self._values.get("email_attribute_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idp_public_cert(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#idp_public_cert AccessIdentityProvider#idp_public_cert}.'''
        result = self._values.get("idp_public_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def issuer_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#issuer_url AccessIdentityProvider#issuer_url}.'''
        result = self._values.get("issuer_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def okta_account(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#okta_account AccessIdentityProvider#okta_account}.'''
        result = self._values.get("okta_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def onelogin_account(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#onelogin_account AccessIdentityProvider#onelogin_account}.'''
        result = self._values.get("onelogin_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pkce_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#pkce_enabled AccessIdentityProvider#pkce_enabled}.'''
        result = self._values.get("pkce_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def redirect_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#redirect_url AccessIdentityProvider#redirect_url}.'''
        result = self._values.get("redirect_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sign_request(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#sign_request AccessIdentityProvider#sign_request}.'''
        result = self._values.get("sign_request")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def sso_target_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#sso_target_url AccessIdentityProvider#sso_target_url}.'''
        result = self._values.get("sso_target_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def support_groups(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#support_groups AccessIdentityProvider#support_groups}.'''
        result = self._values.get("support_groups")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def token_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_identity_provider#token_url AccessIdentityProvider#token_url}.'''
        result = self._values.get("token_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessIdentityProviderConfigA(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessIdentityProviderConfigAList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessIdentityProvider.AccessIdentityProviderConfigAList",
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
            type_hints = typing.get_type_hints(AccessIdentityProviderConfigAList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessIdentityProviderConfigAOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessIdentityProviderConfigAList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessIdentityProviderConfigAOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessIdentityProviderConfigA]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessIdentityProviderConfigA]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessIdentityProviderConfigA]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessIdentityProviderConfigAOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessIdentityProvider.AccessIdentityProviderConfigAOutputReference",
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
            type_hints = typing.get_type_hints(AccessIdentityProviderConfigAOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetApiToken")
    def reset_api_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiToken", []))

    @jsii.member(jsii_name="resetAppsDomain")
    def reset_apps_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppsDomain", []))

    @jsii.member(jsii_name="resetAttributes")
    def reset_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributes", []))

    @jsii.member(jsii_name="resetAuthUrl")
    def reset_auth_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthUrl", []))

    @jsii.member(jsii_name="resetCentrifyAccount")
    def reset_centrify_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCentrifyAccount", []))

    @jsii.member(jsii_name="resetCentrifyAppId")
    def reset_centrify_app_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCentrifyAppId", []))

    @jsii.member(jsii_name="resetCertsUrl")
    def reset_certs_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertsUrl", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetDirectoryId")
    def reset_directory_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectoryId", []))

    @jsii.member(jsii_name="resetEmailAttributeName")
    def reset_email_attribute_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailAttributeName", []))

    @jsii.member(jsii_name="resetIdpPublicCert")
    def reset_idp_public_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdpPublicCert", []))

    @jsii.member(jsii_name="resetIssuerUrl")
    def reset_issuer_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuerUrl", []))

    @jsii.member(jsii_name="resetOktaAccount")
    def reset_okta_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOktaAccount", []))

    @jsii.member(jsii_name="resetOneloginAccount")
    def reset_onelogin_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOneloginAccount", []))

    @jsii.member(jsii_name="resetPkceEnabled")
    def reset_pkce_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPkceEnabled", []))

    @jsii.member(jsii_name="resetRedirectUrl")
    def reset_redirect_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUrl", []))

    @jsii.member(jsii_name="resetSignRequest")
    def reset_sign_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignRequest", []))

    @jsii.member(jsii_name="resetSsoTargetUrl")
    def reset_sso_target_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSsoTargetUrl", []))

    @jsii.member(jsii_name="resetSupportGroups")
    def reset_support_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSupportGroups", []))

    @jsii.member(jsii_name="resetTokenUrl")
    def reset_token_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenUrl", []))

    @builtins.property
    @jsii.member(jsii_name="apiTokenInput")
    def api_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="appsDomainInput")
    def apps_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appsDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="attributesInput")
    def attributes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "attributesInput"))

    @builtins.property
    @jsii.member(jsii_name="authUrlInput")
    def auth_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="centrifyAccountInput")
    def centrify_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "centrifyAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="centrifyAppIdInput")
    def centrify_app_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "centrifyAppIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certsUrlInput")
    def certs_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certsUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryIdInput")
    def directory_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="emailAttributeNameInput")
    def email_attribute_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailAttributeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idpPublicCertInput")
    def idp_public_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idpPublicCertInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerUrlInput")
    def issuer_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="oktaAccountInput")
    def okta_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oktaAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="oneloginAccountInput")
    def onelogin_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oneloginAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="pkceEnabledInput")
    def pkce_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "pkceEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUrlInput")
    def redirect_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="signRequestInput")
    def sign_request_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "signRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="ssoTargetUrlInput")
    def sso_target_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ssoTargetUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="supportGroupsInput")
    def support_groups_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "supportGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenUrlInput")
    def token_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="apiToken")
    def api_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiToken"))

    @api_token.setter
    def api_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "api_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiToken", value)

    @builtins.property
    @jsii.member(jsii_name="appsDomain")
    def apps_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appsDomain"))

    @apps_domain.setter
    def apps_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "apps_domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appsDomain", value)

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributes", value)

    @builtins.property
    @jsii.member(jsii_name="authUrl")
    def auth_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authUrl"))

    @auth_url.setter
    def auth_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "auth_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authUrl", value)

    @builtins.property
    @jsii.member(jsii_name="centrifyAccount")
    def centrify_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "centrifyAccount"))

    @centrify_account.setter
    def centrify_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "centrify_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "centrifyAccount", value)

    @builtins.property
    @jsii.member(jsii_name="centrifyAppId")
    def centrify_app_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "centrifyAppId"))

    @centrify_app_id.setter
    def centrify_app_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "centrify_app_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "centrifyAppId", value)

    @builtins.property
    @jsii.member(jsii_name="certsUrl")
    def certs_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certsUrl"))

    @certs_url.setter
    def certs_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "certs_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certsUrl", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="directoryId")
    def directory_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryId"))

    @directory_id.setter
    def directory_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "directory_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryId", value)

    @builtins.property
    @jsii.member(jsii_name="emailAttributeName")
    def email_attribute_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailAttributeName"))

    @email_attribute_name.setter
    def email_attribute_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "email_attribute_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailAttributeName", value)

    @builtins.property
    @jsii.member(jsii_name="idpPublicCert")
    def idp_public_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idpPublicCert"))

    @idp_public_cert.setter
    def idp_public_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "idp_public_cert").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idpPublicCert", value)

    @builtins.property
    @jsii.member(jsii_name="issuerUrl")
    def issuer_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuerUrl"))

    @issuer_url.setter
    def issuer_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "issuer_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuerUrl", value)

    @builtins.property
    @jsii.member(jsii_name="oktaAccount")
    def okta_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oktaAccount"))

    @okta_account.setter
    def okta_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "okta_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oktaAccount", value)

    @builtins.property
    @jsii.member(jsii_name="oneloginAccount")
    def onelogin_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oneloginAccount"))

    @onelogin_account.setter
    def onelogin_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "onelogin_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oneloginAccount", value)

    @builtins.property
    @jsii.member(jsii_name="pkceEnabled")
    def pkce_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "pkceEnabled"))

    @pkce_enabled.setter
    def pkce_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "pkce_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pkceEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUrl")
    def redirect_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUrl"))

    @redirect_url.setter
    def redirect_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "redirect_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUrl", value)

    @builtins.property
    @jsii.member(jsii_name="signRequest")
    def sign_request(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "signRequest"))

    @sign_request.setter
    def sign_request(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "sign_request").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signRequest", value)

    @builtins.property
    @jsii.member(jsii_name="ssoTargetUrl")
    def sso_target_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ssoTargetUrl"))

    @sso_target_url.setter
    def sso_target_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "sso_target_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ssoTargetUrl", value)

    @builtins.property
    @jsii.member(jsii_name="supportGroups")
    def support_groups(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "supportGroups"))

    @support_groups.setter
    def support_groups(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "support_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportGroups", value)

    @builtins.property
    @jsii.member(jsii_name="tokenUrl")
    def token_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenUrl"))

    @token_url.setter
    def token_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "token_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessIdentityProviderConfigA, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessIdentityProviderConfigA, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessIdentityProviderConfigA, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessIdentityProviderConfigAOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AccessIdentityProvider",
    "AccessIdentityProviderConfig",
    "AccessIdentityProviderConfigA",
    "AccessIdentityProviderConfigAList",
    "AccessIdentityProviderConfigAOutputReference",
]

publication.publish()
