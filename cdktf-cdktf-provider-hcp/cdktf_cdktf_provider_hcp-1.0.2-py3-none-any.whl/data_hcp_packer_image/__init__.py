'''
# `data_hcp_packer_image`

Refer to the Terraform Registory for docs: [`data_hcp_packer_image`](https://www.terraform.io/docs/providers/hcp/d/packer_image).
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


class DataHcpPackerImage(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.dataHcpPackerImage.DataHcpPackerImage",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/hcp/d/packer_image hcp_packer_image}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        bucket_name: builtins.str,
        cloud_provider: builtins.str,
        region: builtins.str,
        channel: typing.Optional[builtins.str] = None,
        component_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        iteration_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataHcpPackerImageTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/hcp/d/packer_image hcp_packer_image} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param bucket_name: The slug of the HCP Packer Registry image bucket to pull from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#bucket_name DataHcpPackerImage#bucket_name}
        :param cloud_provider: Name of the cloud provider this image is stored-in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#cloud_provider DataHcpPackerImage#cloud_provider}
        :param region: Region this image is stored in, if any. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#region DataHcpPackerImage#region}
        :param channel: The channel that points to the version of the image being retrieved. Either this or ``iteration_id`` must be specified. Note: will incur a billable request Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#channel DataHcpPackerImage#channel}
        :param component_type: Name of the builder that built this image. Ex: ``amazon-ebs.example``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#component_type DataHcpPackerImage#component_type}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#id DataHcpPackerImage#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param iteration_id: The iteration from which to get the image. Either this or ``channel`` must be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#iteration_id DataHcpPackerImage#iteration_id}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#timeouts DataHcpPackerImage#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataHcpPackerImage.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataHcpPackerImageConfig(
            bucket_name=bucket_name,
            cloud_provider=cloud_provider,
            region=region,
            channel=channel,
            component_type=component_type,
            id=id,
            iteration_id=iteration_id,
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
    def put_timeouts(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#default DataHcpPackerImage#default}.
        '''
        value = DataHcpPackerImageTimeouts(default=default)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetChannel")
    def reset_channel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChannel", []))

    @jsii.member(jsii_name="resetComponentType")
    def reset_component_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComponentType", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIterationId")
    def reset_iteration_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIterationId", []))

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
    @jsii.member(jsii_name="buildId")
    def build_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildId"))

    @builtins.property
    @jsii.member(jsii_name="cloudImageId")
    def cloud_image_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudImageId"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="organizationId")
    def organization_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationId"))

    @builtins.property
    @jsii.member(jsii_name="packerRunUuid")
    def packer_run_uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "packerRunUuid"))

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @builtins.property
    @jsii.member(jsii_name="revokeAt")
    def revoke_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "revokeAt"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DataHcpPackerImageTimeoutsOutputReference":
        return typing.cast("DataHcpPackerImageTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="channelInput")
    def channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudProviderInput")
    def cloud_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="componentTypeInput")
    def component_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "componentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="iterationIdInput")
    def iteration_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iterationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DataHcpPackerImageTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataHcpPackerImageTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpPackerImage, "bucket_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="channel")
    def channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channel"))

    @channel.setter
    def channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpPackerImage, "channel").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channel", value)

    @builtins.property
    @jsii.member(jsii_name="cloudProvider")
    def cloud_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudProvider"))

    @cloud_provider.setter
    def cloud_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpPackerImage, "cloud_provider").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudProvider", value)

    @builtins.property
    @jsii.member(jsii_name="componentType")
    def component_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "componentType"))

    @component_type.setter
    def component_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpPackerImage, "component_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "componentType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpPackerImage, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="iterationId")
    def iteration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iterationId"))

    @iteration_id.setter
    def iteration_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpPackerImage, "iteration_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iterationId", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpPackerImage, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.dataHcpPackerImage.DataHcpPackerImageConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "bucket_name": "bucketName",
        "cloud_provider": "cloudProvider",
        "region": "region",
        "channel": "channel",
        "component_type": "componentType",
        "id": "id",
        "iteration_id": "iterationId",
        "timeouts": "timeouts",
    },
)
class DataHcpPackerImageConfig(cdktf.TerraformMetaArguments):
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
        bucket_name: builtins.str,
        cloud_provider: builtins.str,
        region: builtins.str,
        channel: typing.Optional[builtins.str] = None,
        component_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        iteration_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataHcpPackerImageTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param bucket_name: The slug of the HCP Packer Registry image bucket to pull from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#bucket_name DataHcpPackerImage#bucket_name}
        :param cloud_provider: Name of the cloud provider this image is stored-in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#cloud_provider DataHcpPackerImage#cloud_provider}
        :param region: Region this image is stored in, if any. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#region DataHcpPackerImage#region}
        :param channel: The channel that points to the version of the image being retrieved. Either this or ``iteration_id`` must be specified. Note: will incur a billable request Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#channel DataHcpPackerImage#channel}
        :param component_type: Name of the builder that built this image. Ex: ``amazon-ebs.example``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#component_type DataHcpPackerImage#component_type}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#id DataHcpPackerImage#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param iteration_id: The iteration from which to get the image. Either this or ``channel`` must be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#iteration_id DataHcpPackerImage#iteration_id}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#timeouts DataHcpPackerImage#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DataHcpPackerImageTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DataHcpPackerImageConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument cloud_provider", value=cloud_provider, expected_type=type_hints["cloud_provider"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument channel", value=channel, expected_type=type_hints["channel"])
            check_type(argname="argument component_type", value=component_type, expected_type=type_hints["component_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument iteration_id", value=iteration_id, expected_type=type_hints["iteration_id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
            "cloud_provider": cloud_provider,
            "region": region,
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
        if channel is not None:
            self._values["channel"] = channel
        if component_type is not None:
            self._values["component_type"] = component_type
        if id is not None:
            self._values["id"] = id
        if iteration_id is not None:
            self._values["iteration_id"] = iteration_id
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
    def bucket_name(self) -> builtins.str:
        '''The slug of the HCP Packer Registry image bucket to pull from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#bucket_name DataHcpPackerImage#bucket_name}
        '''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloud_provider(self) -> builtins.str:
        '''Name of the cloud provider this image is stored-in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#cloud_provider DataHcpPackerImage#cloud_provider}
        '''
        result = self._values.get("cloud_provider")
        assert result is not None, "Required property 'cloud_provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Region this image is stored in, if any.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#region DataHcpPackerImage#region}
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel(self) -> typing.Optional[builtins.str]:
        '''The channel that points to the version of the image being retrieved.

        Either this or ``iteration_id`` must be specified. Note: will incur a billable request

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#channel DataHcpPackerImage#channel}
        '''
        result = self._values.get("channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def component_type(self) -> typing.Optional[builtins.str]:
        '''Name of the builder that built this image. Ex: ``amazon-ebs.example``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#component_type DataHcpPackerImage#component_type}
        '''
        result = self._values.get("component_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#id DataHcpPackerImage#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iteration_id(self) -> typing.Optional[builtins.str]:
        '''The iteration from which to get the image. Either this or ``channel`` must be specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#iteration_id DataHcpPackerImage#iteration_id}
        '''
        result = self._values.get("iteration_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DataHcpPackerImageTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#timeouts DataHcpPackerImage#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataHcpPackerImageTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataHcpPackerImageConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.dataHcpPackerImage.DataHcpPackerImageTimeouts",
    jsii_struct_bases=[],
    name_mapping={"default": "default"},
)
class DataHcpPackerImageTimeouts:
    def __init__(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#default DataHcpPackerImage#default}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataHcpPackerImageTimeouts.__init__)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/packer_image#default DataHcpPackerImage#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataHcpPackerImageTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataHcpPackerImageTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.dataHcpPackerImage.DataHcpPackerImageTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DataHcpPackerImageTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpPackerImageTimeoutsOutputReference, "default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataHcpPackerImageTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataHcpPackerImageTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataHcpPackerImageTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpPackerImageTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataHcpPackerImage",
    "DataHcpPackerImageConfig",
    "DataHcpPackerImageTimeouts",
    "DataHcpPackerImageTimeoutsOutputReference",
]

publication.publish()
