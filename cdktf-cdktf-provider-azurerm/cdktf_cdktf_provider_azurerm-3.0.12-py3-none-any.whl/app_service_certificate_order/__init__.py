'''
# `azurerm_app_service_certificate_order`

Refer to the Terraform Registory for docs: [`azurerm_app_service_certificate_order`](https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order).
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


class AppServiceCertificateOrder(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.appServiceCertificateOrder.AppServiceCertificateOrder",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order azurerm_app_service_certificate_order}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        auto_renew: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        csr: typing.Optional[builtins.str] = None,
        distinguished_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        key_size: typing.Optional[jsii.Number] = None,
        product_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["AppServiceCertificateOrderTimeouts", typing.Dict[str, typing.Any]]] = None,
        validity_in_years: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order azurerm_app_service_certificate_order} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#location AppServiceCertificateOrder#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#name AppServiceCertificateOrder#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#resource_group_name AppServiceCertificateOrder#resource_group_name}.
        :param auto_renew: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#auto_renew AppServiceCertificateOrder#auto_renew}.
        :param csr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#csr AppServiceCertificateOrder#csr}.
        :param distinguished_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#distinguished_name AppServiceCertificateOrder#distinguished_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#id AppServiceCertificateOrder#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param key_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#key_size AppServiceCertificateOrder#key_size}.
        :param product_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#product_type AppServiceCertificateOrder#product_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#tags AppServiceCertificateOrder#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#timeouts AppServiceCertificateOrder#timeouts}
        :param validity_in_years: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#validity_in_years AppServiceCertificateOrder#validity_in_years}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppServiceCertificateOrder.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppServiceCertificateOrderConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            auto_renew=auto_renew,
            csr=csr,
            distinguished_name=distinguished_name,
            id=id,
            key_size=key_size,
            product_type=product_type,
            tags=tags,
            timeouts=timeouts,
            validity_in_years=validity_in_years,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#create AppServiceCertificateOrder#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#delete AppServiceCertificateOrder#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#read AppServiceCertificateOrder#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#update AppServiceCertificateOrder#update}.
        '''
        value = AppServiceCertificateOrderTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAutoRenew")
    def reset_auto_renew(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoRenew", []))

    @jsii.member(jsii_name="resetCsr")
    def reset_csr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsr", []))

    @jsii.member(jsii_name="resetDistinguishedName")
    def reset_distinguished_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDistinguishedName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKeySize")
    def reset_key_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeySize", []))

    @jsii.member(jsii_name="resetProductType")
    def reset_product_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProductType", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetValidityInYears")
    def reset_validity_in_years(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidityInYears", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="appServiceCertificateNotRenewableReasons")
    def app_service_certificate_not_renewable_reasons(
        self,
    ) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "appServiceCertificateNotRenewableReasons"))

    @builtins.property
    @jsii.member(jsii_name="certificates")
    def certificates(self) -> "AppServiceCertificateOrderCertificatesList":
        return typing.cast("AppServiceCertificateOrderCertificatesList", jsii.get(self, "certificates"))

    @builtins.property
    @jsii.member(jsii_name="domainVerificationToken")
    def domain_verification_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainVerificationToken"))

    @builtins.property
    @jsii.member(jsii_name="expirationTime")
    def expiration_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expirationTime"))

    @builtins.property
    @jsii.member(jsii_name="intermediateThumbprint")
    def intermediate_thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intermediateThumbprint"))

    @builtins.property
    @jsii.member(jsii_name="isPrivateKeyExternal")
    def is_private_key_external(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "isPrivateKeyExternal"))

    @builtins.property
    @jsii.member(jsii_name="rootThumbprint")
    def root_thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootThumbprint"))

    @builtins.property
    @jsii.member(jsii_name="signedCertificateThumbprint")
    def signed_certificate_thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signedCertificateThumbprint"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "AppServiceCertificateOrderTimeoutsOutputReference":
        return typing.cast("AppServiceCertificateOrderTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="autoRenewInput")
    def auto_renew_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoRenewInput"))

    @builtins.property
    @jsii.member(jsii_name="csrInput")
    def csr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "csrInput"))

    @builtins.property
    @jsii.member(jsii_name="distinguishedNameInput")
    def distinguished_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "distinguishedNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="keySizeInput")
    def key_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "keySizeInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="productTypeInput")
    def product_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "productTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["AppServiceCertificateOrderTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["AppServiceCertificateOrderTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="validityInYearsInput")
    def validity_in_years_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "validityInYearsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoRenew")
    def auto_renew(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoRenew"))

    @auto_renew.setter
    def auto_renew(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrder, "auto_renew").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoRenew", value)

    @builtins.property
    @jsii.member(jsii_name="csr")
    def csr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "csr"))

    @csr.setter
    def csr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrder, "csr").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csr", value)

    @builtins.property
    @jsii.member(jsii_name="distinguishedName")
    def distinguished_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "distinguishedName"))

    @distinguished_name.setter
    def distinguished_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrder, "distinguished_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distinguishedName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrder, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="keySize")
    def key_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "keySize"))

    @key_size.setter
    def key_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrder, "key_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keySize", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrder, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrder, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="productType")
    def product_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "productType"))

    @product_type.setter
    def product_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrder, "product_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrder, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrder, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="validityInYears")
    def validity_in_years(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "validityInYears"))

    @validity_in_years.setter
    def validity_in_years(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrder, "validity_in_years").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validityInYears", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.appServiceCertificateOrder.AppServiceCertificateOrderCertificates",
    jsii_struct_bases=[],
    name_mapping={},
)
class AppServiceCertificateOrderCertificates:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppServiceCertificateOrderCertificates(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppServiceCertificateOrderCertificatesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.appServiceCertificateOrder.AppServiceCertificateOrderCertificatesList",
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
            type_hints = typing.get_type_hints(AppServiceCertificateOrderCertificatesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AppServiceCertificateOrderCertificatesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppServiceCertificateOrderCertificatesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppServiceCertificateOrderCertificatesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrderCertificatesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrderCertificatesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrderCertificatesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class AppServiceCertificateOrderCertificatesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.appServiceCertificateOrder.AppServiceCertificateOrderCertificatesOutputReference",
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
            type_hints = typing.get_type_hints(AppServiceCertificateOrderCertificatesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="certificateName")
    def certificate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateName"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultId")
    def key_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultId"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultSecretName")
    def key_vault_secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultSecretName"))

    @builtins.property
    @jsii.member(jsii_name="provisioningState")
    def provisioning_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "provisioningState"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppServiceCertificateOrderCertificates]:
        return typing.cast(typing.Optional[AppServiceCertificateOrderCertificates], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppServiceCertificateOrderCertificates],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrderCertificatesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.appServiceCertificateOrder.AppServiceCertificateOrderConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "auto_renew": "autoRenew",
        "csr": "csr",
        "distinguished_name": "distinguishedName",
        "id": "id",
        "key_size": "keySize",
        "product_type": "productType",
        "tags": "tags",
        "timeouts": "timeouts",
        "validity_in_years": "validityInYears",
    },
)
class AppServiceCertificateOrderConfig(cdktf.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        auto_renew: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        csr: typing.Optional[builtins.str] = None,
        distinguished_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        key_size: typing.Optional[jsii.Number] = None,
        product_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["AppServiceCertificateOrderTimeouts", typing.Dict[str, typing.Any]]] = None,
        validity_in_years: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#location AppServiceCertificateOrder#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#name AppServiceCertificateOrder#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#resource_group_name AppServiceCertificateOrder#resource_group_name}.
        :param auto_renew: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#auto_renew AppServiceCertificateOrder#auto_renew}.
        :param csr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#csr AppServiceCertificateOrder#csr}.
        :param distinguished_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#distinguished_name AppServiceCertificateOrder#distinguished_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#id AppServiceCertificateOrder#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param key_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#key_size AppServiceCertificateOrder#key_size}.
        :param product_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#product_type AppServiceCertificateOrder#product_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#tags AppServiceCertificateOrder#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#timeouts AppServiceCertificateOrder#timeouts}
        :param validity_in_years: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#validity_in_years AppServiceCertificateOrder#validity_in_years}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = AppServiceCertificateOrderTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(AppServiceCertificateOrderConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument auto_renew", value=auto_renew, expected_type=type_hints["auto_renew"])
            check_type(argname="argument csr", value=csr, expected_type=type_hints["csr"])
            check_type(argname="argument distinguished_name", value=distinguished_name, expected_type=type_hints["distinguished_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument key_size", value=key_size, expected_type=type_hints["key_size"])
            check_type(argname="argument product_type", value=product_type, expected_type=type_hints["product_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument validity_in_years", value=validity_in_years, expected_type=type_hints["validity_in_years"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
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
        if auto_renew is not None:
            self._values["auto_renew"] = auto_renew
        if csr is not None:
            self._values["csr"] = csr
        if distinguished_name is not None:
            self._values["distinguished_name"] = distinguished_name
        if id is not None:
            self._values["id"] = id
        if key_size is not None:
            self._values["key_size"] = key_size
        if product_type is not None:
            self._values["product_type"] = product_type
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if validity_in_years is not None:
            self._values["validity_in_years"] = validity_in_years

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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#location AppServiceCertificateOrder#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#name AppServiceCertificateOrder#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#resource_group_name AppServiceCertificateOrder#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_renew(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#auto_renew AppServiceCertificateOrder#auto_renew}.'''
        result = self._values.get("auto_renew")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def csr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#csr AppServiceCertificateOrder#csr}.'''
        result = self._values.get("csr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def distinguished_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#distinguished_name AppServiceCertificateOrder#distinguished_name}.'''
        result = self._values.get("distinguished_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#id AppServiceCertificateOrder#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#key_size AppServiceCertificateOrder#key_size}.'''
        result = self._values.get("key_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def product_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#product_type AppServiceCertificateOrder#product_type}.'''
        result = self._values.get("product_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#tags AppServiceCertificateOrder#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["AppServiceCertificateOrderTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#timeouts AppServiceCertificateOrder#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["AppServiceCertificateOrderTimeouts"], result)

    @builtins.property
    def validity_in_years(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#validity_in_years AppServiceCertificateOrder#validity_in_years}.'''
        result = self._values.get("validity_in_years")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppServiceCertificateOrderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.appServiceCertificateOrder.AppServiceCertificateOrderTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class AppServiceCertificateOrderTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#create AppServiceCertificateOrder#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#delete AppServiceCertificateOrder#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#read AppServiceCertificateOrder#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#update AppServiceCertificateOrder#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppServiceCertificateOrderTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#create AppServiceCertificateOrder#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#delete AppServiceCertificateOrder#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#read AppServiceCertificateOrder#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_certificate_order#update AppServiceCertificateOrder#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppServiceCertificateOrderTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppServiceCertificateOrderTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.appServiceCertificateOrder.AppServiceCertificateOrderTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(AppServiceCertificateOrderTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrderTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrderTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrderTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrderTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppServiceCertificateOrderTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppServiceCertificateOrderTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppServiceCertificateOrderTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceCertificateOrderTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppServiceCertificateOrder",
    "AppServiceCertificateOrderCertificates",
    "AppServiceCertificateOrderCertificatesList",
    "AppServiceCertificateOrderCertificatesOutputReference",
    "AppServiceCertificateOrderConfig",
    "AppServiceCertificateOrderTimeouts",
    "AppServiceCertificateOrderTimeoutsOutputReference",
]

publication.publish()
