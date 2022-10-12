'''
# `google_identity_platform_tenant_default_supported_idp_config`

Refer to the Terraform Registory for docs: [`google_identity_platform_tenant_default_supported_idp_config`](https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config).
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


class GoogleIdentityPlatformTenantDefaultSupportedIdpConfig(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleIdentityPlatformTenantDefaultSupportedIdpConfig.GoogleIdentityPlatformTenantDefaultSupportedIdpConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config google_identity_platform_tenant_default_supported_idp_config}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        idp_id: builtins.str,
        tenant: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config google_identity_platform_tenant_default_supported_idp_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param client_id: OAuth client ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#client_id GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#client_id}
        :param client_secret: OAuth client secret. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#client_secret GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#client_secret}
        :param idp_id: ID of the IDP. Possible values include:. 'apple.com' 'facebook.com' 'gc.apple.com' 'github.com' 'google.com' 'linkedin.com' 'microsoft.com' 'playgames.google.com' 'twitter.com' 'yahoo.com' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#idp_id GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#idp_id}
        :param tenant: The name of the tenant where this DefaultSupportedIdpConfig resource exists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#tenant GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#tenant}
        :param enabled: If this IDP allows the user to sign in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#enabled GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#id GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#project GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#timeouts GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantDefaultSupportedIdpConfig.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleIdentityPlatformTenantDefaultSupportedIdpConfigConfig(
            client_id=client_id,
            client_secret=client_secret,
            idp_id=idp_id,
            tenant=tenant,
            enabled=enabled,
            id=id,
            project=project,
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

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#create GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#delete GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#update GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#update}.
        '''
        value = GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeoutsOutputReference":
        return typing.cast("GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

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
    @jsii.member(jsii_name="idpIdInput")
    def idp_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idpIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantInput")
    def tenant_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantDefaultSupportedIdpConfig, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantDefaultSupportedIdpConfig, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantDefaultSupportedIdpConfig, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantDefaultSupportedIdpConfig, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="idpId")
    def idp_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idpId"))

    @idp_id.setter
    def idp_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantDefaultSupportedIdpConfig, "idp_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idpId", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantDefaultSupportedIdpConfig, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="tenant")
    def tenant(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenant"))

    @tenant.setter
    def tenant(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantDefaultSupportedIdpConfig, "tenant").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenant", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleIdentityPlatformTenantDefaultSupportedIdpConfig.GoogleIdentityPlatformTenantDefaultSupportedIdpConfigConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "idp_id": "idpId",
        "tenant": "tenant",
        "enabled": "enabled",
        "id": "id",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GoogleIdentityPlatformTenantDefaultSupportedIdpConfigConfig(
    cdktf.TerraformMetaArguments,
):
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
        client_id: builtins.str,
        client_secret: builtins.str,
        idp_id: builtins.str,
        tenant: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param client_id: OAuth client ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#client_id GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#client_id}
        :param client_secret: OAuth client secret. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#client_secret GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#client_secret}
        :param idp_id: ID of the IDP. Possible values include:. 'apple.com' 'facebook.com' 'gc.apple.com' 'github.com' 'google.com' 'linkedin.com' 'microsoft.com' 'playgames.google.com' 'twitter.com' 'yahoo.com' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#idp_id GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#idp_id}
        :param tenant: The name of the tenant where this DefaultSupportedIdpConfig resource exists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#tenant GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#tenant}
        :param enabled: If this IDP allows the user to sign in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#enabled GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#id GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#project GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#timeouts GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantDefaultSupportedIdpConfigConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument idp_id", value=idp_id, expected_type=type_hints["idp_id"])
            check_type(argname="argument tenant", value=tenant, expected_type=type_hints["tenant"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
            "idp_id": idp_id,
            "tenant": tenant,
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
        if project is not None:
            self._values["project"] = project
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
    def client_id(self) -> builtins.str:
        '''OAuth client ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#client_id GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''OAuth client secret.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#client_secret GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#client_secret}
        '''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def idp_id(self) -> builtins.str:
        '''ID of the IDP. Possible values include:.

        'apple.com'

        'facebook.com'

        'gc.apple.com'

        'github.com'

        'google.com'

        'linkedin.com'

        'microsoft.com'

        'playgames.google.com'

        'twitter.com'

        'yahoo.com'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#idp_id GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#idp_id}
        '''
        result = self._values.get("idp_id")
        assert result is not None, "Required property 'idp_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tenant(self) -> builtins.str:
        '''The name of the tenant where this DefaultSupportedIdpConfig resource exists.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#tenant GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#tenant}
        '''
        result = self._values.get("tenant")
        assert result is not None, "Required property 'tenant' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If this IDP allows the user to sign in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#enabled GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#id GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#project GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#timeouts GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleIdentityPlatformTenantDefaultSupportedIdpConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleIdentityPlatformTenantDefaultSupportedIdpConfig.GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#create GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#delete GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#update GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#create GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#delete GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_default_supported_idp_config#update GoogleIdentityPlatformTenantDefaultSupportedIdpConfig#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleIdentityPlatformTenantDefaultSupportedIdpConfig.GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

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
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleIdentityPlatformTenantDefaultSupportedIdpConfig",
    "GoogleIdentityPlatformTenantDefaultSupportedIdpConfigConfig",
    "GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeouts",
    "GoogleIdentityPlatformTenantDefaultSupportedIdpConfigTimeoutsOutputReference",
]

publication.publish()
