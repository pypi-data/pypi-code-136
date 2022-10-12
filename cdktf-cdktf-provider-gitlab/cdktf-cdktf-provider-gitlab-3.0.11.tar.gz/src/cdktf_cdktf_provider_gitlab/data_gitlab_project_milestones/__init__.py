'''
# `data_gitlab_project_milestones`

Refer to the Terraform Registory for docs: [`data_gitlab_project_milestones`](https://www.terraform.io/docs/providers/gitlab/d/project_milestones).
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


class DataGitlabProjectMilestones(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.dataGitlabProjectMilestones.DataGitlabProjectMilestones",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones gitlab_project_milestones}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        project: builtins.str,
        id: typing.Optional[builtins.str] = None,
        iids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        include_parent_milestones: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        search: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones gitlab_project_milestones} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param project: The ID or URL-encoded path of the project owned by the authenticated user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#project DataGitlabProjectMilestones#project}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#id DataGitlabProjectMilestones#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param iids: Return only the milestones having the given ``iid`` (Note: ignored if ``include_parent_milestones`` is set as ``true``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#iids DataGitlabProjectMilestones#iids}
        :param include_parent_milestones: Include group milestones from parent group and its ancestors. Introduced in GitLab 13.4. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#include_parent_milestones DataGitlabProjectMilestones#include_parent_milestones}
        :param search: Return only milestones with a title or description matching the provided string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#search DataGitlabProjectMilestones#search}
        :param state: Return only ``active`` or ``closed`` milestones. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#state DataGitlabProjectMilestones#state}
        :param title: Return only the milestones having the given ``title``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#title DataGitlabProjectMilestones#title}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGitlabProjectMilestones.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataGitlabProjectMilestonesConfig(
            project=project,
            id=id,
            iids=iids,
            include_parent_milestones=include_parent_milestones,
            search=search,
            state=state,
            title=title,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIids")
    def reset_iids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIids", []))

    @jsii.member(jsii_name="resetIncludeParentMilestones")
    def reset_include_parent_milestones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeParentMilestones", []))

    @jsii.member(jsii_name="resetSearch")
    def reset_search(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearch", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="milestones")
    def milestones(self) -> "DataGitlabProjectMilestonesMilestonesList":
        return typing.cast("DataGitlabProjectMilestonesMilestonesList", jsii.get(self, "milestones"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="iidsInput")
    def iids_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "iidsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeParentMilestonesInput")
    def include_parent_milestones_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeParentMilestonesInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="searchInput")
    def search_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "searchInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectMilestones, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="iids")
    def iids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "iids"))

    @iids.setter
    def iids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectMilestones, "iids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iids", value)

    @builtins.property
    @jsii.member(jsii_name="includeParentMilestones")
    def include_parent_milestones(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeParentMilestones"))

    @include_parent_milestones.setter
    def include_parent_milestones(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectMilestones, "include_parent_milestones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeParentMilestones", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectMilestones, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="search")
    def search(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "search"))

    @search.setter
    def search(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectMilestones, "search").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "search", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectMilestones, "state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectMilestones, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.dataGitlabProjectMilestones.DataGitlabProjectMilestonesConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "project": "project",
        "id": "id",
        "iids": "iids",
        "include_parent_milestones": "includeParentMilestones",
        "search": "search",
        "state": "state",
        "title": "title",
    },
)
class DataGitlabProjectMilestonesConfig(cdktf.TerraformMetaArguments):
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
        project: builtins.str,
        id: typing.Optional[builtins.str] = None,
        iids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        include_parent_milestones: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        search: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param project: The ID or URL-encoded path of the project owned by the authenticated user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#project DataGitlabProjectMilestones#project}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#id DataGitlabProjectMilestones#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param iids: Return only the milestones having the given ``iid`` (Note: ignored if ``include_parent_milestones`` is set as ``true``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#iids DataGitlabProjectMilestones#iids}
        :param include_parent_milestones: Include group milestones from parent group and its ancestors. Introduced in GitLab 13.4. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#include_parent_milestones DataGitlabProjectMilestones#include_parent_milestones}
        :param search: Return only milestones with a title or description matching the provided string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#search DataGitlabProjectMilestones#search}
        :param state: Return only ``active`` or ``closed`` milestones. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#state DataGitlabProjectMilestones#state}
        :param title: Return only the milestones having the given ``title``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#title DataGitlabProjectMilestones#title}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataGitlabProjectMilestonesConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument iids", value=iids, expected_type=type_hints["iids"])
            check_type(argname="argument include_parent_milestones", value=include_parent_milestones, expected_type=type_hints["include_parent_milestones"])
            check_type(argname="argument search", value=search, expected_type=type_hints["search"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[str, typing.Any] = {
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
        if id is not None:
            self._values["id"] = id
        if iids is not None:
            self._values["iids"] = iids
        if include_parent_milestones is not None:
            self._values["include_parent_milestones"] = include_parent_milestones
        if search is not None:
            self._values["search"] = search
        if state is not None:
            self._values["state"] = state
        if title is not None:
            self._values["title"] = title

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
    def project(self) -> builtins.str:
        '''The ID or URL-encoded path of the project owned by the authenticated user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#project DataGitlabProjectMilestones#project}
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#id DataGitlabProjectMilestones#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iids(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Return only the milestones having the given ``iid`` (Note: ignored if ``include_parent_milestones`` is set as ``true``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#iids DataGitlabProjectMilestones#iids}
        '''
        result = self._values.get("iids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def include_parent_milestones(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Include group milestones from parent group and its ancestors. Introduced in GitLab 13.4.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#include_parent_milestones DataGitlabProjectMilestones#include_parent_milestones}
        '''
        result = self._values.get("include_parent_milestones")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def search(self) -> typing.Optional[builtins.str]:
        '''Return only milestones with a title or description matching the provided string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#search DataGitlabProjectMilestones#search}
        '''
        result = self._values.get("search")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Return only ``active`` or ``closed`` milestones.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#state DataGitlabProjectMilestones#state}
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Return only the milestones having the given ``title``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_milestones#title DataGitlabProjectMilestones#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGitlabProjectMilestonesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.dataGitlabProjectMilestones.DataGitlabProjectMilestonesMilestones",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGitlabProjectMilestonesMilestones:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGitlabProjectMilestonesMilestones(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGitlabProjectMilestonesMilestonesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.dataGitlabProjectMilestones.DataGitlabProjectMilestonesMilestonesList",
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
            type_hints = typing.get_type_hints(DataGitlabProjectMilestonesMilestonesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGitlabProjectMilestonesMilestonesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGitlabProjectMilestonesMilestonesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGitlabProjectMilestonesMilestonesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectMilestonesMilestonesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectMilestonesMilestonesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectMilestonesMilestonesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGitlabProjectMilestonesMilestonesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.dataGitlabProjectMilestones.DataGitlabProjectMilestonesMilestonesOutputReference",
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
            type_hints = typing.get_type_hints(DataGitlabProjectMilestonesMilestonesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="dueDate")
    def due_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dueDate"))

    @builtins.property
    @jsii.member(jsii_name="expired")
    def expired(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "expired"))

    @builtins.property
    @jsii.member(jsii_name="iid")
    def iid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iid"))

    @builtins.property
    @jsii.member(jsii_name="milestoneId")
    def milestone_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "milestoneId"))

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "projectId"))

    @builtins.property
    @jsii.member(jsii_name="startDate")
    def start_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startDate"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @builtins.property
    @jsii.member(jsii_name="updatedAt")
    def updated_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedAt"))

    @builtins.property
    @jsii.member(jsii_name="webUrl")
    def web_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webUrl"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataGitlabProjectMilestonesMilestones]:
        return typing.cast(typing.Optional[DataGitlabProjectMilestonesMilestones], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGitlabProjectMilestonesMilestones],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectMilestonesMilestonesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataGitlabProjectMilestones",
    "DataGitlabProjectMilestonesConfig",
    "DataGitlabProjectMilestonesMilestones",
    "DataGitlabProjectMilestonesMilestonesList",
    "DataGitlabProjectMilestonesMilestonesOutputReference",
]

publication.publish()
