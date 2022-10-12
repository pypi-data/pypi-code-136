'''
# `google_data_loss_prevention_job_trigger`

Refer to the Terraform Registory for docs: [`google_data_loss_prevention_job_trigger`](https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger).
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


class GoogleDataLossPreventionJobTrigger(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTrigger",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger google_data_loss_prevention_job_trigger}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        parent: builtins.str,
        triggers: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDataLossPreventionJobTriggerTriggers", typing.Dict[str, typing.Any]]]],
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        inspect_job: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJob", typing.Dict[str, typing.Any]]] = None,
        status: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger google_data_loss_prevention_job_trigger} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param parent: The parent of the trigger, either in the format 'projects/{{project}}' or 'projects/{{project}}/locations/{{location}}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#parent GoogleDataLossPreventionJobTrigger#parent}
        :param triggers: triggers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#triggers GoogleDataLossPreventionJobTrigger#triggers}
        :param description: A description of the job trigger. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#description GoogleDataLossPreventionJobTrigger#description}
        :param display_name: User set display name of the job trigger. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#display_name GoogleDataLossPreventionJobTrigger#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#id GoogleDataLossPreventionJobTrigger#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inspect_job: inspect_job block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#inspect_job GoogleDataLossPreventionJobTrigger#inspect_job}
        :param status: Whether the trigger is currently active. Default value: "HEALTHY" Possible values: ["PAUSED", "HEALTHY", "CANCELLED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#status GoogleDataLossPreventionJobTrigger#status}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#timeouts GoogleDataLossPreventionJobTrigger#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTrigger.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleDataLossPreventionJobTriggerConfig(
            parent=parent,
            triggers=triggers,
            description=description,
            display_name=display_name,
            id=id,
            inspect_job=inspect_job,
            status=status,
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

    @jsii.member(jsii_name="putInspectJob")
    def put_inspect_job(
        self,
        *,
        actions: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobActions", typing.Dict[str, typing.Any]]]],
        inspect_template_name: builtins.str,
        storage_config: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfig", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#actions GoogleDataLossPreventionJobTrigger#actions}
        :param inspect_template_name: The name of the template to run when this job is triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#inspect_template_name GoogleDataLossPreventionJobTrigger#inspect_template_name}
        :param storage_config: storage_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#storage_config GoogleDataLossPreventionJobTrigger#storage_config}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJob(
            actions=actions,
            inspect_template_name=inspect_template_name,
            storage_config=storage_config,
        )

        return typing.cast(None, jsii.invoke(self, "putInspectJob", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#create GoogleDataLossPreventionJobTrigger#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#delete GoogleDataLossPreventionJobTrigger#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#update GoogleDataLossPreventionJobTrigger#update}.
        '''
        value = GoogleDataLossPreventionJobTriggerTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTriggers")
    def put_triggers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDataLossPreventionJobTriggerTriggers", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTrigger.put_triggers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTriggers", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInspectJob")
    def reset_inspect_job(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInspectJob", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

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
    @jsii.member(jsii_name="inspectJob")
    def inspect_job(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobOutputReference", jsii.get(self, "inspectJob"))

    @builtins.property
    @jsii.member(jsii_name="lastRunTime")
    def last_run_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastRunTime"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleDataLossPreventionJobTriggerTimeoutsOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="triggers")
    def triggers(self) -> "GoogleDataLossPreventionJobTriggerTriggersList":
        return typing.cast("GoogleDataLossPreventionJobTriggerTriggersList", jsii.get(self, "triggers"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inspectJobInput")
    def inspect_job_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJob"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJob"], jsii.get(self, "inspectJobInput"))

    @builtins.property
    @jsii.member(jsii_name="parentInput")
    def parent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="triggersInput")
    def triggers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDataLossPreventionJobTriggerTriggers"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDataLossPreventionJobTriggerTriggers"]]], jsii.get(self, "triggersInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTrigger, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTrigger, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTrigger, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parent"))

    @parent.setter
    def parent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTrigger, "parent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parent", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTrigger, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "parent": "parent",
        "triggers": "triggers",
        "description": "description",
        "display_name": "displayName",
        "id": "id",
        "inspect_job": "inspectJob",
        "status": "status",
        "timeouts": "timeouts",
    },
)
class GoogleDataLossPreventionJobTriggerConfig(cdktf.TerraformMetaArguments):
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
        parent: builtins.str,
        triggers: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDataLossPreventionJobTriggerTriggers", typing.Dict[str, typing.Any]]]],
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        inspect_job: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJob", typing.Dict[str, typing.Any]]] = None,
        status: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param parent: The parent of the trigger, either in the format 'projects/{{project}}' or 'projects/{{project}}/locations/{{location}}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#parent GoogleDataLossPreventionJobTrigger#parent}
        :param triggers: triggers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#triggers GoogleDataLossPreventionJobTrigger#triggers}
        :param description: A description of the job trigger. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#description GoogleDataLossPreventionJobTrigger#description}
        :param display_name: User set display name of the job trigger. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#display_name GoogleDataLossPreventionJobTrigger#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#id GoogleDataLossPreventionJobTrigger#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inspect_job: inspect_job block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#inspect_job GoogleDataLossPreventionJobTrigger#inspect_job}
        :param status: Whether the trigger is currently active. Default value: "HEALTHY" Possible values: ["PAUSED", "HEALTHY", "CANCELLED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#status GoogleDataLossPreventionJobTrigger#status}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#timeouts GoogleDataLossPreventionJobTrigger#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(inspect_job, dict):
            inspect_job = GoogleDataLossPreventionJobTriggerInspectJob(**inspect_job)
        if isinstance(timeouts, dict):
            timeouts = GoogleDataLossPreventionJobTriggerTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument triggers", value=triggers, expected_type=type_hints["triggers"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument inspect_job", value=inspect_job, expected_type=type_hints["inspect_job"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "parent": parent,
            "triggers": triggers,
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
        if display_name is not None:
            self._values["display_name"] = display_name
        if id is not None:
            self._values["id"] = id
        if inspect_job is not None:
            self._values["inspect_job"] = inspect_job
        if status is not None:
            self._values["status"] = status
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
    def parent(self) -> builtins.str:
        '''The parent of the trigger, either in the format 'projects/{{project}}' or 'projects/{{project}}/locations/{{location}}'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#parent GoogleDataLossPreventionJobTrigger#parent}
        '''
        result = self._values.get("parent")
        assert result is not None, "Required property 'parent' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def triggers(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleDataLossPreventionJobTriggerTriggers"]]:
        '''triggers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#triggers GoogleDataLossPreventionJobTrigger#triggers}
        '''
        result = self._values.get("triggers")
        assert result is not None, "Required property 'triggers' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleDataLossPreventionJobTriggerTriggers"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the job trigger.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#description GoogleDataLossPreventionJobTrigger#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''User set display name of the job trigger.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#display_name GoogleDataLossPreventionJobTrigger#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#id GoogleDataLossPreventionJobTrigger#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inspect_job(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJob"]:
        '''inspect_job block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#inspect_job GoogleDataLossPreventionJobTrigger#inspect_job}
        '''
        result = self._values.get("inspect_job")
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJob"], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Whether the trigger is currently active. Default value: "HEALTHY" Possible values: ["PAUSED", "HEALTHY", "CANCELLED"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#status GoogleDataLossPreventionJobTrigger#status}
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleDataLossPreventionJobTriggerTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#timeouts GoogleDataLossPreventionJobTrigger#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJob",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "inspect_template_name": "inspectTemplateName",
        "storage_config": "storageConfig",
    },
)
class GoogleDataLossPreventionJobTriggerInspectJob:
    def __init__(
        self,
        *,
        actions: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobActions", typing.Dict[str, typing.Any]]]],
        inspect_template_name: builtins.str,
        storage_config: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfig", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#actions GoogleDataLossPreventionJobTrigger#actions}
        :param inspect_template_name: The name of the template to run when this job is triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#inspect_template_name GoogleDataLossPreventionJobTrigger#inspect_template_name}
        :param storage_config: storage_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#storage_config GoogleDataLossPreventionJobTrigger#storage_config}
        '''
        if isinstance(storage_config, dict):
            storage_config = GoogleDataLossPreventionJobTriggerInspectJobStorageConfig(**storage_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJob.__init__)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument inspect_template_name", value=inspect_template_name, expected_type=type_hints["inspect_template_name"])
            check_type(argname="argument storage_config", value=storage_config, expected_type=type_hints["storage_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "actions": actions,
            "inspect_template_name": inspect_template_name,
            "storage_config": storage_config,
        }

    @builtins.property
    def actions(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleDataLossPreventionJobTriggerInspectJobActions"]]:
        '''actions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#actions GoogleDataLossPreventionJobTrigger#actions}
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleDataLossPreventionJobTriggerInspectJobActions"]], result)

    @builtins.property
    def inspect_template_name(self) -> builtins.str:
        '''The name of the template to run when this job is triggered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#inspect_template_name GoogleDataLossPreventionJobTrigger#inspect_template_name}
        '''
        result = self._values.get("inspect_template_name")
        assert result is not None, "Required property 'inspect_template_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_config(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfig":
        '''storage_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#storage_config GoogleDataLossPreventionJobTrigger#storage_config}
        '''
        result = self._values.get("storage_config")
        assert result is not None, "Required property 'storage_config' is missing"
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfig", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJob(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActions",
    jsii_struct_bases=[],
    name_mapping={"save_findings": "saveFindings"},
)
class GoogleDataLossPreventionJobTriggerInspectJobActions:
    def __init__(
        self,
        *,
        save_findings: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param save_findings: save_findings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#save_findings GoogleDataLossPreventionJobTrigger#save_findings}
        '''
        if isinstance(save_findings, dict):
            save_findings = GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings(**save_findings)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobActions.__init__)
            check_type(argname="argument save_findings", value=save_findings, expected_type=type_hints["save_findings"])
        self._values: typing.Dict[str, typing.Any] = {
            "save_findings": save_findings,
        }

    @builtins.property
    def save_findings(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings":
        '''save_findings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#save_findings GoogleDataLossPreventionJobTrigger#save_findings}
        '''
        result = self._values.get("save_findings")
        assert result is not None, "Required property 'save_findings' is missing"
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobActionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActionsList",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobActionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobActionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobActionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobActionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobActionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobActionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobActionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataLossPreventionJobTriggerInspectJobActions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataLossPreventionJobTriggerInspectJobActions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataLossPreventionJobTriggerInspectJobActions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobActionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataLossPreventionJobTriggerInspectJobActionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobActionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putSaveFindings")
    def put_save_findings(
        self,
        *,
        output_config: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param output_config: output_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#output_config GoogleDataLossPreventionJobTrigger#output_config}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings(
            output_config=output_config
        )

        return typing.cast(None, jsii.invoke(self, "putSaveFindings", [value]))

    @builtins.property
    @jsii.member(jsii_name="saveFindings")
    def save_findings(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputReference", jsii.get(self, "saveFindings"))

    @builtins.property
    @jsii.member(jsii_name="saveFindingsInput")
    def save_findings_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings"], jsii.get(self, "saveFindingsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobActions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobActions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobActions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobActionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings",
    jsii_struct_bases=[],
    name_mapping={"output_config": "outputConfig"},
)
class GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings:
    def __init__(
        self,
        *,
        output_config: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param output_config: output_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#output_config GoogleDataLossPreventionJobTrigger#output_config}
        '''
        if isinstance(output_config, dict):
            output_config = GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig(**output_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings.__init__)
            check_type(argname="argument output_config", value=output_config, expected_type=type_hints["output_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "output_config": output_config,
        }

    @builtins.property
    def output_config(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig":
        '''output_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#output_config GoogleDataLossPreventionJobTrigger#output_config}
        '''
        result = self._values.get("output_config")
        assert result is not None, "Required property 'output_config' is missing"
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig",
    jsii_struct_bases=[],
    name_mapping={"table": "table", "output_schema": "outputSchema"},
)
class GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig:
    def __init__(
        self,
        *,
        table: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable", typing.Dict[str, typing.Any]],
        output_schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param table: table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table GoogleDataLossPreventionJobTrigger#table}
        :param output_schema: Schema used for writing the findings for Inspect jobs. This field is only used for Inspect and must be unspecified for Risk jobs. Columns are derived from the Finding object. If appending to an existing table, any columns from the predefined schema that are missing will be added. No columns in the existing table will be deleted. If unspecified, then all available columns will be used for a new table or an (existing) table with no schema, and no changes will be made to an existing table that has a schema. Only for use with external storage. Possible values: ["BASIC_COLUMNS", "GCS_COLUMNS", "DATASTORE_COLUMNS", "BIG_QUERY_COLUMNS", "ALL_COLUMNS"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#output_schema GoogleDataLossPreventionJobTrigger#output_schema}
        '''
        if isinstance(table, dict):
            table = GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable(**table)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig.__init__)
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument output_schema", value=output_schema, expected_type=type_hints["output_schema"])
        self._values: typing.Dict[str, typing.Any] = {
            "table": table,
        }
        if output_schema is not None:
            self._values["output_schema"] = output_schema

    @builtins.property
    def table(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable":
        '''table block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table GoogleDataLossPreventionJobTrigger#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable", result)

    @builtins.property
    def output_schema(self) -> typing.Optional[builtins.str]:
        '''Schema used for writing the findings for Inspect jobs.

        This field is only used for
        Inspect and must be unspecified for Risk jobs. Columns are derived from the Finding
        object. If appending to an existing table, any columns from the predefined schema
        that are missing will be added. No columns in the existing table will be deleted.

        If unspecified, then all available columns will be used for a new table or an (existing)
        table with no schema, and no changes will be made to an existing table that has a schema.
        Only for use with external storage. Possible values: ["BASIC_COLUMNS", "GCS_COLUMNS", "DATASTORE_COLUMNS", "BIG_QUERY_COLUMNS", "ALL_COLUMNS"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#output_schema GoogleDataLossPreventionJobTrigger#output_schema}
        '''
        result = self._values.get("output_schema")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTable")
    def put_table(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
        table_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dataset_id: Dataset ID of the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#dataset_id GoogleDataLossPreventionJobTrigger#dataset_id}
        :param project_id: The Google Cloud Platform project ID of the project containing the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#project_id GoogleDataLossPreventionJobTrigger#project_id}
        :param table_id: Name of the table. If is not set a new one will be generated for you with the following format: 'dlp_googleapis_yyyy_mm_dd_[dlp_job_id]'. Pacific timezone will be used for generating the date details. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table_id GoogleDataLossPreventionJobTrigger#table_id}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable(
            dataset_id=dataset_id, project_id=project_id, table_id=table_id
        )

        return typing.cast(None, jsii.invoke(self, "putTable", [value]))

    @jsii.member(jsii_name="resetOutputSchema")
    def reset_output_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputSchema", []))

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTableOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTableOutputReference", jsii.get(self, "table"))

    @builtins.property
    @jsii.member(jsii_name="outputSchemaInput")
    def output_schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable"], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="outputSchema")
    def output_schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputSchema"))

    @output_schema.setter
    def output_schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigOutputReference, "output_schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputSchema", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable",
    jsii_struct_bases=[],
    name_mapping={
        "dataset_id": "datasetId",
        "project_id": "projectId",
        "table_id": "tableId",
    },
)
class GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable:
    def __init__(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
        table_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dataset_id: Dataset ID of the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#dataset_id GoogleDataLossPreventionJobTrigger#dataset_id}
        :param project_id: The Google Cloud Platform project ID of the project containing the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#project_id GoogleDataLossPreventionJobTrigger#project_id}
        :param table_id: Name of the table. If is not set a new one will be generated for you with the following format: 'dlp_googleapis_yyyy_mm_dd_[dlp_job_id]'. Pacific timezone will be used for generating the date details. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table_id GoogleDataLossPreventionJobTrigger#table_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable.__init__)
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataset_id": dataset_id,
            "project_id": project_id,
        }
        if table_id is not None:
            self._values["table_id"] = table_id

    @builtins.property
    def dataset_id(self) -> builtins.str:
        '''Dataset ID of the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#dataset_id GoogleDataLossPreventionJobTrigger#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The Google Cloud Platform project ID of the project containing the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#project_id GoogleDataLossPreventionJobTrigger#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_id(self) -> typing.Optional[builtins.str]:
        '''Name of the table.

        If is not set a new one will be generated for you with the following format:
        'dlp_googleapis_yyyy_mm_dd_[dlp_job_id]'. Pacific timezone will be used for generating the date details.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table_id GoogleDataLossPreventionJobTrigger#table_id}
        '''
        result = self._values.get("table_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTableOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTableOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTableId")
    def reset_table_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTableId", []))

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tableIdInput")
    def table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTableOutputReference, "dataset_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTableOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="tableId")
    def table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableId"))

    @table_id.setter
    def table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTableOutputReference, "table_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTableOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOutputConfig")
    def put_output_config(
        self,
        *,
        table: typing.Union[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable, typing.Dict[str, typing.Any]],
        output_schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param table: table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table GoogleDataLossPreventionJobTrigger#table}
        :param output_schema: Schema used for writing the findings for Inspect jobs. This field is only used for Inspect and must be unspecified for Risk jobs. Columns are derived from the Finding object. If appending to an existing table, any columns from the predefined schema that are missing will be added. No columns in the existing table will be deleted. If unspecified, then all available columns will be used for a new table or an (existing) table with no schema, and no changes will be made to an existing table that has a schema. Only for use with external storage. Possible values: ["BASIC_COLUMNS", "GCS_COLUMNS", "DATASTORE_COLUMNS", "BIG_QUERY_COLUMNS", "ALL_COLUMNS"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#output_schema GoogleDataLossPreventionJobTrigger#output_schema}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig(
            table=table, output_schema=output_schema
        )

        return typing.cast(None, jsii.invoke(self, "putOutputConfig", [value]))

    @builtins.property
    @jsii.member(jsii_name="outputConfig")
    def output_config(
        self,
    ) -> GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigOutputReference:
        return typing.cast(GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigOutputReference, jsii.get(self, "outputConfig"))

    @builtins.property
    @jsii.member(jsii_name="outputConfigInput")
    def output_config_input(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig], jsii.get(self, "outputConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataLossPreventionJobTriggerInspectJobOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putActions")
    def put_actions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobActions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobOutputReference.put_actions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putActions", [value]))

    @jsii.member(jsii_name="putStorageConfig")
    def put_storage_config(
        self,
        *,
        big_query_options: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions", typing.Dict[str, typing.Any]]] = None,
        cloud_storage_options: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions", typing.Dict[str, typing.Any]]] = None,
        datastore_options: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions", typing.Dict[str, typing.Any]]] = None,
        timespan_config: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param big_query_options: big_query_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#big_query_options GoogleDataLossPreventionJobTrigger#big_query_options}
        :param cloud_storage_options: cloud_storage_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#cloud_storage_options GoogleDataLossPreventionJobTrigger#cloud_storage_options}
        :param datastore_options: datastore_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#datastore_options GoogleDataLossPreventionJobTrigger#datastore_options}
        :param timespan_config: timespan_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#timespan_config GoogleDataLossPreventionJobTrigger#timespan_config}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfig(
            big_query_options=big_query_options,
            cloud_storage_options=cloud_storage_options,
            datastore_options=datastore_options,
            timespan_config=timespan_config,
        )

        return typing.cast(None, jsii.invoke(self, "putStorageConfig", [value]))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(self) -> GoogleDataLossPreventionJobTriggerInspectJobActionsList:
        return typing.cast(GoogleDataLossPreventionJobTriggerInspectJobActionsList, jsii.get(self, "actions"))

    @builtins.property
    @jsii.member(jsii_name="storageConfig")
    def storage_config(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigOutputReference", jsii.get(self, "storageConfig"))

    @builtins.property
    @jsii.member(jsii_name="actionsInput")
    def actions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataLossPreventionJobTriggerInspectJobActions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataLossPreventionJobTriggerInspectJobActions]]], jsii.get(self, "actionsInput"))

    @builtins.property
    @jsii.member(jsii_name="inspectTemplateNameInput")
    def inspect_template_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inspectTemplateNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageConfigInput")
    def storage_config_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfig"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfig"], jsii.get(self, "storageConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="inspectTemplateName")
    def inspect_template_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inspectTemplateName"))

    @inspect_template_name.setter
    def inspect_template_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobOutputReference, "inspect_template_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inspectTemplateName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJob]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJob], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJob],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfig",
    jsii_struct_bases=[],
    name_mapping={
        "big_query_options": "bigQueryOptions",
        "cloud_storage_options": "cloudStorageOptions",
        "datastore_options": "datastoreOptions",
        "timespan_config": "timespanConfig",
    },
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfig:
    def __init__(
        self,
        *,
        big_query_options: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions", typing.Dict[str, typing.Any]]] = None,
        cloud_storage_options: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions", typing.Dict[str, typing.Any]]] = None,
        datastore_options: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions", typing.Dict[str, typing.Any]]] = None,
        timespan_config: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param big_query_options: big_query_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#big_query_options GoogleDataLossPreventionJobTrigger#big_query_options}
        :param cloud_storage_options: cloud_storage_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#cloud_storage_options GoogleDataLossPreventionJobTrigger#cloud_storage_options}
        :param datastore_options: datastore_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#datastore_options GoogleDataLossPreventionJobTrigger#datastore_options}
        :param timespan_config: timespan_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#timespan_config GoogleDataLossPreventionJobTrigger#timespan_config}
        '''
        if isinstance(big_query_options, dict):
            big_query_options = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions(**big_query_options)
        if isinstance(cloud_storage_options, dict):
            cloud_storage_options = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions(**cloud_storage_options)
        if isinstance(datastore_options, dict):
            datastore_options = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions(**datastore_options)
        if isinstance(timespan_config, dict):
            timespan_config = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig(**timespan_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfig.__init__)
            check_type(argname="argument big_query_options", value=big_query_options, expected_type=type_hints["big_query_options"])
            check_type(argname="argument cloud_storage_options", value=cloud_storage_options, expected_type=type_hints["cloud_storage_options"])
            check_type(argname="argument datastore_options", value=datastore_options, expected_type=type_hints["datastore_options"])
            check_type(argname="argument timespan_config", value=timespan_config, expected_type=type_hints["timespan_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if big_query_options is not None:
            self._values["big_query_options"] = big_query_options
        if cloud_storage_options is not None:
            self._values["cloud_storage_options"] = cloud_storage_options
        if datastore_options is not None:
            self._values["datastore_options"] = datastore_options
        if timespan_config is not None:
            self._values["timespan_config"] = timespan_config

    @builtins.property
    def big_query_options(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions"]:
        '''big_query_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#big_query_options GoogleDataLossPreventionJobTrigger#big_query_options}
        '''
        result = self._values.get("big_query_options")
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions"], result)

    @builtins.property
    def cloud_storage_options(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions"]:
        '''cloud_storage_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#cloud_storage_options GoogleDataLossPreventionJobTrigger#cloud_storage_options}
        '''
        result = self._values.get("cloud_storage_options")
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions"], result)

    @builtins.property
    def datastore_options(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions"]:
        '''datastore_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#datastore_options GoogleDataLossPreventionJobTrigger#datastore_options}
        '''
        result = self._values.get("datastore_options")
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions"], result)

    @builtins.property
    def timespan_config(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig"]:
        '''timespan_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#timespan_config GoogleDataLossPreventionJobTrigger#timespan_config}
        '''
        result = self._values.get("timespan_config")
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions",
    jsii_struct_bases=[],
    name_mapping={"table_reference": "tableReference"},
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions:
    def __init__(
        self,
        *,
        table_reference: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param table_reference: table_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table_reference GoogleDataLossPreventionJobTrigger#table_reference}
        '''
        if isinstance(table_reference, dict):
            table_reference = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference(**table_reference)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions.__init__)
            check_type(argname="argument table_reference", value=table_reference, expected_type=type_hints["table_reference"])
        self._values: typing.Dict[str, typing.Any] = {
            "table_reference": table_reference,
        }

    @builtins.property
    def table_reference(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference":
        '''table_reference block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table_reference GoogleDataLossPreventionJobTrigger#table_reference}
        '''
        result = self._values.get("table_reference")
        assert result is not None, "Required property 'table_reference' is missing"
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTableReference")
    def put_table_reference(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
        table_id: builtins.str,
    ) -> None:
        '''
        :param dataset_id: The dataset ID of the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#dataset_id GoogleDataLossPreventionJobTrigger#dataset_id}
        :param project_id: The Google Cloud Platform project ID of the project containing the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#project_id GoogleDataLossPreventionJobTrigger#project_id}
        :param table_id: The name of the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table_id GoogleDataLossPreventionJobTrigger#table_id}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference(
            dataset_id=dataset_id, project_id=project_id, table_id=table_id
        )

        return typing.cast(None, jsii.invoke(self, "putTableReference", [value]))

    @builtins.property
    @jsii.member(jsii_name="tableReference")
    def table_reference(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceOutputReference", jsii.get(self, "tableReference"))

    @builtins.property
    @jsii.member(jsii_name="tableReferenceInput")
    def table_reference_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference"], jsii.get(self, "tableReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference",
    jsii_struct_bases=[],
    name_mapping={
        "dataset_id": "datasetId",
        "project_id": "projectId",
        "table_id": "tableId",
    },
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference:
    def __init__(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
        table_id: builtins.str,
    ) -> None:
        '''
        :param dataset_id: The dataset ID of the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#dataset_id GoogleDataLossPreventionJobTrigger#dataset_id}
        :param project_id: The Google Cloud Platform project ID of the project containing the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#project_id GoogleDataLossPreventionJobTrigger#project_id}
        :param table_id: The name of the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table_id GoogleDataLossPreventionJobTrigger#table_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference.__init__)
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataset_id": dataset_id,
            "project_id": project_id,
            "table_id": table_id,
        }

    @builtins.property
    def dataset_id(self) -> builtins.str:
        '''The dataset ID of the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#dataset_id GoogleDataLossPreventionJobTrigger#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The Google Cloud Platform project ID of the project containing the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#project_id GoogleDataLossPreventionJobTrigger#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_id(self) -> builtins.str:
        '''The name of the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table_id GoogleDataLossPreventionJobTrigger#table_id}
        '''
        result = self._values.get("table_id")
        assert result is not None, "Required property 'table_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tableIdInput")
    def table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceOutputReference, "dataset_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="tableId")
    def table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableId"))

    @table_id.setter
    def table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceOutputReference, "table_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions",
    jsii_struct_bases=[],
    name_mapping={
        "file_set": "fileSet",
        "bytes_limit_per_file": "bytesLimitPerFile",
        "bytes_limit_per_file_percent": "bytesLimitPerFilePercent",
        "files_limit_percent": "filesLimitPercent",
        "file_types": "fileTypes",
        "sample_method": "sampleMethod",
    },
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions:
    def __init__(
        self,
        *,
        file_set: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet", typing.Dict[str, typing.Any]],
        bytes_limit_per_file: typing.Optional[jsii.Number] = None,
        bytes_limit_per_file_percent: typing.Optional[jsii.Number] = None,
        files_limit_percent: typing.Optional[jsii.Number] = None,
        file_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        sample_method: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file_set: file_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#file_set GoogleDataLossPreventionJobTrigger#file_set}
        :param bytes_limit_per_file: Max number of bytes to scan from a file. If a scanned file's size is bigger than this value then the rest of the bytes are omitted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#bytes_limit_per_file GoogleDataLossPreventionJobTrigger#bytes_limit_per_file}
        :param bytes_limit_per_file_percent: Max percentage of bytes to scan from a file. The rest are omitted. The number of bytes scanned is rounded down. Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#bytes_limit_per_file_percent GoogleDataLossPreventionJobTrigger#bytes_limit_per_file_percent}
        :param files_limit_percent: Limits the number of files to scan to this percentage of the input FileSet. Number of files scanned is rounded down. Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#files_limit_percent GoogleDataLossPreventionJobTrigger#files_limit_percent}
        :param file_types: List of file type groups to include in the scan. If empty, all files are scanned and available data format processors are applied. In addition, the binary content of the selected files is always scanned as well. Images are scanned only as binary if the specified region does not support image inspection and no fileTypes were specified. Possible values: ["BINARY_FILE", "TEXT_FILE", "IMAGE", "WORD", "PDF", "AVRO", "CSV", "TSV"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#file_types GoogleDataLossPreventionJobTrigger#file_types}
        :param sample_method: How to sample bytes if not all bytes are scanned. Meaningful only when used in conjunction with bytesLimitPerFile. If not specified, scanning would start from the top. Possible values: ["TOP", "RANDOM_START"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#sample_method GoogleDataLossPreventionJobTrigger#sample_method}
        '''
        if isinstance(file_set, dict):
            file_set = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet(**file_set)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions.__init__)
            check_type(argname="argument file_set", value=file_set, expected_type=type_hints["file_set"])
            check_type(argname="argument bytes_limit_per_file", value=bytes_limit_per_file, expected_type=type_hints["bytes_limit_per_file"])
            check_type(argname="argument bytes_limit_per_file_percent", value=bytes_limit_per_file_percent, expected_type=type_hints["bytes_limit_per_file_percent"])
            check_type(argname="argument files_limit_percent", value=files_limit_percent, expected_type=type_hints["files_limit_percent"])
            check_type(argname="argument file_types", value=file_types, expected_type=type_hints["file_types"])
            check_type(argname="argument sample_method", value=sample_method, expected_type=type_hints["sample_method"])
        self._values: typing.Dict[str, typing.Any] = {
            "file_set": file_set,
        }
        if bytes_limit_per_file is not None:
            self._values["bytes_limit_per_file"] = bytes_limit_per_file
        if bytes_limit_per_file_percent is not None:
            self._values["bytes_limit_per_file_percent"] = bytes_limit_per_file_percent
        if files_limit_percent is not None:
            self._values["files_limit_percent"] = files_limit_percent
        if file_types is not None:
            self._values["file_types"] = file_types
        if sample_method is not None:
            self._values["sample_method"] = sample_method

    @builtins.property
    def file_set(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet":
        '''file_set block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#file_set GoogleDataLossPreventionJobTrigger#file_set}
        '''
        result = self._values.get("file_set")
        assert result is not None, "Required property 'file_set' is missing"
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet", result)

    @builtins.property
    def bytes_limit_per_file(self) -> typing.Optional[jsii.Number]:
        '''Max number of bytes to scan from a file.

        If a scanned file's size is bigger than this value
        then the rest of the bytes are omitted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#bytes_limit_per_file GoogleDataLossPreventionJobTrigger#bytes_limit_per_file}
        '''
        result = self._values.get("bytes_limit_per_file")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def bytes_limit_per_file_percent(self) -> typing.Optional[jsii.Number]:
        '''Max percentage of bytes to scan from a file.

        The rest are omitted. The number of bytes scanned is rounded down.
        Must be between 0 and 100, inclusively. Both 0 and 100 means no limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#bytes_limit_per_file_percent GoogleDataLossPreventionJobTrigger#bytes_limit_per_file_percent}
        '''
        result = self._values.get("bytes_limit_per_file_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def files_limit_percent(self) -> typing.Optional[jsii.Number]:
        '''Limits the number of files to scan to this percentage of the input FileSet.

        Number of files scanned is rounded down.
        Must be between 0 and 100, inclusively. Both 0 and 100 means no limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#files_limit_percent GoogleDataLossPreventionJobTrigger#files_limit_percent}
        '''
        result = self._values.get("files_limit_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def file_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of file type groups to include in the scan.

        If empty, all files are scanned and available data
        format processors are applied. In addition, the binary content of the selected files is always scanned as well.
        Images are scanned only as binary if the specified region does not support image inspection and no fileTypes were specified. Possible values: ["BINARY_FILE", "TEXT_FILE", "IMAGE", "WORD", "PDF", "AVRO", "CSV", "TSV"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#file_types GoogleDataLossPreventionJobTrigger#file_types}
        '''
        result = self._values.get("file_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sample_method(self) -> typing.Optional[builtins.str]:
        '''How to sample bytes if not all bytes are scanned.

        Meaningful only when used in conjunction with bytesLimitPerFile.
        If not specified, scanning would start from the top. Possible values: ["TOP", "RANDOM_START"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#sample_method GoogleDataLossPreventionJobTrigger#sample_method}
        '''
        result = self._values.get("sample_method")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet",
    jsii_struct_bases=[],
    name_mapping={"regex_file_set": "regexFileSet", "url": "url"},
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet:
    def __init__(
        self,
        *,
        regex_file_set: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet", typing.Dict[str, typing.Any]]] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param regex_file_set: regex_file_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#regex_file_set GoogleDataLossPreventionJobTrigger#regex_file_set}
        :param url: The Cloud Storage url of the file(s) to scan, in the format 'gs:///'. Trailing wildcard in the path is allowed. If the url ends in a trailing slash, the bucket or directory represented by the url will be scanned non-recursively (content in sub-directories will not be scanned). This means that 'gs://mybucket/' is equivalent to 'gs://mybucket/*', and 'gs://mybucket/directory/' is equivalent to 'gs://mybucket/directory/*'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#url GoogleDataLossPreventionJobTrigger#url}
        '''
        if isinstance(regex_file_set, dict):
            regex_file_set = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet(**regex_file_set)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet.__init__)
            check_type(argname="argument regex_file_set", value=regex_file_set, expected_type=type_hints["regex_file_set"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if regex_file_set is not None:
            self._values["regex_file_set"] = regex_file_set
        if url is not None:
            self._values["url"] = url

    @builtins.property
    def regex_file_set(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet"]:
        '''regex_file_set block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#regex_file_set GoogleDataLossPreventionJobTrigger#regex_file_set}
        '''
        result = self._values.get("regex_file_set")
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet"], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''The Cloud Storage url of the file(s) to scan, in the format 'gs:///'. Trailing wildcard in the path is allowed.

        If the url ends in a trailing slash, the bucket or directory represented by the url will be scanned
        non-recursively (content in sub-directories will not be scanned). This means that 'gs://mybucket/' is
        equivalent to 'gs://mybucket/*', and 'gs://mybucket/directory/' is equivalent to 'gs://mybucket/directory/*'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#url GoogleDataLossPreventionJobTrigger#url}
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRegexFileSet")
    def put_regex_file_set(
        self,
        *,
        bucket_name: builtins.str,
        exclude_regex: typing.Optional[typing.Sequence[builtins.str]] = None,
        include_regex: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param bucket_name: The name of a Cloud Storage bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#bucket_name GoogleDataLossPreventionJobTrigger#bucket_name}
        :param exclude_regex: A list of regular expressions matching file paths to exclude. All files in the bucket that match at least one of these regular expressions will be excluded from the scan. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#exclude_regex GoogleDataLossPreventionJobTrigger#exclude_regex}
        :param include_regex: A list of regular expressions matching file paths to include. All files in the bucket that match at least one of these regular expressions will be included in the set of files, except for those that also match an item in excludeRegex. Leaving this field empty will match all files by default (this is equivalent to including .* in the list) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#include_regex GoogleDataLossPreventionJobTrigger#include_regex}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet(
            bucket_name=bucket_name,
            exclude_regex=exclude_regex,
            include_regex=include_regex,
        )

        return typing.cast(None, jsii.invoke(self, "putRegexFileSet", [value]))

    @jsii.member(jsii_name="resetRegexFileSet")
    def reset_regex_file_set(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegexFileSet", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @builtins.property
    @jsii.member(jsii_name="regexFileSet")
    def regex_file_set(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetOutputReference", jsii.get(self, "regexFileSet"))

    @builtins.property
    @jsii.member(jsii_name="regexFileSetInput")
    def regex_file_set_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet"], jsii.get(self, "regexFileSetInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "exclude_regex": "excludeRegex",
        "include_regex": "includeRegex",
    },
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        exclude_regex: typing.Optional[typing.Sequence[builtins.str]] = None,
        include_regex: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param bucket_name: The name of a Cloud Storage bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#bucket_name GoogleDataLossPreventionJobTrigger#bucket_name}
        :param exclude_regex: A list of regular expressions matching file paths to exclude. All files in the bucket that match at least one of these regular expressions will be excluded from the scan. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#exclude_regex GoogleDataLossPreventionJobTrigger#exclude_regex}
        :param include_regex: A list of regular expressions matching file paths to include. All files in the bucket that match at least one of these regular expressions will be included in the set of files, except for those that also match an item in excludeRegex. Leaving this field empty will match all files by default (this is equivalent to including .* in the list) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#include_regex GoogleDataLossPreventionJobTrigger#include_regex}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet.__init__)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument exclude_regex", value=exclude_regex, expected_type=type_hints["exclude_regex"])
            check_type(argname="argument include_regex", value=include_regex, expected_type=type_hints["include_regex"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
        }
        if exclude_regex is not None:
            self._values["exclude_regex"] = exclude_regex
        if include_regex is not None:
            self._values["include_regex"] = include_regex

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''The name of a Cloud Storage bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#bucket_name GoogleDataLossPreventionJobTrigger#bucket_name}
        '''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclude_regex(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of regular expressions matching file paths to exclude.

        All files in the bucket that match at
        least one of these regular expressions will be excluded from the scan.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#exclude_regex GoogleDataLossPreventionJobTrigger#exclude_regex}
        '''
        result = self._values.get("exclude_regex")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def include_regex(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of regular expressions matching file paths to include.

        All files in the bucket
        that match at least one of these regular expressions will be included in the set of files,
        except for those that also match an item in excludeRegex. Leaving this field empty will
        match all files by default (this is equivalent to including .* in the list)

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#include_regex GoogleDataLossPreventionJobTrigger#include_regex}
        '''
        result = self._values.get("include_regex")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExcludeRegex")
    def reset_exclude_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeRegex", []))

    @jsii.member(jsii_name="resetIncludeRegex")
    def reset_include_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeRegex", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeRegexInput")
    def exclude_regex_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludeRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="includeRegexInput")
    def include_regex_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includeRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetOutputReference, "bucket_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="excludeRegex")
    def exclude_regex(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludeRegex"))

    @exclude_regex.setter
    def exclude_regex(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetOutputReference, "exclude_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeRegex", value)

    @builtins.property
    @jsii.member(jsii_name="includeRegex")
    def include_regex(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includeRegex"))

    @include_regex.setter
    def include_regex(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetOutputReference, "include_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeRegex", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFileSet")
    def put_file_set(
        self,
        *,
        regex_file_set: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet, typing.Dict[str, typing.Any]]] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param regex_file_set: regex_file_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#regex_file_set GoogleDataLossPreventionJobTrigger#regex_file_set}
        :param url: The Cloud Storage url of the file(s) to scan, in the format 'gs:///'. Trailing wildcard in the path is allowed. If the url ends in a trailing slash, the bucket or directory represented by the url will be scanned non-recursively (content in sub-directories will not be scanned). This means that 'gs://mybucket/' is equivalent to 'gs://mybucket/*', and 'gs://mybucket/directory/' is equivalent to 'gs://mybucket/directory/*'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#url GoogleDataLossPreventionJobTrigger#url}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet(
            regex_file_set=regex_file_set, url=url
        )

        return typing.cast(None, jsii.invoke(self, "putFileSet", [value]))

    @jsii.member(jsii_name="resetBytesLimitPerFile")
    def reset_bytes_limit_per_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBytesLimitPerFile", []))

    @jsii.member(jsii_name="resetBytesLimitPerFilePercent")
    def reset_bytes_limit_per_file_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBytesLimitPerFilePercent", []))

    @jsii.member(jsii_name="resetFilesLimitPercent")
    def reset_files_limit_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilesLimitPercent", []))

    @jsii.member(jsii_name="resetFileTypes")
    def reset_file_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileTypes", []))

    @jsii.member(jsii_name="resetSampleMethod")
    def reset_sample_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSampleMethod", []))

    @builtins.property
    @jsii.member(jsii_name="fileSet")
    def file_set(
        self,
    ) -> GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetOutputReference:
        return typing.cast(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetOutputReference, jsii.get(self, "fileSet"))

    @builtins.property
    @jsii.member(jsii_name="bytesLimitPerFileInput")
    def bytes_limit_per_file_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bytesLimitPerFileInput"))

    @builtins.property
    @jsii.member(jsii_name="bytesLimitPerFilePercentInput")
    def bytes_limit_per_file_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bytesLimitPerFilePercentInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSetInput")
    def file_set_input(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet], jsii.get(self, "fileSetInput"))

    @builtins.property
    @jsii.member(jsii_name="filesLimitPercentInput")
    def files_limit_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "filesLimitPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="fileTypesInput")
    def file_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "fileTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="sampleMethodInput")
    def sample_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sampleMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="bytesLimitPerFile")
    def bytes_limit_per_file(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bytesLimitPerFile"))

    @bytes_limit_per_file.setter
    def bytes_limit_per_file(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsOutputReference, "bytes_limit_per_file").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bytesLimitPerFile", value)

    @builtins.property
    @jsii.member(jsii_name="bytesLimitPerFilePercent")
    def bytes_limit_per_file_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bytesLimitPerFilePercent"))

    @bytes_limit_per_file_percent.setter
    def bytes_limit_per_file_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsOutputReference, "bytes_limit_per_file_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bytesLimitPerFilePercent", value)

    @builtins.property
    @jsii.member(jsii_name="filesLimitPercent")
    def files_limit_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "filesLimitPercent"))

    @files_limit_percent.setter
    def files_limit_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsOutputReference, "files_limit_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filesLimitPercent", value)

    @builtins.property
    @jsii.member(jsii_name="fileTypes")
    def file_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "fileTypes"))

    @file_types.setter
    def file_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsOutputReference, "file_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileTypes", value)

    @builtins.property
    @jsii.member(jsii_name="sampleMethod")
    def sample_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sampleMethod"))

    @sample_method.setter
    def sample_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsOutputReference, "sample_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleMethod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions",
    jsii_struct_bases=[],
    name_mapping={"kind": "kind", "partition_id": "partitionId"},
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions:
    def __init__(
        self,
        *,
        kind: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind", typing.Dict[str, typing.Any]],
        partition_id: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param kind: kind block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#kind GoogleDataLossPreventionJobTrigger#kind}
        :param partition_id: partition_id block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#partition_id GoogleDataLossPreventionJobTrigger#partition_id}
        '''
        if isinstance(kind, dict):
            kind = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind(**kind)
        if isinstance(partition_id, dict):
            partition_id = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId(**partition_id)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions.__init__)
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument partition_id", value=partition_id, expected_type=type_hints["partition_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "kind": kind,
            "partition_id": partition_id,
        }

    @builtins.property
    def kind(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind":
        '''kind block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#kind GoogleDataLossPreventionJobTrigger#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind", result)

    @builtins.property
    def partition_id(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId":
        '''partition_id block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#partition_id GoogleDataLossPreventionJobTrigger#partition_id}
        '''
        result = self._values.get("partition_id")
        assert result is not None, "Required property 'partition_id' is missing"
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: The name of the Datastore kind. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#name GoogleDataLossPreventionJobTrigger#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the Datastore kind.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#name GoogleDataLossPreventionJobTrigger#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putKind")
    def put_kind(self, *, name: builtins.str) -> None:
        '''
        :param name: The name of the Datastore kind. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#name GoogleDataLossPreventionJobTrigger#name}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind(
            name=name
        )

        return typing.cast(None, jsii.invoke(self, "putKind", [value]))

    @jsii.member(jsii_name="putPartitionId")
    def put_partition_id(
        self,
        *,
        project_id: builtins.str,
        namespace_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param project_id: The ID of the project to which the entities belong. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#project_id GoogleDataLossPreventionJobTrigger#project_id}
        :param namespace_id: If not empty, the ID of the namespace to which the entities belong. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#namespace_id GoogleDataLossPreventionJobTrigger#namespace_id}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId(
            project_id=project_id, namespace_id=namespace_id
        )

        return typing.cast(None, jsii.invoke(self, "putPartitionId", [value]))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(
        self,
    ) -> GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindOutputReference:
        return typing.cast(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindOutputReference, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="partitionId")
    def partition_id(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdOutputReference", jsii.get(self, "partitionId"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionIdInput")
    def partition_id_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId"], jsii.get(self, "partitionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId",
    jsii_struct_bases=[],
    name_mapping={"project_id": "projectId", "namespace_id": "namespaceId"},
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId:
    def __init__(
        self,
        *,
        project_id: builtins.str,
        namespace_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param project_id: The ID of the project to which the entities belong. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#project_id GoogleDataLossPreventionJobTrigger#project_id}
        :param namespace_id: If not empty, the ID of the namespace to which the entities belong. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#namespace_id GoogleDataLossPreventionJobTrigger#namespace_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId.__init__)
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument namespace_id", value=namespace_id, expected_type=type_hints["namespace_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "project_id": project_id,
        }
        if namespace_id is not None:
            self._values["namespace_id"] = namespace_id

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The ID of the project to which the entities belong.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#project_id GoogleDataLossPreventionJobTrigger#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace_id(self) -> typing.Optional[builtins.str]:
        '''If not empty, the ID of the namespace to which the entities belong.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#namespace_id GoogleDataLossPreventionJobTrigger#namespace_id}
        '''
        result = self._values.get("namespace_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNamespaceId")
    def reset_namespace_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespaceId", []))

    @builtins.property
    @jsii.member(jsii_name="namespaceIdInput")
    def namespace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespaceId"))

    @namespace_id.setter
    def namespace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdOutputReference, "namespace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBigQueryOptions")
    def put_big_query_options(
        self,
        *,
        table_reference: typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param table_reference: table_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table_reference GoogleDataLossPreventionJobTrigger#table_reference}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions(
            table_reference=table_reference
        )

        return typing.cast(None, jsii.invoke(self, "putBigQueryOptions", [value]))

    @jsii.member(jsii_name="putCloudStorageOptions")
    def put_cloud_storage_options(
        self,
        *,
        file_set: typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet, typing.Dict[str, typing.Any]],
        bytes_limit_per_file: typing.Optional[jsii.Number] = None,
        bytes_limit_per_file_percent: typing.Optional[jsii.Number] = None,
        files_limit_percent: typing.Optional[jsii.Number] = None,
        file_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        sample_method: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file_set: file_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#file_set GoogleDataLossPreventionJobTrigger#file_set}
        :param bytes_limit_per_file: Max number of bytes to scan from a file. If a scanned file's size is bigger than this value then the rest of the bytes are omitted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#bytes_limit_per_file GoogleDataLossPreventionJobTrigger#bytes_limit_per_file}
        :param bytes_limit_per_file_percent: Max percentage of bytes to scan from a file. The rest are omitted. The number of bytes scanned is rounded down. Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#bytes_limit_per_file_percent GoogleDataLossPreventionJobTrigger#bytes_limit_per_file_percent}
        :param files_limit_percent: Limits the number of files to scan to this percentage of the input FileSet. Number of files scanned is rounded down. Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#files_limit_percent GoogleDataLossPreventionJobTrigger#files_limit_percent}
        :param file_types: List of file type groups to include in the scan. If empty, all files are scanned and available data format processors are applied. In addition, the binary content of the selected files is always scanned as well. Images are scanned only as binary if the specified region does not support image inspection and no fileTypes were specified. Possible values: ["BINARY_FILE", "TEXT_FILE", "IMAGE", "WORD", "PDF", "AVRO", "CSV", "TSV"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#file_types GoogleDataLossPreventionJobTrigger#file_types}
        :param sample_method: How to sample bytes if not all bytes are scanned. Meaningful only when used in conjunction with bytesLimitPerFile. If not specified, scanning would start from the top. Possible values: ["TOP", "RANDOM_START"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#sample_method GoogleDataLossPreventionJobTrigger#sample_method}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions(
            file_set=file_set,
            bytes_limit_per_file=bytes_limit_per_file,
            bytes_limit_per_file_percent=bytes_limit_per_file_percent,
            files_limit_percent=files_limit_percent,
            file_types=file_types,
            sample_method=sample_method,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudStorageOptions", [value]))

    @jsii.member(jsii_name="putDatastoreOptions")
    def put_datastore_options(
        self,
        *,
        kind: typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind, typing.Dict[str, typing.Any]],
        partition_id: typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param kind: kind block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#kind GoogleDataLossPreventionJobTrigger#kind}
        :param partition_id: partition_id block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#partition_id GoogleDataLossPreventionJobTrigger#partition_id}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions(
            kind=kind, partition_id=partition_id
        )

        return typing.cast(None, jsii.invoke(self, "putDatastoreOptions", [value]))

    @jsii.member(jsii_name="putTimespanConfig")
    def put_timespan_config(
        self,
        *,
        timestamp_field: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField", typing.Dict[str, typing.Any]],
        enable_auto_population_of_timespan_config: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        end_time: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param timestamp_field: timestamp_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#timestamp_field GoogleDataLossPreventionJobTrigger#timestamp_field}
        :param enable_auto_population_of_timespan_config: When the job is started by a JobTrigger we will automatically figure out a valid startTime to avoid scanning files that have not been modified since the last time the JobTrigger executed. This will be based on the time of the execution of the last run of the JobTrigger. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#enable_auto_population_of_timespan_config GoogleDataLossPreventionJobTrigger#enable_auto_population_of_timespan_config}
        :param end_time: Exclude files or rows newer than this value. If set to zero, no upper time limit is applied. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#end_time GoogleDataLossPreventionJobTrigger#end_time}
        :param start_time: Exclude files or rows older than this value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#start_time GoogleDataLossPreventionJobTrigger#start_time}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig(
            timestamp_field=timestamp_field,
            enable_auto_population_of_timespan_config=enable_auto_population_of_timespan_config,
            end_time=end_time,
            start_time=start_time,
        )

        return typing.cast(None, jsii.invoke(self, "putTimespanConfig", [value]))

    @jsii.member(jsii_name="resetBigQueryOptions")
    def reset_big_query_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBigQueryOptions", []))

    @jsii.member(jsii_name="resetCloudStorageOptions")
    def reset_cloud_storage_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudStorageOptions", []))

    @jsii.member(jsii_name="resetDatastoreOptions")
    def reset_datastore_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatastoreOptions", []))

    @jsii.member(jsii_name="resetTimespanConfig")
    def reset_timespan_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimespanConfig", []))

    @builtins.property
    @jsii.member(jsii_name="bigQueryOptions")
    def big_query_options(
        self,
    ) -> GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsOutputReference:
        return typing.cast(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsOutputReference, jsii.get(self, "bigQueryOptions"))

    @builtins.property
    @jsii.member(jsii_name="cloudStorageOptions")
    def cloud_storage_options(
        self,
    ) -> GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsOutputReference:
        return typing.cast(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsOutputReference, jsii.get(self, "cloudStorageOptions"))

    @builtins.property
    @jsii.member(jsii_name="datastoreOptions")
    def datastore_options(
        self,
    ) -> GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsOutputReference:
        return typing.cast(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsOutputReference, jsii.get(self, "datastoreOptions"))

    @builtins.property
    @jsii.member(jsii_name="timespanConfig")
    def timespan_config(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigOutputReference", jsii.get(self, "timespanConfig"))

    @builtins.property
    @jsii.member(jsii_name="bigQueryOptionsInput")
    def big_query_options_input(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions], jsii.get(self, "bigQueryOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudStorageOptionsInput")
    def cloud_storage_options_input(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions], jsii.get(self, "cloudStorageOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="datastoreOptionsInput")
    def datastore_options_input(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions], jsii.get(self, "datastoreOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="timespanConfigInput")
    def timespan_config_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig"], jsii.get(self, "timespanConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfig]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig",
    jsii_struct_bases=[],
    name_mapping={
        "timestamp_field": "timestampField",
        "enable_auto_population_of_timespan_config": "enableAutoPopulationOfTimespanConfig",
        "end_time": "endTime",
        "start_time": "startTime",
    },
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig:
    def __init__(
        self,
        *,
        timestamp_field: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField", typing.Dict[str, typing.Any]],
        enable_auto_population_of_timespan_config: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        end_time: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param timestamp_field: timestamp_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#timestamp_field GoogleDataLossPreventionJobTrigger#timestamp_field}
        :param enable_auto_population_of_timespan_config: When the job is started by a JobTrigger we will automatically figure out a valid startTime to avoid scanning files that have not been modified since the last time the JobTrigger executed. This will be based on the time of the execution of the last run of the JobTrigger. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#enable_auto_population_of_timespan_config GoogleDataLossPreventionJobTrigger#enable_auto_population_of_timespan_config}
        :param end_time: Exclude files or rows newer than this value. If set to zero, no upper time limit is applied. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#end_time GoogleDataLossPreventionJobTrigger#end_time}
        :param start_time: Exclude files or rows older than this value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#start_time GoogleDataLossPreventionJobTrigger#start_time}
        '''
        if isinstance(timestamp_field, dict):
            timestamp_field = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField(**timestamp_field)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig.__init__)
            check_type(argname="argument timestamp_field", value=timestamp_field, expected_type=type_hints["timestamp_field"])
            check_type(argname="argument enable_auto_population_of_timespan_config", value=enable_auto_population_of_timespan_config, expected_type=type_hints["enable_auto_population_of_timespan_config"])
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "timestamp_field": timestamp_field,
        }
        if enable_auto_population_of_timespan_config is not None:
            self._values["enable_auto_population_of_timespan_config"] = enable_auto_population_of_timespan_config
        if end_time is not None:
            self._values["end_time"] = end_time
        if start_time is not None:
            self._values["start_time"] = start_time

    @builtins.property
    def timestamp_field(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField":
        '''timestamp_field block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#timestamp_field GoogleDataLossPreventionJobTrigger#timestamp_field}
        '''
        result = self._values.get("timestamp_field")
        assert result is not None, "Required property 'timestamp_field' is missing"
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField", result)

    @builtins.property
    def enable_auto_population_of_timespan_config(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When the job is started by a JobTrigger we will automatically figure out a valid startTime to avoid scanning files that have not been modified since the last time the JobTrigger executed.

        This will
        be based on the time of the execution of the last run of the JobTrigger.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#enable_auto_population_of_timespan_config GoogleDataLossPreventionJobTrigger#enable_auto_population_of_timespan_config}
        '''
        result = self._values.get("enable_auto_population_of_timespan_config")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def end_time(self) -> typing.Optional[builtins.str]:
        '''Exclude files or rows newer than this value. If set to zero, no upper time limit is applied.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#end_time GoogleDataLossPreventionJobTrigger#end_time}
        '''
        result = self._values.get("end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''Exclude files or rows older than this value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#start_time GoogleDataLossPreventionJobTrigger#start_time}
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTimestampField")
    def put_timestamp_field(self, *, name: builtins.str) -> None:
        '''
        :param name: Specification of the field containing the timestamp of scanned items. Used for data sources like Datastore and BigQuery. For BigQuery: Required to filter out rows based on the given start and end times. If not specified and the table was modified between the given start and end times, the entire table will be scanned. The valid data types of the timestamp field are: INTEGER, DATE, TIMESTAMP, or DATETIME BigQuery column. For Datastore. Valid data types of the timestamp field are: TIMESTAMP. Datastore entity will be scanned if the timestamp property does not exist or its value is empty or invalid. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#name GoogleDataLossPreventionJobTrigger#name}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField(
            name=name
        )

        return typing.cast(None, jsii.invoke(self, "putTimestampField", [value]))

    @jsii.member(jsii_name="resetEnableAutoPopulationOfTimespanConfig")
    def reset_enable_auto_population_of_timespan_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAutoPopulationOfTimespanConfig", []))

    @jsii.member(jsii_name="resetEndTime")
    def reset_end_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndTime", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

    @builtins.property
    @jsii.member(jsii_name="timestampField")
    def timestamp_field(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldOutputReference", jsii.get(self, "timestampField"))

    @builtins.property
    @jsii.member(jsii_name="enableAutoPopulationOfTimespanConfigInput")
    def enable_auto_population_of_timespan_config_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableAutoPopulationOfTimespanConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="endTimeInput")
    def end_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="timestampFieldInput")
    def timestamp_field_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField"], jsii.get(self, "timestampFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAutoPopulationOfTimespanConfig")
    def enable_auto_population_of_timespan_config(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableAutoPopulationOfTimespanConfig"))

    @enable_auto_population_of_timespan_config.setter
    def enable_auto_population_of_timespan_config(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigOutputReference, "enable_auto_population_of_timespan_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutoPopulationOfTimespanConfig", value)

    @builtins.property
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endTime"))

    @end_time.setter
    def end_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigOutputReference, "end_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endTime", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigOutputReference, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Specification of the field containing the timestamp of scanned items. Used for data sources like Datastore and BigQuery. For BigQuery: Required to filter out rows based on the given start and end times. If not specified and the table was modified between the given start and end times, the entire table will be scanned. The valid data types of the timestamp field are: INTEGER, DATE, TIMESTAMP, or DATETIME BigQuery column. For Datastore. Valid data types of the timestamp field are: TIMESTAMP. Datastore entity will be scanned if the timestamp property does not exist or its value is empty or invalid. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#name GoogleDataLossPreventionJobTrigger#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Specification of the field containing the timestamp of scanned items. Used for data sources like Datastore and BigQuery.

        For BigQuery: Required to filter out rows based on the given start and end times. If not specified and the table was
        modified between the given start and end times, the entire table will be scanned. The valid data types of the timestamp
        field are: INTEGER, DATE, TIMESTAMP, or DATETIME BigQuery column.

        For Datastore. Valid data types of the timestamp field are: TIMESTAMP. Datastore entity will be scanned if the
        timestamp property does not exist or its value is empty or invalid.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#name GoogleDataLossPreventionJobTrigger#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleDataLossPreventionJobTriggerTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#create GoogleDataLossPreventionJobTrigger#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#delete GoogleDataLossPreventionJobTrigger#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#update GoogleDataLossPreventionJobTrigger#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#create GoogleDataLossPreventionJobTrigger#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#delete GoogleDataLossPreventionJobTrigger#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#update GoogleDataLossPreventionJobTrigger#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

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
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerTriggers",
    jsii_struct_bases=[],
    name_mapping={"schedule": "schedule"},
)
class GoogleDataLossPreventionJobTriggerTriggers:
    def __init__(
        self,
        *,
        schedule: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerTriggersSchedule", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#schedule GoogleDataLossPreventionJobTrigger#schedule}
        '''
        if isinstance(schedule, dict):
            schedule = GoogleDataLossPreventionJobTriggerTriggersSchedule(**schedule)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerTriggers.__init__)
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
        self._values: typing.Dict[str, typing.Any] = {}
        if schedule is not None:
            self._values["schedule"] = schedule

    @builtins.property
    def schedule(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerTriggersSchedule"]:
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#schedule GoogleDataLossPreventionJobTrigger#schedule}
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerTriggersSchedule"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerTriggers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerTriggersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerTriggersList",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerTriggersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDataLossPreventionJobTriggerTriggersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerTriggersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDataLossPreventionJobTriggerTriggersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerTriggersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerTriggersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerTriggersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataLossPreventionJobTriggerTriggers]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataLossPreventionJobTriggerTriggers]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDataLossPreventionJobTriggerTriggers]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerTriggersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataLossPreventionJobTriggerTriggersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerTriggersOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerTriggersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putSchedule")
    def put_schedule(
        self,
        *,
        recurrence_period_duration: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param recurrence_period_duration: With this option a job is started a regular periodic basis. For example: every day (86400 seconds). A scheduled start time will be skipped if the previous execution has not ended when its scheduled time occurs. This value must be set to a time duration greater than or equal to 1 day and can be no longer than 60 days. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#recurrence_period_duration GoogleDataLossPreventionJobTrigger#recurrence_period_duration}
        '''
        value = GoogleDataLossPreventionJobTriggerTriggersSchedule(
            recurrence_period_duration=recurrence_period_duration
        )

        return typing.cast(None, jsii.invoke(self, "putSchedule", [value]))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerTriggersScheduleOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerTriggersScheduleOutputReference", jsii.get(self, "schedule"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerTriggersSchedule"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerTriggersSchedule"], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerTriggers, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerTriggers, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerTriggers, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerTriggersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerTriggersSchedule",
    jsii_struct_bases=[],
    name_mapping={"recurrence_period_duration": "recurrencePeriodDuration"},
)
class GoogleDataLossPreventionJobTriggerTriggersSchedule:
    def __init__(
        self,
        *,
        recurrence_period_duration: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param recurrence_period_duration: With this option a job is started a regular periodic basis. For example: every day (86400 seconds). A scheduled start time will be skipped if the previous execution has not ended when its scheduled time occurs. This value must be set to a time duration greater than or equal to 1 day and can be no longer than 60 days. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#recurrence_period_duration GoogleDataLossPreventionJobTrigger#recurrence_period_duration}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerTriggersSchedule.__init__)
            check_type(argname="argument recurrence_period_duration", value=recurrence_period_duration, expected_type=type_hints["recurrence_period_duration"])
        self._values: typing.Dict[str, typing.Any] = {}
        if recurrence_period_duration is not None:
            self._values["recurrence_period_duration"] = recurrence_period_duration

    @builtins.property
    def recurrence_period_duration(self) -> typing.Optional[builtins.str]:
        '''With this option a job is started a regular periodic basis. For example: every day (86400 seconds).

        A scheduled start time will be skipped if the previous execution has not ended when its scheduled time occurs.

        This value must be set to a time duration greater than or equal to 1 day and can be no longer than 60 days.

        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#recurrence_period_duration GoogleDataLossPreventionJobTrigger#recurrence_period_duration}
        '''
        result = self._values.get("recurrence_period_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerTriggersSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerTriggersScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerTriggersScheduleOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataLossPreventionJobTriggerTriggersScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRecurrencePeriodDuration")
    def reset_recurrence_period_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecurrencePeriodDuration", []))

    @builtins.property
    @jsii.member(jsii_name="recurrencePeriodDurationInput")
    def recurrence_period_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recurrencePeriodDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="recurrencePeriodDuration")
    def recurrence_period_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recurrencePeriodDuration"))

    @recurrence_period_duration.setter
    def recurrence_period_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerTriggersScheduleOutputReference, "recurrence_period_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recurrencePeriodDuration", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerTriggersSchedule]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerTriggersSchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerTriggersSchedule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataLossPreventionJobTriggerTriggersScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleDataLossPreventionJobTrigger",
    "GoogleDataLossPreventionJobTriggerConfig",
    "GoogleDataLossPreventionJobTriggerInspectJob",
    "GoogleDataLossPreventionJobTriggerInspectJobActions",
    "GoogleDataLossPreventionJobTriggerInspectJobActionsList",
    "GoogleDataLossPreventionJobTriggerInspectJobActionsOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings",
    "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig",
    "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable",
    "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTableOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfig",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldOutputReference",
    "GoogleDataLossPreventionJobTriggerTimeouts",
    "GoogleDataLossPreventionJobTriggerTimeoutsOutputReference",
    "GoogleDataLossPreventionJobTriggerTriggers",
    "GoogleDataLossPreventionJobTriggerTriggersList",
    "GoogleDataLossPreventionJobTriggerTriggersOutputReference",
    "GoogleDataLossPreventionJobTriggerTriggersSchedule",
    "GoogleDataLossPreventionJobTriggerTriggersScheduleOutputReference",
]

publication.publish()
