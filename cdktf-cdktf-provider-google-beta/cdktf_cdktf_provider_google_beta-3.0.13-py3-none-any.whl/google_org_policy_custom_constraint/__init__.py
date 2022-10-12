'''
# `google_org_policy_custom_constraint`

Refer to the Terraform Registory for docs: [`google_org_policy_custom_constraint`](https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint).
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


class GoogleOrgPolicyCustomConstraint(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOrgPolicyCustomConstraint.GoogleOrgPolicyCustomConstraint",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint google_org_policy_custom_constraint}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        action_type: builtins.str,
        condition: builtins.str,
        method_types: typing.Sequence[builtins.str],
        name: builtins.str,
        parent: builtins.str,
        resource_types: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleOrgPolicyCustomConstraintTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint google_org_policy_custom_constraint} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param action_type: The action to take if the condition is met. Possible values: ["ALLOW", "DENY"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#action_type GoogleOrgPolicyCustomConstraint#action_type}
        :param condition: A CEL condition that refers to a supported service resource, for example 'resource.management.autoUpgrade == false'. For details about CEL usage, see `Common Expression Language <https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#condition GoogleOrgPolicyCustomConstraint#condition}
        :param method_types: A list of RESTful methods for which to enforce the constraint. Can be 'CREATE', 'UPDATE', or both. Not all Google Cloud services support both methods. To see supported methods for each service, find the service in `Supported services <https://cloud.google.com/resource-manager/docs/organization-policy/custom-constraint-supported-services>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#method_types GoogleOrgPolicyCustomConstraint#method_types}
        :param name: Immutable. The name of the custom constraint. This is unique within the organization. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#name GoogleOrgPolicyCustomConstraint#name}
        :param parent: The parent of the resource, an organization. Format should be 'organizations/{organization_id}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#parent GoogleOrgPolicyCustomConstraint#parent}
        :param resource_types: Immutable. The fully qualified name of the Google Cloud REST resource containing the object and field you want to restrict. For example, 'container.googleapis.com/NodePool'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#resource_types GoogleOrgPolicyCustomConstraint#resource_types}
        :param description: A human-friendly description of the constraint to display as an error message when the policy is violated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#description GoogleOrgPolicyCustomConstraint#description}
        :param display_name: A human-friendly name for the constraint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#display_name GoogleOrgPolicyCustomConstraint#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#id GoogleOrgPolicyCustomConstraint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#timeouts GoogleOrgPolicyCustomConstraint#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOrgPolicyCustomConstraint.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleOrgPolicyCustomConstraintConfig(
            action_type=action_type,
            condition=condition,
            method_types=method_types,
            name=name,
            parent=parent,
            resource_types=resource_types,
            description=description,
            display_name=display_name,
            id=id,
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

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#create GoogleOrgPolicyCustomConstraint#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#delete GoogleOrgPolicyCustomConstraint#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#update GoogleOrgPolicyCustomConstraint#update}.
        '''
        value = GoogleOrgPolicyCustomConstraintTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleOrgPolicyCustomConstraintTimeoutsOutputReference":
        return typing.cast("GoogleOrgPolicyCustomConstraintTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="actionTypeInput")
    def action_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="methodTypesInput")
    def method_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "methodTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parentInput")
    def parent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceTypesInput")
    def resource_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleOrgPolicyCustomConstraintTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleOrgPolicyCustomConstraintTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="actionType")
    def action_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionType"))

    @action_type.setter
    def action_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOrgPolicyCustomConstraint, "action_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionType", value)

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "condition"))

    @condition.setter
    def condition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOrgPolicyCustomConstraint, "condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "condition", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOrgPolicyCustomConstraint, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOrgPolicyCustomConstraint, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOrgPolicyCustomConstraint, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="methodTypes")
    def method_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "methodTypes"))

    @method_types.setter
    def method_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOrgPolicyCustomConstraint, "method_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "methodTypes", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOrgPolicyCustomConstraint, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parent"))

    @parent.setter
    def parent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOrgPolicyCustomConstraint, "parent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parent", value)

    @builtins.property
    @jsii.member(jsii_name="resourceTypes")
    def resource_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceTypes"))

    @resource_types.setter
    def resource_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOrgPolicyCustomConstraint, "resource_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTypes", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOrgPolicyCustomConstraint.GoogleOrgPolicyCustomConstraintConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "action_type": "actionType",
        "condition": "condition",
        "method_types": "methodTypes",
        "name": "name",
        "parent": "parent",
        "resource_types": "resourceTypes",
        "description": "description",
        "display_name": "displayName",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class GoogleOrgPolicyCustomConstraintConfig(cdktf.TerraformMetaArguments):
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
        action_type: builtins.str,
        condition: builtins.str,
        method_types: typing.Sequence[builtins.str],
        name: builtins.str,
        parent: builtins.str,
        resource_types: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleOrgPolicyCustomConstraintTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param action_type: The action to take if the condition is met. Possible values: ["ALLOW", "DENY"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#action_type GoogleOrgPolicyCustomConstraint#action_type}
        :param condition: A CEL condition that refers to a supported service resource, for example 'resource.management.autoUpgrade == false'. For details about CEL usage, see `Common Expression Language <https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#condition GoogleOrgPolicyCustomConstraint#condition}
        :param method_types: A list of RESTful methods for which to enforce the constraint. Can be 'CREATE', 'UPDATE', or both. Not all Google Cloud services support both methods. To see supported methods for each service, find the service in `Supported services <https://cloud.google.com/resource-manager/docs/organization-policy/custom-constraint-supported-services>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#method_types GoogleOrgPolicyCustomConstraint#method_types}
        :param name: Immutable. The name of the custom constraint. This is unique within the organization. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#name GoogleOrgPolicyCustomConstraint#name}
        :param parent: The parent of the resource, an organization. Format should be 'organizations/{organization_id}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#parent GoogleOrgPolicyCustomConstraint#parent}
        :param resource_types: Immutable. The fully qualified name of the Google Cloud REST resource containing the object and field you want to restrict. For example, 'container.googleapis.com/NodePool'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#resource_types GoogleOrgPolicyCustomConstraint#resource_types}
        :param description: A human-friendly description of the constraint to display as an error message when the policy is violated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#description GoogleOrgPolicyCustomConstraint#description}
        :param display_name: A human-friendly name for the constraint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#display_name GoogleOrgPolicyCustomConstraint#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#id GoogleOrgPolicyCustomConstraint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#timeouts GoogleOrgPolicyCustomConstraint#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleOrgPolicyCustomConstraintTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOrgPolicyCustomConstraintConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument action_type", value=action_type, expected_type=type_hints["action_type"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument method_types", value=method_types, expected_type=type_hints["method_types"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument resource_types", value=resource_types, expected_type=type_hints["resource_types"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "action_type": action_type,
            "condition": condition,
            "method_types": method_types,
            "name": name,
            "parent": parent,
            "resource_types": resource_types,
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
        if display_name is not None:
            self._values["display_name"] = display_name
        if id is not None:
            self._values["id"] = id
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
    def action_type(self) -> builtins.str:
        '''The action to take if the condition is met. Possible values: ["ALLOW", "DENY"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#action_type GoogleOrgPolicyCustomConstraint#action_type}
        '''
        result = self._values.get("action_type")
        assert result is not None, "Required property 'action_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition(self) -> builtins.str:
        '''A CEL condition that refers to a supported service resource, for example 'resource.management.autoUpgrade == false'. For details about CEL usage, see `Common Expression Language <https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#condition GoogleOrgPolicyCustomConstraint#condition}
        '''
        result = self._values.get("condition")
        assert result is not None, "Required property 'condition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def method_types(self) -> typing.List[builtins.str]:
        '''A list of RESTful methods for which to enforce the constraint.

        Can be 'CREATE', 'UPDATE', or both. Not all Google Cloud services support both methods. To see supported methods for each service, find the service in `Supported services <https://cloud.google.com/resource-manager/docs/organization-policy/custom-constraint-supported-services>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#method_types GoogleOrgPolicyCustomConstraint#method_types}
        '''
        result = self._values.get("method_types")
        assert result is not None, "Required property 'method_types' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Immutable. The name of the custom constraint. This is unique within the organization.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#name GoogleOrgPolicyCustomConstraint#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parent(self) -> builtins.str:
        '''The parent of the resource, an organization. Format should be 'organizations/{organization_id}'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#parent GoogleOrgPolicyCustomConstraint#parent}
        '''
        result = self._values.get("parent")
        assert result is not None, "Required property 'parent' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_types(self) -> typing.List[builtins.str]:
        '''Immutable.

        The fully qualified name of the Google Cloud REST resource containing the object and field you want to restrict. For example, 'container.googleapis.com/NodePool'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#resource_types GoogleOrgPolicyCustomConstraint#resource_types}
        '''
        result = self._values.get("resource_types")
        assert result is not None, "Required property 'resource_types' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-friendly description of the constraint to display as an error message when the policy is violated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#description GoogleOrgPolicyCustomConstraint#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''A human-friendly name for the constraint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#display_name GoogleOrgPolicyCustomConstraint#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#id GoogleOrgPolicyCustomConstraint#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleOrgPolicyCustomConstraintTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#timeouts GoogleOrgPolicyCustomConstraint#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleOrgPolicyCustomConstraintTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOrgPolicyCustomConstraintConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOrgPolicyCustomConstraint.GoogleOrgPolicyCustomConstraintTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleOrgPolicyCustomConstraintTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#create GoogleOrgPolicyCustomConstraint#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#delete GoogleOrgPolicyCustomConstraint#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#update GoogleOrgPolicyCustomConstraint#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOrgPolicyCustomConstraintTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#create GoogleOrgPolicyCustomConstraint#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#delete GoogleOrgPolicyCustomConstraint#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_org_policy_custom_constraint#update GoogleOrgPolicyCustomConstraint#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOrgPolicyCustomConstraintTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOrgPolicyCustomConstraintTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOrgPolicyCustomConstraint.GoogleOrgPolicyCustomConstraintTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOrgPolicyCustomConstraintTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

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
            type_hints = typing.get_type_hints(getattr(GoogleOrgPolicyCustomConstraintTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOrgPolicyCustomConstraintTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOrgPolicyCustomConstraintTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleOrgPolicyCustomConstraintTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleOrgPolicyCustomConstraintTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleOrgPolicyCustomConstraintTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOrgPolicyCustomConstraintTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleOrgPolicyCustomConstraint",
    "GoogleOrgPolicyCustomConstraintConfig",
    "GoogleOrgPolicyCustomConstraintTimeouts",
    "GoogleOrgPolicyCustomConstraintTimeoutsOutputReference",
]

publication.publish()
