'''
# `vault_ssh_secret_backend_role`

Refer to the Terraform Registory for docs: [`vault_ssh_secret_backend_role`](https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role).
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


class SshSecretBackendRole(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.sshSecretBackendRole.SshSecretBackendRole",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role vault_ssh_secret_backend_role}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        backend: builtins.str,
        key_type: builtins.str,
        name: builtins.str,
        algorithm_signer: typing.Optional[builtins.str] = None,
        allow_bare_domains: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allowed_critical_options: typing.Optional[builtins.str] = None,
        allowed_domains: typing.Optional[builtins.str] = None,
        allowed_extensions: typing.Optional[builtins.str] = None,
        allowed_user_key_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SshSecretBackendRoleAllowedUserKeyConfig", typing.Dict[str, typing.Any]]]]] = None,
        allowed_user_key_lengths: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
        allowed_users: typing.Optional[builtins.str] = None,
        allowed_users_template: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_host_certificates: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_subdomains: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_user_certificates: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_user_key_ids: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cidr_list: typing.Optional[builtins.str] = None,
        default_critical_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        default_extensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        default_user: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        key_id_format: typing.Optional[builtins.str] = None,
        max_ttl: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role vault_ssh_secret_backend_role} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param backend: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#backend SshSecretBackendRole#backend}.
        :param key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#key_type SshSecretBackendRole#key_type}.
        :param name: Unique name for the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#name SshSecretBackendRole#name}
        :param algorithm_signer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#algorithm_signer SshSecretBackendRole#algorithm_signer}.
        :param allow_bare_domains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allow_bare_domains SshSecretBackendRole#allow_bare_domains}.
        :param allowed_critical_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_critical_options SshSecretBackendRole#allowed_critical_options}.
        :param allowed_domains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_domains SshSecretBackendRole#allowed_domains}.
        :param allowed_extensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_extensions SshSecretBackendRole#allowed_extensions}.
        :param allowed_user_key_config: allowed_user_key_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_user_key_config SshSecretBackendRole#allowed_user_key_config}
        :param allowed_user_key_lengths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_user_key_lengths SshSecretBackendRole#allowed_user_key_lengths}.
        :param allowed_users: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_users SshSecretBackendRole#allowed_users}.
        :param allowed_users_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_users_template SshSecretBackendRole#allowed_users_template}.
        :param allow_host_certificates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allow_host_certificates SshSecretBackendRole#allow_host_certificates}.
        :param allow_subdomains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allow_subdomains SshSecretBackendRole#allow_subdomains}.
        :param allow_user_certificates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allow_user_certificates SshSecretBackendRole#allow_user_certificates}.
        :param allow_user_key_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allow_user_key_ids SshSecretBackendRole#allow_user_key_ids}.
        :param cidr_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#cidr_list SshSecretBackendRole#cidr_list}.
        :param default_critical_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#default_critical_options SshSecretBackendRole#default_critical_options}.
        :param default_extensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#default_extensions SshSecretBackendRole#default_extensions}.
        :param default_user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#default_user SshSecretBackendRole#default_user}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#id SshSecretBackendRole#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param key_id_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#key_id_format SshSecretBackendRole#key_id_format}.
        :param max_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#max_ttl SshSecretBackendRole#max_ttl}.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#namespace SshSecretBackendRole#namespace}
        :param ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#ttl SshSecretBackendRole#ttl}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SshSecretBackendRole.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SshSecretBackendRoleConfig(
            backend=backend,
            key_type=key_type,
            name=name,
            algorithm_signer=algorithm_signer,
            allow_bare_domains=allow_bare_domains,
            allowed_critical_options=allowed_critical_options,
            allowed_domains=allowed_domains,
            allowed_extensions=allowed_extensions,
            allowed_user_key_config=allowed_user_key_config,
            allowed_user_key_lengths=allowed_user_key_lengths,
            allowed_users=allowed_users,
            allowed_users_template=allowed_users_template,
            allow_host_certificates=allow_host_certificates,
            allow_subdomains=allow_subdomains,
            allow_user_certificates=allow_user_certificates,
            allow_user_key_ids=allow_user_key_ids,
            cidr_list=cidr_list,
            default_critical_options=default_critical_options,
            default_extensions=default_extensions,
            default_user=default_user,
            id=id,
            key_id_format=key_id_format,
            max_ttl=max_ttl,
            namespace=namespace,
            ttl=ttl,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAllowedUserKeyConfig")
    def put_allowed_user_key_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SshSecretBackendRoleAllowedUserKeyConfig", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SshSecretBackendRole.put_allowed_user_key_config)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAllowedUserKeyConfig", [value]))

    @jsii.member(jsii_name="resetAlgorithmSigner")
    def reset_algorithm_signer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlgorithmSigner", []))

    @jsii.member(jsii_name="resetAllowBareDomains")
    def reset_allow_bare_domains(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowBareDomains", []))

    @jsii.member(jsii_name="resetAllowedCriticalOptions")
    def reset_allowed_critical_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedCriticalOptions", []))

    @jsii.member(jsii_name="resetAllowedDomains")
    def reset_allowed_domains(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedDomains", []))

    @jsii.member(jsii_name="resetAllowedExtensions")
    def reset_allowed_extensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedExtensions", []))

    @jsii.member(jsii_name="resetAllowedUserKeyConfig")
    def reset_allowed_user_key_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedUserKeyConfig", []))

    @jsii.member(jsii_name="resetAllowedUserKeyLengths")
    def reset_allowed_user_key_lengths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedUserKeyLengths", []))

    @jsii.member(jsii_name="resetAllowedUsers")
    def reset_allowed_users(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedUsers", []))

    @jsii.member(jsii_name="resetAllowedUsersTemplate")
    def reset_allowed_users_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedUsersTemplate", []))

    @jsii.member(jsii_name="resetAllowHostCertificates")
    def reset_allow_host_certificates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowHostCertificates", []))

    @jsii.member(jsii_name="resetAllowSubdomains")
    def reset_allow_subdomains(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowSubdomains", []))

    @jsii.member(jsii_name="resetAllowUserCertificates")
    def reset_allow_user_certificates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowUserCertificates", []))

    @jsii.member(jsii_name="resetAllowUserKeyIds")
    def reset_allow_user_key_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowUserKeyIds", []))

    @jsii.member(jsii_name="resetCidrList")
    def reset_cidr_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCidrList", []))

    @jsii.member(jsii_name="resetDefaultCriticalOptions")
    def reset_default_critical_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultCriticalOptions", []))

    @jsii.member(jsii_name="resetDefaultExtensions")
    def reset_default_extensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultExtensions", []))

    @jsii.member(jsii_name="resetDefaultUser")
    def reset_default_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultUser", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKeyIdFormat")
    def reset_key_id_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyIdFormat", []))

    @jsii.member(jsii_name="resetMaxTtl")
    def reset_max_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTtl", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="allowedUserKeyConfig")
    def allowed_user_key_config(self) -> "SshSecretBackendRoleAllowedUserKeyConfigList":
        return typing.cast("SshSecretBackendRoleAllowedUserKeyConfigList", jsii.get(self, "allowedUserKeyConfig"))

    @builtins.property
    @jsii.member(jsii_name="algorithmSignerInput")
    def algorithm_signer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "algorithmSignerInput"))

    @builtins.property
    @jsii.member(jsii_name="allowBareDomainsInput")
    def allow_bare_domains_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowBareDomainsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedCriticalOptionsInput")
    def allowed_critical_options_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allowedCriticalOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedDomainsInput")
    def allowed_domains_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allowedDomainsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedExtensionsInput")
    def allowed_extensions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allowedExtensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedUserKeyConfigInput")
    def allowed_user_key_config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SshSecretBackendRoleAllowedUserKeyConfig"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SshSecretBackendRoleAllowedUserKeyConfig"]]], jsii.get(self, "allowedUserKeyConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedUserKeyLengthsInput")
    def allowed_user_key_lengths_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], jsii.get(self, "allowedUserKeyLengthsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedUsersInput")
    def allowed_users_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allowedUsersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedUsersTemplateInput")
    def allowed_users_template_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowedUsersTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="allowHostCertificatesInput")
    def allow_host_certificates_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowHostCertificatesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowSubdomainsInput")
    def allow_subdomains_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowSubdomainsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowUserCertificatesInput")
    def allow_user_certificates_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowUserCertificatesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowUserKeyIdsInput")
    def allow_user_key_ids_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowUserKeyIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="cidrListInput")
    def cidr_list_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cidrListInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultCriticalOptionsInput")
    def default_critical_options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "defaultCriticalOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultExtensionsInput")
    def default_extensions_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "defaultExtensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultUserInput")
    def default_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultUserInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="keyIdFormatInput")
    def key_id_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyIdFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="keyTypeInput")
    def key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTtlInput")
    def max_ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="algorithmSigner")
    def algorithm_signer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "algorithmSigner"))

    @algorithm_signer.setter
    def algorithm_signer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "algorithm_signer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "algorithmSigner", value)

    @builtins.property
    @jsii.member(jsii_name="allowBareDomains")
    def allow_bare_domains(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowBareDomains"))

    @allow_bare_domains.setter
    def allow_bare_domains(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "allow_bare_domains").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowBareDomains", value)

    @builtins.property
    @jsii.member(jsii_name="allowedCriticalOptions")
    def allowed_critical_options(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allowedCriticalOptions"))

    @allowed_critical_options.setter
    def allowed_critical_options(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "allowed_critical_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedCriticalOptions", value)

    @builtins.property
    @jsii.member(jsii_name="allowedDomains")
    def allowed_domains(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allowedDomains"))

    @allowed_domains.setter
    def allowed_domains(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "allowed_domains").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedDomains", value)

    @builtins.property
    @jsii.member(jsii_name="allowedExtensions")
    def allowed_extensions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allowedExtensions"))

    @allowed_extensions.setter
    def allowed_extensions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "allowed_extensions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedExtensions", value)

    @builtins.property
    @jsii.member(jsii_name="allowedUserKeyLengths")
    def allowed_user_key_lengths(self) -> typing.Mapping[builtins.str, jsii.Number]:
        return typing.cast(typing.Mapping[builtins.str, jsii.Number], jsii.get(self, "allowedUserKeyLengths"))

    @allowed_user_key_lengths.setter
    def allowed_user_key_lengths(
        self,
        value: typing.Mapping[builtins.str, jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "allowed_user_key_lengths").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedUserKeyLengths", value)

    @builtins.property
    @jsii.member(jsii_name="allowedUsers")
    def allowed_users(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allowedUsers"))

    @allowed_users.setter
    def allowed_users(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "allowed_users").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedUsers", value)

    @builtins.property
    @jsii.member(jsii_name="allowedUsersTemplate")
    def allowed_users_template(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowedUsersTemplate"))

    @allowed_users_template.setter
    def allowed_users_template(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "allowed_users_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedUsersTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="allowHostCertificates")
    def allow_host_certificates(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowHostCertificates"))

    @allow_host_certificates.setter
    def allow_host_certificates(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "allow_host_certificates").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowHostCertificates", value)

    @builtins.property
    @jsii.member(jsii_name="allowSubdomains")
    def allow_subdomains(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowSubdomains"))

    @allow_subdomains.setter
    def allow_subdomains(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "allow_subdomains").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowSubdomains", value)

    @builtins.property
    @jsii.member(jsii_name="allowUserCertificates")
    def allow_user_certificates(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowUserCertificates"))

    @allow_user_certificates.setter
    def allow_user_certificates(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "allow_user_certificates").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowUserCertificates", value)

    @builtins.property
    @jsii.member(jsii_name="allowUserKeyIds")
    def allow_user_key_ids(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowUserKeyIds"))

    @allow_user_key_ids.setter
    def allow_user_key_ids(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "allow_user_key_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowUserKeyIds", value)

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backend"))

    @backend.setter
    def backend(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "backend").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backend", value)

    @builtins.property
    @jsii.member(jsii_name="cidrList")
    def cidr_list(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cidrList"))

    @cidr_list.setter
    def cidr_list(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "cidr_list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidrList", value)

    @builtins.property
    @jsii.member(jsii_name="defaultCriticalOptions")
    def default_critical_options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "defaultCriticalOptions"))

    @default_critical_options.setter
    def default_critical_options(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "default_critical_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultCriticalOptions", value)

    @builtins.property
    @jsii.member(jsii_name="defaultExtensions")
    def default_extensions(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "defaultExtensions"))

    @default_extensions.setter
    def default_extensions(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "default_extensions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultExtensions", value)

    @builtins.property
    @jsii.member(jsii_name="defaultUser")
    def default_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultUser"))

    @default_user.setter
    def default_user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "default_user").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultUser", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="keyIdFormat")
    def key_id_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyIdFormat"))

    @key_id_format.setter
    def key_id_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "key_id_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyIdFormat", value)

    @builtins.property
    @jsii.member(jsii_name="keyType")
    def key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyType"))

    @key_type.setter
    def key_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "key_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyType", value)

    @builtins.property
    @jsii.member(jsii_name="maxTtl")
    def max_ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxTtl"))

    @max_ttl.setter
    def max_ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "max_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTtl", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRole, "ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.sshSecretBackendRole.SshSecretBackendRoleAllowedUserKeyConfig",
    jsii_struct_bases=[],
    name_mapping={"lengths": "lengths", "type": "type"},
)
class SshSecretBackendRoleAllowedUserKeyConfig:
    def __init__(
        self,
        *,
        lengths: typing.Sequence[jsii.Number],
        type: builtins.str,
    ) -> None:
        '''
        :param lengths: List of allowed key lengths, vault-1.10 and above. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#lengths SshSecretBackendRole#lengths}
        :param type: Key type, choices: rsa, ecdsa, ec, dsa, ed25519, ssh-rsa, ssh-dss, ssh-ed25519, ecdsa-sha2-nistp256, ecdsa-sha2-nistp384, ecdsa-sha2-nistp521. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#type SshSecretBackendRole#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SshSecretBackendRoleAllowedUserKeyConfig.__init__)
            check_type(argname="argument lengths", value=lengths, expected_type=type_hints["lengths"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "lengths": lengths,
            "type": type,
        }

    @builtins.property
    def lengths(self) -> typing.List[jsii.Number]:
        '''List of allowed key lengths, vault-1.10 and above.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#lengths SshSecretBackendRole#lengths}
        '''
        result = self._values.get("lengths")
        assert result is not None, "Required property 'lengths' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Key type, choices: rsa, ecdsa, ec, dsa, ed25519, ssh-rsa, ssh-dss, ssh-ed25519, ecdsa-sha2-nistp256, ecdsa-sha2-nistp384, ecdsa-sha2-nistp521.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#type SshSecretBackendRole#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SshSecretBackendRoleAllowedUserKeyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SshSecretBackendRoleAllowedUserKeyConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.sshSecretBackendRole.SshSecretBackendRoleAllowedUserKeyConfigList",
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
            type_hints = typing.get_type_hints(SshSecretBackendRoleAllowedUserKeyConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SshSecretBackendRoleAllowedUserKeyConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SshSecretBackendRoleAllowedUserKeyConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SshSecretBackendRoleAllowedUserKeyConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRoleAllowedUserKeyConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRoleAllowedUserKeyConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRoleAllowedUserKeyConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SshSecretBackendRoleAllowedUserKeyConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SshSecretBackendRoleAllowedUserKeyConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SshSecretBackendRoleAllowedUserKeyConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRoleAllowedUserKeyConfigList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SshSecretBackendRoleAllowedUserKeyConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.sshSecretBackendRole.SshSecretBackendRoleAllowedUserKeyConfigOutputReference",
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
            type_hints = typing.get_type_hints(SshSecretBackendRoleAllowedUserKeyConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="lengthsInput")
    def lengths_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "lengthsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="lengths")
    def lengths(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "lengths"))

    @lengths.setter
    def lengths(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRoleAllowedUserKeyConfigOutputReference, "lengths").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lengths", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRoleAllowedUserKeyConfigOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SshSecretBackendRoleAllowedUserKeyConfig, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SshSecretBackendRoleAllowedUserKeyConfig, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SshSecretBackendRoleAllowedUserKeyConfig, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SshSecretBackendRoleAllowedUserKeyConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.sshSecretBackendRole.SshSecretBackendRoleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "backend": "backend",
        "key_type": "keyType",
        "name": "name",
        "algorithm_signer": "algorithmSigner",
        "allow_bare_domains": "allowBareDomains",
        "allowed_critical_options": "allowedCriticalOptions",
        "allowed_domains": "allowedDomains",
        "allowed_extensions": "allowedExtensions",
        "allowed_user_key_config": "allowedUserKeyConfig",
        "allowed_user_key_lengths": "allowedUserKeyLengths",
        "allowed_users": "allowedUsers",
        "allowed_users_template": "allowedUsersTemplate",
        "allow_host_certificates": "allowHostCertificates",
        "allow_subdomains": "allowSubdomains",
        "allow_user_certificates": "allowUserCertificates",
        "allow_user_key_ids": "allowUserKeyIds",
        "cidr_list": "cidrList",
        "default_critical_options": "defaultCriticalOptions",
        "default_extensions": "defaultExtensions",
        "default_user": "defaultUser",
        "id": "id",
        "key_id_format": "keyIdFormat",
        "max_ttl": "maxTtl",
        "namespace": "namespace",
        "ttl": "ttl",
    },
)
class SshSecretBackendRoleConfig(cdktf.TerraformMetaArguments):
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
        backend: builtins.str,
        key_type: builtins.str,
        name: builtins.str,
        algorithm_signer: typing.Optional[builtins.str] = None,
        allow_bare_domains: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allowed_critical_options: typing.Optional[builtins.str] = None,
        allowed_domains: typing.Optional[builtins.str] = None,
        allowed_extensions: typing.Optional[builtins.str] = None,
        allowed_user_key_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SshSecretBackendRoleAllowedUserKeyConfig, typing.Dict[str, typing.Any]]]]] = None,
        allowed_user_key_lengths: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
        allowed_users: typing.Optional[builtins.str] = None,
        allowed_users_template: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_host_certificates: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_subdomains: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_user_certificates: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_user_key_ids: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cidr_list: typing.Optional[builtins.str] = None,
        default_critical_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        default_extensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        default_user: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        key_id_format: typing.Optional[builtins.str] = None,
        max_ttl: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param backend: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#backend SshSecretBackendRole#backend}.
        :param key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#key_type SshSecretBackendRole#key_type}.
        :param name: Unique name for the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#name SshSecretBackendRole#name}
        :param algorithm_signer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#algorithm_signer SshSecretBackendRole#algorithm_signer}.
        :param allow_bare_domains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allow_bare_domains SshSecretBackendRole#allow_bare_domains}.
        :param allowed_critical_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_critical_options SshSecretBackendRole#allowed_critical_options}.
        :param allowed_domains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_domains SshSecretBackendRole#allowed_domains}.
        :param allowed_extensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_extensions SshSecretBackendRole#allowed_extensions}.
        :param allowed_user_key_config: allowed_user_key_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_user_key_config SshSecretBackendRole#allowed_user_key_config}
        :param allowed_user_key_lengths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_user_key_lengths SshSecretBackendRole#allowed_user_key_lengths}.
        :param allowed_users: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_users SshSecretBackendRole#allowed_users}.
        :param allowed_users_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_users_template SshSecretBackendRole#allowed_users_template}.
        :param allow_host_certificates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allow_host_certificates SshSecretBackendRole#allow_host_certificates}.
        :param allow_subdomains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allow_subdomains SshSecretBackendRole#allow_subdomains}.
        :param allow_user_certificates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allow_user_certificates SshSecretBackendRole#allow_user_certificates}.
        :param allow_user_key_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allow_user_key_ids SshSecretBackendRole#allow_user_key_ids}.
        :param cidr_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#cidr_list SshSecretBackendRole#cidr_list}.
        :param default_critical_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#default_critical_options SshSecretBackendRole#default_critical_options}.
        :param default_extensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#default_extensions SshSecretBackendRole#default_extensions}.
        :param default_user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#default_user SshSecretBackendRole#default_user}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#id SshSecretBackendRole#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param key_id_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#key_id_format SshSecretBackendRole#key_id_format}.
        :param max_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#max_ttl SshSecretBackendRole#max_ttl}.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#namespace SshSecretBackendRole#namespace}
        :param ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#ttl SshSecretBackendRole#ttl}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(SshSecretBackendRoleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument algorithm_signer", value=algorithm_signer, expected_type=type_hints["algorithm_signer"])
            check_type(argname="argument allow_bare_domains", value=allow_bare_domains, expected_type=type_hints["allow_bare_domains"])
            check_type(argname="argument allowed_critical_options", value=allowed_critical_options, expected_type=type_hints["allowed_critical_options"])
            check_type(argname="argument allowed_domains", value=allowed_domains, expected_type=type_hints["allowed_domains"])
            check_type(argname="argument allowed_extensions", value=allowed_extensions, expected_type=type_hints["allowed_extensions"])
            check_type(argname="argument allowed_user_key_config", value=allowed_user_key_config, expected_type=type_hints["allowed_user_key_config"])
            check_type(argname="argument allowed_user_key_lengths", value=allowed_user_key_lengths, expected_type=type_hints["allowed_user_key_lengths"])
            check_type(argname="argument allowed_users", value=allowed_users, expected_type=type_hints["allowed_users"])
            check_type(argname="argument allowed_users_template", value=allowed_users_template, expected_type=type_hints["allowed_users_template"])
            check_type(argname="argument allow_host_certificates", value=allow_host_certificates, expected_type=type_hints["allow_host_certificates"])
            check_type(argname="argument allow_subdomains", value=allow_subdomains, expected_type=type_hints["allow_subdomains"])
            check_type(argname="argument allow_user_certificates", value=allow_user_certificates, expected_type=type_hints["allow_user_certificates"])
            check_type(argname="argument allow_user_key_ids", value=allow_user_key_ids, expected_type=type_hints["allow_user_key_ids"])
            check_type(argname="argument cidr_list", value=cidr_list, expected_type=type_hints["cidr_list"])
            check_type(argname="argument default_critical_options", value=default_critical_options, expected_type=type_hints["default_critical_options"])
            check_type(argname="argument default_extensions", value=default_extensions, expected_type=type_hints["default_extensions"])
            check_type(argname="argument default_user", value=default_user, expected_type=type_hints["default_user"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument key_id_format", value=key_id_format, expected_type=type_hints["key_id_format"])
            check_type(argname="argument max_ttl", value=max_ttl, expected_type=type_hints["max_ttl"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend": backend,
            "key_type": key_type,
            "name": name,
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
        if algorithm_signer is not None:
            self._values["algorithm_signer"] = algorithm_signer
        if allow_bare_domains is not None:
            self._values["allow_bare_domains"] = allow_bare_domains
        if allowed_critical_options is not None:
            self._values["allowed_critical_options"] = allowed_critical_options
        if allowed_domains is not None:
            self._values["allowed_domains"] = allowed_domains
        if allowed_extensions is not None:
            self._values["allowed_extensions"] = allowed_extensions
        if allowed_user_key_config is not None:
            self._values["allowed_user_key_config"] = allowed_user_key_config
        if allowed_user_key_lengths is not None:
            self._values["allowed_user_key_lengths"] = allowed_user_key_lengths
        if allowed_users is not None:
            self._values["allowed_users"] = allowed_users
        if allowed_users_template is not None:
            self._values["allowed_users_template"] = allowed_users_template
        if allow_host_certificates is not None:
            self._values["allow_host_certificates"] = allow_host_certificates
        if allow_subdomains is not None:
            self._values["allow_subdomains"] = allow_subdomains
        if allow_user_certificates is not None:
            self._values["allow_user_certificates"] = allow_user_certificates
        if allow_user_key_ids is not None:
            self._values["allow_user_key_ids"] = allow_user_key_ids
        if cidr_list is not None:
            self._values["cidr_list"] = cidr_list
        if default_critical_options is not None:
            self._values["default_critical_options"] = default_critical_options
        if default_extensions is not None:
            self._values["default_extensions"] = default_extensions
        if default_user is not None:
            self._values["default_user"] = default_user
        if id is not None:
            self._values["id"] = id
        if key_id_format is not None:
            self._values["key_id_format"] = key_id_format
        if max_ttl is not None:
            self._values["max_ttl"] = max_ttl
        if namespace is not None:
            self._values["namespace"] = namespace
        if ttl is not None:
            self._values["ttl"] = ttl

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
    def backend(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#backend SshSecretBackendRole#backend}.'''
        result = self._values.get("backend")
        assert result is not None, "Required property 'backend' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#key_type SshSecretBackendRole#key_type}.'''
        result = self._values.get("key_type")
        assert result is not None, "Required property 'key_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Unique name for the role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#name SshSecretBackendRole#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def algorithm_signer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#algorithm_signer SshSecretBackendRole#algorithm_signer}.'''
        result = self._values.get("algorithm_signer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def allow_bare_domains(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allow_bare_domains SshSecretBackendRole#allow_bare_domains}.'''
        result = self._values.get("allow_bare_domains")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allowed_critical_options(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_critical_options SshSecretBackendRole#allowed_critical_options}.'''
        result = self._values.get("allowed_critical_options")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def allowed_domains(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_domains SshSecretBackendRole#allowed_domains}.'''
        result = self._values.get("allowed_domains")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def allowed_extensions(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_extensions SshSecretBackendRole#allowed_extensions}.'''
        result = self._values.get("allowed_extensions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def allowed_user_key_config(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SshSecretBackendRoleAllowedUserKeyConfig]]]:
        '''allowed_user_key_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_user_key_config SshSecretBackendRole#allowed_user_key_config}
        '''
        result = self._values.get("allowed_user_key_config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SshSecretBackendRoleAllowedUserKeyConfig]]], result)

    @builtins.property
    def allowed_user_key_lengths(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_user_key_lengths SshSecretBackendRole#allowed_user_key_lengths}.'''
        result = self._values.get("allowed_user_key_lengths")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], result)

    @builtins.property
    def allowed_users(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_users SshSecretBackendRole#allowed_users}.'''
        result = self._values.get("allowed_users")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def allowed_users_template(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allowed_users_template SshSecretBackendRole#allowed_users_template}.'''
        result = self._values.get("allowed_users_template")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_host_certificates(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allow_host_certificates SshSecretBackendRole#allow_host_certificates}.'''
        result = self._values.get("allow_host_certificates")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_subdomains(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allow_subdomains SshSecretBackendRole#allow_subdomains}.'''
        result = self._values.get("allow_subdomains")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_user_certificates(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allow_user_certificates SshSecretBackendRole#allow_user_certificates}.'''
        result = self._values.get("allow_user_certificates")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_user_key_ids(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#allow_user_key_ids SshSecretBackendRole#allow_user_key_ids}.'''
        result = self._values.get("allow_user_key_ids")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cidr_list(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#cidr_list SshSecretBackendRole#cidr_list}.'''
        result = self._values.get("cidr_list")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_critical_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#default_critical_options SshSecretBackendRole#default_critical_options}.'''
        result = self._values.get("default_critical_options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def default_extensions(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#default_extensions SshSecretBackendRole#default_extensions}.'''
        result = self._values.get("default_extensions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def default_user(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#default_user SshSecretBackendRole#default_user}.'''
        result = self._values.get("default_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#id SshSecretBackendRole#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_id_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#key_id_format SshSecretBackendRole#key_id_format}.'''
        result = self._values.get("key_id_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_ttl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#max_ttl SshSecretBackendRole#max_ttl}.'''
        result = self._values.get("max_ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#namespace SshSecretBackendRole#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role#ttl SshSecretBackendRole#ttl}.'''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SshSecretBackendRoleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SshSecretBackendRole",
    "SshSecretBackendRoleAllowedUserKeyConfig",
    "SshSecretBackendRoleAllowedUserKeyConfigList",
    "SshSecretBackendRoleAllowedUserKeyConfigOutputReference",
    "SshSecretBackendRoleConfig",
]

publication.publish()
