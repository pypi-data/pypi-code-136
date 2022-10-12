'''
# `azurerm_synapse_sql_pool_workload_classifier`

Refer to the Terraform Registory for docs: [`azurerm_synapse_sql_pool_workload_classifier`](https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier).
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


class SynapseSqlPoolWorkloadClassifier(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.synapseSqlPoolWorkloadClassifier.SynapseSqlPoolWorkloadClassifier",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier azurerm_synapse_sql_pool_workload_classifier}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        member_name: builtins.str,
        name: builtins.str,
        workload_group_id: builtins.str,
        context: typing.Optional[builtins.str] = None,
        end_time: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        importance: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SynapseSqlPoolWorkloadClassifierTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier azurerm_synapse_sql_pool_workload_classifier} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param member_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#member_name SynapseSqlPoolWorkloadClassifier#member_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#name SynapseSqlPoolWorkloadClassifier#name}.
        :param workload_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#workload_group_id SynapseSqlPoolWorkloadClassifier#workload_group_id}.
        :param context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#context SynapseSqlPoolWorkloadClassifier#context}.
        :param end_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#end_time SynapseSqlPoolWorkloadClassifier#end_time}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#id SynapseSqlPoolWorkloadClassifier#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param importance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#importance SynapseSqlPoolWorkloadClassifier#importance}.
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#label SynapseSqlPoolWorkloadClassifier#label}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#start_time SynapseSqlPoolWorkloadClassifier#start_time}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#timeouts SynapseSqlPoolWorkloadClassifier#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SynapseSqlPoolWorkloadClassifier.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SynapseSqlPoolWorkloadClassifierConfig(
            member_name=member_name,
            name=name,
            workload_group_id=workload_group_id,
            context=context,
            end_time=end_time,
            id=id,
            importance=importance,
            label=label,
            start_time=start_time,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#create SynapseSqlPoolWorkloadClassifier#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#delete SynapseSqlPoolWorkloadClassifier#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#read SynapseSqlPoolWorkloadClassifier#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#update SynapseSqlPoolWorkloadClassifier#update}.
        '''
        value = SynapseSqlPoolWorkloadClassifierTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetContext")
    def reset_context(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContext", []))

    @jsii.member(jsii_name="resetEndTime")
    def reset_end_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndTime", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImportance")
    def reset_importance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImportance", []))

    @jsii.member(jsii_name="resetLabel")
    def reset_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabel", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

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
    def timeouts(self) -> "SynapseSqlPoolWorkloadClassifierTimeoutsOutputReference":
        return typing.cast("SynapseSqlPoolWorkloadClassifierTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="contextInput")
    def context_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contextInput"))

    @builtins.property
    @jsii.member(jsii_name="endTimeInput")
    def end_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="importanceInput")
    def importance_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "importanceInput"))

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="memberNameInput")
    def member_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "memberNameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SynapseSqlPoolWorkloadClassifierTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SynapseSqlPoolWorkloadClassifierTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="workloadGroupIdInput")
    def workload_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workloadGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "context"))

    @context.setter
    def context(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadClassifier, "context").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "context", value)

    @builtins.property
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endTime"))

    @end_time.setter
    def end_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadClassifier, "end_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endTime", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadClassifier, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="importance")
    def importance(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "importance"))

    @importance.setter
    def importance(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadClassifier, "importance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "importance", value)

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadClassifier, "label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="memberName")
    def member_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "memberName"))

    @member_name.setter
    def member_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadClassifier, "member_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memberName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadClassifier, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadClassifier, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="workloadGroupId")
    def workload_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workloadGroupId"))

    @workload_group_id.setter
    def workload_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadClassifier, "workload_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workloadGroupId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.synapseSqlPoolWorkloadClassifier.SynapseSqlPoolWorkloadClassifierConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "member_name": "memberName",
        "name": "name",
        "workload_group_id": "workloadGroupId",
        "context": "context",
        "end_time": "endTime",
        "id": "id",
        "importance": "importance",
        "label": "label",
        "start_time": "startTime",
        "timeouts": "timeouts",
    },
)
class SynapseSqlPoolWorkloadClassifierConfig(cdktf.TerraformMetaArguments):
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
        member_name: builtins.str,
        name: builtins.str,
        workload_group_id: builtins.str,
        context: typing.Optional[builtins.str] = None,
        end_time: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        importance: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SynapseSqlPoolWorkloadClassifierTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param member_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#member_name SynapseSqlPoolWorkloadClassifier#member_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#name SynapseSqlPoolWorkloadClassifier#name}.
        :param workload_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#workload_group_id SynapseSqlPoolWorkloadClassifier#workload_group_id}.
        :param context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#context SynapseSqlPoolWorkloadClassifier#context}.
        :param end_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#end_time SynapseSqlPoolWorkloadClassifier#end_time}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#id SynapseSqlPoolWorkloadClassifier#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param importance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#importance SynapseSqlPoolWorkloadClassifier#importance}.
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#label SynapseSqlPoolWorkloadClassifier#label}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#start_time SynapseSqlPoolWorkloadClassifier#start_time}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#timeouts SynapseSqlPoolWorkloadClassifier#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = SynapseSqlPoolWorkloadClassifierTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(SynapseSqlPoolWorkloadClassifierConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument member_name", value=member_name, expected_type=type_hints["member_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument workload_group_id", value=workload_group_id, expected_type=type_hints["workload_group_id"])
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument importance", value=importance, expected_type=type_hints["importance"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "member_name": member_name,
            "name": name,
            "workload_group_id": workload_group_id,
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
        if context is not None:
            self._values["context"] = context
        if end_time is not None:
            self._values["end_time"] = end_time
        if id is not None:
            self._values["id"] = id
        if importance is not None:
            self._values["importance"] = importance
        if label is not None:
            self._values["label"] = label
        if start_time is not None:
            self._values["start_time"] = start_time
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
    def member_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#member_name SynapseSqlPoolWorkloadClassifier#member_name}.'''
        result = self._values.get("member_name")
        assert result is not None, "Required property 'member_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#name SynapseSqlPoolWorkloadClassifier#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workload_group_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#workload_group_id SynapseSqlPoolWorkloadClassifier#workload_group_id}.'''
        result = self._values.get("workload_group_id")
        assert result is not None, "Required property 'workload_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def context(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#context SynapseSqlPoolWorkloadClassifier#context}.'''
        result = self._values.get("context")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def end_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#end_time SynapseSqlPoolWorkloadClassifier#end_time}.'''
        result = self._values.get("end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#id SynapseSqlPoolWorkloadClassifier#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def importance(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#importance SynapseSqlPoolWorkloadClassifier#importance}.'''
        result = self._values.get("importance")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#label SynapseSqlPoolWorkloadClassifier#label}.'''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#start_time SynapseSqlPoolWorkloadClassifier#start_time}.'''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SynapseSqlPoolWorkloadClassifierTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#timeouts SynapseSqlPoolWorkloadClassifier#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SynapseSqlPoolWorkloadClassifierTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SynapseSqlPoolWorkloadClassifierConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.synapseSqlPoolWorkloadClassifier.SynapseSqlPoolWorkloadClassifierTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class SynapseSqlPoolWorkloadClassifierTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#create SynapseSqlPoolWorkloadClassifier#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#delete SynapseSqlPoolWorkloadClassifier#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#read SynapseSqlPoolWorkloadClassifier#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#update SynapseSqlPoolWorkloadClassifier#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SynapseSqlPoolWorkloadClassifierTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#create SynapseSqlPoolWorkloadClassifier#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#delete SynapseSqlPoolWorkloadClassifier#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#read SynapseSqlPoolWorkloadClassifier#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_sql_pool_workload_classifier#update SynapseSqlPoolWorkloadClassifier#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SynapseSqlPoolWorkloadClassifierTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SynapseSqlPoolWorkloadClassifierTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.synapseSqlPoolWorkloadClassifier.SynapseSqlPoolWorkloadClassifierTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(SynapseSqlPoolWorkloadClassifierTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadClassifierTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadClassifierTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadClassifierTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadClassifierTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SynapseSqlPoolWorkloadClassifierTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SynapseSqlPoolWorkloadClassifierTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SynapseSqlPoolWorkloadClassifierTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseSqlPoolWorkloadClassifierTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SynapseSqlPoolWorkloadClassifier",
    "SynapseSqlPoolWorkloadClassifierConfig",
    "SynapseSqlPoolWorkloadClassifierTimeouts",
    "SynapseSqlPoolWorkloadClassifierTimeoutsOutputReference",
]

publication.publish()
