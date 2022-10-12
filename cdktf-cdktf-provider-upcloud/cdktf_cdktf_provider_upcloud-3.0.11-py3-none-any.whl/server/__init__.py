'''
# `upcloud_server`

Refer to the Terraform Registory for docs: [`upcloud_server`](https://www.terraform.io/docs/providers/upcloud/r/server).
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


class Server(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.server.Server",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/upcloud/r/server upcloud_server}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        hostname: builtins.str,
        network_interface: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServerNetworkInterface", typing.Dict[str, typing.Any]]]],
        zone: builtins.str,
        cpu: typing.Optional[jsii.Number] = None,
        firewall: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        host: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        login: typing.Optional[typing.Union["ServerLogin", typing.Dict[str, typing.Any]]] = None,
        mem: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        plan: typing.Optional[builtins.str] = None,
        simple_backup: typing.Optional[typing.Union["ServerSimpleBackup", typing.Dict[str, typing.Any]]] = None,
        storage_devices: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServerStorageDevices", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        template: typing.Optional[typing.Union["ServerTemplate", typing.Dict[str, typing.Any]]] = None,
        title: typing.Optional[builtins.str] = None,
        user_data: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/upcloud/r/server upcloud_server} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param hostname: A valid domain name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#hostname Server#hostname}
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#network_interface Server#network_interface}
        :param zone: The zone in which the server will be hosted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#zone Server#zone}
        :param cpu: The number of CPU for the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#cpu Server#cpu}
        :param firewall: Are firewall rules active for the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#firewall Server#firewall}
        :param host: Use this to start the VM on a specific host. Refers to value from host -attribute. Only available for private cloud hosts Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#host Server#host}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#id Server#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param login: login block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#login Server#login}
        :param mem: The size of memory for the server (in megabytes). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#mem Server#mem}
        :param metadata: Is the metadata service active for the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#metadata Server#metadata}
        :param plan: The pricing plan used for the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#plan Server#plan}
        :param simple_backup: simple_backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#simple_backup Server#simple_backup}
        :param storage_devices: storage_devices block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#storage_devices Server#storage_devices}
        :param tags: The server related tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#tags Server#tags}
        :param template: template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#template Server#template}
        :param title: A short, informational description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#title Server#title}
        :param user_data: Defines URL for a server setup script, or the script body itself. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#user_data Server#user_data}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Server.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ServerConfig(
            hostname=hostname,
            network_interface=network_interface,
            zone=zone,
            cpu=cpu,
            firewall=firewall,
            host=host,
            id=id,
            login=login,
            mem=mem,
            metadata=metadata,
            plan=plan,
            simple_backup=simple_backup,
            storage_devices=storage_devices,
            tags=tags,
            template=template,
            title=title,
            user_data=user_data,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putLogin")
    def put_login(
        self,
        *,
        create_password: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        password_delivery: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create_password: Indicates a password should be create to allow access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#create_password Server#create_password}
        :param keys: A list of ssh keys to access the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#keys Server#keys}
        :param password_delivery: The delivery method for the server’s root password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#password_delivery Server#password_delivery}
        :param user: Username to be create to access the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#user Server#user}
        '''
        value = ServerLogin(
            create_password=create_password,
            keys=keys,
            password_delivery=password_delivery,
            user=user,
        )

        return typing.cast(None, jsii.invoke(self, "putLogin", [value]))

    @jsii.member(jsii_name="putNetworkInterface")
    def put_network_interface(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServerNetworkInterface", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Server.put_network_interface)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkInterface", [value]))

    @jsii.member(jsii_name="putSimpleBackup")
    def put_simple_backup(self, *, plan: builtins.str, time: builtins.str) -> None:
        '''
        :param plan: Simple backup plan. Accepted values: dailies, weeklies, monthlies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#plan Server#plan}
        :param time: Time of the day at which backup will be taken. Should be provided in a hhmm format (e.g. 2230). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#time Server#time}
        '''
        value = ServerSimpleBackup(plan=plan, time=time)

        return typing.cast(None, jsii.invoke(self, "putSimpleBackup", [value]))

    @jsii.member(jsii_name="putStorageDevices")
    def put_storage_devices(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServerStorageDevices", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Server.put_storage_devices)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStorageDevices", [value]))

    @jsii.member(jsii_name="putTemplate")
    def put_template(
        self,
        *,
        storage: builtins.str,
        address: typing.Optional[builtins.str] = None,
        backup_rule: typing.Optional[typing.Union["ServerTemplateBackupRule", typing.Dict[str, typing.Any]]] = None,
        delete_autoresize_backup: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        filesystem_autoresize: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        size: typing.Optional[jsii.Number] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param storage: A valid storage UUID or template name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#storage Server#storage}
        :param address: The device address the storage will be attached to. Specify only the bus name (ide/scsi/virtio) to auto-select next available address from that bus. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#address Server#address}
        :param backup_rule: backup_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#backup_rule Server#backup_rule}
        :param delete_autoresize_backup: If set to true, the backup taken before the partition and filesystem resize attempt will be deleted immediately after success. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#delete_autoresize_backup Server#delete_autoresize_backup}
        :param filesystem_autoresize: If set to true, provider will attempt to resize partition and filesystem when the size of template storage changes. Please note that before the resize attempt is made, backup of the storage will be taken. If the resize attempt fails, the backup will be used to restore the storage and then deleted. If the resize attempt succeeds, backup will be kept (unless delete_autoresize_backup option is set to true). Taking and keeping backups incure costs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#filesystem_autoresize Server#filesystem_autoresize}
        :param size: The size of the storage in gigabytes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#size Server#size}
        :param title: A short, informative description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#title Server#title}
        '''
        value = ServerTemplate(
            storage=storage,
            address=address,
            backup_rule=backup_rule,
            delete_autoresize_backup=delete_autoresize_backup,
            filesystem_autoresize=filesystem_autoresize,
            size=size,
            title=title,
        )

        return typing.cast(None, jsii.invoke(self, "putTemplate", [value]))

    @jsii.member(jsii_name="resetCpu")
    def reset_cpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpu", []))

    @jsii.member(jsii_name="resetFirewall")
    def reset_firewall(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirewall", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogin")
    def reset_login(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogin", []))

    @jsii.member(jsii_name="resetMem")
    def reset_mem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMem", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetPlan")
    def reset_plan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlan", []))

    @jsii.member(jsii_name="resetSimpleBackup")
    def reset_simple_backup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSimpleBackup", []))

    @jsii.member(jsii_name="resetStorageDevices")
    def reset_storage_devices(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageDevices", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTemplate")
    def reset_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplate", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @jsii.member(jsii_name="resetUserData")
    def reset_user_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserData", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="login")
    def login(self) -> "ServerLoginOutputReference":
        return typing.cast("ServerLoginOutputReference", jsii.get(self, "login"))

    @builtins.property
    @jsii.member(jsii_name="networkInterface")
    def network_interface(self) -> "ServerNetworkInterfaceList":
        return typing.cast("ServerNetworkInterfaceList", jsii.get(self, "networkInterface"))

    @builtins.property
    @jsii.member(jsii_name="simpleBackup")
    def simple_backup(self) -> "ServerSimpleBackupOutputReference":
        return typing.cast("ServerSimpleBackupOutputReference", jsii.get(self, "simpleBackup"))

    @builtins.property
    @jsii.member(jsii_name="storageDevices")
    def storage_devices(self) -> "ServerStorageDevicesList":
        return typing.cast("ServerStorageDevicesList", jsii.get(self, "storageDevices"))

    @builtins.property
    @jsii.member(jsii_name="template")
    def template(self) -> "ServerTemplateOutputReference":
        return typing.cast("ServerTemplateOutputReference", jsii.get(self, "template"))

    @builtins.property
    @jsii.member(jsii_name="cpuInput")
    def cpu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallInput")
    def firewall_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "firewallInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="loginInput")
    def login_input(self) -> typing.Optional["ServerLogin"]:
        return typing.cast(typing.Optional["ServerLogin"], jsii.get(self, "loginInput"))

    @builtins.property
    @jsii.member(jsii_name="memInput")
    def mem_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceInput")
    def network_interface_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServerNetworkInterface"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServerNetworkInterface"]]], jsii.get(self, "networkInterfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "planInput"))

    @builtins.property
    @jsii.member(jsii_name="simpleBackupInput")
    def simple_backup_input(self) -> typing.Optional["ServerSimpleBackup"]:
        return typing.cast(typing.Optional["ServerSimpleBackup"], jsii.get(self, "simpleBackupInput"))

    @builtins.property
    @jsii.member(jsii_name="storageDevicesInput")
    def storage_devices_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServerStorageDevices"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServerStorageDevices"]]], jsii.get(self, "storageDevicesInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="templateInput")
    def template_input(self) -> typing.Optional["ServerTemplate"]:
        return typing.cast(typing.Optional["ServerTemplate"], jsii.get(self, "templateInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="userDataInput")
    def user_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userDataInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpu"))

    @cpu.setter
    def cpu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Server, "cpu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpu", value)

    @builtins.property
    @jsii.member(jsii_name="firewall")
    def firewall(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "firewall"))

    @firewall.setter
    def firewall(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Server, "firewall").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewall", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "host"))

    @host.setter
    def host(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Server, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Server, "hostname").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Server, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mem")
    def mem(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mem"))

    @mem.setter
    def mem(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Server, "mem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mem", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Server, "metadata").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "plan"))

    @plan.setter
    def plan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Server, "plan").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "plan", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Server, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Server, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userData"))

    @user_data.setter
    def user_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Server, "user_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userData", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Server, "zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.server.ServerConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "hostname": "hostname",
        "network_interface": "networkInterface",
        "zone": "zone",
        "cpu": "cpu",
        "firewall": "firewall",
        "host": "host",
        "id": "id",
        "login": "login",
        "mem": "mem",
        "metadata": "metadata",
        "plan": "plan",
        "simple_backup": "simpleBackup",
        "storage_devices": "storageDevices",
        "tags": "tags",
        "template": "template",
        "title": "title",
        "user_data": "userData",
    },
)
class ServerConfig(cdktf.TerraformMetaArguments):
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
        hostname: builtins.str,
        network_interface: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServerNetworkInterface", typing.Dict[str, typing.Any]]]],
        zone: builtins.str,
        cpu: typing.Optional[jsii.Number] = None,
        firewall: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        host: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        login: typing.Optional[typing.Union["ServerLogin", typing.Dict[str, typing.Any]]] = None,
        mem: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        plan: typing.Optional[builtins.str] = None,
        simple_backup: typing.Optional[typing.Union["ServerSimpleBackup", typing.Dict[str, typing.Any]]] = None,
        storage_devices: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServerStorageDevices", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        template: typing.Optional[typing.Union["ServerTemplate", typing.Dict[str, typing.Any]]] = None,
        title: typing.Optional[builtins.str] = None,
        user_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param hostname: A valid domain name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#hostname Server#hostname}
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#network_interface Server#network_interface}
        :param zone: The zone in which the server will be hosted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#zone Server#zone}
        :param cpu: The number of CPU for the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#cpu Server#cpu}
        :param firewall: Are firewall rules active for the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#firewall Server#firewall}
        :param host: Use this to start the VM on a specific host. Refers to value from host -attribute. Only available for private cloud hosts Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#host Server#host}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#id Server#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param login: login block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#login Server#login}
        :param mem: The size of memory for the server (in megabytes). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#mem Server#mem}
        :param metadata: Is the metadata service active for the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#metadata Server#metadata}
        :param plan: The pricing plan used for the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#plan Server#plan}
        :param simple_backup: simple_backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#simple_backup Server#simple_backup}
        :param storage_devices: storage_devices block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#storage_devices Server#storage_devices}
        :param tags: The server related tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#tags Server#tags}
        :param template: template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#template Server#template}
        :param title: A short, informational description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#title Server#title}
        :param user_data: Defines URL for a server setup script, or the script body itself. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#user_data Server#user_data}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(login, dict):
            login = ServerLogin(**login)
        if isinstance(simple_backup, dict):
            simple_backup = ServerSimpleBackup(**simple_backup)
        if isinstance(template, dict):
            template = ServerTemplate(**template)
        if __debug__:
            type_hints = typing.get_type_hints(ServerConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument network_interface", value=network_interface, expected_type=type_hints["network_interface"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument firewall", value=firewall, expected_type=type_hints["firewall"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument login", value=login, expected_type=type_hints["login"])
            check_type(argname="argument mem", value=mem, expected_type=type_hints["mem"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument plan", value=plan, expected_type=type_hints["plan"])
            check_type(argname="argument simple_backup", value=simple_backup, expected_type=type_hints["simple_backup"])
            check_type(argname="argument storage_devices", value=storage_devices, expected_type=type_hints["storage_devices"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
        self._values: typing.Dict[str, typing.Any] = {
            "hostname": hostname,
            "network_interface": network_interface,
            "zone": zone,
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
        if cpu is not None:
            self._values["cpu"] = cpu
        if firewall is not None:
            self._values["firewall"] = firewall
        if host is not None:
            self._values["host"] = host
        if id is not None:
            self._values["id"] = id
        if login is not None:
            self._values["login"] = login
        if mem is not None:
            self._values["mem"] = mem
        if metadata is not None:
            self._values["metadata"] = metadata
        if plan is not None:
            self._values["plan"] = plan
        if simple_backup is not None:
            self._values["simple_backup"] = simple_backup
        if storage_devices is not None:
            self._values["storage_devices"] = storage_devices
        if tags is not None:
            self._values["tags"] = tags
        if template is not None:
            self._values["template"] = template
        if title is not None:
            self._values["title"] = title
        if user_data is not None:
            self._values["user_data"] = user_data

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
    def hostname(self) -> builtins.str:
        '''A valid domain name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#hostname Server#hostname}
        '''
        result = self._values.get("hostname")
        assert result is not None, "Required property 'hostname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_interface(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ServerNetworkInterface"]]:
        '''network_interface block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#network_interface Server#network_interface}
        '''
        result = self._values.get("network_interface")
        assert result is not None, "Required property 'network_interface' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ServerNetworkInterface"]], result)

    @builtins.property
    def zone(self) -> builtins.str:
        '''The zone in which the server will be hosted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#zone Server#zone}
        '''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cpu(self) -> typing.Optional[jsii.Number]:
        '''The number of CPU for the server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#cpu Server#cpu}
        '''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def firewall(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Are firewall rules active for the server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#firewall Server#firewall}
        '''
        result = self._values.get("firewall")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def host(self) -> typing.Optional[jsii.Number]:
        '''Use this to start the VM on a specific host.

        Refers to value from host -attribute. Only available for private cloud hosts

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#host Server#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#id Server#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def login(self) -> typing.Optional["ServerLogin"]:
        '''login block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#login Server#login}
        '''
        result = self._values.get("login")
        return typing.cast(typing.Optional["ServerLogin"], result)

    @builtins.property
    def mem(self) -> typing.Optional[jsii.Number]:
        '''The size of memory for the server (in megabytes).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#mem Server#mem}
        '''
        result = self._values.get("mem")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metadata(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Is the metadata service active for the server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#metadata Server#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def plan(self) -> typing.Optional[builtins.str]:
        '''The pricing plan used for the server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#plan Server#plan}
        '''
        result = self._values.get("plan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def simple_backup(self) -> typing.Optional["ServerSimpleBackup"]:
        '''simple_backup block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#simple_backup Server#simple_backup}
        '''
        result = self._values.get("simple_backup")
        return typing.cast(typing.Optional["ServerSimpleBackup"], result)

    @builtins.property
    def storage_devices(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServerStorageDevices"]]]:
        '''storage_devices block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#storage_devices Server#storage_devices}
        '''
        result = self._values.get("storage_devices")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServerStorageDevices"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The server related tags.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#tags Server#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def template(self) -> typing.Optional["ServerTemplate"]:
        '''template block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#template Server#template}
        '''
        result = self._values.get("template")
        return typing.cast(typing.Optional["ServerTemplate"], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''A short, informational description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#title Server#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''Defines URL for a server setup script, or the script body itself.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#user_data Server#user_data}
        '''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.server.ServerLogin",
    jsii_struct_bases=[],
    name_mapping={
        "create_password": "createPassword",
        "keys": "keys",
        "password_delivery": "passwordDelivery",
        "user": "user",
    },
)
class ServerLogin:
    def __init__(
        self,
        *,
        create_password: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        password_delivery: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create_password: Indicates a password should be create to allow access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#create_password Server#create_password}
        :param keys: A list of ssh keys to access the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#keys Server#keys}
        :param password_delivery: The delivery method for the server’s root password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#password_delivery Server#password_delivery}
        :param user: Username to be create to access the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#user Server#user}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServerLogin.__init__)
            check_type(argname="argument create_password", value=create_password, expected_type=type_hints["create_password"])
            check_type(argname="argument keys", value=keys, expected_type=type_hints["keys"])
            check_type(argname="argument password_delivery", value=password_delivery, expected_type=type_hints["password_delivery"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create_password is not None:
            self._values["create_password"] = create_password
        if keys is not None:
            self._values["keys"] = keys
        if password_delivery is not None:
            self._values["password_delivery"] = password_delivery
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def create_password(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates a password should be create to allow access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#create_password Server#create_password}
        '''
        result = self._values.get("create_password")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of ssh keys to access the server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#keys Server#keys}
        '''
        result = self._values.get("keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def password_delivery(self) -> typing.Optional[builtins.str]:
        '''The delivery method for the server’s root password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#password_delivery Server#password_delivery}
        '''
        result = self._values.get("password_delivery")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''Username to be create to access the server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#user Server#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerLogin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServerLoginOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.server.ServerLoginOutputReference",
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
            type_hints = typing.get_type_hints(ServerLoginOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreatePassword")
    def reset_create_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreatePassword", []))

    @jsii.member(jsii_name="resetKeys")
    def reset_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeys", []))

    @jsii.member(jsii_name="resetPasswordDelivery")
    def reset_password_delivery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordDelivery", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @builtins.property
    @jsii.member(jsii_name="createPasswordInput")
    def create_password_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "createPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="keysInput")
    def keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "keysInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordDeliveryInput")
    def password_delivery_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordDeliveryInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="createPassword")
    def create_password(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "createPassword"))

    @create_password.setter
    def create_password(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerLoginOutputReference, "create_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createPassword", value)

    @builtins.property
    @jsii.member(jsii_name="keys")
    def keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "keys"))

    @keys.setter
    def keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerLoginOutputReference, "keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keys", value)

    @builtins.property
    @jsii.member(jsii_name="passwordDelivery")
    def password_delivery(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passwordDelivery"))

    @password_delivery.setter
    def password_delivery(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerLoginOutputReference, "password_delivery").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordDelivery", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerLoginOutputReference, "user").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServerLogin]:
        return typing.cast(typing.Optional[ServerLogin], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServerLogin]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerLoginOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.server.ServerNetworkInterface",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "bootable": "bootable",
        "ip_address": "ipAddress",
        "ip_address_family": "ipAddressFamily",
        "network": "network",
        "source_ip_filtering": "sourceIpFiltering",
    },
)
class ServerNetworkInterface:
    def __init__(
        self,
        *,
        type: builtins.str,
        bootable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ip_address: typing.Optional[builtins.str] = None,
        ip_address_family: typing.Optional[builtins.str] = None,
        network: typing.Optional[builtins.str] = None,
        source_ip_filtering: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param type: Network interface type. For private network interfaces, a network must be specified with an existing network id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#type Server#type}
        :param bootable: ``true`` if this interface should be used for network booting. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#bootable Server#bootable}
        :param ip_address: The assigned IP address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#ip_address Server#ip_address}
        :param ip_address_family: The IP address type of this interface (one of ``IPv4`` or ``IPv6``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#ip_address_family Server#ip_address_family}
        :param network: The unique ID of a network to attach this network to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#network Server#network}
        :param source_ip_filtering: ``true`` if source IP should be filtered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#source_ip_filtering Server#source_ip_filtering}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServerNetworkInterface.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument bootable", value=bootable, expected_type=type_hints["bootable"])
            check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
            check_type(argname="argument ip_address_family", value=ip_address_family, expected_type=type_hints["ip_address_family"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument source_ip_filtering", value=source_ip_filtering, expected_type=type_hints["source_ip_filtering"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if bootable is not None:
            self._values["bootable"] = bootable
        if ip_address is not None:
            self._values["ip_address"] = ip_address
        if ip_address_family is not None:
            self._values["ip_address_family"] = ip_address_family
        if network is not None:
            self._values["network"] = network
        if source_ip_filtering is not None:
            self._values["source_ip_filtering"] = source_ip_filtering

    @builtins.property
    def type(self) -> builtins.str:
        '''Network interface type. For private network interfaces, a network must be specified with an existing network id.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#type Server#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bootable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''``true`` if this interface should be used for network booting.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#bootable Server#bootable}
        '''
        result = self._values.get("bootable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''The assigned IP address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#ip_address Server#ip_address}
        '''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_address_family(self) -> typing.Optional[builtins.str]:
        '''The IP address type of this interface (one of ``IPv4`` or ``IPv6``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#ip_address_family Server#ip_address_family}
        '''
        result = self._values.get("ip_address_family")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''The unique ID of a network to attach this network to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#network Server#network}
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_ip_filtering(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''``true`` if source IP should be filtered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#source_ip_filtering Server#source_ip_filtering}
        '''
        result = self._values.get("source_ip_filtering")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerNetworkInterface(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServerNetworkInterfaceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.server.ServerNetworkInterfaceList",
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
            type_hints = typing.get_type_hints(ServerNetworkInterfaceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ServerNetworkInterfaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServerNetworkInterfaceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServerNetworkInterfaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerNetworkInterfaceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServerNetworkInterfaceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServerNetworkInterfaceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServerNetworkInterface]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServerNetworkInterface]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServerNetworkInterface]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerNetworkInterfaceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServerNetworkInterfaceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.server.ServerNetworkInterfaceOutputReference",
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
            type_hints = typing.get_type_hints(ServerNetworkInterfaceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBootable")
    def reset_bootable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootable", []))

    @jsii.member(jsii_name="resetIpAddress")
    def reset_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddress", []))

    @jsii.member(jsii_name="resetIpAddressFamily")
    def reset_ip_address_family(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddressFamily", []))

    @jsii.member(jsii_name="resetNetwork")
    def reset_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetwork", []))

    @jsii.member(jsii_name="resetSourceIpFiltering")
    def reset_source_ip_filtering(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceIpFiltering", []))

    @builtins.property
    @jsii.member(jsii_name="ipAddressFloating")
    def ip_address_floating(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "ipAddressFloating"))

    @builtins.property
    @jsii.member(jsii_name="macAddress")
    def mac_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "macAddress"))

    @builtins.property
    @jsii.member(jsii_name="bootableInput")
    def bootable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "bootableInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressFamilyInput")
    def ip_address_family_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressFamilyInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressInput")
    def ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIpFilteringInput")
    def source_ip_filtering_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sourceIpFilteringInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="bootable")
    def bootable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "bootable"))

    @bootable.setter
    def bootable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerNetworkInterfaceOutputReference, "bootable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootable", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @ip_address.setter
    def ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerNetworkInterfaceOutputReference, "ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddress", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddressFamily")
    def ip_address_family(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddressFamily"))

    @ip_address_family.setter
    def ip_address_family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerNetworkInterfaceOutputReference, "ip_address_family").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddressFamily", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerNetworkInterfaceOutputReference, "network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIpFiltering")
    def source_ip_filtering(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sourceIpFiltering"))

    @source_ip_filtering.setter
    def source_ip_filtering(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerNetworkInterfaceOutputReference, "source_ip_filtering").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIpFiltering", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerNetworkInterfaceOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServerNetworkInterface, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServerNetworkInterface, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServerNetworkInterface, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerNetworkInterfaceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.server.ServerSimpleBackup",
    jsii_struct_bases=[],
    name_mapping={"plan": "plan", "time": "time"},
)
class ServerSimpleBackup:
    def __init__(self, *, plan: builtins.str, time: builtins.str) -> None:
        '''
        :param plan: Simple backup plan. Accepted values: dailies, weeklies, monthlies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#plan Server#plan}
        :param time: Time of the day at which backup will be taken. Should be provided in a hhmm format (e.g. 2230). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#time Server#time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServerSimpleBackup.__init__)
            check_type(argname="argument plan", value=plan, expected_type=type_hints["plan"])
            check_type(argname="argument time", value=time, expected_type=type_hints["time"])
        self._values: typing.Dict[str, typing.Any] = {
            "plan": plan,
            "time": time,
        }

    @builtins.property
    def plan(self) -> builtins.str:
        '''Simple backup plan. Accepted values: dailies, weeklies, monthlies.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#plan Server#plan}
        '''
        result = self._values.get("plan")
        assert result is not None, "Required property 'plan' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time(self) -> builtins.str:
        '''Time of the day at which backup will be taken. Should be provided in a hhmm format (e.g. 2230).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#time Server#time}
        '''
        result = self._values.get("time")
        assert result is not None, "Required property 'time' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerSimpleBackup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServerSimpleBackupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.server.ServerSimpleBackupOutputReference",
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
            type_hints = typing.get_type_hints(ServerSimpleBackupOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "planInput"))

    @builtins.property
    @jsii.member(jsii_name="timeInput")
    def time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeInput"))

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "plan"))

    @plan.setter
    def plan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerSimpleBackupOutputReference, "plan").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "plan", value)

    @builtins.property
    @jsii.member(jsii_name="time")
    def time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "time"))

    @time.setter
    def time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerSimpleBackupOutputReference, "time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "time", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServerSimpleBackup]:
        return typing.cast(typing.Optional[ServerSimpleBackup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServerSimpleBackup]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerSimpleBackupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.server.ServerStorageDevices",
    jsii_struct_bases=[],
    name_mapping={"storage": "storage", "address": "address", "type": "type"},
)
class ServerStorageDevices:
    def __init__(
        self,
        *,
        storage: builtins.str,
        address: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param storage: A valid storage UUID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#storage Server#storage}
        :param address: The device address the storage will be attached to. Specify only the bus name (ide/scsi/virtio) to auto-select next available address from that bus. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#address Server#address}
        :param type: The device type the storage will be attached as. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#type Server#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServerStorageDevices.__init__)
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "storage": storage,
        }
        if address is not None:
            self._values["address"] = address
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def storage(self) -> builtins.str:
        '''A valid storage UUID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#storage Server#storage}
        '''
        result = self._values.get("storage")
        assert result is not None, "Required property 'storage' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        '''The device address the storage will be attached to.

        Specify only the bus name (ide/scsi/virtio) to auto-select next available address from that bus.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#address Server#address}
        '''
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The device type the storage will be attached as.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#type Server#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerStorageDevices(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServerStorageDevicesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.server.ServerStorageDevicesList",
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
            type_hints = typing.get_type_hints(ServerStorageDevicesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ServerStorageDevicesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServerStorageDevicesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServerStorageDevicesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerStorageDevicesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServerStorageDevicesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServerStorageDevicesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServerStorageDevices]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServerStorageDevices]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServerStorageDevices]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerStorageDevicesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServerStorageDevicesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.server.ServerStorageDevicesOutputReference",
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
            type_hints = typing.get_type_hints(ServerStorageDevicesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAddress")
    def reset_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddress", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="storageInput")
    def storage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerStorageDevicesOutputReference, "address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="storage")
    def storage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storage"))

    @storage.setter
    def storage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerStorageDevicesOutputReference, "storage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storage", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerStorageDevicesOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServerStorageDevices, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServerStorageDevices, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServerStorageDevices, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerStorageDevicesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.server.ServerTemplate",
    jsii_struct_bases=[],
    name_mapping={
        "storage": "storage",
        "address": "address",
        "backup_rule": "backupRule",
        "delete_autoresize_backup": "deleteAutoresizeBackup",
        "filesystem_autoresize": "filesystemAutoresize",
        "size": "size",
        "title": "title",
    },
)
class ServerTemplate:
    def __init__(
        self,
        *,
        storage: builtins.str,
        address: typing.Optional[builtins.str] = None,
        backup_rule: typing.Optional[typing.Union["ServerTemplateBackupRule", typing.Dict[str, typing.Any]]] = None,
        delete_autoresize_backup: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        filesystem_autoresize: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        size: typing.Optional[jsii.Number] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param storage: A valid storage UUID or template name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#storage Server#storage}
        :param address: The device address the storage will be attached to. Specify only the bus name (ide/scsi/virtio) to auto-select next available address from that bus. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#address Server#address}
        :param backup_rule: backup_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#backup_rule Server#backup_rule}
        :param delete_autoresize_backup: If set to true, the backup taken before the partition and filesystem resize attempt will be deleted immediately after success. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#delete_autoresize_backup Server#delete_autoresize_backup}
        :param filesystem_autoresize: If set to true, provider will attempt to resize partition and filesystem when the size of template storage changes. Please note that before the resize attempt is made, backup of the storage will be taken. If the resize attempt fails, the backup will be used to restore the storage and then deleted. If the resize attempt succeeds, backup will be kept (unless delete_autoresize_backup option is set to true). Taking and keeping backups incure costs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#filesystem_autoresize Server#filesystem_autoresize}
        :param size: The size of the storage in gigabytes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#size Server#size}
        :param title: A short, informative description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#title Server#title}
        '''
        if isinstance(backup_rule, dict):
            backup_rule = ServerTemplateBackupRule(**backup_rule)
        if __debug__:
            type_hints = typing.get_type_hints(ServerTemplate.__init__)
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument backup_rule", value=backup_rule, expected_type=type_hints["backup_rule"])
            check_type(argname="argument delete_autoresize_backup", value=delete_autoresize_backup, expected_type=type_hints["delete_autoresize_backup"])
            check_type(argname="argument filesystem_autoresize", value=filesystem_autoresize, expected_type=type_hints["filesystem_autoresize"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[str, typing.Any] = {
            "storage": storage,
        }
        if address is not None:
            self._values["address"] = address
        if backup_rule is not None:
            self._values["backup_rule"] = backup_rule
        if delete_autoresize_backup is not None:
            self._values["delete_autoresize_backup"] = delete_autoresize_backup
        if filesystem_autoresize is not None:
            self._values["filesystem_autoresize"] = filesystem_autoresize
        if size is not None:
            self._values["size"] = size
        if title is not None:
            self._values["title"] = title

    @builtins.property
    def storage(self) -> builtins.str:
        '''A valid storage UUID or template name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#storage Server#storage}
        '''
        result = self._values.get("storage")
        assert result is not None, "Required property 'storage' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        '''The device address the storage will be attached to.

        Specify only the bus name (ide/scsi/virtio) to auto-select next available address from that bus.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#address Server#address}
        '''
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_rule(self) -> typing.Optional["ServerTemplateBackupRule"]:
        '''backup_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#backup_rule Server#backup_rule}
        '''
        result = self._values.get("backup_rule")
        return typing.cast(typing.Optional["ServerTemplateBackupRule"], result)

    @builtins.property
    def delete_autoresize_backup(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, the backup taken before the partition and filesystem resize attempt will be deleted immediately after success.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#delete_autoresize_backup Server#delete_autoresize_backup}
        '''
        result = self._values.get("delete_autoresize_backup")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def filesystem_autoresize(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, provider will attempt to resize partition and filesystem when the size of template storage changes.

        Please note that before the resize attempt is made, backup of the storage will be taken. If the resize attempt fails, the backup will be used
        to restore the storage and then deleted. If the resize attempt succeeds, backup will be kept (unless delete_autoresize_backup option is set to true).
        Taking and keeping backups incure costs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#filesystem_autoresize Server#filesystem_autoresize}
        '''
        result = self._values.get("filesystem_autoresize")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def size(self) -> typing.Optional[jsii.Number]:
        '''The size of the storage in gigabytes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#size Server#size}
        '''
        result = self._values.get("size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''A short, informative description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#title Server#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.server.ServerTemplateBackupRule",
    jsii_struct_bases=[],
    name_mapping={"interval": "interval", "retention": "retention", "time": "time"},
)
class ServerTemplateBackupRule:
    def __init__(
        self,
        *,
        interval: builtins.str,
        retention: jsii.Number,
        time: builtins.str,
    ) -> None:
        '''
        :param interval: The weekday when the backup is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#interval Server#interval}
        :param retention: The number of days before a backup is automatically deleted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#retention Server#retention}
        :param time: The time of day when the backup is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#time Server#time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServerTemplateBackupRule.__init__)
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument retention", value=retention, expected_type=type_hints["retention"])
            check_type(argname="argument time", value=time, expected_type=type_hints["time"])
        self._values: typing.Dict[str, typing.Any] = {
            "interval": interval,
            "retention": retention,
            "time": time,
        }

    @builtins.property
    def interval(self) -> builtins.str:
        '''The weekday when the backup is created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#interval Server#interval}
        '''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retention(self) -> jsii.Number:
        '''The number of days before a backup is automatically deleted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#retention Server#retention}
        '''
        result = self._values.get("retention")
        assert result is not None, "Required property 'retention' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def time(self) -> builtins.str:
        '''The time of day when the backup is created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#time Server#time}
        '''
        result = self._values.get("time")
        assert result is not None, "Required property 'time' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerTemplateBackupRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServerTemplateBackupRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.server.ServerTemplateBackupRuleOutputReference",
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
            type_hints = typing.get_type_hints(ServerTemplateBackupRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionInput")
    def retention_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeInput")
    def time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeInput"))

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerTemplateBackupRuleOutputReference, "interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="retention")
    def retention(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retention"))

    @retention.setter
    def retention(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerTemplateBackupRuleOutputReference, "retention").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retention", value)

    @builtins.property
    @jsii.member(jsii_name="time")
    def time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "time"))

    @time.setter
    def time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerTemplateBackupRuleOutputReference, "time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "time", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServerTemplateBackupRule]:
        return typing.cast(typing.Optional[ServerTemplateBackupRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServerTemplateBackupRule]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerTemplateBackupRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServerTemplateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.server.ServerTemplateOutputReference",
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
            type_hints = typing.get_type_hints(ServerTemplateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBackupRule")
    def put_backup_rule(
        self,
        *,
        interval: builtins.str,
        retention: jsii.Number,
        time: builtins.str,
    ) -> None:
        '''
        :param interval: The weekday when the backup is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#interval Server#interval}
        :param retention: The number of days before a backup is automatically deleted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#retention Server#retention}
        :param time: The time of day when the backup is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#time Server#time}
        '''
        value = ServerTemplateBackupRule(
            interval=interval, retention=retention, time=time
        )

        return typing.cast(None, jsii.invoke(self, "putBackupRule", [value]))

    @jsii.member(jsii_name="resetAddress")
    def reset_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddress", []))

    @jsii.member(jsii_name="resetBackupRule")
    def reset_backup_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupRule", []))

    @jsii.member(jsii_name="resetDeleteAutoresizeBackup")
    def reset_delete_autoresize_backup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteAutoresizeBackup", []))

    @jsii.member(jsii_name="resetFilesystemAutoresize")
    def reset_filesystem_autoresize(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilesystemAutoresize", []))

    @jsii.member(jsii_name="resetSize")
    def reset_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSize", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @builtins.property
    @jsii.member(jsii_name="backupRule")
    def backup_rule(self) -> ServerTemplateBackupRuleOutputReference:
        return typing.cast(ServerTemplateBackupRuleOutputReference, jsii.get(self, "backupRule"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="backupRuleInput")
    def backup_rule_input(self) -> typing.Optional[ServerTemplateBackupRule]:
        return typing.cast(typing.Optional[ServerTemplateBackupRule], jsii.get(self, "backupRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteAutoresizeBackupInput")
    def delete_autoresize_backup_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deleteAutoresizeBackupInput"))

    @builtins.property
    @jsii.member(jsii_name="filesystemAutoresizeInput")
    def filesystem_autoresize_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "filesystemAutoresizeInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="storageInput")
    def storage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerTemplateOutputReference, "address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="deleteAutoresizeBackup")
    def delete_autoresize_backup(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deleteAutoresizeBackup"))

    @delete_autoresize_backup.setter
    def delete_autoresize_backup(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerTemplateOutputReference, "delete_autoresize_backup").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteAutoresizeBackup", value)

    @builtins.property
    @jsii.member(jsii_name="filesystemAutoresize")
    def filesystem_autoresize(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "filesystemAutoresize"))

    @filesystem_autoresize.setter
    def filesystem_autoresize(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerTemplateOutputReference, "filesystem_autoresize").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filesystemAutoresize", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerTemplateOutputReference, "size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="storage")
    def storage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storage"))

    @storage.setter
    def storage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerTemplateOutputReference, "storage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storage", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerTemplateOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServerTemplate]:
        return typing.cast(typing.Optional[ServerTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServerTemplate]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServerTemplateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Server",
    "ServerConfig",
    "ServerLogin",
    "ServerLoginOutputReference",
    "ServerNetworkInterface",
    "ServerNetworkInterfaceList",
    "ServerNetworkInterfaceOutputReference",
    "ServerSimpleBackup",
    "ServerSimpleBackupOutputReference",
    "ServerStorageDevices",
    "ServerStorageDevicesList",
    "ServerStorageDevicesOutputReference",
    "ServerTemplate",
    "ServerTemplateBackupRule",
    "ServerTemplateBackupRuleOutputReference",
    "ServerTemplateOutputReference",
]

publication.publish()
