'''
# `vault_ad_secret_backend`

Refer to the Terraform Registory for docs: [`vault_ad_secret_backend`](https://www.terraform.io/docs/providers/vault/r/ad_secret_backend).
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


class AdSecretBackend(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.adSecretBackend.AdSecretBackend",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend vault_ad_secret_backend}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        binddn: builtins.str,
        bindpass: builtins.str,
        anonymous_group_search: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        backend: typing.Optional[builtins.str] = None,
        case_sensitive_names: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        certificate: typing.Optional[builtins.str] = None,
        client_tls_cert: typing.Optional[builtins.str] = None,
        client_tls_key: typing.Optional[builtins.str] = None,
        default_lease_ttl_seconds: typing.Optional[jsii.Number] = None,
        deny_null_bind: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        disable_remount: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        discoverdn: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        formatter: typing.Optional[builtins.str] = None,
        groupattr: typing.Optional[builtins.str] = None,
        groupdn: typing.Optional[builtins.str] = None,
        groupfilter: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        insecure_tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        last_rotation_tolerance: typing.Optional[jsii.Number] = None,
        length: typing.Optional[jsii.Number] = None,
        local: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_lease_ttl_seconds: typing.Optional[jsii.Number] = None,
        max_ttl: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        password_policy: typing.Optional[builtins.str] = None,
        request_timeout: typing.Optional[jsii.Number] = None,
        starttls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_max_version: typing.Optional[builtins.str] = None,
        tls_min_version: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[jsii.Number] = None,
        upndomain: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
        use_pre111_group_cn_behavior: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        userattr: typing.Optional[builtins.str] = None,
        userdn: typing.Optional[builtins.str] = None,
        use_token_groups: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend vault_ad_secret_backend} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param binddn: Distinguished name of object to bind when performing user and group search. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#binddn AdSecretBackend#binddn}
        :param bindpass: LDAP password for searching for the user DN. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#bindpass AdSecretBackend#bindpass}
        :param anonymous_group_search: Use anonymous binds when performing LDAP group searches (if true the initial credentials will still be used for the initial connection test). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#anonymous_group_search AdSecretBackend#anonymous_group_search}
        :param backend: The mount path for a backend, for example, the path given in "$ vault auth enable -path=my-ad ad". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#backend AdSecretBackend#backend}
        :param case_sensitive_names: If true, case sensitivity will be used when comparing usernames and groups for matching policies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#case_sensitive_names AdSecretBackend#case_sensitive_names}
        :param certificate: CA certificate to use when verifying LDAP server certificate, must be x509 PEM encoded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#certificate AdSecretBackend#certificate}
        :param client_tls_cert: Client certificate to provide to the LDAP server, must be x509 PEM encoded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#client_tls_cert AdSecretBackend#client_tls_cert}
        :param client_tls_key: Client certificate key to provide to the LDAP server, must be x509 PEM encoded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#client_tls_key AdSecretBackend#client_tls_key}
        :param default_lease_ttl_seconds: Default lease duration for secrets in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#default_lease_ttl_seconds AdSecretBackend#default_lease_ttl_seconds}
        :param deny_null_bind: Denies an unauthenticated LDAP bind request if the user's password is empty; defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#deny_null_bind AdSecretBackend#deny_null_bind}
        :param description: Human-friendly description of the mount for the backend. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#description AdSecretBackend#description}
        :param disable_remount: If set, opts out of mount migration on path updates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#disable_remount AdSecretBackend#disable_remount}
        :param discoverdn: Use anonymous bind to discover the bind DN of a user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#discoverdn AdSecretBackend#discoverdn}
        :param formatter: Text to insert the password into, ex. "customPrefix{{PASSWORD}}customSuffix". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#formatter AdSecretBackend#formatter}
        :param groupattr: LDAP attribute to follow on objects returned by in order to enumerate user group membership. Examples: "cn" or "memberOf", etc. Default: cn Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#groupattr AdSecretBackend#groupattr}
        :param groupdn: LDAP search base to use for group membership search (eg: ou=Groups,dc=example,dc=org). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#groupdn AdSecretBackend#groupdn}
        :param groupfilter: Go template for querying group membership of user. The template can access the following context variables: UserDN, Username Example: (&(objectClass=group)(member:1.2.840.113556.1.4.1941:={{.UserDN}})) Default: (|(memberUid={{.Username}})(member={{.UserDN}})(uniqueMember={{.UserDN}})) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#groupfilter AdSecretBackend#groupfilter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#id AdSecretBackend#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param insecure_tls: Skip LDAP server SSL Certificate verification - insecure and not recommended for production use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#insecure_tls AdSecretBackend#insecure_tls}
        :param last_rotation_tolerance: The number of seconds after a Vault rotation where, if Active Directory shows a later rotation, it should be considered out-of-band. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#last_rotation_tolerance AdSecretBackend#last_rotation_tolerance}
        :param length: The desired length of passwords that Vault generates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#length AdSecretBackend#length}
        :param local: Mark the secrets engine as local-only. Local engines are not replicated or removed by replication.Tolerance duration to use when checking the last rotation time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#local AdSecretBackend#local}
        :param max_lease_ttl_seconds: Maximum possible lease duration for secrets in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#max_lease_ttl_seconds AdSecretBackend#max_lease_ttl_seconds}
        :param max_ttl: In seconds, the maximum password time-to-live. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#max_ttl AdSecretBackend#max_ttl}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#namespace AdSecretBackend#namespace}
        :param password_policy: Name of the password policy to use to generate passwords. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#password_policy AdSecretBackend#password_policy}
        :param request_timeout: Timeout, in seconds, for the connection when making requests against the server before returning back an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#request_timeout AdSecretBackend#request_timeout}
        :param starttls: Issue a StartTLS command after establishing unencrypted connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#starttls AdSecretBackend#starttls}
        :param tls_max_version: Maximum TLS version to use. Accepted values are 'tls10', 'tls11', 'tls12' or 'tls13'. Defaults to 'tls12'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#tls_max_version AdSecretBackend#tls_max_version}
        :param tls_min_version: Minimum TLS version to use. Accepted values are 'tls10', 'tls11', 'tls12' or 'tls13'. Defaults to 'tls12'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#tls_min_version AdSecretBackend#tls_min_version}
        :param ttl: In seconds, the default password time-to-live. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#ttl AdSecretBackend#ttl}
        :param upndomain: Enables userPrincipalDomain login with [username]@UPNDomain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#upndomain AdSecretBackend#upndomain}
        :param url: LDAP URL to connect to (default: ldap://127.0.0.1). Multiple URLs can be specified by concatenating them with commas; they will be tried in-order. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#url AdSecretBackend#url}
        :param use_pre111_group_cn_behavior: In Vault 1.1.1 a fix for handling group CN values of different cases unfortunately introduced a regression that could cause previously defined groups to not be found due to a change in the resulting name. If set true, the pre-1.1.1 behavior for matching group CNs will be used. This is only needed in some upgrade scenarios for backwards compatibility. It is enabled by default if the config is upgraded but disabled by default on new configurations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#use_pre111_group_cn_behavior AdSecretBackend#use_pre111_group_cn_behavior}
        :param userattr: Attribute used for users (default: cn). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#userattr AdSecretBackend#userattr}
        :param userdn: LDAP domain to use for users (eg: ou=People,dc=example,dc=org). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#userdn AdSecretBackend#userdn}
        :param use_token_groups: If true, use the Active Directory tokenGroups constructed attribute of the user to find the group memberships. This will find all security groups including nested ones. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#use_token_groups AdSecretBackend#use_token_groups}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AdSecretBackend.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AdSecretBackendConfig(
            binddn=binddn,
            bindpass=bindpass,
            anonymous_group_search=anonymous_group_search,
            backend=backend,
            case_sensitive_names=case_sensitive_names,
            certificate=certificate,
            client_tls_cert=client_tls_cert,
            client_tls_key=client_tls_key,
            default_lease_ttl_seconds=default_lease_ttl_seconds,
            deny_null_bind=deny_null_bind,
            description=description,
            disable_remount=disable_remount,
            discoverdn=discoverdn,
            formatter=formatter,
            groupattr=groupattr,
            groupdn=groupdn,
            groupfilter=groupfilter,
            id=id,
            insecure_tls=insecure_tls,
            last_rotation_tolerance=last_rotation_tolerance,
            length=length,
            local=local,
            max_lease_ttl_seconds=max_lease_ttl_seconds,
            max_ttl=max_ttl,
            namespace=namespace,
            password_policy=password_policy,
            request_timeout=request_timeout,
            starttls=starttls,
            tls_max_version=tls_max_version,
            tls_min_version=tls_min_version,
            ttl=ttl,
            upndomain=upndomain,
            url=url,
            use_pre111_group_cn_behavior=use_pre111_group_cn_behavior,
            userattr=userattr,
            userdn=userdn,
            use_token_groups=use_token_groups,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAnonymousGroupSearch")
    def reset_anonymous_group_search(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnonymousGroupSearch", []))

    @jsii.member(jsii_name="resetBackend")
    def reset_backend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackend", []))

    @jsii.member(jsii_name="resetCaseSensitiveNames")
    def reset_case_sensitive_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaseSensitiveNames", []))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetClientTlsCert")
    def reset_client_tls_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientTlsCert", []))

    @jsii.member(jsii_name="resetClientTlsKey")
    def reset_client_tls_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientTlsKey", []))

    @jsii.member(jsii_name="resetDefaultLeaseTtlSeconds")
    def reset_default_lease_ttl_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultLeaseTtlSeconds", []))

    @jsii.member(jsii_name="resetDenyNullBind")
    def reset_deny_null_bind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDenyNullBind", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisableRemount")
    def reset_disable_remount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableRemount", []))

    @jsii.member(jsii_name="resetDiscoverdn")
    def reset_discoverdn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiscoverdn", []))

    @jsii.member(jsii_name="resetFormatter")
    def reset_formatter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFormatter", []))

    @jsii.member(jsii_name="resetGroupattr")
    def reset_groupattr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupattr", []))

    @jsii.member(jsii_name="resetGroupdn")
    def reset_groupdn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupdn", []))

    @jsii.member(jsii_name="resetGroupfilter")
    def reset_groupfilter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupfilter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInsecureTls")
    def reset_insecure_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureTls", []))

    @jsii.member(jsii_name="resetLastRotationTolerance")
    def reset_last_rotation_tolerance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastRotationTolerance", []))

    @jsii.member(jsii_name="resetLength")
    def reset_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLength", []))

    @jsii.member(jsii_name="resetLocal")
    def reset_local(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocal", []))

    @jsii.member(jsii_name="resetMaxLeaseTtlSeconds")
    def reset_max_lease_ttl_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxLeaseTtlSeconds", []))

    @jsii.member(jsii_name="resetMaxTtl")
    def reset_max_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTtl", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetPasswordPolicy")
    def reset_password_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordPolicy", []))

    @jsii.member(jsii_name="resetRequestTimeout")
    def reset_request_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestTimeout", []))

    @jsii.member(jsii_name="resetStarttls")
    def reset_starttls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStarttls", []))

    @jsii.member(jsii_name="resetTlsMaxVersion")
    def reset_tls_max_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsMaxVersion", []))

    @jsii.member(jsii_name="resetTlsMinVersion")
    def reset_tls_min_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsMinVersion", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @jsii.member(jsii_name="resetUpndomain")
    def reset_upndomain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpndomain", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @jsii.member(jsii_name="resetUsePre111GroupCnBehavior")
    def reset_use_pre111_group_cn_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsePre111GroupCnBehavior", []))

    @jsii.member(jsii_name="resetUserattr")
    def reset_userattr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserattr", []))

    @jsii.member(jsii_name="resetUserdn")
    def reset_userdn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserdn", []))

    @jsii.member(jsii_name="resetUseTokenGroups")
    def reset_use_token_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseTokenGroups", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="anonymousGroupSearchInput")
    def anonymous_group_search_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "anonymousGroupSearchInput"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="binddnInput")
    def binddn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "binddnInput"))

    @builtins.property
    @jsii.member(jsii_name="bindpassInput")
    def bindpass_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bindpassInput"))

    @builtins.property
    @jsii.member(jsii_name="caseSensitiveNamesInput")
    def case_sensitive_names_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "caseSensitiveNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="clientTlsCertInput")
    def client_tls_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientTlsCertInput"))

    @builtins.property
    @jsii.member(jsii_name="clientTlsKeyInput")
    def client_tls_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientTlsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultLeaseTtlSecondsInput")
    def default_lease_ttl_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultLeaseTtlSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="denyNullBindInput")
    def deny_null_bind_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "denyNullBindInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="disableRemountInput")
    def disable_remount_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableRemountInput"))

    @builtins.property
    @jsii.member(jsii_name="discoverdnInput")
    def discoverdn_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "discoverdnInput"))

    @builtins.property
    @jsii.member(jsii_name="formatterInput")
    def formatter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatterInput"))

    @builtins.property
    @jsii.member(jsii_name="groupattrInput")
    def groupattr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupattrInput"))

    @builtins.property
    @jsii.member(jsii_name="groupdnInput")
    def groupdn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupdnInput"))

    @builtins.property
    @jsii.member(jsii_name="groupfilterInput")
    def groupfilter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupfilterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureTlsInput")
    def insecure_tls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "insecureTlsInput"))

    @builtins.property
    @jsii.member(jsii_name="lastRotationToleranceInput")
    def last_rotation_tolerance_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lastRotationToleranceInput"))

    @builtins.property
    @jsii.member(jsii_name="lengthInput")
    def length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lengthInput"))

    @builtins.property
    @jsii.member(jsii_name="localInput")
    def local_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "localInput"))

    @builtins.property
    @jsii.member(jsii_name="maxLeaseTtlSecondsInput")
    def max_lease_ttl_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxLeaseTtlSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTtlInput")
    def max_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordPolicyInput")
    def password_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="requestTimeoutInput")
    def request_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "requestTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="starttlsInput")
    def starttls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "starttlsInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsMaxVersionInput")
    def tls_max_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsMaxVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsMinVersionInput")
    def tls_min_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsMinVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="upndomainInput")
    def upndomain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "upndomainInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="usePre111GroupCnBehaviorInput")
    def use_pre111_group_cn_behavior_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "usePre111GroupCnBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="userattrInput")
    def userattr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userattrInput"))

    @builtins.property
    @jsii.member(jsii_name="userdnInput")
    def userdn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userdnInput"))

    @builtins.property
    @jsii.member(jsii_name="useTokenGroupsInput")
    def use_token_groups_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useTokenGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="anonymousGroupSearch")
    def anonymous_group_search(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "anonymousGroupSearch"))

    @anonymous_group_search.setter
    def anonymous_group_search(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "anonymous_group_search").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anonymousGroupSearch", value)

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backend"))

    @backend.setter
    def backend(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "backend").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backend", value)

    @builtins.property
    @jsii.member(jsii_name="binddn")
    def binddn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "binddn"))

    @binddn.setter
    def binddn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "binddn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "binddn", value)

    @builtins.property
    @jsii.member(jsii_name="bindpass")
    def bindpass(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bindpass"))

    @bindpass.setter
    def bindpass(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "bindpass").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bindpass", value)

    @builtins.property
    @jsii.member(jsii_name="caseSensitiveNames")
    def case_sensitive_names(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "caseSensitiveNames"))

    @case_sensitive_names.setter
    def case_sensitive_names(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "case_sensitive_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caseSensitiveNames", value)

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="clientTlsCert")
    def client_tls_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientTlsCert"))

    @client_tls_cert.setter
    def client_tls_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "client_tls_cert").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientTlsCert", value)

    @builtins.property
    @jsii.member(jsii_name="clientTlsKey")
    def client_tls_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientTlsKey"))

    @client_tls_key.setter
    def client_tls_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "client_tls_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientTlsKey", value)

    @builtins.property
    @jsii.member(jsii_name="defaultLeaseTtlSeconds")
    def default_lease_ttl_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultLeaseTtlSeconds"))

    @default_lease_ttl_seconds.setter
    def default_lease_ttl_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "default_lease_ttl_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultLeaseTtlSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="denyNullBind")
    def deny_null_bind(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "denyNullBind"))

    @deny_null_bind.setter
    def deny_null_bind(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "deny_null_bind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "denyNullBind", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disableRemount")
    def disable_remount(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableRemount"))

    @disable_remount.setter
    def disable_remount(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "disable_remount").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableRemount", value)

    @builtins.property
    @jsii.member(jsii_name="discoverdn")
    def discoverdn(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "discoverdn"))

    @discoverdn.setter
    def discoverdn(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "discoverdn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "discoverdn", value)

    @builtins.property
    @jsii.member(jsii_name="formatter")
    def formatter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "formatter"))

    @formatter.setter
    def formatter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "formatter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "formatter", value)

    @builtins.property
    @jsii.member(jsii_name="groupattr")
    def groupattr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupattr"))

    @groupattr.setter
    def groupattr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "groupattr").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupattr", value)

    @builtins.property
    @jsii.member(jsii_name="groupdn")
    def groupdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupdn"))

    @groupdn.setter
    def groupdn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "groupdn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupdn", value)

    @builtins.property
    @jsii.member(jsii_name="groupfilter")
    def groupfilter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupfilter"))

    @groupfilter.setter
    def groupfilter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "groupfilter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupfilter", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="insecureTls")
    def insecure_tls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "insecureTls"))

    @insecure_tls.setter
    def insecure_tls(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "insecure_tls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureTls", value)

    @builtins.property
    @jsii.member(jsii_name="lastRotationTolerance")
    def last_rotation_tolerance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lastRotationTolerance"))

    @last_rotation_tolerance.setter
    def last_rotation_tolerance(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "last_rotation_tolerance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastRotationTolerance", value)

    @builtins.property
    @jsii.member(jsii_name="length")
    def length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "length"))

    @length.setter
    def length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "length", value)

    @builtins.property
    @jsii.member(jsii_name="local")
    def local(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "local"))

    @local.setter
    def local(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "local").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "local", value)

    @builtins.property
    @jsii.member(jsii_name="maxLeaseTtlSeconds")
    def max_lease_ttl_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxLeaseTtlSeconds"))

    @max_lease_ttl_seconds.setter
    def max_lease_ttl_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "max_lease_ttl_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxLeaseTtlSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="maxTtl")
    def max_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxTtl"))

    @max_ttl.setter
    def max_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "max_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTtl", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="passwordPolicy")
    def password_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passwordPolicy"))

    @password_policy.setter
    def password_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "password_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="requestTimeout")
    def request_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "requestTimeout"))

    @request_timeout.setter
    def request_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "request_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="starttls")
    def starttls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "starttls"))

    @starttls.setter
    def starttls(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "starttls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "starttls", value)

    @builtins.property
    @jsii.member(jsii_name="tlsMaxVersion")
    def tls_max_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsMaxVersion"))

    @tls_max_version.setter
    def tls_max_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "tls_max_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsMaxVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tlsMinVersion")
    def tls_min_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsMinVersion"))

    @tls_min_version.setter
    def tls_min_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "tls_min_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsMinVersion", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="upndomain")
    def upndomain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "upndomain"))

    @upndomain.setter
    def upndomain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "upndomain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upndomain", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="usePre111GroupCnBehavior")
    def use_pre111_group_cn_behavior(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "usePre111GroupCnBehavior"))

    @use_pre111_group_cn_behavior.setter
    def use_pre111_group_cn_behavior(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "use_pre111_group_cn_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usePre111GroupCnBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="userattr")
    def userattr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userattr"))

    @userattr.setter
    def userattr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "userattr").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userattr", value)

    @builtins.property
    @jsii.member(jsii_name="userdn")
    def userdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userdn"))

    @userdn.setter
    def userdn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "userdn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userdn", value)

    @builtins.property
    @jsii.member(jsii_name="useTokenGroups")
    def use_token_groups(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useTokenGroups"))

    @use_token_groups.setter
    def use_token_groups(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdSecretBackend, "use_token_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useTokenGroups", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.adSecretBackend.AdSecretBackendConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "binddn": "binddn",
        "bindpass": "bindpass",
        "anonymous_group_search": "anonymousGroupSearch",
        "backend": "backend",
        "case_sensitive_names": "caseSensitiveNames",
        "certificate": "certificate",
        "client_tls_cert": "clientTlsCert",
        "client_tls_key": "clientTlsKey",
        "default_lease_ttl_seconds": "defaultLeaseTtlSeconds",
        "deny_null_bind": "denyNullBind",
        "description": "description",
        "disable_remount": "disableRemount",
        "discoverdn": "discoverdn",
        "formatter": "formatter",
        "groupattr": "groupattr",
        "groupdn": "groupdn",
        "groupfilter": "groupfilter",
        "id": "id",
        "insecure_tls": "insecureTls",
        "last_rotation_tolerance": "lastRotationTolerance",
        "length": "length",
        "local": "local",
        "max_lease_ttl_seconds": "maxLeaseTtlSeconds",
        "max_ttl": "maxTtl",
        "namespace": "namespace",
        "password_policy": "passwordPolicy",
        "request_timeout": "requestTimeout",
        "starttls": "starttls",
        "tls_max_version": "tlsMaxVersion",
        "tls_min_version": "tlsMinVersion",
        "ttl": "ttl",
        "upndomain": "upndomain",
        "url": "url",
        "use_pre111_group_cn_behavior": "usePre111GroupCnBehavior",
        "userattr": "userattr",
        "userdn": "userdn",
        "use_token_groups": "useTokenGroups",
    },
)
class AdSecretBackendConfig(cdktf.TerraformMetaArguments):
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
        binddn: builtins.str,
        bindpass: builtins.str,
        anonymous_group_search: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        backend: typing.Optional[builtins.str] = None,
        case_sensitive_names: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        certificate: typing.Optional[builtins.str] = None,
        client_tls_cert: typing.Optional[builtins.str] = None,
        client_tls_key: typing.Optional[builtins.str] = None,
        default_lease_ttl_seconds: typing.Optional[jsii.Number] = None,
        deny_null_bind: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        disable_remount: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        discoverdn: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        formatter: typing.Optional[builtins.str] = None,
        groupattr: typing.Optional[builtins.str] = None,
        groupdn: typing.Optional[builtins.str] = None,
        groupfilter: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        insecure_tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        last_rotation_tolerance: typing.Optional[jsii.Number] = None,
        length: typing.Optional[jsii.Number] = None,
        local: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_lease_ttl_seconds: typing.Optional[jsii.Number] = None,
        max_ttl: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        password_policy: typing.Optional[builtins.str] = None,
        request_timeout: typing.Optional[jsii.Number] = None,
        starttls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_max_version: typing.Optional[builtins.str] = None,
        tls_min_version: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[jsii.Number] = None,
        upndomain: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
        use_pre111_group_cn_behavior: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        userattr: typing.Optional[builtins.str] = None,
        userdn: typing.Optional[builtins.str] = None,
        use_token_groups: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param binddn: Distinguished name of object to bind when performing user and group search. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#binddn AdSecretBackend#binddn}
        :param bindpass: LDAP password for searching for the user DN. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#bindpass AdSecretBackend#bindpass}
        :param anonymous_group_search: Use anonymous binds when performing LDAP group searches (if true the initial credentials will still be used for the initial connection test). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#anonymous_group_search AdSecretBackend#anonymous_group_search}
        :param backend: The mount path for a backend, for example, the path given in "$ vault auth enable -path=my-ad ad". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#backend AdSecretBackend#backend}
        :param case_sensitive_names: If true, case sensitivity will be used when comparing usernames and groups for matching policies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#case_sensitive_names AdSecretBackend#case_sensitive_names}
        :param certificate: CA certificate to use when verifying LDAP server certificate, must be x509 PEM encoded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#certificate AdSecretBackend#certificate}
        :param client_tls_cert: Client certificate to provide to the LDAP server, must be x509 PEM encoded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#client_tls_cert AdSecretBackend#client_tls_cert}
        :param client_tls_key: Client certificate key to provide to the LDAP server, must be x509 PEM encoded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#client_tls_key AdSecretBackend#client_tls_key}
        :param default_lease_ttl_seconds: Default lease duration for secrets in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#default_lease_ttl_seconds AdSecretBackend#default_lease_ttl_seconds}
        :param deny_null_bind: Denies an unauthenticated LDAP bind request if the user's password is empty; defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#deny_null_bind AdSecretBackend#deny_null_bind}
        :param description: Human-friendly description of the mount for the backend. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#description AdSecretBackend#description}
        :param disable_remount: If set, opts out of mount migration on path updates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#disable_remount AdSecretBackend#disable_remount}
        :param discoverdn: Use anonymous bind to discover the bind DN of a user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#discoverdn AdSecretBackend#discoverdn}
        :param formatter: Text to insert the password into, ex. "customPrefix{{PASSWORD}}customSuffix". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#formatter AdSecretBackend#formatter}
        :param groupattr: LDAP attribute to follow on objects returned by in order to enumerate user group membership. Examples: "cn" or "memberOf", etc. Default: cn Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#groupattr AdSecretBackend#groupattr}
        :param groupdn: LDAP search base to use for group membership search (eg: ou=Groups,dc=example,dc=org). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#groupdn AdSecretBackend#groupdn}
        :param groupfilter: Go template for querying group membership of user. The template can access the following context variables: UserDN, Username Example: (&(objectClass=group)(member:1.2.840.113556.1.4.1941:={{.UserDN}})) Default: (|(memberUid={{.Username}})(member={{.UserDN}})(uniqueMember={{.UserDN}})) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#groupfilter AdSecretBackend#groupfilter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#id AdSecretBackend#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param insecure_tls: Skip LDAP server SSL Certificate verification - insecure and not recommended for production use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#insecure_tls AdSecretBackend#insecure_tls}
        :param last_rotation_tolerance: The number of seconds after a Vault rotation where, if Active Directory shows a later rotation, it should be considered out-of-band. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#last_rotation_tolerance AdSecretBackend#last_rotation_tolerance}
        :param length: The desired length of passwords that Vault generates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#length AdSecretBackend#length}
        :param local: Mark the secrets engine as local-only. Local engines are not replicated or removed by replication.Tolerance duration to use when checking the last rotation time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#local AdSecretBackend#local}
        :param max_lease_ttl_seconds: Maximum possible lease duration for secrets in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#max_lease_ttl_seconds AdSecretBackend#max_lease_ttl_seconds}
        :param max_ttl: In seconds, the maximum password time-to-live. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#max_ttl AdSecretBackend#max_ttl}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#namespace AdSecretBackend#namespace}
        :param password_policy: Name of the password policy to use to generate passwords. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#password_policy AdSecretBackend#password_policy}
        :param request_timeout: Timeout, in seconds, for the connection when making requests against the server before returning back an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#request_timeout AdSecretBackend#request_timeout}
        :param starttls: Issue a StartTLS command after establishing unencrypted connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#starttls AdSecretBackend#starttls}
        :param tls_max_version: Maximum TLS version to use. Accepted values are 'tls10', 'tls11', 'tls12' or 'tls13'. Defaults to 'tls12'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#tls_max_version AdSecretBackend#tls_max_version}
        :param tls_min_version: Minimum TLS version to use. Accepted values are 'tls10', 'tls11', 'tls12' or 'tls13'. Defaults to 'tls12'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#tls_min_version AdSecretBackend#tls_min_version}
        :param ttl: In seconds, the default password time-to-live. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#ttl AdSecretBackend#ttl}
        :param upndomain: Enables userPrincipalDomain login with [username]@UPNDomain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#upndomain AdSecretBackend#upndomain}
        :param url: LDAP URL to connect to (default: ldap://127.0.0.1). Multiple URLs can be specified by concatenating them with commas; they will be tried in-order. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#url AdSecretBackend#url}
        :param use_pre111_group_cn_behavior: In Vault 1.1.1 a fix for handling group CN values of different cases unfortunately introduced a regression that could cause previously defined groups to not be found due to a change in the resulting name. If set true, the pre-1.1.1 behavior for matching group CNs will be used. This is only needed in some upgrade scenarios for backwards compatibility. It is enabled by default if the config is upgraded but disabled by default on new configurations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#use_pre111_group_cn_behavior AdSecretBackend#use_pre111_group_cn_behavior}
        :param userattr: Attribute used for users (default: cn). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#userattr AdSecretBackend#userattr}
        :param userdn: LDAP domain to use for users (eg: ou=People,dc=example,dc=org). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#userdn AdSecretBackend#userdn}
        :param use_token_groups: If true, use the Active Directory tokenGroups constructed attribute of the user to find the group memberships. This will find all security groups including nested ones. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#use_token_groups AdSecretBackend#use_token_groups}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AdSecretBackendConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument binddn", value=binddn, expected_type=type_hints["binddn"])
            check_type(argname="argument bindpass", value=bindpass, expected_type=type_hints["bindpass"])
            check_type(argname="argument anonymous_group_search", value=anonymous_group_search, expected_type=type_hints["anonymous_group_search"])
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument case_sensitive_names", value=case_sensitive_names, expected_type=type_hints["case_sensitive_names"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument client_tls_cert", value=client_tls_cert, expected_type=type_hints["client_tls_cert"])
            check_type(argname="argument client_tls_key", value=client_tls_key, expected_type=type_hints["client_tls_key"])
            check_type(argname="argument default_lease_ttl_seconds", value=default_lease_ttl_seconds, expected_type=type_hints["default_lease_ttl_seconds"])
            check_type(argname="argument deny_null_bind", value=deny_null_bind, expected_type=type_hints["deny_null_bind"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disable_remount", value=disable_remount, expected_type=type_hints["disable_remount"])
            check_type(argname="argument discoverdn", value=discoverdn, expected_type=type_hints["discoverdn"])
            check_type(argname="argument formatter", value=formatter, expected_type=type_hints["formatter"])
            check_type(argname="argument groupattr", value=groupattr, expected_type=type_hints["groupattr"])
            check_type(argname="argument groupdn", value=groupdn, expected_type=type_hints["groupdn"])
            check_type(argname="argument groupfilter", value=groupfilter, expected_type=type_hints["groupfilter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument insecure_tls", value=insecure_tls, expected_type=type_hints["insecure_tls"])
            check_type(argname="argument last_rotation_tolerance", value=last_rotation_tolerance, expected_type=type_hints["last_rotation_tolerance"])
            check_type(argname="argument length", value=length, expected_type=type_hints["length"])
            check_type(argname="argument local", value=local, expected_type=type_hints["local"])
            check_type(argname="argument max_lease_ttl_seconds", value=max_lease_ttl_seconds, expected_type=type_hints["max_lease_ttl_seconds"])
            check_type(argname="argument max_ttl", value=max_ttl, expected_type=type_hints["max_ttl"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument password_policy", value=password_policy, expected_type=type_hints["password_policy"])
            check_type(argname="argument request_timeout", value=request_timeout, expected_type=type_hints["request_timeout"])
            check_type(argname="argument starttls", value=starttls, expected_type=type_hints["starttls"])
            check_type(argname="argument tls_max_version", value=tls_max_version, expected_type=type_hints["tls_max_version"])
            check_type(argname="argument tls_min_version", value=tls_min_version, expected_type=type_hints["tls_min_version"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument upndomain", value=upndomain, expected_type=type_hints["upndomain"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument use_pre111_group_cn_behavior", value=use_pre111_group_cn_behavior, expected_type=type_hints["use_pre111_group_cn_behavior"])
            check_type(argname="argument userattr", value=userattr, expected_type=type_hints["userattr"])
            check_type(argname="argument userdn", value=userdn, expected_type=type_hints["userdn"])
            check_type(argname="argument use_token_groups", value=use_token_groups, expected_type=type_hints["use_token_groups"])
        self._values: typing.Dict[str, typing.Any] = {
            "binddn": binddn,
            "bindpass": bindpass,
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
        if anonymous_group_search is not None:
            self._values["anonymous_group_search"] = anonymous_group_search
        if backend is not None:
            self._values["backend"] = backend
        if case_sensitive_names is not None:
            self._values["case_sensitive_names"] = case_sensitive_names
        if certificate is not None:
            self._values["certificate"] = certificate
        if client_tls_cert is not None:
            self._values["client_tls_cert"] = client_tls_cert
        if client_tls_key is not None:
            self._values["client_tls_key"] = client_tls_key
        if default_lease_ttl_seconds is not None:
            self._values["default_lease_ttl_seconds"] = default_lease_ttl_seconds
        if deny_null_bind is not None:
            self._values["deny_null_bind"] = deny_null_bind
        if description is not None:
            self._values["description"] = description
        if disable_remount is not None:
            self._values["disable_remount"] = disable_remount
        if discoverdn is not None:
            self._values["discoverdn"] = discoverdn
        if formatter is not None:
            self._values["formatter"] = formatter
        if groupattr is not None:
            self._values["groupattr"] = groupattr
        if groupdn is not None:
            self._values["groupdn"] = groupdn
        if groupfilter is not None:
            self._values["groupfilter"] = groupfilter
        if id is not None:
            self._values["id"] = id
        if insecure_tls is not None:
            self._values["insecure_tls"] = insecure_tls
        if last_rotation_tolerance is not None:
            self._values["last_rotation_tolerance"] = last_rotation_tolerance
        if length is not None:
            self._values["length"] = length
        if local is not None:
            self._values["local"] = local
        if max_lease_ttl_seconds is not None:
            self._values["max_lease_ttl_seconds"] = max_lease_ttl_seconds
        if max_ttl is not None:
            self._values["max_ttl"] = max_ttl
        if namespace is not None:
            self._values["namespace"] = namespace
        if password_policy is not None:
            self._values["password_policy"] = password_policy
        if request_timeout is not None:
            self._values["request_timeout"] = request_timeout
        if starttls is not None:
            self._values["starttls"] = starttls
        if tls_max_version is not None:
            self._values["tls_max_version"] = tls_max_version
        if tls_min_version is not None:
            self._values["tls_min_version"] = tls_min_version
        if ttl is not None:
            self._values["ttl"] = ttl
        if upndomain is not None:
            self._values["upndomain"] = upndomain
        if url is not None:
            self._values["url"] = url
        if use_pre111_group_cn_behavior is not None:
            self._values["use_pre111_group_cn_behavior"] = use_pre111_group_cn_behavior
        if userattr is not None:
            self._values["userattr"] = userattr
        if userdn is not None:
            self._values["userdn"] = userdn
        if use_token_groups is not None:
            self._values["use_token_groups"] = use_token_groups

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
    def binddn(self) -> builtins.str:
        '''Distinguished name of object to bind when performing user and group search.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#binddn AdSecretBackend#binddn}
        '''
        result = self._values.get("binddn")
        assert result is not None, "Required property 'binddn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bindpass(self) -> builtins.str:
        '''LDAP password for searching for the user DN.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#bindpass AdSecretBackend#bindpass}
        '''
        result = self._values.get("bindpass")
        assert result is not None, "Required property 'bindpass' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def anonymous_group_search(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Use anonymous binds when performing LDAP group searches (if true the initial credentials will still be used for the initial connection test).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#anonymous_group_search AdSecretBackend#anonymous_group_search}
        '''
        result = self._values.get("anonymous_group_search")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def backend(self) -> typing.Optional[builtins.str]:
        '''The mount path for a backend, for example, the path given in "$ vault auth enable -path=my-ad ad".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#backend AdSecretBackend#backend}
        '''
        result = self._values.get("backend")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def case_sensitive_names(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, case sensitivity will be used when comparing usernames and groups for matching policies.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#case_sensitive_names AdSecretBackend#case_sensitive_names}
        '''
        result = self._values.get("case_sensitive_names")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''CA certificate to use when verifying LDAP server certificate, must be x509 PEM encoded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#certificate AdSecretBackend#certificate}
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_tls_cert(self) -> typing.Optional[builtins.str]:
        '''Client certificate to provide to the LDAP server, must be x509 PEM encoded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#client_tls_cert AdSecretBackend#client_tls_cert}
        '''
        result = self._values.get("client_tls_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_tls_key(self) -> typing.Optional[builtins.str]:
        '''Client certificate key to provide to the LDAP server, must be x509 PEM encoded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#client_tls_key AdSecretBackend#client_tls_key}
        '''
        result = self._values.get("client_tls_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_lease_ttl_seconds(self) -> typing.Optional[jsii.Number]:
        '''Default lease duration for secrets in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#default_lease_ttl_seconds AdSecretBackend#default_lease_ttl_seconds}
        '''
        result = self._values.get("default_lease_ttl_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def deny_null_bind(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Denies an unauthenticated LDAP bind request if the user's password is empty; defaults to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#deny_null_bind AdSecretBackend#deny_null_bind}
        '''
        result = self._values.get("deny_null_bind")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Human-friendly description of the mount for the backend.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#description AdSecretBackend#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_remount(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set, opts out of mount migration on path updates.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#disable_remount AdSecretBackend#disable_remount}
        '''
        result = self._values.get("disable_remount")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def discoverdn(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Use anonymous bind to discover the bind DN of a user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#discoverdn AdSecretBackend#discoverdn}
        '''
        result = self._values.get("discoverdn")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def formatter(self) -> typing.Optional[builtins.str]:
        '''Text to insert the password into, ex. "customPrefix{{PASSWORD}}customSuffix".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#formatter AdSecretBackend#formatter}
        '''
        result = self._values.get("formatter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def groupattr(self) -> typing.Optional[builtins.str]:
        '''LDAP attribute to follow on objects returned by  in order to enumerate user group membership.

        Examples: "cn" or "memberOf", etc. Default: cn

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#groupattr AdSecretBackend#groupattr}
        '''
        result = self._values.get("groupattr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def groupdn(self) -> typing.Optional[builtins.str]:
        '''LDAP search base to use for group membership search (eg: ou=Groups,dc=example,dc=org).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#groupdn AdSecretBackend#groupdn}
        '''
        result = self._values.get("groupdn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def groupfilter(self) -> typing.Optional[builtins.str]:
        '''Go template for querying group membership of user.

        The template can access the following context variables: UserDN, Username Example: (&(objectClass=group)(member:1.2.840.113556.1.4.1941:={{.UserDN}})) Default: (|(memberUid={{.Username}})(member={{.UserDN}})(uniqueMember={{.UserDN}}))

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#groupfilter AdSecretBackend#groupfilter}
        '''
        result = self._values.get("groupfilter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#id AdSecretBackend#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure_tls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Skip LDAP server SSL Certificate verification - insecure and not recommended for production use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#insecure_tls AdSecretBackend#insecure_tls}
        '''
        result = self._values.get("insecure_tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def last_rotation_tolerance(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds after a Vault rotation where, if Active Directory shows a later rotation, it should be considered out-of-band.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#last_rotation_tolerance AdSecretBackend#last_rotation_tolerance}
        '''
        result = self._values.get("last_rotation_tolerance")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def length(self) -> typing.Optional[jsii.Number]:
        '''The desired length of passwords that Vault generates.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#length AdSecretBackend#length}
        '''
        result = self._values.get("length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def local(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Mark the secrets engine as local-only.

        Local engines are not replicated or removed by replication.Tolerance duration to use when checking the last rotation time.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#local AdSecretBackend#local}
        '''
        result = self._values.get("local")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_lease_ttl_seconds(self) -> typing.Optional[jsii.Number]:
        '''Maximum possible lease duration for secrets in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#max_lease_ttl_seconds AdSecretBackend#max_lease_ttl_seconds}
        '''
        result = self._values.get("max_lease_ttl_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_ttl(self) -> typing.Optional[jsii.Number]:
        '''In seconds, the maximum password time-to-live.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#max_ttl AdSecretBackend#max_ttl}
        '''
        result = self._values.get("max_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#namespace AdSecretBackend#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password_policy(self) -> typing.Optional[builtins.str]:
        '''Name of the password policy to use to generate passwords.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#password_policy AdSecretBackend#password_policy}
        '''
        result = self._values.get("password_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_timeout(self) -> typing.Optional[jsii.Number]:
        '''Timeout, in seconds, for the connection when making requests against the server before returning back an error.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#request_timeout AdSecretBackend#request_timeout}
        '''
        result = self._values.get("request_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def starttls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Issue a StartTLS command after establishing unencrypted connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#starttls AdSecretBackend#starttls}
        '''
        result = self._values.get("starttls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tls_max_version(self) -> typing.Optional[builtins.str]:
        '''Maximum TLS version to use. Accepted values are 'tls10', 'tls11', 'tls12' or 'tls13'. Defaults to 'tls12'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#tls_max_version AdSecretBackend#tls_max_version}
        '''
        result = self._values.get("tls_max_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_min_version(self) -> typing.Optional[builtins.str]:
        '''Minimum TLS version to use. Accepted values are 'tls10', 'tls11', 'tls12' or 'tls13'. Defaults to 'tls12'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#tls_min_version AdSecretBackend#tls_min_version}
        '''
        result = self._values.get("tls_min_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[jsii.Number]:
        '''In seconds, the default password time-to-live.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#ttl AdSecretBackend#ttl}
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def upndomain(self) -> typing.Optional[builtins.str]:
        '''Enables userPrincipalDomain login with [username]@UPNDomain.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#upndomain AdSecretBackend#upndomain}
        '''
        result = self._values.get("upndomain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''LDAP URL to connect to (default: ldap://127.0.0.1). Multiple URLs can be specified by concatenating them with commas; they will be tried in-order.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#url AdSecretBackend#url}
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_pre111_group_cn_behavior(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''In Vault 1.1.1 a fix for handling group CN values of different cases unfortunately introduced a regression that could cause previously defined groups to not be found due to a change in the resulting name. If set true, the pre-1.1.1 behavior for matching group CNs will be used. This is only needed in some upgrade scenarios for backwards compatibility. It is enabled by default if the config is upgraded but disabled by default on new configurations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#use_pre111_group_cn_behavior AdSecretBackend#use_pre111_group_cn_behavior}
        '''
        result = self._values.get("use_pre111_group_cn_behavior")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def userattr(self) -> typing.Optional[builtins.str]:
        '''Attribute used for users (default: cn).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#userattr AdSecretBackend#userattr}
        '''
        result = self._values.get("userattr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def userdn(self) -> typing.Optional[builtins.str]:
        '''LDAP domain to use for users (eg: ou=People,dc=example,dc=org).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#userdn AdSecretBackend#userdn}
        '''
        result = self._values.get("userdn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_token_groups(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, use the Active Directory tokenGroups constructed attribute of the user to find the group memberships.

        This will find all security groups including nested ones.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/ad_secret_backend#use_token_groups AdSecretBackend#use_token_groups}
        '''
        result = self._values.get("use_token_groups")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AdSecretBackendConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AdSecretBackend",
    "AdSecretBackendConfig",
]

publication.publish()
