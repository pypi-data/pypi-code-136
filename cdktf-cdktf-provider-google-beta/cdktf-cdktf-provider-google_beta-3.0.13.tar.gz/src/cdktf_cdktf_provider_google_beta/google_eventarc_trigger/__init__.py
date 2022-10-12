'''
# `google_eventarc_trigger`

Refer to the Terraform Registory for docs: [`google_eventarc_trigger`](https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger).
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


class GoogleEventarcTrigger(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleEventarcTrigger.GoogleEventarcTrigger",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger google_eventarc_trigger}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        destination: typing.Union["GoogleEventarcTriggerDestination", typing.Dict[str, typing.Any]],
        location: builtins.str,
        matching_criteria: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleEventarcTriggerMatchingCriteria", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        service_account: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleEventarcTriggerTimeouts", typing.Dict[str, typing.Any]]] = None,
        transport: typing.Optional[typing.Union["GoogleEventarcTriggerTransport", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger google_eventarc_trigger} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param destination: destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#destination GoogleEventarcTrigger#destination}
        :param location: The location for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#location GoogleEventarcTrigger#location}
        :param matching_criteria: matching_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#matching_criteria GoogleEventarcTrigger#matching_criteria}
        :param name: Required. The resource name of the trigger. Must be unique within the location on the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#name GoogleEventarcTrigger#name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#id GoogleEventarcTrigger#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Optional. User labels attached to the triggers that can be used to group resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#labels GoogleEventarcTrigger#labels}
        :param project: The project for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#project GoogleEventarcTrigger#project}
        :param service_account: Optional. The IAM service account email associated with the trigger. The service account represents the identity of the trigger. The principal who calls this API must have ``iam.serviceAccounts.actAs`` permission in the service account. See https://cloud.google.com/iam/docs/understanding-service-accounts#sa_common for more information. For Cloud Run destinations, this service account is used to generate identity tokens when invoking the service. See https://cloud.google.com/run/docs/triggering/pubsub-push#create-service-account for information on how to invoke authenticated Cloud Run services. In order to create Audit Log triggers, the service account should also have ``roles/eventarc.eventReceiver`` IAM role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#service_account GoogleEventarcTrigger#service_account}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#timeouts GoogleEventarcTrigger#timeouts}
        :param transport: transport block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#transport GoogleEventarcTrigger#transport}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleEventarcTrigger.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleEventarcTriggerConfig(
            destination=destination,
            location=location,
            matching_criteria=matching_criteria,
            name=name,
            id=id,
            labels=labels,
            project=project,
            service_account=service_account,
            timeouts=timeouts,
            transport=transport,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDestination")
    def put_destination(
        self,
        *,
        cloud_function: typing.Optional[builtins.str] = None,
        cloud_run_service: typing.Optional[typing.Union["GoogleEventarcTriggerDestinationCloudRunService", typing.Dict[str, typing.Any]]] = None,
        gke: typing.Optional[typing.Union["GoogleEventarcTriggerDestinationGke", typing.Dict[str, typing.Any]]] = None,
        workflow: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cloud_function: [WARNING] Configuring a Cloud Function in Trigger is not supported as of today. The Cloud Function resource name. Format: projects/{project}/locations/{location}/functions/{function} Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#cloud_function GoogleEventarcTrigger#cloud_function}
        :param cloud_run_service: cloud_run_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#cloud_run_service GoogleEventarcTrigger#cloud_run_service}
        :param gke: gke block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#gke GoogleEventarcTrigger#gke}
        :param workflow: The resource name of the Workflow whose Executions are triggered by the events. The Workflow resource should be deployed in the same project as the trigger. Format: ``projects/{project}/locations/{location}/workflows/{workflow}`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#workflow GoogleEventarcTrigger#workflow}
        '''
        value = GoogleEventarcTriggerDestination(
            cloud_function=cloud_function,
            cloud_run_service=cloud_run_service,
            gke=gke,
            workflow=workflow,
        )

        return typing.cast(None, jsii.invoke(self, "putDestination", [value]))

    @jsii.member(jsii_name="putMatchingCriteria")
    def put_matching_criteria(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleEventarcTriggerMatchingCriteria", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleEventarcTrigger.put_matching_criteria)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchingCriteria", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#create GoogleEventarcTrigger#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#delete GoogleEventarcTrigger#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#update GoogleEventarcTrigger#update}.
        '''
        value = GoogleEventarcTriggerTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTransport")
    def put_transport(
        self,
        *,
        pubsub: typing.Optional[typing.Union["GoogleEventarcTriggerTransportPubsub", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param pubsub: pubsub block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#pubsub GoogleEventarcTrigger#pubsub}
        '''
        value = GoogleEventarcTriggerTransport(pubsub=pubsub)

        return typing.cast(None, jsii.invoke(self, "putTransport", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetServiceAccount")
    def reset_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccount", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTransport")
    def reset_transport(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransport", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> "GoogleEventarcTriggerDestinationOutputReference":
        return typing.cast("GoogleEventarcTriggerDestinationOutputReference", jsii.get(self, "destination"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="matchingCriteria")
    def matching_criteria(self) -> "GoogleEventarcTriggerMatchingCriteriaList":
        return typing.cast("GoogleEventarcTriggerMatchingCriteriaList", jsii.get(self, "matchingCriteria"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleEventarcTriggerTimeoutsOutputReference":
        return typing.cast("GoogleEventarcTriggerTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="transport")
    def transport(self) -> "GoogleEventarcTriggerTransportOutputReference":
        return typing.cast("GoogleEventarcTriggerTransportOutputReference", jsii.get(self, "transport"))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional["GoogleEventarcTriggerDestination"]:
        return typing.cast(typing.Optional["GoogleEventarcTriggerDestination"], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="matchingCriteriaInput")
    def matching_criteria_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleEventarcTriggerMatchingCriteria"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleEventarcTriggerMatchingCriteria"]]], jsii.get(self, "matchingCriteriaInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountInput")
    def service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleEventarcTriggerTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleEventarcTriggerTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="transportInput")
    def transport_input(self) -> typing.Optional["GoogleEventarcTriggerTransport"]:
        return typing.cast(typing.Optional["GoogleEventarcTriggerTransport"], jsii.get(self, "transportInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTrigger, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTrigger, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTrigger, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTrigger, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTrigger, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccount"))

    @service_account.setter
    def service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTrigger, "service_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccount", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleEventarcTrigger.GoogleEventarcTriggerConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "destination": "destination",
        "location": "location",
        "matching_criteria": "matchingCriteria",
        "name": "name",
        "id": "id",
        "labels": "labels",
        "project": "project",
        "service_account": "serviceAccount",
        "timeouts": "timeouts",
        "transport": "transport",
    },
)
class GoogleEventarcTriggerConfig(cdktf.TerraformMetaArguments):
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
        destination: typing.Union["GoogleEventarcTriggerDestination", typing.Dict[str, typing.Any]],
        location: builtins.str,
        matching_criteria: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleEventarcTriggerMatchingCriteria", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        service_account: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleEventarcTriggerTimeouts", typing.Dict[str, typing.Any]]] = None,
        transport: typing.Optional[typing.Union["GoogleEventarcTriggerTransport", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param destination: destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#destination GoogleEventarcTrigger#destination}
        :param location: The location for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#location GoogleEventarcTrigger#location}
        :param matching_criteria: matching_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#matching_criteria GoogleEventarcTrigger#matching_criteria}
        :param name: Required. The resource name of the trigger. Must be unique within the location on the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#name GoogleEventarcTrigger#name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#id GoogleEventarcTrigger#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Optional. User labels attached to the triggers that can be used to group resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#labels GoogleEventarcTrigger#labels}
        :param project: The project for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#project GoogleEventarcTrigger#project}
        :param service_account: Optional. The IAM service account email associated with the trigger. The service account represents the identity of the trigger. The principal who calls this API must have ``iam.serviceAccounts.actAs`` permission in the service account. See https://cloud.google.com/iam/docs/understanding-service-accounts#sa_common for more information. For Cloud Run destinations, this service account is used to generate identity tokens when invoking the service. See https://cloud.google.com/run/docs/triggering/pubsub-push#create-service-account for information on how to invoke authenticated Cloud Run services. In order to create Audit Log triggers, the service account should also have ``roles/eventarc.eventReceiver`` IAM role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#service_account GoogleEventarcTrigger#service_account}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#timeouts GoogleEventarcTrigger#timeouts}
        :param transport: transport block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#transport GoogleEventarcTrigger#transport}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(destination, dict):
            destination = GoogleEventarcTriggerDestination(**destination)
        if isinstance(timeouts, dict):
            timeouts = GoogleEventarcTriggerTimeouts(**timeouts)
        if isinstance(transport, dict):
            transport = GoogleEventarcTriggerTransport(**transport)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleEventarcTriggerConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument matching_criteria", value=matching_criteria, expected_type=type_hints["matching_criteria"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument transport", value=transport, expected_type=type_hints["transport"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
            "location": location,
            "matching_criteria": matching_criteria,
            "name": name,
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
        if labels is not None:
            self._values["labels"] = labels
        if project is not None:
            self._values["project"] = project
        if service_account is not None:
            self._values["service_account"] = service_account
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if transport is not None:
            self._values["transport"] = transport

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
    def destination(self) -> "GoogleEventarcTriggerDestination":
        '''destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#destination GoogleEventarcTrigger#destination}
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast("GoogleEventarcTriggerDestination", result)

    @builtins.property
    def location(self) -> builtins.str:
        '''The location for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#location GoogleEventarcTrigger#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def matching_criteria(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleEventarcTriggerMatchingCriteria"]]:
        '''matching_criteria block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#matching_criteria GoogleEventarcTrigger#matching_criteria}
        '''
        result = self._values.get("matching_criteria")
        assert result is not None, "Required property 'matching_criteria' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleEventarcTriggerMatchingCriteria"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Required. The resource name of the trigger. Must be unique within the location on the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#name GoogleEventarcTrigger#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#id GoogleEventarcTrigger#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional. User labels attached to the triggers that can be used to group resources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#labels GoogleEventarcTrigger#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The project for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#project GoogleEventarcTrigger#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The IAM service account email associated with the trigger. The service account represents the identity of the trigger. The principal who calls this API must have ``iam.serviceAccounts.actAs`` permission in the service account. See https://cloud.google.com/iam/docs/understanding-service-accounts#sa_common for more information. For Cloud Run destinations, this service account is used to generate identity tokens when invoking the service. See https://cloud.google.com/run/docs/triggering/pubsub-push#create-service-account for information on how to invoke authenticated Cloud Run services. In order to create Audit Log triggers, the service account should also have ``roles/eventarc.eventReceiver`` IAM role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#service_account GoogleEventarcTrigger#service_account}
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleEventarcTriggerTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#timeouts GoogleEventarcTrigger#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleEventarcTriggerTimeouts"], result)

    @builtins.property
    def transport(self) -> typing.Optional["GoogleEventarcTriggerTransport"]:
        '''transport block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#transport GoogleEventarcTrigger#transport}
        '''
        result = self._values.get("transport")
        return typing.cast(typing.Optional["GoogleEventarcTriggerTransport"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleEventarcTriggerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleEventarcTrigger.GoogleEventarcTriggerDestination",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_function": "cloudFunction",
        "cloud_run_service": "cloudRunService",
        "gke": "gke",
        "workflow": "workflow",
    },
)
class GoogleEventarcTriggerDestination:
    def __init__(
        self,
        *,
        cloud_function: typing.Optional[builtins.str] = None,
        cloud_run_service: typing.Optional[typing.Union["GoogleEventarcTriggerDestinationCloudRunService", typing.Dict[str, typing.Any]]] = None,
        gke: typing.Optional[typing.Union["GoogleEventarcTriggerDestinationGke", typing.Dict[str, typing.Any]]] = None,
        workflow: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cloud_function: [WARNING] Configuring a Cloud Function in Trigger is not supported as of today. The Cloud Function resource name. Format: projects/{project}/locations/{location}/functions/{function} Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#cloud_function GoogleEventarcTrigger#cloud_function}
        :param cloud_run_service: cloud_run_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#cloud_run_service GoogleEventarcTrigger#cloud_run_service}
        :param gke: gke block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#gke GoogleEventarcTrigger#gke}
        :param workflow: The resource name of the Workflow whose Executions are triggered by the events. The Workflow resource should be deployed in the same project as the trigger. Format: ``projects/{project}/locations/{location}/workflows/{workflow}`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#workflow GoogleEventarcTrigger#workflow}
        '''
        if isinstance(cloud_run_service, dict):
            cloud_run_service = GoogleEventarcTriggerDestinationCloudRunService(**cloud_run_service)
        if isinstance(gke, dict):
            gke = GoogleEventarcTriggerDestinationGke(**gke)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleEventarcTriggerDestination.__init__)
            check_type(argname="argument cloud_function", value=cloud_function, expected_type=type_hints["cloud_function"])
            check_type(argname="argument cloud_run_service", value=cloud_run_service, expected_type=type_hints["cloud_run_service"])
            check_type(argname="argument gke", value=gke, expected_type=type_hints["gke"])
            check_type(argname="argument workflow", value=workflow, expected_type=type_hints["workflow"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cloud_function is not None:
            self._values["cloud_function"] = cloud_function
        if cloud_run_service is not None:
            self._values["cloud_run_service"] = cloud_run_service
        if gke is not None:
            self._values["gke"] = gke
        if workflow is not None:
            self._values["workflow"] = workflow

    @builtins.property
    def cloud_function(self) -> typing.Optional[builtins.str]:
        '''[WARNING] Configuring a Cloud Function in Trigger is not supported as of today.

        The Cloud Function resource name. Format: projects/{project}/locations/{location}/functions/{function}

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#cloud_function GoogleEventarcTrigger#cloud_function}
        '''
        result = self._values.get("cloud_function")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_run_service(
        self,
    ) -> typing.Optional["GoogleEventarcTriggerDestinationCloudRunService"]:
        '''cloud_run_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#cloud_run_service GoogleEventarcTrigger#cloud_run_service}
        '''
        result = self._values.get("cloud_run_service")
        return typing.cast(typing.Optional["GoogleEventarcTriggerDestinationCloudRunService"], result)

    @builtins.property
    def gke(self) -> typing.Optional["GoogleEventarcTriggerDestinationGke"]:
        '''gke block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#gke GoogleEventarcTrigger#gke}
        '''
        result = self._values.get("gke")
        return typing.cast(typing.Optional["GoogleEventarcTriggerDestinationGke"], result)

    @builtins.property
    def workflow(self) -> typing.Optional[builtins.str]:
        '''The resource name of the Workflow whose Executions are triggered by the events.

        The Workflow resource should be deployed in the same project as the trigger. Format: ``projects/{project}/locations/{location}/workflows/{workflow}``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#workflow GoogleEventarcTrigger#workflow}
        '''
        result = self._values.get("workflow")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleEventarcTriggerDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleEventarcTrigger.GoogleEventarcTriggerDestinationCloudRunService",
    jsii_struct_bases=[],
    name_mapping={"service": "service", "path": "path", "region": "region"},
)
class GoogleEventarcTriggerDestinationCloudRunService:
    def __init__(
        self,
        *,
        service: builtins.str,
        path: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service: Required. The name of the Cloud Run service being addressed. See https://cloud.google.com/run/docs/reference/rest/v1/namespaces.services. Only services located in the same project of the trigger object can be addressed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#service GoogleEventarcTrigger#service}
        :param path: Optional. The relative path on the Cloud Run service the events should be sent to. The value must conform to the definition of URI path segment (section 3.3 of RFC2396). Examples: "/route", "route", "route/subroute". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#path GoogleEventarcTrigger#path}
        :param region: Required. The region the Cloud Run service is deployed in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#region GoogleEventarcTrigger#region}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleEventarcTriggerDestinationCloudRunService.__init__)
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[str, typing.Any] = {
            "service": service,
        }
        if path is not None:
            self._values["path"] = path
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def service(self) -> builtins.str:
        '''Required.

        The name of the Cloud Run service being addressed. See https://cloud.google.com/run/docs/reference/rest/v1/namespaces.services. Only services located in the same project of the trigger object can be addressed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#service GoogleEventarcTrigger#service}
        '''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The relative path on the Cloud Run service the events should be sent to. The value must conform to the definition of URI path segment (section 3.3 of RFC2396). Examples: "/route", "route", "route/subroute".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#path GoogleEventarcTrigger#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Required. The region the Cloud Run service is deployed in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#region GoogleEventarcTrigger#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleEventarcTriggerDestinationCloudRunService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleEventarcTriggerDestinationCloudRunServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleEventarcTrigger.GoogleEventarcTriggerDestinationCloudRunServiceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleEventarcTriggerDestinationCloudRunServiceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerDestinationCloudRunServiceOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerDestinationCloudRunServiceOutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerDestinationCloudRunServiceOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleEventarcTriggerDestinationCloudRunService]:
        return typing.cast(typing.Optional[GoogleEventarcTriggerDestinationCloudRunService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleEventarcTriggerDestinationCloudRunService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerDestinationCloudRunServiceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleEventarcTrigger.GoogleEventarcTriggerDestinationGke",
    jsii_struct_bases=[],
    name_mapping={
        "cluster": "cluster",
        "location": "location",
        "namespace": "namespace",
        "service": "service",
        "path": "path",
    },
)
class GoogleEventarcTriggerDestinationGke:
    def __init__(
        self,
        *,
        cluster: builtins.str,
        location: builtins.str,
        namespace: builtins.str,
        service: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cluster: Required. The name of the cluster the GKE service is running in. The cluster must be running in the same project as the trigger being created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#cluster GoogleEventarcTrigger#cluster}
        :param location: Required. The name of the Google Compute Engine in which the cluster resides, which can either be compute zone (for example, us-central1-a) for the zonal clusters or region (for example, us-central1) for regional clusters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#location GoogleEventarcTrigger#location}
        :param namespace: Required. The namespace the GKE service is running in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#namespace GoogleEventarcTrigger#namespace}
        :param service: Required. Name of the GKE service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#service GoogleEventarcTrigger#service}
        :param path: Optional. The relative path on the GKE service the events should be sent to. The value must conform to the definition of a URI path segment (section 3.3 of RFC2396). Examples: "/route", "route", "route/subroute". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#path GoogleEventarcTrigger#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleEventarcTriggerDestinationGke.__init__)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster": cluster,
            "location": location,
            "namespace": namespace,
            "service": service,
        }
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def cluster(self) -> builtins.str:
        '''Required.

        The name of the cluster the GKE service is running in. The cluster must be running in the same project as the trigger being created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#cluster GoogleEventarcTrigger#cluster}
        '''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Required.

        The name of the Google Compute Engine in which the cluster resides, which can either be compute zone (for example, us-central1-a) for the zonal clusters or region (for example, us-central1) for regional clusters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#location GoogleEventarcTrigger#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Required. The namespace the GKE service is running in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#namespace GoogleEventarcTrigger#namespace}
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''Required. Name of the GKE service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#service GoogleEventarcTrigger#service}
        '''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The relative path on the GKE service the events should be sent to. The value must conform to the definition of a URI path segment (section 3.3 of RFC2396). Examples: "/route", "route", "route/subroute".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#path GoogleEventarcTrigger#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleEventarcTriggerDestinationGke(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleEventarcTriggerDestinationGkeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleEventarcTrigger.GoogleEventarcTriggerDestinationGkeOutputReference",
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
            type_hints = typing.get_type_hints(GoogleEventarcTriggerDestinationGkeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="clusterInput")
    def cluster_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cluster"))

    @cluster.setter
    def cluster(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerDestinationGkeOutputReference, "cluster").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cluster", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerDestinationGkeOutputReference, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerDestinationGkeOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerDestinationGkeOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerDestinationGkeOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleEventarcTriggerDestinationGke]:
        return typing.cast(typing.Optional[GoogleEventarcTriggerDestinationGke], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleEventarcTriggerDestinationGke],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerDestinationGkeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleEventarcTriggerDestinationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleEventarcTrigger.GoogleEventarcTriggerDestinationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleEventarcTriggerDestinationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudRunService")
    def put_cloud_run_service(
        self,
        *,
        service: builtins.str,
        path: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service: Required. The name of the Cloud Run service being addressed. See https://cloud.google.com/run/docs/reference/rest/v1/namespaces.services. Only services located in the same project of the trigger object can be addressed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#service GoogleEventarcTrigger#service}
        :param path: Optional. The relative path on the Cloud Run service the events should be sent to. The value must conform to the definition of URI path segment (section 3.3 of RFC2396). Examples: "/route", "route", "route/subroute". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#path GoogleEventarcTrigger#path}
        :param region: Required. The region the Cloud Run service is deployed in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#region GoogleEventarcTrigger#region}
        '''
        value = GoogleEventarcTriggerDestinationCloudRunService(
            service=service, path=path, region=region
        )

        return typing.cast(None, jsii.invoke(self, "putCloudRunService", [value]))

    @jsii.member(jsii_name="putGke")
    def put_gke(
        self,
        *,
        cluster: builtins.str,
        location: builtins.str,
        namespace: builtins.str,
        service: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cluster: Required. The name of the cluster the GKE service is running in. The cluster must be running in the same project as the trigger being created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#cluster GoogleEventarcTrigger#cluster}
        :param location: Required. The name of the Google Compute Engine in which the cluster resides, which can either be compute zone (for example, us-central1-a) for the zonal clusters or region (for example, us-central1) for regional clusters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#location GoogleEventarcTrigger#location}
        :param namespace: Required. The namespace the GKE service is running in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#namespace GoogleEventarcTrigger#namespace}
        :param service: Required. Name of the GKE service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#service GoogleEventarcTrigger#service}
        :param path: Optional. The relative path on the GKE service the events should be sent to. The value must conform to the definition of a URI path segment (section 3.3 of RFC2396). Examples: "/route", "route", "route/subroute". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#path GoogleEventarcTrigger#path}
        '''
        value = GoogleEventarcTriggerDestinationGke(
            cluster=cluster,
            location=location,
            namespace=namespace,
            service=service,
            path=path,
        )

        return typing.cast(None, jsii.invoke(self, "putGke", [value]))

    @jsii.member(jsii_name="resetCloudFunction")
    def reset_cloud_function(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudFunction", []))

    @jsii.member(jsii_name="resetCloudRunService")
    def reset_cloud_run_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudRunService", []))

    @jsii.member(jsii_name="resetGke")
    def reset_gke(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGke", []))

    @jsii.member(jsii_name="resetWorkflow")
    def reset_workflow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkflow", []))

    @builtins.property
    @jsii.member(jsii_name="cloudRunService")
    def cloud_run_service(
        self,
    ) -> GoogleEventarcTriggerDestinationCloudRunServiceOutputReference:
        return typing.cast(GoogleEventarcTriggerDestinationCloudRunServiceOutputReference, jsii.get(self, "cloudRunService"))

    @builtins.property
    @jsii.member(jsii_name="gke")
    def gke(self) -> GoogleEventarcTriggerDestinationGkeOutputReference:
        return typing.cast(GoogleEventarcTriggerDestinationGkeOutputReference, jsii.get(self, "gke"))

    @builtins.property
    @jsii.member(jsii_name="cloudFunctionInput")
    def cloud_function_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudFunctionInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudRunServiceInput")
    def cloud_run_service_input(
        self,
    ) -> typing.Optional[GoogleEventarcTriggerDestinationCloudRunService]:
        return typing.cast(typing.Optional[GoogleEventarcTriggerDestinationCloudRunService], jsii.get(self, "cloudRunServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="gkeInput")
    def gke_input(self) -> typing.Optional[GoogleEventarcTriggerDestinationGke]:
        return typing.cast(typing.Optional[GoogleEventarcTriggerDestinationGke], jsii.get(self, "gkeInput"))

    @builtins.property
    @jsii.member(jsii_name="workflowInput")
    def workflow_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workflowInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudFunction")
    def cloud_function(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudFunction"))

    @cloud_function.setter
    def cloud_function(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerDestinationOutputReference, "cloud_function").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudFunction", value)

    @builtins.property
    @jsii.member(jsii_name="workflow")
    def workflow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workflow"))

    @workflow.setter
    def workflow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerDestinationOutputReference, "workflow").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workflow", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleEventarcTriggerDestination]:
        return typing.cast(typing.Optional[GoogleEventarcTriggerDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleEventarcTriggerDestination],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerDestinationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleEventarcTrigger.GoogleEventarcTriggerMatchingCriteria",
    jsii_struct_bases=[],
    name_mapping={"attribute": "attribute", "value": "value", "operator": "operator"},
)
class GoogleEventarcTriggerMatchingCriteria:
    def __init__(
        self,
        *,
        attribute: builtins.str,
        value: builtins.str,
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param attribute: Required. The name of a CloudEvents attribute. Currently, only a subset of attributes are supported for filtering. All triggers MUST provide a filter for the 'type' attribute. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#attribute GoogleEventarcTrigger#attribute}
        :param value: Required. The value for the attribute. See https://cloud.google.com/eventarc/docs/creating-triggers#trigger-gcloud for available values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#value GoogleEventarcTrigger#value}
        :param operator: Optional. The operator used for matching the events with the value of the filter. If not specified, only events that have an exact key-value pair specified in the filter are matched. The only allowed value is ``match-path-pattern``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#operator GoogleEventarcTrigger#operator}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleEventarcTriggerMatchingCriteria.__init__)
            check_type(argname="argument attribute", value=attribute, expected_type=type_hints["attribute"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
        self._values: typing.Dict[str, typing.Any] = {
            "attribute": attribute,
            "value": value,
        }
        if operator is not None:
            self._values["operator"] = operator

    @builtins.property
    def attribute(self) -> builtins.str:
        '''Required.

        The name of a CloudEvents attribute. Currently, only a subset of attributes are supported for filtering. All triggers MUST provide a filter for the 'type' attribute.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#attribute GoogleEventarcTrigger#attribute}
        '''
        result = self._values.get("attribute")
        assert result is not None, "Required property 'attribute' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Required. The value for the attribute. See https://cloud.google.com/eventarc/docs/creating-triggers#trigger-gcloud for available values.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#value GoogleEventarcTrigger#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The operator used for matching the events with the value of the filter. If not specified, only events that have an exact key-value pair specified in the filter are matched. The only allowed value is ``match-path-pattern``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#operator GoogleEventarcTrigger#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleEventarcTriggerMatchingCriteria(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleEventarcTriggerMatchingCriteriaList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleEventarcTrigger.GoogleEventarcTriggerMatchingCriteriaList",
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
            type_hints = typing.get_type_hints(GoogleEventarcTriggerMatchingCriteriaList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleEventarcTriggerMatchingCriteriaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleEventarcTriggerMatchingCriteriaList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleEventarcTriggerMatchingCriteriaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerMatchingCriteriaList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerMatchingCriteriaList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerMatchingCriteriaList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleEventarcTriggerMatchingCriteria]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleEventarcTriggerMatchingCriteria]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleEventarcTriggerMatchingCriteria]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerMatchingCriteriaList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleEventarcTriggerMatchingCriteriaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleEventarcTrigger.GoogleEventarcTriggerMatchingCriteriaOutputReference",
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
            type_hints = typing.get_type_hints(GoogleEventarcTriggerMatchingCriteriaOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @builtins.property
    @jsii.member(jsii_name="attributeInput")
    def attribute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="attribute")
    def attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attribute"))

    @attribute.setter
    def attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerMatchingCriteriaOutputReference, "attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attribute", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerMatchingCriteriaOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerMatchingCriteriaOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleEventarcTriggerMatchingCriteria, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleEventarcTriggerMatchingCriteria, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleEventarcTriggerMatchingCriteria, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerMatchingCriteriaOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleEventarcTrigger.GoogleEventarcTriggerTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleEventarcTriggerTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#create GoogleEventarcTrigger#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#delete GoogleEventarcTrigger#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#update GoogleEventarcTrigger#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleEventarcTriggerTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#create GoogleEventarcTrigger#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#delete GoogleEventarcTrigger#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#update GoogleEventarcTrigger#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleEventarcTriggerTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleEventarcTriggerTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleEventarcTrigger.GoogleEventarcTriggerTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleEventarcTriggerTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleEventarcTriggerTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleEventarcTriggerTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleEventarcTriggerTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleEventarcTrigger.GoogleEventarcTriggerTransport",
    jsii_struct_bases=[],
    name_mapping={"pubsub": "pubsub"},
)
class GoogleEventarcTriggerTransport:
    def __init__(
        self,
        *,
        pubsub: typing.Optional[typing.Union["GoogleEventarcTriggerTransportPubsub", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param pubsub: pubsub block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#pubsub GoogleEventarcTrigger#pubsub}
        '''
        if isinstance(pubsub, dict):
            pubsub = GoogleEventarcTriggerTransportPubsub(**pubsub)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleEventarcTriggerTransport.__init__)
            check_type(argname="argument pubsub", value=pubsub, expected_type=type_hints["pubsub"])
        self._values: typing.Dict[str, typing.Any] = {}
        if pubsub is not None:
            self._values["pubsub"] = pubsub

    @builtins.property
    def pubsub(self) -> typing.Optional["GoogleEventarcTriggerTransportPubsub"]:
        '''pubsub block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#pubsub GoogleEventarcTrigger#pubsub}
        '''
        result = self._values.get("pubsub")
        return typing.cast(typing.Optional["GoogleEventarcTriggerTransportPubsub"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleEventarcTriggerTransport(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleEventarcTriggerTransportOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleEventarcTrigger.GoogleEventarcTriggerTransportOutputReference",
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
            type_hints = typing.get_type_hints(GoogleEventarcTriggerTransportOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPubsub")
    def put_pubsub(self, *, topic: typing.Optional[builtins.str] = None) -> None:
        '''
        :param topic: Optional. The name of the Pub/Sub topic created and managed by Eventarc system as a transport for the event delivery. Format: ``projects/{PROJECT_ID}/topics/{TOPIC_NAME}. You may set an existing topic for triggers of the type google.cloud.pubsub.topic.v1.messagePublished`` only. The topic you provide here will not be deleted by Eventarc at trigger deletion. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#topic GoogleEventarcTrigger#topic}
        '''
        value = GoogleEventarcTriggerTransportPubsub(topic=topic)

        return typing.cast(None, jsii.invoke(self, "putPubsub", [value]))

    @jsii.member(jsii_name="resetPubsub")
    def reset_pubsub(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPubsub", []))

    @builtins.property
    @jsii.member(jsii_name="pubsub")
    def pubsub(self) -> "GoogleEventarcTriggerTransportPubsubOutputReference":
        return typing.cast("GoogleEventarcTriggerTransportPubsubOutputReference", jsii.get(self, "pubsub"))

    @builtins.property
    @jsii.member(jsii_name="pubsubInput")
    def pubsub_input(self) -> typing.Optional["GoogleEventarcTriggerTransportPubsub"]:
        return typing.cast(typing.Optional["GoogleEventarcTriggerTransportPubsub"], jsii.get(self, "pubsubInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleEventarcTriggerTransport]:
        return typing.cast(typing.Optional[GoogleEventarcTriggerTransport], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleEventarcTriggerTransport],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerTransportOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleEventarcTrigger.GoogleEventarcTriggerTransportPubsub",
    jsii_struct_bases=[],
    name_mapping={"topic": "topic"},
)
class GoogleEventarcTriggerTransportPubsub:
    def __init__(self, *, topic: typing.Optional[builtins.str] = None) -> None:
        '''
        :param topic: Optional. The name of the Pub/Sub topic created and managed by Eventarc system as a transport for the event delivery. Format: ``projects/{PROJECT_ID}/topics/{TOPIC_NAME}. You may set an existing topic for triggers of the type google.cloud.pubsub.topic.v1.messagePublished`` only. The topic you provide here will not be deleted by Eventarc at trigger deletion. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#topic GoogleEventarcTrigger#topic}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleEventarcTriggerTransportPubsub.__init__)
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        self._values: typing.Dict[str, typing.Any] = {}
        if topic is not None:
            self._values["topic"] = topic

    @builtins.property
    def topic(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The name of the Pub/Sub topic created and managed by Eventarc system as a transport for the event delivery. Format: ``projects/{PROJECT_ID}/topics/{TOPIC_NAME}. You may set an existing topic for triggers of the type google.cloud.pubsub.topic.v1.messagePublished`` only. The topic you provide here will not be deleted by Eventarc at trigger deletion.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_eventarc_trigger#topic GoogleEventarcTrigger#topic}
        '''
        result = self._values.get("topic")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleEventarcTriggerTransportPubsub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleEventarcTriggerTransportPubsubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleEventarcTrigger.GoogleEventarcTriggerTransportPubsubOutputReference",
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
            type_hints = typing.get_type_hints(GoogleEventarcTriggerTransportPubsubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTopic")
    def reset_topic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTopic", []))

    @builtins.property
    @jsii.member(jsii_name="subscription")
    def subscription(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subscription"))

    @builtins.property
    @jsii.member(jsii_name="topicInput")
    def topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicInput"))

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topic"))

    @topic.setter
    def topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerTransportPubsubOutputReference, "topic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topic", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleEventarcTriggerTransportPubsub]:
        return typing.cast(typing.Optional[GoogleEventarcTriggerTransportPubsub], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleEventarcTriggerTransportPubsub],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleEventarcTriggerTransportPubsubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleEventarcTrigger",
    "GoogleEventarcTriggerConfig",
    "GoogleEventarcTriggerDestination",
    "GoogleEventarcTriggerDestinationCloudRunService",
    "GoogleEventarcTriggerDestinationCloudRunServiceOutputReference",
    "GoogleEventarcTriggerDestinationGke",
    "GoogleEventarcTriggerDestinationGkeOutputReference",
    "GoogleEventarcTriggerDestinationOutputReference",
    "GoogleEventarcTriggerMatchingCriteria",
    "GoogleEventarcTriggerMatchingCriteriaList",
    "GoogleEventarcTriggerMatchingCriteriaOutputReference",
    "GoogleEventarcTriggerTimeouts",
    "GoogleEventarcTriggerTimeoutsOutputReference",
    "GoogleEventarcTriggerTransport",
    "GoogleEventarcTriggerTransportOutputReference",
    "GoogleEventarcTriggerTransportPubsub",
    "GoogleEventarcTriggerTransportPubsubOutputReference",
]

publication.publish()
