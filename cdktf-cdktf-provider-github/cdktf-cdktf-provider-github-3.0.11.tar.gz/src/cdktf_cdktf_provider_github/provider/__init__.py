'''
# `provider`

Refer to the Terraform Registory for docs: [`github`](https://www.terraform.io/docs/providers/github).
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


class GithubProvider(
    cdktf.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.provider.GithubProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/github github}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
        app_auth: typing.Optional[typing.Union["GithubProviderAppAuth", typing.Dict[str, typing.Any]]] = None,
        base_url: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        organization: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        read_delay_ms: typing.Optional[jsii.Number] = None,
        token: typing.Optional[builtins.str] = None,
        write_delay_ms: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/github github} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#alias GithubProvider#alias}
        :param app_auth: app_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#app_auth GithubProvider#app_auth}
        :param base_url: The GitHub Base API URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#base_url GithubProvider#base_url}
        :param insecure: Enable ``insecure`` mode for testing purposes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#insecure GithubProvider#insecure}
        :param organization: The GitHub organization name to manage. Use this field instead of ``owner`` when managing organization accounts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#organization GithubProvider#organization}
        :param owner: The GitHub owner name to manage. Use this field instead of ``organization`` when managing individual accounts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#owner GithubProvider#owner}
        :param read_delay_ms: Amount of time in milliseconds to sleep in between non-write requests to GitHub API. Defaults to 0ms if not set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#read_delay_ms GithubProvider#read_delay_ms}
        :param token: The OAuth token used to connect to GitHub. Anonymous mode is enabled if both ``token`` and ``app_auth`` are not set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#token GithubProvider#token}
        :param write_delay_ms: Amount of time in milliseconds to sleep in between writes to GitHub API. Defaults to 1000ms or 1s if not set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#write_delay_ms GithubProvider#write_delay_ms}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GithubProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = GithubProviderConfig(
            alias=alias,
            app_auth=app_auth,
            base_url=base_url,
            insecure=insecure,
            organization=organization,
            owner=owner,
            read_delay_ms=read_delay_ms,
            token=token,
            write_delay_ms=write_delay_ms,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetAppAuth")
    def reset_app_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppAuth", []))

    @jsii.member(jsii_name="resetBaseUrl")
    def reset_base_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaseUrl", []))

    @jsii.member(jsii_name="resetInsecure")
    def reset_insecure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecure", []))

    @jsii.member(jsii_name="resetOrganization")
    def reset_organization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganization", []))

    @jsii.member(jsii_name="resetOwner")
    def reset_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwner", []))

    @jsii.member(jsii_name="resetReadDelayMs")
    def reset_read_delay_ms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadDelayMs", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="resetWriteDelayMs")
    def reset_write_delay_ms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteDelayMs", []))

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
    @jsii.member(jsii_name="appAuthInput")
    def app_auth_input(self) -> typing.Optional["GithubProviderAppAuth"]:
        return typing.cast(typing.Optional["GithubProviderAppAuth"], jsii.get(self, "appAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="baseUrlInput")
    def base_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "baseUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureInput")
    def insecure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "insecureInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationInput")
    def organization_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationInput"))

    @builtins.property
    @jsii.member(jsii_name="ownerInput")
    def owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInput"))

    @builtins.property
    @jsii.member(jsii_name="readDelayMsInput")
    def read_delay_ms_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "readDelayMsInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="writeDelayMsInput")
    def write_delay_ms_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "writeDelayMsInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubProvider, "alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="appAuth")
    def app_auth(self) -> typing.Optional["GithubProviderAppAuth"]:
        return typing.cast(typing.Optional["GithubProviderAppAuth"], jsii.get(self, "appAuth"))

    @app_auth.setter
    def app_auth(self, value: typing.Optional["GithubProviderAppAuth"]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubProvider, "app_auth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appAuth", value)

    @builtins.property
    @jsii.member(jsii_name="baseUrl")
    def base_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "baseUrl"))

    @base_url.setter
    def base_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubProvider, "base_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseUrl", value)

    @builtins.property
    @jsii.member(jsii_name="insecure")
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "insecure"))

    @insecure.setter
    def insecure(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubProvider, "insecure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecure", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubProvider, "organization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "owner"))

    @owner.setter
    def owner(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubProvider, "owner").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value)

    @builtins.property
    @jsii.member(jsii_name="readDelayMs")
    def read_delay_ms(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "readDelayMs"))

    @read_delay_ms.setter
    def read_delay_ms(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubProvider, "read_delay_ms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readDelayMs", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "token"))

    @token.setter
    def token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubProvider, "token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="writeDelayMs")
    def write_delay_ms(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "writeDelayMs"))

    @write_delay_ms.setter
    def write_delay_ms(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubProvider, "write_delay_ms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeDelayMs", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-github.provider.GithubProviderAppAuth",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "installation_id": "installationId",
        "pem_file": "pemFile",
    },
)
class GithubProviderAppAuth:
    def __init__(
        self,
        *,
        id: builtins.str,
        installation_id: builtins.str,
        pem_file: builtins.str,
    ) -> None:
        '''
        :param id: The GitHub App ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#id GithubProvider#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param installation_id: The GitHub App installation instance ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#installation_id GithubProvider#installation_id}
        :param pem_file: The GitHub App PEM file contents. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#pem_file GithubProvider#pem_file}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GithubProviderAppAuth.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument installation_id", value=installation_id, expected_type=type_hints["installation_id"])
            check_type(argname="argument pem_file", value=pem_file, expected_type=type_hints["pem_file"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
            "installation_id": installation_id,
            "pem_file": pem_file,
        }

    @builtins.property
    def id(self) -> builtins.str:
        '''The GitHub App ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#id GithubProvider#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def installation_id(self) -> builtins.str:
        '''The GitHub App installation instance ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#installation_id GithubProvider#installation_id}
        '''
        result = self._values.get("installation_id")
        assert result is not None, "Required property 'installation_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pem_file(self) -> builtins.str:
        '''The GitHub App PEM file contents.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#pem_file GithubProvider#pem_file}
        '''
        result = self._values.get("pem_file")
        assert result is not None, "Required property 'pem_file' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GithubProviderAppAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-github.provider.GithubProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "app_auth": "appAuth",
        "base_url": "baseUrl",
        "insecure": "insecure",
        "organization": "organization",
        "owner": "owner",
        "read_delay_ms": "readDelayMs",
        "token": "token",
        "write_delay_ms": "writeDelayMs",
    },
)
class GithubProviderConfig:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        app_auth: typing.Optional[typing.Union[GithubProviderAppAuth, typing.Dict[str, typing.Any]]] = None,
        base_url: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        organization: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        read_delay_ms: typing.Optional[jsii.Number] = None,
        token: typing.Optional[builtins.str] = None,
        write_delay_ms: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#alias GithubProvider#alias}
        :param app_auth: app_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#app_auth GithubProvider#app_auth}
        :param base_url: The GitHub Base API URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#base_url GithubProvider#base_url}
        :param insecure: Enable ``insecure`` mode for testing purposes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#insecure GithubProvider#insecure}
        :param organization: The GitHub organization name to manage. Use this field instead of ``owner`` when managing organization accounts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#organization GithubProvider#organization}
        :param owner: The GitHub owner name to manage. Use this field instead of ``organization`` when managing individual accounts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#owner GithubProvider#owner}
        :param read_delay_ms: Amount of time in milliseconds to sleep in between non-write requests to GitHub API. Defaults to 0ms if not set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#read_delay_ms GithubProvider#read_delay_ms}
        :param token: The OAuth token used to connect to GitHub. Anonymous mode is enabled if both ``token`` and ``app_auth`` are not set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#token GithubProvider#token}
        :param write_delay_ms: Amount of time in milliseconds to sleep in between writes to GitHub API. Defaults to 1000ms or 1s if not set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#write_delay_ms GithubProvider#write_delay_ms}
        '''
        if isinstance(app_auth, dict):
            app_auth = GithubProviderAppAuth(**app_auth)
        if __debug__:
            type_hints = typing.get_type_hints(GithubProviderConfig.__init__)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument app_auth", value=app_auth, expected_type=type_hints["app_auth"])
            check_type(argname="argument base_url", value=base_url, expected_type=type_hints["base_url"])
            check_type(argname="argument insecure", value=insecure, expected_type=type_hints["insecure"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
            check_type(argname="argument read_delay_ms", value=read_delay_ms, expected_type=type_hints["read_delay_ms"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument write_delay_ms", value=write_delay_ms, expected_type=type_hints["write_delay_ms"])
        self._values: typing.Dict[str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
        if app_auth is not None:
            self._values["app_auth"] = app_auth
        if base_url is not None:
            self._values["base_url"] = base_url
        if insecure is not None:
            self._values["insecure"] = insecure
        if organization is not None:
            self._values["organization"] = organization
        if owner is not None:
            self._values["owner"] = owner
        if read_delay_ms is not None:
            self._values["read_delay_ms"] = read_delay_ms
        if token is not None:
            self._values["token"] = token
        if write_delay_ms is not None:
            self._values["write_delay_ms"] = write_delay_ms

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#alias GithubProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def app_auth(self) -> typing.Optional[GithubProviderAppAuth]:
        '''app_auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#app_auth GithubProvider#app_auth}
        '''
        result = self._values.get("app_auth")
        return typing.cast(typing.Optional[GithubProviderAppAuth], result)

    @builtins.property
    def base_url(self) -> typing.Optional[builtins.str]:
        '''The GitHub Base API URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#base_url GithubProvider#base_url}
        '''
        result = self._values.get("base_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable ``insecure`` mode for testing purposes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#insecure GithubProvider#insecure}
        '''
        result = self._values.get("insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def organization(self) -> typing.Optional[builtins.str]:
        '''The GitHub organization name to manage. Use this field instead of ``owner`` when managing organization accounts.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#organization GithubProvider#organization}
        '''
        result = self._values.get("organization")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner(self) -> typing.Optional[builtins.str]:
        '''The GitHub owner name to manage. Use this field instead of ``organization`` when managing individual accounts.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#owner GithubProvider#owner}
        '''
        result = self._values.get("owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_delay_ms(self) -> typing.Optional[jsii.Number]:
        '''Amount of time in milliseconds to sleep in between non-write requests to GitHub API.

        Defaults to 0ms if not set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#read_delay_ms GithubProvider#read_delay_ms}
        '''
        result = self._values.get("read_delay_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''The OAuth token used to connect to GitHub.

        Anonymous mode is enabled if both ``token`` and ``app_auth`` are not set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#token GithubProvider#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def write_delay_ms(self) -> typing.Optional[jsii.Number]:
        '''Amount of time in milliseconds to sleep in between writes to GitHub API.

        Defaults to 1000ms or 1s if not set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github#write_delay_ms GithubProvider#write_delay_ms}
        '''
        result = self._values.get("write_delay_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GithubProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GithubProvider",
    "GithubProviderAppAuth",
    "GithubProviderConfig",
]

publication.publish()
