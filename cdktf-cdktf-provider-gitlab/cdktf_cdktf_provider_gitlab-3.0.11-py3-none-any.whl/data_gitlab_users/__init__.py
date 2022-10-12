'''
# `data_gitlab_users`

Refer to the Terraform Registory for docs: [`data_gitlab_users`](https://www.terraform.io/docs/providers/gitlab/d/users).
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


class DataGitlabUsers(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.dataGitlabUsers.DataGitlabUsers",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/d/users gitlab_users}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        active: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        blocked: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        created_after: typing.Optional[builtins.str] = None,
        created_before: typing.Optional[builtins.str] = None,
        extern_provider: typing.Optional[builtins.str] = None,
        extern_uid: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        order_by: typing.Optional[builtins.str] = None,
        search: typing.Optional[builtins.str] = None,
        sort: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/d/users gitlab_users} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param active: Filter users that are active. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#active DataGitlabUsers#active}
        :param blocked: Filter users that are blocked. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#blocked DataGitlabUsers#blocked}
        :param created_after: Search for users created after a specific date. (Requires administrator privileges). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#created_after DataGitlabUsers#created_after}
        :param created_before: Search for users created before a specific date. (Requires administrator privileges). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#created_before DataGitlabUsers#created_before}
        :param extern_provider: Lookup users by external provider. (Requires administrator privileges). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#extern_provider DataGitlabUsers#extern_provider}
        :param extern_uid: Lookup users by external UID. (Requires administrator privileges). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#extern_uid DataGitlabUsers#extern_uid}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#id DataGitlabUsers#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param order_by: Order the users' list by ``id``, ``name``, ``username``, ``created_at`` or ``updated_at``. (Requires administrator privileges). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#order_by DataGitlabUsers#order_by}
        :param search: Search users by username, name or email. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#search DataGitlabUsers#search}
        :param sort: Sort users' list in asc or desc order. (Requires administrator privileges). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#sort DataGitlabUsers#sort}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGitlabUsers.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataGitlabUsersConfig(
            active=active,
            blocked=blocked,
            created_after=created_after,
            created_before=created_before,
            extern_provider=extern_provider,
            extern_uid=extern_uid,
            id=id,
            order_by=order_by,
            search=search,
            sort=sort,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetActive")
    def reset_active(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActive", []))

    @jsii.member(jsii_name="resetBlocked")
    def reset_blocked(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlocked", []))

    @jsii.member(jsii_name="resetCreatedAfter")
    def reset_created_after(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreatedAfter", []))

    @jsii.member(jsii_name="resetCreatedBefore")
    def reset_created_before(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreatedBefore", []))

    @jsii.member(jsii_name="resetExternProvider")
    def reset_extern_provider(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternProvider", []))

    @jsii.member(jsii_name="resetExternUid")
    def reset_extern_uid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternUid", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOrderBy")
    def reset_order_by(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrderBy", []))

    @jsii.member(jsii_name="resetSearch")
    def reset_search(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearch", []))

    @jsii.member(jsii_name="resetSort")
    def reset_sort(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSort", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="users")
    def users(self) -> "DataGitlabUsersUsersList":
        return typing.cast("DataGitlabUsersUsersList", jsii.get(self, "users"))

    @builtins.property
    @jsii.member(jsii_name="activeInput")
    def active_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "activeInput"))

    @builtins.property
    @jsii.member(jsii_name="blockedInput")
    def blocked_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "blockedInput"))

    @builtins.property
    @jsii.member(jsii_name="createdAfterInput")
    def created_after_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createdAfterInput"))

    @builtins.property
    @jsii.member(jsii_name="createdBeforeInput")
    def created_before_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createdBeforeInput"))

    @builtins.property
    @jsii.member(jsii_name="externProviderInput")
    def extern_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="externUidInput")
    def extern_uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externUidInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="orderByInput")
    def order_by_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "orderByInput"))

    @builtins.property
    @jsii.member(jsii_name="searchInput")
    def search_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "searchInput"))

    @builtins.property
    @jsii.member(jsii_name="sortInput")
    def sort_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sortInput"))

    @builtins.property
    @jsii.member(jsii_name="active")
    def active(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "active"))

    @active.setter
    def active(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabUsers, "active").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "active", value)

    @builtins.property
    @jsii.member(jsii_name="blocked")
    def blocked(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "blocked"))

    @blocked.setter
    def blocked(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabUsers, "blocked").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blocked", value)

    @builtins.property
    @jsii.member(jsii_name="createdAfter")
    def created_after(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAfter"))

    @created_after.setter
    def created_after(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabUsers, "created_after").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createdAfter", value)

    @builtins.property
    @jsii.member(jsii_name="createdBefore")
    def created_before(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdBefore"))

    @created_before.setter
    def created_before(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabUsers, "created_before").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createdBefore", value)

    @builtins.property
    @jsii.member(jsii_name="externProvider")
    def extern_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externProvider"))

    @extern_provider.setter
    def extern_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabUsers, "extern_provider").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externProvider", value)

    @builtins.property
    @jsii.member(jsii_name="externUid")
    def extern_uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externUid"))

    @extern_uid.setter
    def extern_uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabUsers, "extern_uid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externUid", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabUsers, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="orderBy")
    def order_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "orderBy"))

    @order_by.setter
    def order_by(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabUsers, "order_by").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "orderBy", value)

    @builtins.property
    @jsii.member(jsii_name="search")
    def search(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "search"))

    @search.setter
    def search(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabUsers, "search").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "search", value)

    @builtins.property
    @jsii.member(jsii_name="sort")
    def sort(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sort"))

    @sort.setter
    def sort(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabUsers, "sort").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sort", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.dataGitlabUsers.DataGitlabUsersConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "active": "active",
        "blocked": "blocked",
        "created_after": "createdAfter",
        "created_before": "createdBefore",
        "extern_provider": "externProvider",
        "extern_uid": "externUid",
        "id": "id",
        "order_by": "orderBy",
        "search": "search",
        "sort": "sort",
    },
)
class DataGitlabUsersConfig(cdktf.TerraformMetaArguments):
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
        active: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        blocked: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        created_after: typing.Optional[builtins.str] = None,
        created_before: typing.Optional[builtins.str] = None,
        extern_provider: typing.Optional[builtins.str] = None,
        extern_uid: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        order_by: typing.Optional[builtins.str] = None,
        search: typing.Optional[builtins.str] = None,
        sort: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param active: Filter users that are active. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#active DataGitlabUsers#active}
        :param blocked: Filter users that are blocked. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#blocked DataGitlabUsers#blocked}
        :param created_after: Search for users created after a specific date. (Requires administrator privileges). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#created_after DataGitlabUsers#created_after}
        :param created_before: Search for users created before a specific date. (Requires administrator privileges). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#created_before DataGitlabUsers#created_before}
        :param extern_provider: Lookup users by external provider. (Requires administrator privileges). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#extern_provider DataGitlabUsers#extern_provider}
        :param extern_uid: Lookup users by external UID. (Requires administrator privileges). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#extern_uid DataGitlabUsers#extern_uid}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#id DataGitlabUsers#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param order_by: Order the users' list by ``id``, ``name``, ``username``, ``created_at`` or ``updated_at``. (Requires administrator privileges). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#order_by DataGitlabUsers#order_by}
        :param search: Search users by username, name or email. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#search DataGitlabUsers#search}
        :param sort: Sort users' list in asc or desc order. (Requires administrator privileges). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#sort DataGitlabUsers#sort}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataGitlabUsersConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument active", value=active, expected_type=type_hints["active"])
            check_type(argname="argument blocked", value=blocked, expected_type=type_hints["blocked"])
            check_type(argname="argument created_after", value=created_after, expected_type=type_hints["created_after"])
            check_type(argname="argument created_before", value=created_before, expected_type=type_hints["created_before"])
            check_type(argname="argument extern_provider", value=extern_provider, expected_type=type_hints["extern_provider"])
            check_type(argname="argument extern_uid", value=extern_uid, expected_type=type_hints["extern_uid"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument order_by", value=order_by, expected_type=type_hints["order_by"])
            check_type(argname="argument search", value=search, expected_type=type_hints["search"])
            check_type(argname="argument sort", value=sort, expected_type=type_hints["sort"])
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
        if active is not None:
            self._values["active"] = active
        if blocked is not None:
            self._values["blocked"] = blocked
        if created_after is not None:
            self._values["created_after"] = created_after
        if created_before is not None:
            self._values["created_before"] = created_before
        if extern_provider is not None:
            self._values["extern_provider"] = extern_provider
        if extern_uid is not None:
            self._values["extern_uid"] = extern_uid
        if id is not None:
            self._values["id"] = id
        if order_by is not None:
            self._values["order_by"] = order_by
        if search is not None:
            self._values["search"] = search
        if sort is not None:
            self._values["sort"] = sort

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
    def active(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Filter users that are active.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#active DataGitlabUsers#active}
        '''
        result = self._values.get("active")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def blocked(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Filter users that are blocked.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#blocked DataGitlabUsers#blocked}
        '''
        result = self._values.get("blocked")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def created_after(self) -> typing.Optional[builtins.str]:
        '''Search for users created after a specific date. (Requires administrator privileges).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#created_after DataGitlabUsers#created_after}
        '''
        result = self._values.get("created_after")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def created_before(self) -> typing.Optional[builtins.str]:
        '''Search for users created before a specific date. (Requires administrator privileges).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#created_before DataGitlabUsers#created_before}
        '''
        result = self._values.get("created_before")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extern_provider(self) -> typing.Optional[builtins.str]:
        '''Lookup users by external provider. (Requires administrator privileges).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#extern_provider DataGitlabUsers#extern_provider}
        '''
        result = self._values.get("extern_provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extern_uid(self) -> typing.Optional[builtins.str]:
        '''Lookup users by external UID. (Requires administrator privileges).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#extern_uid DataGitlabUsers#extern_uid}
        '''
        result = self._values.get("extern_uid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#id DataGitlabUsers#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def order_by(self) -> typing.Optional[builtins.str]:
        '''Order the users' list by ``id``, ``name``, ``username``, ``created_at`` or ``updated_at``. (Requires administrator privileges).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#order_by DataGitlabUsers#order_by}
        '''
        result = self._values.get("order_by")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def search(self) -> typing.Optional[builtins.str]:
        '''Search users by username, name or email.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#search DataGitlabUsers#search}
        '''
        result = self._values.get("search")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sort(self) -> typing.Optional[builtins.str]:
        '''Sort users' list in asc or desc order. (Requires administrator privileges).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/users#sort DataGitlabUsers#sort}
        '''
        result = self._values.get("sort")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGitlabUsersConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.dataGitlabUsers.DataGitlabUsersUsers",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGitlabUsersUsers:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGitlabUsersUsers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGitlabUsersUsersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.dataGitlabUsers.DataGitlabUsersUsersList",
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
            type_hints = typing.get_type_hints(DataGitlabUsersUsersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataGitlabUsersUsersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGitlabUsersUsersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGitlabUsersUsersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabUsersUsersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGitlabUsersUsersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGitlabUsersUsersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGitlabUsersUsersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.dataGitlabUsers.DataGitlabUsersUsersOutputReference",
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
            type_hints = typing.get_type_hints(DataGitlabUsersUsersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="avatarUrl")
    def avatar_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "avatarUrl"))

    @builtins.property
    @jsii.member(jsii_name="bio")
    def bio(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bio"))

    @builtins.property
    @jsii.member(jsii_name="canCreateGroup")
    def can_create_group(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "canCreateGroup"))

    @builtins.property
    @jsii.member(jsii_name="canCreateProject")
    def can_create_project(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "canCreateProject"))

    @builtins.property
    @jsii.member(jsii_name="colorSchemeId")
    def color_scheme_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "colorSchemeId"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="currentSignInAt")
    def current_sign_in_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "currentSignInAt"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @builtins.property
    @jsii.member(jsii_name="external")
    def external(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "external"))

    @builtins.property
    @jsii.member(jsii_name="externUid")
    def extern_uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externUid"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="isAdmin")
    def is_admin(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "isAdmin"))

    @builtins.property
    @jsii.member(jsii_name="lastSignInAt")
    def last_sign_in_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastSignInAt"))

    @builtins.property
    @jsii.member(jsii_name="linkedin")
    def linkedin(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "linkedin"))

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "namespaceId"))

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @builtins.property
    @jsii.member(jsii_name="projectsLimit")
    def projects_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "projectsLimit"))

    @builtins.property
    @jsii.member(jsii_name="provider")
    def provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "provider"))

    @builtins.property
    @jsii.member(jsii_name="skype")
    def skype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skype"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="themeId")
    def theme_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "themeId"))

    @builtins.property
    @jsii.member(jsii_name="twitter")
    def twitter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "twitter"))

    @builtins.property
    @jsii.member(jsii_name="twoFactorEnabled")
    def two_factor_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "twoFactorEnabled"))

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @builtins.property
    @jsii.member(jsii_name="websiteUrl")
    def website_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "websiteUrl"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataGitlabUsersUsers]:
        return typing.cast(typing.Optional[DataGitlabUsersUsers], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DataGitlabUsersUsers]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabUsersUsersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataGitlabUsers",
    "DataGitlabUsersConfig",
    "DataGitlabUsersUsers",
    "DataGitlabUsersUsersList",
    "DataGitlabUsersUsersOutputReference",
]

publication.publish()
