'''
# `acme_registration`

Refer to the Terraform Registory for docs: [`acme_registration`](https://www.terraform.io/docs/providers/acme/r/registration).
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


class Registration(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-acme.registration.Registration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/acme/r/registration acme_registration}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        account_key_pem: builtins.str,
        email_address: builtins.str,
        external_account_binding: typing.Optional[typing.Union["RegistrationExternalAccountBinding", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/acme/r/registration acme_registration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_key_pem: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme/r/registration#account_key_pem Registration#account_key_pem}.
        :param email_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme/r/registration#email_address Registration#email_address}.
        :param external_account_binding: external_account_binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme/r/registration#external_account_binding Registration#external_account_binding}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme/r/registration#id Registration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Registration.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RegistrationConfig(
            account_key_pem=account_key_pem,
            email_address=email_address,
            external_account_binding=external_account_binding,
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

    @jsii.member(jsii_name="putExternalAccountBinding")
    def put_external_account_binding(
        self,
        *,
        hmac_base64: builtins.str,
        key_id: builtins.str,
    ) -> None:
        '''
        :param hmac_base64: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme/r/registration#hmac_base64 Registration#hmac_base64}.
        :param key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme/r/registration#key_id Registration#key_id}.
        '''
        value = RegistrationExternalAccountBinding(
            hmac_base64=hmac_base64, key_id=key_id
        )

        return typing.cast(None, jsii.invoke(self, "putExternalAccountBinding", [value]))

    @jsii.member(jsii_name="resetExternalAccountBinding")
    def reset_external_account_binding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalAccountBinding", []))

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
    @jsii.member(jsii_name="externalAccountBinding")
    def external_account_binding(
        self,
    ) -> "RegistrationExternalAccountBindingOutputReference":
        return typing.cast("RegistrationExternalAccountBindingOutputReference", jsii.get(self, "externalAccountBinding"))

    @builtins.property
    @jsii.member(jsii_name="registrationUrl")
    def registration_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registrationUrl"))

    @builtins.property
    @jsii.member(jsii_name="accountKeyPemInput")
    def account_key_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountKeyPemInput"))

    @builtins.property
    @jsii.member(jsii_name="emailAddressInput")
    def email_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="externalAccountBindingInput")
    def external_account_binding_input(
        self,
    ) -> typing.Optional["RegistrationExternalAccountBinding"]:
        return typing.cast(typing.Optional["RegistrationExternalAccountBinding"], jsii.get(self, "externalAccountBindingInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="accountKeyPem")
    def account_key_pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountKeyPem"))

    @account_key_pem.setter
    def account_key_pem(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Registration, "account_key_pem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountKeyPem", value)

    @builtins.property
    @jsii.member(jsii_name="emailAddress")
    def email_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailAddress"))

    @email_address.setter
    def email_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Registration, "email_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailAddress", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Registration, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-acme.registration.RegistrationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_key_pem": "accountKeyPem",
        "email_address": "emailAddress",
        "external_account_binding": "externalAccountBinding",
        "id": "id",
    },
)
class RegistrationConfig(cdktf.TerraformMetaArguments):
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
        account_key_pem: builtins.str,
        email_address: builtins.str,
        external_account_binding: typing.Optional[typing.Union["RegistrationExternalAccountBinding", typing.Dict[str, typing.Any]]] = None,
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
        :param account_key_pem: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme/r/registration#account_key_pem Registration#account_key_pem}.
        :param email_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme/r/registration#email_address Registration#email_address}.
        :param external_account_binding: external_account_binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme/r/registration#external_account_binding Registration#external_account_binding}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme/r/registration#id Registration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(external_account_binding, dict):
            external_account_binding = RegistrationExternalAccountBinding(**external_account_binding)
        if __debug__:
            type_hints = typing.get_type_hints(RegistrationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_key_pem", value=account_key_pem, expected_type=type_hints["account_key_pem"])
            check_type(argname="argument email_address", value=email_address, expected_type=type_hints["email_address"])
            check_type(argname="argument external_account_binding", value=external_account_binding, expected_type=type_hints["external_account_binding"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_key_pem": account_key_pem,
            "email_address": email_address,
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
        if external_account_binding is not None:
            self._values["external_account_binding"] = external_account_binding
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
    def account_key_pem(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme/r/registration#account_key_pem Registration#account_key_pem}.'''
        result = self._values.get("account_key_pem")
        assert result is not None, "Required property 'account_key_pem' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email_address(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme/r/registration#email_address Registration#email_address}.'''
        result = self._values.get("email_address")
        assert result is not None, "Required property 'email_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def external_account_binding(
        self,
    ) -> typing.Optional["RegistrationExternalAccountBinding"]:
        '''external_account_binding block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme/r/registration#external_account_binding Registration#external_account_binding}
        '''
        result = self._values.get("external_account_binding")
        return typing.cast(typing.Optional["RegistrationExternalAccountBinding"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme/r/registration#id Registration#id}.

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
        return "RegistrationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-acme.registration.RegistrationExternalAccountBinding",
    jsii_struct_bases=[],
    name_mapping={"hmac_base64": "hmacBase64", "key_id": "keyId"},
)
class RegistrationExternalAccountBinding:
    def __init__(self, *, hmac_base64: builtins.str, key_id: builtins.str) -> None:
        '''
        :param hmac_base64: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme/r/registration#hmac_base64 Registration#hmac_base64}.
        :param key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme/r/registration#key_id Registration#key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RegistrationExternalAccountBinding.__init__)
            check_type(argname="argument hmac_base64", value=hmac_base64, expected_type=type_hints["hmac_base64"])
            check_type(argname="argument key_id", value=key_id, expected_type=type_hints["key_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "hmac_base64": hmac_base64,
            "key_id": key_id,
        }

    @builtins.property
    def hmac_base64(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme/r/registration#hmac_base64 Registration#hmac_base64}.'''
        result = self._values.get("hmac_base64")
        assert result is not None, "Required property 'hmac_base64' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme/r/registration#key_id Registration#key_id}.'''
        result = self._values.get("key_id")
        assert result is not None, "Required property 'key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegistrationExternalAccountBinding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RegistrationExternalAccountBindingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-acme.registration.RegistrationExternalAccountBindingOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RegistrationExternalAccountBindingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="hmacBase64Input")
    def hmac_base64_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hmacBase64Input"))

    @builtins.property
    @jsii.member(jsii_name="keyIdInput")
    def key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="hmacBase64")
    def hmac_base64(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hmacBase64"))

    @hmac_base64.setter
    def hmac_base64(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RegistrationExternalAccountBindingOutputReference, "hmac_base64").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hmacBase64", value)

    @builtins.property
    @jsii.member(jsii_name="keyId")
    def key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyId"))

    @key_id.setter
    def key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RegistrationExternalAccountBindingOutputReference, "key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RegistrationExternalAccountBinding]:
        return typing.cast(typing.Optional[RegistrationExternalAccountBinding], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RegistrationExternalAccountBinding],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RegistrationExternalAccountBindingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Registration",
    "RegistrationConfig",
    "RegistrationExternalAccountBinding",
    "RegistrationExternalAccountBindingOutputReference",
]

publication.publish()
