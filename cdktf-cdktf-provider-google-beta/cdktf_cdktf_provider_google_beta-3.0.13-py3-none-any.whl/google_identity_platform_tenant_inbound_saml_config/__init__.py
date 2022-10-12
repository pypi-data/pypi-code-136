'''
# `google_identity_platform_tenant_inbound_saml_config`

Refer to the Terraform Registory for docs: [`google_identity_platform_tenant_inbound_saml_config`](https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config).
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


class GoogleIdentityPlatformTenantInboundSamlConfig(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleIdentityPlatformTenantInboundSamlConfig.GoogleIdentityPlatformTenantInboundSamlConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config google_identity_platform_tenant_inbound_saml_config}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        display_name: builtins.str,
        idp_config: typing.Union["GoogleIdentityPlatformTenantInboundSamlConfigIdpConfig", typing.Dict[str, typing.Any]],
        name: builtins.str,
        sp_config: typing.Union["GoogleIdentityPlatformTenantInboundSamlConfigSpConfig", typing.Dict[str, typing.Any]],
        tenant: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleIdentityPlatformTenantInboundSamlConfigTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config google_identity_platform_tenant_inbound_saml_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param display_name: Human friendly display name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#display_name GoogleIdentityPlatformTenantInboundSamlConfig#display_name}
        :param idp_config: idp_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#idp_config GoogleIdentityPlatformTenantInboundSamlConfig#idp_config}
        :param name: The name of the InboundSamlConfig resource. Must start with 'saml.' and can only have alphanumeric characters, hyphens, underscores or periods. The part after 'saml.' must also start with a lowercase letter, end with an alphanumeric character, and have at least 2 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#name GoogleIdentityPlatformTenantInboundSamlConfig#name}
        :param sp_config: sp_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#sp_config GoogleIdentityPlatformTenantInboundSamlConfig#sp_config}
        :param tenant: The name of the tenant where this inbound SAML config resource exists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#tenant GoogleIdentityPlatformTenantInboundSamlConfig#tenant}
        :param enabled: If this config allows users to sign in with the provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#enabled GoogleIdentityPlatformTenantInboundSamlConfig#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#id GoogleIdentityPlatformTenantInboundSamlConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#project GoogleIdentityPlatformTenantInboundSamlConfig#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#timeouts GoogleIdentityPlatformTenantInboundSamlConfig#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantInboundSamlConfig.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleIdentityPlatformTenantInboundSamlConfigConfig(
            display_name=display_name,
            idp_config=idp_config,
            name=name,
            sp_config=sp_config,
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

    @jsii.member(jsii_name="putIdpConfig")
    def put_idp_config(
        self,
        *,
        idp_certificates: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificates", typing.Dict[str, typing.Any]]]],
        idp_entity_id: builtins.str,
        sso_url: builtins.str,
        sign_request: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param idp_certificates: idp_certificates block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#idp_certificates GoogleIdentityPlatformTenantInboundSamlConfig#idp_certificates}
        :param idp_entity_id: Unique identifier for all SAML entities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#idp_entity_id GoogleIdentityPlatformTenantInboundSamlConfig#idp_entity_id}
        :param sso_url: URL to send Authentication request to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#sso_url GoogleIdentityPlatformTenantInboundSamlConfig#sso_url}
        :param sign_request: Indicates if outbounding SAMLRequest should be signed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#sign_request GoogleIdentityPlatformTenantInboundSamlConfig#sign_request}
        '''
        value = GoogleIdentityPlatformTenantInboundSamlConfigIdpConfig(
            idp_certificates=idp_certificates,
            idp_entity_id=idp_entity_id,
            sso_url=sso_url,
            sign_request=sign_request,
        )

        return typing.cast(None, jsii.invoke(self, "putIdpConfig", [value]))

    @jsii.member(jsii_name="putSpConfig")
    def put_sp_config(
        self,
        *,
        callback_uri: builtins.str,
        sp_entity_id: builtins.str,
    ) -> None:
        '''
        :param callback_uri: Callback URI where responses from IDP are handled. Must start with 'https://'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#callback_uri GoogleIdentityPlatformTenantInboundSamlConfig#callback_uri}
        :param sp_entity_id: Unique identifier for all SAML entities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#sp_entity_id GoogleIdentityPlatformTenantInboundSamlConfig#sp_entity_id}
        '''
        value = GoogleIdentityPlatformTenantInboundSamlConfigSpConfig(
            callback_uri=callback_uri, sp_entity_id=sp_entity_id
        )

        return typing.cast(None, jsii.invoke(self, "putSpConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#create GoogleIdentityPlatformTenantInboundSamlConfig#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#delete GoogleIdentityPlatformTenantInboundSamlConfig#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#update GoogleIdentityPlatformTenantInboundSamlConfig#update}.
        '''
        value = GoogleIdentityPlatformTenantInboundSamlConfigTimeouts(
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
    @jsii.member(jsii_name="idpConfig")
    def idp_config(
        self,
    ) -> "GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigOutputReference":
        return typing.cast("GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigOutputReference", jsii.get(self, "idpConfig"))

    @builtins.property
    @jsii.member(jsii_name="spConfig")
    def sp_config(
        self,
    ) -> "GoogleIdentityPlatformTenantInboundSamlConfigSpConfigOutputReference":
        return typing.cast("GoogleIdentityPlatformTenantInboundSamlConfigSpConfigOutputReference", jsii.get(self, "spConfig"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "GoogleIdentityPlatformTenantInboundSamlConfigTimeoutsOutputReference":
        return typing.cast("GoogleIdentityPlatformTenantInboundSamlConfigTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

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
    @jsii.member(jsii_name="idpConfigInput")
    def idp_config_input(
        self,
    ) -> typing.Optional["GoogleIdentityPlatformTenantInboundSamlConfigIdpConfig"]:
        return typing.cast(typing.Optional["GoogleIdentityPlatformTenantInboundSamlConfigIdpConfig"], jsii.get(self, "idpConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="spConfigInput")
    def sp_config_input(
        self,
    ) -> typing.Optional["GoogleIdentityPlatformTenantInboundSamlConfigSpConfig"]:
        return typing.cast(typing.Optional["GoogleIdentityPlatformTenantInboundSamlConfigSpConfig"], jsii.get(self, "spConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantInput")
    def tenant_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleIdentityPlatformTenantInboundSamlConfigTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleIdentityPlatformTenantInboundSamlConfigTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfig, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfig, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfig, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfig, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfig, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="tenant")
    def tenant(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenant"))

    @tenant.setter
    def tenant(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfig, "tenant").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenant", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleIdentityPlatformTenantInboundSamlConfig.GoogleIdentityPlatformTenantInboundSamlConfigConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "display_name": "displayName",
        "idp_config": "idpConfig",
        "name": "name",
        "sp_config": "spConfig",
        "tenant": "tenant",
        "enabled": "enabled",
        "id": "id",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GoogleIdentityPlatformTenantInboundSamlConfigConfig(cdktf.TerraformMetaArguments):
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
        display_name: builtins.str,
        idp_config: typing.Union["GoogleIdentityPlatformTenantInboundSamlConfigIdpConfig", typing.Dict[str, typing.Any]],
        name: builtins.str,
        sp_config: typing.Union["GoogleIdentityPlatformTenantInboundSamlConfigSpConfig", typing.Dict[str, typing.Any]],
        tenant: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleIdentityPlatformTenantInboundSamlConfigTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param display_name: Human friendly display name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#display_name GoogleIdentityPlatformTenantInboundSamlConfig#display_name}
        :param idp_config: idp_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#idp_config GoogleIdentityPlatformTenantInboundSamlConfig#idp_config}
        :param name: The name of the InboundSamlConfig resource. Must start with 'saml.' and can only have alphanumeric characters, hyphens, underscores or periods. The part after 'saml.' must also start with a lowercase letter, end with an alphanumeric character, and have at least 2 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#name GoogleIdentityPlatformTenantInboundSamlConfig#name}
        :param sp_config: sp_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#sp_config GoogleIdentityPlatformTenantInboundSamlConfig#sp_config}
        :param tenant: The name of the tenant where this inbound SAML config resource exists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#tenant GoogleIdentityPlatformTenantInboundSamlConfig#tenant}
        :param enabled: If this config allows users to sign in with the provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#enabled GoogleIdentityPlatformTenantInboundSamlConfig#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#id GoogleIdentityPlatformTenantInboundSamlConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#project GoogleIdentityPlatformTenantInboundSamlConfig#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#timeouts GoogleIdentityPlatformTenantInboundSamlConfig#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(idp_config, dict):
            idp_config = GoogleIdentityPlatformTenantInboundSamlConfigIdpConfig(**idp_config)
        if isinstance(sp_config, dict):
            sp_config = GoogleIdentityPlatformTenantInboundSamlConfigSpConfig(**sp_config)
        if isinstance(timeouts, dict):
            timeouts = GoogleIdentityPlatformTenantInboundSamlConfigTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantInboundSamlConfigConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument idp_config", value=idp_config, expected_type=type_hints["idp_config"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument sp_config", value=sp_config, expected_type=type_hints["sp_config"])
            check_type(argname="argument tenant", value=tenant, expected_type=type_hints["tenant"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "display_name": display_name,
            "idp_config": idp_config,
            "name": name,
            "sp_config": sp_config,
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
    def display_name(self) -> builtins.str:
        '''Human friendly display name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#display_name GoogleIdentityPlatformTenantInboundSamlConfig#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def idp_config(self) -> "GoogleIdentityPlatformTenantInboundSamlConfigIdpConfig":
        '''idp_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#idp_config GoogleIdentityPlatformTenantInboundSamlConfig#idp_config}
        '''
        result = self._values.get("idp_config")
        assert result is not None, "Required property 'idp_config' is missing"
        return typing.cast("GoogleIdentityPlatformTenantInboundSamlConfigIdpConfig", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the InboundSamlConfig resource.

        Must start with 'saml.' and can only have alphanumeric characters,
        hyphens, underscores or periods. The part after 'saml.' must also start with a lowercase letter, end with an
        alphanumeric character, and have at least 2 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#name GoogleIdentityPlatformTenantInboundSamlConfig#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sp_config(self) -> "GoogleIdentityPlatformTenantInboundSamlConfigSpConfig":
        '''sp_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#sp_config GoogleIdentityPlatformTenantInboundSamlConfig#sp_config}
        '''
        result = self._values.get("sp_config")
        assert result is not None, "Required property 'sp_config' is missing"
        return typing.cast("GoogleIdentityPlatformTenantInboundSamlConfigSpConfig", result)

    @builtins.property
    def tenant(self) -> builtins.str:
        '''The name of the tenant where this inbound SAML config resource exists.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#tenant GoogleIdentityPlatformTenantInboundSamlConfig#tenant}
        '''
        result = self._values.get("tenant")
        assert result is not None, "Required property 'tenant' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If this config allows users to sign in with the provider.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#enabled GoogleIdentityPlatformTenantInboundSamlConfig#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#id GoogleIdentityPlatformTenantInboundSamlConfig#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#project GoogleIdentityPlatformTenantInboundSamlConfig#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["GoogleIdentityPlatformTenantInboundSamlConfigTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#timeouts GoogleIdentityPlatformTenantInboundSamlConfig#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleIdentityPlatformTenantInboundSamlConfigTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleIdentityPlatformTenantInboundSamlConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleIdentityPlatformTenantInboundSamlConfig.GoogleIdentityPlatformTenantInboundSamlConfigIdpConfig",
    jsii_struct_bases=[],
    name_mapping={
        "idp_certificates": "idpCertificates",
        "idp_entity_id": "idpEntityId",
        "sso_url": "ssoUrl",
        "sign_request": "signRequest",
    },
)
class GoogleIdentityPlatformTenantInboundSamlConfigIdpConfig:
    def __init__(
        self,
        *,
        idp_certificates: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificates", typing.Dict[str, typing.Any]]]],
        idp_entity_id: builtins.str,
        sso_url: builtins.str,
        sign_request: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param idp_certificates: idp_certificates block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#idp_certificates GoogleIdentityPlatformTenantInboundSamlConfig#idp_certificates}
        :param idp_entity_id: Unique identifier for all SAML entities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#idp_entity_id GoogleIdentityPlatformTenantInboundSamlConfig#idp_entity_id}
        :param sso_url: URL to send Authentication request to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#sso_url GoogleIdentityPlatformTenantInboundSamlConfig#sso_url}
        :param sign_request: Indicates if outbounding SAMLRequest should be signed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#sign_request GoogleIdentityPlatformTenantInboundSamlConfig#sign_request}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantInboundSamlConfigIdpConfig.__init__)
            check_type(argname="argument idp_certificates", value=idp_certificates, expected_type=type_hints["idp_certificates"])
            check_type(argname="argument idp_entity_id", value=idp_entity_id, expected_type=type_hints["idp_entity_id"])
            check_type(argname="argument sso_url", value=sso_url, expected_type=type_hints["sso_url"])
            check_type(argname="argument sign_request", value=sign_request, expected_type=type_hints["sign_request"])
        self._values: typing.Dict[str, typing.Any] = {
            "idp_certificates": idp_certificates,
            "idp_entity_id": idp_entity_id,
            "sso_url": sso_url,
        }
        if sign_request is not None:
            self._values["sign_request"] = sign_request

    @builtins.property
    def idp_certificates(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificates"]]:
        '''idp_certificates block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#idp_certificates GoogleIdentityPlatformTenantInboundSamlConfig#idp_certificates}
        '''
        result = self._values.get("idp_certificates")
        assert result is not None, "Required property 'idp_certificates' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificates"]], result)

    @builtins.property
    def idp_entity_id(self) -> builtins.str:
        '''Unique identifier for all SAML entities.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#idp_entity_id GoogleIdentityPlatformTenantInboundSamlConfig#idp_entity_id}
        '''
        result = self._values.get("idp_entity_id")
        assert result is not None, "Required property 'idp_entity_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sso_url(self) -> builtins.str:
        '''URL to send Authentication request to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#sso_url GoogleIdentityPlatformTenantInboundSamlConfig#sso_url}
        '''
        result = self._values.get("sso_url")
        assert result is not None, "Required property 'sso_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sign_request(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates if outbounding SAMLRequest should be signed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#sign_request GoogleIdentityPlatformTenantInboundSamlConfig#sign_request}
        '''
        result = self._values.get("sign_request")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleIdentityPlatformTenantInboundSamlConfigIdpConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleIdentityPlatformTenantInboundSamlConfig.GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificates",
    jsii_struct_bases=[],
    name_mapping={"x509_certificate": "x509Certificate"},
)
class GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificates:
    def __init__(
        self,
        *,
        x509_certificate: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param x509_certificate: The x509 certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#x509_certificate GoogleIdentityPlatformTenantInboundSamlConfig#x509_certificate}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificates.__init__)
            check_type(argname="argument x509_certificate", value=x509_certificate, expected_type=type_hints["x509_certificate"])
        self._values: typing.Dict[str, typing.Any] = {}
        if x509_certificate is not None:
            self._values["x509_certificate"] = x509_certificate

    @builtins.property
    def x509_certificate(self) -> typing.Optional[builtins.str]:
        '''The x509 certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#x509_certificate GoogleIdentityPlatformTenantInboundSamlConfig#x509_certificate}
        '''
        result = self._values.get("x509_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificates(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleIdentityPlatformTenantInboundSamlConfig.GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesList",
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
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificates]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificates]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificates]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleIdentityPlatformTenantInboundSamlConfig.GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetX509Certificate")
    def reset_x509_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetX509Certificate", []))

    @builtins.property
    @jsii.member(jsii_name="x509CertificateInput")
    def x509_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "x509CertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="x509Certificate")
    def x509_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "x509Certificate"))

    @x509_certificate.setter
    def x509_certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesOutputReference, "x509_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "x509Certificate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificates, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificates, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificates, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleIdentityPlatformTenantInboundSamlConfig.GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIdpCertificates")
    def put_idp_certificates(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificates, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigOutputReference.put_idp_certificates)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIdpCertificates", [value]))

    @jsii.member(jsii_name="resetSignRequest")
    def reset_sign_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignRequest", []))

    @builtins.property
    @jsii.member(jsii_name="idpCertificates")
    def idp_certificates(
        self,
    ) -> GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesList:
        return typing.cast(GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesList, jsii.get(self, "idpCertificates"))

    @builtins.property
    @jsii.member(jsii_name="idpCertificatesInput")
    def idp_certificates_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificates]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificates]]], jsii.get(self, "idpCertificatesInput"))

    @builtins.property
    @jsii.member(jsii_name="idpEntityIdInput")
    def idp_entity_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idpEntityIdInput"))

    @builtins.property
    @jsii.member(jsii_name="signRequestInput")
    def sign_request_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "signRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="ssoUrlInput")
    def sso_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ssoUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="idpEntityId")
    def idp_entity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idpEntityId"))

    @idp_entity_id.setter
    def idp_entity_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigOutputReference, "idp_entity_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idpEntityId", value)

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
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigOutputReference, "sign_request").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signRequest", value)

    @builtins.property
    @jsii.member(jsii_name="ssoUrl")
    def sso_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ssoUrl"))

    @sso_url.setter
    def sso_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigOutputReference, "sso_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ssoUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleIdentityPlatformTenantInboundSamlConfigIdpConfig]:
        return typing.cast(typing.Optional[GoogleIdentityPlatformTenantInboundSamlConfigIdpConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleIdentityPlatformTenantInboundSamlConfigIdpConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleIdentityPlatformTenantInboundSamlConfig.GoogleIdentityPlatformTenantInboundSamlConfigSpConfig",
    jsii_struct_bases=[],
    name_mapping={"callback_uri": "callbackUri", "sp_entity_id": "spEntityId"},
)
class GoogleIdentityPlatformTenantInboundSamlConfigSpConfig:
    def __init__(
        self,
        *,
        callback_uri: builtins.str,
        sp_entity_id: builtins.str,
    ) -> None:
        '''
        :param callback_uri: Callback URI where responses from IDP are handled. Must start with 'https://'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#callback_uri GoogleIdentityPlatformTenantInboundSamlConfig#callback_uri}
        :param sp_entity_id: Unique identifier for all SAML entities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#sp_entity_id GoogleIdentityPlatformTenantInboundSamlConfig#sp_entity_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantInboundSamlConfigSpConfig.__init__)
            check_type(argname="argument callback_uri", value=callback_uri, expected_type=type_hints["callback_uri"])
            check_type(argname="argument sp_entity_id", value=sp_entity_id, expected_type=type_hints["sp_entity_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "callback_uri": callback_uri,
            "sp_entity_id": sp_entity_id,
        }

    @builtins.property
    def callback_uri(self) -> builtins.str:
        '''Callback URI where responses from IDP are handled. Must start with 'https://'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#callback_uri GoogleIdentityPlatformTenantInboundSamlConfig#callback_uri}
        '''
        result = self._values.get("callback_uri")
        assert result is not None, "Required property 'callback_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sp_entity_id(self) -> builtins.str:
        '''Unique identifier for all SAML entities.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#sp_entity_id GoogleIdentityPlatformTenantInboundSamlConfig#sp_entity_id}
        '''
        result = self._values.get("sp_entity_id")
        assert result is not None, "Required property 'sp_entity_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleIdentityPlatformTenantInboundSamlConfigSpConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleIdentityPlatformTenantInboundSamlConfigSpConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleIdentityPlatformTenantInboundSamlConfig.GoogleIdentityPlatformTenantInboundSamlConfigSpConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantInboundSamlConfigSpConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="spCertificates")
    def sp_certificates(
        self,
    ) -> "GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificatesList":
        return typing.cast("GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificatesList", jsii.get(self, "spCertificates"))

    @builtins.property
    @jsii.member(jsii_name="callbackUriInput")
    def callback_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "callbackUriInput"))

    @builtins.property
    @jsii.member(jsii_name="spEntityIdInput")
    def sp_entity_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spEntityIdInput"))

    @builtins.property
    @jsii.member(jsii_name="callbackUri")
    def callback_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "callbackUri"))

    @callback_uri.setter
    def callback_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigSpConfigOutputReference, "callback_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "callbackUri", value)

    @builtins.property
    @jsii.member(jsii_name="spEntityId")
    def sp_entity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spEntityId"))

    @sp_entity_id.setter
    def sp_entity_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigSpConfigOutputReference, "sp_entity_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spEntityId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleIdentityPlatformTenantInboundSamlConfigSpConfig]:
        return typing.cast(typing.Optional[GoogleIdentityPlatformTenantInboundSamlConfigSpConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleIdentityPlatformTenantInboundSamlConfigSpConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigSpConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleIdentityPlatformTenantInboundSamlConfig.GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificates",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificates:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificates(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificatesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleIdentityPlatformTenantInboundSamlConfig.GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificatesList",
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
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificatesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificatesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificatesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificatesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificatesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificatesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificatesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificatesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleIdentityPlatformTenantInboundSamlConfig.GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificatesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificatesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="x509Certificate")
    def x509_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "x509Certificate"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificates]:
        return typing.cast(typing.Optional[GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificates], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificates],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificatesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleIdentityPlatformTenantInboundSamlConfig.GoogleIdentityPlatformTenantInboundSamlConfigTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleIdentityPlatformTenantInboundSamlConfigTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#create GoogleIdentityPlatformTenantInboundSamlConfig#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#delete GoogleIdentityPlatformTenantInboundSamlConfig#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#update GoogleIdentityPlatformTenantInboundSamlConfig#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantInboundSamlConfigTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#create GoogleIdentityPlatformTenantInboundSamlConfig#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#delete GoogleIdentityPlatformTenantInboundSamlConfig#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_identity_platform_tenant_inbound_saml_config#update GoogleIdentityPlatformTenantInboundSamlConfig#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleIdentityPlatformTenantInboundSamlConfigTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleIdentityPlatformTenantInboundSamlConfigTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleIdentityPlatformTenantInboundSamlConfig.GoogleIdentityPlatformTenantInboundSamlConfigTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleIdentityPlatformTenantInboundSamlConfigTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleIdentityPlatformTenantInboundSamlConfigTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleIdentityPlatformTenantInboundSamlConfigTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleIdentityPlatformTenantInboundSamlConfigTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIdentityPlatformTenantInboundSamlConfigTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleIdentityPlatformTenantInboundSamlConfig",
    "GoogleIdentityPlatformTenantInboundSamlConfigConfig",
    "GoogleIdentityPlatformTenantInboundSamlConfigIdpConfig",
    "GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificates",
    "GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesList",
    "GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigIdpCertificatesOutputReference",
    "GoogleIdentityPlatformTenantInboundSamlConfigIdpConfigOutputReference",
    "GoogleIdentityPlatformTenantInboundSamlConfigSpConfig",
    "GoogleIdentityPlatformTenantInboundSamlConfigSpConfigOutputReference",
    "GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificates",
    "GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificatesList",
    "GoogleIdentityPlatformTenantInboundSamlConfigSpConfigSpCertificatesOutputReference",
    "GoogleIdentityPlatformTenantInboundSamlConfigTimeouts",
    "GoogleIdentityPlatformTenantInboundSamlConfigTimeoutsOutputReference",
]

publication.publish()
