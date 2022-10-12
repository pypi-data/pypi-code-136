'''
# `snowflake_oauth_integration`

Refer to the Terraform Registory for docs: [`snowflake_oauth_integration`](https://www.terraform.io/docs/providers/snowflake/r/oauth_integration).
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


class OauthIntegration(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.oauthIntegration.OauthIntegration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration snowflake_oauth_integration}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        oauth_client: builtins.str,
        blocked_roles_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        comment: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        oauth_issue_refresh_tokens: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        oauth_refresh_token_validity: typing.Optional[jsii.Number] = None,
        oauth_use_secondary_roles: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration snowflake_oauth_integration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Specifies the name of the OAuth integration. This name follows the rules for Object Identifiers. The name should be unique among security integrations in your account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#name OauthIntegration#name}
        :param oauth_client: Specifies the OAuth client type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#oauth_client OauthIntegration#oauth_client}
        :param blocked_roles_list: List of roles that a user cannot explicitly consent to using after authenticating. Do not include ACCOUNTADMIN, ORGADMIN or SECURITYADMIN as they are already implicitly enforced and will cause in-place updates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#blocked_roles_list OauthIntegration#blocked_roles_list}
        :param comment: Specifies a comment for the OAuth integration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#comment OauthIntegration#comment}
        :param enabled: Specifies whether this OAuth integration is enabled or disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#enabled OauthIntegration#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#id OauthIntegration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param oauth_issue_refresh_tokens: Specifies whether to allow the client to exchange a refresh token for an access token when the current access token has expired. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#oauth_issue_refresh_tokens OauthIntegration#oauth_issue_refresh_tokens}
        :param oauth_refresh_token_validity: Specifies how long refresh tokens should be valid (in seconds). OAUTH_ISSUE_REFRESH_TOKENS must be set to TRUE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#oauth_refresh_token_validity OauthIntegration#oauth_refresh_token_validity}
        :param oauth_use_secondary_roles: Specifies whether default secondary roles set in the user properties are activated by default in the session being opened. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#oauth_use_secondary_roles OauthIntegration#oauth_use_secondary_roles}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OauthIntegration.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OauthIntegrationConfig(
            name=name,
            oauth_client=oauth_client,
            blocked_roles_list=blocked_roles_list,
            comment=comment,
            enabled=enabled,
            id=id,
            oauth_issue_refresh_tokens=oauth_issue_refresh_tokens,
            oauth_refresh_token_validity=oauth_refresh_token_validity,
            oauth_use_secondary_roles=oauth_use_secondary_roles,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetBlockedRolesList")
    def reset_blocked_roles_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockedRolesList", []))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOauthIssueRefreshTokens")
    def reset_oauth_issue_refresh_tokens(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthIssueRefreshTokens", []))

    @jsii.member(jsii_name="resetOauthRefreshTokenValidity")
    def reset_oauth_refresh_token_validity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRefreshTokenValidity", []))

    @jsii.member(jsii_name="resetOauthUseSecondaryRoles")
    def reset_oauth_use_secondary_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthUseSecondaryRoles", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="createdOn")
    def created_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdOn"))

    @builtins.property
    @jsii.member(jsii_name="blockedRolesListInput")
    def blocked_roles_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "blockedRolesListInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

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
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthClientInput")
    def oauth_client_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthClientInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthIssueRefreshTokensInput")
    def oauth_issue_refresh_tokens_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "oauthIssueRefreshTokensInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRefreshTokenValidityInput")
    def oauth_refresh_token_validity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "oauthRefreshTokenValidityInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthUseSecondaryRolesInput")
    def oauth_use_secondary_roles_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthUseSecondaryRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="blockedRolesList")
    def blocked_roles_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "blockedRolesList"))

    @blocked_roles_list.setter
    def blocked_roles_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OauthIntegration, "blocked_roles_list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockedRolesList", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OauthIntegration, "comment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OauthIntegration, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OauthIntegration, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OauthIntegration, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="oauthClient")
    def oauth_client(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauthClient"))

    @oauth_client.setter
    def oauth_client(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OauthIntegration, "oauth_client").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthClient", value)

    @builtins.property
    @jsii.member(jsii_name="oauthIssueRefreshTokens")
    def oauth_issue_refresh_tokens(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "oauthIssueRefreshTokens"))

    @oauth_issue_refresh_tokens.setter
    def oauth_issue_refresh_tokens(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OauthIntegration, "oauth_issue_refresh_tokens").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthIssueRefreshTokens", value)

    @builtins.property
    @jsii.member(jsii_name="oauthRefreshTokenValidity")
    def oauth_refresh_token_validity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "oauthRefreshTokenValidity"))

    @oauth_refresh_token_validity.setter
    def oauth_refresh_token_validity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OauthIntegration, "oauth_refresh_token_validity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthRefreshTokenValidity", value)

    @builtins.property
    @jsii.member(jsii_name="oauthUseSecondaryRoles")
    def oauth_use_secondary_roles(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauthUseSecondaryRoles"))

    @oauth_use_secondary_roles.setter
    def oauth_use_secondary_roles(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OauthIntegration, "oauth_use_secondary_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthUseSecondaryRoles", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.oauthIntegration.OauthIntegrationConfig",
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
        "oauth_client": "oauthClient",
        "blocked_roles_list": "blockedRolesList",
        "comment": "comment",
        "enabled": "enabled",
        "id": "id",
        "oauth_issue_refresh_tokens": "oauthIssueRefreshTokens",
        "oauth_refresh_token_validity": "oauthRefreshTokenValidity",
        "oauth_use_secondary_roles": "oauthUseSecondaryRoles",
    },
)
class OauthIntegrationConfig(cdktf.TerraformMetaArguments):
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
        oauth_client: builtins.str,
        blocked_roles_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        comment: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        oauth_issue_refresh_tokens: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        oauth_refresh_token_validity: typing.Optional[jsii.Number] = None,
        oauth_use_secondary_roles: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Specifies the name of the OAuth integration. This name follows the rules for Object Identifiers. The name should be unique among security integrations in your account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#name OauthIntegration#name}
        :param oauth_client: Specifies the OAuth client type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#oauth_client OauthIntegration#oauth_client}
        :param blocked_roles_list: List of roles that a user cannot explicitly consent to using after authenticating. Do not include ACCOUNTADMIN, ORGADMIN or SECURITYADMIN as they are already implicitly enforced and will cause in-place updates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#blocked_roles_list OauthIntegration#blocked_roles_list}
        :param comment: Specifies a comment for the OAuth integration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#comment OauthIntegration#comment}
        :param enabled: Specifies whether this OAuth integration is enabled or disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#enabled OauthIntegration#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#id OauthIntegration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param oauth_issue_refresh_tokens: Specifies whether to allow the client to exchange a refresh token for an access token when the current access token has expired. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#oauth_issue_refresh_tokens OauthIntegration#oauth_issue_refresh_tokens}
        :param oauth_refresh_token_validity: Specifies how long refresh tokens should be valid (in seconds). OAUTH_ISSUE_REFRESH_TOKENS must be set to TRUE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#oauth_refresh_token_validity OauthIntegration#oauth_refresh_token_validity}
        :param oauth_use_secondary_roles: Specifies whether default secondary roles set in the user properties are activated by default in the session being opened. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#oauth_use_secondary_roles OauthIntegration#oauth_use_secondary_roles}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(OauthIntegrationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument oauth_client", value=oauth_client, expected_type=type_hints["oauth_client"])
            check_type(argname="argument blocked_roles_list", value=blocked_roles_list, expected_type=type_hints["blocked_roles_list"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument oauth_issue_refresh_tokens", value=oauth_issue_refresh_tokens, expected_type=type_hints["oauth_issue_refresh_tokens"])
            check_type(argname="argument oauth_refresh_token_validity", value=oauth_refresh_token_validity, expected_type=type_hints["oauth_refresh_token_validity"])
            check_type(argname="argument oauth_use_secondary_roles", value=oauth_use_secondary_roles, expected_type=type_hints["oauth_use_secondary_roles"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "oauth_client": oauth_client,
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
        if blocked_roles_list is not None:
            self._values["blocked_roles_list"] = blocked_roles_list
        if comment is not None:
            self._values["comment"] = comment
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if oauth_issue_refresh_tokens is not None:
            self._values["oauth_issue_refresh_tokens"] = oauth_issue_refresh_tokens
        if oauth_refresh_token_validity is not None:
            self._values["oauth_refresh_token_validity"] = oauth_refresh_token_validity
        if oauth_use_secondary_roles is not None:
            self._values["oauth_use_secondary_roles"] = oauth_use_secondary_roles

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
        '''Specifies the name of the OAuth integration.

        This name follows the rules for Object Identifiers. The name should be unique among security integrations in your account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#name OauthIntegration#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oauth_client(self) -> builtins.str:
        '''Specifies the OAuth client type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#oauth_client OauthIntegration#oauth_client}
        '''
        result = self._values.get("oauth_client")
        assert result is not None, "Required property 'oauth_client' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def blocked_roles_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of roles that a user cannot explicitly consent to using after authenticating.

        Do not include ACCOUNTADMIN, ORGADMIN or SECURITYADMIN as they are already implicitly enforced and will cause in-place updates.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#blocked_roles_list OauthIntegration#blocked_roles_list}
        '''
        result = self._values.get("blocked_roles_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Specifies a comment for the OAuth integration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#comment OauthIntegration#comment}
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether this OAuth integration is enabled or disabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#enabled OauthIntegration#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#id OauthIntegration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_issue_refresh_tokens(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether to allow the client to exchange a refresh token for an access token when the current access token has expired.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#oauth_issue_refresh_tokens OauthIntegration#oauth_issue_refresh_tokens}
        '''
        result = self._values.get("oauth_issue_refresh_tokens")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def oauth_refresh_token_validity(self) -> typing.Optional[jsii.Number]:
        '''Specifies how long refresh tokens should be valid (in seconds). OAUTH_ISSUE_REFRESH_TOKENS must be set to TRUE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#oauth_refresh_token_validity OauthIntegration#oauth_refresh_token_validity}
        '''
        result = self._values.get("oauth_refresh_token_validity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def oauth_use_secondary_roles(self) -> typing.Optional[builtins.str]:
        '''Specifies whether default secondary roles set in the user properties are activated by default in the session being opened.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/oauth_integration#oauth_use_secondary_roles OauthIntegration#oauth_use_secondary_roles}
        '''
        result = self._values.get("oauth_use_secondary_roles")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OauthIntegrationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "OauthIntegration",
    "OauthIntegrationConfig",
]

publication.publish()
