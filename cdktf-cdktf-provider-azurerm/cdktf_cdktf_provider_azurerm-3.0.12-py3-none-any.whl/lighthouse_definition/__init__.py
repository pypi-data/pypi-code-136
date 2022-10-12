'''
# `azurerm_lighthouse_definition`

Refer to the Terraform Registory for docs: [`azurerm_lighthouse_definition`](https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition).
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


class LighthouseDefinition(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.lighthouseDefinition.LighthouseDefinition",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition azurerm_lighthouse_definition}.'''

    def __init__(
        self,
        scope_: constructs.Construct,
        id_: builtins.str,
        *,
        authorization: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LighthouseDefinitionAuthorization", typing.Dict[str, typing.Any]]]],
        managing_tenant_id: builtins.str,
        name: builtins.str,
        scope: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        lighthouse_definition_id: typing.Optional[builtins.str] = None,
        plan: typing.Optional[typing.Union["LighthouseDefinitionPlan", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["LighthouseDefinitionTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition azurerm_lighthouse_definition} Resource.

        :param scope_: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param authorization: authorization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#authorization LighthouseDefinition#authorization}
        :param managing_tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#managing_tenant_id LighthouseDefinition#managing_tenant_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#name LighthouseDefinition#name}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#scope LighthouseDefinition#scope}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#description LighthouseDefinition#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#id LighthouseDefinition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lighthouse_definition_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#lighthouse_definition_id LighthouseDefinition#lighthouse_definition_id}.
        :param plan: plan block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#plan LighthouseDefinition#plan}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#timeouts LighthouseDefinition#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LighthouseDefinition.__init__)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LighthouseDefinitionConfig(
            authorization=authorization,
            managing_tenant_id=managing_tenant_id,
            name=name,
            scope=scope,
            description=description,
            id=id,
            lighthouse_definition_id=lighthouse_definition_id,
            plan=plan,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope_, id_, config])

    @jsii.member(jsii_name="putAuthorization")
    def put_authorization(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LighthouseDefinitionAuthorization", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LighthouseDefinition.put_authorization)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAuthorization", [value]))

    @jsii.member(jsii_name="putPlan")
    def put_plan(
        self,
        *,
        name: builtins.str,
        product: builtins.str,
        publisher: builtins.str,
        version: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#name LighthouseDefinition#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#product LighthouseDefinition#product}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#publisher LighthouseDefinition#publisher}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#version LighthouseDefinition#version}.
        '''
        value = LighthouseDefinitionPlan(
            name=name, product=product, publisher=publisher, version=version
        )

        return typing.cast(None, jsii.invoke(self, "putPlan", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#create LighthouseDefinition#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#delete LighthouseDefinition#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#read LighthouseDefinition#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#update LighthouseDefinition#update}.
        '''
        value = LighthouseDefinitionTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLighthouseDefinitionId")
    def reset_lighthouse_definition_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLighthouseDefinitionId", []))

    @jsii.member(jsii_name="resetPlan")
    def reset_plan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlan", []))

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
    @jsii.member(jsii_name="authorization")
    def authorization(self) -> "LighthouseDefinitionAuthorizationList":
        return typing.cast("LighthouseDefinitionAuthorizationList", jsii.get(self, "authorization"))

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(self) -> "LighthouseDefinitionPlanOutputReference":
        return typing.cast("LighthouseDefinitionPlanOutputReference", jsii.get(self, "plan"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LighthouseDefinitionTimeoutsOutputReference":
        return typing.cast("LighthouseDefinitionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="authorizationInput")
    def authorization_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LighthouseDefinitionAuthorization"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LighthouseDefinitionAuthorization"]]], jsii.get(self, "authorizationInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lighthouseDefinitionIdInput")
    def lighthouse_definition_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lighthouseDefinitionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="managingTenantIdInput")
    def managing_tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managingTenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(self) -> typing.Optional["LighthouseDefinitionPlan"]:
        return typing.cast(typing.Optional["LighthouseDefinitionPlan"], jsii.get(self, "planInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LighthouseDefinitionTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LighthouseDefinitionTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinition, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinition, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="lighthouseDefinitionId")
    def lighthouse_definition_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lighthouseDefinitionId"))

    @lighthouse_definition_id.setter
    def lighthouse_definition_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinition, "lighthouse_definition_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lighthouseDefinitionId", value)

    @builtins.property
    @jsii.member(jsii_name="managingTenantId")
    def managing_tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managingTenantId"))

    @managing_tenant_id.setter
    def managing_tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinition, "managing_tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managingTenantId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinition, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinition, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.lighthouseDefinition.LighthouseDefinitionAuthorization",
    jsii_struct_bases=[],
    name_mapping={
        "principal_id": "principalId",
        "role_definition_id": "roleDefinitionId",
        "delegated_role_definition_ids": "delegatedRoleDefinitionIds",
        "principal_display_name": "principalDisplayName",
    },
)
class LighthouseDefinitionAuthorization:
    def __init__(
        self,
        *,
        principal_id: builtins.str,
        role_definition_id: builtins.str,
        delegated_role_definition_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        principal_display_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param principal_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#principal_id LighthouseDefinition#principal_id}.
        :param role_definition_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#role_definition_id LighthouseDefinition#role_definition_id}.
        :param delegated_role_definition_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#delegated_role_definition_ids LighthouseDefinition#delegated_role_definition_ids}.
        :param principal_display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#principal_display_name LighthouseDefinition#principal_display_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LighthouseDefinitionAuthorization.__init__)
            check_type(argname="argument principal_id", value=principal_id, expected_type=type_hints["principal_id"])
            check_type(argname="argument role_definition_id", value=role_definition_id, expected_type=type_hints["role_definition_id"])
            check_type(argname="argument delegated_role_definition_ids", value=delegated_role_definition_ids, expected_type=type_hints["delegated_role_definition_ids"])
            check_type(argname="argument principal_display_name", value=principal_display_name, expected_type=type_hints["principal_display_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "principal_id": principal_id,
            "role_definition_id": role_definition_id,
        }
        if delegated_role_definition_ids is not None:
            self._values["delegated_role_definition_ids"] = delegated_role_definition_ids
        if principal_display_name is not None:
            self._values["principal_display_name"] = principal_display_name

    @builtins.property
    def principal_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#principal_id LighthouseDefinition#principal_id}.'''
        result = self._values.get("principal_id")
        assert result is not None, "Required property 'principal_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_definition_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#role_definition_id LighthouseDefinition#role_definition_id}.'''
        result = self._values.get("role_definition_id")
        assert result is not None, "Required property 'role_definition_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delegated_role_definition_ids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#delegated_role_definition_ids LighthouseDefinition#delegated_role_definition_ids}.'''
        result = self._values.get("delegated_role_definition_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def principal_display_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#principal_display_name LighthouseDefinition#principal_display_name}.'''
        result = self._values.get("principal_display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LighthouseDefinitionAuthorization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LighthouseDefinitionAuthorizationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.lighthouseDefinition.LighthouseDefinitionAuthorizationList",
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
            type_hints = typing.get_type_hints(LighthouseDefinitionAuthorizationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LighthouseDefinitionAuthorizationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LighthouseDefinitionAuthorizationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LighthouseDefinitionAuthorizationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionAuthorizationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionAuthorizationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionAuthorizationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LighthouseDefinitionAuthorization]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LighthouseDefinitionAuthorization]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LighthouseDefinitionAuthorization]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionAuthorizationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LighthouseDefinitionAuthorizationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.lighthouseDefinition.LighthouseDefinitionAuthorizationOutputReference",
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
            type_hints = typing.get_type_hints(LighthouseDefinitionAuthorizationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDelegatedRoleDefinitionIds")
    def reset_delegated_role_definition_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelegatedRoleDefinitionIds", []))

    @jsii.member(jsii_name="resetPrincipalDisplayName")
    def reset_principal_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrincipalDisplayName", []))

    @builtins.property
    @jsii.member(jsii_name="delegatedRoleDefinitionIdsInput")
    def delegated_role_definition_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "delegatedRoleDefinitionIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="principalDisplayNameInput")
    def principal_display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalDisplayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="principalIdInput")
    def principal_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalIdInput"))

    @builtins.property
    @jsii.member(jsii_name="roleDefinitionIdInput")
    def role_definition_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleDefinitionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="delegatedRoleDefinitionIds")
    def delegated_role_definition_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "delegatedRoleDefinitionIds"))

    @delegated_role_definition_ids.setter
    def delegated_role_definition_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionAuthorizationOutputReference, "delegated_role_definition_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delegatedRoleDefinitionIds", value)

    @builtins.property
    @jsii.member(jsii_name="principalDisplayName")
    def principal_display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalDisplayName"))

    @principal_display_name.setter
    def principal_display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionAuthorizationOutputReference, "principal_display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principalDisplayName", value)

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @principal_id.setter
    def principal_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionAuthorizationOutputReference, "principal_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principalId", value)

    @builtins.property
    @jsii.member(jsii_name="roleDefinitionId")
    def role_definition_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleDefinitionId"))

    @role_definition_id.setter
    def role_definition_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionAuthorizationOutputReference, "role_definition_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleDefinitionId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LighthouseDefinitionAuthorization, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LighthouseDefinitionAuthorization, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LighthouseDefinitionAuthorization, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionAuthorizationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.lighthouseDefinition.LighthouseDefinitionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "authorization": "authorization",
        "managing_tenant_id": "managingTenantId",
        "name": "name",
        "scope": "scope",
        "description": "description",
        "id": "id",
        "lighthouse_definition_id": "lighthouseDefinitionId",
        "plan": "plan",
        "timeouts": "timeouts",
    },
)
class LighthouseDefinitionConfig(cdktf.TerraformMetaArguments):
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
        authorization: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LighthouseDefinitionAuthorization, typing.Dict[str, typing.Any]]]],
        managing_tenant_id: builtins.str,
        name: builtins.str,
        scope: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        lighthouse_definition_id: typing.Optional[builtins.str] = None,
        plan: typing.Optional[typing.Union["LighthouseDefinitionPlan", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["LighthouseDefinitionTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param authorization: authorization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#authorization LighthouseDefinition#authorization}
        :param managing_tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#managing_tenant_id LighthouseDefinition#managing_tenant_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#name LighthouseDefinition#name}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#scope LighthouseDefinition#scope}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#description LighthouseDefinition#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#id LighthouseDefinition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lighthouse_definition_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#lighthouse_definition_id LighthouseDefinition#lighthouse_definition_id}.
        :param plan: plan block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#plan LighthouseDefinition#plan}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#timeouts LighthouseDefinition#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(plan, dict):
            plan = LighthouseDefinitionPlan(**plan)
        if isinstance(timeouts, dict):
            timeouts = LighthouseDefinitionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(LighthouseDefinitionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument authorization", value=authorization, expected_type=type_hints["authorization"])
            check_type(argname="argument managing_tenant_id", value=managing_tenant_id, expected_type=type_hints["managing_tenant_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lighthouse_definition_id", value=lighthouse_definition_id, expected_type=type_hints["lighthouse_definition_id"])
            check_type(argname="argument plan", value=plan, expected_type=type_hints["plan"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "authorization": authorization,
            "managing_tenant_id": managing_tenant_id,
            "name": name,
            "scope": scope,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if lighthouse_definition_id is not None:
            self._values["lighthouse_definition_id"] = lighthouse_definition_id
        if plan is not None:
            self._values["plan"] = plan
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
    def authorization(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List[LighthouseDefinitionAuthorization]]:
        '''authorization block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#authorization LighthouseDefinition#authorization}
        '''
        result = self._values.get("authorization")
        assert result is not None, "Required property 'authorization' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List[LighthouseDefinitionAuthorization]], result)

    @builtins.property
    def managing_tenant_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#managing_tenant_id LighthouseDefinition#managing_tenant_id}.'''
        result = self._values.get("managing_tenant_id")
        assert result is not None, "Required property 'managing_tenant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#name LighthouseDefinition#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#scope LighthouseDefinition#scope}.'''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#description LighthouseDefinition#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#id LighthouseDefinition#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lighthouse_definition_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#lighthouse_definition_id LighthouseDefinition#lighthouse_definition_id}.'''
        result = self._values.get("lighthouse_definition_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plan(self) -> typing.Optional["LighthouseDefinitionPlan"]:
        '''plan block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#plan LighthouseDefinition#plan}
        '''
        result = self._values.get("plan")
        return typing.cast(typing.Optional["LighthouseDefinitionPlan"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LighthouseDefinitionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#timeouts LighthouseDefinition#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LighthouseDefinitionTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LighthouseDefinitionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.lighthouseDefinition.LighthouseDefinitionPlan",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "product": "product",
        "publisher": "publisher",
        "version": "version",
    },
)
class LighthouseDefinitionPlan:
    def __init__(
        self,
        *,
        name: builtins.str,
        product: builtins.str,
        publisher: builtins.str,
        version: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#name LighthouseDefinition#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#product LighthouseDefinition#product}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#publisher LighthouseDefinition#publisher}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#version LighthouseDefinition#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LighthouseDefinitionPlan.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
            check_type(argname="argument publisher", value=publisher, expected_type=type_hints["publisher"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "product": product,
            "publisher": publisher,
            "version": version,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#name LighthouseDefinition#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#product LighthouseDefinition#product}.'''
        result = self._values.get("product")
        assert result is not None, "Required property 'product' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#publisher LighthouseDefinition#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#version LighthouseDefinition#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LighthouseDefinitionPlan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LighthouseDefinitionPlanOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.lighthouseDefinition.LighthouseDefinitionPlanOutputReference",
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
            type_hints = typing.get_type_hints(LighthouseDefinitionPlanOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="productInput")
    def product_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "productInput"))

    @builtins.property
    @jsii.member(jsii_name="publisherInput")
    def publisher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionPlanOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="product")
    def product(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "product"))

    @product.setter
    def product(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionPlanOutputReference, "product").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "product", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionPlanOutputReference, "publisher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionPlanOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LighthouseDefinitionPlan]:
        return typing.cast(typing.Optional[LighthouseDefinitionPlan], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LighthouseDefinitionPlan]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionPlanOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.lighthouseDefinition.LighthouseDefinitionTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class LighthouseDefinitionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#create LighthouseDefinition#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#delete LighthouseDefinition#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#read LighthouseDefinition#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#update LighthouseDefinition#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LighthouseDefinitionTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#create LighthouseDefinition#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#delete LighthouseDefinition#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#read LighthouseDefinition#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/lighthouse_definition#update LighthouseDefinition#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LighthouseDefinitionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LighthouseDefinitionTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.lighthouseDefinition.LighthouseDefinitionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(LighthouseDefinitionTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LighthouseDefinitionTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LighthouseDefinitionTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LighthouseDefinitionTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LighthouseDefinitionTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LighthouseDefinition",
    "LighthouseDefinitionAuthorization",
    "LighthouseDefinitionAuthorizationList",
    "LighthouseDefinitionAuthorizationOutputReference",
    "LighthouseDefinitionConfig",
    "LighthouseDefinitionPlan",
    "LighthouseDefinitionPlanOutputReference",
    "LighthouseDefinitionTimeouts",
    "LighthouseDefinitionTimeoutsOutputReference",
]

publication.publish()
