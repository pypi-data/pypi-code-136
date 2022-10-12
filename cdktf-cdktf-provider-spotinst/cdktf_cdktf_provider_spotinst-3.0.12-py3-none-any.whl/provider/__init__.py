'''
# `provider`

Refer to the Terraform Registory for docs: [`spotinst`](https://www.terraform.io/docs/providers/spotinst).
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


class SpotinstProvider(
    cdktf.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.provider.SpotinstProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/spotinst spotinst}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        feature_flags: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/spotinst spotinst} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account: Spotinst Account ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst#account SpotinstProvider#account}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst#alias SpotinstProvider#alias}
        :param feature_flags: Spotinst SDK Feature Flags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst#feature_flags SpotinstProvider#feature_flags}
        :param token: Spotinst Personal API Access Token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst#token SpotinstProvider#token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpotinstProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = SpotinstProviderConfig(
            account=account, alias=alias, feature_flags=feature_flags, token=token
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAccount")
    def reset_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccount", []))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetFeatureFlags")
    def reset_feature_flags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFeatureFlags", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accountInput")
    def account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="featureFlagsInput")
    def feature_flags_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "featureFlagsInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="account")
    def account(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "account"))

    @account.setter
    def account(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpotinstProvider, "account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "account", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpotinstProvider, "alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="featureFlags")
    def feature_flags(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "featureFlags"))

    @feature_flags.setter
    def feature_flags(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpotinstProvider, "feature_flags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "featureFlags", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "token"))

    @token.setter
    def token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpotinstProvider, "token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.provider.SpotinstProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "alias": "alias",
        "feature_flags": "featureFlags",
        "token": "token",
    },
)
class SpotinstProviderConfig:
    def __init__(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        feature_flags: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account: Spotinst Account ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst#account SpotinstProvider#account}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst#alias SpotinstProvider#alias}
        :param feature_flags: Spotinst SDK Feature Flags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst#feature_flags SpotinstProvider#feature_flags}
        :param token: Spotinst Personal API Access Token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst#token SpotinstProvider#token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpotinstProviderConfig.__init__)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument feature_flags", value=feature_flags, expected_type=type_hints["feature_flags"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
        self._values: typing.Dict[str, typing.Any] = {}
        if account is not None:
            self._values["account"] = account
        if alias is not None:
            self._values["alias"] = alias
        if feature_flags is not None:
            self._values["feature_flags"] = feature_flags
        if token is not None:
            self._values["token"] = token

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''Spotinst Account ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst#account SpotinstProvider#account}
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst#alias SpotinstProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def feature_flags(self) -> typing.Optional[builtins.str]:
        '''Spotinst SDK Feature Flags.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst#feature_flags SpotinstProvider#feature_flags}
        '''
        result = self._values.get("feature_flags")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''Spotinst Personal API Access Token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst#token SpotinstProvider#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpotinstProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SpotinstProvider",
    "SpotinstProviderConfig",
]

publication.publish()
