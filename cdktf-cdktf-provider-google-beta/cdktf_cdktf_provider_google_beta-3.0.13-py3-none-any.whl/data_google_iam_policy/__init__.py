'''
# `data_google_iam_policy`

Refer to the Terraform Registory for docs: [`data_google_iam_policy`](https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy).
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


class DataGoogleIamPolicy(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleIamPolicy.DataGoogleIamPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy google_iam_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        audit_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataGoogleIamPolicyAuditConfig", typing.Dict[str, typing.Any]]]]] = None,
        binding: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataGoogleIamPolicyBinding", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy google_iam_policy} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param audit_config: audit_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#audit_config DataGoogleIamPolicy#audit_config}
        :param binding: binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#binding DataGoogleIamPolicy#binding}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#id DataGoogleIamPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleIamPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataGoogleIamPolicyConfig(
            audit_config=audit_config,
            binding=binding,
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

    @jsii.member(jsii_name="putAuditConfig")
    def put_audit_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataGoogleIamPolicyAuditConfig", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleIamPolicy.put_audit_config)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAuditConfig", [value]))

    @jsii.member(jsii_name="putBinding")
    def put_binding(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataGoogleIamPolicyBinding", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleIamPolicy.put_binding)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBinding", [value]))

    @jsii.member(jsii_name="resetAuditConfig")
    def reset_audit_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditConfig", []))

    @jsii.member(jsii_name="resetBinding")
    def reset_binding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBinding", []))

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
    @jsii.member(jsii_name="auditConfig")
    def audit_config(self) -> "DataGoogleIamPolicyAuditConfigList":
        return typing.cast("DataGoogleIamPolicyAuditConfigList", jsii.get(self, "auditConfig"))

    @builtins.property
    @jsii.member(jsii_name="binding")
    def binding(self) -> "DataGoogleIamPolicyBindingList":
        return typing.cast("DataGoogleIamPolicyBindingList", jsii.get(self, "binding"))

    @builtins.property
    @jsii.member(jsii_name="policyData")
    def policy_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyData"))

    @builtins.property
    @jsii.member(jsii_name="auditConfigInput")
    def audit_config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataGoogleIamPolicyAuditConfig"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataGoogleIamPolicyAuditConfig"]]], jsii.get(self, "auditConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="bindingInput")
    def binding_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataGoogleIamPolicyBinding"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataGoogleIamPolicyBinding"]]], jsii.get(self, "bindingInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleIamPolicy.DataGoogleIamPolicyAuditConfig",
    jsii_struct_bases=[],
    name_mapping={"audit_log_configs": "auditLogConfigs", "service": "service"},
)
class DataGoogleIamPolicyAuditConfig:
    def __init__(
        self,
        *,
        audit_log_configs: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataGoogleIamPolicyAuditConfigAuditLogConfigs", typing.Dict[str, typing.Any]]]],
        service: builtins.str,
    ) -> None:
        '''
        :param audit_log_configs: audit_log_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#audit_log_configs DataGoogleIamPolicy#audit_log_configs}
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#service DataGoogleIamPolicy#service}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleIamPolicyAuditConfig.__init__)
            check_type(argname="argument audit_log_configs", value=audit_log_configs, expected_type=type_hints["audit_log_configs"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        self._values: typing.Dict[str, typing.Any] = {
            "audit_log_configs": audit_log_configs,
            "service": service,
        }

    @builtins.property
    def audit_log_configs(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["DataGoogleIamPolicyAuditConfigAuditLogConfigs"]]:
        '''audit_log_configs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#audit_log_configs DataGoogleIamPolicy#audit_log_configs}
        '''
        result = self._values.get("audit_log_configs")
        assert result is not None, "Required property 'audit_log_configs' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["DataGoogleIamPolicyAuditConfigAuditLogConfigs"]], result)

    @builtins.property
    def service(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#service DataGoogleIamPolicy#service}.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleIamPolicyAuditConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleIamPolicy.DataGoogleIamPolicyAuditConfigAuditLogConfigs",
    jsii_struct_bases=[],
    name_mapping={"log_type": "logType", "exempted_members": "exemptedMembers"},
)
class DataGoogleIamPolicyAuditConfigAuditLogConfigs:
    def __init__(
        self,
        *,
        log_type: builtins.str,
        exempted_members: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param log_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#log_type DataGoogleIamPolicy#log_type}.
        :param exempted_members: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#exempted_members DataGoogleIamPolicy#exempted_members}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleIamPolicyAuditConfigAuditLogConfigs.__init__)
            check_type(argname="argument log_type", value=log_type, expected_type=type_hints["log_type"])
            check_type(argname="argument exempted_members", value=exempted_members, expected_type=type_hints["exempted_members"])
        self._values: typing.Dict[str, typing.Any] = {
            "log_type": log_type,
        }
        if exempted_members is not None:
            self._values["exempted_members"] = exempted_members

    @builtins.property
    def log_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#log_type DataGoogleIamPolicy#log_type}.'''
        result = self._values.get("log_type")
        assert result is not None, "Required property 'log_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exempted_members(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#exempted_members DataGoogleIamPolicy#exempted_members}.'''
        result = self._values.get("exempted_members")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleIamPolicyAuditConfigAuditLogConfigs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGoogleIamPolicyAuditConfigAuditLogConfigsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleIamPolicy.DataGoogleIamPolicyAuditConfigAuditLogConfigsList",
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
            type_hints = typing.get_type_hints(DataGoogleIamPolicyAuditConfigAuditLogConfigsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleIamPolicyAuditConfigAuditLogConfigsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleIamPolicyAuditConfigAuditLogConfigsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleIamPolicyAuditConfigAuditLogConfigsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyAuditConfigAuditLogConfigsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyAuditConfigAuditLogConfigsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyAuditConfigAuditLogConfigsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataGoogleIamPolicyAuditConfigAuditLogConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataGoogleIamPolicyAuditConfigAuditLogConfigs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataGoogleIamPolicyAuditConfigAuditLogConfigs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyAuditConfigAuditLogConfigsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataGoogleIamPolicyAuditConfigAuditLogConfigsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleIamPolicy.DataGoogleIamPolicyAuditConfigAuditLogConfigsOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleIamPolicyAuditConfigAuditLogConfigsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExemptedMembers")
    def reset_exempted_members(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExemptedMembers", []))

    @builtins.property
    @jsii.member(jsii_name="exemptedMembersInput")
    def exempted_members_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exemptedMembersInput"))

    @builtins.property
    @jsii.member(jsii_name="logTypeInput")
    def log_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="exemptedMembers")
    def exempted_members(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exemptedMembers"))

    @exempted_members.setter
    def exempted_members(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyAuditConfigAuditLogConfigsOutputReference, "exempted_members").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exemptedMembers", value)

    @builtins.property
    @jsii.member(jsii_name="logType")
    def log_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logType"))

    @log_type.setter
    def log_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyAuditConfigAuditLogConfigsOutputReference, "log_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataGoogleIamPolicyAuditConfigAuditLogConfigs, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataGoogleIamPolicyAuditConfigAuditLogConfigs, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataGoogleIamPolicyAuditConfigAuditLogConfigs, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyAuditConfigAuditLogConfigsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataGoogleIamPolicyAuditConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleIamPolicy.DataGoogleIamPolicyAuditConfigList",
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
            type_hints = typing.get_type_hints(DataGoogleIamPolicyAuditConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleIamPolicyAuditConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleIamPolicyAuditConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleIamPolicyAuditConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyAuditConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyAuditConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyAuditConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataGoogleIamPolicyAuditConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataGoogleIamPolicyAuditConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataGoogleIamPolicyAuditConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyAuditConfigList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataGoogleIamPolicyAuditConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleIamPolicy.DataGoogleIamPolicyAuditConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleIamPolicyAuditConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAuditLogConfigs")
    def put_audit_log_configs(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataGoogleIamPolicyAuditConfigAuditLogConfigs, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleIamPolicyAuditConfigOutputReference.put_audit_log_configs)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAuditLogConfigs", [value]))

    @builtins.property
    @jsii.member(jsii_name="auditLogConfigs")
    def audit_log_configs(self) -> DataGoogleIamPolicyAuditConfigAuditLogConfigsList:
        return typing.cast(DataGoogleIamPolicyAuditConfigAuditLogConfigsList, jsii.get(self, "auditLogConfigs"))

    @builtins.property
    @jsii.member(jsii_name="auditLogConfigsInput")
    def audit_log_configs_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataGoogleIamPolicyAuditConfigAuditLogConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataGoogleIamPolicyAuditConfigAuditLogConfigs]]], jsii.get(self, "auditLogConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyAuditConfigOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataGoogleIamPolicyAuditConfig, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataGoogleIamPolicyAuditConfig, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataGoogleIamPolicyAuditConfig, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyAuditConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleIamPolicy.DataGoogleIamPolicyBinding",
    jsii_struct_bases=[],
    name_mapping={"members": "members", "role": "role", "condition": "condition"},
)
class DataGoogleIamPolicyBinding:
    def __init__(
        self,
        *,
        members: typing.Sequence[builtins.str],
        role: builtins.str,
        condition: typing.Optional[typing.Union["DataGoogleIamPolicyBindingCondition", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param members: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#members DataGoogleIamPolicy#members}.
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#role DataGoogleIamPolicy#role}.
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#condition DataGoogleIamPolicy#condition}
        '''
        if isinstance(condition, dict):
            condition = DataGoogleIamPolicyBindingCondition(**condition)
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleIamPolicyBinding.__init__)
            check_type(argname="argument members", value=members, expected_type=type_hints["members"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
        self._values: typing.Dict[str, typing.Any] = {
            "members": members,
            "role": role,
        }
        if condition is not None:
            self._values["condition"] = condition

    @builtins.property
    def members(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#members DataGoogleIamPolicy#members}.'''
        result = self._values.get("members")
        assert result is not None, "Required property 'members' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#role DataGoogleIamPolicy#role}.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition(self) -> typing.Optional["DataGoogleIamPolicyBindingCondition"]:
        '''condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#condition DataGoogleIamPolicy#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional["DataGoogleIamPolicyBindingCondition"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleIamPolicyBinding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleIamPolicy.DataGoogleIamPolicyBindingCondition",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "title": "title",
        "description": "description",
    },
)
class DataGoogleIamPolicyBindingCondition:
    def __init__(
        self,
        *,
        expression: builtins.str,
        title: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#expression DataGoogleIamPolicy#expression}.
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#title DataGoogleIamPolicy#title}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#description DataGoogleIamPolicy#description}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleIamPolicyBindingCondition.__init__)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[str, typing.Any] = {
            "expression": expression,
            "title": title,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def expression(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#expression DataGoogleIamPolicy#expression}.'''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#title DataGoogleIamPolicy#title}.'''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#description DataGoogleIamPolicy#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleIamPolicyBindingCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGoogleIamPolicyBindingConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleIamPolicy.DataGoogleIamPolicyBindingConditionOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleIamPolicyBindingConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

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
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyBindingConditionOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyBindingConditionOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyBindingConditionOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataGoogleIamPolicyBindingCondition]:
        return typing.cast(typing.Optional[DataGoogleIamPolicyBindingCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGoogleIamPolicyBindingCondition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyBindingConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataGoogleIamPolicyBindingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleIamPolicy.DataGoogleIamPolicyBindingList",
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
            type_hints = typing.get_type_hints(DataGoogleIamPolicyBindingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataGoogleIamPolicyBindingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleIamPolicyBindingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleIamPolicyBindingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyBindingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyBindingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyBindingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataGoogleIamPolicyBinding]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataGoogleIamPolicyBinding]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataGoogleIamPolicyBinding]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyBindingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataGoogleIamPolicyBindingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleIamPolicy.DataGoogleIamPolicyBindingOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleIamPolicyBindingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        *,
        expression: builtins.str,
        title: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#expression DataGoogleIamPolicy#expression}.
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#title DataGoogleIamPolicy#title}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#description DataGoogleIamPolicy#description}.
        '''
        value = DataGoogleIamPolicyBindingCondition(
            expression=expression, title=title, description=description
        )

        return typing.cast(None, jsii.invoke(self, "putCondition", [value]))

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> DataGoogleIamPolicyBindingConditionOutputReference:
        return typing.cast(DataGoogleIamPolicyBindingConditionOutputReference, jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(self) -> typing.Optional[DataGoogleIamPolicyBindingCondition]:
        return typing.cast(typing.Optional[DataGoogleIamPolicyBindingCondition], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="membersInput")
    def members_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "membersInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="members")
    def members(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "members"))

    @members.setter
    def members(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyBindingOutputReference, "members").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "members", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyBindingOutputReference, "role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataGoogleIamPolicyBinding, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataGoogleIamPolicyBinding, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataGoogleIamPolicyBinding, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamPolicyBindingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleIamPolicy.DataGoogleIamPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "audit_config": "auditConfig",
        "binding": "binding",
        "id": "id",
    },
)
class DataGoogleIamPolicyConfig(cdktf.TerraformMetaArguments):
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
        audit_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataGoogleIamPolicyAuditConfig, typing.Dict[str, typing.Any]]]]] = None,
        binding: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataGoogleIamPolicyBinding, typing.Dict[str, typing.Any]]]]] = None,
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
        :param audit_config: audit_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#audit_config DataGoogleIamPolicy#audit_config}
        :param binding: binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#binding DataGoogleIamPolicy#binding}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#id DataGoogleIamPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleIamPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument audit_config", value=audit_config, expected_type=type_hints["audit_config"])
            check_type(argname="argument binding", value=binding, expected_type=type_hints["binding"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {}
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
        if audit_config is not None:
            self._values["audit_config"] = audit_config
        if binding is not None:
            self._values["binding"] = binding
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
    def audit_config(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataGoogleIamPolicyAuditConfig]]]:
        '''audit_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#audit_config DataGoogleIamPolicy#audit_config}
        '''
        result = self._values.get("audit_config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataGoogleIamPolicyAuditConfig]]], result)

    @builtins.property
    def binding(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataGoogleIamPolicyBinding]]]:
        '''binding block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#binding DataGoogleIamPolicy#binding}
        '''
        result = self._values.get("binding")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataGoogleIamPolicyBinding]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_policy#id DataGoogleIamPolicy#id}.

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
        return "DataGoogleIamPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataGoogleIamPolicy",
    "DataGoogleIamPolicyAuditConfig",
    "DataGoogleIamPolicyAuditConfigAuditLogConfigs",
    "DataGoogleIamPolicyAuditConfigAuditLogConfigsList",
    "DataGoogleIamPolicyAuditConfigAuditLogConfigsOutputReference",
    "DataGoogleIamPolicyAuditConfigList",
    "DataGoogleIamPolicyAuditConfigOutputReference",
    "DataGoogleIamPolicyBinding",
    "DataGoogleIamPolicyBindingCondition",
    "DataGoogleIamPolicyBindingConditionOutputReference",
    "DataGoogleIamPolicyBindingList",
    "DataGoogleIamPolicyBindingOutputReference",
    "DataGoogleIamPolicyConfig",
]

publication.publish()
