'''
# `provider`

Refer to the Terraform Registory for docs: [`upcloud`](https://www.terraform.io/docs/providers/upcloud).
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


class UpcloudProvider(
    cdktf.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.provider.UpcloudProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/upcloud upcloud}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        password: builtins.str,
        username: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        retry_max: typing.Optional[jsii.Number] = None,
        retry_wait_max_sec: typing.Optional[jsii.Number] = None,
        retry_wait_min_sec: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/upcloud upcloud} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param password: Password for UpCloud API user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud#password UpcloudProvider#password}
        :param username: UpCloud username with API access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud#username UpcloudProvider#username}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud#alias UpcloudProvider#alias}
        :param retry_max: Maximum number of retries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud#retry_max UpcloudProvider#retry_max}
        :param retry_wait_max_sec: Maximum time to wait between retries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud#retry_wait_max_sec UpcloudProvider#retry_wait_max_sec}
        :param retry_wait_min_sec: Minimum time to wait between retries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud#retry_wait_min_sec UpcloudProvider#retry_wait_min_sec}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UpcloudProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = UpcloudProviderConfig(
            password=password,
            username=username,
            alias=alias,
            retry_max=retry_max,
            retry_wait_max_sec=retry_wait_max_sec,
            retry_wait_min_sec=retry_wait_min_sec,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetRetryMax")
    def reset_retry_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryMax", []))

    @jsii.member(jsii_name="resetRetryWaitMaxSec")
    def reset_retry_wait_max_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryWaitMaxSec", []))

    @jsii.member(jsii_name="resetRetryWaitMinSec")
    def reset_retry_wait_min_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryWaitMinSec", []))

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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="retryMaxInput")
    def retry_max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryMaxInput"))

    @builtins.property
    @jsii.member(jsii_name="retryWaitMaxSecInput")
    def retry_wait_max_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryWaitMaxSecInput"))

    @builtins.property
    @jsii.member(jsii_name="retryWaitMinSecInput")
    def retry_wait_min_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryWaitMinSecInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UpcloudProvider, "alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UpcloudProvider, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="retryMax")
    def retry_max(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryMax"))

    @retry_max.setter
    def retry_max(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UpcloudProvider, "retry_max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryMax", value)

    @builtins.property
    @jsii.member(jsii_name="retryWaitMaxSec")
    def retry_wait_max_sec(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryWaitMaxSec"))

    @retry_wait_max_sec.setter
    def retry_wait_max_sec(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UpcloudProvider, "retry_wait_max_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryWaitMaxSec", value)

    @builtins.property
    @jsii.member(jsii_name="retryWaitMinSec")
    def retry_wait_min_sec(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryWaitMinSec"))

    @retry_wait_min_sec.setter
    def retry_wait_min_sec(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UpcloudProvider, "retry_wait_min_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryWaitMinSec", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "username"))

    @username.setter
    def username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(UpcloudProvider, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.provider.UpcloudProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "password": "password",
        "username": "username",
        "alias": "alias",
        "retry_max": "retryMax",
        "retry_wait_max_sec": "retryWaitMaxSec",
        "retry_wait_min_sec": "retryWaitMinSec",
    },
)
class UpcloudProviderConfig:
    def __init__(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        retry_max: typing.Optional[jsii.Number] = None,
        retry_wait_max_sec: typing.Optional[jsii.Number] = None,
        retry_wait_min_sec: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param password: Password for UpCloud API user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud#password UpcloudProvider#password}
        :param username: UpCloud username with API access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud#username UpcloudProvider#username}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud#alias UpcloudProvider#alias}
        :param retry_max: Maximum number of retries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud#retry_max UpcloudProvider#retry_max}
        :param retry_wait_max_sec: Maximum time to wait between retries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud#retry_wait_max_sec UpcloudProvider#retry_wait_max_sec}
        :param retry_wait_min_sec: Minimum time to wait between retries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud#retry_wait_min_sec UpcloudProvider#retry_wait_min_sec}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UpcloudProviderConfig.__init__)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument retry_max", value=retry_max, expected_type=type_hints["retry_max"])
            check_type(argname="argument retry_wait_max_sec", value=retry_wait_max_sec, expected_type=type_hints["retry_wait_max_sec"])
            check_type(argname="argument retry_wait_min_sec", value=retry_wait_min_sec, expected_type=type_hints["retry_wait_min_sec"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }
        if alias is not None:
            self._values["alias"] = alias
        if retry_max is not None:
            self._values["retry_max"] = retry_max
        if retry_wait_max_sec is not None:
            self._values["retry_wait_max_sec"] = retry_wait_max_sec
        if retry_wait_min_sec is not None:
            self._values["retry_wait_min_sec"] = retry_wait_min_sec

    @builtins.property
    def password(self) -> builtins.str:
        '''Password for UpCloud API user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud#password UpcloudProvider#password}
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''UpCloud username with API access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud#username UpcloudProvider#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud#alias UpcloudProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retry_max(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of retries.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud#retry_max UpcloudProvider#retry_max}
        '''
        result = self._values.get("retry_max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def retry_wait_max_sec(self) -> typing.Optional[jsii.Number]:
        '''Maximum time to wait between retries.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud#retry_wait_max_sec UpcloudProvider#retry_wait_max_sec}
        '''
        result = self._values.get("retry_wait_max_sec")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def retry_wait_min_sec(self) -> typing.Optional[jsii.Number]:
        '''Minimum time to wait between retries.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud#retry_wait_min_sec UpcloudProvider#retry_wait_min_sec}
        '''
        result = self._values.get("retry_wait_min_sec")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpcloudProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "UpcloudProvider",
    "UpcloudProviderConfig",
]

publication.publish()
