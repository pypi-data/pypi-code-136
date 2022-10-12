'''
# `cloudflare_access_policy`

Refer to the Terraform Registory for docs: [`cloudflare_access_policy`](https://www.terraform.io/docs/providers/cloudflare/r/access_policy).
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


class AccessPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy cloudflare_access_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        application_id: builtins.str,
        decision: builtins.str,
        include: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyInclude", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        precedence: jsii.Number,
        account_id: typing.Optional[builtins.str] = None,
        approval_group: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyApprovalGroup", typing.Dict[str, typing.Any]]]]] = None,
        approval_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        exclude: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyExclude", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        purpose_justification_prompt: typing.Optional[builtins.str] = None,
        purpose_justification_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        require: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyRequire", typing.Dict[str, typing.Any]]]]] = None,
        zone_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy cloudflare_access_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param application_id: The ID of the application the policy is associated with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#application_id AccessPolicy#application_id}
        :param decision: Defines the action Access will take if the policy matches the user. Available values: ``allow``, ``deny``, ``non_identity``, ``bypass``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#decision AccessPolicy#decision}
        :param include: include block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#include AccessPolicy#include}
        :param name: Friendly name of the Access Policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#name AccessPolicy#name}
        :param precedence: The unique precedence for policies on a single application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#precedence AccessPolicy#precedence}
        :param account_id: The account identifier to target for the resource. Conflicts with ``zone_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#account_id AccessPolicy#account_id}
        :param approval_group: approval_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#approval_group AccessPolicy#approval_group}
        :param approval_required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#approval_required AccessPolicy#approval_required}.
        :param exclude: exclude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#exclude AccessPolicy#exclude}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#id AccessPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param purpose_justification_prompt: The prompt to display to the user for a justification for accessing the resource. Required when using ``purpose_justification_required``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#purpose_justification_prompt AccessPolicy#purpose_justification_prompt}
        :param purpose_justification_required: Whether to prompt the user for a justification for accessing the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#purpose_justification_required AccessPolicy#purpose_justification_required}
        :param require: require block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#require AccessPolicy#require}
        :param zone_id: The zone identifier to target for the resource. Conflicts with ``account_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#zone_id AccessPolicy#zone_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AccessPolicyConfig(
            application_id=application_id,
            decision=decision,
            include=include,
            name=name,
            precedence=precedence,
            account_id=account_id,
            approval_group=approval_group,
            approval_required=approval_required,
            exclude=exclude,
            id=id,
            purpose_justification_prompt=purpose_justification_prompt,
            purpose_justification_required=purpose_justification_required,
            require=require,
            zone_id=zone_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putApprovalGroup")
    def put_approval_group(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyApprovalGroup", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicy.put_approval_group)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putApprovalGroup", [value]))

    @jsii.member(jsii_name="putExclude")
    def put_exclude(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyExclude", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicy.put_exclude)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExclude", [value]))

    @jsii.member(jsii_name="putInclude")
    def put_include(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyInclude", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicy.put_include)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInclude", [value]))

    @jsii.member(jsii_name="putRequire")
    def put_require(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyRequire", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicy.put_require)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequire", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetApprovalGroup")
    def reset_approval_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApprovalGroup", []))

    @jsii.member(jsii_name="resetApprovalRequired")
    def reset_approval_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApprovalRequired", []))

    @jsii.member(jsii_name="resetExclude")
    def reset_exclude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclude", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPurposeJustificationPrompt")
    def reset_purpose_justification_prompt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPurposeJustificationPrompt", []))

    @jsii.member(jsii_name="resetPurposeJustificationRequired")
    def reset_purpose_justification_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPurposeJustificationRequired", []))

    @jsii.member(jsii_name="resetRequire")
    def reset_require(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequire", []))

    @jsii.member(jsii_name="resetZoneId")
    def reset_zone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="approvalGroup")
    def approval_group(self) -> "AccessPolicyApprovalGroupList":
        return typing.cast("AccessPolicyApprovalGroupList", jsii.get(self, "approvalGroup"))

    @builtins.property
    @jsii.member(jsii_name="exclude")
    def exclude(self) -> "AccessPolicyExcludeList":
        return typing.cast("AccessPolicyExcludeList", jsii.get(self, "exclude"))

    @builtins.property
    @jsii.member(jsii_name="include")
    def include(self) -> "AccessPolicyIncludeList":
        return typing.cast("AccessPolicyIncludeList", jsii.get(self, "include"))

    @builtins.property
    @jsii.member(jsii_name="require")
    def require(self) -> "AccessPolicyRequireList":
        return typing.cast("AccessPolicyRequireList", jsii.get(self, "require"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationIdInput")
    def application_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="approvalGroupInput")
    def approval_group_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyApprovalGroup"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyApprovalGroup"]]], jsii.get(self, "approvalGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="approvalRequiredInput")
    def approval_required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "approvalRequiredInput"))

    @builtins.property
    @jsii.member(jsii_name="decisionInput")
    def decision_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "decisionInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeInput")
    def exclude_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyExclude"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyExclude"]]], jsii.get(self, "excludeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="includeInput")
    def include_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyInclude"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyInclude"]]], jsii.get(self, "includeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="precedenceInput")
    def precedence_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "precedenceInput"))

    @builtins.property
    @jsii.member(jsii_name="purposeJustificationPromptInput")
    def purpose_justification_prompt_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "purposeJustificationPromptInput"))

    @builtins.property
    @jsii.member(jsii_name="purposeJustificationRequiredInput")
    def purpose_justification_required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "purposeJustificationRequiredInput"))

    @builtins.property
    @jsii.member(jsii_name="requireInput")
    def require_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyRequire"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyRequire"]]], jsii.get(self, "requireInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicy, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicy, "application_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="approvalRequired")
    def approval_required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "approvalRequired"))

    @approval_required.setter
    def approval_required(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicy, "approval_required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvalRequired", value)

    @builtins.property
    @jsii.member(jsii_name="decision")
    def decision(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "decision"))

    @decision.setter
    def decision(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicy, "decision").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "decision", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicy, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="precedence")
    def precedence(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "precedence"))

    @precedence.setter
    def precedence(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicy, "precedence").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "precedence", value)

    @builtins.property
    @jsii.member(jsii_name="purposeJustificationPrompt")
    def purpose_justification_prompt(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "purposeJustificationPrompt"))

    @purpose_justification_prompt.setter
    def purpose_justification_prompt(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicy, "purpose_justification_prompt").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "purposeJustificationPrompt", value)

    @builtins.property
    @jsii.member(jsii_name="purposeJustificationRequired")
    def purpose_justification_required(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "purposeJustificationRequired"))

    @purpose_justification_required.setter
    def purpose_justification_required(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicy, "purpose_justification_required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "purposeJustificationRequired", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicy, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyApprovalGroup",
    jsii_struct_bases=[],
    name_mapping={
        "approvals_needed": "approvalsNeeded",
        "email_addresses": "emailAddresses",
        "email_list_uuid": "emailListUuid",
    },
)
class AccessPolicyApprovalGroup:
    def __init__(
        self,
        *,
        approvals_needed: jsii.Number,
        email_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        email_list_uuid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param approvals_needed: Number of approvals needed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#approvals_needed AccessPolicy#approvals_needed}
        :param email_addresses: List of emails to request approval from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email_addresses AccessPolicy#email_addresses}
        :param email_list_uuid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email_list_uuid AccessPolicy#email_list_uuid}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyApprovalGroup.__init__)
            check_type(argname="argument approvals_needed", value=approvals_needed, expected_type=type_hints["approvals_needed"])
            check_type(argname="argument email_addresses", value=email_addresses, expected_type=type_hints["email_addresses"])
            check_type(argname="argument email_list_uuid", value=email_list_uuid, expected_type=type_hints["email_list_uuid"])
        self._values: typing.Dict[str, typing.Any] = {
            "approvals_needed": approvals_needed,
        }
        if email_addresses is not None:
            self._values["email_addresses"] = email_addresses
        if email_list_uuid is not None:
            self._values["email_list_uuid"] = email_list_uuid

    @builtins.property
    def approvals_needed(self) -> jsii.Number:
        '''Number of approvals needed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#approvals_needed AccessPolicy#approvals_needed}
        '''
        result = self._values.get("approvals_needed")
        assert result is not None, "Required property 'approvals_needed' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def email_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of emails to request approval from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email_addresses AccessPolicy#email_addresses}
        '''
        result = self._values.get("email_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email_list_uuid(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email_list_uuid AccessPolicy#email_list_uuid}.'''
        result = self._values.get("email_list_uuid")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyApprovalGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyApprovalGroupList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyApprovalGroupList",
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
            type_hints = typing.get_type_hints(AccessPolicyApprovalGroupList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyApprovalGroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyApprovalGroupList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyApprovalGroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyApprovalGroupList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyApprovalGroupList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyApprovalGroupList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyApprovalGroup]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyApprovalGroup]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyApprovalGroup]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyApprovalGroupList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyApprovalGroupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyApprovalGroupOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyApprovalGroupOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEmailAddresses")
    def reset_email_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailAddresses", []))

    @jsii.member(jsii_name="resetEmailListUuid")
    def reset_email_list_uuid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailListUuid", []))

    @builtins.property
    @jsii.member(jsii_name="approvalsNeededInput")
    def approvals_needed_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "approvalsNeededInput"))

    @builtins.property
    @jsii.member(jsii_name="emailAddressesInput")
    def email_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="emailListUuidInput")
    def email_list_uuid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailListUuidInput"))

    @builtins.property
    @jsii.member(jsii_name="approvalsNeeded")
    def approvals_needed(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "approvalsNeeded"))

    @approvals_needed.setter
    def approvals_needed(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyApprovalGroupOutputReference, "approvals_needed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvalsNeeded", value)

    @builtins.property
    @jsii.member(jsii_name="emailAddresses")
    def email_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "emailAddresses"))

    @email_addresses.setter
    def email_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyApprovalGroupOutputReference, "email_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="emailListUuid")
    def email_list_uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailListUuid"))

    @email_list_uuid.setter
    def email_list_uuid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyApprovalGroupOutputReference, "email_list_uuid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailListUuid", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyApprovalGroup, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyApprovalGroup, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyApprovalGroup, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyApprovalGroupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "application_id": "applicationId",
        "decision": "decision",
        "include": "include",
        "name": "name",
        "precedence": "precedence",
        "account_id": "accountId",
        "approval_group": "approvalGroup",
        "approval_required": "approvalRequired",
        "exclude": "exclude",
        "id": "id",
        "purpose_justification_prompt": "purposeJustificationPrompt",
        "purpose_justification_required": "purposeJustificationRequired",
        "require": "require",
        "zone_id": "zoneId",
    },
)
class AccessPolicyConfig(cdktf.TerraformMetaArguments):
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
        application_id: builtins.str,
        decision: builtins.str,
        include: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyInclude", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        precedence: jsii.Number,
        account_id: typing.Optional[builtins.str] = None,
        approval_group: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessPolicyApprovalGroup, typing.Dict[str, typing.Any]]]]] = None,
        approval_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        exclude: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyExclude", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        purpose_justification_prompt: typing.Optional[builtins.str] = None,
        purpose_justification_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        require: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyRequire", typing.Dict[str, typing.Any]]]]] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param application_id: The ID of the application the policy is associated with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#application_id AccessPolicy#application_id}
        :param decision: Defines the action Access will take if the policy matches the user. Available values: ``allow``, ``deny``, ``non_identity``, ``bypass``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#decision AccessPolicy#decision}
        :param include: include block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#include AccessPolicy#include}
        :param name: Friendly name of the Access Policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#name AccessPolicy#name}
        :param precedence: The unique precedence for policies on a single application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#precedence AccessPolicy#precedence}
        :param account_id: The account identifier to target for the resource. Conflicts with ``zone_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#account_id AccessPolicy#account_id}
        :param approval_group: approval_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#approval_group AccessPolicy#approval_group}
        :param approval_required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#approval_required AccessPolicy#approval_required}.
        :param exclude: exclude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#exclude AccessPolicy#exclude}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#id AccessPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param purpose_justification_prompt: The prompt to display to the user for a justification for accessing the resource. Required when using ``purpose_justification_required``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#purpose_justification_prompt AccessPolicy#purpose_justification_prompt}
        :param purpose_justification_required: Whether to prompt the user for a justification for accessing the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#purpose_justification_required AccessPolicy#purpose_justification_required}
        :param require: require block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#require AccessPolicy#require}
        :param zone_id: The zone identifier to target for the resource. Conflicts with ``account_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#zone_id AccessPolicy#zone_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument decision", value=decision, expected_type=type_hints["decision"])
            check_type(argname="argument include", value=include, expected_type=type_hints["include"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument precedence", value=precedence, expected_type=type_hints["precedence"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument approval_group", value=approval_group, expected_type=type_hints["approval_group"])
            check_type(argname="argument approval_required", value=approval_required, expected_type=type_hints["approval_required"])
            check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument purpose_justification_prompt", value=purpose_justification_prompt, expected_type=type_hints["purpose_justification_prompt"])
            check_type(argname="argument purpose_justification_required", value=purpose_justification_required, expected_type=type_hints["purpose_justification_required"])
            check_type(argname="argument require", value=require, expected_type=type_hints["require"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
            "decision": decision,
            "include": include,
            "name": name,
            "precedence": precedence,
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
        if account_id is not None:
            self._values["account_id"] = account_id
        if approval_group is not None:
            self._values["approval_group"] = approval_group
        if approval_required is not None:
            self._values["approval_required"] = approval_required
        if exclude is not None:
            self._values["exclude"] = exclude
        if id is not None:
            self._values["id"] = id
        if purpose_justification_prompt is not None:
            self._values["purpose_justification_prompt"] = purpose_justification_prompt
        if purpose_justification_required is not None:
            self._values["purpose_justification_required"] = purpose_justification_required
        if require is not None:
            self._values["require"] = require
        if zone_id is not None:
            self._values["zone_id"] = zone_id

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
    def application_id(self) -> builtins.str:
        '''The ID of the application the policy is associated with.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#application_id AccessPolicy#application_id}
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def decision(self) -> builtins.str:
        '''Defines the action Access will take if the policy matches the user. Available values: ``allow``, ``deny``, ``non_identity``, ``bypass``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#decision AccessPolicy#decision}
        '''
        result = self._values.get("decision")
        assert result is not None, "Required property 'decision' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def include(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["AccessPolicyInclude"]]:
        '''include block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#include AccessPolicy#include}
        '''
        result = self._values.get("include")
        assert result is not None, "Required property 'include' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["AccessPolicyInclude"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Friendly name of the Access Policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#name AccessPolicy#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def precedence(self) -> jsii.Number:
        '''The unique precedence for policies on a single application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#precedence AccessPolicy#precedence}
        '''
        result = self._values.get("precedence")
        assert result is not None, "Required property 'precedence' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''The account identifier to target for the resource. Conflicts with ``zone_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#account_id AccessPolicy#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def approval_group(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyApprovalGroup]]]:
        '''approval_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#approval_group AccessPolicy#approval_group}
        '''
        result = self._values.get("approval_group")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyApprovalGroup]]], result)

    @builtins.property
    def approval_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#approval_required AccessPolicy#approval_required}.'''
        result = self._values.get("approval_required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def exclude(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyExclude"]]]:
        '''exclude block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#exclude AccessPolicy#exclude}
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyExclude"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#id AccessPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def purpose_justification_prompt(self) -> typing.Optional[builtins.str]:
        '''The prompt to display to the user for a justification for accessing the resource. Required when using ``purpose_justification_required``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#purpose_justification_prompt AccessPolicy#purpose_justification_prompt}
        '''
        result = self._values.get("purpose_justification_prompt")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def purpose_justification_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to prompt the user for a justification for accessing the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#purpose_justification_required AccessPolicy#purpose_justification_required}
        '''
        result = self._values.get("purpose_justification_required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def require(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyRequire"]]]:
        '''require block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#require AccessPolicy#require}
        '''
        result = self._values.get("require")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyRequire"]]], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''The zone identifier to target for the resource. Conflicts with ``account_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#zone_id AccessPolicy#zone_id}
        '''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExclude",
    jsii_struct_bases=[],
    name_mapping={
        "any_valid_service_token": "anyValidServiceToken",
        "auth_method": "authMethod",
        "azure": "azure",
        "certificate": "certificate",
        "common_name": "commonName",
        "device_posture": "devicePosture",
        "email": "email",
        "email_domain": "emailDomain",
        "everyone": "everyone",
        "external_evaluation": "externalEvaluation",
        "geo": "geo",
        "github": "github",
        "group": "group",
        "gsuite": "gsuite",
        "ip": "ip",
        "login_method": "loginMethod",
        "okta": "okta",
        "saml": "saml",
        "service_token": "serviceToken",
    },
)
class AccessPolicyExclude:
    def __init__(
        self,
        *,
        any_valid_service_token: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auth_method: typing.Optional[builtins.str] = None,
        azure: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyExcludeAzure", typing.Dict[str, typing.Any]]]]] = None,
        certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        common_name: typing.Optional[builtins.str] = None,
        device_posture: typing.Optional[typing.Sequence[builtins.str]] = None,
        email: typing.Optional[typing.Sequence[builtins.str]] = None,
        email_domain: typing.Optional[typing.Sequence[builtins.str]] = None,
        everyone: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        external_evaluation: typing.Optional[typing.Union["AccessPolicyExcludeExternalEvaluation", typing.Dict[str, typing.Any]]] = None,
        geo: typing.Optional[typing.Sequence[builtins.str]] = None,
        github: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyExcludeGithub", typing.Dict[str, typing.Any]]]]] = None,
        group: typing.Optional[typing.Sequence[builtins.str]] = None,
        gsuite: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyExcludeGsuite", typing.Dict[str, typing.Any]]]]] = None,
        ip: typing.Optional[typing.Sequence[builtins.str]] = None,
        login_method: typing.Optional[typing.Sequence[builtins.str]] = None,
        okta: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyExcludeOkta", typing.Dict[str, typing.Any]]]]] = None,
        saml: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyExcludeSaml", typing.Dict[str, typing.Any]]]]] = None,
        service_token: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param any_valid_service_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#any_valid_service_token AccessPolicy#any_valid_service_token}.
        :param auth_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#auth_method AccessPolicy#auth_method}.
        :param azure: azure block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#azure AccessPolicy#azure}
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#certificate AccessPolicy#certificate}.
        :param common_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#common_name AccessPolicy#common_name}.
        :param device_posture: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#device_posture AccessPolicy#device_posture}.
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email AccessPolicy#email}.
        :param email_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email_domain AccessPolicy#email_domain}.
        :param everyone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#everyone AccessPolicy#everyone}.
        :param external_evaluation: external_evaluation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#external_evaluation AccessPolicy#external_evaluation}
        :param geo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#geo AccessPolicy#geo}.
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#github AccessPolicy#github}
        :param group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#group AccessPolicy#group}.
        :param gsuite: gsuite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#gsuite AccessPolicy#gsuite}
        :param ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#ip AccessPolicy#ip}.
        :param login_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#login_method AccessPolicy#login_method}.
        :param okta: okta block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#okta AccessPolicy#okta}
        :param saml: saml block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#saml AccessPolicy#saml}
        :param service_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#service_token AccessPolicy#service_token}.
        '''
        if isinstance(external_evaluation, dict):
            external_evaluation = AccessPolicyExcludeExternalEvaluation(**external_evaluation)
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyExclude.__init__)
            check_type(argname="argument any_valid_service_token", value=any_valid_service_token, expected_type=type_hints["any_valid_service_token"])
            check_type(argname="argument auth_method", value=auth_method, expected_type=type_hints["auth_method"])
            check_type(argname="argument azure", value=azure, expected_type=type_hints["azure"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument common_name", value=common_name, expected_type=type_hints["common_name"])
            check_type(argname="argument device_posture", value=device_posture, expected_type=type_hints["device_posture"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument email_domain", value=email_domain, expected_type=type_hints["email_domain"])
            check_type(argname="argument everyone", value=everyone, expected_type=type_hints["everyone"])
            check_type(argname="argument external_evaluation", value=external_evaluation, expected_type=type_hints["external_evaluation"])
            check_type(argname="argument geo", value=geo, expected_type=type_hints["geo"])
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument gsuite", value=gsuite, expected_type=type_hints["gsuite"])
            check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
            check_type(argname="argument login_method", value=login_method, expected_type=type_hints["login_method"])
            check_type(argname="argument okta", value=okta, expected_type=type_hints["okta"])
            check_type(argname="argument saml", value=saml, expected_type=type_hints["saml"])
            check_type(argname="argument service_token", value=service_token, expected_type=type_hints["service_token"])
        self._values: typing.Dict[str, typing.Any] = {}
        if any_valid_service_token is not None:
            self._values["any_valid_service_token"] = any_valid_service_token
        if auth_method is not None:
            self._values["auth_method"] = auth_method
        if azure is not None:
            self._values["azure"] = azure
        if certificate is not None:
            self._values["certificate"] = certificate
        if common_name is not None:
            self._values["common_name"] = common_name
        if device_posture is not None:
            self._values["device_posture"] = device_posture
        if email is not None:
            self._values["email"] = email
        if email_domain is not None:
            self._values["email_domain"] = email_domain
        if everyone is not None:
            self._values["everyone"] = everyone
        if external_evaluation is not None:
            self._values["external_evaluation"] = external_evaluation
        if geo is not None:
            self._values["geo"] = geo
        if github is not None:
            self._values["github"] = github
        if group is not None:
            self._values["group"] = group
        if gsuite is not None:
            self._values["gsuite"] = gsuite
        if ip is not None:
            self._values["ip"] = ip
        if login_method is not None:
            self._values["login_method"] = login_method
        if okta is not None:
            self._values["okta"] = okta
        if saml is not None:
            self._values["saml"] = saml
        if service_token is not None:
            self._values["service_token"] = service_token

    @builtins.property
    def any_valid_service_token(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#any_valid_service_token AccessPolicy#any_valid_service_token}.'''
        result = self._values.get("any_valid_service_token")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auth_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#auth_method AccessPolicy#auth_method}.'''
        result = self._values.get("auth_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyExcludeAzure"]]]:
        '''azure block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#azure AccessPolicy#azure}
        '''
        result = self._values.get("azure")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyExcludeAzure"]]], result)

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#certificate AccessPolicy#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def common_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#common_name AccessPolicy#common_name}.'''
        result = self._values.get("common_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def device_posture(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#device_posture AccessPolicy#device_posture}.'''
        result = self._values.get("device_posture")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email AccessPolicy#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email_domain(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email_domain AccessPolicy#email_domain}.'''
        result = self._values.get("email_domain")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def everyone(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#everyone AccessPolicy#everyone}.'''
        result = self._values.get("everyone")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def external_evaluation(
        self,
    ) -> typing.Optional["AccessPolicyExcludeExternalEvaluation"]:
        '''external_evaluation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#external_evaluation AccessPolicy#external_evaluation}
        '''
        result = self._values.get("external_evaluation")
        return typing.cast(typing.Optional["AccessPolicyExcludeExternalEvaluation"], result)

    @builtins.property
    def geo(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#geo AccessPolicy#geo}.'''
        result = self._values.get("geo")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def github(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyExcludeGithub"]]]:
        '''github block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#github AccessPolicy#github}
        '''
        result = self._values.get("github")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyExcludeGithub"]]], result)

    @builtins.property
    def group(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#group AccessPolicy#group}.'''
        result = self._values.get("group")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def gsuite(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyExcludeGsuite"]]]:
        '''gsuite block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#gsuite AccessPolicy#gsuite}
        '''
        result = self._values.get("gsuite")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyExcludeGsuite"]]], result)

    @builtins.property
    def ip(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#ip AccessPolicy#ip}.'''
        result = self._values.get("ip")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def login_method(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#login_method AccessPolicy#login_method}.'''
        result = self._values.get("login_method")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def okta(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyExcludeOkta"]]]:
        '''okta block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#okta AccessPolicy#okta}
        '''
        result = self._values.get("okta")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyExcludeOkta"]]], result)

    @builtins.property
    def saml(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyExcludeSaml"]]]:
        '''saml block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#saml AccessPolicy#saml}
        '''
        result = self._values.get("saml")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyExcludeSaml"]]], result)

    @builtins.property
    def service_token(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#service_token AccessPolicy#service_token}.'''
        result = self._values.get("service_token")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyExclude(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeAzure",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "identity_provider_id": "identityProviderId"},
)
class AccessPolicyExcludeAzure:
    def __init__(
        self,
        *,
        id: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_provider_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#id AccessPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyExcludeAzure.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id

    @builtins.property
    def id(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#id AccessPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyExcludeAzure(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyExcludeAzureList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeAzureList",
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
            type_hints = typing.get_type_hints(AccessPolicyExcludeAzureList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyExcludeAzureOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyExcludeAzureList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyExcludeAzureOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeAzureList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeAzureList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeAzureList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeAzure]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeAzure]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeAzure]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeAzureList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyExcludeAzureOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeAzureOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyExcludeAzureOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "id"))

    @id.setter
    def id(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeAzureOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeAzureOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyExcludeAzure, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyExcludeAzure, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyExcludeAzure, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeAzureOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeExternalEvaluation",
    jsii_struct_bases=[],
    name_mapping={"evaluate_url": "evaluateUrl", "keys_url": "keysUrl"},
)
class AccessPolicyExcludeExternalEvaluation:
    def __init__(
        self,
        *,
        evaluate_url: typing.Optional[builtins.str] = None,
        keys_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param evaluate_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#evaluate_url AccessPolicy#evaluate_url}.
        :param keys_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#keys_url AccessPolicy#keys_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyExcludeExternalEvaluation.__init__)
            check_type(argname="argument evaluate_url", value=evaluate_url, expected_type=type_hints["evaluate_url"])
            check_type(argname="argument keys_url", value=keys_url, expected_type=type_hints["keys_url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if evaluate_url is not None:
            self._values["evaluate_url"] = evaluate_url
        if keys_url is not None:
            self._values["keys_url"] = keys_url

    @builtins.property
    def evaluate_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#evaluate_url AccessPolicy#evaluate_url}.'''
        result = self._values.get("evaluate_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keys_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#keys_url AccessPolicy#keys_url}.'''
        result = self._values.get("keys_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyExcludeExternalEvaluation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyExcludeExternalEvaluationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeExternalEvaluationOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyExcludeExternalEvaluationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEvaluateUrl")
    def reset_evaluate_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluateUrl", []))

    @jsii.member(jsii_name="resetKeysUrl")
    def reset_keys_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeysUrl", []))

    @builtins.property
    @jsii.member(jsii_name="evaluateUrlInput")
    def evaluate_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluateUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="keysUrlInput")
    def keys_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keysUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluateUrl")
    def evaluate_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "evaluateUrl"))

    @evaluate_url.setter
    def evaluate_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeExternalEvaluationOutputReference, "evaluate_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluateUrl", value)

    @builtins.property
    @jsii.member(jsii_name="keysUrl")
    def keys_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keysUrl"))

    @keys_url.setter
    def keys_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeExternalEvaluationOutputReference, "keys_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keysUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AccessPolicyExcludeExternalEvaluation]:
        return typing.cast(typing.Optional[AccessPolicyExcludeExternalEvaluation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AccessPolicyExcludeExternalEvaluation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeExternalEvaluationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeGithub",
    jsii_struct_bases=[],
    name_mapping={
        "identity_provider_id": "identityProviderId",
        "name": "name",
        "teams": "teams",
    },
)
class AccessPolicyExcludeGithub:
    def __init__(
        self,
        *,
        identity_provider_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        teams: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#name AccessPolicy#name}.
        :param teams: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#teams AccessPolicy#teams}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyExcludeGithub.__init__)
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument teams", value=teams, expected_type=type_hints["teams"])
        self._values: typing.Dict[str, typing.Any] = {}
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id
        if name is not None:
            self._values["name"] = name
        if teams is not None:
            self._values["teams"] = teams

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#name AccessPolicy#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def teams(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#teams AccessPolicy#teams}.'''
        result = self._values.get("teams")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyExcludeGithub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyExcludeGithubList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeGithubList",
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
            type_hints = typing.get_type_hints(AccessPolicyExcludeGithubList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyExcludeGithubOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyExcludeGithubList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyExcludeGithubOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeGithubList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeGithubList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeGithubList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeGithub]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeGithub]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeGithub]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeGithubList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyExcludeGithubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeGithubOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyExcludeGithubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetTeams")
    def reset_teams(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeams", []))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="teamsInput")
    def teams_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "teamsInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeGithubOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeGithubOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="teams")
    def teams(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "teams"))

    @teams.setter
    def teams(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeGithubOutputReference, "teams").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teams", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyExcludeGithub, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyExcludeGithub, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyExcludeGithub, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeGithubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeGsuite",
    jsii_struct_bases=[],
    name_mapping={"email": "email", "identity_provider_id": "identityProviderId"},
)
class AccessPolicyExcludeGsuite:
    def __init__(
        self,
        *,
        email: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_provider_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email AccessPolicy#email}.
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyExcludeGsuite.__init__)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if email is not None:
            self._values["email"] = email
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id

    @builtins.property
    def email(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email AccessPolicy#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyExcludeGsuite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyExcludeGsuiteList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeGsuiteList",
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
            type_hints = typing.get_type_hints(AccessPolicyExcludeGsuiteList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyExcludeGsuiteOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyExcludeGsuiteList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyExcludeGsuiteOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeGsuiteList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeGsuiteList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeGsuiteList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeGsuite]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeGsuite]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeGsuite]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeGsuiteList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyExcludeGsuiteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeGsuiteOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyExcludeGsuiteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeGsuiteOutputReference, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeGsuiteOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyExcludeGsuite, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyExcludeGsuite, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyExcludeGsuite, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeGsuiteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyExcludeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeList",
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
            type_hints = typing.get_type_hints(AccessPolicyExcludeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyExcludeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyExcludeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyExcludeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExclude]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExclude]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExclude]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeOkta",
    jsii_struct_bases=[],
    name_mapping={"identity_provider_id": "identityProviderId", "name": "name"},
)
class AccessPolicyExcludeOkta:
    def __init__(
        self,
        *,
        identity_provider_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#name AccessPolicy#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyExcludeOkta.__init__)
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#name AccessPolicy#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyExcludeOkta(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyExcludeOktaList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeOktaList",
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
            type_hints = typing.get_type_hints(AccessPolicyExcludeOktaList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyExcludeOktaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyExcludeOktaList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyExcludeOktaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOktaList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOktaList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOktaList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeOkta]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeOkta]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeOkta]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOktaList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyExcludeOktaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeOktaOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyExcludeOktaOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOktaOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOktaOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyExcludeOkta, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyExcludeOkta, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyExcludeOkta, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOktaOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyExcludeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyExcludeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAzure")
    def put_azure(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessPolicyExcludeAzure, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyExcludeOutputReference.put_azure)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAzure", [value]))

    @jsii.member(jsii_name="putExternalEvaluation")
    def put_external_evaluation(
        self,
        *,
        evaluate_url: typing.Optional[builtins.str] = None,
        keys_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param evaluate_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#evaluate_url AccessPolicy#evaluate_url}.
        :param keys_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#keys_url AccessPolicy#keys_url}.
        '''
        value = AccessPolicyExcludeExternalEvaluation(
            evaluate_url=evaluate_url, keys_url=keys_url
        )

        return typing.cast(None, jsii.invoke(self, "putExternalEvaluation", [value]))

    @jsii.member(jsii_name="putGithub")
    def put_github(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessPolicyExcludeGithub, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyExcludeOutputReference.put_github)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGithub", [value]))

    @jsii.member(jsii_name="putGsuite")
    def put_gsuite(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessPolicyExcludeGsuite, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyExcludeOutputReference.put_gsuite)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGsuite", [value]))

    @jsii.member(jsii_name="putOkta")
    def put_okta(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessPolicyExcludeOkta, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyExcludeOutputReference.put_okta)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOkta", [value]))

    @jsii.member(jsii_name="putSaml")
    def put_saml(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyExcludeSaml", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyExcludeOutputReference.put_saml)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSaml", [value]))

    @jsii.member(jsii_name="resetAnyValidServiceToken")
    def reset_any_valid_service_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnyValidServiceToken", []))

    @jsii.member(jsii_name="resetAuthMethod")
    def reset_auth_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthMethod", []))

    @jsii.member(jsii_name="resetAzure")
    def reset_azure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzure", []))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetCommonName")
    def reset_common_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommonName", []))

    @jsii.member(jsii_name="resetDevicePosture")
    def reset_device_posture(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDevicePosture", []))

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetEmailDomain")
    def reset_email_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailDomain", []))

    @jsii.member(jsii_name="resetEveryone")
    def reset_everyone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEveryone", []))

    @jsii.member(jsii_name="resetExternalEvaluation")
    def reset_external_evaluation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalEvaluation", []))

    @jsii.member(jsii_name="resetGeo")
    def reset_geo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeo", []))

    @jsii.member(jsii_name="resetGithub")
    def reset_github(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithub", []))

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetGsuite")
    def reset_gsuite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGsuite", []))

    @jsii.member(jsii_name="resetIp")
    def reset_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIp", []))

    @jsii.member(jsii_name="resetLoginMethod")
    def reset_login_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginMethod", []))

    @jsii.member(jsii_name="resetOkta")
    def reset_okta(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOkta", []))

    @jsii.member(jsii_name="resetSaml")
    def reset_saml(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaml", []))

    @jsii.member(jsii_name="resetServiceToken")
    def reset_service_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceToken", []))

    @builtins.property
    @jsii.member(jsii_name="azure")
    def azure(self) -> AccessPolicyExcludeAzureList:
        return typing.cast(AccessPolicyExcludeAzureList, jsii.get(self, "azure"))

    @builtins.property
    @jsii.member(jsii_name="externalEvaluation")
    def external_evaluation(
        self,
    ) -> AccessPolicyExcludeExternalEvaluationOutputReference:
        return typing.cast(AccessPolicyExcludeExternalEvaluationOutputReference, jsii.get(self, "externalEvaluation"))

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> AccessPolicyExcludeGithubList:
        return typing.cast(AccessPolicyExcludeGithubList, jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="gsuite")
    def gsuite(self) -> AccessPolicyExcludeGsuiteList:
        return typing.cast(AccessPolicyExcludeGsuiteList, jsii.get(self, "gsuite"))

    @builtins.property
    @jsii.member(jsii_name="okta")
    def okta(self) -> AccessPolicyExcludeOktaList:
        return typing.cast(AccessPolicyExcludeOktaList, jsii.get(self, "okta"))

    @builtins.property
    @jsii.member(jsii_name="saml")
    def saml(self) -> "AccessPolicyExcludeSamlList":
        return typing.cast("AccessPolicyExcludeSamlList", jsii.get(self, "saml"))

    @builtins.property
    @jsii.member(jsii_name="anyValidServiceTokenInput")
    def any_valid_service_token_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "anyValidServiceTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="authMethodInput")
    def auth_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="azureInput")
    def azure_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeAzure]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeAzure]]], jsii.get(self, "azureInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="commonNameInput")
    def common_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commonNameInput"))

    @builtins.property
    @jsii.member(jsii_name="devicePostureInput")
    def device_posture_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "devicePostureInput"))

    @builtins.property
    @jsii.member(jsii_name="emailDomainInput")
    def email_domain_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="everyoneInput")
    def everyone_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "everyoneInput"))

    @builtins.property
    @jsii.member(jsii_name="externalEvaluationInput")
    def external_evaluation_input(
        self,
    ) -> typing.Optional[AccessPolicyExcludeExternalEvaluation]:
        return typing.cast(typing.Optional[AccessPolicyExcludeExternalEvaluation], jsii.get(self, "externalEvaluationInput"))

    @builtins.property
    @jsii.member(jsii_name="geoInput")
    def geo_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "geoInput"))

    @builtins.property
    @jsii.member(jsii_name="githubInput")
    def github_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeGithub]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeGithub]]], jsii.get(self, "githubInput"))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="gsuiteInput")
    def gsuite_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeGsuite]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeGsuite]]], jsii.get(self, "gsuiteInput"))

    @builtins.property
    @jsii.member(jsii_name="ipInput")
    def ip_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipInput"))

    @builtins.property
    @jsii.member(jsii_name="loginMethodInput")
    def login_method_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loginMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="oktaInput")
    def okta_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeOkta]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeOkta]]], jsii.get(self, "oktaInput"))

    @builtins.property
    @jsii.member(jsii_name="samlInput")
    def saml_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyExcludeSaml"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyExcludeSaml"]]], jsii.get(self, "samlInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceTokenInput")
    def service_token_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serviceTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="anyValidServiceToken")
    def any_valid_service_token(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "anyValidServiceToken"))

    @any_valid_service_token.setter
    def any_valid_service_token(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOutputReference, "any_valid_service_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anyValidServiceToken", value)

    @builtins.property
    @jsii.member(jsii_name="authMethod")
    def auth_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authMethod"))

    @auth_method.setter
    def auth_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOutputReference, "auth_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authMethod", value)

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOutputReference, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="commonName")
    def common_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commonName"))

    @common_name.setter
    def common_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOutputReference, "common_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commonName", value)

    @builtins.property
    @jsii.member(jsii_name="devicePosture")
    def device_posture(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "devicePosture"))

    @device_posture.setter
    def device_posture(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOutputReference, "device_posture").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "devicePosture", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOutputReference, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="emailDomain")
    def email_domain(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "emailDomain"))

    @email_domain.setter
    def email_domain(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOutputReference, "email_domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailDomain", value)

    @builtins.property
    @jsii.member(jsii_name="everyone")
    def everyone(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "everyone"))

    @everyone.setter
    def everyone(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOutputReference, "everyone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "everyone", value)

    @builtins.property
    @jsii.member(jsii_name="geo")
    def geo(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "geo"))

    @geo.setter
    def geo(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOutputReference, "geo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geo", value)

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "group"))

    @group.setter
    def group(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOutputReference, "group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="ip")
    def ip(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ip"))

    @ip.setter
    def ip(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOutputReference, "ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ip", value)

    @builtins.property
    @jsii.member(jsii_name="loginMethod")
    def login_method(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loginMethod"))

    @login_method.setter
    def login_method(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOutputReference, "login_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginMethod", value)

    @builtins.property
    @jsii.member(jsii_name="serviceToken")
    def service_token(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "serviceToken"))

    @service_token.setter
    def service_token(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOutputReference, "service_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyExclude, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyExclude, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyExclude, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeSaml",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_name": "attributeName",
        "attribute_value": "attributeValue",
        "identity_provider_id": "identityProviderId",
    },
)
class AccessPolicyExcludeSaml:
    def __init__(
        self,
        *,
        attribute_name: typing.Optional[builtins.str] = None,
        attribute_value: typing.Optional[builtins.str] = None,
        identity_provider_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param attribute_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#attribute_name AccessPolicy#attribute_name}.
        :param attribute_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#attribute_value AccessPolicy#attribute_value}.
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyExcludeSaml.__init__)
            check_type(argname="argument attribute_name", value=attribute_name, expected_type=type_hints["attribute_name"])
            check_type(argname="argument attribute_value", value=attribute_value, expected_type=type_hints["attribute_value"])
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if attribute_name is not None:
            self._values["attribute_name"] = attribute_name
        if attribute_value is not None:
            self._values["attribute_value"] = attribute_value
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id

    @builtins.property
    def attribute_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#attribute_name AccessPolicy#attribute_name}.'''
        result = self._values.get("attribute_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attribute_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#attribute_value AccessPolicy#attribute_value}.'''
        result = self._values.get("attribute_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyExcludeSaml(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyExcludeSamlList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeSamlList",
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
            type_hints = typing.get_type_hints(AccessPolicyExcludeSamlList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyExcludeSamlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyExcludeSamlList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyExcludeSamlOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeSamlList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeSamlList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeSamlList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeSaml]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeSaml]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyExcludeSaml]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeSamlList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyExcludeSamlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyExcludeSamlOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyExcludeSamlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAttributeName")
    def reset_attribute_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeName", []))

    @jsii.member(jsii_name="resetAttributeValue")
    def reset_attribute_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeValue", []))

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @builtins.property
    @jsii.member(jsii_name="attributeNameInput")
    def attribute_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeValueInput")
    def attribute_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeValueInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeName")
    def attribute_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeName"))

    @attribute_name.setter
    def attribute_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeSamlOutputReference, "attribute_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeName", value)

    @builtins.property
    @jsii.member(jsii_name="attributeValue")
    def attribute_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeValue"))

    @attribute_value.setter
    def attribute_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeSamlOutputReference, "attribute_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeValue", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeSamlOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyExcludeSaml, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyExcludeSaml, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyExcludeSaml, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyExcludeSamlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyInclude",
    jsii_struct_bases=[],
    name_mapping={
        "any_valid_service_token": "anyValidServiceToken",
        "auth_method": "authMethod",
        "azure": "azure",
        "certificate": "certificate",
        "common_name": "commonName",
        "device_posture": "devicePosture",
        "email": "email",
        "email_domain": "emailDomain",
        "everyone": "everyone",
        "external_evaluation": "externalEvaluation",
        "geo": "geo",
        "github": "github",
        "group": "group",
        "gsuite": "gsuite",
        "ip": "ip",
        "login_method": "loginMethod",
        "okta": "okta",
        "saml": "saml",
        "service_token": "serviceToken",
    },
)
class AccessPolicyInclude:
    def __init__(
        self,
        *,
        any_valid_service_token: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auth_method: typing.Optional[builtins.str] = None,
        azure: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyIncludeAzure", typing.Dict[str, typing.Any]]]]] = None,
        certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        common_name: typing.Optional[builtins.str] = None,
        device_posture: typing.Optional[typing.Sequence[builtins.str]] = None,
        email: typing.Optional[typing.Sequence[builtins.str]] = None,
        email_domain: typing.Optional[typing.Sequence[builtins.str]] = None,
        everyone: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        external_evaluation: typing.Optional[typing.Union["AccessPolicyIncludeExternalEvaluation", typing.Dict[str, typing.Any]]] = None,
        geo: typing.Optional[typing.Sequence[builtins.str]] = None,
        github: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyIncludeGithub", typing.Dict[str, typing.Any]]]]] = None,
        group: typing.Optional[typing.Sequence[builtins.str]] = None,
        gsuite: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyIncludeGsuite", typing.Dict[str, typing.Any]]]]] = None,
        ip: typing.Optional[typing.Sequence[builtins.str]] = None,
        login_method: typing.Optional[typing.Sequence[builtins.str]] = None,
        okta: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyIncludeOkta", typing.Dict[str, typing.Any]]]]] = None,
        saml: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyIncludeSaml", typing.Dict[str, typing.Any]]]]] = None,
        service_token: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param any_valid_service_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#any_valid_service_token AccessPolicy#any_valid_service_token}.
        :param auth_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#auth_method AccessPolicy#auth_method}.
        :param azure: azure block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#azure AccessPolicy#azure}
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#certificate AccessPolicy#certificate}.
        :param common_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#common_name AccessPolicy#common_name}.
        :param device_posture: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#device_posture AccessPolicy#device_posture}.
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email AccessPolicy#email}.
        :param email_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email_domain AccessPolicy#email_domain}.
        :param everyone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#everyone AccessPolicy#everyone}.
        :param external_evaluation: external_evaluation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#external_evaluation AccessPolicy#external_evaluation}
        :param geo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#geo AccessPolicy#geo}.
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#github AccessPolicy#github}
        :param group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#group AccessPolicy#group}.
        :param gsuite: gsuite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#gsuite AccessPolicy#gsuite}
        :param ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#ip AccessPolicy#ip}.
        :param login_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#login_method AccessPolicy#login_method}.
        :param okta: okta block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#okta AccessPolicy#okta}
        :param saml: saml block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#saml AccessPolicy#saml}
        :param service_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#service_token AccessPolicy#service_token}.
        '''
        if isinstance(external_evaluation, dict):
            external_evaluation = AccessPolicyIncludeExternalEvaluation(**external_evaluation)
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyInclude.__init__)
            check_type(argname="argument any_valid_service_token", value=any_valid_service_token, expected_type=type_hints["any_valid_service_token"])
            check_type(argname="argument auth_method", value=auth_method, expected_type=type_hints["auth_method"])
            check_type(argname="argument azure", value=azure, expected_type=type_hints["azure"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument common_name", value=common_name, expected_type=type_hints["common_name"])
            check_type(argname="argument device_posture", value=device_posture, expected_type=type_hints["device_posture"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument email_domain", value=email_domain, expected_type=type_hints["email_domain"])
            check_type(argname="argument everyone", value=everyone, expected_type=type_hints["everyone"])
            check_type(argname="argument external_evaluation", value=external_evaluation, expected_type=type_hints["external_evaluation"])
            check_type(argname="argument geo", value=geo, expected_type=type_hints["geo"])
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument gsuite", value=gsuite, expected_type=type_hints["gsuite"])
            check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
            check_type(argname="argument login_method", value=login_method, expected_type=type_hints["login_method"])
            check_type(argname="argument okta", value=okta, expected_type=type_hints["okta"])
            check_type(argname="argument saml", value=saml, expected_type=type_hints["saml"])
            check_type(argname="argument service_token", value=service_token, expected_type=type_hints["service_token"])
        self._values: typing.Dict[str, typing.Any] = {}
        if any_valid_service_token is not None:
            self._values["any_valid_service_token"] = any_valid_service_token
        if auth_method is not None:
            self._values["auth_method"] = auth_method
        if azure is not None:
            self._values["azure"] = azure
        if certificate is not None:
            self._values["certificate"] = certificate
        if common_name is not None:
            self._values["common_name"] = common_name
        if device_posture is not None:
            self._values["device_posture"] = device_posture
        if email is not None:
            self._values["email"] = email
        if email_domain is not None:
            self._values["email_domain"] = email_domain
        if everyone is not None:
            self._values["everyone"] = everyone
        if external_evaluation is not None:
            self._values["external_evaluation"] = external_evaluation
        if geo is not None:
            self._values["geo"] = geo
        if github is not None:
            self._values["github"] = github
        if group is not None:
            self._values["group"] = group
        if gsuite is not None:
            self._values["gsuite"] = gsuite
        if ip is not None:
            self._values["ip"] = ip
        if login_method is not None:
            self._values["login_method"] = login_method
        if okta is not None:
            self._values["okta"] = okta
        if saml is not None:
            self._values["saml"] = saml
        if service_token is not None:
            self._values["service_token"] = service_token

    @builtins.property
    def any_valid_service_token(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#any_valid_service_token AccessPolicy#any_valid_service_token}.'''
        result = self._values.get("any_valid_service_token")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auth_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#auth_method AccessPolicy#auth_method}.'''
        result = self._values.get("auth_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyIncludeAzure"]]]:
        '''azure block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#azure AccessPolicy#azure}
        '''
        result = self._values.get("azure")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyIncludeAzure"]]], result)

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#certificate AccessPolicy#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def common_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#common_name AccessPolicy#common_name}.'''
        result = self._values.get("common_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def device_posture(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#device_posture AccessPolicy#device_posture}.'''
        result = self._values.get("device_posture")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email AccessPolicy#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email_domain(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email_domain AccessPolicy#email_domain}.'''
        result = self._values.get("email_domain")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def everyone(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#everyone AccessPolicy#everyone}.'''
        result = self._values.get("everyone")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def external_evaluation(
        self,
    ) -> typing.Optional["AccessPolicyIncludeExternalEvaluation"]:
        '''external_evaluation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#external_evaluation AccessPolicy#external_evaluation}
        '''
        result = self._values.get("external_evaluation")
        return typing.cast(typing.Optional["AccessPolicyIncludeExternalEvaluation"], result)

    @builtins.property
    def geo(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#geo AccessPolicy#geo}.'''
        result = self._values.get("geo")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def github(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyIncludeGithub"]]]:
        '''github block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#github AccessPolicy#github}
        '''
        result = self._values.get("github")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyIncludeGithub"]]], result)

    @builtins.property
    def group(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#group AccessPolicy#group}.'''
        result = self._values.get("group")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def gsuite(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyIncludeGsuite"]]]:
        '''gsuite block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#gsuite AccessPolicy#gsuite}
        '''
        result = self._values.get("gsuite")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyIncludeGsuite"]]], result)

    @builtins.property
    def ip(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#ip AccessPolicy#ip}.'''
        result = self._values.get("ip")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def login_method(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#login_method AccessPolicy#login_method}.'''
        result = self._values.get("login_method")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def okta(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyIncludeOkta"]]]:
        '''okta block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#okta AccessPolicy#okta}
        '''
        result = self._values.get("okta")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyIncludeOkta"]]], result)

    @builtins.property
    def saml(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyIncludeSaml"]]]:
        '''saml block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#saml AccessPolicy#saml}
        '''
        result = self._values.get("saml")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyIncludeSaml"]]], result)

    @builtins.property
    def service_token(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#service_token AccessPolicy#service_token}.'''
        result = self._values.get("service_token")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyInclude(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeAzure",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "identity_provider_id": "identityProviderId"},
)
class AccessPolicyIncludeAzure:
    def __init__(
        self,
        *,
        id: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_provider_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#id AccessPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyIncludeAzure.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id

    @builtins.property
    def id(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#id AccessPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyIncludeAzure(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyIncludeAzureList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeAzureList",
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
            type_hints = typing.get_type_hints(AccessPolicyIncludeAzureList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyIncludeAzureOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyIncludeAzureList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyIncludeAzureOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeAzureList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeAzureList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeAzureList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeAzure]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeAzure]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeAzure]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeAzureList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyIncludeAzureOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeAzureOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyIncludeAzureOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "id"))

    @id.setter
    def id(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeAzureOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeAzureOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyIncludeAzure, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyIncludeAzure, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyIncludeAzure, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeAzureOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeExternalEvaluation",
    jsii_struct_bases=[],
    name_mapping={"evaluate_url": "evaluateUrl", "keys_url": "keysUrl"},
)
class AccessPolicyIncludeExternalEvaluation:
    def __init__(
        self,
        *,
        evaluate_url: typing.Optional[builtins.str] = None,
        keys_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param evaluate_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#evaluate_url AccessPolicy#evaluate_url}.
        :param keys_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#keys_url AccessPolicy#keys_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyIncludeExternalEvaluation.__init__)
            check_type(argname="argument evaluate_url", value=evaluate_url, expected_type=type_hints["evaluate_url"])
            check_type(argname="argument keys_url", value=keys_url, expected_type=type_hints["keys_url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if evaluate_url is not None:
            self._values["evaluate_url"] = evaluate_url
        if keys_url is not None:
            self._values["keys_url"] = keys_url

    @builtins.property
    def evaluate_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#evaluate_url AccessPolicy#evaluate_url}.'''
        result = self._values.get("evaluate_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keys_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#keys_url AccessPolicy#keys_url}.'''
        result = self._values.get("keys_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyIncludeExternalEvaluation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyIncludeExternalEvaluationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeExternalEvaluationOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyIncludeExternalEvaluationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEvaluateUrl")
    def reset_evaluate_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluateUrl", []))

    @jsii.member(jsii_name="resetKeysUrl")
    def reset_keys_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeysUrl", []))

    @builtins.property
    @jsii.member(jsii_name="evaluateUrlInput")
    def evaluate_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluateUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="keysUrlInput")
    def keys_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keysUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluateUrl")
    def evaluate_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "evaluateUrl"))

    @evaluate_url.setter
    def evaluate_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeExternalEvaluationOutputReference, "evaluate_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluateUrl", value)

    @builtins.property
    @jsii.member(jsii_name="keysUrl")
    def keys_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keysUrl"))

    @keys_url.setter
    def keys_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeExternalEvaluationOutputReference, "keys_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keysUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AccessPolicyIncludeExternalEvaluation]:
        return typing.cast(typing.Optional[AccessPolicyIncludeExternalEvaluation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AccessPolicyIncludeExternalEvaluation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeExternalEvaluationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeGithub",
    jsii_struct_bases=[],
    name_mapping={
        "identity_provider_id": "identityProviderId",
        "name": "name",
        "teams": "teams",
    },
)
class AccessPolicyIncludeGithub:
    def __init__(
        self,
        *,
        identity_provider_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        teams: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#name AccessPolicy#name}.
        :param teams: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#teams AccessPolicy#teams}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyIncludeGithub.__init__)
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument teams", value=teams, expected_type=type_hints["teams"])
        self._values: typing.Dict[str, typing.Any] = {}
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id
        if name is not None:
            self._values["name"] = name
        if teams is not None:
            self._values["teams"] = teams

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#name AccessPolicy#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def teams(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#teams AccessPolicy#teams}.'''
        result = self._values.get("teams")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyIncludeGithub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyIncludeGithubList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeGithubList",
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
            type_hints = typing.get_type_hints(AccessPolicyIncludeGithubList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyIncludeGithubOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyIncludeGithubList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyIncludeGithubOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeGithubList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeGithubList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeGithubList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeGithub]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeGithub]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeGithub]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeGithubList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyIncludeGithubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeGithubOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyIncludeGithubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetTeams")
    def reset_teams(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeams", []))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="teamsInput")
    def teams_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "teamsInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeGithubOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeGithubOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="teams")
    def teams(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "teams"))

    @teams.setter
    def teams(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeGithubOutputReference, "teams").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teams", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyIncludeGithub, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyIncludeGithub, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyIncludeGithub, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeGithubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeGsuite",
    jsii_struct_bases=[],
    name_mapping={"email": "email", "identity_provider_id": "identityProviderId"},
)
class AccessPolicyIncludeGsuite:
    def __init__(
        self,
        *,
        email: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_provider_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email AccessPolicy#email}.
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyIncludeGsuite.__init__)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if email is not None:
            self._values["email"] = email
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id

    @builtins.property
    def email(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email AccessPolicy#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyIncludeGsuite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyIncludeGsuiteList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeGsuiteList",
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
            type_hints = typing.get_type_hints(AccessPolicyIncludeGsuiteList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyIncludeGsuiteOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyIncludeGsuiteList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyIncludeGsuiteOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeGsuiteList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeGsuiteList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeGsuiteList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeGsuite]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeGsuite]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeGsuite]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeGsuiteList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyIncludeGsuiteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeGsuiteOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyIncludeGsuiteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeGsuiteOutputReference, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeGsuiteOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyIncludeGsuite, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyIncludeGsuite, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyIncludeGsuite, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeGsuiteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyIncludeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeList",
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
            type_hints = typing.get_type_hints(AccessPolicyIncludeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyIncludeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyIncludeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyIncludeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyInclude]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyInclude]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyInclude]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeOkta",
    jsii_struct_bases=[],
    name_mapping={"identity_provider_id": "identityProviderId", "name": "name"},
)
class AccessPolicyIncludeOkta:
    def __init__(
        self,
        *,
        identity_provider_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#name AccessPolicy#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyIncludeOkta.__init__)
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#name AccessPolicy#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyIncludeOkta(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyIncludeOktaList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeOktaList",
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
            type_hints = typing.get_type_hints(AccessPolicyIncludeOktaList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyIncludeOktaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyIncludeOktaList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyIncludeOktaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOktaList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOktaList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOktaList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeOkta]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeOkta]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeOkta]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOktaList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyIncludeOktaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeOktaOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyIncludeOktaOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOktaOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOktaOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyIncludeOkta, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyIncludeOkta, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyIncludeOkta, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOktaOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyIncludeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyIncludeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAzure")
    def put_azure(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessPolicyIncludeAzure, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyIncludeOutputReference.put_azure)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAzure", [value]))

    @jsii.member(jsii_name="putExternalEvaluation")
    def put_external_evaluation(
        self,
        *,
        evaluate_url: typing.Optional[builtins.str] = None,
        keys_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param evaluate_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#evaluate_url AccessPolicy#evaluate_url}.
        :param keys_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#keys_url AccessPolicy#keys_url}.
        '''
        value = AccessPolicyIncludeExternalEvaluation(
            evaluate_url=evaluate_url, keys_url=keys_url
        )

        return typing.cast(None, jsii.invoke(self, "putExternalEvaluation", [value]))

    @jsii.member(jsii_name="putGithub")
    def put_github(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessPolicyIncludeGithub, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyIncludeOutputReference.put_github)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGithub", [value]))

    @jsii.member(jsii_name="putGsuite")
    def put_gsuite(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessPolicyIncludeGsuite, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyIncludeOutputReference.put_gsuite)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGsuite", [value]))

    @jsii.member(jsii_name="putOkta")
    def put_okta(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessPolicyIncludeOkta, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyIncludeOutputReference.put_okta)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOkta", [value]))

    @jsii.member(jsii_name="putSaml")
    def put_saml(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyIncludeSaml", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyIncludeOutputReference.put_saml)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSaml", [value]))

    @jsii.member(jsii_name="resetAnyValidServiceToken")
    def reset_any_valid_service_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnyValidServiceToken", []))

    @jsii.member(jsii_name="resetAuthMethod")
    def reset_auth_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthMethod", []))

    @jsii.member(jsii_name="resetAzure")
    def reset_azure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzure", []))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetCommonName")
    def reset_common_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommonName", []))

    @jsii.member(jsii_name="resetDevicePosture")
    def reset_device_posture(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDevicePosture", []))

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetEmailDomain")
    def reset_email_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailDomain", []))

    @jsii.member(jsii_name="resetEveryone")
    def reset_everyone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEveryone", []))

    @jsii.member(jsii_name="resetExternalEvaluation")
    def reset_external_evaluation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalEvaluation", []))

    @jsii.member(jsii_name="resetGeo")
    def reset_geo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeo", []))

    @jsii.member(jsii_name="resetGithub")
    def reset_github(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithub", []))

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetGsuite")
    def reset_gsuite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGsuite", []))

    @jsii.member(jsii_name="resetIp")
    def reset_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIp", []))

    @jsii.member(jsii_name="resetLoginMethod")
    def reset_login_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginMethod", []))

    @jsii.member(jsii_name="resetOkta")
    def reset_okta(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOkta", []))

    @jsii.member(jsii_name="resetSaml")
    def reset_saml(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaml", []))

    @jsii.member(jsii_name="resetServiceToken")
    def reset_service_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceToken", []))

    @builtins.property
    @jsii.member(jsii_name="azure")
    def azure(self) -> AccessPolicyIncludeAzureList:
        return typing.cast(AccessPolicyIncludeAzureList, jsii.get(self, "azure"))

    @builtins.property
    @jsii.member(jsii_name="externalEvaluation")
    def external_evaluation(
        self,
    ) -> AccessPolicyIncludeExternalEvaluationOutputReference:
        return typing.cast(AccessPolicyIncludeExternalEvaluationOutputReference, jsii.get(self, "externalEvaluation"))

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> AccessPolicyIncludeGithubList:
        return typing.cast(AccessPolicyIncludeGithubList, jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="gsuite")
    def gsuite(self) -> AccessPolicyIncludeGsuiteList:
        return typing.cast(AccessPolicyIncludeGsuiteList, jsii.get(self, "gsuite"))

    @builtins.property
    @jsii.member(jsii_name="okta")
    def okta(self) -> AccessPolicyIncludeOktaList:
        return typing.cast(AccessPolicyIncludeOktaList, jsii.get(self, "okta"))

    @builtins.property
    @jsii.member(jsii_name="saml")
    def saml(self) -> "AccessPolicyIncludeSamlList":
        return typing.cast("AccessPolicyIncludeSamlList", jsii.get(self, "saml"))

    @builtins.property
    @jsii.member(jsii_name="anyValidServiceTokenInput")
    def any_valid_service_token_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "anyValidServiceTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="authMethodInput")
    def auth_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="azureInput")
    def azure_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeAzure]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeAzure]]], jsii.get(self, "azureInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="commonNameInput")
    def common_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commonNameInput"))

    @builtins.property
    @jsii.member(jsii_name="devicePostureInput")
    def device_posture_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "devicePostureInput"))

    @builtins.property
    @jsii.member(jsii_name="emailDomainInput")
    def email_domain_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="everyoneInput")
    def everyone_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "everyoneInput"))

    @builtins.property
    @jsii.member(jsii_name="externalEvaluationInput")
    def external_evaluation_input(
        self,
    ) -> typing.Optional[AccessPolicyIncludeExternalEvaluation]:
        return typing.cast(typing.Optional[AccessPolicyIncludeExternalEvaluation], jsii.get(self, "externalEvaluationInput"))

    @builtins.property
    @jsii.member(jsii_name="geoInput")
    def geo_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "geoInput"))

    @builtins.property
    @jsii.member(jsii_name="githubInput")
    def github_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeGithub]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeGithub]]], jsii.get(self, "githubInput"))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="gsuiteInput")
    def gsuite_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeGsuite]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeGsuite]]], jsii.get(self, "gsuiteInput"))

    @builtins.property
    @jsii.member(jsii_name="ipInput")
    def ip_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipInput"))

    @builtins.property
    @jsii.member(jsii_name="loginMethodInput")
    def login_method_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loginMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="oktaInput")
    def okta_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeOkta]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeOkta]]], jsii.get(self, "oktaInput"))

    @builtins.property
    @jsii.member(jsii_name="samlInput")
    def saml_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyIncludeSaml"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyIncludeSaml"]]], jsii.get(self, "samlInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceTokenInput")
    def service_token_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serviceTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="anyValidServiceToken")
    def any_valid_service_token(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "anyValidServiceToken"))

    @any_valid_service_token.setter
    def any_valid_service_token(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOutputReference, "any_valid_service_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anyValidServiceToken", value)

    @builtins.property
    @jsii.member(jsii_name="authMethod")
    def auth_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authMethod"))

    @auth_method.setter
    def auth_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOutputReference, "auth_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authMethod", value)

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOutputReference, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="commonName")
    def common_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commonName"))

    @common_name.setter
    def common_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOutputReference, "common_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commonName", value)

    @builtins.property
    @jsii.member(jsii_name="devicePosture")
    def device_posture(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "devicePosture"))

    @device_posture.setter
    def device_posture(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOutputReference, "device_posture").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "devicePosture", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOutputReference, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="emailDomain")
    def email_domain(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "emailDomain"))

    @email_domain.setter
    def email_domain(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOutputReference, "email_domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailDomain", value)

    @builtins.property
    @jsii.member(jsii_name="everyone")
    def everyone(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "everyone"))

    @everyone.setter
    def everyone(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOutputReference, "everyone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "everyone", value)

    @builtins.property
    @jsii.member(jsii_name="geo")
    def geo(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "geo"))

    @geo.setter
    def geo(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOutputReference, "geo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geo", value)

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "group"))

    @group.setter
    def group(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOutputReference, "group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="ip")
    def ip(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ip"))

    @ip.setter
    def ip(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOutputReference, "ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ip", value)

    @builtins.property
    @jsii.member(jsii_name="loginMethod")
    def login_method(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loginMethod"))

    @login_method.setter
    def login_method(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOutputReference, "login_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginMethod", value)

    @builtins.property
    @jsii.member(jsii_name="serviceToken")
    def service_token(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "serviceToken"))

    @service_token.setter
    def service_token(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOutputReference, "service_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyInclude, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyInclude, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyInclude, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeSaml",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_name": "attributeName",
        "attribute_value": "attributeValue",
        "identity_provider_id": "identityProviderId",
    },
)
class AccessPolicyIncludeSaml:
    def __init__(
        self,
        *,
        attribute_name: typing.Optional[builtins.str] = None,
        attribute_value: typing.Optional[builtins.str] = None,
        identity_provider_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param attribute_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#attribute_name AccessPolicy#attribute_name}.
        :param attribute_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#attribute_value AccessPolicy#attribute_value}.
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyIncludeSaml.__init__)
            check_type(argname="argument attribute_name", value=attribute_name, expected_type=type_hints["attribute_name"])
            check_type(argname="argument attribute_value", value=attribute_value, expected_type=type_hints["attribute_value"])
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if attribute_name is not None:
            self._values["attribute_name"] = attribute_name
        if attribute_value is not None:
            self._values["attribute_value"] = attribute_value
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id

    @builtins.property
    def attribute_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#attribute_name AccessPolicy#attribute_name}.'''
        result = self._values.get("attribute_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attribute_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#attribute_value AccessPolicy#attribute_value}.'''
        result = self._values.get("attribute_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyIncludeSaml(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyIncludeSamlList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeSamlList",
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
            type_hints = typing.get_type_hints(AccessPolicyIncludeSamlList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyIncludeSamlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyIncludeSamlList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyIncludeSamlOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeSamlList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeSamlList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeSamlList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeSaml]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeSaml]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyIncludeSaml]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeSamlList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyIncludeSamlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyIncludeSamlOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyIncludeSamlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAttributeName")
    def reset_attribute_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeName", []))

    @jsii.member(jsii_name="resetAttributeValue")
    def reset_attribute_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeValue", []))

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @builtins.property
    @jsii.member(jsii_name="attributeNameInput")
    def attribute_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeValueInput")
    def attribute_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeValueInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeName")
    def attribute_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeName"))

    @attribute_name.setter
    def attribute_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeSamlOutputReference, "attribute_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeName", value)

    @builtins.property
    @jsii.member(jsii_name="attributeValue")
    def attribute_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeValue"))

    @attribute_value.setter
    def attribute_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeSamlOutputReference, "attribute_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeValue", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeSamlOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyIncludeSaml, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyIncludeSaml, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyIncludeSaml, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyIncludeSamlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequire",
    jsii_struct_bases=[],
    name_mapping={
        "any_valid_service_token": "anyValidServiceToken",
        "auth_method": "authMethod",
        "azure": "azure",
        "certificate": "certificate",
        "common_name": "commonName",
        "device_posture": "devicePosture",
        "email": "email",
        "email_domain": "emailDomain",
        "everyone": "everyone",
        "external_evaluation": "externalEvaluation",
        "geo": "geo",
        "github": "github",
        "group": "group",
        "gsuite": "gsuite",
        "ip": "ip",
        "login_method": "loginMethod",
        "okta": "okta",
        "saml": "saml",
        "service_token": "serviceToken",
    },
)
class AccessPolicyRequire:
    def __init__(
        self,
        *,
        any_valid_service_token: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auth_method: typing.Optional[builtins.str] = None,
        azure: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyRequireAzure", typing.Dict[str, typing.Any]]]]] = None,
        certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        common_name: typing.Optional[builtins.str] = None,
        device_posture: typing.Optional[typing.Sequence[builtins.str]] = None,
        email: typing.Optional[typing.Sequence[builtins.str]] = None,
        email_domain: typing.Optional[typing.Sequence[builtins.str]] = None,
        everyone: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        external_evaluation: typing.Optional[typing.Union["AccessPolicyRequireExternalEvaluation", typing.Dict[str, typing.Any]]] = None,
        geo: typing.Optional[typing.Sequence[builtins.str]] = None,
        github: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyRequireGithub", typing.Dict[str, typing.Any]]]]] = None,
        group: typing.Optional[typing.Sequence[builtins.str]] = None,
        gsuite: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyRequireGsuite", typing.Dict[str, typing.Any]]]]] = None,
        ip: typing.Optional[typing.Sequence[builtins.str]] = None,
        login_method: typing.Optional[typing.Sequence[builtins.str]] = None,
        okta: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyRequireOkta", typing.Dict[str, typing.Any]]]]] = None,
        saml: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyRequireSaml", typing.Dict[str, typing.Any]]]]] = None,
        service_token: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param any_valid_service_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#any_valid_service_token AccessPolicy#any_valid_service_token}.
        :param auth_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#auth_method AccessPolicy#auth_method}.
        :param azure: azure block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#azure AccessPolicy#azure}
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#certificate AccessPolicy#certificate}.
        :param common_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#common_name AccessPolicy#common_name}.
        :param device_posture: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#device_posture AccessPolicy#device_posture}.
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email AccessPolicy#email}.
        :param email_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email_domain AccessPolicy#email_domain}.
        :param everyone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#everyone AccessPolicy#everyone}.
        :param external_evaluation: external_evaluation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#external_evaluation AccessPolicy#external_evaluation}
        :param geo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#geo AccessPolicy#geo}.
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#github AccessPolicy#github}
        :param group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#group AccessPolicy#group}.
        :param gsuite: gsuite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#gsuite AccessPolicy#gsuite}
        :param ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#ip AccessPolicy#ip}.
        :param login_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#login_method AccessPolicy#login_method}.
        :param okta: okta block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#okta AccessPolicy#okta}
        :param saml: saml block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#saml AccessPolicy#saml}
        :param service_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#service_token AccessPolicy#service_token}.
        '''
        if isinstance(external_evaluation, dict):
            external_evaluation = AccessPolicyRequireExternalEvaluation(**external_evaluation)
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyRequire.__init__)
            check_type(argname="argument any_valid_service_token", value=any_valid_service_token, expected_type=type_hints["any_valid_service_token"])
            check_type(argname="argument auth_method", value=auth_method, expected_type=type_hints["auth_method"])
            check_type(argname="argument azure", value=azure, expected_type=type_hints["azure"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument common_name", value=common_name, expected_type=type_hints["common_name"])
            check_type(argname="argument device_posture", value=device_posture, expected_type=type_hints["device_posture"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument email_domain", value=email_domain, expected_type=type_hints["email_domain"])
            check_type(argname="argument everyone", value=everyone, expected_type=type_hints["everyone"])
            check_type(argname="argument external_evaluation", value=external_evaluation, expected_type=type_hints["external_evaluation"])
            check_type(argname="argument geo", value=geo, expected_type=type_hints["geo"])
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument gsuite", value=gsuite, expected_type=type_hints["gsuite"])
            check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
            check_type(argname="argument login_method", value=login_method, expected_type=type_hints["login_method"])
            check_type(argname="argument okta", value=okta, expected_type=type_hints["okta"])
            check_type(argname="argument saml", value=saml, expected_type=type_hints["saml"])
            check_type(argname="argument service_token", value=service_token, expected_type=type_hints["service_token"])
        self._values: typing.Dict[str, typing.Any] = {}
        if any_valid_service_token is not None:
            self._values["any_valid_service_token"] = any_valid_service_token
        if auth_method is not None:
            self._values["auth_method"] = auth_method
        if azure is not None:
            self._values["azure"] = azure
        if certificate is not None:
            self._values["certificate"] = certificate
        if common_name is not None:
            self._values["common_name"] = common_name
        if device_posture is not None:
            self._values["device_posture"] = device_posture
        if email is not None:
            self._values["email"] = email
        if email_domain is not None:
            self._values["email_domain"] = email_domain
        if everyone is not None:
            self._values["everyone"] = everyone
        if external_evaluation is not None:
            self._values["external_evaluation"] = external_evaluation
        if geo is not None:
            self._values["geo"] = geo
        if github is not None:
            self._values["github"] = github
        if group is not None:
            self._values["group"] = group
        if gsuite is not None:
            self._values["gsuite"] = gsuite
        if ip is not None:
            self._values["ip"] = ip
        if login_method is not None:
            self._values["login_method"] = login_method
        if okta is not None:
            self._values["okta"] = okta
        if saml is not None:
            self._values["saml"] = saml
        if service_token is not None:
            self._values["service_token"] = service_token

    @builtins.property
    def any_valid_service_token(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#any_valid_service_token AccessPolicy#any_valid_service_token}.'''
        result = self._values.get("any_valid_service_token")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auth_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#auth_method AccessPolicy#auth_method}.'''
        result = self._values.get("auth_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyRequireAzure"]]]:
        '''azure block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#azure AccessPolicy#azure}
        '''
        result = self._values.get("azure")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyRequireAzure"]]], result)

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#certificate AccessPolicy#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def common_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#common_name AccessPolicy#common_name}.'''
        result = self._values.get("common_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def device_posture(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#device_posture AccessPolicy#device_posture}.'''
        result = self._values.get("device_posture")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email AccessPolicy#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email_domain(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email_domain AccessPolicy#email_domain}.'''
        result = self._values.get("email_domain")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def everyone(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#everyone AccessPolicy#everyone}.'''
        result = self._values.get("everyone")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def external_evaluation(
        self,
    ) -> typing.Optional["AccessPolicyRequireExternalEvaluation"]:
        '''external_evaluation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#external_evaluation AccessPolicy#external_evaluation}
        '''
        result = self._values.get("external_evaluation")
        return typing.cast(typing.Optional["AccessPolicyRequireExternalEvaluation"], result)

    @builtins.property
    def geo(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#geo AccessPolicy#geo}.'''
        result = self._values.get("geo")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def github(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyRequireGithub"]]]:
        '''github block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#github AccessPolicy#github}
        '''
        result = self._values.get("github")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyRequireGithub"]]], result)

    @builtins.property
    def group(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#group AccessPolicy#group}.'''
        result = self._values.get("group")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def gsuite(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyRequireGsuite"]]]:
        '''gsuite block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#gsuite AccessPolicy#gsuite}
        '''
        result = self._values.get("gsuite")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyRequireGsuite"]]], result)

    @builtins.property
    def ip(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#ip AccessPolicy#ip}.'''
        result = self._values.get("ip")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def login_method(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#login_method AccessPolicy#login_method}.'''
        result = self._values.get("login_method")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def okta(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyRequireOkta"]]]:
        '''okta block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#okta AccessPolicy#okta}
        '''
        result = self._values.get("okta")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyRequireOkta"]]], result)

    @builtins.property
    def saml(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyRequireSaml"]]]:
        '''saml block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#saml AccessPolicy#saml}
        '''
        result = self._values.get("saml")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyRequireSaml"]]], result)

    @builtins.property
    def service_token(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#service_token AccessPolicy#service_token}.'''
        result = self._values.get("service_token")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyRequire(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireAzure",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "identity_provider_id": "identityProviderId"},
)
class AccessPolicyRequireAzure:
    def __init__(
        self,
        *,
        id: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_provider_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#id AccessPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyRequireAzure.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id

    @builtins.property
    def id(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#id AccessPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyRequireAzure(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyRequireAzureList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireAzureList",
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
            type_hints = typing.get_type_hints(AccessPolicyRequireAzureList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyRequireAzureOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyRequireAzureList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyRequireAzureOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireAzureList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireAzureList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireAzureList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireAzure]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireAzure]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireAzure]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireAzureList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyRequireAzureOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireAzureOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyRequireAzureOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "id"))

    @id.setter
    def id(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireAzureOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireAzureOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyRequireAzure, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyRequireAzure, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyRequireAzure, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireAzureOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireExternalEvaluation",
    jsii_struct_bases=[],
    name_mapping={"evaluate_url": "evaluateUrl", "keys_url": "keysUrl"},
)
class AccessPolicyRequireExternalEvaluation:
    def __init__(
        self,
        *,
        evaluate_url: typing.Optional[builtins.str] = None,
        keys_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param evaluate_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#evaluate_url AccessPolicy#evaluate_url}.
        :param keys_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#keys_url AccessPolicy#keys_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyRequireExternalEvaluation.__init__)
            check_type(argname="argument evaluate_url", value=evaluate_url, expected_type=type_hints["evaluate_url"])
            check_type(argname="argument keys_url", value=keys_url, expected_type=type_hints["keys_url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if evaluate_url is not None:
            self._values["evaluate_url"] = evaluate_url
        if keys_url is not None:
            self._values["keys_url"] = keys_url

    @builtins.property
    def evaluate_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#evaluate_url AccessPolicy#evaluate_url}.'''
        result = self._values.get("evaluate_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keys_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#keys_url AccessPolicy#keys_url}.'''
        result = self._values.get("keys_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyRequireExternalEvaluation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyRequireExternalEvaluationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireExternalEvaluationOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyRequireExternalEvaluationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEvaluateUrl")
    def reset_evaluate_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluateUrl", []))

    @jsii.member(jsii_name="resetKeysUrl")
    def reset_keys_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeysUrl", []))

    @builtins.property
    @jsii.member(jsii_name="evaluateUrlInput")
    def evaluate_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluateUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="keysUrlInput")
    def keys_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keysUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluateUrl")
    def evaluate_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "evaluateUrl"))

    @evaluate_url.setter
    def evaluate_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireExternalEvaluationOutputReference, "evaluate_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluateUrl", value)

    @builtins.property
    @jsii.member(jsii_name="keysUrl")
    def keys_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keysUrl"))

    @keys_url.setter
    def keys_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireExternalEvaluationOutputReference, "keys_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keysUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AccessPolicyRequireExternalEvaluation]:
        return typing.cast(typing.Optional[AccessPolicyRequireExternalEvaluation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AccessPolicyRequireExternalEvaluation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireExternalEvaluationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireGithub",
    jsii_struct_bases=[],
    name_mapping={
        "identity_provider_id": "identityProviderId",
        "name": "name",
        "teams": "teams",
    },
)
class AccessPolicyRequireGithub:
    def __init__(
        self,
        *,
        identity_provider_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        teams: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#name AccessPolicy#name}.
        :param teams: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#teams AccessPolicy#teams}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyRequireGithub.__init__)
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument teams", value=teams, expected_type=type_hints["teams"])
        self._values: typing.Dict[str, typing.Any] = {}
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id
        if name is not None:
            self._values["name"] = name
        if teams is not None:
            self._values["teams"] = teams

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#name AccessPolicy#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def teams(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#teams AccessPolicy#teams}.'''
        result = self._values.get("teams")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyRequireGithub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyRequireGithubList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireGithubList",
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
            type_hints = typing.get_type_hints(AccessPolicyRequireGithubList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyRequireGithubOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyRequireGithubList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyRequireGithubOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireGithubList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireGithubList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireGithubList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireGithub]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireGithub]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireGithub]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireGithubList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyRequireGithubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireGithubOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyRequireGithubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetTeams")
    def reset_teams(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeams", []))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="teamsInput")
    def teams_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "teamsInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireGithubOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireGithubOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="teams")
    def teams(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "teams"))

    @teams.setter
    def teams(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireGithubOutputReference, "teams").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teams", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyRequireGithub, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyRequireGithub, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyRequireGithub, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireGithubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireGsuite",
    jsii_struct_bases=[],
    name_mapping={"email": "email", "identity_provider_id": "identityProviderId"},
)
class AccessPolicyRequireGsuite:
    def __init__(
        self,
        *,
        email: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_provider_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email AccessPolicy#email}.
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyRequireGsuite.__init__)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if email is not None:
            self._values["email"] = email
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id

    @builtins.property
    def email(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#email AccessPolicy#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyRequireGsuite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyRequireGsuiteList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireGsuiteList",
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
            type_hints = typing.get_type_hints(AccessPolicyRequireGsuiteList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyRequireGsuiteOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyRequireGsuiteList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyRequireGsuiteOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireGsuiteList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireGsuiteList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireGsuiteList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireGsuite]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireGsuite]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireGsuite]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireGsuiteList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyRequireGsuiteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireGsuiteOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyRequireGsuiteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireGsuiteOutputReference, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireGsuiteOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyRequireGsuite, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyRequireGsuite, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyRequireGsuite, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireGsuiteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyRequireList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireList",
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
            type_hints = typing.get_type_hints(AccessPolicyRequireList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyRequireOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyRequireList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyRequireOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequire]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequire]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequire]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireOkta",
    jsii_struct_bases=[],
    name_mapping={"identity_provider_id": "identityProviderId", "name": "name"},
)
class AccessPolicyRequireOkta:
    def __init__(
        self,
        *,
        identity_provider_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#name AccessPolicy#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyRequireOkta.__init__)
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#name AccessPolicy#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyRequireOkta(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyRequireOktaList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireOktaList",
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
            type_hints = typing.get_type_hints(AccessPolicyRequireOktaList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyRequireOktaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyRequireOktaList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyRequireOktaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOktaList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOktaList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOktaList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireOkta]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireOkta]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireOkta]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOktaList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyRequireOktaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireOktaOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyRequireOktaOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOktaOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOktaOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyRequireOkta, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyRequireOkta, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyRequireOkta, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOktaOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyRequireOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyRequireOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAzure")
    def put_azure(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessPolicyRequireAzure, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyRequireOutputReference.put_azure)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAzure", [value]))

    @jsii.member(jsii_name="putExternalEvaluation")
    def put_external_evaluation(
        self,
        *,
        evaluate_url: typing.Optional[builtins.str] = None,
        keys_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param evaluate_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#evaluate_url AccessPolicy#evaluate_url}.
        :param keys_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#keys_url AccessPolicy#keys_url}.
        '''
        value = AccessPolicyRequireExternalEvaluation(
            evaluate_url=evaluate_url, keys_url=keys_url
        )

        return typing.cast(None, jsii.invoke(self, "putExternalEvaluation", [value]))

    @jsii.member(jsii_name="putGithub")
    def put_github(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessPolicyRequireGithub, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyRequireOutputReference.put_github)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGithub", [value]))

    @jsii.member(jsii_name="putGsuite")
    def put_gsuite(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessPolicyRequireGsuite, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyRequireOutputReference.put_gsuite)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGsuite", [value]))

    @jsii.member(jsii_name="putOkta")
    def put_okta(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessPolicyRequireOkta, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyRequireOutputReference.put_okta)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOkta", [value]))

    @jsii.member(jsii_name="putSaml")
    def put_saml(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessPolicyRequireSaml", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyRequireOutputReference.put_saml)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSaml", [value]))

    @jsii.member(jsii_name="resetAnyValidServiceToken")
    def reset_any_valid_service_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnyValidServiceToken", []))

    @jsii.member(jsii_name="resetAuthMethod")
    def reset_auth_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthMethod", []))

    @jsii.member(jsii_name="resetAzure")
    def reset_azure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzure", []))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetCommonName")
    def reset_common_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommonName", []))

    @jsii.member(jsii_name="resetDevicePosture")
    def reset_device_posture(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDevicePosture", []))

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetEmailDomain")
    def reset_email_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailDomain", []))

    @jsii.member(jsii_name="resetEveryone")
    def reset_everyone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEveryone", []))

    @jsii.member(jsii_name="resetExternalEvaluation")
    def reset_external_evaluation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalEvaluation", []))

    @jsii.member(jsii_name="resetGeo")
    def reset_geo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeo", []))

    @jsii.member(jsii_name="resetGithub")
    def reset_github(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithub", []))

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetGsuite")
    def reset_gsuite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGsuite", []))

    @jsii.member(jsii_name="resetIp")
    def reset_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIp", []))

    @jsii.member(jsii_name="resetLoginMethod")
    def reset_login_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginMethod", []))

    @jsii.member(jsii_name="resetOkta")
    def reset_okta(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOkta", []))

    @jsii.member(jsii_name="resetSaml")
    def reset_saml(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaml", []))

    @jsii.member(jsii_name="resetServiceToken")
    def reset_service_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceToken", []))

    @builtins.property
    @jsii.member(jsii_name="azure")
    def azure(self) -> AccessPolicyRequireAzureList:
        return typing.cast(AccessPolicyRequireAzureList, jsii.get(self, "azure"))

    @builtins.property
    @jsii.member(jsii_name="externalEvaluation")
    def external_evaluation(
        self,
    ) -> AccessPolicyRequireExternalEvaluationOutputReference:
        return typing.cast(AccessPolicyRequireExternalEvaluationOutputReference, jsii.get(self, "externalEvaluation"))

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> AccessPolicyRequireGithubList:
        return typing.cast(AccessPolicyRequireGithubList, jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="gsuite")
    def gsuite(self) -> AccessPolicyRequireGsuiteList:
        return typing.cast(AccessPolicyRequireGsuiteList, jsii.get(self, "gsuite"))

    @builtins.property
    @jsii.member(jsii_name="okta")
    def okta(self) -> AccessPolicyRequireOktaList:
        return typing.cast(AccessPolicyRequireOktaList, jsii.get(self, "okta"))

    @builtins.property
    @jsii.member(jsii_name="saml")
    def saml(self) -> "AccessPolicyRequireSamlList":
        return typing.cast("AccessPolicyRequireSamlList", jsii.get(self, "saml"))

    @builtins.property
    @jsii.member(jsii_name="anyValidServiceTokenInput")
    def any_valid_service_token_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "anyValidServiceTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="authMethodInput")
    def auth_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="azureInput")
    def azure_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireAzure]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireAzure]]], jsii.get(self, "azureInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="commonNameInput")
    def common_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commonNameInput"))

    @builtins.property
    @jsii.member(jsii_name="devicePostureInput")
    def device_posture_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "devicePostureInput"))

    @builtins.property
    @jsii.member(jsii_name="emailDomainInput")
    def email_domain_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="everyoneInput")
    def everyone_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "everyoneInput"))

    @builtins.property
    @jsii.member(jsii_name="externalEvaluationInput")
    def external_evaluation_input(
        self,
    ) -> typing.Optional[AccessPolicyRequireExternalEvaluation]:
        return typing.cast(typing.Optional[AccessPolicyRequireExternalEvaluation], jsii.get(self, "externalEvaluationInput"))

    @builtins.property
    @jsii.member(jsii_name="geoInput")
    def geo_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "geoInput"))

    @builtins.property
    @jsii.member(jsii_name="githubInput")
    def github_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireGithub]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireGithub]]], jsii.get(self, "githubInput"))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="gsuiteInput")
    def gsuite_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireGsuite]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireGsuite]]], jsii.get(self, "gsuiteInput"))

    @builtins.property
    @jsii.member(jsii_name="ipInput")
    def ip_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipInput"))

    @builtins.property
    @jsii.member(jsii_name="loginMethodInput")
    def login_method_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loginMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="oktaInput")
    def okta_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireOkta]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireOkta]]], jsii.get(self, "oktaInput"))

    @builtins.property
    @jsii.member(jsii_name="samlInput")
    def saml_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyRequireSaml"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessPolicyRequireSaml"]]], jsii.get(self, "samlInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceTokenInput")
    def service_token_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serviceTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="anyValidServiceToken")
    def any_valid_service_token(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "anyValidServiceToken"))

    @any_valid_service_token.setter
    def any_valid_service_token(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOutputReference, "any_valid_service_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anyValidServiceToken", value)

    @builtins.property
    @jsii.member(jsii_name="authMethod")
    def auth_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authMethod"))

    @auth_method.setter
    def auth_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOutputReference, "auth_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authMethod", value)

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOutputReference, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="commonName")
    def common_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commonName"))

    @common_name.setter
    def common_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOutputReference, "common_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commonName", value)

    @builtins.property
    @jsii.member(jsii_name="devicePosture")
    def device_posture(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "devicePosture"))

    @device_posture.setter
    def device_posture(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOutputReference, "device_posture").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "devicePosture", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOutputReference, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="emailDomain")
    def email_domain(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "emailDomain"))

    @email_domain.setter
    def email_domain(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOutputReference, "email_domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailDomain", value)

    @builtins.property
    @jsii.member(jsii_name="everyone")
    def everyone(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "everyone"))

    @everyone.setter
    def everyone(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOutputReference, "everyone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "everyone", value)

    @builtins.property
    @jsii.member(jsii_name="geo")
    def geo(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "geo"))

    @geo.setter
    def geo(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOutputReference, "geo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geo", value)

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "group"))

    @group.setter
    def group(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOutputReference, "group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="ip")
    def ip(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ip"))

    @ip.setter
    def ip(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOutputReference, "ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ip", value)

    @builtins.property
    @jsii.member(jsii_name="loginMethod")
    def login_method(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loginMethod"))

    @login_method.setter
    def login_method(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOutputReference, "login_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginMethod", value)

    @builtins.property
    @jsii.member(jsii_name="serviceToken")
    def service_token(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "serviceToken"))

    @service_token.setter
    def service_token(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOutputReference, "service_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyRequire, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyRequire, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyRequire, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireSaml",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_name": "attributeName",
        "attribute_value": "attributeValue",
        "identity_provider_id": "identityProviderId",
    },
)
class AccessPolicyRequireSaml:
    def __init__(
        self,
        *,
        attribute_name: typing.Optional[builtins.str] = None,
        attribute_value: typing.Optional[builtins.str] = None,
        identity_provider_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param attribute_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#attribute_name AccessPolicy#attribute_name}.
        :param attribute_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#attribute_value AccessPolicy#attribute_value}.
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyRequireSaml.__init__)
            check_type(argname="argument attribute_name", value=attribute_name, expected_type=type_hints["attribute_name"])
            check_type(argname="argument attribute_value", value=attribute_value, expected_type=type_hints["attribute_value"])
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if attribute_name is not None:
            self._values["attribute_name"] = attribute_name
        if attribute_value is not None:
            self._values["attribute_value"] = attribute_value
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id

    @builtins.property
    def attribute_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#attribute_name AccessPolicy#attribute_name}.'''
        result = self._values.get("attribute_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attribute_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#attribute_value AccessPolicy#attribute_value}.'''
        result = self._values.get("attribute_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_policy#identity_provider_id AccessPolicy#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyRequireSaml(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessPolicyRequireSamlList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireSamlList",
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
            type_hints = typing.get_type_hints(AccessPolicyRequireSamlList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessPolicyRequireSamlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessPolicyRequireSamlList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessPolicyRequireSamlOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireSamlList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireSamlList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireSamlList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireSaml]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireSaml]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessPolicyRequireSaml]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireSamlList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessPolicyRequireSamlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessPolicy.AccessPolicyRequireSamlOutputReference",
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
            type_hints = typing.get_type_hints(AccessPolicyRequireSamlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAttributeName")
    def reset_attribute_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeName", []))

    @jsii.member(jsii_name="resetAttributeValue")
    def reset_attribute_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeValue", []))

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @builtins.property
    @jsii.member(jsii_name="attributeNameInput")
    def attribute_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeValueInput")
    def attribute_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeValueInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeName")
    def attribute_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeName"))

    @attribute_name.setter
    def attribute_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireSamlOutputReference, "attribute_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeName", value)

    @builtins.property
    @jsii.member(jsii_name="attributeValue")
    def attribute_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeValue"))

    @attribute_value.setter
    def attribute_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireSamlOutputReference, "attribute_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeValue", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireSamlOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessPolicyRequireSaml, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessPolicyRequireSaml, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessPolicyRequireSaml, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessPolicyRequireSamlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AccessPolicy",
    "AccessPolicyApprovalGroup",
    "AccessPolicyApprovalGroupList",
    "AccessPolicyApprovalGroupOutputReference",
    "AccessPolicyConfig",
    "AccessPolicyExclude",
    "AccessPolicyExcludeAzure",
    "AccessPolicyExcludeAzureList",
    "AccessPolicyExcludeAzureOutputReference",
    "AccessPolicyExcludeExternalEvaluation",
    "AccessPolicyExcludeExternalEvaluationOutputReference",
    "AccessPolicyExcludeGithub",
    "AccessPolicyExcludeGithubList",
    "AccessPolicyExcludeGithubOutputReference",
    "AccessPolicyExcludeGsuite",
    "AccessPolicyExcludeGsuiteList",
    "AccessPolicyExcludeGsuiteOutputReference",
    "AccessPolicyExcludeList",
    "AccessPolicyExcludeOkta",
    "AccessPolicyExcludeOktaList",
    "AccessPolicyExcludeOktaOutputReference",
    "AccessPolicyExcludeOutputReference",
    "AccessPolicyExcludeSaml",
    "AccessPolicyExcludeSamlList",
    "AccessPolicyExcludeSamlOutputReference",
    "AccessPolicyInclude",
    "AccessPolicyIncludeAzure",
    "AccessPolicyIncludeAzureList",
    "AccessPolicyIncludeAzureOutputReference",
    "AccessPolicyIncludeExternalEvaluation",
    "AccessPolicyIncludeExternalEvaluationOutputReference",
    "AccessPolicyIncludeGithub",
    "AccessPolicyIncludeGithubList",
    "AccessPolicyIncludeGithubOutputReference",
    "AccessPolicyIncludeGsuite",
    "AccessPolicyIncludeGsuiteList",
    "AccessPolicyIncludeGsuiteOutputReference",
    "AccessPolicyIncludeList",
    "AccessPolicyIncludeOkta",
    "AccessPolicyIncludeOktaList",
    "AccessPolicyIncludeOktaOutputReference",
    "AccessPolicyIncludeOutputReference",
    "AccessPolicyIncludeSaml",
    "AccessPolicyIncludeSamlList",
    "AccessPolicyIncludeSamlOutputReference",
    "AccessPolicyRequire",
    "AccessPolicyRequireAzure",
    "AccessPolicyRequireAzureList",
    "AccessPolicyRequireAzureOutputReference",
    "AccessPolicyRequireExternalEvaluation",
    "AccessPolicyRequireExternalEvaluationOutputReference",
    "AccessPolicyRequireGithub",
    "AccessPolicyRequireGithubList",
    "AccessPolicyRequireGithubOutputReference",
    "AccessPolicyRequireGsuite",
    "AccessPolicyRequireGsuiteList",
    "AccessPolicyRequireGsuiteOutputReference",
    "AccessPolicyRequireList",
    "AccessPolicyRequireOkta",
    "AccessPolicyRequireOktaList",
    "AccessPolicyRequireOktaOutputReference",
    "AccessPolicyRequireOutputReference",
    "AccessPolicyRequireSaml",
    "AccessPolicyRequireSamlList",
    "AccessPolicyRequireSamlOutputReference",
]

publication.publish()
