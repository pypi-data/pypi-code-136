'''
# `gitlab_group_membership`

Refer to the Terraform Registory for docs: [`gitlab_group_membership`](https://www.terraform.io/docs/providers/gitlab/r/group_membership).
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


class GroupMembership(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.groupMembership.GroupMembership",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership gitlab_group_membership}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        access_level: builtins.str,
        group_id: builtins.str,
        user_id: jsii.Number,
        expires_at: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        skip_subresources_on_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        unassign_issuables_on_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership gitlab_group_membership} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param access_level: Access level for the member. Valid values are: ``no one``, ``minimal``, ``guest``, ``reporter``, ``developer``, ``maintainer``, ``owner``, ``master``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#access_level GroupMembership#access_level}
        :param group_id: The id of the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#group_id GroupMembership#group_id}
        :param user_id: The id of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#user_id GroupMembership#user_id}
        :param expires_at: Expiration date for the group membership. Format: ``YYYY-MM-DD``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#expires_at GroupMembership#expires_at}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#id GroupMembership#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param skip_subresources_on_destroy: Whether the deletion of direct memberships of the removed member in subgroups and projects should be skipped. Only used during a destroy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#skip_subresources_on_destroy GroupMembership#skip_subresources_on_destroy}
        :param unassign_issuables_on_destroy: Whether the removed member should be unassigned from any issues or merge requests inside a given group or project. Only used during a destroy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#unassign_issuables_on_destroy GroupMembership#unassign_issuables_on_destroy}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GroupMembership.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GroupMembershipConfig(
            access_level=access_level,
            group_id=group_id,
            user_id=user_id,
            expires_at=expires_at,
            id=id,
            skip_subresources_on_destroy=skip_subresources_on_destroy,
            unassign_issuables_on_destroy=unassign_issuables_on_destroy,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetExpiresAt")
    def reset_expires_at(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpiresAt", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSkipSubresourcesOnDestroy")
    def reset_skip_subresources_on_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipSubresourcesOnDestroy", []))

    @jsii.member(jsii_name="resetUnassignIssuablesOnDestroy")
    def reset_unassign_issuables_on_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnassignIssuablesOnDestroy", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accessLevelInput")
    def access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="expiresAtInput")
    def expires_at_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expiresAtInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="skipSubresourcesOnDestroyInput")
    def skip_subresources_on_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipSubresourcesOnDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="unassignIssuablesOnDestroyInput")
    def unassign_issuables_on_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "unassignIssuablesOnDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="userIdInput")
    def user_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "userIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accessLevel")
    def access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessLevel"))

    @access_level.setter
    def access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupMembership, "access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="expiresAt")
    def expires_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiresAt"))

    @expires_at.setter
    def expires_at(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupMembership, "expires_at").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiresAt", value)

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupMembership, "group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupMembership, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="skipSubresourcesOnDestroy")
    def skip_subresources_on_destroy(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "skipSubresourcesOnDestroy"))

    @skip_subresources_on_destroy.setter
    def skip_subresources_on_destroy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupMembership, "skip_subresources_on_destroy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipSubresourcesOnDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="unassignIssuablesOnDestroy")
    def unassign_issuables_on_destroy(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "unassignIssuablesOnDestroy"))

    @unassign_issuables_on_destroy.setter
    def unassign_issuables_on_destroy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupMembership, "unassign_issuables_on_destroy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unassignIssuablesOnDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="userId")
    def user_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "userId"))

    @user_id.setter
    def user_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupMembership, "user_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.groupMembership.GroupMembershipConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "access_level": "accessLevel",
        "group_id": "groupId",
        "user_id": "userId",
        "expires_at": "expiresAt",
        "id": "id",
        "skip_subresources_on_destroy": "skipSubresourcesOnDestroy",
        "unassign_issuables_on_destroy": "unassignIssuablesOnDestroy",
    },
)
class GroupMembershipConfig(cdktf.TerraformMetaArguments):
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
        access_level: builtins.str,
        group_id: builtins.str,
        user_id: jsii.Number,
        expires_at: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        skip_subresources_on_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        unassign_issuables_on_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param access_level: Access level for the member. Valid values are: ``no one``, ``minimal``, ``guest``, ``reporter``, ``developer``, ``maintainer``, ``owner``, ``master``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#access_level GroupMembership#access_level}
        :param group_id: The id of the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#group_id GroupMembership#group_id}
        :param user_id: The id of the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#user_id GroupMembership#user_id}
        :param expires_at: Expiration date for the group membership. Format: ``YYYY-MM-DD``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#expires_at GroupMembership#expires_at}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#id GroupMembership#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param skip_subresources_on_destroy: Whether the deletion of direct memberships of the removed member in subgroups and projects should be skipped. Only used during a destroy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#skip_subresources_on_destroy GroupMembership#skip_subresources_on_destroy}
        :param unassign_issuables_on_destroy: Whether the removed member should be unassigned from any issues or merge requests inside a given group or project. Only used during a destroy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#unassign_issuables_on_destroy GroupMembership#unassign_issuables_on_destroy}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(GroupMembershipConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument access_level", value=access_level, expected_type=type_hints["access_level"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
            check_type(argname="argument expires_at", value=expires_at, expected_type=type_hints["expires_at"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument skip_subresources_on_destroy", value=skip_subresources_on_destroy, expected_type=type_hints["skip_subresources_on_destroy"])
            check_type(argname="argument unassign_issuables_on_destroy", value=unassign_issuables_on_destroy, expected_type=type_hints["unassign_issuables_on_destroy"])
        self._values: typing.Dict[str, typing.Any] = {
            "access_level": access_level,
            "group_id": group_id,
            "user_id": user_id,
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
        if expires_at is not None:
            self._values["expires_at"] = expires_at
        if id is not None:
            self._values["id"] = id
        if skip_subresources_on_destroy is not None:
            self._values["skip_subresources_on_destroy"] = skip_subresources_on_destroy
        if unassign_issuables_on_destroy is not None:
            self._values["unassign_issuables_on_destroy"] = unassign_issuables_on_destroy

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
    def access_level(self) -> builtins.str:
        '''Access level for the member. Valid values are: ``no one``, ``minimal``, ``guest``, ``reporter``, ``developer``, ``maintainer``, ``owner``, ``master``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#access_level GroupMembership#access_level}
        '''
        result = self._values.get("access_level")
        assert result is not None, "Required property 'access_level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_id(self) -> builtins.str:
        '''The id of the group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#group_id GroupMembership#group_id}
        '''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_id(self) -> jsii.Number:
        '''The id of the user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#user_id GroupMembership#user_id}
        '''
        result = self._values.get("user_id")
        assert result is not None, "Required property 'user_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def expires_at(self) -> typing.Optional[builtins.str]:
        '''Expiration date for the group membership. Format: ``YYYY-MM-DD``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#expires_at GroupMembership#expires_at}
        '''
        result = self._values.get("expires_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#id GroupMembership#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_subresources_on_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the deletion of direct memberships of the removed member in subgroups and projects should be skipped.

        Only used during a destroy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#skip_subresources_on_destroy GroupMembership#skip_subresources_on_destroy}
        '''
        result = self._values.get("skip_subresources_on_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def unassign_issuables_on_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the removed member should be unassigned from any issues or merge requests inside a given group or project.

        Only used during a destroy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_membership#unassign_issuables_on_destroy GroupMembership#unassign_issuables_on_destroy}
        '''
        result = self._values.get("unassign_issuables_on_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupMembershipConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GroupMembership",
    "GroupMembershipConfig",
]

publication.publish()
