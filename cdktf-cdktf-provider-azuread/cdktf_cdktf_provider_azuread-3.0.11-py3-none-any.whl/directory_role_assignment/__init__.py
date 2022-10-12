'''
# `azuread_directory_role_assignment`

Refer to the Terraform Registory for docs: [`azuread_directory_role_assignment`](https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment).
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


class DirectoryRoleAssignment(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.directoryRoleAssignment.DirectoryRoleAssignment",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment azuread_directory_role_assignment}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        principal_object_id: builtins.str,
        role_id: builtins.str,
        app_scope_id: typing.Optional[builtins.str] = None,
        app_scope_object_id: typing.Optional[builtins.str] = None,
        directory_scope_id: typing.Optional[builtins.str] = None,
        directory_scope_object_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DirectoryRoleAssignmentTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment azuread_directory_role_assignment} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param principal_object_id: The object ID of the member principal. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#principal_object_id DirectoryRoleAssignment#principal_object_id}
        :param role_id: The object ID of the directory role for this assignment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#role_id DirectoryRoleAssignment#role_id}
        :param app_scope_id: Identifier of the app-specific scope when the assignment scope is app-specific. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#app_scope_id DirectoryRoleAssignment#app_scope_id}
        :param app_scope_object_id: Identifier of the app-specific scope when the assignment scope is app-specific. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#app_scope_object_id DirectoryRoleAssignment#app_scope_object_id}
        :param directory_scope_id: Identifier of the directory object representing the scope of the assignment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#directory_scope_id DirectoryRoleAssignment#directory_scope_id}
        :param directory_scope_object_id: Identifier of the directory object representing the scope of the assignment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#directory_scope_object_id DirectoryRoleAssignment#directory_scope_object_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#id DirectoryRoleAssignment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#timeouts DirectoryRoleAssignment#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DirectoryRoleAssignment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DirectoryRoleAssignmentConfig(
            principal_object_id=principal_object_id,
            role_id=role_id,
            app_scope_id=app_scope_id,
            app_scope_object_id=app_scope_object_id,
            directory_scope_id=directory_scope_id,
            directory_scope_object_id=directory_scope_object_id,
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
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#create DirectoryRoleAssignment#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#delete DirectoryRoleAssignment#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#read DirectoryRoleAssignment#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#update DirectoryRoleAssignment#update}.
        '''
        value = DirectoryRoleAssignmentTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAppScopeId")
    def reset_app_scope_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppScopeId", []))

    @jsii.member(jsii_name="resetAppScopeObjectId")
    def reset_app_scope_object_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppScopeObjectId", []))

    @jsii.member(jsii_name="resetDirectoryScopeId")
    def reset_directory_scope_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectoryScopeId", []))

    @jsii.member(jsii_name="resetDirectoryScopeObjectId")
    def reset_directory_scope_object_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectoryScopeObjectId", []))

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
    def timeouts(self) -> "DirectoryRoleAssignmentTimeoutsOutputReference":
        return typing.cast("DirectoryRoleAssignmentTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="appScopeIdInput")
    def app_scope_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appScopeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="appScopeObjectIdInput")
    def app_scope_object_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appScopeObjectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryScopeIdInput")
    def directory_scope_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryScopeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryScopeObjectIdInput")
    def directory_scope_object_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryScopeObjectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="principalObjectIdInput")
    def principal_object_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalObjectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="roleIdInput")
    def role_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DirectoryRoleAssignmentTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DirectoryRoleAssignmentTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="appScopeId")
    def app_scope_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appScopeId"))

    @app_scope_id.setter
    def app_scope_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DirectoryRoleAssignment, "app_scope_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appScopeId", value)

    @builtins.property
    @jsii.member(jsii_name="appScopeObjectId")
    def app_scope_object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appScopeObjectId"))

    @app_scope_object_id.setter
    def app_scope_object_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DirectoryRoleAssignment, "app_scope_object_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appScopeObjectId", value)

    @builtins.property
    @jsii.member(jsii_name="directoryScopeId")
    def directory_scope_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryScopeId"))

    @directory_scope_id.setter
    def directory_scope_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DirectoryRoleAssignment, "directory_scope_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryScopeId", value)

    @builtins.property
    @jsii.member(jsii_name="directoryScopeObjectId")
    def directory_scope_object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryScopeObjectId"))

    @directory_scope_object_id.setter
    def directory_scope_object_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DirectoryRoleAssignment, "directory_scope_object_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryScopeObjectId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DirectoryRoleAssignment, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="principalObjectId")
    def principal_object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalObjectId"))

    @principal_object_id.setter
    def principal_object_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DirectoryRoleAssignment, "principal_object_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principalObjectId", value)

    @builtins.property
    @jsii.member(jsii_name="roleId")
    def role_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleId"))

    @role_id.setter
    def role_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DirectoryRoleAssignment, "role_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.directoryRoleAssignment.DirectoryRoleAssignmentConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "principal_object_id": "principalObjectId",
        "role_id": "roleId",
        "app_scope_id": "appScopeId",
        "app_scope_object_id": "appScopeObjectId",
        "directory_scope_id": "directoryScopeId",
        "directory_scope_object_id": "directoryScopeObjectId",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class DirectoryRoleAssignmentConfig(cdktf.TerraformMetaArguments):
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
        principal_object_id: builtins.str,
        role_id: builtins.str,
        app_scope_id: typing.Optional[builtins.str] = None,
        app_scope_object_id: typing.Optional[builtins.str] = None,
        directory_scope_id: typing.Optional[builtins.str] = None,
        directory_scope_object_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DirectoryRoleAssignmentTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param principal_object_id: The object ID of the member principal. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#principal_object_id DirectoryRoleAssignment#principal_object_id}
        :param role_id: The object ID of the directory role for this assignment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#role_id DirectoryRoleAssignment#role_id}
        :param app_scope_id: Identifier of the app-specific scope when the assignment scope is app-specific. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#app_scope_id DirectoryRoleAssignment#app_scope_id}
        :param app_scope_object_id: Identifier of the app-specific scope when the assignment scope is app-specific. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#app_scope_object_id DirectoryRoleAssignment#app_scope_object_id}
        :param directory_scope_id: Identifier of the directory object representing the scope of the assignment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#directory_scope_id DirectoryRoleAssignment#directory_scope_id}
        :param directory_scope_object_id: Identifier of the directory object representing the scope of the assignment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#directory_scope_object_id DirectoryRoleAssignment#directory_scope_object_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#id DirectoryRoleAssignment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#timeouts DirectoryRoleAssignment#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DirectoryRoleAssignmentTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DirectoryRoleAssignmentConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument principal_object_id", value=principal_object_id, expected_type=type_hints["principal_object_id"])
            check_type(argname="argument role_id", value=role_id, expected_type=type_hints["role_id"])
            check_type(argname="argument app_scope_id", value=app_scope_id, expected_type=type_hints["app_scope_id"])
            check_type(argname="argument app_scope_object_id", value=app_scope_object_id, expected_type=type_hints["app_scope_object_id"])
            check_type(argname="argument directory_scope_id", value=directory_scope_id, expected_type=type_hints["directory_scope_id"])
            check_type(argname="argument directory_scope_object_id", value=directory_scope_object_id, expected_type=type_hints["directory_scope_object_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "principal_object_id": principal_object_id,
            "role_id": role_id,
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
        if app_scope_id is not None:
            self._values["app_scope_id"] = app_scope_id
        if app_scope_object_id is not None:
            self._values["app_scope_object_id"] = app_scope_object_id
        if directory_scope_id is not None:
            self._values["directory_scope_id"] = directory_scope_id
        if directory_scope_object_id is not None:
            self._values["directory_scope_object_id"] = directory_scope_object_id
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
    def principal_object_id(self) -> builtins.str:
        '''The object ID of the member principal.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#principal_object_id DirectoryRoleAssignment#principal_object_id}
        '''
        result = self._values.get("principal_object_id")
        assert result is not None, "Required property 'principal_object_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_id(self) -> builtins.str:
        '''The object ID of the directory role for this assignment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#role_id DirectoryRoleAssignment#role_id}
        '''
        result = self._values.get("role_id")
        assert result is not None, "Required property 'role_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_scope_id(self) -> typing.Optional[builtins.str]:
        '''Identifier of the app-specific scope when the assignment scope is app-specific.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#app_scope_id DirectoryRoleAssignment#app_scope_id}
        '''
        result = self._values.get("app_scope_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def app_scope_object_id(self) -> typing.Optional[builtins.str]:
        '''Identifier of the app-specific scope when the assignment scope is app-specific.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#app_scope_object_id DirectoryRoleAssignment#app_scope_object_id}
        '''
        result = self._values.get("app_scope_object_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory_scope_id(self) -> typing.Optional[builtins.str]:
        '''Identifier of the directory object representing the scope of the assignment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#directory_scope_id DirectoryRoleAssignment#directory_scope_id}
        '''
        result = self._values.get("directory_scope_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory_scope_object_id(self) -> typing.Optional[builtins.str]:
        '''Identifier of the directory object representing the scope of the assignment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#directory_scope_object_id DirectoryRoleAssignment#directory_scope_object_id}
        '''
        result = self._values.get("directory_scope_object_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#id DirectoryRoleAssignment#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DirectoryRoleAssignmentTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#timeouts DirectoryRoleAssignment#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DirectoryRoleAssignmentTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DirectoryRoleAssignmentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.directoryRoleAssignment.DirectoryRoleAssignmentTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class DirectoryRoleAssignmentTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#create DirectoryRoleAssignment#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#delete DirectoryRoleAssignment#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#read DirectoryRoleAssignment#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#update DirectoryRoleAssignment#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DirectoryRoleAssignmentTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#create DirectoryRoleAssignment#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#delete DirectoryRoleAssignment#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#read DirectoryRoleAssignment#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/r/directory_role_assignment#update DirectoryRoleAssignment#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DirectoryRoleAssignmentTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DirectoryRoleAssignmentTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.directoryRoleAssignment.DirectoryRoleAssignmentTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DirectoryRoleAssignmentTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(DirectoryRoleAssignmentTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DirectoryRoleAssignmentTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DirectoryRoleAssignmentTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DirectoryRoleAssignmentTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DirectoryRoleAssignmentTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DirectoryRoleAssignmentTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DirectoryRoleAssignmentTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DirectoryRoleAssignmentTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DirectoryRoleAssignment",
    "DirectoryRoleAssignmentConfig",
    "DirectoryRoleAssignmentTimeouts",
    "DirectoryRoleAssignmentTimeoutsOutputReference",
]

publication.publish()
