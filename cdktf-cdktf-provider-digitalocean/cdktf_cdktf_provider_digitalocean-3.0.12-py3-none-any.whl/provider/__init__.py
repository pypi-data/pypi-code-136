'''
# `provider`

Refer to the Terraform Registory for docs: [`digitalocean`](https://www.terraform.io/docs/providers/digitalocean).
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


class DigitaloceanProvider(
    cdktf.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.provider.DigitaloceanProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/digitalocean digitalocean}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
        api_endpoint: typing.Optional[builtins.str] = None,
        spaces_access_id: typing.Optional[builtins.str] = None,
        spaces_endpoint: typing.Optional[builtins.str] = None,
        spaces_secret_key: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/digitalocean digitalocean} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#alias DigitaloceanProvider#alias}
        :param api_endpoint: The URL to use for the DigitalOcean API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#api_endpoint DigitaloceanProvider#api_endpoint}
        :param spaces_access_id: The access key ID for Spaces API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#spaces_access_id DigitaloceanProvider#spaces_access_id}
        :param spaces_endpoint: The URL to use for the DigitalOcean Spaces API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#spaces_endpoint DigitaloceanProvider#spaces_endpoint}
        :param spaces_secret_key: The secret access key for Spaces API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#spaces_secret_key DigitaloceanProvider#spaces_secret_key}
        :param token: The token key for API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#token DigitaloceanProvider#token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DigitaloceanProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DigitaloceanProviderConfig(
            alias=alias,
            api_endpoint=api_endpoint,
            spaces_access_id=spaces_access_id,
            spaces_endpoint=spaces_endpoint,
            spaces_secret_key=spaces_secret_key,
            token=token,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetApiEndpoint")
    def reset_api_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiEndpoint", []))

    @jsii.member(jsii_name="resetSpacesAccessId")
    def reset_spaces_access_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpacesAccessId", []))

    @jsii.member(jsii_name="resetSpacesEndpoint")
    def reset_spaces_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpacesEndpoint", []))

    @jsii.member(jsii_name="resetSpacesSecretKey")
    def reset_spaces_secret_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpacesSecretKey", []))

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
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="apiEndpointInput")
    def api_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="spacesAccessIdInput")
    def spaces_access_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spacesAccessIdInput"))

    @builtins.property
    @jsii.member(jsii_name="spacesEndpointInput")
    def spaces_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spacesEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="spacesSecretKeyInput")
    def spaces_secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spacesSecretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DigitaloceanProvider, "alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="apiEndpoint")
    def api_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiEndpoint"))

    @api_endpoint.setter
    def api_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DigitaloceanProvider, "api_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="spacesAccessId")
    def spaces_access_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spacesAccessId"))

    @spaces_access_id.setter
    def spaces_access_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DigitaloceanProvider, "spaces_access_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spacesAccessId", value)

    @builtins.property
    @jsii.member(jsii_name="spacesEndpoint")
    def spaces_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spacesEndpoint"))

    @spaces_endpoint.setter
    def spaces_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DigitaloceanProvider, "spaces_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spacesEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="spacesSecretKey")
    def spaces_secret_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spacesSecretKey"))

    @spaces_secret_key.setter
    def spaces_secret_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DigitaloceanProvider, "spaces_secret_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spacesSecretKey", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "token"))

    @token.setter
    def token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DigitaloceanProvider, "token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.provider.DigitaloceanProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "api_endpoint": "apiEndpoint",
        "spaces_access_id": "spacesAccessId",
        "spaces_endpoint": "spacesEndpoint",
        "spaces_secret_key": "spacesSecretKey",
        "token": "token",
    },
)
class DigitaloceanProviderConfig:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        api_endpoint: typing.Optional[builtins.str] = None,
        spaces_access_id: typing.Optional[builtins.str] = None,
        spaces_endpoint: typing.Optional[builtins.str] = None,
        spaces_secret_key: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#alias DigitaloceanProvider#alias}
        :param api_endpoint: The URL to use for the DigitalOcean API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#api_endpoint DigitaloceanProvider#api_endpoint}
        :param spaces_access_id: The access key ID for Spaces API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#spaces_access_id DigitaloceanProvider#spaces_access_id}
        :param spaces_endpoint: The URL to use for the DigitalOcean Spaces API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#spaces_endpoint DigitaloceanProvider#spaces_endpoint}
        :param spaces_secret_key: The secret access key for Spaces API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#spaces_secret_key DigitaloceanProvider#spaces_secret_key}
        :param token: The token key for API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#token DigitaloceanProvider#token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DigitaloceanProviderConfig.__init__)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument api_endpoint", value=api_endpoint, expected_type=type_hints["api_endpoint"])
            check_type(argname="argument spaces_access_id", value=spaces_access_id, expected_type=type_hints["spaces_access_id"])
            check_type(argname="argument spaces_endpoint", value=spaces_endpoint, expected_type=type_hints["spaces_endpoint"])
            check_type(argname="argument spaces_secret_key", value=spaces_secret_key, expected_type=type_hints["spaces_secret_key"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
        self._values: typing.Dict[str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
        if api_endpoint is not None:
            self._values["api_endpoint"] = api_endpoint
        if spaces_access_id is not None:
            self._values["spaces_access_id"] = spaces_access_id
        if spaces_endpoint is not None:
            self._values["spaces_endpoint"] = spaces_endpoint
        if spaces_secret_key is not None:
            self._values["spaces_secret_key"] = spaces_secret_key
        if token is not None:
            self._values["token"] = token

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#alias DigitaloceanProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_endpoint(self) -> typing.Optional[builtins.str]:
        '''The URL to use for the DigitalOcean API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#api_endpoint DigitaloceanProvider#api_endpoint}
        '''
        result = self._values.get("api_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spaces_access_id(self) -> typing.Optional[builtins.str]:
        '''The access key ID for Spaces API operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#spaces_access_id DigitaloceanProvider#spaces_access_id}
        '''
        result = self._values.get("spaces_access_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spaces_endpoint(self) -> typing.Optional[builtins.str]:
        '''The URL to use for the DigitalOcean Spaces API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#spaces_endpoint DigitaloceanProvider#spaces_endpoint}
        '''
        result = self._values.get("spaces_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spaces_secret_key(self) -> typing.Optional[builtins.str]:
        '''The secret access key for Spaces API operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#spaces_secret_key DigitaloceanProvider#spaces_secret_key}
        '''
        result = self._values.get("spaces_secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''The token key for API operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean#token DigitaloceanProvider#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DigitaloceanProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DigitaloceanProvider",
    "DigitaloceanProviderConfig",
]

publication.publish()
