'''
# `ionoscloud_pg_cluster`

Refer to the Terraform Registory for docs: [`ionoscloud_pg_cluster`](https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster).
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


class PgCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.pgCluster.PgCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster ionoscloud_pg_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cores: jsii.Number,
        credentials: typing.Union["PgClusterCredentials", typing.Dict[str, typing.Any]],
        display_name: builtins.str,
        instances: jsii.Number,
        location: builtins.str,
        postgres_version: builtins.str,
        ram: jsii.Number,
        storage_size: jsii.Number,
        storage_type: builtins.str,
        synchronization_mode: builtins.str,
        backup_location: typing.Optional[builtins.str] = None,
        connections: typing.Optional[typing.Union["PgClusterConnections", typing.Dict[str, typing.Any]]] = None,
        from_backup: typing.Optional[typing.Union["PgClusterFromBackup", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        maintenance_window: typing.Optional[typing.Union["PgClusterMaintenanceWindow", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["PgClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster ionoscloud_pg_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cores: The number of CPU cores per replica. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#cores PgCluster#cores}
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#credentials PgCluster#credentials}
        :param display_name: The friendly name of your cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#display_name PgCluster#display_name}
        :param instances: The total number of instances in the cluster (one master and n-1 standbys). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#instances PgCluster#instances}
        :param location: The physical location where the cluster will be created. This will be where all of your instances live. Property cannot be modified after datacenter creation (disallowed in update requests) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#location PgCluster#location}
        :param postgres_version: The PostgreSQL version of your cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#postgres_version PgCluster#postgres_version}
        :param ram: The amount of memory per instance in megabytes. Has to be a multiple of 1024. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#ram PgCluster#ram}
        :param storage_size: The amount of storage per instance in megabytes. Has to be a multiple of 2048. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#storage_size PgCluster#storage_size}
        :param storage_type: The storage type used in your cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#storage_type PgCluster#storage_type}
        :param synchronization_mode: Represents different modes of replication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#synchronization_mode PgCluster#synchronization_mode}
        :param backup_location: The S3 location where the backups will be stored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#backup_location PgCluster#backup_location}
        :param connections: connections block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#connections PgCluster#connections}
        :param from_backup: from_backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#from_backup PgCluster#from_backup}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#id PgCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance_window: maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#maintenance_window PgCluster#maintenance_window}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#timeouts PgCluster#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PgCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PgClusterConfig(
            cores=cores,
            credentials=credentials,
            display_name=display_name,
            instances=instances,
            location=location,
            postgres_version=postgres_version,
            ram=ram,
            storage_size=storage_size,
            storage_type=storage_type,
            synchronization_mode=synchronization_mode,
            backup_location=backup_location,
            connections=connections,
            from_backup=from_backup,
            id=id,
            maintenance_window=maintenance_window,
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

    @jsii.member(jsii_name="putConnections")
    def put_connections(
        self,
        *,
        cidr: builtins.str,
        datacenter_id: builtins.str,
        lan_id: builtins.str,
    ) -> None:
        '''
        :param cidr: The IP and subnet for the database. Note the following unavailable IP ranges: 10.233.64.0/18 10.233.0.0/18 10.233.114.0/24 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#cidr PgCluster#cidr}
        :param datacenter_id: The datacenter to connect your cluster to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#datacenter_id PgCluster#datacenter_id}
        :param lan_id: The LAN to connect your cluster to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#lan_id PgCluster#lan_id}
        '''
        value = PgClusterConnections(
            cidr=cidr, datacenter_id=datacenter_id, lan_id=lan_id
        )

        return typing.cast(None, jsii.invoke(self, "putConnections", [value]))

    @jsii.member(jsii_name="putCredentials")
    def put_credentials(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#password PgCluster#password}.
        :param username: the username for the initial postgres user. some system usernames are restricted (e.g. "postgres", "admin", "standby"). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#username PgCluster#username}
        '''
        value = PgClusterCredentials(password=password, username=username)

        return typing.cast(None, jsii.invoke(self, "putCredentials", [value]))

    @jsii.member(jsii_name="putFromBackup")
    def put_from_backup(
        self,
        *,
        backup_id: builtins.str,
        recovery_target_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param backup_id: The unique ID of the backup you want to restore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#backup_id PgCluster#backup_id}
        :param recovery_target_time: If this value is supplied as ISO 8601 timestamp, the backup will be replayed up until the given timestamp. If empty, the backup will be applied completely. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#recovery_target_time PgCluster#recovery_target_time}
        '''
        value = PgClusterFromBackup(
            backup_id=backup_id, recovery_target_time=recovery_target_time
        )

        return typing.cast(None, jsii.invoke(self, "putFromBackup", [value]))

    @jsii.member(jsii_name="putMaintenanceWindow")
    def put_maintenance_window(
        self,
        *,
        day_of_the_week: builtins.str,
        time: builtins.str,
    ) -> None:
        '''
        :param day_of_the_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#day_of_the_week PgCluster#day_of_the_week}.
        :param time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#time PgCluster#time}.
        '''
        value = PgClusterMaintenanceWindow(day_of_the_week=day_of_the_week, time=time)

        return typing.cast(None, jsii.invoke(self, "putMaintenanceWindow", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#create PgCluster#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#default PgCluster#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#delete PgCluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#update PgCluster#update}.
        '''
        value = PgClusterTimeouts(
            create=create, default=default, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetBackupLocation")
    def reset_backup_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupLocation", []))

    @jsii.member(jsii_name="resetConnections")
    def reset_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnections", []))

    @jsii.member(jsii_name="resetFromBackup")
    def reset_from_backup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFromBackup", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaintenanceWindow")
    def reset_maintenance_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceWindow", []))

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
    @jsii.member(jsii_name="connections")
    def connections(self) -> "PgClusterConnectionsOutputReference":
        return typing.cast("PgClusterConnectionsOutputReference", jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="credentials")
    def credentials(self) -> "PgClusterCredentialsOutputReference":
        return typing.cast("PgClusterCredentialsOutputReference", jsii.get(self, "credentials"))

    @builtins.property
    @jsii.member(jsii_name="fromBackup")
    def from_backup(self) -> "PgClusterFromBackupOutputReference":
        return typing.cast("PgClusterFromBackupOutputReference", jsii.get(self, "fromBackup"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindow")
    def maintenance_window(self) -> "PgClusterMaintenanceWindowOutputReference":
        return typing.cast("PgClusterMaintenanceWindowOutputReference", jsii.get(self, "maintenanceWindow"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "PgClusterTimeoutsOutputReference":
        return typing.cast("PgClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="backupLocationInput")
    def backup_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionsInput")
    def connections_input(self) -> typing.Optional["PgClusterConnections"]:
        return typing.cast(typing.Optional["PgClusterConnections"], jsii.get(self, "connectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="coresInput")
    def cores_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "coresInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsInput")
    def credentials_input(self) -> typing.Optional["PgClusterCredentials"]:
        return typing.cast(typing.Optional["PgClusterCredentials"], jsii.get(self, "credentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="fromBackupInput")
    def from_backup_input(self) -> typing.Optional["PgClusterFromBackup"]:
        return typing.cast(typing.Optional["PgClusterFromBackup"], jsii.get(self, "fromBackupInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instancesInput")
    def instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instancesInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowInput")
    def maintenance_window_input(self) -> typing.Optional["PgClusterMaintenanceWindow"]:
        return typing.cast(typing.Optional["PgClusterMaintenanceWindow"], jsii.get(self, "maintenanceWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="postgresVersionInput")
    def postgres_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "postgresVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="ramInput")
    def ram_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ramInput"))

    @builtins.property
    @jsii.member(jsii_name="storageSizeInput")
    def storage_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="storageTypeInput")
    def storage_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="synchronizationModeInput")
    def synchronization_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "synchronizationModeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["PgClusterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["PgClusterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="backupLocation")
    def backup_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupLocation"))

    @backup_location.setter
    def backup_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgCluster, "backup_location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupLocation", value)

    @builtins.property
    @jsii.member(jsii_name="cores")
    def cores(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cores"))

    @cores.setter
    def cores(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgCluster, "cores").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cores", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgCluster, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgCluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instances")
    def instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instances"))

    @instances.setter
    def instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgCluster, "instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instances", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgCluster, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="postgresVersion")
    def postgres_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postgresVersion"))

    @postgres_version.setter
    def postgres_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgCluster, "postgres_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postgresVersion", value)

    @builtins.property
    @jsii.member(jsii_name="ram")
    def ram(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ram"))

    @ram.setter
    def ram(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgCluster, "ram").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ram", value)

    @builtins.property
    @jsii.member(jsii_name="storageSize")
    def storage_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storageSize"))

    @storage_size.setter
    def storage_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgCluster, "storage_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageSize", value)

    @builtins.property
    @jsii.member(jsii_name="storageType")
    def storage_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageType"))

    @storage_type.setter
    def storage_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgCluster, "storage_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageType", value)

    @builtins.property
    @jsii.member(jsii_name="synchronizationMode")
    def synchronization_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "synchronizationMode"))

    @synchronization_mode.setter
    def synchronization_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgCluster, "synchronization_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "synchronizationMode", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.pgCluster.PgClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cores": "cores",
        "credentials": "credentials",
        "display_name": "displayName",
        "instances": "instances",
        "location": "location",
        "postgres_version": "postgresVersion",
        "ram": "ram",
        "storage_size": "storageSize",
        "storage_type": "storageType",
        "synchronization_mode": "synchronizationMode",
        "backup_location": "backupLocation",
        "connections": "connections",
        "from_backup": "fromBackup",
        "id": "id",
        "maintenance_window": "maintenanceWindow",
        "timeouts": "timeouts",
    },
)
class PgClusterConfig(cdktf.TerraformMetaArguments):
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
        cores: jsii.Number,
        credentials: typing.Union["PgClusterCredentials", typing.Dict[str, typing.Any]],
        display_name: builtins.str,
        instances: jsii.Number,
        location: builtins.str,
        postgres_version: builtins.str,
        ram: jsii.Number,
        storage_size: jsii.Number,
        storage_type: builtins.str,
        synchronization_mode: builtins.str,
        backup_location: typing.Optional[builtins.str] = None,
        connections: typing.Optional[typing.Union["PgClusterConnections", typing.Dict[str, typing.Any]]] = None,
        from_backup: typing.Optional[typing.Union["PgClusterFromBackup", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        maintenance_window: typing.Optional[typing.Union["PgClusterMaintenanceWindow", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["PgClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cores: The number of CPU cores per replica. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#cores PgCluster#cores}
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#credentials PgCluster#credentials}
        :param display_name: The friendly name of your cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#display_name PgCluster#display_name}
        :param instances: The total number of instances in the cluster (one master and n-1 standbys). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#instances PgCluster#instances}
        :param location: The physical location where the cluster will be created. This will be where all of your instances live. Property cannot be modified after datacenter creation (disallowed in update requests) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#location PgCluster#location}
        :param postgres_version: The PostgreSQL version of your cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#postgres_version PgCluster#postgres_version}
        :param ram: The amount of memory per instance in megabytes. Has to be a multiple of 1024. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#ram PgCluster#ram}
        :param storage_size: The amount of storage per instance in megabytes. Has to be a multiple of 2048. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#storage_size PgCluster#storage_size}
        :param storage_type: The storage type used in your cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#storage_type PgCluster#storage_type}
        :param synchronization_mode: Represents different modes of replication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#synchronization_mode PgCluster#synchronization_mode}
        :param backup_location: The S3 location where the backups will be stored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#backup_location PgCluster#backup_location}
        :param connections: connections block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#connections PgCluster#connections}
        :param from_backup: from_backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#from_backup PgCluster#from_backup}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#id PgCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance_window: maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#maintenance_window PgCluster#maintenance_window}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#timeouts PgCluster#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(credentials, dict):
            credentials = PgClusterCredentials(**credentials)
        if isinstance(connections, dict):
            connections = PgClusterConnections(**connections)
        if isinstance(from_backup, dict):
            from_backup = PgClusterFromBackup(**from_backup)
        if isinstance(maintenance_window, dict):
            maintenance_window = PgClusterMaintenanceWindow(**maintenance_window)
        if isinstance(timeouts, dict):
            timeouts = PgClusterTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(PgClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cores", value=cores, expected_type=type_hints["cores"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument instances", value=instances, expected_type=type_hints["instances"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument postgres_version", value=postgres_version, expected_type=type_hints["postgres_version"])
            check_type(argname="argument ram", value=ram, expected_type=type_hints["ram"])
            check_type(argname="argument storage_size", value=storage_size, expected_type=type_hints["storage_size"])
            check_type(argname="argument storage_type", value=storage_type, expected_type=type_hints["storage_type"])
            check_type(argname="argument synchronization_mode", value=synchronization_mode, expected_type=type_hints["synchronization_mode"])
            check_type(argname="argument backup_location", value=backup_location, expected_type=type_hints["backup_location"])
            check_type(argname="argument connections", value=connections, expected_type=type_hints["connections"])
            check_type(argname="argument from_backup", value=from_backup, expected_type=type_hints["from_backup"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument maintenance_window", value=maintenance_window, expected_type=type_hints["maintenance_window"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "cores": cores,
            "credentials": credentials,
            "display_name": display_name,
            "instances": instances,
            "location": location,
            "postgres_version": postgres_version,
            "ram": ram,
            "storage_size": storage_size,
            "storage_type": storage_type,
            "synchronization_mode": synchronization_mode,
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
        if backup_location is not None:
            self._values["backup_location"] = backup_location
        if connections is not None:
            self._values["connections"] = connections
        if from_backup is not None:
            self._values["from_backup"] = from_backup
        if id is not None:
            self._values["id"] = id
        if maintenance_window is not None:
            self._values["maintenance_window"] = maintenance_window
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
    def cores(self) -> jsii.Number:
        '''The number of CPU cores per replica.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#cores PgCluster#cores}
        '''
        result = self._values.get("cores")
        assert result is not None, "Required property 'cores' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def credentials(self) -> "PgClusterCredentials":
        '''credentials block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#credentials PgCluster#credentials}
        '''
        result = self._values.get("credentials")
        assert result is not None, "Required property 'credentials' is missing"
        return typing.cast("PgClusterCredentials", result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The friendly name of your cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#display_name PgCluster#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instances(self) -> jsii.Number:
        '''The total number of instances in the cluster (one master and n-1 standbys).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#instances PgCluster#instances}
        '''
        result = self._values.get("instances")
        assert result is not None, "Required property 'instances' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''The physical location where the cluster will be created.

        This will be where all of your instances live. Property cannot be modified after datacenter creation (disallowed in update requests)

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#location PgCluster#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def postgres_version(self) -> builtins.str:
        '''The PostgreSQL version of your cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#postgres_version PgCluster#postgres_version}
        '''
        result = self._values.get("postgres_version")
        assert result is not None, "Required property 'postgres_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ram(self) -> jsii.Number:
        '''The amount of memory per instance in megabytes. Has to be a multiple of 1024.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#ram PgCluster#ram}
        '''
        result = self._values.get("ram")
        assert result is not None, "Required property 'ram' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def storage_size(self) -> jsii.Number:
        '''The amount of storage per instance in megabytes. Has to be a multiple of 2048.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#storage_size PgCluster#storage_size}
        '''
        result = self._values.get("storage_size")
        assert result is not None, "Required property 'storage_size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def storage_type(self) -> builtins.str:
        '''The storage type used in your cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#storage_type PgCluster#storage_type}
        '''
        result = self._values.get("storage_type")
        assert result is not None, "Required property 'storage_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def synchronization_mode(self) -> builtins.str:
        '''Represents different modes of replication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#synchronization_mode PgCluster#synchronization_mode}
        '''
        result = self._values.get("synchronization_mode")
        assert result is not None, "Required property 'synchronization_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backup_location(self) -> typing.Optional[builtins.str]:
        '''The S3 location where the backups will be stored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#backup_location PgCluster#backup_location}
        '''
        result = self._values.get("backup_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connections(self) -> typing.Optional["PgClusterConnections"]:
        '''connections block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#connections PgCluster#connections}
        '''
        result = self._values.get("connections")
        return typing.cast(typing.Optional["PgClusterConnections"], result)

    @builtins.property
    def from_backup(self) -> typing.Optional["PgClusterFromBackup"]:
        '''from_backup block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#from_backup PgCluster#from_backup}
        '''
        result = self._values.get("from_backup")
        return typing.cast(typing.Optional["PgClusterFromBackup"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#id PgCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_window(self) -> typing.Optional["PgClusterMaintenanceWindow"]:
        '''maintenance_window block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#maintenance_window PgCluster#maintenance_window}
        '''
        result = self._values.get("maintenance_window")
        return typing.cast(typing.Optional["PgClusterMaintenanceWindow"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["PgClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#timeouts PgCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["PgClusterTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PgClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.pgCluster.PgClusterConnections",
    jsii_struct_bases=[],
    name_mapping={"cidr": "cidr", "datacenter_id": "datacenterId", "lan_id": "lanId"},
)
class PgClusterConnections:
    def __init__(
        self,
        *,
        cidr: builtins.str,
        datacenter_id: builtins.str,
        lan_id: builtins.str,
    ) -> None:
        '''
        :param cidr: The IP and subnet for the database. Note the following unavailable IP ranges: 10.233.64.0/18 10.233.0.0/18 10.233.114.0/24 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#cidr PgCluster#cidr}
        :param datacenter_id: The datacenter to connect your cluster to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#datacenter_id PgCluster#datacenter_id}
        :param lan_id: The LAN to connect your cluster to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#lan_id PgCluster#lan_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PgClusterConnections.__init__)
            check_type(argname="argument cidr", value=cidr, expected_type=type_hints["cidr"])
            check_type(argname="argument datacenter_id", value=datacenter_id, expected_type=type_hints["datacenter_id"])
            check_type(argname="argument lan_id", value=lan_id, expected_type=type_hints["lan_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "cidr": cidr,
            "datacenter_id": datacenter_id,
            "lan_id": lan_id,
        }

    @builtins.property
    def cidr(self) -> builtins.str:
        '''The IP and subnet for the database.

        Note the following unavailable IP ranges:
        10.233.64.0/18
        10.233.0.0/18
        10.233.114.0/24

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#cidr PgCluster#cidr}
        '''
        result = self._values.get("cidr")
        assert result is not None, "Required property 'cidr' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def datacenter_id(self) -> builtins.str:
        '''The datacenter to connect your cluster to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#datacenter_id PgCluster#datacenter_id}
        '''
        result = self._values.get("datacenter_id")
        assert result is not None, "Required property 'datacenter_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lan_id(self) -> builtins.str:
        '''The LAN to connect your cluster to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#lan_id PgCluster#lan_id}
        '''
        result = self._values.get("lan_id")
        assert result is not None, "Required property 'lan_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PgClusterConnections(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PgClusterConnectionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.pgCluster.PgClusterConnectionsOutputReference",
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
            type_hints = typing.get_type_hints(PgClusterConnectionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="cidrInput")
    def cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cidrInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterIdInput")
    def datacenter_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datacenterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="lanIdInput")
    def lan_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lanIdInput"))

    @builtins.property
    @jsii.member(jsii_name="cidr")
    def cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cidr"))

    @cidr.setter
    def cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgClusterConnectionsOutputReference, "cidr").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidr", value)

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datacenterId"))

    @datacenter_id.setter
    def datacenter_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgClusterConnectionsOutputReference, "datacenter_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenterId", value)

    @builtins.property
    @jsii.member(jsii_name="lanId")
    def lan_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lanId"))

    @lan_id.setter
    def lan_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgClusterConnectionsOutputReference, "lan_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lanId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PgClusterConnections]:
        return typing.cast(typing.Optional[PgClusterConnections], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PgClusterConnections]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgClusterConnectionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.pgCluster.PgClusterCredentials",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class PgClusterCredentials:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#password PgCluster#password}.
        :param username: the username for the initial postgres user. some system usernames are restricted (e.g. "postgres", "admin", "standby"). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#username PgCluster#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PgClusterCredentials.__init__)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#password PgCluster#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''the username for the initial postgres user. some system usernames are restricted (e.g. "postgres", "admin", "standby").

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#username PgCluster#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PgClusterCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PgClusterCredentialsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.pgCluster.PgClusterCredentialsOutputReference",
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
            type_hints = typing.get_type_hints(PgClusterCredentialsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgClusterCredentialsOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgClusterCredentialsOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PgClusterCredentials]:
        return typing.cast(typing.Optional[PgClusterCredentials], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PgClusterCredentials]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgClusterCredentialsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.pgCluster.PgClusterFromBackup",
    jsii_struct_bases=[],
    name_mapping={
        "backup_id": "backupId",
        "recovery_target_time": "recoveryTargetTime",
    },
)
class PgClusterFromBackup:
    def __init__(
        self,
        *,
        backup_id: builtins.str,
        recovery_target_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param backup_id: The unique ID of the backup you want to restore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#backup_id PgCluster#backup_id}
        :param recovery_target_time: If this value is supplied as ISO 8601 timestamp, the backup will be replayed up until the given timestamp. If empty, the backup will be applied completely. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#recovery_target_time PgCluster#recovery_target_time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PgClusterFromBackup.__init__)
            check_type(argname="argument backup_id", value=backup_id, expected_type=type_hints["backup_id"])
            check_type(argname="argument recovery_target_time", value=recovery_target_time, expected_type=type_hints["recovery_target_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "backup_id": backup_id,
        }
        if recovery_target_time is not None:
            self._values["recovery_target_time"] = recovery_target_time

    @builtins.property
    def backup_id(self) -> builtins.str:
        '''The unique ID of the backup you want to restore.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#backup_id PgCluster#backup_id}
        '''
        result = self._values.get("backup_id")
        assert result is not None, "Required property 'backup_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recovery_target_time(self) -> typing.Optional[builtins.str]:
        '''If this value is supplied as ISO 8601 timestamp, the backup will be replayed up until the given timestamp.

        If empty, the backup will be applied completely.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#recovery_target_time PgCluster#recovery_target_time}
        '''
        result = self._values.get("recovery_target_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PgClusterFromBackup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PgClusterFromBackupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.pgCluster.PgClusterFromBackupOutputReference",
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
            type_hints = typing.get_type_hints(PgClusterFromBackupOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRecoveryTargetTime")
    def reset_recovery_target_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecoveryTargetTime", []))

    @builtins.property
    @jsii.member(jsii_name="backupIdInput")
    def backup_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="recoveryTargetTimeInput")
    def recovery_target_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recoveryTargetTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="backupId")
    def backup_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupId"))

    @backup_id.setter
    def backup_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgClusterFromBackupOutputReference, "backup_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupId", value)

    @builtins.property
    @jsii.member(jsii_name="recoveryTargetTime")
    def recovery_target_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recoveryTargetTime"))

    @recovery_target_time.setter
    def recovery_target_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgClusterFromBackupOutputReference, "recovery_target_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryTargetTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PgClusterFromBackup]:
        return typing.cast(typing.Optional[PgClusterFromBackup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PgClusterFromBackup]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgClusterFromBackupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.pgCluster.PgClusterMaintenanceWindow",
    jsii_struct_bases=[],
    name_mapping={"day_of_the_week": "dayOfTheWeek", "time": "time"},
)
class PgClusterMaintenanceWindow:
    def __init__(self, *, day_of_the_week: builtins.str, time: builtins.str) -> None:
        '''
        :param day_of_the_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#day_of_the_week PgCluster#day_of_the_week}.
        :param time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#time PgCluster#time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PgClusterMaintenanceWindow.__init__)
            check_type(argname="argument day_of_the_week", value=day_of_the_week, expected_type=type_hints["day_of_the_week"])
            check_type(argname="argument time", value=time, expected_type=type_hints["time"])
        self._values: typing.Dict[str, typing.Any] = {
            "day_of_the_week": day_of_the_week,
            "time": time,
        }

    @builtins.property
    def day_of_the_week(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#day_of_the_week PgCluster#day_of_the_week}.'''
        result = self._values.get("day_of_the_week")
        assert result is not None, "Required property 'day_of_the_week' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#time PgCluster#time}.'''
        result = self._values.get("time")
        assert result is not None, "Required property 'time' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PgClusterMaintenanceWindow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PgClusterMaintenanceWindowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.pgCluster.PgClusterMaintenanceWindowOutputReference",
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
            type_hints = typing.get_type_hints(PgClusterMaintenanceWindowOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dayOfTheWeekInput")
    def day_of_the_week_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfTheWeekInput"))

    @builtins.property
    @jsii.member(jsii_name="timeInput")
    def time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeInput"))

    @builtins.property
    @jsii.member(jsii_name="dayOfTheWeek")
    def day_of_the_week(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayOfTheWeek"))

    @day_of_the_week.setter
    def day_of_the_week(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgClusterMaintenanceWindowOutputReference, "day_of_the_week").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfTheWeek", value)

    @builtins.property
    @jsii.member(jsii_name="time")
    def time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "time"))

    @time.setter
    def time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgClusterMaintenanceWindowOutputReference, "time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "time", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PgClusterMaintenanceWindow]:
        return typing.cast(typing.Optional[PgClusterMaintenanceWindow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PgClusterMaintenanceWindow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgClusterMaintenanceWindowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.pgCluster.PgClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "default": "default",
        "delete": "delete",
        "update": "update",
    },
)
class PgClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#create PgCluster#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#default PgCluster#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#delete PgCluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#update PgCluster#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PgClusterTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if default is not None:
            self._values["default"] = default
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#create PgCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#default PgCluster#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#delete PgCluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/pg_cluster#update PgCluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PgClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PgClusterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.pgCluster.PgClusterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(PgClusterTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

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
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

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
            type_hints = typing.get_type_hints(getattr(PgClusterTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgClusterTimeoutsOutputReference, "default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgClusterTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgClusterTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PgClusterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PgClusterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PgClusterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PgClusterTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "PgCluster",
    "PgClusterConfig",
    "PgClusterConnections",
    "PgClusterConnectionsOutputReference",
    "PgClusterCredentials",
    "PgClusterCredentialsOutputReference",
    "PgClusterFromBackup",
    "PgClusterFromBackupOutputReference",
    "PgClusterMaintenanceWindow",
    "PgClusterMaintenanceWindowOutputReference",
    "PgClusterTimeouts",
    "PgClusterTimeoutsOutputReference",
]

publication.publish()
