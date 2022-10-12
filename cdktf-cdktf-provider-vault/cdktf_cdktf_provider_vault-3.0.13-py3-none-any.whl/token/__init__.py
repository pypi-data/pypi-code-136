'''
# `vault_token`

Refer to the Terraform Registory for docs: [`vault_token`](https://www.terraform.io/docs/providers/vault/r/token).
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


class Token(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.token.Token",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/token vault_token}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        display_name: typing.Optional[builtins.str] = None,
        explicit_max_ttl: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        no_default_policy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        no_parent: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        num_uses: typing.Optional[jsii.Number] = None,
        period: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        renewable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        renew_increment: typing.Optional[jsii.Number] = None,
        renew_min_lease: typing.Optional[jsii.Number] = None,
        role_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[builtins.str] = None,
        wrapping_ttl: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/token vault_token} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param display_name: The display name of the token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#display_name Token#display_name}
        :param explicit_max_ttl: The explicit max TTL of the token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#explicit_max_ttl Token#explicit_max_ttl}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#id Token#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metadata: Metadata to be associated with the token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#metadata Token#metadata}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#namespace Token#namespace}
        :param no_default_policy: Flag to disable the default policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#no_default_policy Token#no_default_policy}
        :param no_parent: Flag to create a token without parent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#no_parent Token#no_parent}
        :param num_uses: The number of allowed uses of the token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#num_uses Token#num_uses}
        :param period: The period of the token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#period Token#period}
        :param policies: List of policies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#policies Token#policies}
        :param renewable: Flag to allow the token to be renewed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#renewable Token#renewable}
        :param renew_increment: The renew increment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#renew_increment Token#renew_increment}
        :param renew_min_lease: The minimum lease to renew token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#renew_min_lease Token#renew_min_lease}
        :param role_name: The token role name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#role_name Token#role_name}
        :param ttl: The TTL period of the token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#ttl Token#ttl}
        :param wrapping_ttl: The TTL period of the wrapped token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#wrapping_ttl Token#wrapping_ttl}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Token.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = TokenConfig(
            display_name=display_name,
            explicit_max_ttl=explicit_max_ttl,
            id=id,
            metadata=metadata,
            namespace=namespace,
            no_default_policy=no_default_policy,
            no_parent=no_parent,
            num_uses=num_uses,
            period=period,
            policies=policies,
            renewable=renewable,
            renew_increment=renew_increment,
            renew_min_lease=renew_min_lease,
            role_name=role_name,
            ttl=ttl,
            wrapping_ttl=wrapping_ttl,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetExplicitMaxTtl")
    def reset_explicit_max_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExplicitMaxTtl", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetNoDefaultPolicy")
    def reset_no_default_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoDefaultPolicy", []))

    @jsii.member(jsii_name="resetNoParent")
    def reset_no_parent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoParent", []))

    @jsii.member(jsii_name="resetNumUses")
    def reset_num_uses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumUses", []))

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @jsii.member(jsii_name="resetPolicies")
    def reset_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicies", []))

    @jsii.member(jsii_name="resetRenewable")
    def reset_renewable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRenewable", []))

    @jsii.member(jsii_name="resetRenewIncrement")
    def reset_renew_increment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRenewIncrement", []))

    @jsii.member(jsii_name="resetRenewMinLease")
    def reset_renew_min_lease(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRenewMinLease", []))

    @jsii.member(jsii_name="resetRoleName")
    def reset_role_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleName", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @jsii.member(jsii_name="resetWrappingTtl")
    def reset_wrapping_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWrappingTtl", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="clientToken")
    def client_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientToken"))

    @builtins.property
    @jsii.member(jsii_name="leaseDuration")
    def lease_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "leaseDuration"))

    @builtins.property
    @jsii.member(jsii_name="leaseStarted")
    def lease_started(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "leaseStarted"))

    @builtins.property
    @jsii.member(jsii_name="wrappedToken")
    def wrapped_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "wrappedToken"))

    @builtins.property
    @jsii.member(jsii_name="wrappingAccessor")
    def wrapping_accessor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "wrappingAccessor"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="explicitMaxTtlInput")
    def explicit_max_ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "explicitMaxTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="noDefaultPolicyInput")
    def no_default_policy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "noDefaultPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="noParentInput")
    def no_parent_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "noParentInput"))

    @builtins.property
    @jsii.member(jsii_name="numUsesInput")
    def num_uses_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numUsesInput"))

    @builtins.property
    @jsii.member(jsii_name="periodInput")
    def period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "periodInput"))

    @builtins.property
    @jsii.member(jsii_name="policiesInput")
    def policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "policiesInput"))

    @builtins.property
    @jsii.member(jsii_name="renewableInput")
    def renewable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "renewableInput"))

    @builtins.property
    @jsii.member(jsii_name="renewIncrementInput")
    def renew_increment_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "renewIncrementInput"))

    @builtins.property
    @jsii.member(jsii_name="renewMinLeaseInput")
    def renew_min_lease_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "renewMinLeaseInput"))

    @builtins.property
    @jsii.member(jsii_name="roleNameInput")
    def role_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="wrappingTtlInput")
    def wrapping_ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "wrappingTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Token, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="explicitMaxTtl")
    def explicit_max_ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "explicitMaxTtl"))

    @explicit_max_ttl.setter
    def explicit_max_ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Token, "explicit_max_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "explicitMaxTtl", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Token, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Token, "metadata").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Token, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="noDefaultPolicy")
    def no_default_policy(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "noDefaultPolicy"))

    @no_default_policy.setter
    def no_default_policy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Token, "no_default_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noDefaultPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="noParent")
    def no_parent(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "noParent"))

    @no_parent.setter
    def no_parent(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Token, "no_parent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noParent", value)

    @builtins.property
    @jsii.member(jsii_name="numUses")
    def num_uses(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numUses"))

    @num_uses.setter
    def num_uses(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Token, "num_uses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numUses", value)

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "period"))

    @period.setter
    def period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Token, "period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "policies"))

    @policies.setter
    def policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Token, "policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="renewable")
    def renewable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "renewable"))

    @renewable.setter
    def renewable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Token, "renewable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "renewable", value)

    @builtins.property
    @jsii.member(jsii_name="renewIncrement")
    def renew_increment(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "renewIncrement"))

    @renew_increment.setter
    def renew_increment(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Token, "renew_increment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "renewIncrement", value)

    @builtins.property
    @jsii.member(jsii_name="renewMinLease")
    def renew_min_lease(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "renewMinLease"))

    @renew_min_lease.setter
    def renew_min_lease(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Token, "renew_min_lease").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "renewMinLease", value)

    @builtins.property
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleName"))

    @role_name.setter
    def role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Token, "role_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleName", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Token, "ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="wrappingTtl")
    def wrapping_ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "wrappingTtl"))

    @wrapping_ttl.setter
    def wrapping_ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Token, "wrapping_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrappingTtl", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.token.TokenConfig",
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
        "explicit_max_ttl": "explicitMaxTtl",
        "id": "id",
        "metadata": "metadata",
        "namespace": "namespace",
        "no_default_policy": "noDefaultPolicy",
        "no_parent": "noParent",
        "num_uses": "numUses",
        "period": "period",
        "policies": "policies",
        "renewable": "renewable",
        "renew_increment": "renewIncrement",
        "renew_min_lease": "renewMinLease",
        "role_name": "roleName",
        "ttl": "ttl",
        "wrapping_ttl": "wrappingTtl",
    },
)
class TokenConfig(cdktf.TerraformMetaArguments):
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
        display_name: typing.Optional[builtins.str] = None,
        explicit_max_ttl: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        no_default_policy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        no_parent: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        num_uses: typing.Optional[jsii.Number] = None,
        period: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        renewable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        renew_increment: typing.Optional[jsii.Number] = None,
        renew_min_lease: typing.Optional[jsii.Number] = None,
        role_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[builtins.str] = None,
        wrapping_ttl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param display_name: The display name of the token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#display_name Token#display_name}
        :param explicit_max_ttl: The explicit max TTL of the token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#explicit_max_ttl Token#explicit_max_ttl}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#id Token#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metadata: Metadata to be associated with the token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#metadata Token#metadata}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#namespace Token#namespace}
        :param no_default_policy: Flag to disable the default policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#no_default_policy Token#no_default_policy}
        :param no_parent: Flag to create a token without parent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#no_parent Token#no_parent}
        :param num_uses: The number of allowed uses of the token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#num_uses Token#num_uses}
        :param period: The period of the token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#period Token#period}
        :param policies: List of policies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#policies Token#policies}
        :param renewable: Flag to allow the token to be renewed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#renewable Token#renewable}
        :param renew_increment: The renew increment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#renew_increment Token#renew_increment}
        :param renew_min_lease: The minimum lease to renew token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#renew_min_lease Token#renew_min_lease}
        :param role_name: The token role name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#role_name Token#role_name}
        :param ttl: The TTL period of the token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#ttl Token#ttl}
        :param wrapping_ttl: The TTL period of the wrapped token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#wrapping_ttl Token#wrapping_ttl}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(TokenConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument explicit_max_ttl", value=explicit_max_ttl, expected_type=type_hints["explicit_max_ttl"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument no_default_policy", value=no_default_policy, expected_type=type_hints["no_default_policy"])
            check_type(argname="argument no_parent", value=no_parent, expected_type=type_hints["no_parent"])
            check_type(argname="argument num_uses", value=num_uses, expected_type=type_hints["num_uses"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument policies", value=policies, expected_type=type_hints["policies"])
            check_type(argname="argument renewable", value=renewable, expected_type=type_hints["renewable"])
            check_type(argname="argument renew_increment", value=renew_increment, expected_type=type_hints["renew_increment"])
            check_type(argname="argument renew_min_lease", value=renew_min_lease, expected_type=type_hints["renew_min_lease"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument wrapping_ttl", value=wrapping_ttl, expected_type=type_hints["wrapping_ttl"])
        self._values: typing.Dict[str, typing.Any] = {}
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
        if display_name is not None:
            self._values["display_name"] = display_name
        if explicit_max_ttl is not None:
            self._values["explicit_max_ttl"] = explicit_max_ttl
        if id is not None:
            self._values["id"] = id
        if metadata is not None:
            self._values["metadata"] = metadata
        if namespace is not None:
            self._values["namespace"] = namespace
        if no_default_policy is not None:
            self._values["no_default_policy"] = no_default_policy
        if no_parent is not None:
            self._values["no_parent"] = no_parent
        if num_uses is not None:
            self._values["num_uses"] = num_uses
        if period is not None:
            self._values["period"] = period
        if policies is not None:
            self._values["policies"] = policies
        if renewable is not None:
            self._values["renewable"] = renewable
        if renew_increment is not None:
            self._values["renew_increment"] = renew_increment
        if renew_min_lease is not None:
            self._values["renew_min_lease"] = renew_min_lease
        if role_name is not None:
            self._values["role_name"] = role_name
        if ttl is not None:
            self._values["ttl"] = ttl
        if wrapping_ttl is not None:
            self._values["wrapping_ttl"] = wrapping_ttl

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
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#display_name Token#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def explicit_max_ttl(self) -> typing.Optional[builtins.str]:
        '''The explicit max TTL of the token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#explicit_max_ttl Token#explicit_max_ttl}
        '''
        result = self._values.get("explicit_max_ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#id Token#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Metadata to be associated with the token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#metadata Token#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#namespace Token#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def no_default_policy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Flag to disable the default policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#no_default_policy Token#no_default_policy}
        '''
        result = self._values.get("no_default_policy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def no_parent(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Flag to create a token without parent.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#no_parent Token#no_parent}
        '''
        result = self._values.get("no_parent")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def num_uses(self) -> typing.Optional[jsii.Number]:
        '''The number of allowed uses of the token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#num_uses Token#num_uses}
        '''
        result = self._values.get("num_uses")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def period(self) -> typing.Optional[builtins.str]:
        '''The period of the token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#period Token#period}
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of policies.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#policies Token#policies}
        '''
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def renewable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Flag to allow the token to be renewed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#renewable Token#renewable}
        '''
        result = self._values.get("renewable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def renew_increment(self) -> typing.Optional[jsii.Number]:
        '''The renew increment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#renew_increment Token#renew_increment}
        '''
        result = self._values.get("renew_increment")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def renew_min_lease(self) -> typing.Optional[jsii.Number]:
        '''The minimum lease to renew token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#renew_min_lease Token#renew_min_lease}
        '''
        result = self._values.get("renew_min_lease")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role_name(self) -> typing.Optional[builtins.str]:
        '''The token role name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#role_name Token#role_name}
        '''
        result = self._values.get("role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[builtins.str]:
        '''The TTL period of the token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#ttl Token#ttl}
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wrapping_ttl(self) -> typing.Optional[builtins.str]:
        '''The TTL period of the wrapped token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/token#wrapping_ttl Token#wrapping_ttl}
        '''
        result = self._values.get("wrapping_ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TokenConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Token",
    "TokenConfig",
]

publication.publish()
