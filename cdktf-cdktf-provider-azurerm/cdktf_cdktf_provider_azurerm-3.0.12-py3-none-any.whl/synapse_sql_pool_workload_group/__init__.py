'''
# `azurerm_synapse_sql_pool_workload_group`

Refer to the Terraform Registory for docs: [`azurerm_synapse_sql_pool_workload_group`](https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group).
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


class SynapseSqlPoolWorkloadGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.synapseSqlPoolWorkloadGroup.SynapseSqlPoolWorkloadGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group azurerm_synapse_sql_pool_workload_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        max_resource_percent: jsii.Number,
        min_resource_percent: jsii.Number,
        name: builtins.str,
        sql_pool_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        importance: typing.Optional[builtins.str] = None,
        max_resource_percent_per_request: typing.Optional[jsii.Number] = None,
        min_resource_percent_per_request: typing.Optional[jsii.Number] = None,
        query_execution_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        timeouts: typing.Optional[typing.Union["SynapseSqlPoolWorkloadGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group azurerm_synapse_sql_pool_workload_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param max_resource_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#max_resource_percent SynapseSqlPoolWorkloadGroup#max_resource_percent}.
        :param min_resource_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#min_resource_percent SynapseSqlPoolWorkloadGroup#min_resource_percent}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#name SynapseSqlPoolWorkloadGroup#name}.
        :param sql_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#sql_pool_id SynapseSqlPoolWorkloadGroup#sql_pool_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#id SynapseSqlPoolWorkloadGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param importance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#importance SynapseSqlPoolWorkloadGroup#importance}.
        :param max_resource_percent_per_request: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#max_resource_percent_per_request SynapseSqlPoolWorkloadGroup#max_resource_percent_per_request}.
        :param min_resource_percent_per_request: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#min_resource_percent_per_request SynapseSqlPoolWorkloadGroup#min_resource_percent_per_request}.
        :param query_execution_timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#query_execution_timeout_in_seconds SynapseSqlPoolWorkloadGroup#query_execution_timeout_in_seconds}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#timeouts SynapseSqlPoolWorkloadGroup#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SynapseSqlPoolWorkloadGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SynapseSqlPoolWorkloadGroupConfig(
            max_resource_percent=max_resource_percent,
            min_resource_percent=min_resource_percent,
            name=name,
            sql_pool_id=sql_pool_id,
            id=id,
            importance=importance,
            max_resource_percent_per_request=max_resource_percent_per_request,
            min_resource_percent_per_request=min_resource_percent_per_request,
            query_execution_timeout_in_seconds=query_execution_timeout_in_seconds,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#create SynapseSqlPoolWorkloadGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#delete SynapseSqlPoolWorkloadGroup#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#read SynapseSqlPoolWorkloadGroup#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#update SynapseSqlPoolWorkloadGroup#update}.
        '''
        value = SynapseSqlPoolWorkloadGroupTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImportance")
    def reset_importance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImportance", []))

    @jsii.member(jsii_name="resetMaxResourcePercentPerRequest")
    def reset_max_resource_percent_per_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxResourcePercentPerRequest", []))

    @jsii.member(jsii_name="resetMinResourcePercentPerRequest")
    def reset_min_resource_percent_per_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinResourcePercentPerRequest", []))

    @jsii.member(jsii_name="resetQueryExecutionTimeoutInSeconds")
    def reset_query_execution_timeout_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryExecutionTimeoutInSeconds", []))

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
    def timeouts(self) -> "SynapseSqlPoolWorkloadGroupTimeoutsOutputReference":
        return typing.cast("SynapseSqlPoolWorkloadGroupTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="importanceInput")
    def importance_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "importanceInput"))

    @builtins.property
    @jsii.member(jsii_name="maxResourcePercentInput")
    def max_resource_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxResourcePercentInput"))

    @builtins.property
    @jsii.member(jsii_name="maxResourcePercentPerRequestInput")
    def max_resource_percent_per_request_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxResourcePercentPerRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="minResourcePercentInput")
    def min_resource_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minResourcePercentInput"))

    @builtins.property
    @jsii.member(jsii_name="minResourcePercentPerRequestInput")
    def min_resource_percent_per_request_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minResourcePercentPerRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="queryExecutionTimeoutInSecondsInput")
    def query_execution_timeout_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "queryExecutionTimeoutInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlPoolIdInput")
    def sql_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlPoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SynapseSqlPoolWorkloadGroupTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SynapseSqlPoolWorkloadGroupTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="importance")
    def importance(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "importance"))

    @importance.setter
    def importance(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadGroup, "importance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "importance", value)

    @builtins.property
    @jsii.member(jsii_name="maxResourcePercent")
    def max_resource_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxResourcePercent"))

    @max_resource_percent.setter
    def max_resource_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadGroup, "max_resource_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxResourcePercent", value)

    @builtins.property
    @jsii.member(jsii_name="maxResourcePercentPerRequest")
    def max_resource_percent_per_request(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxResourcePercentPerRequest"))

    @max_resource_percent_per_request.setter
    def max_resource_percent_per_request(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadGroup, "max_resource_percent_per_request").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxResourcePercentPerRequest", value)

    @builtins.property
    @jsii.member(jsii_name="minResourcePercent")
    def min_resource_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minResourcePercent"))

    @min_resource_percent.setter
    def min_resource_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadGroup, "min_resource_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minResourcePercent", value)

    @builtins.property
    @jsii.member(jsii_name="minResourcePercentPerRequest")
    def min_resource_percent_per_request(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minResourcePercentPerRequest"))

    @min_resource_percent_per_request.setter
    def min_resource_percent_per_request(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadGroup, "min_resource_percent_per_request").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minResourcePercentPerRequest", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadGroup, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="queryExecutionTimeoutInSeconds")
    def query_execution_timeout_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "queryExecutionTimeoutInSeconds"))

    @query_execution_timeout_in_seconds.setter
    def query_execution_timeout_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadGroup, "query_execution_timeout_in_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryExecutionTimeoutInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="sqlPoolId")
    def sql_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlPoolId"))

    @sql_pool_id.setter
    def sql_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadGroup, "sql_pool_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlPoolId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.synapseSqlPoolWorkloadGroup.SynapseSqlPoolWorkloadGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "max_resource_percent": "maxResourcePercent",
        "min_resource_percent": "minResourcePercent",
        "name": "name",
        "sql_pool_id": "sqlPoolId",
        "id": "id",
        "importance": "importance",
        "max_resource_percent_per_request": "maxResourcePercentPerRequest",
        "min_resource_percent_per_request": "minResourcePercentPerRequest",
        "query_execution_timeout_in_seconds": "queryExecutionTimeoutInSeconds",
        "timeouts": "timeouts",
    },
)
class SynapseSqlPoolWorkloadGroupConfig(cdktf.TerraformMetaArguments):
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
        max_resource_percent: jsii.Number,
        min_resource_percent: jsii.Number,
        name: builtins.str,
        sql_pool_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        importance: typing.Optional[builtins.str] = None,
        max_resource_percent_per_request: typing.Optional[jsii.Number] = None,
        min_resource_percent_per_request: typing.Optional[jsii.Number] = None,
        query_execution_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        timeouts: typing.Optional[typing.Union["SynapseSqlPoolWorkloadGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param max_resource_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#max_resource_percent SynapseSqlPoolWorkloadGroup#max_resource_percent}.
        :param min_resource_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#min_resource_percent SynapseSqlPoolWorkloadGroup#min_resource_percent}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#name SynapseSqlPoolWorkloadGroup#name}.
        :param sql_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#sql_pool_id SynapseSqlPoolWorkloadGroup#sql_pool_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#id SynapseSqlPoolWorkloadGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param importance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#importance SynapseSqlPoolWorkloadGroup#importance}.
        :param max_resource_percent_per_request: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#max_resource_percent_per_request SynapseSqlPoolWorkloadGroup#max_resource_percent_per_request}.
        :param min_resource_percent_per_request: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#min_resource_percent_per_request SynapseSqlPoolWorkloadGroup#min_resource_percent_per_request}.
        :param query_execution_timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#query_execution_timeout_in_seconds SynapseSqlPoolWorkloadGroup#query_execution_timeout_in_seconds}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#timeouts SynapseSqlPoolWorkloadGroup#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = SynapseSqlPoolWorkloadGroupTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(SynapseSqlPoolWorkloadGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument max_resource_percent", value=max_resource_percent, expected_type=type_hints["max_resource_percent"])
            check_type(argname="argument min_resource_percent", value=min_resource_percent, expected_type=type_hints["min_resource_percent"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument sql_pool_id", value=sql_pool_id, expected_type=type_hints["sql_pool_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument importance", value=importance, expected_type=type_hints["importance"])
            check_type(argname="argument max_resource_percent_per_request", value=max_resource_percent_per_request, expected_type=type_hints["max_resource_percent_per_request"])
            check_type(argname="argument min_resource_percent_per_request", value=min_resource_percent_per_request, expected_type=type_hints["min_resource_percent_per_request"])
            check_type(argname="argument query_execution_timeout_in_seconds", value=query_execution_timeout_in_seconds, expected_type=type_hints["query_execution_timeout_in_seconds"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_resource_percent": max_resource_percent,
            "min_resource_percent": min_resource_percent,
            "name": name,
            "sql_pool_id": sql_pool_id,
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
        if importance is not None:
            self._values["importance"] = importance
        if max_resource_percent_per_request is not None:
            self._values["max_resource_percent_per_request"] = max_resource_percent_per_request
        if min_resource_percent_per_request is not None:
            self._values["min_resource_percent_per_request"] = min_resource_percent_per_request
        if query_execution_timeout_in_seconds is not None:
            self._values["query_execution_timeout_in_seconds"] = query_execution_timeout_in_seconds
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
    def max_resource_percent(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#max_resource_percent SynapseSqlPoolWorkloadGroup#max_resource_percent}.'''
        result = self._values.get("max_resource_percent")
        assert result is not None, "Required property 'max_resource_percent' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_resource_percent(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#min_resource_percent SynapseSqlPoolWorkloadGroup#min_resource_percent}.'''
        result = self._values.get("min_resource_percent")
        assert result is not None, "Required property 'min_resource_percent' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#name SynapseSqlPoolWorkloadGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sql_pool_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#sql_pool_id SynapseSqlPoolWorkloadGroup#sql_pool_id}.'''
        result = self._values.get("sql_pool_id")
        assert result is not None, "Required property 'sql_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#id SynapseSqlPoolWorkloadGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def importance(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#importance SynapseSqlPoolWorkloadGroup#importance}.'''
        result = self._values.get("importance")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_resource_percent_per_request(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#max_resource_percent_per_request SynapseSqlPoolWorkloadGroup#max_resource_percent_per_request}.'''
        result = self._values.get("max_resource_percent_per_request")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_resource_percent_per_request(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#min_resource_percent_per_request SynapseSqlPoolWorkloadGroup#min_resource_percent_per_request}.'''
        result = self._values.get("min_resource_percent_per_request")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def query_execution_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#query_execution_timeout_in_seconds SynapseSqlPoolWorkloadGroup#query_execution_timeout_in_seconds}.'''
        result = self._values.get("query_execution_timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SynapseSqlPoolWorkloadGroupTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#timeouts SynapseSqlPoolWorkloadGroup#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SynapseSqlPoolWorkloadGroupTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SynapseSqlPoolWorkloadGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.synapseSqlPoolWorkloadGroup.SynapseSqlPoolWorkloadGroupTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class SynapseSqlPoolWorkloadGroupTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#create SynapseSqlPoolWorkloadGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#delete SynapseSqlPoolWorkloadGroup#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#read SynapseSqlPoolWorkloadGroup#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#update SynapseSqlPoolWorkloadGroup#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SynapseSqlPoolWorkloadGroupTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#create SynapseSqlPoolWorkloadGroup#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#delete SynapseSqlPoolWorkloadGroup#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#read SynapseSqlPoolWorkloadGroup#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_group#update SynapseSqlPoolWorkloadGroup#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SynapseSqlPoolWorkloadGroupTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SynapseSqlPoolWorkloadGroupTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.synapseSqlPoolWorkloadGroup.SynapseSqlPoolWorkloadGroupTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(SynapseSqlPoolWorkloadGroupTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadGroupTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadGroupTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadGroupTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadGroupTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SynapseSqlPoolWorkloadGroupTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SynapseSqlPoolWorkloadGroupTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SynapseSqlPoolWorkloadGroupTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadGroupTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SynapseSqlPoolWorkloadGroup",
    "SynapseSqlPoolWorkloadGroupConfig",
    "SynapseSqlPoolWorkloadGroupTimeouts",
    "SynapseSqlPoolWorkloadGroupTimeoutsOutputReference",
]

publication.publish()
