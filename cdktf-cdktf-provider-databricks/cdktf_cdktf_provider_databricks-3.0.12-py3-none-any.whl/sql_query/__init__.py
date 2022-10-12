'''
# `databricks_sql_query`

Refer to the Terraform Registory for docs: [`databricks_sql_query`](https://www.terraform.io/docs/providers/databricks/r/sql_query).
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


class SqlQuery(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQuery",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/sql_query databricks_sql_query}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        data_source_id: builtins.str,
        name: builtins.str,
        query: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SqlQueryParameter", typing.Dict[str, typing.Any]]]]] = None,
        run_as_role: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[typing.Union["SqlQuerySchedule", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/sql_query databricks_sql_query} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_source_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#data_source_id SqlQuery#data_source_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#name SqlQuery#name}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#query SqlQuery#query}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#description SqlQuery#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#id SqlQuery#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#parameter SqlQuery#parameter}
        :param run_as_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#run_as_role SqlQuery#run_as_role}.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#schedule SqlQuery#schedule}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#tags SqlQuery#tags}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlQuery.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SqlQueryConfig(
            data_source_id=data_source_id,
            name=name,
            query=query,
            description=description,
            id=id,
            parameter=parameter,
            run_as_role=run_as_role,
            schedule=schedule,
            tags=tags,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putParameter")
    def put_parameter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SqlQueryParameter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlQuery.put_parameter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameter", [value]))

    @jsii.member(jsii_name="putSchedule")
    def put_schedule(
        self,
        *,
        continuous: typing.Optional[typing.Union["SqlQueryScheduleContinuous", typing.Dict[str, typing.Any]]] = None,
        daily: typing.Optional[typing.Union["SqlQueryScheduleDaily", typing.Dict[str, typing.Any]]] = None,
        weekly: typing.Optional[typing.Union["SqlQueryScheduleWeekly", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param continuous: continuous block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#continuous SqlQuery#continuous}
        :param daily: daily block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#daily SqlQuery#daily}
        :param weekly: weekly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#weekly SqlQuery#weekly}
        '''
        value = SqlQuerySchedule(continuous=continuous, daily=daily, weekly=weekly)

        return typing.cast(None, jsii.invoke(self, "putSchedule", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetParameter")
    def reset_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameter", []))

    @jsii.member(jsii_name="resetRunAsRole")
    def reset_run_as_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunAsRole", []))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(self) -> "SqlQueryParameterList":
        return typing.cast("SqlQueryParameterList", jsii.get(self, "parameter"))

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> "SqlQueryScheduleOutputReference":
        return typing.cast("SqlQueryScheduleOutputReference", jsii.get(self, "schedule"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceIdInput")
    def data_source_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SqlQueryParameter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SqlQueryParameter"]]], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="runAsRoleInput")
    def run_as_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runAsRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional["SqlQuerySchedule"]:
        return typing.cast(typing.Optional["SqlQuerySchedule"], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceId")
    def data_source_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSourceId"))

    @data_source_id.setter
    def data_source_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQuery, "data_source_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSourceId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQuery, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQuery, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQuery, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQuery, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="runAsRole")
    def run_as_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runAsRole"))

    @run_as_role.setter
    def run_as_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQuery, "run_as_role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runAsRole", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQuery, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "data_source_id": "dataSourceId",
        "name": "name",
        "query": "query",
        "description": "description",
        "id": "id",
        "parameter": "parameter",
        "run_as_role": "runAsRole",
        "schedule": "schedule",
        "tags": "tags",
    },
)
class SqlQueryConfig(cdktf.TerraformMetaArguments):
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
        data_source_id: builtins.str,
        name: builtins.str,
        query: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SqlQueryParameter", typing.Dict[str, typing.Any]]]]] = None,
        run_as_role: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[typing.Union["SqlQuerySchedule", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_source_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#data_source_id SqlQuery#data_source_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#name SqlQuery#name}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#query SqlQuery#query}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#description SqlQuery#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#id SqlQuery#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#parameter SqlQuery#parameter}
        :param run_as_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#run_as_role SqlQuery#run_as_role}.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#schedule SqlQuery#schedule}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#tags SqlQuery#tags}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(schedule, dict):
            schedule = SqlQuerySchedule(**schedule)
        if __debug__:
            type_hints = typing.get_type_hints(SqlQueryConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument data_source_id", value=data_source_id, expected_type=type_hints["data_source_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
            check_type(argname="argument run_as_role", value=run_as_role, expected_type=type_hints["run_as_role"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "data_source_id": data_source_id,
            "name": name,
            "query": query,
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
        if id is not None:
            self._values["id"] = id
        if parameter is not None:
            self._values["parameter"] = parameter
        if run_as_role is not None:
            self._values["run_as_role"] = run_as_role
        if schedule is not None:
            self._values["schedule"] = schedule
        if tags is not None:
            self._values["tags"] = tags

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
    def data_source_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#data_source_id SqlQuery#data_source_id}.'''
        result = self._values.get("data_source_id")
        assert result is not None, "Required property 'data_source_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#name SqlQuery#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#query SqlQuery#query}.'''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#description SqlQuery#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#id SqlQuery#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SqlQueryParameter"]]]:
        '''parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#parameter SqlQuery#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SqlQueryParameter"]]], result)

    @builtins.property
    def run_as_role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#run_as_role SqlQuery#run_as_role}.'''
        result = self._values.get("run_as_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule(self) -> typing.Optional["SqlQuerySchedule"]:
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#schedule SqlQuery#schedule}
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional["SqlQuerySchedule"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#tags SqlQuery#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameter",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "date": "date",
        "date_range": "dateRange",
        "datetime": "datetime",
        "datetime_range": "datetimeRange",
        "datetimesec": "datetimesec",
        "datetimesec_range": "datetimesecRange",
        "enum": "enum",
        "number": "number",
        "query": "query",
        "text": "text",
        "title": "title",
    },
)
class SqlQueryParameter:
    def __init__(
        self,
        *,
        name: builtins.str,
        date: typing.Optional[typing.Union["SqlQueryParameterDate", typing.Dict[str, typing.Any]]] = None,
        date_range: typing.Optional[typing.Union["SqlQueryParameterDateRange", typing.Dict[str, typing.Any]]] = None,
        datetime: typing.Optional[typing.Union["SqlQueryParameterDatetime", typing.Dict[str, typing.Any]]] = None,
        datetime_range: typing.Optional[typing.Union["SqlQueryParameterDatetimeRange", typing.Dict[str, typing.Any]]] = None,
        datetimesec: typing.Optional[typing.Union["SqlQueryParameterDatetimesec", typing.Dict[str, typing.Any]]] = None,
        datetimesec_range: typing.Optional[typing.Union["SqlQueryParameterDatetimesecRange", typing.Dict[str, typing.Any]]] = None,
        enum: typing.Optional[typing.Union["SqlQueryParameterEnum", typing.Dict[str, typing.Any]]] = None,
        number: typing.Optional[typing.Union["SqlQueryParameterNumber", typing.Dict[str, typing.Any]]] = None,
        query: typing.Optional[typing.Union["SqlQueryParameterQuery", typing.Dict[str, typing.Any]]] = None,
        text: typing.Optional[typing.Union["SqlQueryParameterText", typing.Dict[str, typing.Any]]] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#name SqlQuery#name}.
        :param date: date block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#date SqlQuery#date}
        :param date_range: date_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#date_range SqlQuery#date_range}
        :param datetime: datetime block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#datetime SqlQuery#datetime}
        :param datetime_range: datetime_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#datetime_range SqlQuery#datetime_range}
        :param datetimesec: datetimesec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#datetimesec SqlQuery#datetimesec}
        :param datetimesec_range: datetimesec_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#datetimesec_range SqlQuery#datetimesec_range}
        :param enum: enum block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#enum SqlQuery#enum}
        :param number: number block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#number SqlQuery#number}
        :param query: query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#query SqlQuery#query}
        :param text: text block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#text SqlQuery#text}
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#title SqlQuery#title}.
        '''
        if isinstance(date, dict):
            date = SqlQueryParameterDate(**date)
        if isinstance(date_range, dict):
            date_range = SqlQueryParameterDateRange(**date_range)
        if isinstance(datetime, dict):
            datetime = SqlQueryParameterDatetime(**datetime)
        if isinstance(datetime_range, dict):
            datetime_range = SqlQueryParameterDatetimeRange(**datetime_range)
        if isinstance(datetimesec, dict):
            datetimesec = SqlQueryParameterDatetimesec(**datetimesec)
        if isinstance(datetimesec_range, dict):
            datetimesec_range = SqlQueryParameterDatetimesecRange(**datetimesec_range)
        if isinstance(enum, dict):
            enum = SqlQueryParameterEnum(**enum)
        if isinstance(number, dict):
            number = SqlQueryParameterNumber(**number)
        if isinstance(query, dict):
            query = SqlQueryParameterQuery(**query)
        if isinstance(text, dict):
            text = SqlQueryParameterText(**text)
        if __debug__:
            type_hints = typing.get_type_hints(SqlQueryParameter.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument date", value=date, expected_type=type_hints["date"])
            check_type(argname="argument date_range", value=date_range, expected_type=type_hints["date_range"])
            check_type(argname="argument datetime", value=datetime, expected_type=type_hints["datetime"])
            check_type(argname="argument datetime_range", value=datetime_range, expected_type=type_hints["datetime_range"])
            check_type(argname="argument datetimesec", value=datetimesec, expected_type=type_hints["datetimesec"])
            check_type(argname="argument datetimesec_range", value=datetimesec_range, expected_type=type_hints["datetimesec_range"])
            check_type(argname="argument enum", value=enum, expected_type=type_hints["enum"])
            check_type(argname="argument number", value=number, expected_type=type_hints["number"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if date is not None:
            self._values["date"] = date
        if date_range is not None:
            self._values["date_range"] = date_range
        if datetime is not None:
            self._values["datetime"] = datetime
        if datetime_range is not None:
            self._values["datetime_range"] = datetime_range
        if datetimesec is not None:
            self._values["datetimesec"] = datetimesec
        if datetimesec_range is not None:
            self._values["datetimesec_range"] = datetimesec_range
        if enum is not None:
            self._values["enum"] = enum
        if number is not None:
            self._values["number"] = number
        if query is not None:
            self._values["query"] = query
        if text is not None:
            self._values["text"] = text
        if title is not None:
            self._values["title"] = title

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#name SqlQuery#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def date(self) -> typing.Optional["SqlQueryParameterDate"]:
        '''date block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#date SqlQuery#date}
        '''
        result = self._values.get("date")
        return typing.cast(typing.Optional["SqlQueryParameterDate"], result)

    @builtins.property
    def date_range(self) -> typing.Optional["SqlQueryParameterDateRange"]:
        '''date_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#date_range SqlQuery#date_range}
        '''
        result = self._values.get("date_range")
        return typing.cast(typing.Optional["SqlQueryParameterDateRange"], result)

    @builtins.property
    def datetime(self) -> typing.Optional["SqlQueryParameterDatetime"]:
        '''datetime block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#datetime SqlQuery#datetime}
        '''
        result = self._values.get("datetime")
        return typing.cast(typing.Optional["SqlQueryParameterDatetime"], result)

    @builtins.property
    def datetime_range(self) -> typing.Optional["SqlQueryParameterDatetimeRange"]:
        '''datetime_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#datetime_range SqlQuery#datetime_range}
        '''
        result = self._values.get("datetime_range")
        return typing.cast(typing.Optional["SqlQueryParameterDatetimeRange"], result)

    @builtins.property
    def datetimesec(self) -> typing.Optional["SqlQueryParameterDatetimesec"]:
        '''datetimesec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#datetimesec SqlQuery#datetimesec}
        '''
        result = self._values.get("datetimesec")
        return typing.cast(typing.Optional["SqlQueryParameterDatetimesec"], result)

    @builtins.property
    def datetimesec_range(self) -> typing.Optional["SqlQueryParameterDatetimesecRange"]:
        '''datetimesec_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#datetimesec_range SqlQuery#datetimesec_range}
        '''
        result = self._values.get("datetimesec_range")
        return typing.cast(typing.Optional["SqlQueryParameterDatetimesecRange"], result)

    @builtins.property
    def enum(self) -> typing.Optional["SqlQueryParameterEnum"]:
        '''enum block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#enum SqlQuery#enum}
        '''
        result = self._values.get("enum")
        return typing.cast(typing.Optional["SqlQueryParameterEnum"], result)

    @builtins.property
    def number(self) -> typing.Optional["SqlQueryParameterNumber"]:
        '''number block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#number SqlQuery#number}
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional["SqlQueryParameterNumber"], result)

    @builtins.property
    def query(self) -> typing.Optional["SqlQueryParameterQuery"]:
        '''query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#query SqlQuery#query}
        '''
        result = self._values.get("query")
        return typing.cast(typing.Optional["SqlQueryParameterQuery"], result)

    @builtins.property
    def text(self) -> typing.Optional["SqlQueryParameterText"]:
        '''text block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#text SqlQuery#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional["SqlQueryParameterText"], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#title SqlQuery#title}.'''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterDate",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class SqlQueryParameterDate:
    def __init__(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlQueryParameterDate.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterDate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterDateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterDateOutputReference",
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
            type_hints = typing.get_type_hints(SqlQueryParameterDateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterDateOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterDate]:
        return typing.cast(typing.Optional[SqlQueryParameterDate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlQueryParameterDate]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterDateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterDateRange",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class SqlQueryParameterDateRange:
    def __init__(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlQueryParameterDateRange.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterDateRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterDateRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterDateRangeOutputReference",
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
            type_hints = typing.get_type_hints(SqlQueryParameterDateRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterDateRangeOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterDateRange]:
        return typing.cast(typing.Optional[SqlQueryParameterDateRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlQueryParameterDateRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterDateRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterDatetime",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class SqlQueryParameterDatetime:
    def __init__(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlQueryParameterDatetime.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterDatetime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterDatetimeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterDatetimeOutputReference",
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
            type_hints = typing.get_type_hints(SqlQueryParameterDatetimeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterDatetimeOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterDatetime]:
        return typing.cast(typing.Optional[SqlQueryParameterDatetime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlQueryParameterDatetime]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterDatetimeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterDatetimeRange",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class SqlQueryParameterDatetimeRange:
    def __init__(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlQueryParameterDatetimeRange.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterDatetimeRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterDatetimeRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterDatetimeRangeOutputReference",
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
            type_hints = typing.get_type_hints(SqlQueryParameterDatetimeRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterDatetimeRangeOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterDatetimeRange]:
        return typing.cast(typing.Optional[SqlQueryParameterDatetimeRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlQueryParameterDatetimeRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterDatetimeRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterDatetimesec",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class SqlQueryParameterDatetimesec:
    def __init__(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlQueryParameterDatetimesec.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterDatetimesec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterDatetimesecOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterDatetimesecOutputReference",
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
            type_hints = typing.get_type_hints(SqlQueryParameterDatetimesecOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterDatetimesecOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterDatetimesec]:
        return typing.cast(typing.Optional[SqlQueryParameterDatetimesec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlQueryParameterDatetimesec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterDatetimesecOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterDatetimesecRange",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class SqlQueryParameterDatetimesecRange:
    def __init__(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlQueryParameterDatetimesecRange.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterDatetimesecRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterDatetimesecRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterDatetimesecRangeOutputReference",
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
            type_hints = typing.get_type_hints(SqlQueryParameterDatetimesecRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterDatetimesecRangeOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterDatetimesecRange]:
        return typing.cast(typing.Optional[SqlQueryParameterDatetimesecRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlQueryParameterDatetimesecRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterDatetimesecRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterEnum",
    jsii_struct_bases=[],
    name_mapping={
        "options": "options",
        "multiple": "multiple",
        "value": "value",
        "values": "values",
    },
)
class SqlQueryParameterEnum:
    def __init__(
        self,
        *,
        options: typing.Sequence[builtins.str],
        multiple: typing.Optional[typing.Union["SqlQueryParameterEnumMultiple", typing.Dict[str, typing.Any]]] = None,
        value: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#options SqlQuery#options}.
        :param multiple: multiple block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#multiple SqlQuery#multiple}
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#values SqlQuery#values}.
        '''
        if isinstance(multiple, dict):
            multiple = SqlQueryParameterEnumMultiple(**multiple)
        if __debug__:
            type_hints = typing.get_type_hints(SqlQueryParameterEnum.__init__)
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument multiple", value=multiple, expected_type=type_hints["multiple"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "options": options,
        }
        if multiple is not None:
            self._values["multiple"] = multiple
        if value is not None:
            self._values["value"] = value
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def options(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#options SqlQuery#options}.'''
        result = self._values.get("options")
        assert result is not None, "Required property 'options' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def multiple(self) -> typing.Optional["SqlQueryParameterEnumMultiple"]:
        '''multiple block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#multiple SqlQuery#multiple}
        '''
        result = self._values.get("multiple")
        return typing.cast(typing.Optional["SqlQueryParameterEnumMultiple"], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#values SqlQuery#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterEnum(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterEnumMultiple",
    jsii_struct_bases=[],
    name_mapping={"prefix": "prefix", "separator": "separator", "suffix": "suffix"},
)
class SqlQueryParameterEnumMultiple:
    def __init__(
        self,
        *,
        prefix: builtins.str,
        separator: builtins.str,
        suffix: builtins.str,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#prefix SqlQuery#prefix}.
        :param separator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#separator SqlQuery#separator}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#suffix SqlQuery#suffix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlQueryParameterEnumMultiple.__init__)
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument separator", value=separator, expected_type=type_hints["separator"])
            check_type(argname="argument suffix", value=suffix, expected_type=type_hints["suffix"])
        self._values: typing.Dict[str, typing.Any] = {
            "prefix": prefix,
            "separator": separator,
            "suffix": suffix,
        }

    @builtins.property
    def prefix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#prefix SqlQuery#prefix}.'''
        result = self._values.get("prefix")
        assert result is not None, "Required property 'prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def separator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#separator SqlQuery#separator}.'''
        result = self._values.get("separator")
        assert result is not None, "Required property 'separator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def suffix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#suffix SqlQuery#suffix}.'''
        result = self._values.get("suffix")
        assert result is not None, "Required property 'suffix' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterEnumMultiple(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterEnumMultipleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterEnumMultipleOutputReference",
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
            type_hints = typing.get_type_hints(SqlQueryParameterEnumMultipleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="separatorInput")
    def separator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "separatorInput"))

    @builtins.property
    @jsii.member(jsii_name="suffixInput")
    def suffix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "suffixInput"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterEnumMultipleOutputReference, "prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="separator")
    def separator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "separator"))

    @separator.setter
    def separator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterEnumMultipleOutputReference, "separator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "separator", value)

    @builtins.property
    @jsii.member(jsii_name="suffix")
    def suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suffix"))

    @suffix.setter
    def suffix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterEnumMultipleOutputReference, "suffix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suffix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterEnumMultiple]:
        return typing.cast(typing.Optional[SqlQueryParameterEnumMultiple], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlQueryParameterEnumMultiple],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterEnumMultipleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SqlQueryParameterEnumOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterEnumOutputReference",
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
            type_hints = typing.get_type_hints(SqlQueryParameterEnumOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMultiple")
    def put_multiple(
        self,
        *,
        prefix: builtins.str,
        separator: builtins.str,
        suffix: builtins.str,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#prefix SqlQuery#prefix}.
        :param separator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#separator SqlQuery#separator}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#suffix SqlQuery#suffix}.
        '''
        value = SqlQueryParameterEnumMultiple(
            prefix=prefix, separator=separator, suffix=suffix
        )

        return typing.cast(None, jsii.invoke(self, "putMultiple", [value]))

    @jsii.member(jsii_name="resetMultiple")
    def reset_multiple(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMultiple", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="multiple")
    def multiple(self) -> SqlQueryParameterEnumMultipleOutputReference:
        return typing.cast(SqlQueryParameterEnumMultipleOutputReference, jsii.get(self, "multiple"))

    @builtins.property
    @jsii.member(jsii_name="multipleInput")
    def multiple_input(self) -> typing.Optional[SqlQueryParameterEnumMultiple]:
        return typing.cast(typing.Optional[SqlQueryParameterEnumMultiple], jsii.get(self, "multipleInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterEnumOutputReference, "options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterEnumOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterEnumOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterEnum]:
        return typing.cast(typing.Optional[SqlQueryParameterEnum], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlQueryParameterEnum]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterEnumOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SqlQueryParameterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterList",
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
            type_hints = typing.get_type_hints(SqlQueryParameterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SqlQueryParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlQueryParameterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SqlQueryParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SqlQueryParameter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SqlQueryParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SqlQueryParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterNumber",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class SqlQueryParameterNumber:
    def __init__(self, *, value: jsii.Number) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlQueryParameterNumber.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterNumber(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterNumberOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterNumberOutputReference",
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
            type_hints = typing.get_type_hints(SqlQueryParameterNumberOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterNumberOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterNumber]:
        return typing.cast(typing.Optional[SqlQueryParameterNumber], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlQueryParameterNumber]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterNumberOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SqlQueryParameterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterOutputReference",
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
            type_hints = typing.get_type_hints(SqlQueryParameterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDate")
    def put_date(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        value_ = SqlQueryParameterDate(value=value)

        return typing.cast(None, jsii.invoke(self, "putDate", [value_]))

    @jsii.member(jsii_name="putDateRange")
    def put_date_range(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        value_ = SqlQueryParameterDateRange(value=value)

        return typing.cast(None, jsii.invoke(self, "putDateRange", [value_]))

    @jsii.member(jsii_name="putDatetime")
    def put_datetime(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        value_ = SqlQueryParameterDatetime(value=value)

        return typing.cast(None, jsii.invoke(self, "putDatetime", [value_]))

    @jsii.member(jsii_name="putDatetimeRange")
    def put_datetime_range(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        value_ = SqlQueryParameterDatetimeRange(value=value)

        return typing.cast(None, jsii.invoke(self, "putDatetimeRange", [value_]))

    @jsii.member(jsii_name="putDatetimesec")
    def put_datetimesec(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        value_ = SqlQueryParameterDatetimesec(value=value)

        return typing.cast(None, jsii.invoke(self, "putDatetimesec", [value_]))

    @jsii.member(jsii_name="putDatetimesecRange")
    def put_datetimesec_range(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        value_ = SqlQueryParameterDatetimesecRange(value=value)

        return typing.cast(None, jsii.invoke(self, "putDatetimesecRange", [value_]))

    @jsii.member(jsii_name="putEnum")
    def put_enum(
        self,
        *,
        options: typing.Sequence[builtins.str],
        multiple: typing.Optional[typing.Union[SqlQueryParameterEnumMultiple, typing.Dict[str, typing.Any]]] = None,
        value: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#options SqlQuery#options}.
        :param multiple: multiple block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#multiple SqlQuery#multiple}
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#values SqlQuery#values}.
        '''
        value_ = SqlQueryParameterEnum(
            options=options, multiple=multiple, value=value, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putEnum", [value_]))

    @jsii.member(jsii_name="putNumber")
    def put_number(self, *, value: jsii.Number) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        value_ = SqlQueryParameterNumber(value=value)

        return typing.cast(None, jsii.invoke(self, "putNumber", [value_]))

    @jsii.member(jsii_name="putQuery")
    def put_query(
        self,
        *,
        query_id: builtins.str,
        multiple: typing.Optional[typing.Union["SqlQueryParameterQueryMultiple", typing.Dict[str, typing.Any]]] = None,
        value: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param query_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#query_id SqlQuery#query_id}.
        :param multiple: multiple block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#multiple SqlQuery#multiple}
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#values SqlQuery#values}.
        '''
        value_ = SqlQueryParameterQuery(
            query_id=query_id, multiple=multiple, value=value, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putQuery", [value_]))

    @jsii.member(jsii_name="putText")
    def put_text(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        value_ = SqlQueryParameterText(value=value)

        return typing.cast(None, jsii.invoke(self, "putText", [value_]))

    @jsii.member(jsii_name="resetDate")
    def reset_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDate", []))

    @jsii.member(jsii_name="resetDateRange")
    def reset_date_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDateRange", []))

    @jsii.member(jsii_name="resetDatetime")
    def reset_datetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatetime", []))

    @jsii.member(jsii_name="resetDatetimeRange")
    def reset_datetime_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatetimeRange", []))

    @jsii.member(jsii_name="resetDatetimesec")
    def reset_datetimesec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatetimesec", []))

    @jsii.member(jsii_name="resetDatetimesecRange")
    def reset_datetimesec_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatetimesecRange", []))

    @jsii.member(jsii_name="resetEnum")
    def reset_enum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnum", []))

    @jsii.member(jsii_name="resetNumber")
    def reset_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumber", []))

    @jsii.member(jsii_name="resetQuery")
    def reset_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuery", []))

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @builtins.property
    @jsii.member(jsii_name="date")
    def date(self) -> SqlQueryParameterDateOutputReference:
        return typing.cast(SqlQueryParameterDateOutputReference, jsii.get(self, "date"))

    @builtins.property
    @jsii.member(jsii_name="dateRange")
    def date_range(self) -> SqlQueryParameterDateRangeOutputReference:
        return typing.cast(SqlQueryParameterDateRangeOutputReference, jsii.get(self, "dateRange"))

    @builtins.property
    @jsii.member(jsii_name="datetime")
    def datetime(self) -> SqlQueryParameterDatetimeOutputReference:
        return typing.cast(SqlQueryParameterDatetimeOutputReference, jsii.get(self, "datetime"))

    @builtins.property
    @jsii.member(jsii_name="datetimeRange")
    def datetime_range(self) -> SqlQueryParameterDatetimeRangeOutputReference:
        return typing.cast(SqlQueryParameterDatetimeRangeOutputReference, jsii.get(self, "datetimeRange"))

    @builtins.property
    @jsii.member(jsii_name="datetimesec")
    def datetimesec(self) -> SqlQueryParameterDatetimesecOutputReference:
        return typing.cast(SqlQueryParameterDatetimesecOutputReference, jsii.get(self, "datetimesec"))

    @builtins.property
    @jsii.member(jsii_name="datetimesecRange")
    def datetimesec_range(self) -> SqlQueryParameterDatetimesecRangeOutputReference:
        return typing.cast(SqlQueryParameterDatetimesecRangeOutputReference, jsii.get(self, "datetimesecRange"))

    @builtins.property
    @jsii.member(jsii_name="enum")
    def enum(self) -> SqlQueryParameterEnumOutputReference:
        return typing.cast(SqlQueryParameterEnumOutputReference, jsii.get(self, "enum"))

    @builtins.property
    @jsii.member(jsii_name="number")
    def number(self) -> SqlQueryParameterNumberOutputReference:
        return typing.cast(SqlQueryParameterNumberOutputReference, jsii.get(self, "number"))

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> "SqlQueryParameterQueryOutputReference":
        return typing.cast("SqlQueryParameterQueryOutputReference", jsii.get(self, "query"))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> "SqlQueryParameterTextOutputReference":
        return typing.cast("SqlQueryParameterTextOutputReference", jsii.get(self, "text"))

    @builtins.property
    @jsii.member(jsii_name="dateInput")
    def date_input(self) -> typing.Optional[SqlQueryParameterDate]:
        return typing.cast(typing.Optional[SqlQueryParameterDate], jsii.get(self, "dateInput"))

    @builtins.property
    @jsii.member(jsii_name="dateRangeInput")
    def date_range_input(self) -> typing.Optional[SqlQueryParameterDateRange]:
        return typing.cast(typing.Optional[SqlQueryParameterDateRange], jsii.get(self, "dateRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="datetimeInput")
    def datetime_input(self) -> typing.Optional[SqlQueryParameterDatetime]:
        return typing.cast(typing.Optional[SqlQueryParameterDatetime], jsii.get(self, "datetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="datetimeRangeInput")
    def datetime_range_input(self) -> typing.Optional[SqlQueryParameterDatetimeRange]:
        return typing.cast(typing.Optional[SqlQueryParameterDatetimeRange], jsii.get(self, "datetimeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="datetimesecInput")
    def datetimesec_input(self) -> typing.Optional[SqlQueryParameterDatetimesec]:
        return typing.cast(typing.Optional[SqlQueryParameterDatetimesec], jsii.get(self, "datetimesecInput"))

    @builtins.property
    @jsii.member(jsii_name="datetimesecRangeInput")
    def datetimesec_range_input(
        self,
    ) -> typing.Optional[SqlQueryParameterDatetimesecRange]:
        return typing.cast(typing.Optional[SqlQueryParameterDatetimesecRange], jsii.get(self, "datetimesecRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="enumInput")
    def enum_input(self) -> typing.Optional[SqlQueryParameterEnum]:
        return typing.cast(typing.Optional[SqlQueryParameterEnum], jsii.get(self, "enumInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="numberInput")
    def number_input(self) -> typing.Optional[SqlQueryParameterNumber]:
        return typing.cast(typing.Optional[SqlQueryParameterNumber], jsii.get(self, "numberInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional["SqlQueryParameterQuery"]:
        return typing.cast(typing.Optional["SqlQueryParameterQuery"], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(self) -> typing.Optional["SqlQueryParameterText"]:
        return typing.cast(typing.Optional["SqlQueryParameterText"], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SqlQueryParameter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SqlQueryParameter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SqlQueryParameter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterQuery",
    jsii_struct_bases=[],
    name_mapping={
        "query_id": "queryId",
        "multiple": "multiple",
        "value": "value",
        "values": "values",
    },
)
class SqlQueryParameterQuery:
    def __init__(
        self,
        *,
        query_id: builtins.str,
        multiple: typing.Optional[typing.Union["SqlQueryParameterQueryMultiple", typing.Dict[str, typing.Any]]] = None,
        value: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param query_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#query_id SqlQuery#query_id}.
        :param multiple: multiple block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#multiple SqlQuery#multiple}
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#values SqlQuery#values}.
        '''
        if isinstance(multiple, dict):
            multiple = SqlQueryParameterQueryMultiple(**multiple)
        if __debug__:
            type_hints = typing.get_type_hints(SqlQueryParameterQuery.__init__)
            check_type(argname="argument query_id", value=query_id, expected_type=type_hints["query_id"])
            check_type(argname="argument multiple", value=multiple, expected_type=type_hints["multiple"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "query_id": query_id,
        }
        if multiple is not None:
            self._values["multiple"] = multiple
        if value is not None:
            self._values["value"] = value
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def query_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#query_id SqlQuery#query_id}.'''
        result = self._values.get("query_id")
        assert result is not None, "Required property 'query_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def multiple(self) -> typing.Optional["SqlQueryParameterQueryMultiple"]:
        '''multiple block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#multiple SqlQuery#multiple}
        '''
        result = self._values.get("multiple")
        return typing.cast(typing.Optional["SqlQueryParameterQueryMultiple"], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#values SqlQuery#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterQueryMultiple",
    jsii_struct_bases=[],
    name_mapping={"prefix": "prefix", "separator": "separator", "suffix": "suffix"},
)
class SqlQueryParameterQueryMultiple:
    def __init__(
        self,
        *,
        prefix: builtins.str,
        separator: builtins.str,
        suffix: builtins.str,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#prefix SqlQuery#prefix}.
        :param separator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#separator SqlQuery#separator}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#suffix SqlQuery#suffix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlQueryParameterQueryMultiple.__init__)
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument separator", value=separator, expected_type=type_hints["separator"])
            check_type(argname="argument suffix", value=suffix, expected_type=type_hints["suffix"])
        self._values: typing.Dict[str, typing.Any] = {
            "prefix": prefix,
            "separator": separator,
            "suffix": suffix,
        }

    @builtins.property
    def prefix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#prefix SqlQuery#prefix}.'''
        result = self._values.get("prefix")
        assert result is not None, "Required property 'prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def separator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#separator SqlQuery#separator}.'''
        result = self._values.get("separator")
        assert result is not None, "Required property 'separator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def suffix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#suffix SqlQuery#suffix}.'''
        result = self._values.get("suffix")
        assert result is not None, "Required property 'suffix' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterQueryMultiple(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterQueryMultipleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterQueryMultipleOutputReference",
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
            type_hints = typing.get_type_hints(SqlQueryParameterQueryMultipleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="separatorInput")
    def separator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "separatorInput"))

    @builtins.property
    @jsii.member(jsii_name="suffixInput")
    def suffix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "suffixInput"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterQueryMultipleOutputReference, "prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="separator")
    def separator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "separator"))

    @separator.setter
    def separator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterQueryMultipleOutputReference, "separator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "separator", value)

    @builtins.property
    @jsii.member(jsii_name="suffix")
    def suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suffix"))

    @suffix.setter
    def suffix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterQueryMultipleOutputReference, "suffix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suffix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterQueryMultiple]:
        return typing.cast(typing.Optional[SqlQueryParameterQueryMultiple], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlQueryParameterQueryMultiple],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterQueryMultipleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SqlQueryParameterQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterQueryOutputReference",
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
            type_hints = typing.get_type_hints(SqlQueryParameterQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMultiple")
    def put_multiple(
        self,
        *,
        prefix: builtins.str,
        separator: builtins.str,
        suffix: builtins.str,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#prefix SqlQuery#prefix}.
        :param separator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#separator SqlQuery#separator}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#suffix SqlQuery#suffix}.
        '''
        value = SqlQueryParameterQueryMultiple(
            prefix=prefix, separator=separator, suffix=suffix
        )

        return typing.cast(None, jsii.invoke(self, "putMultiple", [value]))

    @jsii.member(jsii_name="resetMultiple")
    def reset_multiple(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMultiple", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="multiple")
    def multiple(self) -> SqlQueryParameterQueryMultipleOutputReference:
        return typing.cast(SqlQueryParameterQueryMultipleOutputReference, jsii.get(self, "multiple"))

    @builtins.property
    @jsii.member(jsii_name="multipleInput")
    def multiple_input(self) -> typing.Optional[SqlQueryParameterQueryMultiple]:
        return typing.cast(typing.Optional[SqlQueryParameterQueryMultiple], jsii.get(self, "multipleInput"))

    @builtins.property
    @jsii.member(jsii_name="queryIdInput")
    def query_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="queryId")
    def query_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryId"))

    @query_id.setter
    def query_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterQueryOutputReference, "query_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryId", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterQueryOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterQueryOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterQuery]:
        return typing.cast(typing.Optional[SqlQueryParameterQuery], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlQueryParameterQuery]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterText",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class SqlQueryParameterText:
    def __init__(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlQueryParameterText.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterTextOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryParameterTextOutputReference",
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
            type_hints = typing.get_type_hints(SqlQueryParameterTextOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterTextOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterText]:
        return typing.cast(typing.Optional[SqlQueryParameterText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlQueryParameterText]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryParameterTextOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQuerySchedule",
    jsii_struct_bases=[],
    name_mapping={"continuous": "continuous", "daily": "daily", "weekly": "weekly"},
)
class SqlQuerySchedule:
    def __init__(
        self,
        *,
        continuous: typing.Optional[typing.Union["SqlQueryScheduleContinuous", typing.Dict[str, typing.Any]]] = None,
        daily: typing.Optional[typing.Union["SqlQueryScheduleDaily", typing.Dict[str, typing.Any]]] = None,
        weekly: typing.Optional[typing.Union["SqlQueryScheduleWeekly", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param continuous: continuous block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#continuous SqlQuery#continuous}
        :param daily: daily block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#daily SqlQuery#daily}
        :param weekly: weekly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#weekly SqlQuery#weekly}
        '''
        if isinstance(continuous, dict):
            continuous = SqlQueryScheduleContinuous(**continuous)
        if isinstance(daily, dict):
            daily = SqlQueryScheduleDaily(**daily)
        if isinstance(weekly, dict):
            weekly = SqlQueryScheduleWeekly(**weekly)
        if __debug__:
            type_hints = typing.get_type_hints(SqlQuerySchedule.__init__)
            check_type(argname="argument continuous", value=continuous, expected_type=type_hints["continuous"])
            check_type(argname="argument daily", value=daily, expected_type=type_hints["daily"])
            check_type(argname="argument weekly", value=weekly, expected_type=type_hints["weekly"])
        self._values: typing.Dict[str, typing.Any] = {}
        if continuous is not None:
            self._values["continuous"] = continuous
        if daily is not None:
            self._values["daily"] = daily
        if weekly is not None:
            self._values["weekly"] = weekly

    @builtins.property
    def continuous(self) -> typing.Optional["SqlQueryScheduleContinuous"]:
        '''continuous block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#continuous SqlQuery#continuous}
        '''
        result = self._values.get("continuous")
        return typing.cast(typing.Optional["SqlQueryScheduleContinuous"], result)

    @builtins.property
    def daily(self) -> typing.Optional["SqlQueryScheduleDaily"]:
        '''daily block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#daily SqlQuery#daily}
        '''
        result = self._values.get("daily")
        return typing.cast(typing.Optional["SqlQueryScheduleDaily"], result)

    @builtins.property
    def weekly(self) -> typing.Optional["SqlQueryScheduleWeekly"]:
        '''weekly block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#weekly SqlQuery#weekly}
        '''
        result = self._values.get("weekly")
        return typing.cast(typing.Optional["SqlQueryScheduleWeekly"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQuerySchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryScheduleContinuous",
    jsii_struct_bases=[],
    name_mapping={"interval_seconds": "intervalSeconds", "until_date": "untilDate"},
)
class SqlQueryScheduleContinuous:
    def __init__(
        self,
        *,
        interval_seconds: jsii.Number,
        until_date: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param interval_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#interval_seconds SqlQuery#interval_seconds}.
        :param until_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#until_date SqlQuery#until_date}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlQueryScheduleContinuous.__init__)
            check_type(argname="argument interval_seconds", value=interval_seconds, expected_type=type_hints["interval_seconds"])
            check_type(argname="argument until_date", value=until_date, expected_type=type_hints["until_date"])
        self._values: typing.Dict[str, typing.Any] = {
            "interval_seconds": interval_seconds,
        }
        if until_date is not None:
            self._values["until_date"] = until_date

    @builtins.property
    def interval_seconds(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#interval_seconds SqlQuery#interval_seconds}.'''
        result = self._values.get("interval_seconds")
        assert result is not None, "Required property 'interval_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def until_date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#until_date SqlQuery#until_date}.'''
        result = self._values.get("until_date")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryScheduleContinuous(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryScheduleContinuousOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryScheduleContinuousOutputReference",
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
            type_hints = typing.get_type_hints(SqlQueryScheduleContinuousOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUntilDate")
    def reset_until_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUntilDate", []))

    @builtins.property
    @jsii.member(jsii_name="intervalSecondsInput")
    def interval_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="untilDateInput")
    def until_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "untilDateInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalSeconds")
    def interval_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalSeconds"))

    @interval_seconds.setter
    def interval_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryScheduleContinuousOutputReference, "interval_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="untilDate")
    def until_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "untilDate"))

    @until_date.setter
    def until_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryScheduleContinuousOutputReference, "until_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "untilDate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryScheduleContinuous]:
        return typing.cast(typing.Optional[SqlQueryScheduleContinuous], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlQueryScheduleContinuous],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryScheduleContinuousOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryScheduleDaily",
    jsii_struct_bases=[],
    name_mapping={
        "interval_days": "intervalDays",
        "time_of_day": "timeOfDay",
        "until_date": "untilDate",
    },
)
class SqlQueryScheduleDaily:
    def __init__(
        self,
        *,
        interval_days: jsii.Number,
        time_of_day: builtins.str,
        until_date: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param interval_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#interval_days SqlQuery#interval_days}.
        :param time_of_day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#time_of_day SqlQuery#time_of_day}.
        :param until_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#until_date SqlQuery#until_date}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlQueryScheduleDaily.__init__)
            check_type(argname="argument interval_days", value=interval_days, expected_type=type_hints["interval_days"])
            check_type(argname="argument time_of_day", value=time_of_day, expected_type=type_hints["time_of_day"])
            check_type(argname="argument until_date", value=until_date, expected_type=type_hints["until_date"])
        self._values: typing.Dict[str, typing.Any] = {
            "interval_days": interval_days,
            "time_of_day": time_of_day,
        }
        if until_date is not None:
            self._values["until_date"] = until_date

    @builtins.property
    def interval_days(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#interval_days SqlQuery#interval_days}.'''
        result = self._values.get("interval_days")
        assert result is not None, "Required property 'interval_days' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def time_of_day(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#time_of_day SqlQuery#time_of_day}.'''
        result = self._values.get("time_of_day")
        assert result is not None, "Required property 'time_of_day' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def until_date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#until_date SqlQuery#until_date}.'''
        result = self._values.get("until_date")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryScheduleDaily(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryScheduleDailyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryScheduleDailyOutputReference",
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
            type_hints = typing.get_type_hints(SqlQueryScheduleDailyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUntilDate")
    def reset_until_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUntilDate", []))

    @builtins.property
    @jsii.member(jsii_name="intervalDaysInput")
    def interval_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="timeOfDayInput")
    def time_of_day_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeOfDayInput"))

    @builtins.property
    @jsii.member(jsii_name="untilDateInput")
    def until_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "untilDateInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalDays")
    def interval_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalDays"))

    @interval_days.setter
    def interval_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryScheduleDailyOutputReference, "interval_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalDays", value)

    @builtins.property
    @jsii.member(jsii_name="timeOfDay")
    def time_of_day(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeOfDay"))

    @time_of_day.setter
    def time_of_day(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryScheduleDailyOutputReference, "time_of_day").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeOfDay", value)

    @builtins.property
    @jsii.member(jsii_name="untilDate")
    def until_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "untilDate"))

    @until_date.setter
    def until_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryScheduleDailyOutputReference, "until_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "untilDate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryScheduleDaily]:
        return typing.cast(typing.Optional[SqlQueryScheduleDaily], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlQueryScheduleDaily]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryScheduleDailyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SqlQueryScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryScheduleOutputReference",
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
            type_hints = typing.get_type_hints(SqlQueryScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putContinuous")
    def put_continuous(
        self,
        *,
        interval_seconds: jsii.Number,
        until_date: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param interval_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#interval_seconds SqlQuery#interval_seconds}.
        :param until_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#until_date SqlQuery#until_date}.
        '''
        value = SqlQueryScheduleContinuous(
            interval_seconds=interval_seconds, until_date=until_date
        )

        return typing.cast(None, jsii.invoke(self, "putContinuous", [value]))

    @jsii.member(jsii_name="putDaily")
    def put_daily(
        self,
        *,
        interval_days: jsii.Number,
        time_of_day: builtins.str,
        until_date: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param interval_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#interval_days SqlQuery#interval_days}.
        :param time_of_day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#time_of_day SqlQuery#time_of_day}.
        :param until_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#until_date SqlQuery#until_date}.
        '''
        value = SqlQueryScheduleDaily(
            interval_days=interval_days, time_of_day=time_of_day, until_date=until_date
        )

        return typing.cast(None, jsii.invoke(self, "putDaily", [value]))

    @jsii.member(jsii_name="putWeekly")
    def put_weekly(
        self,
        *,
        day_of_week: builtins.str,
        interval_weeks: jsii.Number,
        time_of_day: builtins.str,
        until_date: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param day_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#day_of_week SqlQuery#day_of_week}.
        :param interval_weeks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#interval_weeks SqlQuery#interval_weeks}.
        :param time_of_day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#time_of_day SqlQuery#time_of_day}.
        :param until_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#until_date SqlQuery#until_date}.
        '''
        value = SqlQueryScheduleWeekly(
            day_of_week=day_of_week,
            interval_weeks=interval_weeks,
            time_of_day=time_of_day,
            until_date=until_date,
        )

        return typing.cast(None, jsii.invoke(self, "putWeekly", [value]))

    @jsii.member(jsii_name="resetContinuous")
    def reset_continuous(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContinuous", []))

    @jsii.member(jsii_name="resetDaily")
    def reset_daily(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDaily", []))

    @jsii.member(jsii_name="resetWeekly")
    def reset_weekly(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeekly", []))

    @builtins.property
    @jsii.member(jsii_name="continuous")
    def continuous(self) -> SqlQueryScheduleContinuousOutputReference:
        return typing.cast(SqlQueryScheduleContinuousOutputReference, jsii.get(self, "continuous"))

    @builtins.property
    @jsii.member(jsii_name="daily")
    def daily(self) -> SqlQueryScheduleDailyOutputReference:
        return typing.cast(SqlQueryScheduleDailyOutputReference, jsii.get(self, "daily"))

    @builtins.property
    @jsii.member(jsii_name="weekly")
    def weekly(self) -> "SqlQueryScheduleWeeklyOutputReference":
        return typing.cast("SqlQueryScheduleWeeklyOutputReference", jsii.get(self, "weekly"))

    @builtins.property
    @jsii.member(jsii_name="continuousInput")
    def continuous_input(self) -> typing.Optional[SqlQueryScheduleContinuous]:
        return typing.cast(typing.Optional[SqlQueryScheduleContinuous], jsii.get(self, "continuousInput"))

    @builtins.property
    @jsii.member(jsii_name="dailyInput")
    def daily_input(self) -> typing.Optional[SqlQueryScheduleDaily]:
        return typing.cast(typing.Optional[SqlQueryScheduleDaily], jsii.get(self, "dailyInput"))

    @builtins.property
    @jsii.member(jsii_name="weeklyInput")
    def weekly_input(self) -> typing.Optional["SqlQueryScheduleWeekly"]:
        return typing.cast(typing.Optional["SqlQueryScheduleWeekly"], jsii.get(self, "weeklyInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQuerySchedule]:
        return typing.cast(typing.Optional[SqlQuerySchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlQuerySchedule]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryScheduleWeekly",
    jsii_struct_bases=[],
    name_mapping={
        "day_of_week": "dayOfWeek",
        "interval_weeks": "intervalWeeks",
        "time_of_day": "timeOfDay",
        "until_date": "untilDate",
    },
)
class SqlQueryScheduleWeekly:
    def __init__(
        self,
        *,
        day_of_week: builtins.str,
        interval_weeks: jsii.Number,
        time_of_day: builtins.str,
        until_date: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param day_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#day_of_week SqlQuery#day_of_week}.
        :param interval_weeks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#interval_weeks SqlQuery#interval_weeks}.
        :param time_of_day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#time_of_day SqlQuery#time_of_day}.
        :param until_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#until_date SqlQuery#until_date}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlQueryScheduleWeekly.__init__)
            check_type(argname="argument day_of_week", value=day_of_week, expected_type=type_hints["day_of_week"])
            check_type(argname="argument interval_weeks", value=interval_weeks, expected_type=type_hints["interval_weeks"])
            check_type(argname="argument time_of_day", value=time_of_day, expected_type=type_hints["time_of_day"])
            check_type(argname="argument until_date", value=until_date, expected_type=type_hints["until_date"])
        self._values: typing.Dict[str, typing.Any] = {
            "day_of_week": day_of_week,
            "interval_weeks": interval_weeks,
            "time_of_day": time_of_day,
        }
        if until_date is not None:
            self._values["until_date"] = until_date

    @builtins.property
    def day_of_week(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#day_of_week SqlQuery#day_of_week}.'''
        result = self._values.get("day_of_week")
        assert result is not None, "Required property 'day_of_week' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def interval_weeks(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#interval_weeks SqlQuery#interval_weeks}.'''
        result = self._values.get("interval_weeks")
        assert result is not None, "Required property 'interval_weeks' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def time_of_day(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#time_of_day SqlQuery#time_of_day}.'''
        result = self._values.get("time_of_day")
        assert result is not None, "Required property 'time_of_day' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def until_date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#until_date SqlQuery#until_date}.'''
        result = self._values.get("until_date")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryScheduleWeekly(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryScheduleWeeklyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlQuery.SqlQueryScheduleWeeklyOutputReference",
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
            type_hints = typing.get_type_hints(SqlQueryScheduleWeeklyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUntilDate")
    def reset_until_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUntilDate", []))

    @builtins.property
    @jsii.member(jsii_name="dayOfWeekInput")
    def day_of_week_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfWeekInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalWeeksInput")
    def interval_weeks_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalWeeksInput"))

    @builtins.property
    @jsii.member(jsii_name="timeOfDayInput")
    def time_of_day_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeOfDayInput"))

    @builtins.property
    @jsii.member(jsii_name="untilDateInput")
    def until_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "untilDateInput"))

    @builtins.property
    @jsii.member(jsii_name="dayOfWeek")
    def day_of_week(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayOfWeek"))

    @day_of_week.setter
    def day_of_week(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryScheduleWeeklyOutputReference, "day_of_week").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfWeek", value)

    @builtins.property
    @jsii.member(jsii_name="intervalWeeks")
    def interval_weeks(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalWeeks"))

    @interval_weeks.setter
    def interval_weeks(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryScheduleWeeklyOutputReference, "interval_weeks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalWeeks", value)

    @builtins.property
    @jsii.member(jsii_name="timeOfDay")
    def time_of_day(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeOfDay"))

    @time_of_day.setter
    def time_of_day(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryScheduleWeeklyOutputReference, "time_of_day").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeOfDay", value)

    @builtins.property
    @jsii.member(jsii_name="untilDate")
    def until_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "untilDate"))

    @until_date.setter
    def until_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryScheduleWeeklyOutputReference, "until_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "untilDate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryScheduleWeekly]:
        return typing.cast(typing.Optional[SqlQueryScheduleWeekly], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlQueryScheduleWeekly]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlQueryScheduleWeeklyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SqlQuery",
    "SqlQueryConfig",
    "SqlQueryParameter",
    "SqlQueryParameterDate",
    "SqlQueryParameterDateOutputReference",
    "SqlQueryParameterDateRange",
    "SqlQueryParameterDateRangeOutputReference",
    "SqlQueryParameterDatetime",
    "SqlQueryParameterDatetimeOutputReference",
    "SqlQueryParameterDatetimeRange",
    "SqlQueryParameterDatetimeRangeOutputReference",
    "SqlQueryParameterDatetimesec",
    "SqlQueryParameterDatetimesecOutputReference",
    "SqlQueryParameterDatetimesecRange",
    "SqlQueryParameterDatetimesecRangeOutputReference",
    "SqlQueryParameterEnum",
    "SqlQueryParameterEnumMultiple",
    "SqlQueryParameterEnumMultipleOutputReference",
    "SqlQueryParameterEnumOutputReference",
    "SqlQueryParameterList",
    "SqlQueryParameterNumber",
    "SqlQueryParameterNumberOutputReference",
    "SqlQueryParameterOutputReference",
    "SqlQueryParameterQuery",
    "SqlQueryParameterQueryMultiple",
    "SqlQueryParameterQueryMultipleOutputReference",
    "SqlQueryParameterQueryOutputReference",
    "SqlQueryParameterText",
    "SqlQueryParameterTextOutputReference",
    "SqlQuerySchedule",
    "SqlQueryScheduleContinuous",
    "SqlQueryScheduleContinuousOutputReference",
    "SqlQueryScheduleDaily",
    "SqlQueryScheduleDailyOutputReference",
    "SqlQueryScheduleOutputReference",
    "SqlQueryScheduleWeekly",
    "SqlQueryScheduleWeeklyOutputReference",
]

publication.publish()
