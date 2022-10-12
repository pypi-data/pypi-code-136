'''
# `azurerm_confidential_ledger`

Refer to the Terraform Registory for docs: [`azurerm_confidential_ledger`](https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger).
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


class ConfidentialLedger(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.confidentialLedger.ConfidentialLedger",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger azurerm_confidential_ledger}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        azuread_based_service_principal: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConfidentialLedgerAzureadBasedServicePrincipal", typing.Dict[str, typing.Any]]]],
        ledger_type: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        certificate_based_security_principal: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConfidentialLedgerCertificateBasedSecurityPrincipal", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ConfidentialLedgerTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger azurerm_confidential_ledger} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param azuread_based_service_principal: azuread_based_service_principal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#azuread_based_service_principal ConfidentialLedger#azuread_based_service_principal}
        :param ledger_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#ledger_type ConfidentialLedger#ledger_type}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#location ConfidentialLedger#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#name ConfidentialLedger#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#resource_group_name ConfidentialLedger#resource_group_name}.
        :param certificate_based_security_principal: certificate_based_security_principal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#certificate_based_security_principal ConfidentialLedger#certificate_based_security_principal}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#id ConfidentialLedger#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#tags ConfidentialLedger#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#timeouts ConfidentialLedger#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfidentialLedger.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ConfidentialLedgerConfig(
            azuread_based_service_principal=azuread_based_service_principal,
            ledger_type=ledger_type,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            certificate_based_security_principal=certificate_based_security_principal,
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

    @jsii.member(jsii_name="putAzureadBasedServicePrincipal")
    def put_azuread_based_service_principal(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConfidentialLedgerAzureadBasedServicePrincipal", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfidentialLedger.put_azuread_based_service_principal)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAzureadBasedServicePrincipal", [value]))

    @jsii.member(jsii_name="putCertificateBasedSecurityPrincipal")
    def put_certificate_based_security_principal(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConfidentialLedgerCertificateBasedSecurityPrincipal", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfidentialLedger.put_certificate_based_security_principal)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCertificateBasedSecurityPrincipal", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#create ConfidentialLedger#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#delete ConfidentialLedger#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#read ConfidentialLedger#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#update ConfidentialLedger#update}.
        '''
        value = ConfidentialLedgerTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCertificateBasedSecurityPrincipal")
    def reset_certificate_based_security_principal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateBasedSecurityPrincipal", []))

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
    @jsii.member(jsii_name="azureadBasedServicePrincipal")
    def azuread_based_service_principal(
        self,
    ) -> "ConfidentialLedgerAzureadBasedServicePrincipalList":
        return typing.cast("ConfidentialLedgerAzureadBasedServicePrincipalList", jsii.get(self, "azureadBasedServicePrincipal"))

    @builtins.property
    @jsii.member(jsii_name="certificateBasedSecurityPrincipal")
    def certificate_based_security_principal(
        self,
    ) -> "ConfidentialLedgerCertificateBasedSecurityPrincipalList":
        return typing.cast("ConfidentialLedgerCertificateBasedSecurityPrincipalList", jsii.get(self, "certificateBasedSecurityPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="identityServiceEndpoint")
    def identity_service_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityServiceEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="ledgerEndpoint")
    def ledger_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ledgerEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ConfidentialLedgerTimeoutsOutputReference":
        return typing.cast("ConfidentialLedgerTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="azureadBasedServicePrincipalInput")
    def azuread_based_service_principal_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConfidentialLedgerAzureadBasedServicePrincipal"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConfidentialLedgerAzureadBasedServicePrincipal"]]], jsii.get(self, "azureadBasedServicePrincipalInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateBasedSecurityPrincipalInput")
    def certificate_based_security_principal_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConfidentialLedgerCertificateBasedSecurityPrincipal"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConfidentialLedgerCertificateBasedSecurityPrincipal"]]], jsii.get(self, "certificateBasedSecurityPrincipalInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ledgerTypeInput")
    def ledger_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ledgerTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

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
    ) -> typing.Optional[typing.Union["ConfidentialLedgerTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ConfidentialLedgerTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedger, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ledgerType")
    def ledger_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ledgerType"))

    @ledger_type.setter
    def ledger_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedger, "ledger_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ledgerType", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedger, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedger, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedger, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedger, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.confidentialLedger.ConfidentialLedgerAzureadBasedServicePrincipal",
    jsii_struct_bases=[],
    name_mapping={
        "ledger_role_name": "ledgerRoleName",
        "principal_id": "principalId",
        "tenant_id": "tenantId",
    },
)
class ConfidentialLedgerAzureadBasedServicePrincipal:
    def __init__(
        self,
        *,
        ledger_role_name: builtins.str,
        principal_id: builtins.str,
        tenant_id: builtins.str,
    ) -> None:
        '''
        :param ledger_role_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#ledger_role_name ConfidentialLedger#ledger_role_name}.
        :param principal_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#principal_id ConfidentialLedger#principal_id}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#tenant_id ConfidentialLedger#tenant_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfidentialLedgerAzureadBasedServicePrincipal.__init__)
            check_type(argname="argument ledger_role_name", value=ledger_role_name, expected_type=type_hints["ledger_role_name"])
            check_type(argname="argument principal_id", value=principal_id, expected_type=type_hints["principal_id"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "ledger_role_name": ledger_role_name,
            "principal_id": principal_id,
            "tenant_id": tenant_id,
        }

    @builtins.property
    def ledger_role_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#ledger_role_name ConfidentialLedger#ledger_role_name}.'''
        result = self._values.get("ledger_role_name")
        assert result is not None, "Required property 'ledger_role_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#principal_id ConfidentialLedger#principal_id}.'''
        result = self._values.get("principal_id")
        assert result is not None, "Required property 'principal_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tenant_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#tenant_id ConfidentialLedger#tenant_id}.'''
        result = self._values.get("tenant_id")
        assert result is not None, "Required property 'tenant_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfidentialLedgerAzureadBasedServicePrincipal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConfidentialLedgerAzureadBasedServicePrincipalList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.confidentialLedger.ConfidentialLedgerAzureadBasedServicePrincipalList",
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
            type_hints = typing.get_type_hints(ConfidentialLedgerAzureadBasedServicePrincipalList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ConfidentialLedgerAzureadBasedServicePrincipalOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfidentialLedgerAzureadBasedServicePrincipalList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ConfidentialLedgerAzureadBasedServicePrincipalOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerAzureadBasedServicePrincipalList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerAzureadBasedServicePrincipalList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerAzureadBasedServicePrincipalList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConfidentialLedgerAzureadBasedServicePrincipal]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConfidentialLedgerAzureadBasedServicePrincipal]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConfidentialLedgerAzureadBasedServicePrincipal]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerAzureadBasedServicePrincipalList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ConfidentialLedgerAzureadBasedServicePrincipalOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.confidentialLedger.ConfidentialLedgerAzureadBasedServicePrincipalOutputReference",
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
            type_hints = typing.get_type_hints(ConfidentialLedgerAzureadBasedServicePrincipalOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="ledgerRoleNameInput")
    def ledger_role_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ledgerRoleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="principalIdInput")
    def principal_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="ledgerRoleName")
    def ledger_role_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ledgerRoleName"))

    @ledger_role_name.setter
    def ledger_role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerAzureadBasedServicePrincipalOutputReference, "ledger_role_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ledgerRoleName", value)

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @principal_id.setter
    def principal_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerAzureadBasedServicePrincipalOutputReference, "principal_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principalId", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerAzureadBasedServicePrincipalOutputReference, "tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ConfidentialLedgerAzureadBasedServicePrincipal, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ConfidentialLedgerAzureadBasedServicePrincipal, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ConfidentialLedgerAzureadBasedServicePrincipal, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerAzureadBasedServicePrincipalOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.confidentialLedger.ConfidentialLedgerCertificateBasedSecurityPrincipal",
    jsii_struct_bases=[],
    name_mapping={
        "ledger_role_name": "ledgerRoleName",
        "pem_public_key": "pemPublicKey",
    },
)
class ConfidentialLedgerCertificateBasedSecurityPrincipal:
    def __init__(
        self,
        *,
        ledger_role_name: builtins.str,
        pem_public_key: builtins.str,
    ) -> None:
        '''
        :param ledger_role_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#ledger_role_name ConfidentialLedger#ledger_role_name}.
        :param pem_public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#pem_public_key ConfidentialLedger#pem_public_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfidentialLedgerCertificateBasedSecurityPrincipal.__init__)
            check_type(argname="argument ledger_role_name", value=ledger_role_name, expected_type=type_hints["ledger_role_name"])
            check_type(argname="argument pem_public_key", value=pem_public_key, expected_type=type_hints["pem_public_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "ledger_role_name": ledger_role_name,
            "pem_public_key": pem_public_key,
        }

    @builtins.property
    def ledger_role_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#ledger_role_name ConfidentialLedger#ledger_role_name}.'''
        result = self._values.get("ledger_role_name")
        assert result is not None, "Required property 'ledger_role_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pem_public_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#pem_public_key ConfidentialLedger#pem_public_key}.'''
        result = self._values.get("pem_public_key")
        assert result is not None, "Required property 'pem_public_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfidentialLedgerCertificateBasedSecurityPrincipal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConfidentialLedgerCertificateBasedSecurityPrincipalList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.confidentialLedger.ConfidentialLedgerCertificateBasedSecurityPrincipalList",
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
            type_hints = typing.get_type_hints(ConfidentialLedgerCertificateBasedSecurityPrincipalList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ConfidentialLedgerCertificateBasedSecurityPrincipalOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfidentialLedgerCertificateBasedSecurityPrincipalList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ConfidentialLedgerCertificateBasedSecurityPrincipalOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerCertificateBasedSecurityPrincipalList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerCertificateBasedSecurityPrincipalList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerCertificateBasedSecurityPrincipalList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConfidentialLedgerCertificateBasedSecurityPrincipal]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConfidentialLedgerCertificateBasedSecurityPrincipal]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConfidentialLedgerCertificateBasedSecurityPrincipal]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerCertificateBasedSecurityPrincipalList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ConfidentialLedgerCertificateBasedSecurityPrincipalOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.confidentialLedger.ConfidentialLedgerCertificateBasedSecurityPrincipalOutputReference",
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
            type_hints = typing.get_type_hints(ConfidentialLedgerCertificateBasedSecurityPrincipalOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="ledgerRoleNameInput")
    def ledger_role_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ledgerRoleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="pemPublicKeyInput")
    def pem_public_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pemPublicKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="ledgerRoleName")
    def ledger_role_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ledgerRoleName"))

    @ledger_role_name.setter
    def ledger_role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerCertificateBasedSecurityPrincipalOutputReference, "ledger_role_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ledgerRoleName", value)

    @builtins.property
    @jsii.member(jsii_name="pemPublicKey")
    def pem_public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pemPublicKey"))

    @pem_public_key.setter
    def pem_public_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerCertificateBasedSecurityPrincipalOutputReference, "pem_public_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pemPublicKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ConfidentialLedgerCertificateBasedSecurityPrincipal, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ConfidentialLedgerCertificateBasedSecurityPrincipal, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ConfidentialLedgerCertificateBasedSecurityPrincipal, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerCertificateBasedSecurityPrincipalOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.confidentialLedger.ConfidentialLedgerConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "azuread_based_service_principal": "azureadBasedServicePrincipal",
        "ledger_type": "ledgerType",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "certificate_based_security_principal": "certificateBasedSecurityPrincipal",
        "id": "id",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class ConfidentialLedgerConfig(cdktf.TerraformMetaArguments):
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
        azuread_based_service_principal: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ConfidentialLedgerAzureadBasedServicePrincipal, typing.Dict[str, typing.Any]]]],
        ledger_type: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        certificate_based_security_principal: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ConfidentialLedgerCertificateBasedSecurityPrincipal, typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ConfidentialLedgerTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param azuread_based_service_principal: azuread_based_service_principal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#azuread_based_service_principal ConfidentialLedger#azuread_based_service_principal}
        :param ledger_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#ledger_type ConfidentialLedger#ledger_type}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#location ConfidentialLedger#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#name ConfidentialLedger#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#resource_group_name ConfidentialLedger#resource_group_name}.
        :param certificate_based_security_principal: certificate_based_security_principal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#certificate_based_security_principal ConfidentialLedger#certificate_based_security_principal}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#id ConfidentialLedger#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#tags ConfidentialLedger#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#timeouts ConfidentialLedger#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = ConfidentialLedgerTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ConfidentialLedgerConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument azuread_based_service_principal", value=azuread_based_service_principal, expected_type=type_hints["azuread_based_service_principal"])
            check_type(argname="argument ledger_type", value=ledger_type, expected_type=type_hints["ledger_type"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument certificate_based_security_principal", value=certificate_based_security_principal, expected_type=type_hints["certificate_based_security_principal"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "azuread_based_service_principal": azuread_based_service_principal,
            "ledger_type": ledger_type,
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
        if certificate_based_security_principal is not None:
            self._values["certificate_based_security_principal"] = certificate_based_security_principal
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
    def azuread_based_service_principal(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List[ConfidentialLedgerAzureadBasedServicePrincipal]]:
        '''azuread_based_service_principal block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#azuread_based_service_principal ConfidentialLedger#azuread_based_service_principal}
        '''
        result = self._values.get("azuread_based_service_principal")
        assert result is not None, "Required property 'azuread_based_service_principal' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List[ConfidentialLedgerAzureadBasedServicePrincipal]], result)

    @builtins.property
    def ledger_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#ledger_type ConfidentialLedger#ledger_type}.'''
        result = self._values.get("ledger_type")
        assert result is not None, "Required property 'ledger_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#location ConfidentialLedger#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#name ConfidentialLedger#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#resource_group_name ConfidentialLedger#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_based_security_principal(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConfidentialLedgerCertificateBasedSecurityPrincipal]]]:
        '''certificate_based_security_principal block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#certificate_based_security_principal ConfidentialLedger#certificate_based_security_principal}
        '''
        result = self._values.get("certificate_based_security_principal")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ConfidentialLedgerCertificateBasedSecurityPrincipal]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#id ConfidentialLedger#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#tags ConfidentialLedger#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ConfidentialLedgerTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#timeouts ConfidentialLedger#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ConfidentialLedgerTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfidentialLedgerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.confidentialLedger.ConfidentialLedgerTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ConfidentialLedgerTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#create ConfidentialLedger#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#delete ConfidentialLedger#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#read ConfidentialLedger#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#update ConfidentialLedger#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfidentialLedgerTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#create ConfidentialLedger#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#delete ConfidentialLedger#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#read ConfidentialLedger#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/confidential_ledger#update ConfidentialLedger#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfidentialLedgerTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConfidentialLedgerTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.confidentialLedger.ConfidentialLedgerTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ConfidentialLedgerTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ConfidentialLedgerTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ConfidentialLedgerTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ConfidentialLedgerTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfidentialLedgerTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ConfidentialLedger",
    "ConfidentialLedgerAzureadBasedServicePrincipal",
    "ConfidentialLedgerAzureadBasedServicePrincipalList",
    "ConfidentialLedgerAzureadBasedServicePrincipalOutputReference",
    "ConfidentialLedgerCertificateBasedSecurityPrincipal",
    "ConfidentialLedgerCertificateBasedSecurityPrincipalList",
    "ConfidentialLedgerCertificateBasedSecurityPrincipalOutputReference",
    "ConfidentialLedgerConfig",
    "ConfidentialLedgerTimeouts",
    "ConfidentialLedgerTimeoutsOutputReference",
]

publication.publish()
