'''
# `google_iam_deny_policy`

Refer to the Terraform Registory for docs: [`google_iam_deny_policy`](https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy).
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


class GoogleIamDenyPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleIamDenyPolicy.GoogleIamDenyPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy google_iam_deny_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        parent: builtins.str,
        rules: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleIamDenyPolicyRules", typing.Dict[str, typing.Any]]]],
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleIamDenyPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy google_iam_deny_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#name GoogleIamDenyPolicy#name}
        :param parent: The attachment point is identified by its URL-encoded full resource name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#parent GoogleIamDenyPolicy#parent}
        :param rules: rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#rules GoogleIamDenyPolicy#rules}
        :param display_name: The display name of the rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#display_name GoogleIamDenyPolicy#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#id GoogleIamDenyPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#timeouts GoogleIamDenyPolicy#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIamDenyPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleIamDenyPolicyConfig(
            name=name,
            parent=parent,
            rules=rules,
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

    @jsii.member(jsii_name="putRules")
    def put_rules(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleIamDenyPolicyRules", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIamDenyPolicy.put_rules)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRules", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#create GoogleIamDenyPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#delete GoogleIamDenyPolicy#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#update GoogleIamDenyPolicy#update}.
        '''
        value = GoogleIamDenyPolicyTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

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
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> "GoogleIamDenyPolicyRulesList":
        return typing.cast("GoogleIamDenyPolicyRulesList", jsii.get(self, "rules"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleIamDenyPolicyTimeoutsOutputReference":
        return typing.cast("GoogleIamDenyPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parentInput")
    def parent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentInput"))

    @builtins.property
    @jsii.member(jsii_name="rulesInput")
    def rules_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleIamDenyPolicyRules"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleIamDenyPolicyRules"]]], jsii.get(self, "rulesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleIamDenyPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleIamDenyPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicy, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicy, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parent"))

    @parent.setter
    def parent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicy, "parent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parent", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleIamDenyPolicy.GoogleIamDenyPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "parent": "parent",
        "rules": "rules",
        "display_name": "displayName",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class GoogleIamDenyPolicyConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        parent: builtins.str,
        rules: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleIamDenyPolicyRules", typing.Dict[str, typing.Any]]]],
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleIamDenyPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#name GoogleIamDenyPolicy#name}
        :param parent: The attachment point is identified by its URL-encoded full resource name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#parent GoogleIamDenyPolicy#parent}
        :param rules: rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#rules GoogleIamDenyPolicy#rules}
        :param display_name: The display name of the rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#display_name GoogleIamDenyPolicy#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#id GoogleIamDenyPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#timeouts GoogleIamDenyPolicy#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleIamDenyPolicyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIamDenyPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "parent": parent,
            "rules": rules,
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
    def name(self) -> builtins.str:
        '''The name of the policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#name GoogleIamDenyPolicy#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parent(self) -> builtins.str:
        '''The attachment point is identified by its URL-encoded full resource name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#parent GoogleIamDenyPolicy#parent}
        '''
        result = self._values.get("parent")
        assert result is not None, "Required property 'parent' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rules(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleIamDenyPolicyRules"]]:
        '''rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#rules GoogleIamDenyPolicy#rules}
        '''
        result = self._values.get("rules")
        assert result is not None, "Required property 'rules' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleIamDenyPolicyRules"]], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#display_name GoogleIamDenyPolicy#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#id GoogleIamDenyPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleIamDenyPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#timeouts GoogleIamDenyPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleIamDenyPolicyTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleIamDenyPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleIamDenyPolicy.GoogleIamDenyPolicyRules",
    jsii_struct_bases=[],
    name_mapping={"deny_rule": "denyRule", "description": "description"},
)
class GoogleIamDenyPolicyRules:
    def __init__(
        self,
        *,
        deny_rule: typing.Optional[typing.Union["GoogleIamDenyPolicyRulesDenyRule", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param deny_rule: deny_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#deny_rule GoogleIamDenyPolicy#deny_rule}
        :param description: The description of the rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#description GoogleIamDenyPolicy#description}
        '''
        if isinstance(deny_rule, dict):
            deny_rule = GoogleIamDenyPolicyRulesDenyRule(**deny_rule)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIamDenyPolicyRules.__init__)
            check_type(argname="argument deny_rule", value=deny_rule, expected_type=type_hints["deny_rule"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[str, typing.Any] = {}
        if deny_rule is not None:
            self._values["deny_rule"] = deny_rule
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def deny_rule(self) -> typing.Optional["GoogleIamDenyPolicyRulesDenyRule"]:
        '''deny_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#deny_rule GoogleIamDenyPolicy#deny_rule}
        '''
        result = self._values.get("deny_rule")
        return typing.cast(typing.Optional["GoogleIamDenyPolicyRulesDenyRule"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#description GoogleIamDenyPolicy#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleIamDenyPolicyRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleIamDenyPolicy.GoogleIamDenyPolicyRulesDenyRule",
    jsii_struct_bases=[],
    name_mapping={
        "denial_condition": "denialCondition",
        "denied_permissions": "deniedPermissions",
        "denied_principals": "deniedPrincipals",
        "exception_permissions": "exceptionPermissions",
        "exception_principals": "exceptionPrincipals",
    },
)
class GoogleIamDenyPolicyRulesDenyRule:
    def __init__(
        self,
        *,
        denial_condition: typing.Optional[typing.Union["GoogleIamDenyPolicyRulesDenyRuleDenialCondition", typing.Dict[str, typing.Any]]] = None,
        denied_permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        denied_principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        exception_permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        exception_principals: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param denial_condition: denial_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#denial_condition GoogleIamDenyPolicy#denial_condition}
        :param denied_permissions: The permissions that are explicitly denied by this rule. Each permission uses the format '{service-fqdn}/{resource}.{verb}', where '{service-fqdn}' is the fully qualified domain name for the service. For example, 'iam.googleapis.com/roles.list'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#denied_permissions GoogleIamDenyPolicy#denied_permissions}
        :param denied_principals: The identities that are prevented from using one or more permissions on Google Cloud resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#denied_principals GoogleIamDenyPolicy#denied_principals}
        :param exception_permissions: Specifies the permissions that this rule excludes from the set of denied permissions given by deniedPermissions. If a permission appears in deniedPermissions and in exceptionPermissions then it will not be denied. The excluded permissions can be specified using the same syntax as deniedPermissions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#exception_permissions GoogleIamDenyPolicy#exception_permissions}
        :param exception_principals: The identities that are excluded from the deny rule, even if they are listed in the deniedPrincipals. For example, you could add a Google group to the deniedPrincipals, then exclude specific users who belong to that group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#exception_principals GoogleIamDenyPolicy#exception_principals}
        '''
        if isinstance(denial_condition, dict):
            denial_condition = GoogleIamDenyPolicyRulesDenyRuleDenialCondition(**denial_condition)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIamDenyPolicyRulesDenyRule.__init__)
            check_type(argname="argument denial_condition", value=denial_condition, expected_type=type_hints["denial_condition"])
            check_type(argname="argument denied_permissions", value=denied_permissions, expected_type=type_hints["denied_permissions"])
            check_type(argname="argument denied_principals", value=denied_principals, expected_type=type_hints["denied_principals"])
            check_type(argname="argument exception_permissions", value=exception_permissions, expected_type=type_hints["exception_permissions"])
            check_type(argname="argument exception_principals", value=exception_principals, expected_type=type_hints["exception_principals"])
        self._values: typing.Dict[str, typing.Any] = {}
        if denial_condition is not None:
            self._values["denial_condition"] = denial_condition
        if denied_permissions is not None:
            self._values["denied_permissions"] = denied_permissions
        if denied_principals is not None:
            self._values["denied_principals"] = denied_principals
        if exception_permissions is not None:
            self._values["exception_permissions"] = exception_permissions
        if exception_principals is not None:
            self._values["exception_principals"] = exception_principals

    @builtins.property
    def denial_condition(
        self,
    ) -> typing.Optional["GoogleIamDenyPolicyRulesDenyRuleDenialCondition"]:
        '''denial_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#denial_condition GoogleIamDenyPolicy#denial_condition}
        '''
        result = self._values.get("denial_condition")
        return typing.cast(typing.Optional["GoogleIamDenyPolicyRulesDenyRuleDenialCondition"], result)

    @builtins.property
    def denied_permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The permissions that are explicitly denied by this rule.

        Each permission uses the format '{service-fqdn}/{resource}.{verb}',
        where '{service-fqdn}' is the fully qualified domain name for the service. For example, 'iam.googleapis.com/roles.list'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#denied_permissions GoogleIamDenyPolicy#denied_permissions}
        '''
        result = self._values.get("denied_permissions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def denied_principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The identities that are prevented from using one or more permissions on Google Cloud resources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#denied_principals GoogleIamDenyPolicy#denied_principals}
        '''
        result = self._values.get("denied_principals")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def exception_permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the permissions that this rule excludes from the set of denied permissions given by deniedPermissions.

        If a permission appears in deniedPermissions and in exceptionPermissions then it will not be denied.
        The excluded permissions can be specified using the same syntax as deniedPermissions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#exception_permissions GoogleIamDenyPolicy#exception_permissions}
        '''
        result = self._values.get("exception_permissions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def exception_principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The identities that are excluded from the deny rule, even if they are listed in the deniedPrincipals.

        For example, you could add a Google group to the deniedPrincipals, then exclude specific users who belong to that group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#exception_principals GoogleIamDenyPolicy#exception_principals}
        '''
        result = self._values.get("exception_principals")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleIamDenyPolicyRulesDenyRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleIamDenyPolicy.GoogleIamDenyPolicyRulesDenyRuleDenialCondition",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "description": "description",
        "location": "location",
        "title": "title",
    },
)
class GoogleIamDenyPolicyRulesDenyRuleDenialCondition:
    def __init__(
        self,
        *,
        expression: builtins.str,
        description: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Textual representation of an expression in Common Expression Language syntax. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#expression GoogleIamDenyPolicy#expression}
        :param description: Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#description GoogleIamDenyPolicy#description}
        :param location: String indicating the location of the expression for error reporting, e.g. a file name and a position in the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#location GoogleIamDenyPolicy#location}
        :param title: Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#title GoogleIamDenyPolicy#title}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIamDenyPolicyRulesDenyRuleDenialCondition.__init__)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[str, typing.Any] = {
            "expression": expression,
        }
        if description is not None:
            self._values["description"] = description
        if location is not None:
            self._values["location"] = location
        if title is not None:
            self._values["title"] = title

    @builtins.property
    def expression(self) -> builtins.str:
        '''Textual representation of an expression in Common Expression Language syntax.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#expression GoogleIamDenyPolicy#expression}
        '''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the expression.

        This is a longer text which describes the expression,
        e.g. when hovered over it in a UI.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#description GoogleIamDenyPolicy#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#location GoogleIamDenyPolicy#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#title GoogleIamDenyPolicy#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleIamDenyPolicyRulesDenyRuleDenialCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleIamDenyPolicyRulesDenyRuleDenialConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleIamDenyPolicy.GoogleIamDenyPolicyRulesDenyRuleDenialConditionOutputReference",
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
            type_hints = typing.get_type_hints(GoogleIamDenyPolicyRulesDenyRuleDenialConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyRulesDenyRuleDenialConditionOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyRulesDenyRuleDenialConditionOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyRulesDenyRuleDenialConditionOutputReference, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyRulesDenyRuleDenialConditionOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleIamDenyPolicyRulesDenyRuleDenialCondition]:
        return typing.cast(typing.Optional[GoogleIamDenyPolicyRulesDenyRuleDenialCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleIamDenyPolicyRulesDenyRuleDenialCondition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyRulesDenyRuleDenialConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleIamDenyPolicyRulesDenyRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleIamDenyPolicy.GoogleIamDenyPolicyRulesDenyRuleOutputReference",
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
            type_hints = typing.get_type_hints(GoogleIamDenyPolicyRulesDenyRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDenialCondition")
    def put_denial_condition(
        self,
        *,
        expression: builtins.str,
        description: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Textual representation of an expression in Common Expression Language syntax. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#expression GoogleIamDenyPolicy#expression}
        :param description: Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#description GoogleIamDenyPolicy#description}
        :param location: String indicating the location of the expression for error reporting, e.g. a file name and a position in the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#location GoogleIamDenyPolicy#location}
        :param title: Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#title GoogleIamDenyPolicy#title}
        '''
        value = GoogleIamDenyPolicyRulesDenyRuleDenialCondition(
            expression=expression,
            description=description,
            location=location,
            title=title,
        )

        return typing.cast(None, jsii.invoke(self, "putDenialCondition", [value]))

    @jsii.member(jsii_name="resetDenialCondition")
    def reset_denial_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDenialCondition", []))

    @jsii.member(jsii_name="resetDeniedPermissions")
    def reset_denied_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeniedPermissions", []))

    @jsii.member(jsii_name="resetDeniedPrincipals")
    def reset_denied_principals(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeniedPrincipals", []))

    @jsii.member(jsii_name="resetExceptionPermissions")
    def reset_exception_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExceptionPermissions", []))

    @jsii.member(jsii_name="resetExceptionPrincipals")
    def reset_exception_principals(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExceptionPrincipals", []))

    @builtins.property
    @jsii.member(jsii_name="denialCondition")
    def denial_condition(
        self,
    ) -> GoogleIamDenyPolicyRulesDenyRuleDenialConditionOutputReference:
        return typing.cast(GoogleIamDenyPolicyRulesDenyRuleDenialConditionOutputReference, jsii.get(self, "denialCondition"))

    @builtins.property
    @jsii.member(jsii_name="denialConditionInput")
    def denial_condition_input(
        self,
    ) -> typing.Optional[GoogleIamDenyPolicyRulesDenyRuleDenialCondition]:
        return typing.cast(typing.Optional[GoogleIamDenyPolicyRulesDenyRuleDenialCondition], jsii.get(self, "denialConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="deniedPermissionsInput")
    def denied_permissions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "deniedPermissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="deniedPrincipalsInput")
    def denied_principals_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "deniedPrincipalsInput"))

    @builtins.property
    @jsii.member(jsii_name="exceptionPermissionsInput")
    def exception_permissions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exceptionPermissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="exceptionPrincipalsInput")
    def exception_principals_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exceptionPrincipalsInput"))

    @builtins.property
    @jsii.member(jsii_name="deniedPermissions")
    def denied_permissions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "deniedPermissions"))

    @denied_permissions.setter
    def denied_permissions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyRulesDenyRuleOutputReference, "denied_permissions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deniedPermissions", value)

    @builtins.property
    @jsii.member(jsii_name="deniedPrincipals")
    def denied_principals(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "deniedPrincipals"))

    @denied_principals.setter
    def denied_principals(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyRulesDenyRuleOutputReference, "denied_principals").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deniedPrincipals", value)

    @builtins.property
    @jsii.member(jsii_name="exceptionPermissions")
    def exception_permissions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exceptionPermissions"))

    @exception_permissions.setter
    def exception_permissions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyRulesDenyRuleOutputReference, "exception_permissions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exceptionPermissions", value)

    @builtins.property
    @jsii.member(jsii_name="exceptionPrincipals")
    def exception_principals(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exceptionPrincipals"))

    @exception_principals.setter
    def exception_principals(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyRulesDenyRuleOutputReference, "exception_principals").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exceptionPrincipals", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleIamDenyPolicyRulesDenyRule]:
        return typing.cast(typing.Optional[GoogleIamDenyPolicyRulesDenyRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleIamDenyPolicyRulesDenyRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyRulesDenyRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleIamDenyPolicyRulesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleIamDenyPolicy.GoogleIamDenyPolicyRulesList",
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
            type_hints = typing.get_type_hints(GoogleIamDenyPolicyRulesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GoogleIamDenyPolicyRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIamDenyPolicyRulesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleIamDenyPolicyRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyRulesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyRulesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyRulesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleIamDenyPolicyRules]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleIamDenyPolicyRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleIamDenyPolicyRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyRulesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleIamDenyPolicyRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleIamDenyPolicy.GoogleIamDenyPolicyRulesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleIamDenyPolicyRulesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDenyRule")
    def put_deny_rule(
        self,
        *,
        denial_condition: typing.Optional[typing.Union[GoogleIamDenyPolicyRulesDenyRuleDenialCondition, typing.Dict[str, typing.Any]]] = None,
        denied_permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        denied_principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        exception_permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        exception_principals: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param denial_condition: denial_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#denial_condition GoogleIamDenyPolicy#denial_condition}
        :param denied_permissions: The permissions that are explicitly denied by this rule. Each permission uses the format '{service-fqdn}/{resource}.{verb}', where '{service-fqdn}' is the fully qualified domain name for the service. For example, 'iam.googleapis.com/roles.list'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#denied_permissions GoogleIamDenyPolicy#denied_permissions}
        :param denied_principals: The identities that are prevented from using one or more permissions on Google Cloud resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#denied_principals GoogleIamDenyPolicy#denied_principals}
        :param exception_permissions: Specifies the permissions that this rule excludes from the set of denied permissions given by deniedPermissions. If a permission appears in deniedPermissions and in exceptionPermissions then it will not be denied. The excluded permissions can be specified using the same syntax as deniedPermissions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#exception_permissions GoogleIamDenyPolicy#exception_permissions}
        :param exception_principals: The identities that are excluded from the deny rule, even if they are listed in the deniedPrincipals. For example, you could add a Google group to the deniedPrincipals, then exclude specific users who belong to that group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#exception_principals GoogleIamDenyPolicy#exception_principals}
        '''
        value = GoogleIamDenyPolicyRulesDenyRule(
            denial_condition=denial_condition,
            denied_permissions=denied_permissions,
            denied_principals=denied_principals,
            exception_permissions=exception_permissions,
            exception_principals=exception_principals,
        )

        return typing.cast(None, jsii.invoke(self, "putDenyRule", [value]))

    @jsii.member(jsii_name="resetDenyRule")
    def reset_deny_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDenyRule", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @builtins.property
    @jsii.member(jsii_name="denyRule")
    def deny_rule(self) -> GoogleIamDenyPolicyRulesDenyRuleOutputReference:
        return typing.cast(GoogleIamDenyPolicyRulesDenyRuleOutputReference, jsii.get(self, "denyRule"))

    @builtins.property
    @jsii.member(jsii_name="denyRuleInput")
    def deny_rule_input(self) -> typing.Optional[GoogleIamDenyPolicyRulesDenyRule]:
        return typing.cast(typing.Optional[GoogleIamDenyPolicyRulesDenyRule], jsii.get(self, "denyRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyRulesOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleIamDenyPolicyRules, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleIamDenyPolicyRules, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleIamDenyPolicyRules, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyRulesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleIamDenyPolicy.GoogleIamDenyPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleIamDenyPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#create GoogleIamDenyPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#delete GoogleIamDenyPolicy#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#update GoogleIamDenyPolicy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleIamDenyPolicyTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#create GoogleIamDenyPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#delete GoogleIamDenyPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_iam_deny_policy#update GoogleIamDenyPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleIamDenyPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleIamDenyPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleIamDenyPolicy.GoogleIamDenyPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleIamDenyPolicyTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleIamDenyPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleIamDenyPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleIamDenyPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleIamDenyPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleIamDenyPolicy",
    "GoogleIamDenyPolicyConfig",
    "GoogleIamDenyPolicyRules",
    "GoogleIamDenyPolicyRulesDenyRule",
    "GoogleIamDenyPolicyRulesDenyRuleDenialCondition",
    "GoogleIamDenyPolicyRulesDenyRuleDenialConditionOutputReference",
    "GoogleIamDenyPolicyRulesDenyRuleOutputReference",
    "GoogleIamDenyPolicyRulesList",
    "GoogleIamDenyPolicyRulesOutputReference",
    "GoogleIamDenyPolicyTimeouts",
    "GoogleIamDenyPolicyTimeoutsOutputReference",
]

publication.publish()
