'''
# `vault_token_auth_backend_role`

Refer to the Terraform Registory for docs: [`vault_token_auth_backend_role`](https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role).
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


class TokenAuthBackendRole(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.tokenAuthBackendRole.TokenAuthBackendRole",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role vault_token_auth_backend_role}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        role_name: builtins.str,
        allowed_entity_aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_policies_glob: typing.Optional[typing.Sequence[builtins.str]] = None,
        disallowed_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        disallowed_policies_glob: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        orphan: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path_suffix: typing.Optional[builtins.str] = None,
        renewable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        token_bound_cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_explicit_max_ttl: typing.Optional[jsii.Number] = None,
        token_max_ttl: typing.Optional[jsii.Number] = None,
        token_no_default_policy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        token_num_uses: typing.Optional[jsii.Number] = None,
        token_period: typing.Optional[jsii.Number] = None,
        token_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_ttl: typing.Optional[jsii.Number] = None,
        token_type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role vault_token_auth_backend_role} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param role_name: Name of the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#role_name TokenAuthBackendRole#role_name}
        :param allowed_entity_aliases: Set of allowed entity aliases for this role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#allowed_entity_aliases TokenAuthBackendRole#allowed_entity_aliases}
        :param allowed_policies: List of allowed policies for given role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#allowed_policies TokenAuthBackendRole#allowed_policies}
        :param allowed_policies_glob: Set of allowed policies with glob match for given role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#allowed_policies_glob TokenAuthBackendRole#allowed_policies_glob}
        :param disallowed_policies: List of disallowed policies for given role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#disallowed_policies TokenAuthBackendRole#disallowed_policies}
        :param disallowed_policies_glob: Set of disallowed policies with glob match for given role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#disallowed_policies_glob TokenAuthBackendRole#disallowed_policies_glob}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#id TokenAuthBackendRole#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#namespace TokenAuthBackendRole#namespace}
        :param orphan: If true, tokens created against this policy will be orphan tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#orphan TokenAuthBackendRole#orphan}
        :param path_suffix: Tokens created against this role will have the given suffix as part of their path in addition to the role name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#path_suffix TokenAuthBackendRole#path_suffix}
        :param renewable: Whether to disable the ability of the token to be renewed past its initial TTL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#renewable TokenAuthBackendRole#renewable}
        :param token_bound_cidrs: Specifies the blocks of IP addresses which are allowed to use the generated token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_bound_cidrs TokenAuthBackendRole#token_bound_cidrs}
        :param token_explicit_max_ttl: Generated Token's Explicit Maximum TTL in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_explicit_max_ttl TokenAuthBackendRole#token_explicit_max_ttl}
        :param token_max_ttl: The maximum lifetime of the generated token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_max_ttl TokenAuthBackendRole#token_max_ttl}
        :param token_no_default_policy: If true, the 'default' policy will not automatically be added to generated tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_no_default_policy TokenAuthBackendRole#token_no_default_policy}
        :param token_num_uses: The maximum number of times a token may be used, a value of zero means unlimited. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_num_uses TokenAuthBackendRole#token_num_uses}
        :param token_period: Generated Token's Period. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_period TokenAuthBackendRole#token_period}
        :param token_policies: Generated Token's Policies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_policies TokenAuthBackendRole#token_policies}
        :param token_ttl: The initial ttl of the token to generate in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_ttl TokenAuthBackendRole#token_ttl}
        :param token_type: The type of token to generate, service or batch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_type TokenAuthBackendRole#token_type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TokenAuthBackendRole.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = TokenAuthBackendRoleConfig(
            role_name=role_name,
            allowed_entity_aliases=allowed_entity_aliases,
            allowed_policies=allowed_policies,
            allowed_policies_glob=allowed_policies_glob,
            disallowed_policies=disallowed_policies,
            disallowed_policies_glob=disallowed_policies_glob,
            id=id,
            namespace=namespace,
            orphan=orphan,
            path_suffix=path_suffix,
            renewable=renewable,
            token_bound_cidrs=token_bound_cidrs,
            token_explicit_max_ttl=token_explicit_max_ttl,
            token_max_ttl=token_max_ttl,
            token_no_default_policy=token_no_default_policy,
            token_num_uses=token_num_uses,
            token_period=token_period,
            token_policies=token_policies,
            token_ttl=token_ttl,
            token_type=token_type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAllowedEntityAliases")
    def reset_allowed_entity_aliases(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedEntityAliases", []))

    @jsii.member(jsii_name="resetAllowedPolicies")
    def reset_allowed_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedPolicies", []))

    @jsii.member(jsii_name="resetAllowedPoliciesGlob")
    def reset_allowed_policies_glob(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedPoliciesGlob", []))

    @jsii.member(jsii_name="resetDisallowedPolicies")
    def reset_disallowed_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisallowedPolicies", []))

    @jsii.member(jsii_name="resetDisallowedPoliciesGlob")
    def reset_disallowed_policies_glob(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisallowedPoliciesGlob", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetOrphan")
    def reset_orphan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrphan", []))

    @jsii.member(jsii_name="resetPathSuffix")
    def reset_path_suffix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathSuffix", []))

    @jsii.member(jsii_name="resetRenewable")
    def reset_renewable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRenewable", []))

    @jsii.member(jsii_name="resetTokenBoundCidrs")
    def reset_token_bound_cidrs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenBoundCidrs", []))

    @jsii.member(jsii_name="resetTokenExplicitMaxTtl")
    def reset_token_explicit_max_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenExplicitMaxTtl", []))

    @jsii.member(jsii_name="resetTokenMaxTtl")
    def reset_token_max_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenMaxTtl", []))

    @jsii.member(jsii_name="resetTokenNoDefaultPolicy")
    def reset_token_no_default_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenNoDefaultPolicy", []))

    @jsii.member(jsii_name="resetTokenNumUses")
    def reset_token_num_uses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenNumUses", []))

    @jsii.member(jsii_name="resetTokenPeriod")
    def reset_token_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenPeriod", []))

    @jsii.member(jsii_name="resetTokenPolicies")
    def reset_token_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenPolicies", []))

    @jsii.member(jsii_name="resetTokenTtl")
    def reset_token_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenTtl", []))

    @jsii.member(jsii_name="resetTokenType")
    def reset_token_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="allowedEntityAliasesInput")
    def allowed_entity_aliases_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedEntityAliasesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedPoliciesGlobInput")
    def allowed_policies_glob_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedPoliciesGlobInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedPoliciesInput")
    def allowed_policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="disallowedPoliciesGlobInput")
    def disallowed_policies_glob_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "disallowedPoliciesGlobInput"))

    @builtins.property
    @jsii.member(jsii_name="disallowedPoliciesInput")
    def disallowed_policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "disallowedPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="orphanInput")
    def orphan_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "orphanInput"))

    @builtins.property
    @jsii.member(jsii_name="pathSuffixInput")
    def path_suffix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathSuffixInput"))

    @builtins.property
    @jsii.member(jsii_name="renewableInput")
    def renewable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "renewableInput"))

    @builtins.property
    @jsii.member(jsii_name="roleNameInput")
    def role_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenBoundCidrsInput")
    def token_bound_cidrs_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tokenBoundCidrsInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenExplicitMaxTtlInput")
    def token_explicit_max_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tokenExplicitMaxTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenMaxTtlInput")
    def token_max_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tokenMaxTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenNoDefaultPolicyInput")
    def token_no_default_policy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tokenNoDefaultPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenNumUsesInput")
    def token_num_uses_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tokenNumUsesInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenPeriodInput")
    def token_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tokenPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenPoliciesInput")
    def token_policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tokenPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenTtlInput")
    def token_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tokenTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenTypeInput")
    def token_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedEntityAliases")
    def allowed_entity_aliases(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedEntityAliases"))

    @allowed_entity_aliases.setter
    def allowed_entity_aliases(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "allowed_entity_aliases").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedEntityAliases", value)

    @builtins.property
    @jsii.member(jsii_name="allowedPolicies")
    def allowed_policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedPolicies"))

    @allowed_policies.setter
    def allowed_policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "allowed_policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="allowedPoliciesGlob")
    def allowed_policies_glob(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedPoliciesGlob"))

    @allowed_policies_glob.setter
    def allowed_policies_glob(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "allowed_policies_glob").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedPoliciesGlob", value)

    @builtins.property
    @jsii.member(jsii_name="disallowedPolicies")
    def disallowed_policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "disallowedPolicies"))

    @disallowed_policies.setter
    def disallowed_policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "disallowed_policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disallowedPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="disallowedPoliciesGlob")
    def disallowed_policies_glob(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "disallowedPoliciesGlob"))

    @disallowed_policies_glob.setter
    def disallowed_policies_glob(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "disallowed_policies_glob").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disallowedPoliciesGlob", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="orphan")
    def orphan(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "orphan"))

    @orphan.setter
    def orphan(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "orphan").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "orphan", value)

    @builtins.property
    @jsii.member(jsii_name="pathSuffix")
    def path_suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathSuffix"))

    @path_suffix.setter
    def path_suffix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "path_suffix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathSuffix", value)

    @builtins.property
    @jsii.member(jsii_name="renewable")
    def renewable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "renewable"))

    @renewable.setter
    def renewable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "renewable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "renewable", value)

    @builtins.property
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleName"))

    @role_name.setter
    def role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "role_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleName", value)

    @builtins.property
    @jsii.member(jsii_name="tokenBoundCidrs")
    def token_bound_cidrs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tokenBoundCidrs"))

    @token_bound_cidrs.setter
    def token_bound_cidrs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "token_bound_cidrs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenBoundCidrs", value)

    @builtins.property
    @jsii.member(jsii_name="tokenExplicitMaxTtl")
    def token_explicit_max_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenExplicitMaxTtl"))

    @token_explicit_max_ttl.setter
    def token_explicit_max_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "token_explicit_max_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenExplicitMaxTtl", value)

    @builtins.property
    @jsii.member(jsii_name="tokenMaxTtl")
    def token_max_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenMaxTtl"))

    @token_max_ttl.setter
    def token_max_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "token_max_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenMaxTtl", value)

    @builtins.property
    @jsii.member(jsii_name="tokenNoDefaultPolicy")
    def token_no_default_policy(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tokenNoDefaultPolicy"))

    @token_no_default_policy.setter
    def token_no_default_policy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "token_no_default_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenNoDefaultPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="tokenNumUses")
    def token_num_uses(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenNumUses"))

    @token_num_uses.setter
    def token_num_uses(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "token_num_uses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenNumUses", value)

    @builtins.property
    @jsii.member(jsii_name="tokenPeriod")
    def token_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenPeriod"))

    @token_period.setter
    def token_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "token_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="tokenPolicies")
    def token_policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tokenPolicies"))

    @token_policies.setter
    def token_policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "token_policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="tokenTtl")
    def token_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenTtl"))

    @token_ttl.setter
    def token_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "token_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenTtl", value)

    @builtins.property
    @jsii.member(jsii_name="tokenType")
    def token_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenType"))

    @token_type.setter
    def token_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TokenAuthBackendRole, "token_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.tokenAuthBackendRole.TokenAuthBackendRoleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "role_name": "roleName",
        "allowed_entity_aliases": "allowedEntityAliases",
        "allowed_policies": "allowedPolicies",
        "allowed_policies_glob": "allowedPoliciesGlob",
        "disallowed_policies": "disallowedPolicies",
        "disallowed_policies_glob": "disallowedPoliciesGlob",
        "id": "id",
        "namespace": "namespace",
        "orphan": "orphan",
        "path_suffix": "pathSuffix",
        "renewable": "renewable",
        "token_bound_cidrs": "tokenBoundCidrs",
        "token_explicit_max_ttl": "tokenExplicitMaxTtl",
        "token_max_ttl": "tokenMaxTtl",
        "token_no_default_policy": "tokenNoDefaultPolicy",
        "token_num_uses": "tokenNumUses",
        "token_period": "tokenPeriod",
        "token_policies": "tokenPolicies",
        "token_ttl": "tokenTtl",
        "token_type": "tokenType",
    },
)
class TokenAuthBackendRoleConfig(cdktf.TerraformMetaArguments):
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
        role_name: builtins.str,
        allowed_entity_aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_policies_glob: typing.Optional[typing.Sequence[builtins.str]] = None,
        disallowed_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        disallowed_policies_glob: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        orphan: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path_suffix: typing.Optional[builtins.str] = None,
        renewable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        token_bound_cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_explicit_max_ttl: typing.Optional[jsii.Number] = None,
        token_max_ttl: typing.Optional[jsii.Number] = None,
        token_no_default_policy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        token_num_uses: typing.Optional[jsii.Number] = None,
        token_period: typing.Optional[jsii.Number] = None,
        token_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_ttl: typing.Optional[jsii.Number] = None,
        token_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param role_name: Name of the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#role_name TokenAuthBackendRole#role_name}
        :param allowed_entity_aliases: Set of allowed entity aliases for this role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#allowed_entity_aliases TokenAuthBackendRole#allowed_entity_aliases}
        :param allowed_policies: List of allowed policies for given role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#allowed_policies TokenAuthBackendRole#allowed_policies}
        :param allowed_policies_glob: Set of allowed policies with glob match for given role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#allowed_policies_glob TokenAuthBackendRole#allowed_policies_glob}
        :param disallowed_policies: List of disallowed policies for given role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#disallowed_policies TokenAuthBackendRole#disallowed_policies}
        :param disallowed_policies_glob: Set of disallowed policies with glob match for given role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#disallowed_policies_glob TokenAuthBackendRole#disallowed_policies_glob}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#id TokenAuthBackendRole#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#namespace TokenAuthBackendRole#namespace}
        :param orphan: If true, tokens created against this policy will be orphan tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#orphan TokenAuthBackendRole#orphan}
        :param path_suffix: Tokens created against this role will have the given suffix as part of their path in addition to the role name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#path_suffix TokenAuthBackendRole#path_suffix}
        :param renewable: Whether to disable the ability of the token to be renewed past its initial TTL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#renewable TokenAuthBackendRole#renewable}
        :param token_bound_cidrs: Specifies the blocks of IP addresses which are allowed to use the generated token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_bound_cidrs TokenAuthBackendRole#token_bound_cidrs}
        :param token_explicit_max_ttl: Generated Token's Explicit Maximum TTL in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_explicit_max_ttl TokenAuthBackendRole#token_explicit_max_ttl}
        :param token_max_ttl: The maximum lifetime of the generated token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_max_ttl TokenAuthBackendRole#token_max_ttl}
        :param token_no_default_policy: If true, the 'default' policy will not automatically be added to generated tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_no_default_policy TokenAuthBackendRole#token_no_default_policy}
        :param token_num_uses: The maximum number of times a token may be used, a value of zero means unlimited. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_num_uses TokenAuthBackendRole#token_num_uses}
        :param token_period: Generated Token's Period. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_period TokenAuthBackendRole#token_period}
        :param token_policies: Generated Token's Policies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_policies TokenAuthBackendRole#token_policies}
        :param token_ttl: The initial ttl of the token to generate in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_ttl TokenAuthBackendRole#token_ttl}
        :param token_type: The type of token to generate, service or batch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_type TokenAuthBackendRole#token_type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(TokenAuthBackendRoleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
            check_type(argname="argument allowed_entity_aliases", value=allowed_entity_aliases, expected_type=type_hints["allowed_entity_aliases"])
            check_type(argname="argument allowed_policies", value=allowed_policies, expected_type=type_hints["allowed_policies"])
            check_type(argname="argument allowed_policies_glob", value=allowed_policies_glob, expected_type=type_hints["allowed_policies_glob"])
            check_type(argname="argument disallowed_policies", value=disallowed_policies, expected_type=type_hints["disallowed_policies"])
            check_type(argname="argument disallowed_policies_glob", value=disallowed_policies_glob, expected_type=type_hints["disallowed_policies_glob"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument orphan", value=orphan, expected_type=type_hints["orphan"])
            check_type(argname="argument path_suffix", value=path_suffix, expected_type=type_hints["path_suffix"])
            check_type(argname="argument renewable", value=renewable, expected_type=type_hints["renewable"])
            check_type(argname="argument token_bound_cidrs", value=token_bound_cidrs, expected_type=type_hints["token_bound_cidrs"])
            check_type(argname="argument token_explicit_max_ttl", value=token_explicit_max_ttl, expected_type=type_hints["token_explicit_max_ttl"])
            check_type(argname="argument token_max_ttl", value=token_max_ttl, expected_type=type_hints["token_max_ttl"])
            check_type(argname="argument token_no_default_policy", value=token_no_default_policy, expected_type=type_hints["token_no_default_policy"])
            check_type(argname="argument token_num_uses", value=token_num_uses, expected_type=type_hints["token_num_uses"])
            check_type(argname="argument token_period", value=token_period, expected_type=type_hints["token_period"])
            check_type(argname="argument token_policies", value=token_policies, expected_type=type_hints["token_policies"])
            check_type(argname="argument token_ttl", value=token_ttl, expected_type=type_hints["token_ttl"])
            check_type(argname="argument token_type", value=token_type, expected_type=type_hints["token_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "role_name": role_name,
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
        if allowed_entity_aliases is not None:
            self._values["allowed_entity_aliases"] = allowed_entity_aliases
        if allowed_policies is not None:
            self._values["allowed_policies"] = allowed_policies
        if allowed_policies_glob is not None:
            self._values["allowed_policies_glob"] = allowed_policies_glob
        if disallowed_policies is not None:
            self._values["disallowed_policies"] = disallowed_policies
        if disallowed_policies_glob is not None:
            self._values["disallowed_policies_glob"] = disallowed_policies_glob
        if id is not None:
            self._values["id"] = id
        if namespace is not None:
            self._values["namespace"] = namespace
        if orphan is not None:
            self._values["orphan"] = orphan
        if path_suffix is not None:
            self._values["path_suffix"] = path_suffix
        if renewable is not None:
            self._values["renewable"] = renewable
        if token_bound_cidrs is not None:
            self._values["token_bound_cidrs"] = token_bound_cidrs
        if token_explicit_max_ttl is not None:
            self._values["token_explicit_max_ttl"] = token_explicit_max_ttl
        if token_max_ttl is not None:
            self._values["token_max_ttl"] = token_max_ttl
        if token_no_default_policy is not None:
            self._values["token_no_default_policy"] = token_no_default_policy
        if token_num_uses is not None:
            self._values["token_num_uses"] = token_num_uses
        if token_period is not None:
            self._values["token_period"] = token_period
        if token_policies is not None:
            self._values["token_policies"] = token_policies
        if token_ttl is not None:
            self._values["token_ttl"] = token_ttl
        if token_type is not None:
            self._values["token_type"] = token_type

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
    def role_name(self) -> builtins.str:
        '''Name of the role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#role_name TokenAuthBackendRole#role_name}
        '''
        result = self._values.get("role_name")
        assert result is not None, "Required property 'role_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_entity_aliases(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set of allowed entity aliases for this role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#allowed_entity_aliases TokenAuthBackendRole#allowed_entity_aliases}
        '''
        result = self._values.get("allowed_entity_aliases")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of allowed policies for given role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#allowed_policies TokenAuthBackendRole#allowed_policies}
        '''
        result = self._values.get("allowed_policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_policies_glob(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set of allowed policies with glob match for given role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#allowed_policies_glob TokenAuthBackendRole#allowed_policies_glob}
        '''
        result = self._values.get("allowed_policies_glob")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def disallowed_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of disallowed policies for given role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#disallowed_policies TokenAuthBackendRole#disallowed_policies}
        '''
        result = self._values.get("disallowed_policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def disallowed_policies_glob(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set of disallowed policies with glob match for given role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#disallowed_policies_glob TokenAuthBackendRole#disallowed_policies_glob}
        '''
        result = self._values.get("disallowed_policies_glob")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#id TokenAuthBackendRole#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#namespace TokenAuthBackendRole#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def orphan(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, tokens created against this policy will be orphan tokens.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#orphan TokenAuthBackendRole#orphan}
        '''
        result = self._values.get("orphan")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def path_suffix(self) -> typing.Optional[builtins.str]:
        '''Tokens created against this role will have the given suffix as part of their path in addition to the role name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#path_suffix TokenAuthBackendRole#path_suffix}
        '''
        result = self._values.get("path_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def renewable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to disable the ability of the token to be renewed past its initial TTL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#renewable TokenAuthBackendRole#renewable}
        '''
        result = self._values.get("renewable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def token_bound_cidrs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the blocks of IP addresses which are allowed to use the generated token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_bound_cidrs TokenAuthBackendRole#token_bound_cidrs}
        '''
        result = self._values.get("token_bound_cidrs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def token_explicit_max_ttl(self) -> typing.Optional[jsii.Number]:
        '''Generated Token's Explicit Maximum TTL in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_explicit_max_ttl TokenAuthBackendRole#token_explicit_max_ttl}
        '''
        result = self._values.get("token_explicit_max_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_max_ttl(self) -> typing.Optional[jsii.Number]:
        '''The maximum lifetime of the generated token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_max_ttl TokenAuthBackendRole#token_max_ttl}
        '''
        result = self._values.get("token_max_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_no_default_policy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the 'default' policy will not automatically be added to generated tokens.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_no_default_policy TokenAuthBackendRole#token_no_default_policy}
        '''
        result = self._values.get("token_no_default_policy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def token_num_uses(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times a token may be used, a value of zero means unlimited.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_num_uses TokenAuthBackendRole#token_num_uses}
        '''
        result = self._values.get("token_num_uses")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_period(self) -> typing.Optional[jsii.Number]:
        '''Generated Token's Period.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_period TokenAuthBackendRole#token_period}
        '''
        result = self._values.get("token_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Generated Token's Policies.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_policies TokenAuthBackendRole#token_policies}
        '''
        result = self._values.get("token_policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def token_ttl(self) -> typing.Optional[jsii.Number]:
        '''The initial ttl of the token to generate in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_ttl TokenAuthBackendRole#token_ttl}
        '''
        result = self._values.get("token_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_type(self) -> typing.Optional[builtins.str]:
        '''The type of token to generate, service or batch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token_auth_backend_role#token_type TokenAuthBackendRole#token_type}
        '''
        result = self._values.get("token_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TokenAuthBackendRoleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "TokenAuthBackendRole",
    "TokenAuthBackendRoleConfig",
]

publication.publish()
