'''
# `azurerm_stream_analytics_output_powerbi`

Refer to the Terraform Registory for docs: [`azurerm_stream_analytics_output_powerbi`](https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi).
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


class StreamAnalyticsOutputPowerbi(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsOutputPowerbi.StreamAnalyticsOutputPowerbi",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi azurerm_stream_analytics_output_powerbi}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        dataset: builtins.str,
        group_id: builtins.str,
        group_name: builtins.str,
        name: builtins.str,
        stream_analytics_job_id: builtins.str,
        table: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["StreamAnalyticsOutputPowerbiTimeouts", typing.Dict[str, typing.Any]]] = None,
        token_user_display_name: typing.Optional[builtins.str] = None,
        token_user_principal_name: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi azurerm_stream_analytics_output_powerbi} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param dataset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#dataset StreamAnalyticsOutputPowerbi#dataset}.
        :param group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#group_id StreamAnalyticsOutputPowerbi#group_id}.
        :param group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#group_name StreamAnalyticsOutputPowerbi#group_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#name StreamAnalyticsOutputPowerbi#name}.
        :param stream_analytics_job_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#stream_analytics_job_id StreamAnalyticsOutputPowerbi#stream_analytics_job_id}.
        :param table: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#table StreamAnalyticsOutputPowerbi#table}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#id StreamAnalyticsOutputPowerbi#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#timeouts StreamAnalyticsOutputPowerbi#timeouts}
        :param token_user_display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#token_user_display_name StreamAnalyticsOutputPowerbi#token_user_display_name}.
        :param token_user_principal_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#token_user_principal_name StreamAnalyticsOutputPowerbi#token_user_principal_name}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StreamAnalyticsOutputPowerbi.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StreamAnalyticsOutputPowerbiConfig(
            dataset=dataset,
            group_id=group_id,
            group_name=group_name,
            name=name,
            stream_analytics_job_id=stream_analytics_job_id,
            table=table,
            id=id,
            timeouts=timeouts,
            token_user_display_name=token_user_display_name,
            token_user_principal_name=token_user_principal_name,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#create StreamAnalyticsOutputPowerbi#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#delete StreamAnalyticsOutputPowerbi#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#read StreamAnalyticsOutputPowerbi#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#update StreamAnalyticsOutputPowerbi#update}.
        '''
        value = StreamAnalyticsOutputPowerbiTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTokenUserDisplayName")
    def reset_token_user_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenUserDisplayName", []))

    @jsii.member(jsii_name="resetTokenUserPrincipalName")
    def reset_token_user_principal_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenUserPrincipalName", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "StreamAnalyticsOutputPowerbiTimeoutsOutputReference":
        return typing.cast("StreamAnalyticsOutputPowerbiTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="datasetInput")
    def dataset_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNameInput")
    def group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="streamAnalyticsJobIdInput")
    def stream_analytics_job_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamAnalyticsJobIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["StreamAnalyticsOutputPowerbiTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["StreamAnalyticsOutputPowerbiTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenUserDisplayNameInput")
    def token_user_display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenUserDisplayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenUserPrincipalNameInput")
    def token_user_principal_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenUserPrincipalNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dataset")
    def dataset(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataset"))

    @dataset.setter
    def dataset(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputPowerbi, "dataset").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataset", value)

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputPowerbi, "group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupName"))

    @group_name.setter
    def group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputPowerbi, "group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputPowerbi, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputPowerbi, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="streamAnalyticsJobId")
    def stream_analytics_job_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamAnalyticsJobId"))

    @stream_analytics_job_id.setter
    def stream_analytics_job_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputPowerbi, "stream_analytics_job_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamAnalyticsJobId", value)

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "table"))

    @table.setter
    def table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputPowerbi, "table").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="tokenUserDisplayName")
    def token_user_display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenUserDisplayName"))

    @token_user_display_name.setter
    def token_user_display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputPowerbi, "token_user_display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenUserDisplayName", value)

    @builtins.property
    @jsii.member(jsii_name="tokenUserPrincipalName")
    def token_user_principal_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenUserPrincipalName"))

    @token_user_principal_name.setter
    def token_user_principal_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputPowerbi, "token_user_principal_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenUserPrincipalName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsOutputPowerbi.StreamAnalyticsOutputPowerbiConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "dataset": "dataset",
        "group_id": "groupId",
        "group_name": "groupName",
        "name": "name",
        "stream_analytics_job_id": "streamAnalyticsJobId",
        "table": "table",
        "id": "id",
        "timeouts": "timeouts",
        "token_user_display_name": "tokenUserDisplayName",
        "token_user_principal_name": "tokenUserPrincipalName",
    },
)
class StreamAnalyticsOutputPowerbiConfig(cdktf.TerraformMetaArguments):
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
        dataset: builtins.str,
        group_id: builtins.str,
        group_name: builtins.str,
        name: builtins.str,
        stream_analytics_job_id: builtins.str,
        table: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["StreamAnalyticsOutputPowerbiTimeouts", typing.Dict[str, typing.Any]]] = None,
        token_user_display_name: typing.Optional[builtins.str] = None,
        token_user_principal_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param dataset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#dataset StreamAnalyticsOutputPowerbi#dataset}.
        :param group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#group_id StreamAnalyticsOutputPowerbi#group_id}.
        :param group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#group_name StreamAnalyticsOutputPowerbi#group_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#name StreamAnalyticsOutputPowerbi#name}.
        :param stream_analytics_job_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#stream_analytics_job_id StreamAnalyticsOutputPowerbi#stream_analytics_job_id}.
        :param table: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#table StreamAnalyticsOutputPowerbi#table}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#id StreamAnalyticsOutputPowerbi#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#timeouts StreamAnalyticsOutputPowerbi#timeouts}
        :param token_user_display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#token_user_display_name StreamAnalyticsOutputPowerbi#token_user_display_name}.
        :param token_user_principal_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#token_user_principal_name StreamAnalyticsOutputPowerbi#token_user_principal_name}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = StreamAnalyticsOutputPowerbiTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(StreamAnalyticsOutputPowerbiConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument dataset", value=dataset, expected_type=type_hints["dataset"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument stream_analytics_job_id", value=stream_analytics_job_id, expected_type=type_hints["stream_analytics_job_id"])
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument token_user_display_name", value=token_user_display_name, expected_type=type_hints["token_user_display_name"])
            check_type(argname="argument token_user_principal_name", value=token_user_principal_name, expected_type=type_hints["token_user_principal_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataset": dataset,
            "group_id": group_id,
            "group_name": group_name,
            "name": name,
            "stream_analytics_job_id": stream_analytics_job_id,
            "table": table,
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
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if token_user_display_name is not None:
            self._values["token_user_display_name"] = token_user_display_name
        if token_user_principal_name is not None:
            self._values["token_user_principal_name"] = token_user_principal_name

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
    def dataset(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#dataset StreamAnalyticsOutputPowerbi#dataset}.'''
        result = self._values.get("dataset")
        assert result is not None, "Required property 'dataset' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#group_id StreamAnalyticsOutputPowerbi#group_id}.'''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#group_name StreamAnalyticsOutputPowerbi#group_name}.'''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#name StreamAnalyticsOutputPowerbi#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stream_analytics_job_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#stream_analytics_job_id StreamAnalyticsOutputPowerbi#stream_analytics_job_id}.'''
        result = self._values.get("stream_analytics_job_id")
        assert result is not None, "Required property 'stream_analytics_job_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#table StreamAnalyticsOutputPowerbi#table}.'''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#id StreamAnalyticsOutputPowerbi#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["StreamAnalyticsOutputPowerbiTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#timeouts StreamAnalyticsOutputPowerbi#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["StreamAnalyticsOutputPowerbiTimeouts"], result)

    @builtins.property
    def token_user_display_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#token_user_display_name StreamAnalyticsOutputPowerbi#token_user_display_name}.'''
        result = self._values.get("token_user_display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_user_principal_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#token_user_principal_name StreamAnalyticsOutputPowerbi#token_user_principal_name}.'''
        result = self._values.get("token_user_principal_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamAnalyticsOutputPowerbiConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsOutputPowerbi.StreamAnalyticsOutputPowerbiTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class StreamAnalyticsOutputPowerbiTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#create StreamAnalyticsOutputPowerbi#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#delete StreamAnalyticsOutputPowerbi#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#read StreamAnalyticsOutputPowerbi#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#update StreamAnalyticsOutputPowerbi#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StreamAnalyticsOutputPowerbiTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#create StreamAnalyticsOutputPowerbi#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#delete StreamAnalyticsOutputPowerbi#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#read StreamAnalyticsOutputPowerbi#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_powerbi#update StreamAnalyticsOutputPowerbi#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamAnalyticsOutputPowerbiTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StreamAnalyticsOutputPowerbiTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsOutputPowerbi.StreamAnalyticsOutputPowerbiTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(StreamAnalyticsOutputPowerbiTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputPowerbiTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputPowerbiTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputPowerbiTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputPowerbiTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StreamAnalyticsOutputPowerbiTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StreamAnalyticsOutputPowerbiTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StreamAnalyticsOutputPowerbiTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputPowerbiTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StreamAnalyticsOutputPowerbi",
    "StreamAnalyticsOutputPowerbiConfig",
    "StreamAnalyticsOutputPowerbiTimeouts",
    "StreamAnalyticsOutputPowerbiTimeoutsOutputReference",
]

publication.publish()
