'''
# `oraclepaas_mysql_service_instance`

Refer to the Terraform Registory for docs: [`oraclepaas_mysql_service_instance`](https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance).
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


class MysqlServiceInstance(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance oraclepaas_mysql_service_instance}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        mysql_configuration: typing.Union["MysqlServiceInstanceMysqlConfiguration", typing.Dict[str, typing.Any]],
        name: builtins.str,
        shape: builtins.str,
        ssh_public_key: builtins.str,
        availability_domain: typing.Optional[builtins.str] = None,
        backup_destination: typing.Optional[builtins.str] = None,
        backups: typing.Optional[typing.Union["MysqlServiceInstanceBackups", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ip_network: typing.Optional[builtins.str] = None,
        metering_frequency: typing.Optional[builtins.str] = None,
        notification_email: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        subnet: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MysqlServiceInstanceTimeouts", typing.Dict[str, typing.Any]]] = None,
        vm_user: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance oraclepaas_mysql_service_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param mysql_configuration: mysql_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_configuration MysqlServiceInstance#mysql_configuration}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#name MysqlServiceInstance#name}.
        :param shape: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#shape MysqlServiceInstance#shape}.
        :param ssh_public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#ssh_public_key MysqlServiceInstance#ssh_public_key}.
        :param availability_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#availability_domain MysqlServiceInstance#availability_domain}.
        :param backup_destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#backup_destination MysqlServiceInstance#backup_destination}.
        :param backups: backups block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#backups MysqlServiceInstance#backups}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#description MysqlServiceInstance#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#id MysqlServiceInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#ip_network MysqlServiceInstance#ip_network}.
        :param metering_frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#metering_frequency MysqlServiceInstance#metering_frequency}.
        :param notification_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#notification_email MysqlServiceInstance#notification_email}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#region MysqlServiceInstance#region}.
        :param subnet: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#subnet MysqlServiceInstance#subnet}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#timeouts MysqlServiceInstance#timeouts}
        :param vm_user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#vm_user MysqlServiceInstance#vm_user}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MysqlServiceInstance.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MysqlServiceInstanceConfig(
            mysql_configuration=mysql_configuration,
            name=name,
            shape=shape,
            ssh_public_key=ssh_public_key,
            availability_domain=availability_domain,
            backup_destination=backup_destination,
            backups=backups,
            description=description,
            id=id,
            ip_network=ip_network,
            metering_frequency=metering_frequency,
            notification_email=notification_email,
            region=region,
            subnet=subnet,
            timeouts=timeouts,
            vm_user=vm_user,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBackups")
    def put_backups(
        self,
        *,
        cloud_storage_container: builtins.str,
        cloud_storage_password: typing.Optional[builtins.str] = None,
        cloud_storage_username: typing.Optional[builtins.str] = None,
        create_if_missing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cloud_storage_container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#cloud_storage_container MysqlServiceInstance#cloud_storage_container}.
        :param cloud_storage_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#cloud_storage_password MysqlServiceInstance#cloud_storage_password}.
        :param cloud_storage_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#cloud_storage_username MysqlServiceInstance#cloud_storage_username}.
        :param create_if_missing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#create_if_missing MysqlServiceInstance#create_if_missing}.
        '''
        value = MysqlServiceInstanceBackups(
            cloud_storage_container=cloud_storage_container,
            cloud_storage_password=cloud_storage_password,
            cloud_storage_username=cloud_storage_username,
            create_if_missing=create_if_missing,
        )

        return typing.cast(None, jsii.invoke(self, "putBackups", [value]))

    @jsii.member(jsii_name="putMysqlConfiguration")
    def put_mysql_configuration(
        self,
        *,
        db_name: typing.Optional[builtins.str] = None,
        db_storage: typing.Optional[jsii.Number] = None,
        enterprise_monitor_configuration: typing.Optional[typing.Union["MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration", typing.Dict[str, typing.Any]]] = None,
        mysql_charset: typing.Optional[builtins.str] = None,
        mysql_collation: typing.Optional[builtins.str] = None,
        mysql_password: typing.Optional[builtins.str] = None,
        mysql_port: typing.Optional[jsii.Number] = None,
        mysql_username: typing.Optional[builtins.str] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        source_service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param db_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#db_name MysqlServiceInstance#db_name}.
        :param db_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#db_storage MysqlServiceInstance#db_storage}.
        :param enterprise_monitor_configuration: enterprise_monitor_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#enterprise_monitor_configuration MysqlServiceInstance#enterprise_monitor_configuration}
        :param mysql_charset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_charset MysqlServiceInstance#mysql_charset}.
        :param mysql_collation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_collation MysqlServiceInstance#mysql_collation}.
        :param mysql_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_password MysqlServiceInstance#mysql_password}.
        :param mysql_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_port MysqlServiceInstance#mysql_port}.
        :param mysql_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_username MysqlServiceInstance#mysql_username}.
        :param snapshot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#snapshot_name MysqlServiceInstance#snapshot_name}.
        :param source_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#source_service_name MysqlServiceInstance#source_service_name}.
        '''
        value = MysqlServiceInstanceMysqlConfiguration(
            db_name=db_name,
            db_storage=db_storage,
            enterprise_monitor_configuration=enterprise_monitor_configuration,
            mysql_charset=mysql_charset,
            mysql_collation=mysql_collation,
            mysql_password=mysql_password,
            mysql_port=mysql_port,
            mysql_username=mysql_username,
            snapshot_name=snapshot_name,
            source_service_name=source_service_name,
        )

        return typing.cast(None, jsii.invoke(self, "putMysqlConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#create MysqlServiceInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#delete MysqlServiceInstance#delete}.
        '''
        value = MysqlServiceInstanceTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAvailabilityDomain")
    def reset_availability_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityDomain", []))

    @jsii.member(jsii_name="resetBackupDestination")
    def reset_backup_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupDestination", []))

    @jsii.member(jsii_name="resetBackups")
    def reset_backups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackups", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpNetwork")
    def reset_ip_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpNetwork", []))

    @jsii.member(jsii_name="resetMeteringFrequency")
    def reset_metering_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMeteringFrequency", []))

    @jsii.member(jsii_name="resetNotificationEmail")
    def reset_notification_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationEmail", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetSubnet")
    def reset_subnet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnet", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVmUser")
    def reset_vm_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVmUser", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="backups")
    def backups(self) -> "MysqlServiceInstanceBackupsOutputReference":
        return typing.cast("MysqlServiceInstanceBackupsOutputReference", jsii.get(self, "backups"))

    @builtins.property
    @jsii.member(jsii_name="baseReleaseVersion")
    def base_release_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baseReleaseVersion"))

    @builtins.property
    @jsii.member(jsii_name="emUrl")
    def em_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emUrl"))

    @builtins.property
    @jsii.member(jsii_name="mysqlConfiguration")
    def mysql_configuration(
        self,
    ) -> "MysqlServiceInstanceMysqlConfigurationOutputReference":
        return typing.cast("MysqlServiceInstanceMysqlConfigurationOutputReference", jsii.get(self, "mysqlConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="releaseVersion")
    def release_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "releaseVersion"))

    @builtins.property
    @jsii.member(jsii_name="serviceVersion")
    def service_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceVersion"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MysqlServiceInstanceTimeoutsOutputReference":
        return typing.cast("MysqlServiceInstanceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="availabilityDomainInput")
    def availability_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="backupDestinationInput")
    def backup_destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupDestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="backupsInput")
    def backups_input(self) -> typing.Optional["MysqlServiceInstanceBackups"]:
        return typing.cast(typing.Optional["MysqlServiceInstanceBackups"], jsii.get(self, "backupsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipNetworkInput")
    def ip_network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="meteringFrequencyInput")
    def metering_frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "meteringFrequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlConfigurationInput")
    def mysql_configuration_input(
        self,
    ) -> typing.Optional["MysqlServiceInstanceMysqlConfiguration"]:
        return typing.cast(typing.Optional["MysqlServiceInstanceMysqlConfiguration"], jsii.get(self, "mysqlConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationEmailInput")
    def notification_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="shapeInput")
    def shape_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shapeInput"))

    @builtins.property
    @jsii.member(jsii_name="sshPublicKeyInput")
    def ssh_public_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sshPublicKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetInput")
    def subnet_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MysqlServiceInstanceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MysqlServiceInstanceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vmUserInput")
    def vm_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmUserInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityDomain")
    def availability_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityDomain"))

    @availability_domain.setter
    def availability_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstance, "availability_domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityDomain", value)

    @builtins.property
    @jsii.member(jsii_name="backupDestination")
    def backup_destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupDestination"))

    @backup_destination.setter
    def backup_destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstance, "backup_destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupDestination", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstance, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstance, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipNetwork")
    def ip_network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipNetwork"))

    @ip_network.setter
    def ip_network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstance, "ip_network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="meteringFrequency")
    def metering_frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "meteringFrequency"))

    @metering_frequency.setter
    def metering_frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstance, "metering_frequency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "meteringFrequency", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstance, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notificationEmail")
    def notification_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationEmail"))

    @notification_email.setter
    def notification_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstance, "notification_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationEmail", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstance, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="shape")
    def shape(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shape"))

    @shape.setter
    def shape(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstance, "shape").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shape", value)

    @builtins.property
    @jsii.member(jsii_name="sshPublicKey")
    def ssh_public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sshPublicKey"))

    @ssh_public_key.setter
    def ssh_public_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstance, "ssh_public_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPublicKey", value)

    @builtins.property
    @jsii.member(jsii_name="subnet")
    def subnet(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnet"))

    @subnet.setter
    def subnet(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstance, "subnet").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnet", value)

    @builtins.property
    @jsii.member(jsii_name="vmUser")
    def vm_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmUser"))

    @vm_user.setter
    def vm_user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstance, "vm_user").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmUser", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstanceBackups",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_storage_container": "cloudStorageContainer",
        "cloud_storage_password": "cloudStoragePassword",
        "cloud_storage_username": "cloudStorageUsername",
        "create_if_missing": "createIfMissing",
    },
)
class MysqlServiceInstanceBackups:
    def __init__(
        self,
        *,
        cloud_storage_container: builtins.str,
        cloud_storage_password: typing.Optional[builtins.str] = None,
        cloud_storage_username: typing.Optional[builtins.str] = None,
        create_if_missing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cloud_storage_container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#cloud_storage_container MysqlServiceInstance#cloud_storage_container}.
        :param cloud_storage_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#cloud_storage_password MysqlServiceInstance#cloud_storage_password}.
        :param cloud_storage_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#cloud_storage_username MysqlServiceInstance#cloud_storage_username}.
        :param create_if_missing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#create_if_missing MysqlServiceInstance#create_if_missing}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MysqlServiceInstanceBackups.__init__)
            check_type(argname="argument cloud_storage_container", value=cloud_storage_container, expected_type=type_hints["cloud_storage_container"])
            check_type(argname="argument cloud_storage_password", value=cloud_storage_password, expected_type=type_hints["cloud_storage_password"])
            check_type(argname="argument cloud_storage_username", value=cloud_storage_username, expected_type=type_hints["cloud_storage_username"])
            check_type(argname="argument create_if_missing", value=create_if_missing, expected_type=type_hints["create_if_missing"])
        self._values: typing.Dict[str, typing.Any] = {
            "cloud_storage_container": cloud_storage_container,
        }
        if cloud_storage_password is not None:
            self._values["cloud_storage_password"] = cloud_storage_password
        if cloud_storage_username is not None:
            self._values["cloud_storage_username"] = cloud_storage_username
        if create_if_missing is not None:
            self._values["create_if_missing"] = create_if_missing

    @builtins.property
    def cloud_storage_container(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#cloud_storage_container MysqlServiceInstance#cloud_storage_container}.'''
        result = self._values.get("cloud_storage_container")
        assert result is not None, "Required property 'cloud_storage_container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloud_storage_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#cloud_storage_password MysqlServiceInstance#cloud_storage_password}.'''
        result = self._values.get("cloud_storage_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_storage_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#cloud_storage_username MysqlServiceInstance#cloud_storage_username}.'''
        result = self._values.get("cloud_storage_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def create_if_missing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#create_if_missing MysqlServiceInstance#create_if_missing}.'''
        result = self._values.get("create_if_missing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MysqlServiceInstanceBackups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MysqlServiceInstanceBackupsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstanceBackupsOutputReference",
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
            type_hints = typing.get_type_hints(MysqlServiceInstanceBackupsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCloudStoragePassword")
    def reset_cloud_storage_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudStoragePassword", []))

    @jsii.member(jsii_name="resetCloudStorageUsername")
    def reset_cloud_storage_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudStorageUsername", []))

    @jsii.member(jsii_name="resetCreateIfMissing")
    def reset_create_if_missing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateIfMissing", []))

    @builtins.property
    @jsii.member(jsii_name="cloudStorageContainerInput")
    def cloud_storage_container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudStorageContainerInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudStoragePasswordInput")
    def cloud_storage_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudStoragePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudStorageUsernameInput")
    def cloud_storage_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudStorageUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="createIfMissingInput")
    def create_if_missing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "createIfMissingInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudStorageContainer")
    def cloud_storage_container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudStorageContainer"))

    @cloud_storage_container.setter
    def cloud_storage_container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceBackupsOutputReference, "cloud_storage_container").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudStorageContainer", value)

    @builtins.property
    @jsii.member(jsii_name="cloudStoragePassword")
    def cloud_storage_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudStoragePassword"))

    @cloud_storage_password.setter
    def cloud_storage_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceBackupsOutputReference, "cloud_storage_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudStoragePassword", value)

    @builtins.property
    @jsii.member(jsii_name="cloudStorageUsername")
    def cloud_storage_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudStorageUsername"))

    @cloud_storage_username.setter
    def cloud_storage_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceBackupsOutputReference, "cloud_storage_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudStorageUsername", value)

    @builtins.property
    @jsii.member(jsii_name="createIfMissing")
    def create_if_missing(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "createIfMissing"))

    @create_if_missing.setter
    def create_if_missing(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceBackupsOutputReference, "create_if_missing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createIfMissing", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MysqlServiceInstanceBackups]:
        return typing.cast(typing.Optional[MysqlServiceInstanceBackups], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MysqlServiceInstanceBackups],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceBackupsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstanceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "mysql_configuration": "mysqlConfiguration",
        "name": "name",
        "shape": "shape",
        "ssh_public_key": "sshPublicKey",
        "availability_domain": "availabilityDomain",
        "backup_destination": "backupDestination",
        "backups": "backups",
        "description": "description",
        "id": "id",
        "ip_network": "ipNetwork",
        "metering_frequency": "meteringFrequency",
        "notification_email": "notificationEmail",
        "region": "region",
        "subnet": "subnet",
        "timeouts": "timeouts",
        "vm_user": "vmUser",
    },
)
class MysqlServiceInstanceConfig(cdktf.TerraformMetaArguments):
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
        mysql_configuration: typing.Union["MysqlServiceInstanceMysqlConfiguration", typing.Dict[str, typing.Any]],
        name: builtins.str,
        shape: builtins.str,
        ssh_public_key: builtins.str,
        availability_domain: typing.Optional[builtins.str] = None,
        backup_destination: typing.Optional[builtins.str] = None,
        backups: typing.Optional[typing.Union[MysqlServiceInstanceBackups, typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ip_network: typing.Optional[builtins.str] = None,
        metering_frequency: typing.Optional[builtins.str] = None,
        notification_email: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        subnet: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MysqlServiceInstanceTimeouts", typing.Dict[str, typing.Any]]] = None,
        vm_user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param mysql_configuration: mysql_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_configuration MysqlServiceInstance#mysql_configuration}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#name MysqlServiceInstance#name}.
        :param shape: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#shape MysqlServiceInstance#shape}.
        :param ssh_public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#ssh_public_key MysqlServiceInstance#ssh_public_key}.
        :param availability_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#availability_domain MysqlServiceInstance#availability_domain}.
        :param backup_destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#backup_destination MysqlServiceInstance#backup_destination}.
        :param backups: backups block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#backups MysqlServiceInstance#backups}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#description MysqlServiceInstance#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#id MysqlServiceInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#ip_network MysqlServiceInstance#ip_network}.
        :param metering_frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#metering_frequency MysqlServiceInstance#metering_frequency}.
        :param notification_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#notification_email MysqlServiceInstance#notification_email}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#region MysqlServiceInstance#region}.
        :param subnet: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#subnet MysqlServiceInstance#subnet}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#timeouts MysqlServiceInstance#timeouts}
        :param vm_user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#vm_user MysqlServiceInstance#vm_user}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(mysql_configuration, dict):
            mysql_configuration = MysqlServiceInstanceMysqlConfiguration(**mysql_configuration)
        if isinstance(backups, dict):
            backups = MysqlServiceInstanceBackups(**backups)
        if isinstance(timeouts, dict):
            timeouts = MysqlServiceInstanceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MysqlServiceInstanceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument mysql_configuration", value=mysql_configuration, expected_type=type_hints["mysql_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument shape", value=shape, expected_type=type_hints["shape"])
            check_type(argname="argument ssh_public_key", value=ssh_public_key, expected_type=type_hints["ssh_public_key"])
            check_type(argname="argument availability_domain", value=availability_domain, expected_type=type_hints["availability_domain"])
            check_type(argname="argument backup_destination", value=backup_destination, expected_type=type_hints["backup_destination"])
            check_type(argname="argument backups", value=backups, expected_type=type_hints["backups"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_network", value=ip_network, expected_type=type_hints["ip_network"])
            check_type(argname="argument metering_frequency", value=metering_frequency, expected_type=type_hints["metering_frequency"])
            check_type(argname="argument notification_email", value=notification_email, expected_type=type_hints["notification_email"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument subnet", value=subnet, expected_type=type_hints["subnet"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vm_user", value=vm_user, expected_type=type_hints["vm_user"])
        self._values: typing.Dict[str, typing.Any] = {
            "mysql_configuration": mysql_configuration,
            "name": name,
            "shape": shape,
            "ssh_public_key": ssh_public_key,
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
        if availability_domain is not None:
            self._values["availability_domain"] = availability_domain
        if backup_destination is not None:
            self._values["backup_destination"] = backup_destination
        if backups is not None:
            self._values["backups"] = backups
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if ip_network is not None:
            self._values["ip_network"] = ip_network
        if metering_frequency is not None:
            self._values["metering_frequency"] = metering_frequency
        if notification_email is not None:
            self._values["notification_email"] = notification_email
        if region is not None:
            self._values["region"] = region
        if subnet is not None:
            self._values["subnet"] = subnet
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vm_user is not None:
            self._values["vm_user"] = vm_user

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
    def mysql_configuration(self) -> "MysqlServiceInstanceMysqlConfiguration":
        '''mysql_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_configuration MysqlServiceInstance#mysql_configuration}
        '''
        result = self._values.get("mysql_configuration")
        assert result is not None, "Required property 'mysql_configuration' is missing"
        return typing.cast("MysqlServiceInstanceMysqlConfiguration", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#name MysqlServiceInstance#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def shape(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#shape MysqlServiceInstance#shape}.'''
        result = self._values.get("shape")
        assert result is not None, "Required property 'shape' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ssh_public_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#ssh_public_key MysqlServiceInstance#ssh_public_key}.'''
        result = self._values.get("ssh_public_key")
        assert result is not None, "Required property 'ssh_public_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def availability_domain(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#availability_domain MysqlServiceInstance#availability_domain}.'''
        result = self._values.get("availability_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_destination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#backup_destination MysqlServiceInstance#backup_destination}.'''
        result = self._values.get("backup_destination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backups(self) -> typing.Optional[MysqlServiceInstanceBackups]:
        '''backups block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#backups MysqlServiceInstance#backups}
        '''
        result = self._values.get("backups")
        return typing.cast(typing.Optional[MysqlServiceInstanceBackups], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#description MysqlServiceInstance#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#id MysqlServiceInstance#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_network(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#ip_network MysqlServiceInstance#ip_network}.'''
        result = self._values.get("ip_network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metering_frequency(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#metering_frequency MysqlServiceInstance#metering_frequency}.'''
        result = self._values.get("metering_frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_email(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#notification_email MysqlServiceInstance#notification_email}.'''
        result = self._values.get("notification_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#region MysqlServiceInstance#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#subnet MysqlServiceInstance#subnet}.'''
        result = self._values.get("subnet")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MysqlServiceInstanceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#timeouts MysqlServiceInstance#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MysqlServiceInstanceTimeouts"], result)

    @builtins.property
    def vm_user(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#vm_user MysqlServiceInstance#vm_user}.'''
        result = self._values.get("vm_user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MysqlServiceInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstanceMysqlConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "db_name": "dbName",
        "db_storage": "dbStorage",
        "enterprise_monitor_configuration": "enterpriseMonitorConfiguration",
        "mysql_charset": "mysqlCharset",
        "mysql_collation": "mysqlCollation",
        "mysql_password": "mysqlPassword",
        "mysql_port": "mysqlPort",
        "mysql_username": "mysqlUsername",
        "snapshot_name": "snapshotName",
        "source_service_name": "sourceServiceName",
    },
)
class MysqlServiceInstanceMysqlConfiguration:
    def __init__(
        self,
        *,
        db_name: typing.Optional[builtins.str] = None,
        db_storage: typing.Optional[jsii.Number] = None,
        enterprise_monitor_configuration: typing.Optional[typing.Union["MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration", typing.Dict[str, typing.Any]]] = None,
        mysql_charset: typing.Optional[builtins.str] = None,
        mysql_collation: typing.Optional[builtins.str] = None,
        mysql_password: typing.Optional[builtins.str] = None,
        mysql_port: typing.Optional[jsii.Number] = None,
        mysql_username: typing.Optional[builtins.str] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        source_service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param db_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#db_name MysqlServiceInstance#db_name}.
        :param db_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#db_storage MysqlServiceInstance#db_storage}.
        :param enterprise_monitor_configuration: enterprise_monitor_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#enterprise_monitor_configuration MysqlServiceInstance#enterprise_monitor_configuration}
        :param mysql_charset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_charset MysqlServiceInstance#mysql_charset}.
        :param mysql_collation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_collation MysqlServiceInstance#mysql_collation}.
        :param mysql_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_password MysqlServiceInstance#mysql_password}.
        :param mysql_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_port MysqlServiceInstance#mysql_port}.
        :param mysql_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_username MysqlServiceInstance#mysql_username}.
        :param snapshot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#snapshot_name MysqlServiceInstance#snapshot_name}.
        :param source_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#source_service_name MysqlServiceInstance#source_service_name}.
        '''
        if isinstance(enterprise_monitor_configuration, dict):
            enterprise_monitor_configuration = MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration(**enterprise_monitor_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(MysqlServiceInstanceMysqlConfiguration.__init__)
            check_type(argname="argument db_name", value=db_name, expected_type=type_hints["db_name"])
            check_type(argname="argument db_storage", value=db_storage, expected_type=type_hints["db_storage"])
            check_type(argname="argument enterprise_monitor_configuration", value=enterprise_monitor_configuration, expected_type=type_hints["enterprise_monitor_configuration"])
            check_type(argname="argument mysql_charset", value=mysql_charset, expected_type=type_hints["mysql_charset"])
            check_type(argname="argument mysql_collation", value=mysql_collation, expected_type=type_hints["mysql_collation"])
            check_type(argname="argument mysql_password", value=mysql_password, expected_type=type_hints["mysql_password"])
            check_type(argname="argument mysql_port", value=mysql_port, expected_type=type_hints["mysql_port"])
            check_type(argname="argument mysql_username", value=mysql_username, expected_type=type_hints["mysql_username"])
            check_type(argname="argument snapshot_name", value=snapshot_name, expected_type=type_hints["snapshot_name"])
            check_type(argname="argument source_service_name", value=source_service_name, expected_type=type_hints["source_service_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if db_name is not None:
            self._values["db_name"] = db_name
        if db_storage is not None:
            self._values["db_storage"] = db_storage
        if enterprise_monitor_configuration is not None:
            self._values["enterprise_monitor_configuration"] = enterprise_monitor_configuration
        if mysql_charset is not None:
            self._values["mysql_charset"] = mysql_charset
        if mysql_collation is not None:
            self._values["mysql_collation"] = mysql_collation
        if mysql_password is not None:
            self._values["mysql_password"] = mysql_password
        if mysql_port is not None:
            self._values["mysql_port"] = mysql_port
        if mysql_username is not None:
            self._values["mysql_username"] = mysql_username
        if snapshot_name is not None:
            self._values["snapshot_name"] = snapshot_name
        if source_service_name is not None:
            self._values["source_service_name"] = source_service_name

    @builtins.property
    def db_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#db_name MysqlServiceInstance#db_name}.'''
        result = self._values.get("db_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_storage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#db_storage MysqlServiceInstance#db_storage}.'''
        result = self._values.get("db_storage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enterprise_monitor_configuration(
        self,
    ) -> typing.Optional["MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration"]:
        '''enterprise_monitor_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#enterprise_monitor_configuration MysqlServiceInstance#enterprise_monitor_configuration}
        '''
        result = self._values.get("enterprise_monitor_configuration")
        return typing.cast(typing.Optional["MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration"], result)

    @builtins.property
    def mysql_charset(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_charset MysqlServiceInstance#mysql_charset}.'''
        result = self._values.get("mysql_charset")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mysql_collation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_collation MysqlServiceInstance#mysql_collation}.'''
        result = self._values.get("mysql_collation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mysql_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_password MysqlServiceInstance#mysql_password}.'''
        result = self._values.get("mysql_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mysql_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_port MysqlServiceInstance#mysql_port}.'''
        result = self._values.get("mysql_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def mysql_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_username MysqlServiceInstance#mysql_username}.'''
        result = self._values.get("mysql_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#snapshot_name MysqlServiceInstance#snapshot_name}.'''
        result = self._values.get("snapshot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_service_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#source_service_name MysqlServiceInstance#source_service_name}.'''
        result = self._values.get("source_service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MysqlServiceInstanceMysqlConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "em_agent_password": "emAgentPassword",
        "em_agent_username": "emAgentUsername",
        "em_password": "emPassword",
        "em_port": "emPort",
        "em_username": "emUsername",
    },
)
class MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration:
    def __init__(
        self,
        *,
        em_agent_password: typing.Optional[builtins.str] = None,
        em_agent_username: typing.Optional[builtins.str] = None,
        em_password: typing.Optional[builtins.str] = None,
        em_port: typing.Optional[jsii.Number] = None,
        em_username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param em_agent_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_agent_password MysqlServiceInstance#em_agent_password}.
        :param em_agent_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_agent_username MysqlServiceInstance#em_agent_username}.
        :param em_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_password MysqlServiceInstance#em_password}.
        :param em_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_port MysqlServiceInstance#em_port}.
        :param em_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_username MysqlServiceInstance#em_username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration.__init__)
            check_type(argname="argument em_agent_password", value=em_agent_password, expected_type=type_hints["em_agent_password"])
            check_type(argname="argument em_agent_username", value=em_agent_username, expected_type=type_hints["em_agent_username"])
            check_type(argname="argument em_password", value=em_password, expected_type=type_hints["em_password"])
            check_type(argname="argument em_port", value=em_port, expected_type=type_hints["em_port"])
            check_type(argname="argument em_username", value=em_username, expected_type=type_hints["em_username"])
        self._values: typing.Dict[str, typing.Any] = {}
        if em_agent_password is not None:
            self._values["em_agent_password"] = em_agent_password
        if em_agent_username is not None:
            self._values["em_agent_username"] = em_agent_username
        if em_password is not None:
            self._values["em_password"] = em_password
        if em_port is not None:
            self._values["em_port"] = em_port
        if em_username is not None:
            self._values["em_username"] = em_username

    @builtins.property
    def em_agent_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_agent_password MysqlServiceInstance#em_agent_password}.'''
        result = self._values.get("em_agent_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def em_agent_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_agent_username MysqlServiceInstance#em_agent_username}.'''
        result = self._values.get("em_agent_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def em_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_password MysqlServiceInstance#em_password}.'''
        result = self._values.get("em_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def em_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_port MysqlServiceInstance#em_port}.'''
        result = self._values.get("em_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def em_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_username MysqlServiceInstance#em_username}.'''
        result = self._values.get("em_username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEmAgentPassword")
    def reset_em_agent_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmAgentPassword", []))

    @jsii.member(jsii_name="resetEmAgentUsername")
    def reset_em_agent_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmAgentUsername", []))

    @jsii.member(jsii_name="resetEmPassword")
    def reset_em_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmPassword", []))

    @jsii.member(jsii_name="resetEmPort")
    def reset_em_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmPort", []))

    @jsii.member(jsii_name="resetEmUsername")
    def reset_em_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmUsername", []))

    @builtins.property
    @jsii.member(jsii_name="emAgentPasswordInput")
    def em_agent_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emAgentPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="emAgentUsernameInput")
    def em_agent_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emAgentUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="emPasswordInput")
    def em_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="emPortInput")
    def em_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "emPortInput"))

    @builtins.property
    @jsii.member(jsii_name="emUsernameInput")
    def em_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="emAgentPassword")
    def em_agent_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emAgentPassword"))

    @em_agent_password.setter
    def em_agent_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfigurationOutputReference, "em_agent_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emAgentPassword", value)

    @builtins.property
    @jsii.member(jsii_name="emAgentUsername")
    def em_agent_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emAgentUsername"))

    @em_agent_username.setter
    def em_agent_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfigurationOutputReference, "em_agent_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emAgentUsername", value)

    @builtins.property
    @jsii.member(jsii_name="emPassword")
    def em_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emPassword"))

    @em_password.setter
    def em_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfigurationOutputReference, "em_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emPassword", value)

    @builtins.property
    @jsii.member(jsii_name="emPort")
    def em_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "emPort"))

    @em_port.setter
    def em_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfigurationOutputReference, "em_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emPort", value)

    @builtins.property
    @jsii.member(jsii_name="emUsername")
    def em_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emUsername"))

    @em_username.setter
    def em_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfigurationOutputReference, "em_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emUsername", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration]:
        return typing.cast(typing.Optional[MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MysqlServiceInstanceMysqlConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstanceMysqlConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(MysqlServiceInstanceMysqlConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEnterpriseMonitorConfiguration")
    def put_enterprise_monitor_configuration(
        self,
        *,
        em_agent_password: typing.Optional[builtins.str] = None,
        em_agent_username: typing.Optional[builtins.str] = None,
        em_password: typing.Optional[builtins.str] = None,
        em_port: typing.Optional[jsii.Number] = None,
        em_username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param em_agent_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_agent_password MysqlServiceInstance#em_agent_password}.
        :param em_agent_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_agent_username MysqlServiceInstance#em_agent_username}.
        :param em_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_password MysqlServiceInstance#em_password}.
        :param em_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_port MysqlServiceInstance#em_port}.
        :param em_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_username MysqlServiceInstance#em_username}.
        '''
        value = MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration(
            em_agent_password=em_agent_password,
            em_agent_username=em_agent_username,
            em_password=em_password,
            em_port=em_port,
            em_username=em_username,
        )

        return typing.cast(None, jsii.invoke(self, "putEnterpriseMonitorConfiguration", [value]))

    @jsii.member(jsii_name="resetDbName")
    def reset_db_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbName", []))

    @jsii.member(jsii_name="resetDbStorage")
    def reset_db_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbStorage", []))

    @jsii.member(jsii_name="resetEnterpriseMonitorConfiguration")
    def reset_enterprise_monitor_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnterpriseMonitorConfiguration", []))

    @jsii.member(jsii_name="resetMysqlCharset")
    def reset_mysql_charset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlCharset", []))

    @jsii.member(jsii_name="resetMysqlCollation")
    def reset_mysql_collation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlCollation", []))

    @jsii.member(jsii_name="resetMysqlPassword")
    def reset_mysql_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlPassword", []))

    @jsii.member(jsii_name="resetMysqlPort")
    def reset_mysql_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlPort", []))

    @jsii.member(jsii_name="resetMysqlUsername")
    def reset_mysql_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlUsername", []))

    @jsii.member(jsii_name="resetSnapshotName")
    def reset_snapshot_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotName", []))

    @jsii.member(jsii_name="resetSourceServiceName")
    def reset_source_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceServiceName", []))

    @builtins.property
    @jsii.member(jsii_name="connectString")
    def connect_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectString"))

    @builtins.property
    @jsii.member(jsii_name="enterpriseMonitorConfiguration")
    def enterprise_monitor_configuration(
        self,
    ) -> MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfigurationOutputReference:
        return typing.cast(MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfigurationOutputReference, jsii.get(self, "enterpriseMonitorConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddress")
    def public_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="dbNameInput")
    def db_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dbStorageInput")
    def db_storage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dbStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="enterpriseMonitorConfigurationInput")
    def enterprise_monitor_configuration_input(
        self,
    ) -> typing.Optional[MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration]:
        return typing.cast(typing.Optional[MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration], jsii.get(self, "enterpriseMonitorConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlCharsetInput")
    def mysql_charset_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mysqlCharsetInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlCollationInput")
    def mysql_collation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mysqlCollationInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlPasswordInput")
    def mysql_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mysqlPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlPortInput")
    def mysql_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mysqlPortInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlUsernameInput")
    def mysql_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mysqlUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotNameInput")
    def snapshot_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceServiceNameInput")
    def source_service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceServiceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dbName")
    def db_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbName"))

    @db_name.setter
    def db_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceMysqlConfigurationOutputReference, "db_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbName", value)

    @builtins.property
    @jsii.member(jsii_name="dbStorage")
    def db_storage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dbStorage"))

    @db_storage.setter
    def db_storage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceMysqlConfigurationOutputReference, "db_storage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbStorage", value)

    @builtins.property
    @jsii.member(jsii_name="mysqlCharset")
    def mysql_charset(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mysqlCharset"))

    @mysql_charset.setter
    def mysql_charset(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceMysqlConfigurationOutputReference, "mysql_charset").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mysqlCharset", value)

    @builtins.property
    @jsii.member(jsii_name="mysqlCollation")
    def mysql_collation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mysqlCollation"))

    @mysql_collation.setter
    def mysql_collation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceMysqlConfigurationOutputReference, "mysql_collation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mysqlCollation", value)

    @builtins.property
    @jsii.member(jsii_name="mysqlPassword")
    def mysql_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mysqlPassword"))

    @mysql_password.setter
    def mysql_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceMysqlConfigurationOutputReference, "mysql_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mysqlPassword", value)

    @builtins.property
    @jsii.member(jsii_name="mysqlPort")
    def mysql_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mysqlPort"))

    @mysql_port.setter
    def mysql_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceMysqlConfigurationOutputReference, "mysql_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mysqlPort", value)

    @builtins.property
    @jsii.member(jsii_name="mysqlUsername")
    def mysql_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mysqlUsername"))

    @mysql_username.setter
    def mysql_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceMysqlConfigurationOutputReference, "mysql_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mysqlUsername", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotName")
    def snapshot_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotName"))

    @snapshot_name.setter
    def snapshot_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceMysqlConfigurationOutputReference, "snapshot_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotName", value)

    @builtins.property
    @jsii.member(jsii_name="sourceServiceName")
    def source_service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceServiceName"))

    @source_service_name.setter
    def source_service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceMysqlConfigurationOutputReference, "source_service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MysqlServiceInstanceMysqlConfiguration]:
        return typing.cast(typing.Optional[MysqlServiceInstanceMysqlConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MysqlServiceInstanceMysqlConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceMysqlConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstanceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class MysqlServiceInstanceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#create MysqlServiceInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#delete MysqlServiceInstance#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MysqlServiceInstanceTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#create MysqlServiceInstance#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#delete MysqlServiceInstance#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MysqlServiceInstanceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MysqlServiceInstanceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstanceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MysqlServiceInstanceTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MysqlServiceInstanceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MysqlServiceInstanceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MysqlServiceInstanceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MysqlServiceInstanceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MysqlServiceInstance",
    "MysqlServiceInstanceBackups",
    "MysqlServiceInstanceBackupsOutputReference",
    "MysqlServiceInstanceConfig",
    "MysqlServiceInstanceMysqlConfiguration",
    "MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration",
    "MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfigurationOutputReference",
    "MysqlServiceInstanceMysqlConfigurationOutputReference",
    "MysqlServiceInstanceTimeouts",
    "MysqlServiceInstanceTimeoutsOutputReference",
]

publication.publish()
