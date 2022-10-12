'''
# `google_project_organization_policy`

Refer to the Terraform Registory for docs: [`google_project_organization_policy`](https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy).
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


class GoogleProjectOrganizationPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleProjectOrganizationPolicy.GoogleProjectOrganizationPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy google_project_organization_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        constraint: builtins.str,
        project: builtins.str,
        boolean_policy: typing.Optional[typing.Union["GoogleProjectOrganizationPolicyBooleanPolicy", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        list_policy: typing.Optional[typing.Union["GoogleProjectOrganizationPolicyListPolicy", typing.Dict[str, typing.Any]]] = None,
        restore_policy: typing.Optional[typing.Union["GoogleProjectOrganizationPolicyRestorePolicy", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleProjectOrganizationPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy google_project_organization_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param constraint: The name of the Constraint the Policy is configuring, for example, serviceuser.services. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#constraint GoogleProjectOrganizationPolicy#constraint}
        :param project: The project ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#project GoogleProjectOrganizationPolicy#project}
        :param boolean_policy: boolean_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#boolean_policy GoogleProjectOrganizationPolicy#boolean_policy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#id GoogleProjectOrganizationPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param list_policy: list_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#list_policy GoogleProjectOrganizationPolicy#list_policy}
        :param restore_policy: restore_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#restore_policy GoogleProjectOrganizationPolicy#restore_policy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#timeouts GoogleProjectOrganizationPolicy#timeouts}
        :param version: Version of the Policy. Default version is 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#version GoogleProjectOrganizationPolicy#version}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleProjectOrganizationPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleProjectOrganizationPolicyConfig(
            constraint=constraint,
            project=project,
            boolean_policy=boolean_policy,
            id=id,
            list_policy=list_policy,
            restore_policy=restore_policy,
            timeouts=timeouts,
            version=version,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBooleanPolicy")
    def put_boolean_policy(
        self,
        *,
        enforced: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enforced: If true, then the Policy is enforced. If false, then any configuration is acceptable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#enforced GoogleProjectOrganizationPolicy#enforced}
        '''
        value = GoogleProjectOrganizationPolicyBooleanPolicy(enforced=enforced)

        return typing.cast(None, jsii.invoke(self, "putBooleanPolicy", [value]))

    @jsii.member(jsii_name="putListPolicy")
    def put_list_policy(
        self,
        *,
        allow: typing.Optional[typing.Union["GoogleProjectOrganizationPolicyListPolicyAllow", typing.Dict[str, typing.Any]]] = None,
        deny: typing.Optional[typing.Union["GoogleProjectOrganizationPolicyListPolicyDeny", typing.Dict[str, typing.Any]]] = None,
        inherit_from_parent: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        suggested_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow: allow block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#allow GoogleProjectOrganizationPolicy#allow}
        :param deny: deny block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#deny GoogleProjectOrganizationPolicy#deny}
        :param inherit_from_parent: If set to true, the values from the effective Policy of the parent resource are inherited, meaning the values set in this Policy are added to the values inherited up the hierarchy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#inherit_from_parent GoogleProjectOrganizationPolicy#inherit_from_parent}
        :param suggested_value: The Google Cloud Console will try to default to a configuration that matches the value specified in this field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#suggested_value GoogleProjectOrganizationPolicy#suggested_value}
        '''
        value = GoogleProjectOrganizationPolicyListPolicy(
            allow=allow,
            deny=deny,
            inherit_from_parent=inherit_from_parent,
            suggested_value=suggested_value,
        )

        return typing.cast(None, jsii.invoke(self, "putListPolicy", [value]))

    @jsii.member(jsii_name="putRestorePolicy")
    def put_restore_policy(
        self,
        *,
        default: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param default: May only be set to true. If set, then the default Policy is restored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#default GoogleProjectOrganizationPolicy#default}
        '''
        value = GoogleProjectOrganizationPolicyRestorePolicy(default=default)

        return typing.cast(None, jsii.invoke(self, "putRestorePolicy", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#create GoogleProjectOrganizationPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#delete GoogleProjectOrganizationPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#read GoogleProjectOrganizationPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#update GoogleProjectOrganizationPolicy#update}.
        '''
        value = GoogleProjectOrganizationPolicyTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetBooleanPolicy")
    def reset_boolean_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBooleanPolicy", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetListPolicy")
    def reset_list_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetListPolicy", []))

    @jsii.member(jsii_name="resetRestorePolicy")
    def reset_restore_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestorePolicy", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="booleanPolicy")
    def boolean_policy(
        self,
    ) -> "GoogleProjectOrganizationPolicyBooleanPolicyOutputReference":
        return typing.cast("GoogleProjectOrganizationPolicyBooleanPolicyOutputReference", jsii.get(self, "booleanPolicy"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="listPolicy")
    def list_policy(self) -> "GoogleProjectOrganizationPolicyListPolicyOutputReference":
        return typing.cast("GoogleProjectOrganizationPolicyListPolicyOutputReference", jsii.get(self, "listPolicy"))

    @builtins.property
    @jsii.member(jsii_name="restorePolicy")
    def restore_policy(
        self,
    ) -> "GoogleProjectOrganizationPolicyRestorePolicyOutputReference":
        return typing.cast("GoogleProjectOrganizationPolicyRestorePolicyOutputReference", jsii.get(self, "restorePolicy"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleProjectOrganizationPolicyTimeoutsOutputReference":
        return typing.cast("GoogleProjectOrganizationPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="booleanPolicyInput")
    def boolean_policy_input(
        self,
    ) -> typing.Optional["GoogleProjectOrganizationPolicyBooleanPolicy"]:
        return typing.cast(typing.Optional["GoogleProjectOrganizationPolicyBooleanPolicy"], jsii.get(self, "booleanPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="constraintInput")
    def constraint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "constraintInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="listPolicyInput")
    def list_policy_input(
        self,
    ) -> typing.Optional["GoogleProjectOrganizationPolicyListPolicy"]:
        return typing.cast(typing.Optional["GoogleProjectOrganizationPolicyListPolicy"], jsii.get(self, "listPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="restorePolicyInput")
    def restore_policy_input(
        self,
    ) -> typing.Optional["GoogleProjectOrganizationPolicyRestorePolicy"]:
        return typing.cast(typing.Optional["GoogleProjectOrganizationPolicyRestorePolicy"], jsii.get(self, "restorePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleProjectOrganizationPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleProjectOrganizationPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="constraint")
    def constraint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "constraint"))

    @constraint.setter
    def constraint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicy, "constraint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "constraint", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicy, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @version.setter
    def version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicy, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleProjectOrganizationPolicy.GoogleProjectOrganizationPolicyBooleanPolicy",
    jsii_struct_bases=[],
    name_mapping={"enforced": "enforced"},
)
class GoogleProjectOrganizationPolicyBooleanPolicy:
    def __init__(
        self,
        *,
        enforced: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enforced: If true, then the Policy is enforced. If false, then any configuration is acceptable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#enforced GoogleProjectOrganizationPolicy#enforced}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleProjectOrganizationPolicyBooleanPolicy.__init__)
            check_type(argname="argument enforced", value=enforced, expected_type=type_hints["enforced"])
        self._values: typing.Dict[str, typing.Any] = {
            "enforced": enforced,
        }

    @builtins.property
    def enforced(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If true, then the Policy is enforced. If false, then any configuration is acceptable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#enforced GoogleProjectOrganizationPolicy#enforced}
        '''
        result = self._values.get("enforced")
        assert result is not None, "Required property 'enforced' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleProjectOrganizationPolicyBooleanPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleProjectOrganizationPolicyBooleanPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleProjectOrganizationPolicy.GoogleProjectOrganizationPolicyBooleanPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleProjectOrganizationPolicyBooleanPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="enforcedInput")
    def enforced_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enforcedInput"))

    @builtins.property
    @jsii.member(jsii_name="enforced")
    def enforced(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enforced"))

    @enforced.setter
    def enforced(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicyBooleanPolicyOutputReference, "enforced").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforced", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleProjectOrganizationPolicyBooleanPolicy]:
        return typing.cast(typing.Optional[GoogleProjectOrganizationPolicyBooleanPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleProjectOrganizationPolicyBooleanPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicyBooleanPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleProjectOrganizationPolicy.GoogleProjectOrganizationPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "constraint": "constraint",
        "project": "project",
        "boolean_policy": "booleanPolicy",
        "id": "id",
        "list_policy": "listPolicy",
        "restore_policy": "restorePolicy",
        "timeouts": "timeouts",
        "version": "version",
    },
)
class GoogleProjectOrganizationPolicyConfig(cdktf.TerraformMetaArguments):
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
        constraint: builtins.str,
        project: builtins.str,
        boolean_policy: typing.Optional[typing.Union[GoogleProjectOrganizationPolicyBooleanPolicy, typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        list_policy: typing.Optional[typing.Union["GoogleProjectOrganizationPolicyListPolicy", typing.Dict[str, typing.Any]]] = None,
        restore_policy: typing.Optional[typing.Union["GoogleProjectOrganizationPolicyRestorePolicy", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleProjectOrganizationPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param constraint: The name of the Constraint the Policy is configuring, for example, serviceuser.services. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#constraint GoogleProjectOrganizationPolicy#constraint}
        :param project: The project ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#project GoogleProjectOrganizationPolicy#project}
        :param boolean_policy: boolean_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#boolean_policy GoogleProjectOrganizationPolicy#boolean_policy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#id GoogleProjectOrganizationPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param list_policy: list_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#list_policy GoogleProjectOrganizationPolicy#list_policy}
        :param restore_policy: restore_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#restore_policy GoogleProjectOrganizationPolicy#restore_policy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#timeouts GoogleProjectOrganizationPolicy#timeouts}
        :param version: Version of the Policy. Default version is 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#version GoogleProjectOrganizationPolicy#version}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(boolean_policy, dict):
            boolean_policy = GoogleProjectOrganizationPolicyBooleanPolicy(**boolean_policy)
        if isinstance(list_policy, dict):
            list_policy = GoogleProjectOrganizationPolicyListPolicy(**list_policy)
        if isinstance(restore_policy, dict):
            restore_policy = GoogleProjectOrganizationPolicyRestorePolicy(**restore_policy)
        if isinstance(timeouts, dict):
            timeouts = GoogleProjectOrganizationPolicyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleProjectOrganizationPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument constraint", value=constraint, expected_type=type_hints["constraint"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument boolean_policy", value=boolean_policy, expected_type=type_hints["boolean_policy"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument list_policy", value=list_policy, expected_type=type_hints["list_policy"])
            check_type(argname="argument restore_policy", value=restore_policy, expected_type=type_hints["restore_policy"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {
            "constraint": constraint,
            "project": project,
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
        if boolean_policy is not None:
            self._values["boolean_policy"] = boolean_policy
        if id is not None:
            self._values["id"] = id
        if list_policy is not None:
            self._values["list_policy"] = list_policy
        if restore_policy is not None:
            self._values["restore_policy"] = restore_policy
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if version is not None:
            self._values["version"] = version

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
    def constraint(self) -> builtins.str:
        '''The name of the Constraint the Policy is configuring, for example, serviceuser.services.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#constraint GoogleProjectOrganizationPolicy#constraint}
        '''
        result = self._values.get("constraint")
        assert result is not None, "Required property 'constraint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project(self) -> builtins.str:
        '''The project ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#project GoogleProjectOrganizationPolicy#project}
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def boolean_policy(
        self,
    ) -> typing.Optional[GoogleProjectOrganizationPolicyBooleanPolicy]:
        '''boolean_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#boolean_policy GoogleProjectOrganizationPolicy#boolean_policy}
        '''
        result = self._values.get("boolean_policy")
        return typing.cast(typing.Optional[GoogleProjectOrganizationPolicyBooleanPolicy], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#id GoogleProjectOrganizationPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def list_policy(
        self,
    ) -> typing.Optional["GoogleProjectOrganizationPolicyListPolicy"]:
        '''list_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#list_policy GoogleProjectOrganizationPolicy#list_policy}
        '''
        result = self._values.get("list_policy")
        return typing.cast(typing.Optional["GoogleProjectOrganizationPolicyListPolicy"], result)

    @builtins.property
    def restore_policy(
        self,
    ) -> typing.Optional["GoogleProjectOrganizationPolicyRestorePolicy"]:
        '''restore_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#restore_policy GoogleProjectOrganizationPolicy#restore_policy}
        '''
        result = self._values.get("restore_policy")
        return typing.cast(typing.Optional["GoogleProjectOrganizationPolicyRestorePolicy"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleProjectOrganizationPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#timeouts GoogleProjectOrganizationPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleProjectOrganizationPolicyTimeouts"], result)

    @builtins.property
    def version(self) -> typing.Optional[jsii.Number]:
        '''Version of the Policy. Default version is 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#version GoogleProjectOrganizationPolicy#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleProjectOrganizationPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleProjectOrganizationPolicy.GoogleProjectOrganizationPolicyListPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "allow": "allow",
        "deny": "deny",
        "inherit_from_parent": "inheritFromParent",
        "suggested_value": "suggestedValue",
    },
)
class GoogleProjectOrganizationPolicyListPolicy:
    def __init__(
        self,
        *,
        allow: typing.Optional[typing.Union["GoogleProjectOrganizationPolicyListPolicyAllow", typing.Dict[str, typing.Any]]] = None,
        deny: typing.Optional[typing.Union["GoogleProjectOrganizationPolicyListPolicyDeny", typing.Dict[str, typing.Any]]] = None,
        inherit_from_parent: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        suggested_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow: allow block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#allow GoogleProjectOrganizationPolicy#allow}
        :param deny: deny block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#deny GoogleProjectOrganizationPolicy#deny}
        :param inherit_from_parent: If set to true, the values from the effective Policy of the parent resource are inherited, meaning the values set in this Policy are added to the values inherited up the hierarchy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#inherit_from_parent GoogleProjectOrganizationPolicy#inherit_from_parent}
        :param suggested_value: The Google Cloud Console will try to default to a configuration that matches the value specified in this field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#suggested_value GoogleProjectOrganizationPolicy#suggested_value}
        '''
        if isinstance(allow, dict):
            allow = GoogleProjectOrganizationPolicyListPolicyAllow(**allow)
        if isinstance(deny, dict):
            deny = GoogleProjectOrganizationPolicyListPolicyDeny(**deny)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleProjectOrganizationPolicyListPolicy.__init__)
            check_type(argname="argument allow", value=allow, expected_type=type_hints["allow"])
            check_type(argname="argument deny", value=deny, expected_type=type_hints["deny"])
            check_type(argname="argument inherit_from_parent", value=inherit_from_parent, expected_type=type_hints["inherit_from_parent"])
            check_type(argname="argument suggested_value", value=suggested_value, expected_type=type_hints["suggested_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow is not None:
            self._values["allow"] = allow
        if deny is not None:
            self._values["deny"] = deny
        if inherit_from_parent is not None:
            self._values["inherit_from_parent"] = inherit_from_parent
        if suggested_value is not None:
            self._values["suggested_value"] = suggested_value

    @builtins.property
    def allow(
        self,
    ) -> typing.Optional["GoogleProjectOrganizationPolicyListPolicyAllow"]:
        '''allow block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#allow GoogleProjectOrganizationPolicy#allow}
        '''
        result = self._values.get("allow")
        return typing.cast(typing.Optional["GoogleProjectOrganizationPolicyListPolicyAllow"], result)

    @builtins.property
    def deny(self) -> typing.Optional["GoogleProjectOrganizationPolicyListPolicyDeny"]:
        '''deny block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#deny GoogleProjectOrganizationPolicy#deny}
        '''
        result = self._values.get("deny")
        return typing.cast(typing.Optional["GoogleProjectOrganizationPolicyListPolicyDeny"], result)

    @builtins.property
    def inherit_from_parent(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, the values from the effective Policy of the parent resource are inherited, meaning the values set in this Policy are added to the values inherited up the hierarchy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#inherit_from_parent GoogleProjectOrganizationPolicy#inherit_from_parent}
        '''
        result = self._values.get("inherit_from_parent")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def suggested_value(self) -> typing.Optional[builtins.str]:
        '''The Google Cloud Console will try to default to a configuration that matches the value specified in this field.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#suggested_value GoogleProjectOrganizationPolicy#suggested_value}
        '''
        result = self._values.get("suggested_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleProjectOrganizationPolicyListPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleProjectOrganizationPolicy.GoogleProjectOrganizationPolicyListPolicyAllow",
    jsii_struct_bases=[],
    name_mapping={"all": "all", "values": "values"},
)
class GoogleProjectOrganizationPolicyListPolicyAllow:
    def __init__(
        self,
        *,
        all: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: The policy allows or denies all values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#all GoogleProjectOrganizationPolicy#all}
        :param values: The policy can define specific values that are allowed or denied. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#values GoogleProjectOrganizationPolicy#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleProjectOrganizationPolicyListPolicyAllow.__init__)
            check_type(argname="argument all", value=all, expected_type=type_hints["all"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all is not None:
            self._values["all"] = all
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def all(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The policy allows or denies all values.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#all GoogleProjectOrganizationPolicy#all}
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The policy can define specific values that are allowed or denied.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#values GoogleProjectOrganizationPolicy#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleProjectOrganizationPolicyListPolicyAllow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleProjectOrganizationPolicyListPolicyAllowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleProjectOrganizationPolicy.GoogleProjectOrganizationPolicyListPolicyAllowOutputReference",
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
            type_hints = typing.get_type_hints(GoogleProjectOrganizationPolicyListPolicyAllowOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAll")
    def reset_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAll", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="allInput")
    def all_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="all")
    def all(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "all"))

    @all.setter
    def all(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicyListPolicyAllowOutputReference, "all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "all", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicyListPolicyAllowOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleProjectOrganizationPolicyListPolicyAllow]:
        return typing.cast(typing.Optional[GoogleProjectOrganizationPolicyListPolicyAllow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleProjectOrganizationPolicyListPolicyAllow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicyListPolicyAllowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleProjectOrganizationPolicy.GoogleProjectOrganizationPolicyListPolicyDeny",
    jsii_struct_bases=[],
    name_mapping={"all": "all", "values": "values"},
)
class GoogleProjectOrganizationPolicyListPolicyDeny:
    def __init__(
        self,
        *,
        all: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: The policy allows or denies all values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#all GoogleProjectOrganizationPolicy#all}
        :param values: The policy can define specific values that are allowed or denied. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#values GoogleProjectOrganizationPolicy#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleProjectOrganizationPolicyListPolicyDeny.__init__)
            check_type(argname="argument all", value=all, expected_type=type_hints["all"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all is not None:
            self._values["all"] = all
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def all(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The policy allows or denies all values.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#all GoogleProjectOrganizationPolicy#all}
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The policy can define specific values that are allowed or denied.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#values GoogleProjectOrganizationPolicy#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleProjectOrganizationPolicyListPolicyDeny(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleProjectOrganizationPolicyListPolicyDenyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleProjectOrganizationPolicy.GoogleProjectOrganizationPolicyListPolicyDenyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleProjectOrganizationPolicyListPolicyDenyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAll")
    def reset_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAll", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="allInput")
    def all_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="all")
    def all(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "all"))

    @all.setter
    def all(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicyListPolicyDenyOutputReference, "all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "all", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicyListPolicyDenyOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleProjectOrganizationPolicyListPolicyDeny]:
        return typing.cast(typing.Optional[GoogleProjectOrganizationPolicyListPolicyDeny], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleProjectOrganizationPolicyListPolicyDeny],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicyListPolicyDenyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleProjectOrganizationPolicyListPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleProjectOrganizationPolicy.GoogleProjectOrganizationPolicyListPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleProjectOrganizationPolicyListPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAllow")
    def put_allow(
        self,
        *,
        all: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: The policy allows or denies all values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#all GoogleProjectOrganizationPolicy#all}
        :param values: The policy can define specific values that are allowed or denied. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#values GoogleProjectOrganizationPolicy#values}
        '''
        value = GoogleProjectOrganizationPolicyListPolicyAllow(all=all, values=values)

        return typing.cast(None, jsii.invoke(self, "putAllow", [value]))

    @jsii.member(jsii_name="putDeny")
    def put_deny(
        self,
        *,
        all: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: The policy allows or denies all values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#all GoogleProjectOrganizationPolicy#all}
        :param values: The policy can define specific values that are allowed or denied. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#values GoogleProjectOrganizationPolicy#values}
        '''
        value = GoogleProjectOrganizationPolicyListPolicyDeny(all=all, values=values)

        return typing.cast(None, jsii.invoke(self, "putDeny", [value]))

    @jsii.member(jsii_name="resetAllow")
    def reset_allow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllow", []))

    @jsii.member(jsii_name="resetDeny")
    def reset_deny(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeny", []))

    @jsii.member(jsii_name="resetInheritFromParent")
    def reset_inherit_from_parent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInheritFromParent", []))

    @jsii.member(jsii_name="resetSuggestedValue")
    def reset_suggested_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuggestedValue", []))

    @builtins.property
    @jsii.member(jsii_name="allow")
    def allow(self) -> GoogleProjectOrganizationPolicyListPolicyAllowOutputReference:
        return typing.cast(GoogleProjectOrganizationPolicyListPolicyAllowOutputReference, jsii.get(self, "allow"))

    @builtins.property
    @jsii.member(jsii_name="deny")
    def deny(self) -> GoogleProjectOrganizationPolicyListPolicyDenyOutputReference:
        return typing.cast(GoogleProjectOrganizationPolicyListPolicyDenyOutputReference, jsii.get(self, "deny"))

    @builtins.property
    @jsii.member(jsii_name="allowInput")
    def allow_input(
        self,
    ) -> typing.Optional[GoogleProjectOrganizationPolicyListPolicyAllow]:
        return typing.cast(typing.Optional[GoogleProjectOrganizationPolicyListPolicyAllow], jsii.get(self, "allowInput"))

    @builtins.property
    @jsii.member(jsii_name="denyInput")
    def deny_input(
        self,
    ) -> typing.Optional[GoogleProjectOrganizationPolicyListPolicyDeny]:
        return typing.cast(typing.Optional[GoogleProjectOrganizationPolicyListPolicyDeny], jsii.get(self, "denyInput"))

    @builtins.property
    @jsii.member(jsii_name="inheritFromParentInput")
    def inherit_from_parent_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "inheritFromParentInput"))

    @builtins.property
    @jsii.member(jsii_name="suggestedValueInput")
    def suggested_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "suggestedValueInput"))

    @builtins.property
    @jsii.member(jsii_name="inheritFromParent")
    def inherit_from_parent(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "inheritFromParent"))

    @inherit_from_parent.setter
    def inherit_from_parent(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicyListPolicyOutputReference, "inherit_from_parent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inheritFromParent", value)

    @builtins.property
    @jsii.member(jsii_name="suggestedValue")
    def suggested_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suggestedValue"))

    @suggested_value.setter
    def suggested_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicyListPolicyOutputReference, "suggested_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suggestedValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleProjectOrganizationPolicyListPolicy]:
        return typing.cast(typing.Optional[GoogleProjectOrganizationPolicyListPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleProjectOrganizationPolicyListPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicyListPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleProjectOrganizationPolicy.GoogleProjectOrganizationPolicyRestorePolicy",
    jsii_struct_bases=[],
    name_mapping={"default": "default"},
)
class GoogleProjectOrganizationPolicyRestorePolicy:
    def __init__(
        self,
        *,
        default: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param default: May only be set to true. If set, then the default Policy is restored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#default GoogleProjectOrganizationPolicy#default}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleProjectOrganizationPolicyRestorePolicy.__init__)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[str, typing.Any] = {
            "default": default,
        }

    @builtins.property
    def default(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''May only be set to true. If set, then the default Policy is restored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#default GoogleProjectOrganizationPolicy#default}
        '''
        result = self._values.get("default")
        assert result is not None, "Required property 'default' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleProjectOrganizationPolicyRestorePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleProjectOrganizationPolicyRestorePolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleProjectOrganizationPolicy.GoogleProjectOrganizationPolicyRestorePolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleProjectOrganizationPolicyRestorePolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "default"))

    @default.setter
    def default(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicyRestorePolicyOutputReference, "default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleProjectOrganizationPolicyRestorePolicy]:
        return typing.cast(typing.Optional[GoogleProjectOrganizationPolicyRestorePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleProjectOrganizationPolicyRestorePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicyRestorePolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleProjectOrganizationPolicy.GoogleProjectOrganizationPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class GoogleProjectOrganizationPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#create GoogleProjectOrganizationPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#delete GoogleProjectOrganizationPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#read GoogleProjectOrganizationPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#update GoogleProjectOrganizationPolicy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleProjectOrganizationPolicyTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#create GoogleProjectOrganizationPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#delete GoogleProjectOrganizationPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#read GoogleProjectOrganizationPolicy#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_project_organization_policy#update GoogleProjectOrganizationPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleProjectOrganizationPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleProjectOrganizationPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleProjectOrganizationPolicy.GoogleProjectOrganizationPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleProjectOrganizationPolicyTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicyTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleProjectOrganizationPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleProjectOrganizationPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleProjectOrganizationPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleProjectOrganizationPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleProjectOrganizationPolicy",
    "GoogleProjectOrganizationPolicyBooleanPolicy",
    "GoogleProjectOrganizationPolicyBooleanPolicyOutputReference",
    "GoogleProjectOrganizationPolicyConfig",
    "GoogleProjectOrganizationPolicyListPolicy",
    "GoogleProjectOrganizationPolicyListPolicyAllow",
    "GoogleProjectOrganizationPolicyListPolicyAllowOutputReference",
    "GoogleProjectOrganizationPolicyListPolicyDeny",
    "GoogleProjectOrganizationPolicyListPolicyDenyOutputReference",
    "GoogleProjectOrganizationPolicyListPolicyOutputReference",
    "GoogleProjectOrganizationPolicyRestorePolicy",
    "GoogleProjectOrganizationPolicyRestorePolicyOutputReference",
    "GoogleProjectOrganizationPolicyTimeouts",
    "GoogleProjectOrganizationPolicyTimeoutsOutputReference",
]

publication.publish()
