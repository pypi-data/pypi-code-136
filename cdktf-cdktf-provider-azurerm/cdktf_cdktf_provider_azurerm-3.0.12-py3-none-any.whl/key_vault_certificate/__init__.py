'''
# `azurerm_key_vault_certificate`

Refer to the Terraform Registory for docs: [`azurerm_key_vault_certificate`](https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate).
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


class KeyVaultCertificate(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificate",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate azurerm_key_vault_certificate}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        key_vault_id: builtins.str,
        name: builtins.str,
        certificate: typing.Optional[typing.Union["KeyVaultCertificateCertificate", typing.Dict[str, typing.Any]]] = None,
        certificate_policy: typing.Optional[typing.Union["KeyVaultCertificateCertificatePolicy", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KeyVaultCertificateTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate azurerm_key_vault_certificate} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#key_vault_id KeyVaultCertificate#key_vault_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#name KeyVaultCertificate#name}.
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#certificate KeyVaultCertificate#certificate}
        :param certificate_policy: certificate_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#certificate_policy KeyVaultCertificate#certificate_policy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#id KeyVaultCertificate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#tags KeyVaultCertificate#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#timeouts KeyVaultCertificate#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificate.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = KeyVaultCertificateConfig(
            key_vault_id=key_vault_id,
            name=name,
            certificate=certificate,
            certificate_policy=certificate_policy,
            id=id,
            tags=tags,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        *,
        contents: builtins.str,
        password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param contents: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#contents KeyVaultCertificate#contents}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#password KeyVaultCertificate#password}.
        '''
        value = KeyVaultCertificateCertificate(contents=contents, password=password)

        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @jsii.member(jsii_name="putCertificatePolicy")
    def put_certificate_policy(
        self,
        *,
        issuer_parameters: typing.Union["KeyVaultCertificateCertificatePolicyIssuerParameters", typing.Dict[str, typing.Any]],
        key_properties: typing.Union["KeyVaultCertificateCertificatePolicyKeyProperties", typing.Dict[str, typing.Any]],
        secret_properties: typing.Union["KeyVaultCertificateCertificatePolicySecretProperties", typing.Dict[str, typing.Any]],
        lifetime_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KeyVaultCertificateCertificatePolicyLifetimeAction", typing.Dict[str, typing.Any]]]]] = None,
        x509_certificate_properties: typing.Optional[typing.Union["KeyVaultCertificateCertificatePolicyX509CertificateProperties", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param issuer_parameters: issuer_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#issuer_parameters KeyVaultCertificate#issuer_parameters}
        :param key_properties: key_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#key_properties KeyVaultCertificate#key_properties}
        :param secret_properties: secret_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#secret_properties KeyVaultCertificate#secret_properties}
        :param lifetime_action: lifetime_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#lifetime_action KeyVaultCertificate#lifetime_action}
        :param x509_certificate_properties: x509_certificate_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#x509_certificate_properties KeyVaultCertificate#x509_certificate_properties}
        '''
        value = KeyVaultCertificateCertificatePolicy(
            issuer_parameters=issuer_parameters,
            key_properties=key_properties,
            secret_properties=secret_properties,
            lifetime_action=lifetime_action,
            x509_certificate_properties=x509_certificate_properties,
        )

        return typing.cast(None, jsii.invoke(self, "putCertificatePolicy", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#create KeyVaultCertificate#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#delete KeyVaultCertificate#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#read KeyVaultCertificate#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#update KeyVaultCertificate#update}.
        '''
        value = KeyVaultCertificateTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetCertificatePolicy")
    def reset_certificate_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificatePolicy", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> "KeyVaultCertificateCertificateOutputReference":
        return typing.cast("KeyVaultCertificateCertificateOutputReference", jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="certificateAttribute")
    def certificate_attribute(self) -> "KeyVaultCertificateCertificateAttributeList":
        return typing.cast("KeyVaultCertificateCertificateAttributeList", jsii.get(self, "certificateAttribute"))

    @builtins.property
    @jsii.member(jsii_name="certificateData")
    def certificate_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateData"))

    @builtins.property
    @jsii.member(jsii_name="certificateDataBase64")
    def certificate_data_base64(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateDataBase64"))

    @builtins.property
    @jsii.member(jsii_name="certificatePolicy")
    def certificate_policy(
        self,
    ) -> "KeyVaultCertificateCertificatePolicyOutputReference":
        return typing.cast("KeyVaultCertificateCertificatePolicyOutputReference", jsii.get(self, "certificatePolicy"))

    @builtins.property
    @jsii.member(jsii_name="secretId")
    def secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretId"))

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "KeyVaultCertificateTimeoutsOutputReference":
        return typing.cast("KeyVaultCertificateTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="versionlessId")
    def versionless_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionlessId"))

    @builtins.property
    @jsii.member(jsii_name="versionlessSecretId")
    def versionless_secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionlessSecretId"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional["KeyVaultCertificateCertificate"]:
        return typing.cast(typing.Optional["KeyVaultCertificateCertificate"], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="certificatePolicyInput")
    def certificate_policy_input(
        self,
    ) -> typing.Optional["KeyVaultCertificateCertificatePolicy"]:
        return typing.cast(typing.Optional["KeyVaultCertificateCertificatePolicy"], jsii.get(self, "certificatePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultIdInput")
    def key_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["KeyVaultCertificateTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["KeyVaultCertificateTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificate, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultId")
    def key_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultId"))

    @key_vault_id.setter
    def key_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificate, "key_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificate, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificate, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificate",
    jsii_struct_bases=[],
    name_mapping={"contents": "contents", "password": "password"},
)
class KeyVaultCertificateCertificate:
    def __init__(
        self,
        *,
        contents: builtins.str,
        password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param contents: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#contents KeyVaultCertificate#contents}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#password KeyVaultCertificate#password}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificate.__init__)
            check_type(argname="argument contents", value=contents, expected_type=type_hints["contents"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
        self._values: typing.Dict[str, typing.Any] = {
            "contents": contents,
        }
        if password is not None:
            self._values["password"] = password

    @builtins.property
    def contents(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#contents KeyVaultCertificate#contents}.'''
        result = self._values.get("contents")
        assert result is not None, "Required property 'contents' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#password KeyVaultCertificate#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultCertificateCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificateAttribute",
    jsii_struct_bases=[],
    name_mapping={},
)
class KeyVaultCertificateCertificateAttribute:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultCertificateCertificateAttribute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyVaultCertificateCertificateAttributeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificateAttributeList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificateAttributeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KeyVaultCertificateCertificateAttributeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificateAttributeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KeyVaultCertificateCertificateAttributeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificateAttributeList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificateAttributeList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificateAttributeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class KeyVaultCertificateCertificateAttributeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificateAttributeOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificateAttributeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="created")
    def created(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "created"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enabled"))

    @builtins.property
    @jsii.member(jsii_name="expires")
    def expires(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expires"))

    @builtins.property
    @jsii.member(jsii_name="notBefore")
    def not_before(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notBefore"))

    @builtins.property
    @jsii.member(jsii_name="recoveryLevel")
    def recovery_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recoveryLevel"))

    @builtins.property
    @jsii.member(jsii_name="updated")
    def updated(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updated"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KeyVaultCertificateCertificateAttribute]:
        return typing.cast(typing.Optional[KeyVaultCertificateCertificateAttribute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KeyVaultCertificateCertificateAttribute],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificateAttributeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KeyVaultCertificateCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificateOutputReference",
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
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @builtins.property
    @jsii.member(jsii_name="contentsInput")
    def contents_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentsInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="contents")
    def contents(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contents"))

    @contents.setter
    def contents(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificateOutputReference, "contents").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contents", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificateOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KeyVaultCertificateCertificate]:
        return typing.cast(typing.Optional[KeyVaultCertificateCertificate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KeyVaultCertificateCertificate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicy",
    jsii_struct_bases=[],
    name_mapping={
        "issuer_parameters": "issuerParameters",
        "key_properties": "keyProperties",
        "secret_properties": "secretProperties",
        "lifetime_action": "lifetimeAction",
        "x509_certificate_properties": "x509CertificateProperties",
    },
)
class KeyVaultCertificateCertificatePolicy:
    def __init__(
        self,
        *,
        issuer_parameters: typing.Union["KeyVaultCertificateCertificatePolicyIssuerParameters", typing.Dict[str, typing.Any]],
        key_properties: typing.Union["KeyVaultCertificateCertificatePolicyKeyProperties", typing.Dict[str, typing.Any]],
        secret_properties: typing.Union["KeyVaultCertificateCertificatePolicySecretProperties", typing.Dict[str, typing.Any]],
        lifetime_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KeyVaultCertificateCertificatePolicyLifetimeAction", typing.Dict[str, typing.Any]]]]] = None,
        x509_certificate_properties: typing.Optional[typing.Union["KeyVaultCertificateCertificatePolicyX509CertificateProperties", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param issuer_parameters: issuer_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#issuer_parameters KeyVaultCertificate#issuer_parameters}
        :param key_properties: key_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#key_properties KeyVaultCertificate#key_properties}
        :param secret_properties: secret_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#secret_properties KeyVaultCertificate#secret_properties}
        :param lifetime_action: lifetime_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#lifetime_action KeyVaultCertificate#lifetime_action}
        :param x509_certificate_properties: x509_certificate_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#x509_certificate_properties KeyVaultCertificate#x509_certificate_properties}
        '''
        if isinstance(issuer_parameters, dict):
            issuer_parameters = KeyVaultCertificateCertificatePolicyIssuerParameters(**issuer_parameters)
        if isinstance(key_properties, dict):
            key_properties = KeyVaultCertificateCertificatePolicyKeyProperties(**key_properties)
        if isinstance(secret_properties, dict):
            secret_properties = KeyVaultCertificateCertificatePolicySecretProperties(**secret_properties)
        if isinstance(x509_certificate_properties, dict):
            x509_certificate_properties = KeyVaultCertificateCertificatePolicyX509CertificateProperties(**x509_certificate_properties)
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicy.__init__)
            check_type(argname="argument issuer_parameters", value=issuer_parameters, expected_type=type_hints["issuer_parameters"])
            check_type(argname="argument key_properties", value=key_properties, expected_type=type_hints["key_properties"])
            check_type(argname="argument secret_properties", value=secret_properties, expected_type=type_hints["secret_properties"])
            check_type(argname="argument lifetime_action", value=lifetime_action, expected_type=type_hints["lifetime_action"])
            check_type(argname="argument x509_certificate_properties", value=x509_certificate_properties, expected_type=type_hints["x509_certificate_properties"])
        self._values: typing.Dict[str, typing.Any] = {
            "issuer_parameters": issuer_parameters,
            "key_properties": key_properties,
            "secret_properties": secret_properties,
        }
        if lifetime_action is not None:
            self._values["lifetime_action"] = lifetime_action
        if x509_certificate_properties is not None:
            self._values["x509_certificate_properties"] = x509_certificate_properties

    @builtins.property
    def issuer_parameters(
        self,
    ) -> "KeyVaultCertificateCertificatePolicyIssuerParameters":
        '''issuer_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#issuer_parameters KeyVaultCertificate#issuer_parameters}
        '''
        result = self._values.get("issuer_parameters")
        assert result is not None, "Required property 'issuer_parameters' is missing"
        return typing.cast("KeyVaultCertificateCertificatePolicyIssuerParameters", result)

    @builtins.property
    def key_properties(self) -> "KeyVaultCertificateCertificatePolicyKeyProperties":
        '''key_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#key_properties KeyVaultCertificate#key_properties}
        '''
        result = self._values.get("key_properties")
        assert result is not None, "Required property 'key_properties' is missing"
        return typing.cast("KeyVaultCertificateCertificatePolicyKeyProperties", result)

    @builtins.property
    def secret_properties(
        self,
    ) -> "KeyVaultCertificateCertificatePolicySecretProperties":
        '''secret_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#secret_properties KeyVaultCertificate#secret_properties}
        '''
        result = self._values.get("secret_properties")
        assert result is not None, "Required property 'secret_properties' is missing"
        return typing.cast("KeyVaultCertificateCertificatePolicySecretProperties", result)

    @builtins.property
    def lifetime_action(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KeyVaultCertificateCertificatePolicyLifetimeAction"]]]:
        '''lifetime_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#lifetime_action KeyVaultCertificate#lifetime_action}
        '''
        result = self._values.get("lifetime_action")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KeyVaultCertificateCertificatePolicyLifetimeAction"]]], result)

    @builtins.property
    def x509_certificate_properties(
        self,
    ) -> typing.Optional["KeyVaultCertificateCertificatePolicyX509CertificateProperties"]:
        '''x509_certificate_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#x509_certificate_properties KeyVaultCertificate#x509_certificate_properties}
        '''
        result = self._values.get("x509_certificate_properties")
        return typing.cast(typing.Optional["KeyVaultCertificateCertificatePolicyX509CertificateProperties"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultCertificateCertificatePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicyIssuerParameters",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class KeyVaultCertificateCertificatePolicyIssuerParameters:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#name KeyVaultCertificate#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicyIssuerParameters.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#name KeyVaultCertificate#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultCertificateCertificatePolicyIssuerParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyVaultCertificateCertificatePolicyIssuerParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicyIssuerParametersOutputReference",
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
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicyIssuerParametersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyIssuerParametersOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KeyVaultCertificateCertificatePolicyIssuerParameters]:
        return typing.cast(typing.Optional[KeyVaultCertificateCertificatePolicyIssuerParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KeyVaultCertificateCertificatePolicyIssuerParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyIssuerParametersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicyKeyProperties",
    jsii_struct_bases=[],
    name_mapping={
        "exportable": "exportable",
        "key_type": "keyType",
        "reuse_key": "reuseKey",
        "curve": "curve",
        "key_size": "keySize",
    },
)
class KeyVaultCertificateCertificatePolicyKeyProperties:
    def __init__(
        self,
        *,
        exportable: typing.Union[builtins.bool, cdktf.IResolvable],
        key_type: builtins.str,
        reuse_key: typing.Union[builtins.bool, cdktf.IResolvable],
        curve: typing.Optional[builtins.str] = None,
        key_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param exportable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#exportable KeyVaultCertificate#exportable}.
        :param key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#key_type KeyVaultCertificate#key_type}.
        :param reuse_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#reuse_key KeyVaultCertificate#reuse_key}.
        :param curve: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#curve KeyVaultCertificate#curve}.
        :param key_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#key_size KeyVaultCertificate#key_size}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicyKeyProperties.__init__)
            check_type(argname="argument exportable", value=exportable, expected_type=type_hints["exportable"])
            check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
            check_type(argname="argument reuse_key", value=reuse_key, expected_type=type_hints["reuse_key"])
            check_type(argname="argument curve", value=curve, expected_type=type_hints["curve"])
            check_type(argname="argument key_size", value=key_size, expected_type=type_hints["key_size"])
        self._values: typing.Dict[str, typing.Any] = {
            "exportable": exportable,
            "key_type": key_type,
            "reuse_key": reuse_key,
        }
        if curve is not None:
            self._values["curve"] = curve
        if key_size is not None:
            self._values["key_size"] = key_size

    @builtins.property
    def exportable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#exportable KeyVaultCertificate#exportable}.'''
        result = self._values.get("exportable")
        assert result is not None, "Required property 'exportable' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def key_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#key_type KeyVaultCertificate#key_type}.'''
        result = self._values.get("key_type")
        assert result is not None, "Required property 'key_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def reuse_key(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#reuse_key KeyVaultCertificate#reuse_key}.'''
        result = self._values.get("reuse_key")
        assert result is not None, "Required property 'reuse_key' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def curve(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#curve KeyVaultCertificate#curve}.'''
        result = self._values.get("curve")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#key_size KeyVaultCertificate#key_size}.'''
        result = self._values.get("key_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultCertificateCertificatePolicyKeyProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyVaultCertificateCertificatePolicyKeyPropertiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicyKeyPropertiesOutputReference",
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
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicyKeyPropertiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCurve")
    def reset_curve(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCurve", []))

    @jsii.member(jsii_name="resetKeySize")
    def reset_key_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeySize", []))

    @builtins.property
    @jsii.member(jsii_name="curveInput")
    def curve_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "curveInput"))

    @builtins.property
    @jsii.member(jsii_name="exportableInput")
    def exportable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "exportableInput"))

    @builtins.property
    @jsii.member(jsii_name="keySizeInput")
    def key_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "keySizeInput"))

    @builtins.property
    @jsii.member(jsii_name="keyTypeInput")
    def key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="reuseKeyInput")
    def reuse_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "reuseKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="curve")
    def curve(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "curve"))

    @curve.setter
    def curve(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyKeyPropertiesOutputReference, "curve").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "curve", value)

    @builtins.property
    @jsii.member(jsii_name="exportable")
    def exportable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "exportable"))

    @exportable.setter
    def exportable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyKeyPropertiesOutputReference, "exportable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exportable", value)

    @builtins.property
    @jsii.member(jsii_name="keySize")
    def key_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "keySize"))

    @key_size.setter
    def key_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyKeyPropertiesOutputReference, "key_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keySize", value)

    @builtins.property
    @jsii.member(jsii_name="keyType")
    def key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyType"))

    @key_type.setter
    def key_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyKeyPropertiesOutputReference, "key_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyType", value)

    @builtins.property
    @jsii.member(jsii_name="reuseKey")
    def reuse_key(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "reuseKey"))

    @reuse_key.setter
    def reuse_key(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyKeyPropertiesOutputReference, "reuse_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reuseKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KeyVaultCertificateCertificatePolicyKeyProperties]:
        return typing.cast(typing.Optional[KeyVaultCertificateCertificatePolicyKeyProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KeyVaultCertificateCertificatePolicyKeyProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyKeyPropertiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicyLifetimeAction",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "trigger": "trigger"},
)
class KeyVaultCertificateCertificatePolicyLifetimeAction:
    def __init__(
        self,
        *,
        action: typing.Union["KeyVaultCertificateCertificatePolicyLifetimeActionAction", typing.Dict[str, typing.Any]],
        trigger: typing.Union["KeyVaultCertificateCertificatePolicyLifetimeActionTrigger", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#action KeyVaultCertificate#action}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#trigger KeyVaultCertificate#trigger}
        '''
        if isinstance(action, dict):
            action = KeyVaultCertificateCertificatePolicyLifetimeActionAction(**action)
        if isinstance(trigger, dict):
            trigger = KeyVaultCertificateCertificatePolicyLifetimeActionTrigger(**trigger)
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicyLifetimeAction.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "trigger": trigger,
        }

    @builtins.property
    def action(self) -> "KeyVaultCertificateCertificatePolicyLifetimeActionAction":
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#action KeyVaultCertificate#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast("KeyVaultCertificateCertificatePolicyLifetimeActionAction", result)

    @builtins.property
    def trigger(self) -> "KeyVaultCertificateCertificatePolicyLifetimeActionTrigger":
        '''trigger block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#trigger KeyVaultCertificate#trigger}
        '''
        result = self._values.get("trigger")
        assert result is not None, "Required property 'trigger' is missing"
        return typing.cast("KeyVaultCertificateCertificatePolicyLifetimeActionTrigger", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultCertificateCertificatePolicyLifetimeAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicyLifetimeActionAction",
    jsii_struct_bases=[],
    name_mapping={"action_type": "actionType"},
)
class KeyVaultCertificateCertificatePolicyLifetimeActionAction:
    def __init__(self, *, action_type: builtins.str) -> None:
        '''
        :param action_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#action_type KeyVaultCertificate#action_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicyLifetimeActionAction.__init__)
            check_type(argname="argument action_type", value=action_type, expected_type=type_hints["action_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "action_type": action_type,
        }

    @builtins.property
    def action_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#action_type KeyVaultCertificate#action_type}.'''
        result = self._values.get("action_type")
        assert result is not None, "Required property 'action_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultCertificateCertificatePolicyLifetimeActionAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyVaultCertificateCertificatePolicyLifetimeActionActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicyLifetimeActionActionOutputReference",
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
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicyLifetimeActionActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="actionTypeInput")
    def action_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="actionType")
    def action_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionType"))

    @action_type.setter
    def action_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyLifetimeActionActionOutputReference, "action_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KeyVaultCertificateCertificatePolicyLifetimeActionAction]:
        return typing.cast(typing.Optional[KeyVaultCertificateCertificatePolicyLifetimeActionAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KeyVaultCertificateCertificatePolicyLifetimeActionAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyLifetimeActionActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KeyVaultCertificateCertificatePolicyLifetimeActionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicyLifetimeActionList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicyLifetimeActionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KeyVaultCertificateCertificatePolicyLifetimeActionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicyLifetimeActionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KeyVaultCertificateCertificatePolicyLifetimeActionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyLifetimeActionList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyLifetimeActionList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyLifetimeActionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyVaultCertificateCertificatePolicyLifetimeAction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyVaultCertificateCertificatePolicyLifetimeAction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyVaultCertificateCertificatePolicyLifetimeAction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyLifetimeActionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KeyVaultCertificateCertificatePolicyLifetimeActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicyLifetimeActionOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicyLifetimeActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAction")
    def put_action(self, *, action_type: builtins.str) -> None:
        '''
        :param action_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#action_type KeyVaultCertificate#action_type}.
        '''
        value = KeyVaultCertificateCertificatePolicyLifetimeActionAction(
            action_type=action_type
        )

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putTrigger")
    def put_trigger(
        self,
        *,
        days_before_expiry: typing.Optional[jsii.Number] = None,
        lifetime_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param days_before_expiry: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#days_before_expiry KeyVaultCertificate#days_before_expiry}.
        :param lifetime_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#lifetime_percentage KeyVaultCertificate#lifetime_percentage}.
        '''
        value = KeyVaultCertificateCertificatePolicyLifetimeActionTrigger(
            days_before_expiry=days_before_expiry,
            lifetime_percentage=lifetime_percentage,
        )

        return typing.cast(None, jsii.invoke(self, "putTrigger", [value]))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(
        self,
    ) -> KeyVaultCertificateCertificatePolicyLifetimeActionActionOutputReference:
        return typing.cast(KeyVaultCertificateCertificatePolicyLifetimeActionActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="trigger")
    def trigger(
        self,
    ) -> "KeyVaultCertificateCertificatePolicyLifetimeActionTriggerOutputReference":
        return typing.cast("KeyVaultCertificateCertificatePolicyLifetimeActionTriggerOutputReference", jsii.get(self, "trigger"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(
        self,
    ) -> typing.Optional[KeyVaultCertificateCertificatePolicyLifetimeActionAction]:
        return typing.cast(typing.Optional[KeyVaultCertificateCertificatePolicyLifetimeActionAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerInput")
    def trigger_input(
        self,
    ) -> typing.Optional["KeyVaultCertificateCertificatePolicyLifetimeActionTrigger"]:
        return typing.cast(typing.Optional["KeyVaultCertificateCertificatePolicyLifetimeActionTrigger"], jsii.get(self, "triggerInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KeyVaultCertificateCertificatePolicyLifetimeAction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KeyVaultCertificateCertificatePolicyLifetimeAction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KeyVaultCertificateCertificatePolicyLifetimeAction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyLifetimeActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicyLifetimeActionTrigger",
    jsii_struct_bases=[],
    name_mapping={
        "days_before_expiry": "daysBeforeExpiry",
        "lifetime_percentage": "lifetimePercentage",
    },
)
class KeyVaultCertificateCertificatePolicyLifetimeActionTrigger:
    def __init__(
        self,
        *,
        days_before_expiry: typing.Optional[jsii.Number] = None,
        lifetime_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param days_before_expiry: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#days_before_expiry KeyVaultCertificate#days_before_expiry}.
        :param lifetime_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#lifetime_percentage KeyVaultCertificate#lifetime_percentage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicyLifetimeActionTrigger.__init__)
            check_type(argname="argument days_before_expiry", value=days_before_expiry, expected_type=type_hints["days_before_expiry"])
            check_type(argname="argument lifetime_percentage", value=lifetime_percentage, expected_type=type_hints["lifetime_percentage"])
        self._values: typing.Dict[str, typing.Any] = {}
        if days_before_expiry is not None:
            self._values["days_before_expiry"] = days_before_expiry
        if lifetime_percentage is not None:
            self._values["lifetime_percentage"] = lifetime_percentage

    @builtins.property
    def days_before_expiry(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#days_before_expiry KeyVaultCertificate#days_before_expiry}.'''
        result = self._values.get("days_before_expiry")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def lifetime_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#lifetime_percentage KeyVaultCertificate#lifetime_percentage}.'''
        result = self._values.get("lifetime_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultCertificateCertificatePolicyLifetimeActionTrigger(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyVaultCertificateCertificatePolicyLifetimeActionTriggerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicyLifetimeActionTriggerOutputReference",
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
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicyLifetimeActionTriggerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDaysBeforeExpiry")
    def reset_days_before_expiry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDaysBeforeExpiry", []))

    @jsii.member(jsii_name="resetLifetimePercentage")
    def reset_lifetime_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifetimePercentage", []))

    @builtins.property
    @jsii.member(jsii_name="daysBeforeExpiryInput")
    def days_before_expiry_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysBeforeExpiryInput"))

    @builtins.property
    @jsii.member(jsii_name="lifetimePercentageInput")
    def lifetime_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lifetimePercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="daysBeforeExpiry")
    def days_before_expiry(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "daysBeforeExpiry"))

    @days_before_expiry.setter
    def days_before_expiry(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyLifetimeActionTriggerOutputReference, "days_before_expiry").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "daysBeforeExpiry", value)

    @builtins.property
    @jsii.member(jsii_name="lifetimePercentage")
    def lifetime_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lifetimePercentage"))

    @lifetime_percentage.setter
    def lifetime_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyLifetimeActionTriggerOutputReference, "lifetime_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifetimePercentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KeyVaultCertificateCertificatePolicyLifetimeActionTrigger]:
        return typing.cast(typing.Optional[KeyVaultCertificateCertificatePolicyLifetimeActionTrigger], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KeyVaultCertificateCertificatePolicyLifetimeActionTrigger],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyLifetimeActionTriggerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KeyVaultCertificateCertificatePolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicyOutputReference",
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
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIssuerParameters")
    def put_issuer_parameters(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#name KeyVaultCertificate#name}.
        '''
        value = KeyVaultCertificateCertificatePolicyIssuerParameters(name=name)

        return typing.cast(None, jsii.invoke(self, "putIssuerParameters", [value]))

    @jsii.member(jsii_name="putKeyProperties")
    def put_key_properties(
        self,
        *,
        exportable: typing.Union[builtins.bool, cdktf.IResolvable],
        key_type: builtins.str,
        reuse_key: typing.Union[builtins.bool, cdktf.IResolvable],
        curve: typing.Optional[builtins.str] = None,
        key_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param exportable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#exportable KeyVaultCertificate#exportable}.
        :param key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#key_type KeyVaultCertificate#key_type}.
        :param reuse_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#reuse_key KeyVaultCertificate#reuse_key}.
        :param curve: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#curve KeyVaultCertificate#curve}.
        :param key_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#key_size KeyVaultCertificate#key_size}.
        '''
        value = KeyVaultCertificateCertificatePolicyKeyProperties(
            exportable=exportable,
            key_type=key_type,
            reuse_key=reuse_key,
            curve=curve,
            key_size=key_size,
        )

        return typing.cast(None, jsii.invoke(self, "putKeyProperties", [value]))

    @jsii.member(jsii_name="putLifetimeAction")
    def put_lifetime_action(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KeyVaultCertificateCertificatePolicyLifetimeAction, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicyOutputReference.put_lifetime_action)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLifetimeAction", [value]))

    @jsii.member(jsii_name="putSecretProperties")
    def put_secret_properties(self, *, content_type: builtins.str) -> None:
        '''
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#content_type KeyVaultCertificate#content_type}.
        '''
        value = KeyVaultCertificateCertificatePolicySecretProperties(
            content_type=content_type
        )

        return typing.cast(None, jsii.invoke(self, "putSecretProperties", [value]))

    @jsii.member(jsii_name="putX509CertificateProperties")
    def put_x509_certificate_properties(
        self,
        *,
        key_usage: typing.Sequence[builtins.str],
        subject: builtins.str,
        validity_in_months: jsii.Number,
        extended_key_usage: typing.Optional[typing.Sequence[builtins.str]] = None,
        subject_alternative_names: typing.Optional[typing.Union["KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNames", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param key_usage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#key_usage KeyVaultCertificate#key_usage}.
        :param subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#subject KeyVaultCertificate#subject}.
        :param validity_in_months: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#validity_in_months KeyVaultCertificate#validity_in_months}.
        :param extended_key_usage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#extended_key_usage KeyVaultCertificate#extended_key_usage}.
        :param subject_alternative_names: subject_alternative_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#subject_alternative_names KeyVaultCertificate#subject_alternative_names}
        '''
        value = KeyVaultCertificateCertificatePolicyX509CertificateProperties(
            key_usage=key_usage,
            subject=subject,
            validity_in_months=validity_in_months,
            extended_key_usage=extended_key_usage,
            subject_alternative_names=subject_alternative_names,
        )

        return typing.cast(None, jsii.invoke(self, "putX509CertificateProperties", [value]))

    @jsii.member(jsii_name="resetLifetimeAction")
    def reset_lifetime_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifetimeAction", []))

    @jsii.member(jsii_name="resetX509CertificateProperties")
    def reset_x509_certificate_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetX509CertificateProperties", []))

    @builtins.property
    @jsii.member(jsii_name="issuerParameters")
    def issuer_parameters(
        self,
    ) -> KeyVaultCertificateCertificatePolicyIssuerParametersOutputReference:
        return typing.cast(KeyVaultCertificateCertificatePolicyIssuerParametersOutputReference, jsii.get(self, "issuerParameters"))

    @builtins.property
    @jsii.member(jsii_name="keyProperties")
    def key_properties(
        self,
    ) -> KeyVaultCertificateCertificatePolicyKeyPropertiesOutputReference:
        return typing.cast(KeyVaultCertificateCertificatePolicyKeyPropertiesOutputReference, jsii.get(self, "keyProperties"))

    @builtins.property
    @jsii.member(jsii_name="lifetimeAction")
    def lifetime_action(self) -> KeyVaultCertificateCertificatePolicyLifetimeActionList:
        return typing.cast(KeyVaultCertificateCertificatePolicyLifetimeActionList, jsii.get(self, "lifetimeAction"))

    @builtins.property
    @jsii.member(jsii_name="secretProperties")
    def secret_properties(
        self,
    ) -> "KeyVaultCertificateCertificatePolicySecretPropertiesOutputReference":
        return typing.cast("KeyVaultCertificateCertificatePolicySecretPropertiesOutputReference", jsii.get(self, "secretProperties"))

    @builtins.property
    @jsii.member(jsii_name="x509CertificateProperties")
    def x509_certificate_properties(
        self,
    ) -> "KeyVaultCertificateCertificatePolicyX509CertificatePropertiesOutputReference":
        return typing.cast("KeyVaultCertificateCertificatePolicyX509CertificatePropertiesOutputReference", jsii.get(self, "x509CertificateProperties"))

    @builtins.property
    @jsii.member(jsii_name="issuerParametersInput")
    def issuer_parameters_input(
        self,
    ) -> typing.Optional[KeyVaultCertificateCertificatePolicyIssuerParameters]:
        return typing.cast(typing.Optional[KeyVaultCertificateCertificatePolicyIssuerParameters], jsii.get(self, "issuerParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="keyPropertiesInput")
    def key_properties_input(
        self,
    ) -> typing.Optional[KeyVaultCertificateCertificatePolicyKeyProperties]:
        return typing.cast(typing.Optional[KeyVaultCertificateCertificatePolicyKeyProperties], jsii.get(self, "keyPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="lifetimeActionInput")
    def lifetime_action_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyVaultCertificateCertificatePolicyLifetimeAction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyVaultCertificateCertificatePolicyLifetimeAction]]], jsii.get(self, "lifetimeActionInput"))

    @builtins.property
    @jsii.member(jsii_name="secretPropertiesInput")
    def secret_properties_input(
        self,
    ) -> typing.Optional["KeyVaultCertificateCertificatePolicySecretProperties"]:
        return typing.cast(typing.Optional["KeyVaultCertificateCertificatePolicySecretProperties"], jsii.get(self, "secretPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="x509CertificatePropertiesInput")
    def x509_certificate_properties_input(
        self,
    ) -> typing.Optional["KeyVaultCertificateCertificatePolicyX509CertificateProperties"]:
        return typing.cast(typing.Optional["KeyVaultCertificateCertificatePolicyX509CertificateProperties"], jsii.get(self, "x509CertificatePropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KeyVaultCertificateCertificatePolicy]:
        return typing.cast(typing.Optional[KeyVaultCertificateCertificatePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KeyVaultCertificateCertificatePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicySecretProperties",
    jsii_struct_bases=[],
    name_mapping={"content_type": "contentType"},
)
class KeyVaultCertificateCertificatePolicySecretProperties:
    def __init__(self, *, content_type: builtins.str) -> None:
        '''
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#content_type KeyVaultCertificate#content_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicySecretProperties.__init__)
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "content_type": content_type,
        }

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#content_type KeyVaultCertificate#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultCertificateCertificatePolicySecretProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyVaultCertificateCertificatePolicySecretPropertiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicySecretPropertiesOutputReference",
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
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicySecretPropertiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicySecretPropertiesOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KeyVaultCertificateCertificatePolicySecretProperties]:
        return typing.cast(typing.Optional[KeyVaultCertificateCertificatePolicySecretProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KeyVaultCertificateCertificatePolicySecretProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicySecretPropertiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicyX509CertificateProperties",
    jsii_struct_bases=[],
    name_mapping={
        "key_usage": "keyUsage",
        "subject": "subject",
        "validity_in_months": "validityInMonths",
        "extended_key_usage": "extendedKeyUsage",
        "subject_alternative_names": "subjectAlternativeNames",
    },
)
class KeyVaultCertificateCertificatePolicyX509CertificateProperties:
    def __init__(
        self,
        *,
        key_usage: typing.Sequence[builtins.str],
        subject: builtins.str,
        validity_in_months: jsii.Number,
        extended_key_usage: typing.Optional[typing.Sequence[builtins.str]] = None,
        subject_alternative_names: typing.Optional[typing.Union["KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNames", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param key_usage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#key_usage KeyVaultCertificate#key_usage}.
        :param subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#subject KeyVaultCertificate#subject}.
        :param validity_in_months: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#validity_in_months KeyVaultCertificate#validity_in_months}.
        :param extended_key_usage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#extended_key_usage KeyVaultCertificate#extended_key_usage}.
        :param subject_alternative_names: subject_alternative_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#subject_alternative_names KeyVaultCertificate#subject_alternative_names}
        '''
        if isinstance(subject_alternative_names, dict):
            subject_alternative_names = KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNames(**subject_alternative_names)
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicyX509CertificateProperties.__init__)
            check_type(argname="argument key_usage", value=key_usage, expected_type=type_hints["key_usage"])
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            check_type(argname="argument validity_in_months", value=validity_in_months, expected_type=type_hints["validity_in_months"])
            check_type(argname="argument extended_key_usage", value=extended_key_usage, expected_type=type_hints["extended_key_usage"])
            check_type(argname="argument subject_alternative_names", value=subject_alternative_names, expected_type=type_hints["subject_alternative_names"])
        self._values: typing.Dict[str, typing.Any] = {
            "key_usage": key_usage,
            "subject": subject,
            "validity_in_months": validity_in_months,
        }
        if extended_key_usage is not None:
            self._values["extended_key_usage"] = extended_key_usage
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names

    @builtins.property
    def key_usage(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#key_usage KeyVaultCertificate#key_usage}.'''
        result = self._values.get("key_usage")
        assert result is not None, "Required property 'key_usage' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subject(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#subject KeyVaultCertificate#subject}.'''
        result = self._values.get("subject")
        assert result is not None, "Required property 'subject' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def validity_in_months(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#validity_in_months KeyVaultCertificate#validity_in_months}.'''
        result = self._values.get("validity_in_months")
        assert result is not None, "Required property 'validity_in_months' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def extended_key_usage(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#extended_key_usage KeyVaultCertificate#extended_key_usage}.'''
        result = self._values.get("extended_key_usage")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subject_alternative_names(
        self,
    ) -> typing.Optional["KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNames"]:
        '''subject_alternative_names block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#subject_alternative_names KeyVaultCertificate#subject_alternative_names}
        '''
        result = self._values.get("subject_alternative_names")
        return typing.cast(typing.Optional["KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNames"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultCertificateCertificatePolicyX509CertificateProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyVaultCertificateCertificatePolicyX509CertificatePropertiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicyX509CertificatePropertiesOutputReference",
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
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicyX509CertificatePropertiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSubjectAlternativeNames")
    def put_subject_alternative_names(
        self,
        *,
        dns_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        emails: typing.Optional[typing.Sequence[builtins.str]] = None,
        upns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param dns_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#dns_names KeyVaultCertificate#dns_names}.
        :param emails: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#emails KeyVaultCertificate#emails}.
        :param upns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#upns KeyVaultCertificate#upns}.
        '''
        value = KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNames(
            dns_names=dns_names, emails=emails, upns=upns
        )

        return typing.cast(None, jsii.invoke(self, "putSubjectAlternativeNames", [value]))

    @jsii.member(jsii_name="resetExtendedKeyUsage")
    def reset_extended_key_usage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtendedKeyUsage", []))

    @jsii.member(jsii_name="resetSubjectAlternativeNames")
    def reset_subject_alternative_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubjectAlternativeNames", []))

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> "KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNamesOutputReference":
        return typing.cast("KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNamesOutputReference", jsii.get(self, "subjectAlternativeNames"))

    @builtins.property
    @jsii.member(jsii_name="extendedKeyUsageInput")
    def extended_key_usage_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "extendedKeyUsageInput"))

    @builtins.property
    @jsii.member(jsii_name="keyUsageInput")
    def key_usage_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "keyUsageInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNamesInput")
    def subject_alternative_names_input(
        self,
    ) -> typing.Optional["KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNames"]:
        return typing.cast(typing.Optional["KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNames"], jsii.get(self, "subjectAlternativeNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectInput")
    def subject_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subjectInput"))

    @builtins.property
    @jsii.member(jsii_name="validityInMonthsInput")
    def validity_in_months_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "validityInMonthsInput"))

    @builtins.property
    @jsii.member(jsii_name="extendedKeyUsage")
    def extended_key_usage(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "extendedKeyUsage"))

    @extended_key_usage.setter
    def extended_key_usage(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyX509CertificatePropertiesOutputReference, "extended_key_usage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extendedKeyUsage", value)

    @builtins.property
    @jsii.member(jsii_name="keyUsage")
    def key_usage(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "keyUsage"))

    @key_usage.setter
    def key_usage(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyX509CertificatePropertiesOutputReference, "key_usage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyUsage", value)

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @subject.setter
    def subject(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyX509CertificatePropertiesOutputReference, "subject").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subject", value)

    @builtins.property
    @jsii.member(jsii_name="validityInMonths")
    def validity_in_months(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "validityInMonths"))

    @validity_in_months.setter
    def validity_in_months(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyX509CertificatePropertiesOutputReference, "validity_in_months").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validityInMonths", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KeyVaultCertificateCertificatePolicyX509CertificateProperties]:
        return typing.cast(typing.Optional[KeyVaultCertificateCertificatePolicyX509CertificateProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KeyVaultCertificateCertificatePolicyX509CertificateProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyX509CertificatePropertiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNames",
    jsii_struct_bases=[],
    name_mapping={"dns_names": "dnsNames", "emails": "emails", "upns": "upns"},
)
class KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNames:
    def __init__(
        self,
        *,
        dns_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        emails: typing.Optional[typing.Sequence[builtins.str]] = None,
        upns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param dns_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#dns_names KeyVaultCertificate#dns_names}.
        :param emails: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#emails KeyVaultCertificate#emails}.
        :param upns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#upns KeyVaultCertificate#upns}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNames.__init__)
            check_type(argname="argument dns_names", value=dns_names, expected_type=type_hints["dns_names"])
            check_type(argname="argument emails", value=emails, expected_type=type_hints["emails"])
            check_type(argname="argument upns", value=upns, expected_type=type_hints["upns"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dns_names is not None:
            self._values["dns_names"] = dns_names
        if emails is not None:
            self._values["emails"] = emails
        if upns is not None:
            self._values["upns"] = upns

    @builtins.property
    def dns_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#dns_names KeyVaultCertificate#dns_names}.'''
        result = self._values.get("dns_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def emails(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#emails KeyVaultCertificate#emails}.'''
        result = self._values.get("emails")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def upns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#upns KeyVaultCertificate#upns}.'''
        result = self._values.get("upns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNames(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNamesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNamesOutputReference",
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
            type_hints = typing.get_type_hints(KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNamesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDnsNames")
    def reset_dns_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsNames", []))

    @jsii.member(jsii_name="resetEmails")
    def reset_emails(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmails", []))

    @jsii.member(jsii_name="resetUpns")
    def reset_upns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpns", []))

    @builtins.property
    @jsii.member(jsii_name="dnsNamesInput")
    def dns_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="emailsInput")
    def emails_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailsInput"))

    @builtins.property
    @jsii.member(jsii_name="upnsInput")
    def upns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "upnsInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsNames")
    def dns_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsNames"))

    @dns_names.setter
    def dns_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNamesOutputReference, "dns_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsNames", value)

    @builtins.property
    @jsii.member(jsii_name="emails")
    def emails(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "emails"))

    @emails.setter
    def emails(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNamesOutputReference, "emails").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emails", value)

    @builtins.property
    @jsii.member(jsii_name="upns")
    def upns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "upns"))

    @upns.setter
    def upns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNamesOutputReference, "upns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNames]:
        return typing.cast(typing.Optional[KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNames], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNames],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNamesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "key_vault_id": "keyVaultId",
        "name": "name",
        "certificate": "certificate",
        "certificate_policy": "certificatePolicy",
        "id": "id",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class KeyVaultCertificateConfig(cdktf.TerraformMetaArguments):
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
        key_vault_id: builtins.str,
        name: builtins.str,
        certificate: typing.Optional[typing.Union[KeyVaultCertificateCertificate, typing.Dict[str, typing.Any]]] = None,
        certificate_policy: typing.Optional[typing.Union[KeyVaultCertificateCertificatePolicy, typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KeyVaultCertificateTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#key_vault_id KeyVaultCertificate#key_vault_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#name KeyVaultCertificate#name}.
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#certificate KeyVaultCertificate#certificate}
        :param certificate_policy: certificate_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#certificate_policy KeyVaultCertificate#certificate_policy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#id KeyVaultCertificate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#tags KeyVaultCertificate#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#timeouts KeyVaultCertificate#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(certificate, dict):
            certificate = KeyVaultCertificateCertificate(**certificate)
        if isinstance(certificate_policy, dict):
            certificate_policy = KeyVaultCertificateCertificatePolicy(**certificate_policy)
        if isinstance(timeouts, dict):
            timeouts = KeyVaultCertificateTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument certificate_policy", value=certificate_policy, expected_type=type_hints["certificate_policy"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "key_vault_id": key_vault_id,
            "name": name,
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
        if certificate is not None:
            self._values["certificate"] = certificate
        if certificate_policy is not None:
            self._values["certificate_policy"] = certificate_policy
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def key_vault_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#key_vault_id KeyVaultCertificate#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        assert result is not None, "Required property 'key_vault_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#name KeyVaultCertificate#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate(self) -> typing.Optional[KeyVaultCertificateCertificate]:
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#certificate KeyVaultCertificate#certificate}
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[KeyVaultCertificateCertificate], result)

    @builtins.property
    def certificate_policy(
        self,
    ) -> typing.Optional[KeyVaultCertificateCertificatePolicy]:
        '''certificate_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#certificate_policy KeyVaultCertificate#certificate_policy}
        '''
        result = self._values.get("certificate_policy")
        return typing.cast(typing.Optional[KeyVaultCertificateCertificatePolicy], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#id KeyVaultCertificate#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#tags KeyVaultCertificate#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["KeyVaultCertificateTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#timeouts KeyVaultCertificate#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["KeyVaultCertificateTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultCertificateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class KeyVaultCertificateTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#create KeyVaultCertificate#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#delete KeyVaultCertificate#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#read KeyVaultCertificate#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#update KeyVaultCertificate#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultCertificateTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#create KeyVaultCertificate#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#delete KeyVaultCertificate#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#read KeyVaultCertificate#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate#update KeyVaultCertificate#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultCertificateTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyVaultCertificateTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVaultCertificate.KeyVaultCertificateTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(KeyVaultCertificateTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KeyVaultCertificateTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KeyVaultCertificateTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KeyVaultCertificateTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultCertificateTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KeyVaultCertificate",
    "KeyVaultCertificateCertificate",
    "KeyVaultCertificateCertificateAttribute",
    "KeyVaultCertificateCertificateAttributeList",
    "KeyVaultCertificateCertificateAttributeOutputReference",
    "KeyVaultCertificateCertificateOutputReference",
    "KeyVaultCertificateCertificatePolicy",
    "KeyVaultCertificateCertificatePolicyIssuerParameters",
    "KeyVaultCertificateCertificatePolicyIssuerParametersOutputReference",
    "KeyVaultCertificateCertificatePolicyKeyProperties",
    "KeyVaultCertificateCertificatePolicyKeyPropertiesOutputReference",
    "KeyVaultCertificateCertificatePolicyLifetimeAction",
    "KeyVaultCertificateCertificatePolicyLifetimeActionAction",
    "KeyVaultCertificateCertificatePolicyLifetimeActionActionOutputReference",
    "KeyVaultCertificateCertificatePolicyLifetimeActionList",
    "KeyVaultCertificateCertificatePolicyLifetimeActionOutputReference",
    "KeyVaultCertificateCertificatePolicyLifetimeActionTrigger",
    "KeyVaultCertificateCertificatePolicyLifetimeActionTriggerOutputReference",
    "KeyVaultCertificateCertificatePolicyOutputReference",
    "KeyVaultCertificateCertificatePolicySecretProperties",
    "KeyVaultCertificateCertificatePolicySecretPropertiesOutputReference",
    "KeyVaultCertificateCertificatePolicyX509CertificateProperties",
    "KeyVaultCertificateCertificatePolicyX509CertificatePropertiesOutputReference",
    "KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNames",
    "KeyVaultCertificateCertificatePolicyX509CertificatePropertiesSubjectAlternativeNamesOutputReference",
    "KeyVaultCertificateConfig",
    "KeyVaultCertificateTimeouts",
    "KeyVaultCertificateTimeoutsOutputReference",
]

publication.publish()
