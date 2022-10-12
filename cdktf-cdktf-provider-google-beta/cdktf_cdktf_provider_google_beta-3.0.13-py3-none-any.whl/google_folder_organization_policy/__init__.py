'''
# `google_folder_organization_policy`

Refer to the Terraform Registory for docs: [`google_folder_organization_policy`](https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy).
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


class GoogleFolderOrganizationPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleFolderOrganizationPolicy.GoogleFolderOrganizationPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy google_folder_organization_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        constraint: builtins.str,
        folder: builtins.str,
        boolean_policy: typing.Optional[typing.Union["GoogleFolderOrganizationPolicyBooleanPolicy", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        list_policy: typing.Optional[typing.Union["GoogleFolderOrganizationPolicyListPolicy", typing.Dict[str, typing.Any]]] = None,
        restore_policy: typing.Optional[typing.Union["GoogleFolderOrganizationPolicyRestorePolicy", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleFolderOrganizationPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy google_folder_organization_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param constraint: The name of the Constraint the Policy is configuring, for example, serviceuser.services. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#constraint GoogleFolderOrganizationPolicy#constraint}
        :param folder: The resource name of the folder to set the policy for. Its format is folders/{folder_id}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#folder GoogleFolderOrganizationPolicy#folder}
        :param boolean_policy: boolean_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#boolean_policy GoogleFolderOrganizationPolicy#boolean_policy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#id GoogleFolderOrganizationPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param list_policy: list_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#list_policy GoogleFolderOrganizationPolicy#list_policy}
        :param restore_policy: restore_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#restore_policy GoogleFolderOrganizationPolicy#restore_policy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#timeouts GoogleFolderOrganizationPolicy#timeouts}
        :param version: Version of the Policy. Default version is 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#version GoogleFolderOrganizationPolicy#version}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleFolderOrganizationPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleFolderOrganizationPolicyConfig(
            constraint=constraint,
            folder=folder,
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
        :param enforced: If true, then the Policy is enforced. If false, then any configuration is acceptable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#enforced GoogleFolderOrganizationPolicy#enforced}
        '''
        value = GoogleFolderOrganizationPolicyBooleanPolicy(enforced=enforced)

        return typing.cast(None, jsii.invoke(self, "putBooleanPolicy", [value]))

    @jsii.member(jsii_name="putListPolicy")
    def put_list_policy(
        self,
        *,
        allow: typing.Optional[typing.Union["GoogleFolderOrganizationPolicyListPolicyAllow", typing.Dict[str, typing.Any]]] = None,
        deny: typing.Optional[typing.Union["GoogleFolderOrganizationPolicyListPolicyDeny", typing.Dict[str, typing.Any]]] = None,
        inherit_from_parent: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        suggested_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow: allow block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#allow GoogleFolderOrganizationPolicy#allow}
        :param deny: deny block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#deny GoogleFolderOrganizationPolicy#deny}
        :param inherit_from_parent: If set to true, the values from the effective Policy of the parent resource are inherited, meaning the values set in this Policy are added to the values inherited up the hierarchy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#inherit_from_parent GoogleFolderOrganizationPolicy#inherit_from_parent}
        :param suggested_value: The Google Cloud Console will try to default to a configuration that matches the value specified in this field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#suggested_value GoogleFolderOrganizationPolicy#suggested_value}
        '''
        value = GoogleFolderOrganizationPolicyListPolicy(
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
        :param default: May only be set to true. If set, then the default Policy is restored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#default GoogleFolderOrganizationPolicy#default}
        '''
        value = GoogleFolderOrganizationPolicyRestorePolicy(default=default)

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#create GoogleFolderOrganizationPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#delete GoogleFolderOrganizationPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#read GoogleFolderOrganizationPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#update GoogleFolderOrganizationPolicy#update}.
        '''
        value = GoogleFolderOrganizationPolicyTimeouts(
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
    ) -> "GoogleFolderOrganizationPolicyBooleanPolicyOutputReference":
        return typing.cast("GoogleFolderOrganizationPolicyBooleanPolicyOutputReference", jsii.get(self, "booleanPolicy"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="listPolicy")
    def list_policy(self) -> "GoogleFolderOrganizationPolicyListPolicyOutputReference":
        return typing.cast("GoogleFolderOrganizationPolicyListPolicyOutputReference", jsii.get(self, "listPolicy"))

    @builtins.property
    @jsii.member(jsii_name="restorePolicy")
    def restore_policy(
        self,
    ) -> "GoogleFolderOrganizationPolicyRestorePolicyOutputReference":
        return typing.cast("GoogleFolderOrganizationPolicyRestorePolicyOutputReference", jsii.get(self, "restorePolicy"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleFolderOrganizationPolicyTimeoutsOutputReference":
        return typing.cast("GoogleFolderOrganizationPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="booleanPolicyInput")
    def boolean_policy_input(
        self,
    ) -> typing.Optional["GoogleFolderOrganizationPolicyBooleanPolicy"]:
        return typing.cast(typing.Optional["GoogleFolderOrganizationPolicyBooleanPolicy"], jsii.get(self, "booleanPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="constraintInput")
    def constraint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "constraintInput"))

    @builtins.property
    @jsii.member(jsii_name="folderInput")
    def folder_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "folderInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="listPolicyInput")
    def list_policy_input(
        self,
    ) -> typing.Optional["GoogleFolderOrganizationPolicyListPolicy"]:
        return typing.cast(typing.Optional["GoogleFolderOrganizationPolicyListPolicy"], jsii.get(self, "listPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="restorePolicyInput")
    def restore_policy_input(
        self,
    ) -> typing.Optional["GoogleFolderOrganizationPolicyRestorePolicy"]:
        return typing.cast(typing.Optional["GoogleFolderOrganizationPolicyRestorePolicy"], jsii.get(self, "restorePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleFolderOrganizationPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleFolderOrganizationPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

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
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicy, "constraint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "constraint", value)

    @builtins.property
    @jsii.member(jsii_name="folder")
    def folder(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "folder"))

    @folder.setter
    def folder(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicy, "folder").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "folder", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @version.setter
    def version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicy, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleFolderOrganizationPolicy.GoogleFolderOrganizationPolicyBooleanPolicy",
    jsii_struct_bases=[],
    name_mapping={"enforced": "enforced"},
)
class GoogleFolderOrganizationPolicyBooleanPolicy:
    def __init__(
        self,
        *,
        enforced: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enforced: If true, then the Policy is enforced. If false, then any configuration is acceptable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#enforced GoogleFolderOrganizationPolicy#enforced}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleFolderOrganizationPolicyBooleanPolicy.__init__)
            check_type(argname="argument enforced", value=enforced, expected_type=type_hints["enforced"])
        self._values: typing.Dict[str, typing.Any] = {
            "enforced": enforced,
        }

    @builtins.property
    def enforced(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If true, then the Policy is enforced. If false, then any configuration is acceptable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#enforced GoogleFolderOrganizationPolicy#enforced}
        '''
        result = self._values.get("enforced")
        assert result is not None, "Required property 'enforced' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleFolderOrganizationPolicyBooleanPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleFolderOrganizationPolicyBooleanPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleFolderOrganizationPolicy.GoogleFolderOrganizationPolicyBooleanPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleFolderOrganizationPolicyBooleanPolicyOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicyBooleanPolicyOutputReference, "enforced").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforced", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleFolderOrganizationPolicyBooleanPolicy]:
        return typing.cast(typing.Optional[GoogleFolderOrganizationPolicyBooleanPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleFolderOrganizationPolicyBooleanPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicyBooleanPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleFolderOrganizationPolicy.GoogleFolderOrganizationPolicyConfig",
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
        "folder": "folder",
        "boolean_policy": "booleanPolicy",
        "id": "id",
        "list_policy": "listPolicy",
        "restore_policy": "restorePolicy",
        "timeouts": "timeouts",
        "version": "version",
    },
)
class GoogleFolderOrganizationPolicyConfig(cdktf.TerraformMetaArguments):
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
        folder: builtins.str,
        boolean_policy: typing.Optional[typing.Union[GoogleFolderOrganizationPolicyBooleanPolicy, typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        list_policy: typing.Optional[typing.Union["GoogleFolderOrganizationPolicyListPolicy", typing.Dict[str, typing.Any]]] = None,
        restore_policy: typing.Optional[typing.Union["GoogleFolderOrganizationPolicyRestorePolicy", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleFolderOrganizationPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
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
        :param constraint: The name of the Constraint the Policy is configuring, for example, serviceuser.services. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#constraint GoogleFolderOrganizationPolicy#constraint}
        :param folder: The resource name of the folder to set the policy for. Its format is folders/{folder_id}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#folder GoogleFolderOrganizationPolicy#folder}
        :param boolean_policy: boolean_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#boolean_policy GoogleFolderOrganizationPolicy#boolean_policy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#id GoogleFolderOrganizationPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param list_policy: list_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#list_policy GoogleFolderOrganizationPolicy#list_policy}
        :param restore_policy: restore_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#restore_policy GoogleFolderOrganizationPolicy#restore_policy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#timeouts GoogleFolderOrganizationPolicy#timeouts}
        :param version: Version of the Policy. Default version is 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#version GoogleFolderOrganizationPolicy#version}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(boolean_policy, dict):
            boolean_policy = GoogleFolderOrganizationPolicyBooleanPolicy(**boolean_policy)
        if isinstance(list_policy, dict):
            list_policy = GoogleFolderOrganizationPolicyListPolicy(**list_policy)
        if isinstance(restore_policy, dict):
            restore_policy = GoogleFolderOrganizationPolicyRestorePolicy(**restore_policy)
        if isinstance(timeouts, dict):
            timeouts = GoogleFolderOrganizationPolicyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleFolderOrganizationPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument constraint", value=constraint, expected_type=type_hints["constraint"])
            check_type(argname="argument folder", value=folder, expected_type=type_hints["folder"])
            check_type(argname="argument boolean_policy", value=boolean_policy, expected_type=type_hints["boolean_policy"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument list_policy", value=list_policy, expected_type=type_hints["list_policy"])
            check_type(argname="argument restore_policy", value=restore_policy, expected_type=type_hints["restore_policy"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {
            "constraint": constraint,
            "folder": folder,
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#constraint GoogleFolderOrganizationPolicy#constraint}
        '''
        result = self._values.get("constraint")
        assert result is not None, "Required property 'constraint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def folder(self) -> builtins.str:
        '''The resource name of the folder to set the policy for. Its format is folders/{folder_id}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#folder GoogleFolderOrganizationPolicy#folder}
        '''
        result = self._values.get("folder")
        assert result is not None, "Required property 'folder' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def boolean_policy(
        self,
    ) -> typing.Optional[GoogleFolderOrganizationPolicyBooleanPolicy]:
        '''boolean_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#boolean_policy GoogleFolderOrganizationPolicy#boolean_policy}
        '''
        result = self._values.get("boolean_policy")
        return typing.cast(typing.Optional[GoogleFolderOrganizationPolicyBooleanPolicy], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#id GoogleFolderOrganizationPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def list_policy(
        self,
    ) -> typing.Optional["GoogleFolderOrganizationPolicyListPolicy"]:
        '''list_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#list_policy GoogleFolderOrganizationPolicy#list_policy}
        '''
        result = self._values.get("list_policy")
        return typing.cast(typing.Optional["GoogleFolderOrganizationPolicyListPolicy"], result)

    @builtins.property
    def restore_policy(
        self,
    ) -> typing.Optional["GoogleFolderOrganizationPolicyRestorePolicy"]:
        '''restore_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#restore_policy GoogleFolderOrganizationPolicy#restore_policy}
        '''
        result = self._values.get("restore_policy")
        return typing.cast(typing.Optional["GoogleFolderOrganizationPolicyRestorePolicy"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleFolderOrganizationPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#timeouts GoogleFolderOrganizationPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleFolderOrganizationPolicyTimeouts"], result)

    @builtins.property
    def version(self) -> typing.Optional[jsii.Number]:
        '''Version of the Policy. Default version is 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#version GoogleFolderOrganizationPolicy#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleFolderOrganizationPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleFolderOrganizationPolicy.GoogleFolderOrganizationPolicyListPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "allow": "allow",
        "deny": "deny",
        "inherit_from_parent": "inheritFromParent",
        "suggested_value": "suggestedValue",
    },
)
class GoogleFolderOrganizationPolicyListPolicy:
    def __init__(
        self,
        *,
        allow: typing.Optional[typing.Union["GoogleFolderOrganizationPolicyListPolicyAllow", typing.Dict[str, typing.Any]]] = None,
        deny: typing.Optional[typing.Union["GoogleFolderOrganizationPolicyListPolicyDeny", typing.Dict[str, typing.Any]]] = None,
        inherit_from_parent: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        suggested_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow: allow block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#allow GoogleFolderOrganizationPolicy#allow}
        :param deny: deny block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#deny GoogleFolderOrganizationPolicy#deny}
        :param inherit_from_parent: If set to true, the values from the effective Policy of the parent resource are inherited, meaning the values set in this Policy are added to the values inherited up the hierarchy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#inherit_from_parent GoogleFolderOrganizationPolicy#inherit_from_parent}
        :param suggested_value: The Google Cloud Console will try to default to a configuration that matches the value specified in this field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#suggested_value GoogleFolderOrganizationPolicy#suggested_value}
        '''
        if isinstance(allow, dict):
            allow = GoogleFolderOrganizationPolicyListPolicyAllow(**allow)
        if isinstance(deny, dict):
            deny = GoogleFolderOrganizationPolicyListPolicyDeny(**deny)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleFolderOrganizationPolicyListPolicy.__init__)
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
    def allow(self) -> typing.Optional["GoogleFolderOrganizationPolicyListPolicyAllow"]:
        '''allow block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#allow GoogleFolderOrganizationPolicy#allow}
        '''
        result = self._values.get("allow")
        return typing.cast(typing.Optional["GoogleFolderOrganizationPolicyListPolicyAllow"], result)

    @builtins.property
    def deny(self) -> typing.Optional["GoogleFolderOrganizationPolicyListPolicyDeny"]:
        '''deny block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#deny GoogleFolderOrganizationPolicy#deny}
        '''
        result = self._values.get("deny")
        return typing.cast(typing.Optional["GoogleFolderOrganizationPolicyListPolicyDeny"], result)

    @builtins.property
    def inherit_from_parent(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, the values from the effective Policy of the parent resource are inherited, meaning the values set in this Policy are added to the values inherited up the hierarchy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#inherit_from_parent GoogleFolderOrganizationPolicy#inherit_from_parent}
        '''
        result = self._values.get("inherit_from_parent")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def suggested_value(self) -> typing.Optional[builtins.str]:
        '''The Google Cloud Console will try to default to a configuration that matches the value specified in this field.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#suggested_value GoogleFolderOrganizationPolicy#suggested_value}
        '''
        result = self._values.get("suggested_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleFolderOrganizationPolicyListPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleFolderOrganizationPolicy.GoogleFolderOrganizationPolicyListPolicyAllow",
    jsii_struct_bases=[],
    name_mapping={"all": "all", "values": "values"},
)
class GoogleFolderOrganizationPolicyListPolicyAllow:
    def __init__(
        self,
        *,
        all: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: The policy allows or denies all values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#all GoogleFolderOrganizationPolicy#all}
        :param values: The policy can define specific values that are allowed or denied. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#values GoogleFolderOrganizationPolicy#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleFolderOrganizationPolicyListPolicyAllow.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#all GoogleFolderOrganizationPolicy#all}
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The policy can define specific values that are allowed or denied.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#values GoogleFolderOrganizationPolicy#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleFolderOrganizationPolicyListPolicyAllow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleFolderOrganizationPolicyListPolicyAllowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleFolderOrganizationPolicy.GoogleFolderOrganizationPolicyListPolicyAllowOutputReference",
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
            type_hints = typing.get_type_hints(GoogleFolderOrganizationPolicyListPolicyAllowOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicyListPolicyAllowOutputReference, "all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "all", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicyListPolicyAllowOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleFolderOrganizationPolicyListPolicyAllow]:
        return typing.cast(typing.Optional[GoogleFolderOrganizationPolicyListPolicyAllow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleFolderOrganizationPolicyListPolicyAllow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicyListPolicyAllowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleFolderOrganizationPolicy.GoogleFolderOrganizationPolicyListPolicyDeny",
    jsii_struct_bases=[],
    name_mapping={"all": "all", "values": "values"},
)
class GoogleFolderOrganizationPolicyListPolicyDeny:
    def __init__(
        self,
        *,
        all: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: The policy allows or denies all values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#all GoogleFolderOrganizationPolicy#all}
        :param values: The policy can define specific values that are allowed or denied. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#values GoogleFolderOrganizationPolicy#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleFolderOrganizationPolicyListPolicyDeny.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#all GoogleFolderOrganizationPolicy#all}
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The policy can define specific values that are allowed or denied.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#values GoogleFolderOrganizationPolicy#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleFolderOrganizationPolicyListPolicyDeny(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleFolderOrganizationPolicyListPolicyDenyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleFolderOrganizationPolicy.GoogleFolderOrganizationPolicyListPolicyDenyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleFolderOrganizationPolicyListPolicyDenyOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicyListPolicyDenyOutputReference, "all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "all", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicyListPolicyDenyOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleFolderOrganizationPolicyListPolicyDeny]:
        return typing.cast(typing.Optional[GoogleFolderOrganizationPolicyListPolicyDeny], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleFolderOrganizationPolicyListPolicyDeny],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicyListPolicyDenyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleFolderOrganizationPolicyListPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleFolderOrganizationPolicy.GoogleFolderOrganizationPolicyListPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleFolderOrganizationPolicyListPolicyOutputReference.__init__)
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
        :param all: The policy allows or denies all values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#all GoogleFolderOrganizationPolicy#all}
        :param values: The policy can define specific values that are allowed or denied. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#values GoogleFolderOrganizationPolicy#values}
        '''
        value = GoogleFolderOrganizationPolicyListPolicyAllow(all=all, values=values)

        return typing.cast(None, jsii.invoke(self, "putAllow", [value]))

    @jsii.member(jsii_name="putDeny")
    def put_deny(
        self,
        *,
        all: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param all: The policy allows or denies all values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#all GoogleFolderOrganizationPolicy#all}
        :param values: The policy can define specific values that are allowed or denied. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#values GoogleFolderOrganizationPolicy#values}
        '''
        value = GoogleFolderOrganizationPolicyListPolicyDeny(all=all, values=values)

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
    def allow(self) -> GoogleFolderOrganizationPolicyListPolicyAllowOutputReference:
        return typing.cast(GoogleFolderOrganizationPolicyListPolicyAllowOutputReference, jsii.get(self, "allow"))

    @builtins.property
    @jsii.member(jsii_name="deny")
    def deny(self) -> GoogleFolderOrganizationPolicyListPolicyDenyOutputReference:
        return typing.cast(GoogleFolderOrganizationPolicyListPolicyDenyOutputReference, jsii.get(self, "deny"))

    @builtins.property
    @jsii.member(jsii_name="allowInput")
    def allow_input(
        self,
    ) -> typing.Optional[GoogleFolderOrganizationPolicyListPolicyAllow]:
        return typing.cast(typing.Optional[GoogleFolderOrganizationPolicyListPolicyAllow], jsii.get(self, "allowInput"))

    @builtins.property
    @jsii.member(jsii_name="denyInput")
    def deny_input(
        self,
    ) -> typing.Optional[GoogleFolderOrganizationPolicyListPolicyDeny]:
        return typing.cast(typing.Optional[GoogleFolderOrganizationPolicyListPolicyDeny], jsii.get(self, "denyInput"))

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
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicyListPolicyOutputReference, "inherit_from_parent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inheritFromParent", value)

    @builtins.property
    @jsii.member(jsii_name="suggestedValue")
    def suggested_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suggestedValue"))

    @suggested_value.setter
    def suggested_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicyListPolicyOutputReference, "suggested_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suggestedValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleFolderOrganizationPolicyListPolicy]:
        return typing.cast(typing.Optional[GoogleFolderOrganizationPolicyListPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleFolderOrganizationPolicyListPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicyListPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleFolderOrganizationPolicy.GoogleFolderOrganizationPolicyRestorePolicy",
    jsii_struct_bases=[],
    name_mapping={"default": "default"},
)
class GoogleFolderOrganizationPolicyRestorePolicy:
    def __init__(
        self,
        *,
        default: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param default: May only be set to true. If set, then the default Policy is restored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#default GoogleFolderOrganizationPolicy#default}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleFolderOrganizationPolicyRestorePolicy.__init__)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[str, typing.Any] = {
            "default": default,
        }

    @builtins.property
    def default(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''May only be set to true. If set, then the default Policy is restored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#default GoogleFolderOrganizationPolicy#default}
        '''
        result = self._values.get("default")
        assert result is not None, "Required property 'default' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleFolderOrganizationPolicyRestorePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleFolderOrganizationPolicyRestorePolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleFolderOrganizationPolicy.GoogleFolderOrganizationPolicyRestorePolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleFolderOrganizationPolicyRestorePolicyOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicyRestorePolicyOutputReference, "default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleFolderOrganizationPolicyRestorePolicy]:
        return typing.cast(typing.Optional[GoogleFolderOrganizationPolicyRestorePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleFolderOrganizationPolicyRestorePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicyRestorePolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleFolderOrganizationPolicy.GoogleFolderOrganizationPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class GoogleFolderOrganizationPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#create GoogleFolderOrganizationPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#delete GoogleFolderOrganizationPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#read GoogleFolderOrganizationPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#update GoogleFolderOrganizationPolicy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleFolderOrganizationPolicyTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#create GoogleFolderOrganizationPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#delete GoogleFolderOrganizationPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#read GoogleFolderOrganizationPolicy#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_folder_organization_policy#update GoogleFolderOrganizationPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleFolderOrganizationPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleFolderOrganizationPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleFolderOrganizationPolicy.GoogleFolderOrganizationPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleFolderOrganizationPolicyTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicyTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleFolderOrganizationPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleFolderOrganizationPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleFolderOrganizationPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleFolderOrganizationPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleFolderOrganizationPolicy",
    "GoogleFolderOrganizationPolicyBooleanPolicy",
    "GoogleFolderOrganizationPolicyBooleanPolicyOutputReference",
    "GoogleFolderOrganizationPolicyConfig",
    "GoogleFolderOrganizationPolicyListPolicy",
    "GoogleFolderOrganizationPolicyListPolicyAllow",
    "GoogleFolderOrganizationPolicyListPolicyAllowOutputReference",
    "GoogleFolderOrganizationPolicyListPolicyDeny",
    "GoogleFolderOrganizationPolicyListPolicyDenyOutputReference",
    "GoogleFolderOrganizationPolicyListPolicyOutputReference",
    "GoogleFolderOrganizationPolicyRestorePolicy",
    "GoogleFolderOrganizationPolicyRestorePolicyOutputReference",
    "GoogleFolderOrganizationPolicyTimeouts",
    "GoogleFolderOrganizationPolicyTimeoutsOutputReference",
]

publication.publish()
