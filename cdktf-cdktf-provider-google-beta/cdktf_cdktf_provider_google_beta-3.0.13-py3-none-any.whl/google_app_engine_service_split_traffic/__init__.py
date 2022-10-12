'''
# `google_app_engine_service_split_traffic`

Refer to the Terraform Registory for docs: [`google_app_engine_service_split_traffic`](https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic).
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


class GoogleAppEngineServiceSplitTraffic(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineServiceSplitTraffic.GoogleAppEngineServiceSplitTraffic",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic google_app_engine_service_split_traffic}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        service: builtins.str,
        split: typing.Union["GoogleAppEngineServiceSplitTrafficSplit", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        migrate_traffic: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleAppEngineServiceSplitTrafficTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic google_app_engine_service_split_traffic} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param service: The name of the service these settings apply to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#service GoogleAppEngineServiceSplitTraffic#service}
        :param split: split block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#split GoogleAppEngineServiceSplitTraffic#split}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#id GoogleAppEngineServiceSplitTraffic#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param migrate_traffic: If set to true traffic will be migrated to this version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#migrate_traffic GoogleAppEngineServiceSplitTraffic#migrate_traffic}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#project GoogleAppEngineServiceSplitTraffic#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#timeouts GoogleAppEngineServiceSplitTraffic#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineServiceSplitTraffic.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleAppEngineServiceSplitTrafficConfig(
            service=service,
            split=split,
            id=id,
            migrate_traffic=migrate_traffic,
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

    @jsii.member(jsii_name="putSplit")
    def put_split(
        self,
        *,
        allocations: typing.Mapping[builtins.str, builtins.str],
        shard_by: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allocations: Mapping from version IDs within the service to fractional (0.000, 1] allocations of traffic for that version. Each version can be specified only once, but some versions in the service may not have any traffic allocation. Services that have traffic allocated cannot be deleted until either the service is deleted or their traffic allocation is removed. Allocations must sum to 1. Up to two decimal place precision is supported for IP-based splits and up to three decimal places is supported for cookie-based splits. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#allocations GoogleAppEngineServiceSplitTraffic#allocations}
        :param shard_by: Mechanism used to determine which version a request is sent to. The traffic selection algorithm will be stable for either type until allocations are changed. Possible values: ["UNSPECIFIED", "COOKIE", "IP", "RANDOM"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#shard_by GoogleAppEngineServiceSplitTraffic#shard_by}
        '''
        value = GoogleAppEngineServiceSplitTrafficSplit(
            allocations=allocations, shard_by=shard_by
        )

        return typing.cast(None, jsii.invoke(self, "putSplit", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#create GoogleAppEngineServiceSplitTraffic#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#delete GoogleAppEngineServiceSplitTraffic#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#update GoogleAppEngineServiceSplitTraffic#update}.
        '''
        value = GoogleAppEngineServiceSplitTrafficTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMigrateTraffic")
    def reset_migrate_traffic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMigrateTraffic", []))

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
    @jsii.member(jsii_name="split")
    def split(self) -> "GoogleAppEngineServiceSplitTrafficSplitOutputReference":
        return typing.cast("GoogleAppEngineServiceSplitTrafficSplitOutputReference", jsii.get(self, "split"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleAppEngineServiceSplitTrafficTimeoutsOutputReference":
        return typing.cast("GoogleAppEngineServiceSplitTrafficTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="migrateTrafficInput")
    def migrate_traffic_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "migrateTrafficInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="splitInput")
    def split_input(self) -> typing.Optional["GoogleAppEngineServiceSplitTrafficSplit"]:
        return typing.cast(typing.Optional["GoogleAppEngineServiceSplitTrafficSplit"], jsii.get(self, "splitInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleAppEngineServiceSplitTrafficTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleAppEngineServiceSplitTrafficTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineServiceSplitTraffic, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="migrateTraffic")
    def migrate_traffic(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "migrateTraffic"))

    @migrate_traffic.setter
    def migrate_traffic(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineServiceSplitTraffic, "migrate_traffic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "migrateTraffic", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineServiceSplitTraffic, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineServiceSplitTraffic, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineServiceSplitTraffic.GoogleAppEngineServiceSplitTrafficConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "service": "service",
        "split": "split",
        "id": "id",
        "migrate_traffic": "migrateTraffic",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GoogleAppEngineServiceSplitTrafficConfig(cdktf.TerraformMetaArguments):
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
        service: builtins.str,
        split: typing.Union["GoogleAppEngineServiceSplitTrafficSplit", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        migrate_traffic: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleAppEngineServiceSplitTrafficTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param service: The name of the service these settings apply to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#service GoogleAppEngineServiceSplitTraffic#service}
        :param split: split block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#split GoogleAppEngineServiceSplitTraffic#split}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#id GoogleAppEngineServiceSplitTraffic#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param migrate_traffic: If set to true traffic will be migrated to this version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#migrate_traffic GoogleAppEngineServiceSplitTraffic#migrate_traffic}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#project GoogleAppEngineServiceSplitTraffic#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#timeouts GoogleAppEngineServiceSplitTraffic#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(split, dict):
            split = GoogleAppEngineServiceSplitTrafficSplit(**split)
        if isinstance(timeouts, dict):
            timeouts = GoogleAppEngineServiceSplitTrafficTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineServiceSplitTrafficConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument split", value=split, expected_type=type_hints["split"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument migrate_traffic", value=migrate_traffic, expected_type=type_hints["migrate_traffic"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "service": service,
            "split": split,
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
        if migrate_traffic is not None:
            self._values["migrate_traffic"] = migrate_traffic
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
    def service(self) -> builtins.str:
        '''The name of the service these settings apply to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#service GoogleAppEngineServiceSplitTraffic#service}
        '''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def split(self) -> "GoogleAppEngineServiceSplitTrafficSplit":
        '''split block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#split GoogleAppEngineServiceSplitTraffic#split}
        '''
        result = self._values.get("split")
        assert result is not None, "Required property 'split' is missing"
        return typing.cast("GoogleAppEngineServiceSplitTrafficSplit", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#id GoogleAppEngineServiceSplitTraffic#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def migrate_traffic(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true traffic will be migrated to this version.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#migrate_traffic GoogleAppEngineServiceSplitTraffic#migrate_traffic}
        '''
        result = self._values.get("migrate_traffic")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#project GoogleAppEngineServiceSplitTraffic#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleAppEngineServiceSplitTrafficTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#timeouts GoogleAppEngineServiceSplitTraffic#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleAppEngineServiceSplitTrafficTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineServiceSplitTrafficConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineServiceSplitTraffic.GoogleAppEngineServiceSplitTrafficSplit",
    jsii_struct_bases=[],
    name_mapping={"allocations": "allocations", "shard_by": "shardBy"},
)
class GoogleAppEngineServiceSplitTrafficSplit:
    def __init__(
        self,
        *,
        allocations: typing.Mapping[builtins.str, builtins.str],
        shard_by: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allocations: Mapping from version IDs within the service to fractional (0.000, 1] allocations of traffic for that version. Each version can be specified only once, but some versions in the service may not have any traffic allocation. Services that have traffic allocated cannot be deleted until either the service is deleted or their traffic allocation is removed. Allocations must sum to 1. Up to two decimal place precision is supported for IP-based splits and up to three decimal places is supported for cookie-based splits. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#allocations GoogleAppEngineServiceSplitTraffic#allocations}
        :param shard_by: Mechanism used to determine which version a request is sent to. The traffic selection algorithm will be stable for either type until allocations are changed. Possible values: ["UNSPECIFIED", "COOKIE", "IP", "RANDOM"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#shard_by GoogleAppEngineServiceSplitTraffic#shard_by}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineServiceSplitTrafficSplit.__init__)
            check_type(argname="argument allocations", value=allocations, expected_type=type_hints["allocations"])
            check_type(argname="argument shard_by", value=shard_by, expected_type=type_hints["shard_by"])
        self._values: typing.Dict[str, typing.Any] = {
            "allocations": allocations,
        }
        if shard_by is not None:
            self._values["shard_by"] = shard_by

    @builtins.property
    def allocations(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Mapping from version IDs within the service to fractional (0.000, 1] allocations of traffic for that version. Each version can be specified only once, but some versions in the service may not have any traffic allocation. Services that have traffic allocated cannot be deleted until either the service is deleted or their traffic allocation is removed. Allocations must sum to 1. Up to two decimal place precision is supported for IP-based splits and up to three decimal places is supported for cookie-based splits.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#allocations GoogleAppEngineServiceSplitTraffic#allocations}
        '''
        result = self._values.get("allocations")
        assert result is not None, "Required property 'allocations' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def shard_by(self) -> typing.Optional[builtins.str]:
        '''Mechanism used to determine which version a request is sent to.

        The traffic selection algorithm will be stable for either type until allocations are changed. Possible values: ["UNSPECIFIED", "COOKIE", "IP", "RANDOM"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#shard_by GoogleAppEngineServiceSplitTraffic#shard_by}
        '''
        result = self._values.get("shard_by")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineServiceSplitTrafficSplit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineServiceSplitTrafficSplitOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineServiceSplitTraffic.GoogleAppEngineServiceSplitTrafficSplitOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineServiceSplitTrafficSplitOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetShardBy")
    def reset_shard_by(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShardBy", []))

    @builtins.property
    @jsii.member(jsii_name="allocationsInput")
    def allocations_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "allocationsInput"))

    @builtins.property
    @jsii.member(jsii_name="shardByInput")
    def shard_by_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shardByInput"))

    @builtins.property
    @jsii.member(jsii_name="allocations")
    def allocations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "allocations"))

    @allocations.setter
    def allocations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineServiceSplitTrafficSplitOutputReference, "allocations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocations", value)

    @builtins.property
    @jsii.member(jsii_name="shardBy")
    def shard_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shardBy"))

    @shard_by.setter
    def shard_by(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineServiceSplitTrafficSplitOutputReference, "shard_by").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shardBy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineServiceSplitTrafficSplit]:
        return typing.cast(typing.Optional[GoogleAppEngineServiceSplitTrafficSplit], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineServiceSplitTrafficSplit],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineServiceSplitTrafficSplitOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineServiceSplitTraffic.GoogleAppEngineServiceSplitTrafficTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleAppEngineServiceSplitTrafficTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#create GoogleAppEngineServiceSplitTraffic#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#delete GoogleAppEngineServiceSplitTraffic#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#update GoogleAppEngineServiceSplitTraffic#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineServiceSplitTrafficTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#create GoogleAppEngineServiceSplitTraffic#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#delete GoogleAppEngineServiceSplitTraffic#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_service_split_traffic#update GoogleAppEngineServiceSplitTraffic#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineServiceSplitTrafficTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineServiceSplitTrafficTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineServiceSplitTraffic.GoogleAppEngineServiceSplitTrafficTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineServiceSplitTrafficTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineServiceSplitTrafficTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineServiceSplitTrafficTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineServiceSplitTrafficTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAppEngineServiceSplitTrafficTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAppEngineServiceSplitTrafficTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAppEngineServiceSplitTrafficTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineServiceSplitTrafficTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleAppEngineServiceSplitTraffic",
    "GoogleAppEngineServiceSplitTrafficConfig",
    "GoogleAppEngineServiceSplitTrafficSplit",
    "GoogleAppEngineServiceSplitTrafficSplitOutputReference",
    "GoogleAppEngineServiceSplitTrafficTimeouts",
    "GoogleAppEngineServiceSplitTrafficTimeoutsOutputReference",
]

publication.publish()
