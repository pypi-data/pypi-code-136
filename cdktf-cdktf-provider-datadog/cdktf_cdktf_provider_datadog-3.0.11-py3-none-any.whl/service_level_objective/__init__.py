'''
# `datadog_service_level_objective`

Refer to the Terraform Registory for docs: [`datadog_service_level_objective`](https://www.terraform.io/docs/providers/datadog/r/service_level_objective).
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


class ServiceLevelObjective(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.serviceLevelObjective.ServiceLevelObjective",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective datadog_service_level_objective}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        thresholds: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceLevelObjectiveThresholds", typing.Dict[str, typing.Any]]]],
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        monitor_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        query: typing.Optional[typing.Union["ServiceLevelObjectiveQuery", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        validate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective datadog_service_level_objective} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of Datadog service level objective. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#name ServiceLevelObjective#name}
        :param thresholds: thresholds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#thresholds ServiceLevelObjective#thresholds}
        :param type: The type of the service level objective. The mapping from these types to the types found in the Datadog Web UI can be found in the Datadog API `documentation page <https://docs.datadoghq.com/api/v1/service-level-objectives/#create-a-slo-object>`_. Valid values are ``metric``, ``monitor``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#type ServiceLevelObjective#type}
        :param description: A description of this service level objective. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#description ServiceLevelObjective#description}
        :param force_delete: A boolean indicating whether this monitor can be deleted even if it’s referenced by other resources (e.g. dashboards). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#force_delete ServiceLevelObjective#force_delete}
        :param groups: A static set of groups to filter monitor-based SLOs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#groups ServiceLevelObjective#groups}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#id ServiceLevelObjective#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param monitor_ids: A static set of monitor IDs to use as part of the SLO. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#monitor_ids ServiceLevelObjective#monitor_ids}
        :param query: query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#query ServiceLevelObjective#query}
        :param tags: A list of tags to associate with your service level objective. This can help you categorize and filter service level objectives in the service level objectives page of the UI. Note: it's not currently possible to filter by these tags when querying via the API Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#tags ServiceLevelObjective#tags}
        :param validate: Whether or not to validate the SLO. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#validate ServiceLevelObjective#validate}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceLevelObjective.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ServiceLevelObjectiveConfig(
            name=name,
            thresholds=thresholds,
            type=type,
            description=description,
            force_delete=force_delete,
            groups=groups,
            id=id,
            monitor_ids=monitor_ids,
            query=query,
            tags=tags,
            validate=validate,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putQuery")
    def put_query(self, *, denominator: builtins.str, numerator: builtins.str) -> None:
        '''
        :param denominator: The sum of the ``total`` events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#denominator ServiceLevelObjective#denominator}
        :param numerator: The sum of all the ``good`` events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#numerator ServiceLevelObjective#numerator}
        '''
        value = ServiceLevelObjectiveQuery(
            denominator=denominator, numerator=numerator
        )

        return typing.cast(None, jsii.invoke(self, "putQuery", [value]))

    @jsii.member(jsii_name="putThresholds")
    def put_thresholds(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceLevelObjectiveThresholds", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceLevelObjective.put_thresholds)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putThresholds", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetForceDelete")
    def reset_force_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDelete", []))

    @jsii.member(jsii_name="resetGroups")
    def reset_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroups", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMonitorIds")
    def reset_monitor_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitorIds", []))

    @jsii.member(jsii_name="resetQuery")
    def reset_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuery", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetValidate")
    def reset_validate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidate", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> "ServiceLevelObjectiveQueryOutputReference":
        return typing.cast("ServiceLevelObjectiveQueryOutputReference", jsii.get(self, "query"))

    @builtins.property
    @jsii.member(jsii_name="thresholds")
    def thresholds(self) -> "ServiceLevelObjectiveThresholdsList":
        return typing.cast("ServiceLevelObjectiveThresholdsList", jsii.get(self, "thresholds"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDeleteInput")
    def force_delete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceDeleteInput"))

    @builtins.property
    @jsii.member(jsii_name="groupsInput")
    def groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="monitorIdsInput")
    def monitor_ids_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "monitorIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional["ServiceLevelObjectiveQuery"]:
        return typing.cast(typing.Optional["ServiceLevelObjectiveQuery"], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdsInput")
    def thresholds_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceLevelObjectiveThresholds"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceLevelObjectiveThresholds"]]], jsii.get(self, "thresholdsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="validateInput")
    def validate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "validateInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjective, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="forceDelete")
    def force_delete(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forceDelete"))

    @force_delete.setter
    def force_delete(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjective, "force_delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDelete", value)

    @builtins.property
    @jsii.member(jsii_name="groups")
    def groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groups"))

    @groups.setter
    def groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjective, "groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groups", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjective, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="monitorIds")
    def monitor_ids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "monitorIds"))

    @monitor_ids.setter
    def monitor_ids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjective, "monitor_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitorIds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjective, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjective, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjective, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="validate")
    def validate(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "validate"))

    @validate.setter
    def validate(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjective, "validate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validate", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.serviceLevelObjective.ServiceLevelObjectiveConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "thresholds": "thresholds",
        "type": "type",
        "description": "description",
        "force_delete": "forceDelete",
        "groups": "groups",
        "id": "id",
        "monitor_ids": "monitorIds",
        "query": "query",
        "tags": "tags",
        "validate": "validate",
    },
)
class ServiceLevelObjectiveConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        thresholds: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceLevelObjectiveThresholds", typing.Dict[str, typing.Any]]]],
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        monitor_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        query: typing.Optional[typing.Union["ServiceLevelObjectiveQuery", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        validate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of Datadog service level objective. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#name ServiceLevelObjective#name}
        :param thresholds: thresholds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#thresholds ServiceLevelObjective#thresholds}
        :param type: The type of the service level objective. The mapping from these types to the types found in the Datadog Web UI can be found in the Datadog API `documentation page <https://docs.datadoghq.com/api/v1/service-level-objectives/#create-a-slo-object>`_. Valid values are ``metric``, ``monitor``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#type ServiceLevelObjective#type}
        :param description: A description of this service level objective. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#description ServiceLevelObjective#description}
        :param force_delete: A boolean indicating whether this monitor can be deleted even if it’s referenced by other resources (e.g. dashboards). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#force_delete ServiceLevelObjective#force_delete}
        :param groups: A static set of groups to filter monitor-based SLOs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#groups ServiceLevelObjective#groups}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#id ServiceLevelObjective#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param monitor_ids: A static set of monitor IDs to use as part of the SLO. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#monitor_ids ServiceLevelObjective#monitor_ids}
        :param query: query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#query ServiceLevelObjective#query}
        :param tags: A list of tags to associate with your service level objective. This can help you categorize and filter service level objectives in the service level objectives page of the UI. Note: it's not currently possible to filter by these tags when querying via the API Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#tags ServiceLevelObjective#tags}
        :param validate: Whether or not to validate the SLO. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#validate ServiceLevelObjective#validate}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(query, dict):
            query = ServiceLevelObjectiveQuery(**query)
        if __debug__:
            type_hints = typing.get_type_hints(ServiceLevelObjectiveConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument thresholds", value=thresholds, expected_type=type_hints["thresholds"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument force_delete", value=force_delete, expected_type=type_hints["force_delete"])
            check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument monitor_ids", value=monitor_ids, expected_type=type_hints["monitor_ids"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument validate", value=validate, expected_type=type_hints["validate"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "thresholds": thresholds,
            "type": type,
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
        if force_delete is not None:
            self._values["force_delete"] = force_delete
        if groups is not None:
            self._values["groups"] = groups
        if id is not None:
            self._values["id"] = id
        if monitor_ids is not None:
            self._values["monitor_ids"] = monitor_ids
        if query is not None:
            self._values["query"] = query
        if tags is not None:
            self._values["tags"] = tags
        if validate is not None:
            self._values["validate"] = validate

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
    def name(self) -> builtins.str:
        '''Name of Datadog service level objective.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#name ServiceLevelObjective#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def thresholds(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ServiceLevelObjectiveThresholds"]]:
        '''thresholds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#thresholds ServiceLevelObjective#thresholds}
        '''
        result = self._values.get("thresholds")
        assert result is not None, "Required property 'thresholds' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ServiceLevelObjectiveThresholds"]], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the service level objective.

        The mapping from these types to the types found in the Datadog Web UI can be found in the Datadog API `documentation page <https://docs.datadoghq.com/api/v1/service-level-objectives/#create-a-slo-object>`_. Valid values are ``metric``, ``monitor``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#type ServiceLevelObjective#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of this service level objective.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#description ServiceLevelObjective#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''A boolean indicating whether this monitor can be deleted even if it’s referenced by other resources (e.g. dashboards).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#force_delete ServiceLevelObjective#force_delete}
        '''
        result = self._values.get("force_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A static set of groups to filter monitor-based SLOs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#groups ServiceLevelObjective#groups}
        '''
        result = self._values.get("groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#id ServiceLevelObjective#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monitor_ids(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''A static set of monitor IDs to use as part of the SLO.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#monitor_ids ServiceLevelObjective#monitor_ids}
        '''
        result = self._values.get("monitor_ids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def query(self) -> typing.Optional["ServiceLevelObjectiveQuery"]:
        '''query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#query ServiceLevelObjective#query}
        '''
        result = self._values.get("query")
        return typing.cast(typing.Optional["ServiceLevelObjectiveQuery"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of tags to associate with your service level objective.

        This can help you categorize and filter service level objectives in the service level objectives page of the UI. Note: it's not currently possible to filter by these tags when querying via the API

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#tags ServiceLevelObjective#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def validate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not to validate the SLO.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#validate ServiceLevelObjective#validate}
        '''
        result = self._values.get("validate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceLevelObjectiveConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.serviceLevelObjective.ServiceLevelObjectiveQuery",
    jsii_struct_bases=[],
    name_mapping={"denominator": "denominator", "numerator": "numerator"},
)
class ServiceLevelObjectiveQuery:
    def __init__(self, *, denominator: builtins.str, numerator: builtins.str) -> None:
        '''
        :param denominator: The sum of the ``total`` events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#denominator ServiceLevelObjective#denominator}
        :param numerator: The sum of all the ``good`` events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#numerator ServiceLevelObjective#numerator}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceLevelObjectiveQuery.__init__)
            check_type(argname="argument denominator", value=denominator, expected_type=type_hints["denominator"])
            check_type(argname="argument numerator", value=numerator, expected_type=type_hints["numerator"])
        self._values: typing.Dict[str, typing.Any] = {
            "denominator": denominator,
            "numerator": numerator,
        }

    @builtins.property
    def denominator(self) -> builtins.str:
        '''The sum of the ``total`` events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#denominator ServiceLevelObjective#denominator}
        '''
        result = self._values.get("denominator")
        assert result is not None, "Required property 'denominator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def numerator(self) -> builtins.str:
        '''The sum of all the ``good`` events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#numerator ServiceLevelObjective#numerator}
        '''
        result = self._values.get("numerator")
        assert result is not None, "Required property 'numerator' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceLevelObjectiveQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceLevelObjectiveQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.serviceLevelObjective.ServiceLevelObjectiveQueryOutputReference",
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
            type_hints = typing.get_type_hints(ServiceLevelObjectiveQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="denominatorInput")
    def denominator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "denominatorInput"))

    @builtins.property
    @jsii.member(jsii_name="numeratorInput")
    def numerator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "numeratorInput"))

    @builtins.property
    @jsii.member(jsii_name="denominator")
    def denominator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "denominator"))

    @denominator.setter
    def denominator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveQueryOutputReference, "denominator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "denominator", value)

    @builtins.property
    @jsii.member(jsii_name="numerator")
    def numerator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "numerator"))

    @numerator.setter
    def numerator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveQueryOutputReference, "numerator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numerator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceLevelObjectiveQuery]:
        return typing.cast(typing.Optional[ServiceLevelObjectiveQuery], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceLevelObjectiveQuery],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.serviceLevelObjective.ServiceLevelObjectiveThresholds",
    jsii_struct_bases=[],
    name_mapping={"target": "target", "timeframe": "timeframe", "warning": "warning"},
)
class ServiceLevelObjectiveThresholds:
    def __init__(
        self,
        *,
        target: jsii.Number,
        timeframe: builtins.str,
        warning: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param target: The objective's target in``[0,100]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#target ServiceLevelObjective#target}
        :param timeframe: The time frame for the objective. The mapping from these types to the types found in the Datadog Web UI can be found in the Datadog API documentation page. Valid values are ``7d``, ``30d``, ``90d``, ``custom``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#timeframe ServiceLevelObjective#timeframe}
        :param warning: The objective's warning value in ``[0,100]``. This must be greater than the target value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#warning ServiceLevelObjective#warning}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceLevelObjectiveThresholds.__init__)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument timeframe", value=timeframe, expected_type=type_hints["timeframe"])
            check_type(argname="argument warning", value=warning, expected_type=type_hints["warning"])
        self._values: typing.Dict[str, typing.Any] = {
            "target": target,
            "timeframe": timeframe,
        }
        if warning is not None:
            self._values["warning"] = warning

    @builtins.property
    def target(self) -> jsii.Number:
        '''The objective's target in``[0,100]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#target ServiceLevelObjective#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def timeframe(self) -> builtins.str:
        '''The time frame for the objective.

        The mapping from these types to the types found in the Datadog Web UI can be found in the Datadog API documentation page. Valid values are ``7d``, ``30d``, ``90d``, ``custom``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#timeframe ServiceLevelObjective#timeframe}
        '''
        result = self._values.get("timeframe")
        assert result is not None, "Required property 'timeframe' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def warning(self) -> typing.Optional[jsii.Number]:
        '''The objective's warning value in ``[0,100]``. This must be greater than the target value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/service_level_objective#warning ServiceLevelObjective#warning}
        '''
        result = self._values.get("warning")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceLevelObjectiveThresholds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceLevelObjectiveThresholdsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.serviceLevelObjective.ServiceLevelObjectiveThresholdsList",
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
            type_hints = typing.get_type_hints(ServiceLevelObjectiveThresholdsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceLevelObjectiveThresholdsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceLevelObjectiveThresholdsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceLevelObjectiveThresholdsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveThresholdsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveThresholdsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveThresholdsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceLevelObjectiveThresholds]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceLevelObjectiveThresholds]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceLevelObjectiveThresholds]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveThresholdsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceLevelObjectiveThresholdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.serviceLevelObjective.ServiceLevelObjectiveThresholdsOutputReference",
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
            type_hints = typing.get_type_hints(ServiceLevelObjectiveThresholdsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetWarning")
    def reset_warning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarning", []))

    @builtins.property
    @jsii.member(jsii_name="targetDisplay")
    def target_display(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetDisplay"))

    @builtins.property
    @jsii.member(jsii_name="warningDisplay")
    def warning_display(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warningDisplay"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="timeframeInput")
    def timeframe_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeframeInput"))

    @builtins.property
    @jsii.member(jsii_name="warningInput")
    def warning_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "warningInput"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "target"))

    @target.setter
    def target(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveThresholdsOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="timeframe")
    def timeframe(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeframe"))

    @timeframe.setter
    def timeframe(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveThresholdsOutputReference, "timeframe").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeframe", value)

    @builtins.property
    @jsii.member(jsii_name="warning")
    def warning(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "warning"))

    @warning.setter
    def warning(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveThresholdsOutputReference, "warning").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warning", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceLevelObjectiveThresholds, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceLevelObjectiveThresholds, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceLevelObjectiveThresholds, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceLevelObjectiveThresholdsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ServiceLevelObjective",
    "ServiceLevelObjectiveConfig",
    "ServiceLevelObjectiveQuery",
    "ServiceLevelObjectiveQueryOutputReference",
    "ServiceLevelObjectiveThresholds",
    "ServiceLevelObjectiveThresholdsList",
    "ServiceLevelObjectiveThresholdsOutputReference",
]

publication.publish()
