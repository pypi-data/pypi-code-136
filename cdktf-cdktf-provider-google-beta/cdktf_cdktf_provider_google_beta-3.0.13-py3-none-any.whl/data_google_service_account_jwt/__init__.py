'''
# `data_google_service_account_jwt`

Refer to the Terraform Registory for docs: [`data_google_service_account_jwt`](https://www.terraform.io/docs/providers/google-beta/d/google_service_account_jwt).
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


class DataGoogleServiceAccountJwt(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleServiceAccountJwt.DataGoogleServiceAccountJwt",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/d/google_service_account_jwt google_service_account_jwt}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        payload: builtins.str,
        target_service_account: builtins.str,
        delegates: typing.Optional[typing.Sequence[builtins.str]] = None,
        expires_in: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/d/google_service_account_jwt google_service_account_jwt} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param payload: A JSON-encoded JWT claims set that will be included in the signed JWT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_service_account_jwt#payload DataGoogleServiceAccountJwt#payload}
        :param target_service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_service_account_jwt#target_service_account DataGoogleServiceAccountJwt#target_service_account}.
        :param delegates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_service_account_jwt#delegates DataGoogleServiceAccountJwt#delegates}.
        :param expires_in: Number of seconds until the JWT expires. If set and non-zero an ``exp`` claim will be added to the payload derived from the current timestamp plus expires_in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_service_account_jwt#expires_in DataGoogleServiceAccountJwt#expires_in}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_service_account_jwt#id DataGoogleServiceAccountJwt#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleServiceAccountJwt.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataGoogleServiceAccountJwtConfig(
            payload=payload,
            target_service_account=target_service_account,
            delegates=delegates,
            expires_in=expires_in,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDelegates")
    def reset_delegates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelegates", []))

    @jsii.member(jsii_name="resetExpiresIn")
    def reset_expires_in(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpiresIn", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="jwt")
    def jwt(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jwt"))

    @builtins.property
    @jsii.member(jsii_name="delegatesInput")
    def delegates_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "delegatesInput"))

    @builtins.property
    @jsii.member(jsii_name="expiresInInput")
    def expires_in_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expiresInInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadInput")
    def payload_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "payloadInput"))

    @builtins.property
    @jsii.member(jsii_name="targetServiceAccountInput")
    def target_service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetServiceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="delegates")
    def delegates(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "delegates"))

    @delegates.setter
    def delegates(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleServiceAccountJwt, "delegates").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delegates", value)

    @builtins.property
    @jsii.member(jsii_name="expiresIn")
    def expires_in(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "expiresIn"))

    @expires_in.setter
    def expires_in(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleServiceAccountJwt, "expires_in").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiresIn", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleServiceAccountJwt, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="payload")
    def payload(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "payload"))

    @payload.setter
    def payload(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleServiceAccountJwt, "payload").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payload", value)

    @builtins.property
    @jsii.member(jsii_name="targetServiceAccount")
    def target_service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetServiceAccount"))

    @target_service_account.setter
    def target_service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleServiceAccountJwt, "target_service_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetServiceAccount", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleServiceAccountJwt.DataGoogleServiceAccountJwtConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "payload": "payload",
        "target_service_account": "targetServiceAccount",
        "delegates": "delegates",
        "expires_in": "expiresIn",
        "id": "id",
    },
)
class DataGoogleServiceAccountJwtConfig(cdktf.TerraformMetaArguments):
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
        payload: builtins.str,
        target_service_account: builtins.str,
        delegates: typing.Optional[typing.Sequence[builtins.str]] = None,
        expires_in: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param payload: A JSON-encoded JWT claims set that will be included in the signed JWT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_service_account_jwt#payload DataGoogleServiceAccountJwt#payload}
        :param target_service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_service_account_jwt#target_service_account DataGoogleServiceAccountJwt#target_service_account}.
        :param delegates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_service_account_jwt#delegates DataGoogleServiceAccountJwt#delegates}.
        :param expires_in: Number of seconds until the JWT expires. If set and non-zero an ``exp`` claim will be added to the payload derived from the current timestamp plus expires_in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_service_account_jwt#expires_in DataGoogleServiceAccountJwt#expires_in}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_service_account_jwt#id DataGoogleServiceAccountJwt#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleServiceAccountJwtConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            check_type(argname="argument target_service_account", value=target_service_account, expected_type=type_hints["target_service_account"])
            check_type(argname="argument delegates", value=delegates, expected_type=type_hints["delegates"])
            check_type(argname="argument expires_in", value=expires_in, expected_type=type_hints["expires_in"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "payload": payload,
            "target_service_account": target_service_account,
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
        if delegates is not None:
            self._values["delegates"] = delegates
        if expires_in is not None:
            self._values["expires_in"] = expires_in
        if id is not None:
            self._values["id"] = id

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
    def payload(self) -> builtins.str:
        '''A JSON-encoded JWT claims set that will be included in the signed JWT.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_service_account_jwt#payload DataGoogleServiceAccountJwt#payload}
        '''
        result = self._values.get("payload")
        assert result is not None, "Required property 'payload' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_service_account(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_service_account_jwt#target_service_account DataGoogleServiceAccountJwt#target_service_account}.'''
        result = self._values.get("target_service_account")
        assert result is not None, "Required property 'target_service_account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delegates(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_service_account_jwt#delegates DataGoogleServiceAccountJwt#delegates}.'''
        result = self._values.get("delegates")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def expires_in(self) -> typing.Optional[jsii.Number]:
        '''Number of seconds until the JWT expires.

        If set and non-zero an ``exp`` claim will be added to the payload derived from the current timestamp plus expires_in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_service_account_jwt#expires_in DataGoogleServiceAccountJwt#expires_in}
        '''
        result = self._values.get("expires_in")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_service_account_jwt#id DataGoogleServiceAccountJwt#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleServiceAccountJwtConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataGoogleServiceAccountJwt",
    "DataGoogleServiceAccountJwtConfig",
]

publication.publish()
