'''
# `consul_autopilot_config`

Refer to the Terraform Registory for docs: [`consul_autopilot_config`](https://www.terraform.io/docs/providers/consul/r/autopilot_config).
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


class AutopilotConfig(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.autopilotConfig.AutopilotConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config consul_autopilot_config}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cleanup_dead_servers: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        datacenter: typing.Optional[builtins.str] = None,
        disable_upgrade_migration: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        last_contact_threshold: typing.Optional[builtins.str] = None,
        max_trailing_logs: typing.Optional[jsii.Number] = None,
        redundancy_zone_tag: typing.Optional[builtins.str] = None,
        server_stabilization_time: typing.Optional[builtins.str] = None,
        upgrade_version_tag: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config consul_autopilot_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cleanup_dead_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#cleanup_dead_servers AutopilotConfig#cleanup_dead_servers}.
        :param datacenter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#datacenter AutopilotConfig#datacenter}.
        :param disable_upgrade_migration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#disable_upgrade_migration AutopilotConfig#disable_upgrade_migration}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#id AutopilotConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param last_contact_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#last_contact_threshold AutopilotConfig#last_contact_threshold}.
        :param max_trailing_logs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#max_trailing_logs AutopilotConfig#max_trailing_logs}.
        :param redundancy_zone_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#redundancy_zone_tag AutopilotConfig#redundancy_zone_tag}.
        :param server_stabilization_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#server_stabilization_time AutopilotConfig#server_stabilization_time}.
        :param upgrade_version_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#upgrade_version_tag AutopilotConfig#upgrade_version_tag}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutopilotConfig.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AutopilotConfigConfig(
            cleanup_dead_servers=cleanup_dead_servers,
            datacenter=datacenter,
            disable_upgrade_migration=disable_upgrade_migration,
            id=id,
            last_contact_threshold=last_contact_threshold,
            max_trailing_logs=max_trailing_logs,
            redundancy_zone_tag=redundancy_zone_tag,
            server_stabilization_time=server_stabilization_time,
            upgrade_version_tag=upgrade_version_tag,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCleanupDeadServers")
    def reset_cleanup_dead_servers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCleanupDeadServers", []))

    @jsii.member(jsii_name="resetDatacenter")
    def reset_datacenter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatacenter", []))

    @jsii.member(jsii_name="resetDisableUpgradeMigration")
    def reset_disable_upgrade_migration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableUpgradeMigration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLastContactThreshold")
    def reset_last_contact_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastContactThreshold", []))

    @jsii.member(jsii_name="resetMaxTrailingLogs")
    def reset_max_trailing_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTrailingLogs", []))

    @jsii.member(jsii_name="resetRedundancyZoneTag")
    def reset_redundancy_zone_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedundancyZoneTag", []))

    @jsii.member(jsii_name="resetServerStabilizationTime")
    def reset_server_stabilization_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerStabilizationTime", []))

    @jsii.member(jsii_name="resetUpgradeVersionTag")
    def reset_upgrade_version_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpgradeVersionTag", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="cleanupDeadServersInput")
    def cleanup_dead_servers_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cleanupDeadServersInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterInput")
    def datacenter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datacenterInput"))

    @builtins.property
    @jsii.member(jsii_name="disableUpgradeMigrationInput")
    def disable_upgrade_migration_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableUpgradeMigrationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lastContactThresholdInput")
    def last_contact_threshold_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastContactThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTrailingLogsInput")
    def max_trailing_logs_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxTrailingLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="redundancyZoneTagInput")
    def redundancy_zone_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redundancyZoneTagInput"))

    @builtins.property
    @jsii.member(jsii_name="serverStabilizationTimeInput")
    def server_stabilization_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverStabilizationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="upgradeVersionTagInput")
    def upgrade_version_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "upgradeVersionTagInput"))

    @builtins.property
    @jsii.member(jsii_name="cleanupDeadServers")
    def cleanup_dead_servers(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cleanupDeadServers"))

    @cleanup_dead_servers.setter
    def cleanup_dead_servers(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutopilotConfig, "cleanup_dead_servers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cleanupDeadServers", value)

    @builtins.property
    @jsii.member(jsii_name="datacenter")
    def datacenter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datacenter"))

    @datacenter.setter
    def datacenter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutopilotConfig, "datacenter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenter", value)

    @builtins.property
    @jsii.member(jsii_name="disableUpgradeMigration")
    def disable_upgrade_migration(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableUpgradeMigration"))

    @disable_upgrade_migration.setter
    def disable_upgrade_migration(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutopilotConfig, "disable_upgrade_migration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableUpgradeMigration", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutopilotConfig, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="lastContactThreshold")
    def last_contact_threshold(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastContactThreshold"))

    @last_contact_threshold.setter
    def last_contact_threshold(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutopilotConfig, "last_contact_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastContactThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="maxTrailingLogs")
    def max_trailing_logs(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxTrailingLogs"))

    @max_trailing_logs.setter
    def max_trailing_logs(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutopilotConfig, "max_trailing_logs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTrailingLogs", value)

    @builtins.property
    @jsii.member(jsii_name="redundancyZoneTag")
    def redundancy_zone_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redundancyZoneTag"))

    @redundancy_zone_tag.setter
    def redundancy_zone_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutopilotConfig, "redundancy_zone_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redundancyZoneTag", value)

    @builtins.property
    @jsii.member(jsii_name="serverStabilizationTime")
    def server_stabilization_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverStabilizationTime"))

    @server_stabilization_time.setter
    def server_stabilization_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutopilotConfig, "server_stabilization_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverStabilizationTime", value)

    @builtins.property
    @jsii.member(jsii_name="upgradeVersionTag")
    def upgrade_version_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "upgradeVersionTag"))

    @upgrade_version_tag.setter
    def upgrade_version_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutopilotConfig, "upgrade_version_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upgradeVersionTag", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.autopilotConfig.AutopilotConfigConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cleanup_dead_servers": "cleanupDeadServers",
        "datacenter": "datacenter",
        "disable_upgrade_migration": "disableUpgradeMigration",
        "id": "id",
        "last_contact_threshold": "lastContactThreshold",
        "max_trailing_logs": "maxTrailingLogs",
        "redundancy_zone_tag": "redundancyZoneTag",
        "server_stabilization_time": "serverStabilizationTime",
        "upgrade_version_tag": "upgradeVersionTag",
    },
)
class AutopilotConfigConfig(cdktf.TerraformMetaArguments):
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
        cleanup_dead_servers: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        datacenter: typing.Optional[builtins.str] = None,
        disable_upgrade_migration: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        last_contact_threshold: typing.Optional[builtins.str] = None,
        max_trailing_logs: typing.Optional[jsii.Number] = None,
        redundancy_zone_tag: typing.Optional[builtins.str] = None,
        server_stabilization_time: typing.Optional[builtins.str] = None,
        upgrade_version_tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cleanup_dead_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#cleanup_dead_servers AutopilotConfig#cleanup_dead_servers}.
        :param datacenter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#datacenter AutopilotConfig#datacenter}.
        :param disable_upgrade_migration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#disable_upgrade_migration AutopilotConfig#disable_upgrade_migration}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#id AutopilotConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param last_contact_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#last_contact_threshold AutopilotConfig#last_contact_threshold}.
        :param max_trailing_logs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#max_trailing_logs AutopilotConfig#max_trailing_logs}.
        :param redundancy_zone_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#redundancy_zone_tag AutopilotConfig#redundancy_zone_tag}.
        :param server_stabilization_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#server_stabilization_time AutopilotConfig#server_stabilization_time}.
        :param upgrade_version_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#upgrade_version_tag AutopilotConfig#upgrade_version_tag}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AutopilotConfigConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cleanup_dead_servers", value=cleanup_dead_servers, expected_type=type_hints["cleanup_dead_servers"])
            check_type(argname="argument datacenter", value=datacenter, expected_type=type_hints["datacenter"])
            check_type(argname="argument disable_upgrade_migration", value=disable_upgrade_migration, expected_type=type_hints["disable_upgrade_migration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument last_contact_threshold", value=last_contact_threshold, expected_type=type_hints["last_contact_threshold"])
            check_type(argname="argument max_trailing_logs", value=max_trailing_logs, expected_type=type_hints["max_trailing_logs"])
            check_type(argname="argument redundancy_zone_tag", value=redundancy_zone_tag, expected_type=type_hints["redundancy_zone_tag"])
            check_type(argname="argument server_stabilization_time", value=server_stabilization_time, expected_type=type_hints["server_stabilization_time"])
            check_type(argname="argument upgrade_version_tag", value=upgrade_version_tag, expected_type=type_hints["upgrade_version_tag"])
        self._values: typing.Dict[str, typing.Any] = {}
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
        if cleanup_dead_servers is not None:
            self._values["cleanup_dead_servers"] = cleanup_dead_servers
        if datacenter is not None:
            self._values["datacenter"] = datacenter
        if disable_upgrade_migration is not None:
            self._values["disable_upgrade_migration"] = disable_upgrade_migration
        if id is not None:
            self._values["id"] = id
        if last_contact_threshold is not None:
            self._values["last_contact_threshold"] = last_contact_threshold
        if max_trailing_logs is not None:
            self._values["max_trailing_logs"] = max_trailing_logs
        if redundancy_zone_tag is not None:
            self._values["redundancy_zone_tag"] = redundancy_zone_tag
        if server_stabilization_time is not None:
            self._values["server_stabilization_time"] = server_stabilization_time
        if upgrade_version_tag is not None:
            self._values["upgrade_version_tag"] = upgrade_version_tag

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
    def cleanup_dead_servers(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#cleanup_dead_servers AutopilotConfig#cleanup_dead_servers}.'''
        result = self._values.get("cleanup_dead_servers")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def datacenter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#datacenter AutopilotConfig#datacenter}.'''
        result = self._values.get("datacenter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_upgrade_migration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#disable_upgrade_migration AutopilotConfig#disable_upgrade_migration}.'''
        result = self._values.get("disable_upgrade_migration")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#id AutopilotConfig#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_contact_threshold(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#last_contact_threshold AutopilotConfig#last_contact_threshold}.'''
        result = self._values.get("last_contact_threshold")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_trailing_logs(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#max_trailing_logs AutopilotConfig#max_trailing_logs}.'''
        result = self._values.get("max_trailing_logs")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def redundancy_zone_tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#redundancy_zone_tag AutopilotConfig#redundancy_zone_tag}.'''
        result = self._values.get("redundancy_zone_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_stabilization_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#server_stabilization_time AutopilotConfig#server_stabilization_time}.'''
        result = self._values.get("server_stabilization_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def upgrade_version_tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/autopilot_config#upgrade_version_tag AutopilotConfig#upgrade_version_tag}.'''
        result = self._values.get("upgrade_version_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutopilotConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AutopilotConfig",
    "AutopilotConfigConfig",
]

publication.publish()
