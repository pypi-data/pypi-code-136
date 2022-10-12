'''
# `google_datastream_private_connection`

Refer to the Terraform Registory for docs: [`google_datastream_private_connection`](https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection).
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


class GoogleDatastreamPrivateConnection(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamPrivateConnection.GoogleDatastreamPrivateConnection",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection google_datastream_private_connection}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        display_name: builtins.str,
        location: builtins.str,
        private_connection_id: builtins.str,
        vpc_peering_config: typing.Union["GoogleDatastreamPrivateConnectionVpcPeeringConfig", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDatastreamPrivateConnectionTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection google_datastream_private_connection} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param display_name: Display name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#display_name GoogleDatastreamPrivateConnection#display_name}
        :param location: The name of the location this repository is located in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#location GoogleDatastreamPrivateConnection#location}
        :param private_connection_id: The private connectivity identifier. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#private_connection_id GoogleDatastreamPrivateConnection#private_connection_id}
        :param vpc_peering_config: vpc_peering_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#vpc_peering_config GoogleDatastreamPrivateConnection#vpc_peering_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#id GoogleDatastreamPrivateConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Labels. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#labels GoogleDatastreamPrivateConnection#labels}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#project GoogleDatastreamPrivateConnection#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#timeouts GoogleDatastreamPrivateConnection#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDatastreamPrivateConnection.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleDatastreamPrivateConnectionConfig(
            display_name=display_name,
            location=location,
            private_connection_id=private_connection_id,
            vpc_peering_config=vpc_peering_config,
            id=id,
            labels=labels,
            project=project,
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
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#create GoogleDatastreamPrivateConnection#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#delete GoogleDatastreamPrivateConnection#delete}.
        '''
        value = GoogleDatastreamPrivateConnectionTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVpcPeeringConfig")
    def put_vpc_peering_config(
        self,
        *,
        subnet: builtins.str,
        vpc: builtins.str,
    ) -> None:
        '''
        :param subnet: A free subnet for peering. (CIDR of /29). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#subnet GoogleDatastreamPrivateConnection#subnet}
        :param vpc: Fully qualified name of the VPC that Datastream will peer to. Format: projects/{project}/global/{networks}/{name}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#vpc GoogleDatastreamPrivateConnection#vpc}
        '''
        value = GoogleDatastreamPrivateConnectionVpcPeeringConfig(
            subnet=subnet, vpc=vpc
        )

        return typing.cast(None, jsii.invoke(self, "putVpcPeeringConfig", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleDatastreamPrivateConnectionTimeoutsOutputReference":
        return typing.cast("GoogleDatastreamPrivateConnectionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="vpcPeeringConfig")
    def vpc_peering_config(
        self,
    ) -> "GoogleDatastreamPrivateConnectionVpcPeeringConfigOutputReference":
        return typing.cast("GoogleDatastreamPrivateConnectionVpcPeeringConfigOutputReference", jsii.get(self, "vpcPeeringConfig"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

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
    @jsii.member(jsii_name="privateConnectionIdInput")
    def private_connection_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateConnectionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleDatastreamPrivateConnectionTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleDatastreamPrivateConnectionTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcPeeringConfigInput")
    def vpc_peering_config_input(
        self,
    ) -> typing.Optional["GoogleDatastreamPrivateConnectionVpcPeeringConfig"]:
        return typing.cast(typing.Optional["GoogleDatastreamPrivateConnectionVpcPeeringConfig"], jsii.get(self, "vpcPeeringConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDatastreamPrivateConnection, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDatastreamPrivateConnection, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDatastreamPrivateConnection, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDatastreamPrivateConnection, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="privateConnectionId")
    def private_connection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateConnectionId"))

    @private_connection_id.setter
    def private_connection_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDatastreamPrivateConnection, "private_connection_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateConnectionId", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDatastreamPrivateConnection, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamPrivateConnection.GoogleDatastreamPrivateConnectionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "display_name": "displayName",
        "location": "location",
        "private_connection_id": "privateConnectionId",
        "vpc_peering_config": "vpcPeeringConfig",
        "id": "id",
        "labels": "labels",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GoogleDatastreamPrivateConnectionConfig(cdktf.TerraformMetaArguments):
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
        display_name: builtins.str,
        location: builtins.str,
        private_connection_id: builtins.str,
        vpc_peering_config: typing.Union["GoogleDatastreamPrivateConnectionVpcPeeringConfig", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDatastreamPrivateConnectionTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param display_name: Display name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#display_name GoogleDatastreamPrivateConnection#display_name}
        :param location: The name of the location this repository is located in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#location GoogleDatastreamPrivateConnection#location}
        :param private_connection_id: The private connectivity identifier. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#private_connection_id GoogleDatastreamPrivateConnection#private_connection_id}
        :param vpc_peering_config: vpc_peering_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#vpc_peering_config GoogleDatastreamPrivateConnection#vpc_peering_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#id GoogleDatastreamPrivateConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Labels. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#labels GoogleDatastreamPrivateConnection#labels}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#project GoogleDatastreamPrivateConnection#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#timeouts GoogleDatastreamPrivateConnection#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(vpc_peering_config, dict):
            vpc_peering_config = GoogleDatastreamPrivateConnectionVpcPeeringConfig(**vpc_peering_config)
        if isinstance(timeouts, dict):
            timeouts = GoogleDatastreamPrivateConnectionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDatastreamPrivateConnectionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument private_connection_id", value=private_connection_id, expected_type=type_hints["private_connection_id"])
            check_type(argname="argument vpc_peering_config", value=vpc_peering_config, expected_type=type_hints["vpc_peering_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "display_name": display_name,
            "location": location,
            "private_connection_id": private_connection_id,
            "vpc_peering_config": vpc_peering_config,
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
    def display_name(self) -> builtins.str:
        '''Display name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#display_name GoogleDatastreamPrivateConnection#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''The name of the location this repository is located in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#location GoogleDatastreamPrivateConnection#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_connection_id(self) -> builtins.str:
        '''The private connectivity identifier.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#private_connection_id GoogleDatastreamPrivateConnection#private_connection_id}
        '''
        result = self._values.get("private_connection_id")
        assert result is not None, "Required property 'private_connection_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_peering_config(self) -> "GoogleDatastreamPrivateConnectionVpcPeeringConfig":
        '''vpc_peering_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#vpc_peering_config GoogleDatastreamPrivateConnection#vpc_peering_config}
        '''
        result = self._values.get("vpc_peering_config")
        assert result is not None, "Required property 'vpc_peering_config' is missing"
        return typing.cast("GoogleDatastreamPrivateConnectionVpcPeeringConfig", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#id GoogleDatastreamPrivateConnection#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#labels GoogleDatastreamPrivateConnection#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#project GoogleDatastreamPrivateConnection#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleDatastreamPrivateConnectionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#timeouts GoogleDatastreamPrivateConnection#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleDatastreamPrivateConnectionTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamPrivateConnectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamPrivateConnection.GoogleDatastreamPrivateConnectionTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class GoogleDatastreamPrivateConnectionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#create GoogleDatastreamPrivateConnection#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#delete GoogleDatastreamPrivateConnection#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDatastreamPrivateConnectionTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#create GoogleDatastreamPrivateConnection#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#delete GoogleDatastreamPrivateConnection#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamPrivateConnectionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamPrivateConnectionTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamPrivateConnection.GoogleDatastreamPrivateConnectionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDatastreamPrivateConnectionTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDatastreamPrivateConnectionTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDatastreamPrivateConnectionTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDatastreamPrivateConnectionTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDatastreamPrivateConnectionTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDatastreamPrivateConnectionTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDatastreamPrivateConnectionTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamPrivateConnection.GoogleDatastreamPrivateConnectionVpcPeeringConfig",
    jsii_struct_bases=[],
    name_mapping={"subnet": "subnet", "vpc": "vpc"},
)
class GoogleDatastreamPrivateConnectionVpcPeeringConfig:
    def __init__(self, *, subnet: builtins.str, vpc: builtins.str) -> None:
        '''
        :param subnet: A free subnet for peering. (CIDR of /29). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#subnet GoogleDatastreamPrivateConnection#subnet}
        :param vpc: Fully qualified name of the VPC that Datastream will peer to. Format: projects/{project}/global/{networks}/{name}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#vpc GoogleDatastreamPrivateConnection#vpc}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDatastreamPrivateConnectionVpcPeeringConfig.__init__)
            check_type(argname="argument subnet", value=subnet, expected_type=type_hints["subnet"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[str, typing.Any] = {
            "subnet": subnet,
            "vpc": vpc,
        }

    @builtins.property
    def subnet(self) -> builtins.str:
        '''A free subnet for peering. (CIDR of /29).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#subnet GoogleDatastreamPrivateConnection#subnet}
        '''
        result = self._values.get("subnet")
        assert result is not None, "Required property 'subnet' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc(self) -> builtins.str:
        '''Fully qualified name of the VPC that Datastream will peer to. Format: projects/{project}/global/{networks}/{name}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_private_connection#vpc GoogleDatastreamPrivateConnection#vpc}
        '''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamPrivateConnectionVpcPeeringConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamPrivateConnectionVpcPeeringConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamPrivateConnection.GoogleDatastreamPrivateConnectionVpcPeeringConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDatastreamPrivateConnectionVpcPeeringConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="subnetInput")
    def subnet_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcInput")
    def vpc_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcInput"))

    @builtins.property
    @jsii.member(jsii_name="subnet")
    def subnet(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnet"))

    @subnet.setter
    def subnet(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDatastreamPrivateConnectionVpcPeeringConfigOutputReference, "subnet").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnet", value)

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpc"))

    @vpc.setter
    def vpc(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDatastreamPrivateConnectionVpcPeeringConfigOutputReference, "vpc").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpc", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamPrivateConnectionVpcPeeringConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamPrivateConnectionVpcPeeringConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamPrivateConnectionVpcPeeringConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDatastreamPrivateConnectionVpcPeeringConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleDatastreamPrivateConnection",
    "GoogleDatastreamPrivateConnectionConfig",
    "GoogleDatastreamPrivateConnectionTimeouts",
    "GoogleDatastreamPrivateConnectionTimeoutsOutputReference",
    "GoogleDatastreamPrivateConnectionVpcPeeringConfig",
    "GoogleDatastreamPrivateConnectionVpcPeeringConfigOutputReference",
]

publication.publish()
