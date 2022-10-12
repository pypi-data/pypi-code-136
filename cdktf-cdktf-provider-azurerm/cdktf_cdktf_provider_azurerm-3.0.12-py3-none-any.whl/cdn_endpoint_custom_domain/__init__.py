'''
# `azurerm_cdn_endpoint_custom_domain`

Refer to the Terraform Registory for docs: [`azurerm_cdn_endpoint_custom_domain`](https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain).
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


class CdnEndpointCustomDomain(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpointCustomDomain.CdnEndpointCustomDomain",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain azurerm_cdn_endpoint_custom_domain}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cdn_endpoint_id: builtins.str,
        host_name: builtins.str,
        name: builtins.str,
        cdn_managed_https: typing.Optional[typing.Union["CdnEndpointCustomDomainCdnManagedHttps", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CdnEndpointCustomDomainTimeouts", typing.Dict[str, typing.Any]]] = None,
        user_managed_https: typing.Optional[typing.Union["CdnEndpointCustomDomainUserManagedHttps", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain azurerm_cdn_endpoint_custom_domain} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cdn_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#cdn_endpoint_id CdnEndpointCustomDomain#cdn_endpoint_id}.
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#host_name CdnEndpointCustomDomain#host_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#name CdnEndpointCustomDomain#name}.
        :param cdn_managed_https: cdn_managed_https block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#cdn_managed_https CdnEndpointCustomDomain#cdn_managed_https}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#id CdnEndpointCustomDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#timeouts CdnEndpointCustomDomain#timeouts}
        :param user_managed_https: user_managed_https block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#user_managed_https CdnEndpointCustomDomain#user_managed_https}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointCustomDomain.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CdnEndpointCustomDomainConfig(
            cdn_endpoint_id=cdn_endpoint_id,
            host_name=host_name,
            name=name,
            cdn_managed_https=cdn_managed_https,
            id=id,
            timeouts=timeouts,
            user_managed_https=user_managed_https,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCdnManagedHttps")
    def put_cdn_managed_https(
        self,
        *,
        certificate_type: builtins.str,
        protocol_type: builtins.str,
        tls_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param certificate_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#certificate_type CdnEndpointCustomDomain#certificate_type}.
        :param protocol_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#protocol_type CdnEndpointCustomDomain#protocol_type}.
        :param tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#tls_version CdnEndpointCustomDomain#tls_version}.
        '''
        value = CdnEndpointCustomDomainCdnManagedHttps(
            certificate_type=certificate_type,
            protocol_type=protocol_type,
            tls_version=tls_version,
        )

        return typing.cast(None, jsii.invoke(self, "putCdnManagedHttps", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#create CdnEndpointCustomDomain#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#delete CdnEndpointCustomDomain#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#read CdnEndpointCustomDomain#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#update CdnEndpointCustomDomain#update}.
        '''
        value = CdnEndpointCustomDomainTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putUserManagedHttps")
    def put_user_managed_https(
        self,
        *,
        key_vault_certificate_id: typing.Optional[builtins.str] = None,
        key_vault_secret_id: typing.Optional[builtins.str] = None,
        tls_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_vault_certificate_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#key_vault_certificate_id CdnEndpointCustomDomain#key_vault_certificate_id}.
        :param key_vault_secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#key_vault_secret_id CdnEndpointCustomDomain#key_vault_secret_id}.
        :param tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#tls_version CdnEndpointCustomDomain#tls_version}.
        '''
        value = CdnEndpointCustomDomainUserManagedHttps(
            key_vault_certificate_id=key_vault_certificate_id,
            key_vault_secret_id=key_vault_secret_id,
            tls_version=tls_version,
        )

        return typing.cast(None, jsii.invoke(self, "putUserManagedHttps", [value]))

    @jsii.member(jsii_name="resetCdnManagedHttps")
    def reset_cdn_managed_https(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdnManagedHttps", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUserManagedHttps")
    def reset_user_managed_https(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserManagedHttps", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="cdnManagedHttps")
    def cdn_managed_https(
        self,
    ) -> "CdnEndpointCustomDomainCdnManagedHttpsOutputReference":
        return typing.cast("CdnEndpointCustomDomainCdnManagedHttpsOutputReference", jsii.get(self, "cdnManagedHttps"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "CdnEndpointCustomDomainTimeoutsOutputReference":
        return typing.cast("CdnEndpointCustomDomainTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="userManagedHttps")
    def user_managed_https(
        self,
    ) -> "CdnEndpointCustomDomainUserManagedHttpsOutputReference":
        return typing.cast("CdnEndpointCustomDomainUserManagedHttpsOutputReference", jsii.get(self, "userManagedHttps"))

    @builtins.property
    @jsii.member(jsii_name="cdnEndpointIdInput")
    def cdn_endpoint_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdnEndpointIdInput"))

    @builtins.property
    @jsii.member(jsii_name="cdnManagedHttpsInput")
    def cdn_managed_https_input(
        self,
    ) -> typing.Optional["CdnEndpointCustomDomainCdnManagedHttps"]:
        return typing.cast(typing.Optional["CdnEndpointCustomDomainCdnManagedHttps"], jsii.get(self, "cdnManagedHttpsInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["CdnEndpointCustomDomainTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["CdnEndpointCustomDomainTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="userManagedHttpsInput")
    def user_managed_https_input(
        self,
    ) -> typing.Optional["CdnEndpointCustomDomainUserManagedHttps"]:
        return typing.cast(typing.Optional["CdnEndpointCustomDomainUserManagedHttps"], jsii.get(self, "userManagedHttpsInput"))

    @builtins.property
    @jsii.member(jsii_name="cdnEndpointId")
    def cdn_endpoint_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdnEndpointId"))

    @cdn_endpoint_id.setter
    def cdn_endpoint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointCustomDomain, "cdn_endpoint_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdnEndpointId", value)

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointCustomDomain, "host_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointCustomDomain, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointCustomDomain, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpointCustomDomain.CdnEndpointCustomDomainCdnManagedHttps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_type": "certificateType",
        "protocol_type": "protocolType",
        "tls_version": "tlsVersion",
    },
)
class CdnEndpointCustomDomainCdnManagedHttps:
    def __init__(
        self,
        *,
        certificate_type: builtins.str,
        protocol_type: builtins.str,
        tls_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param certificate_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#certificate_type CdnEndpointCustomDomain#certificate_type}.
        :param protocol_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#protocol_type CdnEndpointCustomDomain#protocol_type}.
        :param tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#tls_version CdnEndpointCustomDomain#tls_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointCustomDomainCdnManagedHttps.__init__)
            check_type(argname="argument certificate_type", value=certificate_type, expected_type=type_hints["certificate_type"])
            check_type(argname="argument protocol_type", value=protocol_type, expected_type=type_hints["protocol_type"])
            check_type(argname="argument tls_version", value=tls_version, expected_type=type_hints["tls_version"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate_type": certificate_type,
            "protocol_type": protocol_type,
        }
        if tls_version is not None:
            self._values["tls_version"] = tls_version

    @builtins.property
    def certificate_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#certificate_type CdnEndpointCustomDomain#certificate_type}.'''
        result = self._values.get("certificate_type")
        assert result is not None, "Required property 'certificate_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#protocol_type CdnEndpointCustomDomain#protocol_type}.'''
        result = self._values.get("protocol_type")
        assert result is not None, "Required property 'protocol_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tls_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#tls_version CdnEndpointCustomDomain#tls_version}.'''
        result = self._values.get("tls_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointCustomDomainCdnManagedHttps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointCustomDomainCdnManagedHttpsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpointCustomDomain.CdnEndpointCustomDomainCdnManagedHttpsOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointCustomDomainCdnManagedHttpsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTlsVersion")
    def reset_tls_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsVersion", []))

    @builtins.property
    @jsii.member(jsii_name="certificateTypeInput")
    def certificate_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolTypeInput")
    def protocol_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsVersionInput")
    def tls_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateType")
    def certificate_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateType"))

    @certificate_type.setter
    def certificate_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointCustomDomainCdnManagedHttpsOutputReference, "certificate_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateType", value)

    @builtins.property
    @jsii.member(jsii_name="protocolType")
    def protocol_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocolType"))

    @protocol_type.setter
    def protocol_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointCustomDomainCdnManagedHttpsOutputReference, "protocol_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocolType", value)

    @builtins.property
    @jsii.member(jsii_name="tlsVersion")
    def tls_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsVersion"))

    @tls_version.setter
    def tls_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointCustomDomainCdnManagedHttpsOutputReference, "tls_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CdnEndpointCustomDomainCdnManagedHttps]:
        return typing.cast(typing.Optional[CdnEndpointCustomDomainCdnManagedHttps], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnEndpointCustomDomainCdnManagedHttps],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointCustomDomainCdnManagedHttpsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpointCustomDomain.CdnEndpointCustomDomainConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cdn_endpoint_id": "cdnEndpointId",
        "host_name": "hostName",
        "name": "name",
        "cdn_managed_https": "cdnManagedHttps",
        "id": "id",
        "timeouts": "timeouts",
        "user_managed_https": "userManagedHttps",
    },
)
class CdnEndpointCustomDomainConfig(cdktf.TerraformMetaArguments):
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
        cdn_endpoint_id: builtins.str,
        host_name: builtins.str,
        name: builtins.str,
        cdn_managed_https: typing.Optional[typing.Union[CdnEndpointCustomDomainCdnManagedHttps, typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CdnEndpointCustomDomainTimeouts", typing.Dict[str, typing.Any]]] = None,
        user_managed_https: typing.Optional[typing.Union["CdnEndpointCustomDomainUserManagedHttps", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cdn_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#cdn_endpoint_id CdnEndpointCustomDomain#cdn_endpoint_id}.
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#host_name CdnEndpointCustomDomain#host_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#name CdnEndpointCustomDomain#name}.
        :param cdn_managed_https: cdn_managed_https block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#cdn_managed_https CdnEndpointCustomDomain#cdn_managed_https}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#id CdnEndpointCustomDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#timeouts CdnEndpointCustomDomain#timeouts}
        :param user_managed_https: user_managed_https block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#user_managed_https CdnEndpointCustomDomain#user_managed_https}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cdn_managed_https, dict):
            cdn_managed_https = CdnEndpointCustomDomainCdnManagedHttps(**cdn_managed_https)
        if isinstance(timeouts, dict):
            timeouts = CdnEndpointCustomDomainTimeouts(**timeouts)
        if isinstance(user_managed_https, dict):
            user_managed_https = CdnEndpointCustomDomainUserManagedHttps(**user_managed_https)
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointCustomDomainConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cdn_endpoint_id", value=cdn_endpoint_id, expected_type=type_hints["cdn_endpoint_id"])
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument cdn_managed_https", value=cdn_managed_https, expected_type=type_hints["cdn_managed_https"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument user_managed_https", value=user_managed_https, expected_type=type_hints["user_managed_https"])
        self._values: typing.Dict[str, typing.Any] = {
            "cdn_endpoint_id": cdn_endpoint_id,
            "host_name": host_name,
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
        if cdn_managed_https is not None:
            self._values["cdn_managed_https"] = cdn_managed_https
        if id is not None:
            self._values["id"] = id
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if user_managed_https is not None:
            self._values["user_managed_https"] = user_managed_https

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
    def cdn_endpoint_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#cdn_endpoint_id CdnEndpointCustomDomain#cdn_endpoint_id}.'''
        result = self._values.get("cdn_endpoint_id")
        assert result is not None, "Required property 'cdn_endpoint_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#host_name CdnEndpointCustomDomain#host_name}.'''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#name CdnEndpointCustomDomain#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cdn_managed_https(
        self,
    ) -> typing.Optional[CdnEndpointCustomDomainCdnManagedHttps]:
        '''cdn_managed_https block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#cdn_managed_https CdnEndpointCustomDomain#cdn_managed_https}
        '''
        result = self._values.get("cdn_managed_https")
        return typing.cast(typing.Optional[CdnEndpointCustomDomainCdnManagedHttps], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#id CdnEndpointCustomDomain#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CdnEndpointCustomDomainTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#timeouts CdnEndpointCustomDomain#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CdnEndpointCustomDomainTimeouts"], result)

    @builtins.property
    def user_managed_https(
        self,
    ) -> typing.Optional["CdnEndpointCustomDomainUserManagedHttps"]:
        '''user_managed_https block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#user_managed_https CdnEndpointCustomDomain#user_managed_https}
        '''
        result = self._values.get("user_managed_https")
        return typing.cast(typing.Optional["CdnEndpointCustomDomainUserManagedHttps"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointCustomDomainConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpointCustomDomain.CdnEndpointCustomDomainTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class CdnEndpointCustomDomainTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#create CdnEndpointCustomDomain#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#delete CdnEndpointCustomDomain#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#read CdnEndpointCustomDomain#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#update CdnEndpointCustomDomain#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointCustomDomainTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#create CdnEndpointCustomDomain#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#delete CdnEndpointCustomDomain#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#read CdnEndpointCustomDomain#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#update CdnEndpointCustomDomain#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointCustomDomainTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointCustomDomainTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpointCustomDomain.CdnEndpointCustomDomainTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointCustomDomainTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointCustomDomainTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointCustomDomainTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointCustomDomainTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointCustomDomainTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointCustomDomainTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointCustomDomainTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointCustomDomainTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointCustomDomainTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpointCustomDomain.CdnEndpointCustomDomainUserManagedHttps",
    jsii_struct_bases=[],
    name_mapping={
        "key_vault_certificate_id": "keyVaultCertificateId",
        "key_vault_secret_id": "keyVaultSecretId",
        "tls_version": "tlsVersion",
    },
)
class CdnEndpointCustomDomainUserManagedHttps:
    def __init__(
        self,
        *,
        key_vault_certificate_id: typing.Optional[builtins.str] = None,
        key_vault_secret_id: typing.Optional[builtins.str] = None,
        tls_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_vault_certificate_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#key_vault_certificate_id CdnEndpointCustomDomain#key_vault_certificate_id}.
        :param key_vault_secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#key_vault_secret_id CdnEndpointCustomDomain#key_vault_secret_id}.
        :param tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#tls_version CdnEndpointCustomDomain#tls_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointCustomDomainUserManagedHttps.__init__)
            check_type(argname="argument key_vault_certificate_id", value=key_vault_certificate_id, expected_type=type_hints["key_vault_certificate_id"])
            check_type(argname="argument key_vault_secret_id", value=key_vault_secret_id, expected_type=type_hints["key_vault_secret_id"])
            check_type(argname="argument tls_version", value=tls_version, expected_type=type_hints["tls_version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key_vault_certificate_id is not None:
            self._values["key_vault_certificate_id"] = key_vault_certificate_id
        if key_vault_secret_id is not None:
            self._values["key_vault_secret_id"] = key_vault_secret_id
        if tls_version is not None:
            self._values["tls_version"] = tls_version

    @builtins.property
    def key_vault_certificate_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#key_vault_certificate_id CdnEndpointCustomDomain#key_vault_certificate_id}.'''
        result = self._values.get("key_vault_certificate_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_vault_secret_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#key_vault_secret_id CdnEndpointCustomDomain#key_vault_secret_id}.'''
        result = self._values.get("key_vault_secret_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint_custom_domain#tls_version CdnEndpointCustomDomain#tls_version}.'''
        result = self._values.get("tls_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointCustomDomainUserManagedHttps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointCustomDomainUserManagedHttpsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpointCustomDomain.CdnEndpointCustomDomainUserManagedHttpsOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointCustomDomainUserManagedHttpsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKeyVaultCertificateId")
    def reset_key_vault_certificate_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultCertificateId", []))

    @jsii.member(jsii_name="resetKeyVaultSecretId")
    def reset_key_vault_secret_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultSecretId", []))

    @jsii.member(jsii_name="resetTlsVersion")
    def reset_tls_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsVersion", []))

    @builtins.property
    @jsii.member(jsii_name="keyVaultCertificateIdInput")
    def key_vault_certificate_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultCertificateIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultSecretIdInput")
    def key_vault_secret_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultSecretIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsVersionInput")
    def tls_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultCertificateId")
    def key_vault_certificate_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultCertificateId"))

    @key_vault_certificate_id.setter
    def key_vault_certificate_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointCustomDomainUserManagedHttpsOutputReference, "key_vault_certificate_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultCertificateId", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultSecretId")
    def key_vault_secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultSecretId"))

    @key_vault_secret_id.setter
    def key_vault_secret_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointCustomDomainUserManagedHttpsOutputReference, "key_vault_secret_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultSecretId", value)

    @builtins.property
    @jsii.member(jsii_name="tlsVersion")
    def tls_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsVersion"))

    @tls_version.setter
    def tls_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointCustomDomainUserManagedHttpsOutputReference, "tls_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CdnEndpointCustomDomainUserManagedHttps]:
        return typing.cast(typing.Optional[CdnEndpointCustomDomainUserManagedHttps], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnEndpointCustomDomainUserManagedHttps],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointCustomDomainUserManagedHttpsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CdnEndpointCustomDomain",
    "CdnEndpointCustomDomainCdnManagedHttps",
    "CdnEndpointCustomDomainCdnManagedHttpsOutputReference",
    "CdnEndpointCustomDomainConfig",
    "CdnEndpointCustomDomainTimeouts",
    "CdnEndpointCustomDomainTimeoutsOutputReference",
    "CdnEndpointCustomDomainUserManagedHttps",
    "CdnEndpointCustomDomainUserManagedHttpsOutputReference",
]

publication.publish()
