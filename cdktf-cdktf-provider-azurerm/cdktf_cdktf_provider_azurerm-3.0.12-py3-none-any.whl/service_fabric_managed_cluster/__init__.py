'''
# `azurerm_service_fabric_managed_cluster`

Refer to the Terraform Registory for docs: [`azurerm_service_fabric_managed_cluster`](https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster).
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


class ServiceFabricManagedCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster azurerm_service_fabric_managed_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        client_connection_port: jsii.Number,
        http_gateway_port: jsii.Number,
        lb_rule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricManagedClusterLbRule", typing.Dict[str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        authentication: typing.Optional[typing.Union["ServiceFabricManagedClusterAuthentication", typing.Dict[str, typing.Any]]] = None,
        backup_service_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_fabric_setting: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricManagedClusterCustomFabricSetting", typing.Dict[str, typing.Any]]]]] = None,
        dns_name: typing.Optional[builtins.str] = None,
        dns_service_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        node_type: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricManagedClusterNodeType", typing.Dict[str, typing.Any]]]]] = None,
        password: typing.Optional[builtins.str] = None,
        sku: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ServiceFabricManagedClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        upgrade_wave: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster azurerm_service_fabric_managed_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param client_connection_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#client_connection_port ServiceFabricManagedCluster#client_connection_port}.
        :param http_gateway_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#http_gateway_port ServiceFabricManagedCluster#http_gateway_port}.
        :param lb_rule: lb_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#lb_rule ServiceFabricManagedCluster#lb_rule}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#location ServiceFabricManagedCluster#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#name ServiceFabricManagedCluster#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#resource_group_name ServiceFabricManagedCluster#resource_group_name}.
        :param authentication: authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#authentication ServiceFabricManagedCluster#authentication}
        :param backup_service_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#backup_service_enabled ServiceFabricManagedCluster#backup_service_enabled}.
        :param custom_fabric_setting: custom_fabric_setting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#custom_fabric_setting ServiceFabricManagedCluster#custom_fabric_setting}
        :param dns_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#dns_name ServiceFabricManagedCluster#dns_name}.
        :param dns_service_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#dns_service_enabled ServiceFabricManagedCluster#dns_service_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#id ServiceFabricManagedCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param node_type: node_type block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#node_type ServiceFabricManagedCluster#node_type}
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#password ServiceFabricManagedCluster#password}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#sku ServiceFabricManagedCluster#sku}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#tags ServiceFabricManagedCluster#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#timeouts ServiceFabricManagedCluster#timeouts}
        :param upgrade_wave: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#upgrade_wave ServiceFabricManagedCluster#upgrade_wave}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#username ServiceFabricManagedCluster#username}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ServiceFabricManagedClusterConfig(
            client_connection_port=client_connection_port,
            http_gateway_port=http_gateway_port,
            lb_rule=lb_rule,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            authentication=authentication,
            backup_service_enabled=backup_service_enabled,
            custom_fabric_setting=custom_fabric_setting,
            dns_name=dns_name,
            dns_service_enabled=dns_service_enabled,
            id=id,
            node_type=node_type,
            password=password,
            sku=sku,
            tags=tags,
            timeouts=timeouts,
            upgrade_wave=upgrade_wave,
            username=username,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAuthentication")
    def put_authentication(
        self,
        *,
        active_directory: typing.Optional[typing.Union["ServiceFabricManagedClusterAuthenticationActiveDirectory", typing.Dict[str, typing.Any]]] = None,
        certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricManagedClusterAuthenticationCertificate", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param active_directory: active_directory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#active_directory ServiceFabricManagedCluster#active_directory}
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#certificate ServiceFabricManagedCluster#certificate}
        '''
        value = ServiceFabricManagedClusterAuthentication(
            active_directory=active_directory, certificate=certificate
        )

        return typing.cast(None, jsii.invoke(self, "putAuthentication", [value]))

    @jsii.member(jsii_name="putCustomFabricSetting")
    def put_custom_fabric_setting(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricManagedClusterCustomFabricSetting", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedCluster.put_custom_fabric_setting)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomFabricSetting", [value]))

    @jsii.member(jsii_name="putLbRule")
    def put_lb_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricManagedClusterLbRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedCluster.put_lb_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLbRule", [value]))

    @jsii.member(jsii_name="putNodeType")
    def put_node_type(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricManagedClusterNodeType", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedCluster.put_node_type)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNodeType", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#create ServiceFabricManagedCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#delete ServiceFabricManagedCluster#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#read ServiceFabricManagedCluster#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#update ServiceFabricManagedCluster#update}.
        '''
        value = ServiceFabricManagedClusterTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAuthentication")
    def reset_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthentication", []))

    @jsii.member(jsii_name="resetBackupServiceEnabled")
    def reset_backup_service_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupServiceEnabled", []))

    @jsii.member(jsii_name="resetCustomFabricSetting")
    def reset_custom_fabric_setting(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomFabricSetting", []))

    @jsii.member(jsii_name="resetDnsName")
    def reset_dns_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsName", []))

    @jsii.member(jsii_name="resetDnsServiceEnabled")
    def reset_dns_service_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsServiceEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNodeType")
    def reset_node_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeType", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetSku")
    def reset_sku(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSku", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUpgradeWave")
    def reset_upgrade_wave(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpgradeWave", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="authentication")
    def authentication(
        self,
    ) -> "ServiceFabricManagedClusterAuthenticationOutputReference":
        return typing.cast("ServiceFabricManagedClusterAuthenticationOutputReference", jsii.get(self, "authentication"))

    @builtins.property
    @jsii.member(jsii_name="customFabricSetting")
    def custom_fabric_setting(
        self,
    ) -> "ServiceFabricManagedClusterCustomFabricSettingList":
        return typing.cast("ServiceFabricManagedClusterCustomFabricSettingList", jsii.get(self, "customFabricSetting"))

    @builtins.property
    @jsii.member(jsii_name="lbRule")
    def lb_rule(self) -> "ServiceFabricManagedClusterLbRuleList":
        return typing.cast("ServiceFabricManagedClusterLbRuleList", jsii.get(self, "lbRule"))

    @builtins.property
    @jsii.member(jsii_name="nodeType")
    def node_type(self) -> "ServiceFabricManagedClusterNodeTypeList":
        return typing.cast("ServiceFabricManagedClusterNodeTypeList", jsii.get(self, "nodeType"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ServiceFabricManagedClusterTimeoutsOutputReference":
        return typing.cast("ServiceFabricManagedClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="authenticationInput")
    def authentication_input(
        self,
    ) -> typing.Optional["ServiceFabricManagedClusterAuthentication"]:
        return typing.cast(typing.Optional["ServiceFabricManagedClusterAuthentication"], jsii.get(self, "authenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="backupServiceEnabledInput")
    def backup_service_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "backupServiceEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="clientConnectionPortInput")
    def client_connection_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "clientConnectionPortInput"))

    @builtins.property
    @jsii.member(jsii_name="customFabricSettingInput")
    def custom_fabric_setting_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterCustomFabricSetting"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterCustomFabricSetting"]]], jsii.get(self, "customFabricSettingInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsNameInput")
    def dns_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsServiceEnabledInput")
    def dns_service_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dnsServiceEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="httpGatewayPortInput")
    def http_gateway_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpGatewayPortInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lbRuleInput")
    def lb_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterLbRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterLbRule"]]], jsii.get(self, "lbRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeTypeInput")
    def node_type_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterNodeType"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterNodeType"]]], jsii.get(self, "nodeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ServiceFabricManagedClusterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ServiceFabricManagedClusterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="upgradeWaveInput")
    def upgrade_wave_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "upgradeWaveInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="backupServiceEnabled")
    def backup_service_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "backupServiceEnabled"))

    @backup_service_enabled.setter
    def backup_service_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedCluster, "backup_service_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupServiceEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="clientConnectionPort")
    def client_connection_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "clientConnectionPort"))

    @client_connection_port.setter
    def client_connection_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedCluster, "client_connection_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientConnectionPort", value)

    @builtins.property
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

    @dns_name.setter
    def dns_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedCluster, "dns_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsName", value)

    @builtins.property
    @jsii.member(jsii_name="dnsServiceEnabled")
    def dns_service_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dnsServiceEnabled"))

    @dns_service_enabled.setter
    def dns_service_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedCluster, "dns_service_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsServiceEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="httpGatewayPort")
    def http_gateway_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpGatewayPort"))

    @http_gateway_port.setter
    def http_gateway_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedCluster, "http_gateway_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpGatewayPort", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedCluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedCluster, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedCluster, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedCluster, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedCluster, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedCluster, "sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedCluster, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="upgradeWave")
    def upgrade_wave(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "upgradeWave"))

    @upgrade_wave.setter
    def upgrade_wave(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedCluster, "upgrade_wave").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upgradeWave", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedCluster, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterAuthentication",
    jsii_struct_bases=[],
    name_mapping={"active_directory": "activeDirectory", "certificate": "certificate"},
)
class ServiceFabricManagedClusterAuthentication:
    def __init__(
        self,
        *,
        active_directory: typing.Optional[typing.Union["ServiceFabricManagedClusterAuthenticationActiveDirectory", typing.Dict[str, typing.Any]]] = None,
        certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricManagedClusterAuthenticationCertificate", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param active_directory: active_directory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#active_directory ServiceFabricManagedCluster#active_directory}
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#certificate ServiceFabricManagedCluster#certificate}
        '''
        if isinstance(active_directory, dict):
            active_directory = ServiceFabricManagedClusterAuthenticationActiveDirectory(**active_directory)
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterAuthentication.__init__)
            check_type(argname="argument active_directory", value=active_directory, expected_type=type_hints["active_directory"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
        self._values: typing.Dict[str, typing.Any] = {}
        if active_directory is not None:
            self._values["active_directory"] = active_directory
        if certificate is not None:
            self._values["certificate"] = certificate

    @builtins.property
    def active_directory(
        self,
    ) -> typing.Optional["ServiceFabricManagedClusterAuthenticationActiveDirectory"]:
        '''active_directory block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#active_directory ServiceFabricManagedCluster#active_directory}
        '''
        result = self._values.get("active_directory")
        return typing.cast(typing.Optional["ServiceFabricManagedClusterAuthenticationActiveDirectory"], result)

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterAuthenticationCertificate"]]]:
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#certificate ServiceFabricManagedCluster#certificate}
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterAuthenticationCertificate"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricManagedClusterAuthentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterAuthenticationActiveDirectory",
    jsii_struct_bases=[],
    name_mapping={
        "client_application_id": "clientApplicationId",
        "cluster_application_id": "clusterApplicationId",
        "tenant_id": "tenantId",
    },
)
class ServiceFabricManagedClusterAuthenticationActiveDirectory:
    def __init__(
        self,
        *,
        client_application_id: builtins.str,
        cluster_application_id: builtins.str,
        tenant_id: builtins.str,
    ) -> None:
        '''
        :param client_application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#client_application_id ServiceFabricManagedCluster#client_application_id}.
        :param cluster_application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#cluster_application_id ServiceFabricManagedCluster#cluster_application_id}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#tenant_id ServiceFabricManagedCluster#tenant_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterAuthenticationActiveDirectory.__init__)
            check_type(argname="argument client_application_id", value=client_application_id, expected_type=type_hints["client_application_id"])
            check_type(argname="argument cluster_application_id", value=cluster_application_id, expected_type=type_hints["cluster_application_id"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_application_id": client_application_id,
            "cluster_application_id": cluster_application_id,
            "tenant_id": tenant_id,
        }

    @builtins.property
    def client_application_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#client_application_id ServiceFabricManagedCluster#client_application_id}.'''
        result = self._values.get("client_application_id")
        assert result is not None, "Required property 'client_application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_application_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#cluster_application_id ServiceFabricManagedCluster#cluster_application_id}.'''
        result = self._values.get("cluster_application_id")
        assert result is not None, "Required property 'cluster_application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tenant_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#tenant_id ServiceFabricManagedCluster#tenant_id}.'''
        result = self._values.get("tenant_id")
        assert result is not None, "Required property 'tenant_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricManagedClusterAuthenticationActiveDirectory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricManagedClusterAuthenticationActiveDirectoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterAuthenticationActiveDirectoryOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterAuthenticationActiveDirectoryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="clientApplicationIdInput")
    def client_application_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientApplicationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterApplicationIdInput")
    def cluster_application_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterApplicationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientApplicationId")
    def client_application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientApplicationId"))

    @client_application_id.setter
    def client_application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterAuthenticationActiveDirectoryOutputReference, "client_application_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientApplicationId", value)

    @builtins.property
    @jsii.member(jsii_name="clusterApplicationId")
    def cluster_application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterApplicationId"))

    @cluster_application_id.setter
    def cluster_application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterAuthenticationActiveDirectoryOutputReference, "cluster_application_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterApplicationId", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterAuthenticationActiveDirectoryOutputReference, "tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceFabricManagedClusterAuthenticationActiveDirectory]:
        return typing.cast(typing.Optional[ServiceFabricManagedClusterAuthenticationActiveDirectory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceFabricManagedClusterAuthenticationActiveDirectory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterAuthenticationActiveDirectoryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterAuthenticationCertificate",
    jsii_struct_bases=[],
    name_mapping={
        "thumbprint": "thumbprint",
        "type": "type",
        "common_name": "commonName",
    },
)
class ServiceFabricManagedClusterAuthenticationCertificate:
    def __init__(
        self,
        *,
        thumbprint: builtins.str,
        type: builtins.str,
        common_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param thumbprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#thumbprint ServiceFabricManagedCluster#thumbprint}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#type ServiceFabricManagedCluster#type}.
        :param common_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#common_name ServiceFabricManagedCluster#common_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterAuthenticationCertificate.__init__)
            check_type(argname="argument thumbprint", value=thumbprint, expected_type=type_hints["thumbprint"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument common_name", value=common_name, expected_type=type_hints["common_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "thumbprint": thumbprint,
            "type": type,
        }
        if common_name is not None:
            self._values["common_name"] = common_name

    @builtins.property
    def thumbprint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#thumbprint ServiceFabricManagedCluster#thumbprint}.'''
        result = self._values.get("thumbprint")
        assert result is not None, "Required property 'thumbprint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#type ServiceFabricManagedCluster#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def common_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#common_name ServiceFabricManagedCluster#common_name}.'''
        result = self._values.get("common_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricManagedClusterAuthenticationCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricManagedClusterAuthenticationCertificateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterAuthenticationCertificateList",
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
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterAuthenticationCertificateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceFabricManagedClusterAuthenticationCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterAuthenticationCertificateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceFabricManagedClusterAuthenticationCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterAuthenticationCertificateList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterAuthenticationCertificateList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterAuthenticationCertificateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterAuthenticationCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterAuthenticationCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterAuthenticationCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterAuthenticationCertificateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricManagedClusterAuthenticationCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterAuthenticationCertificateOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterAuthenticationCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCommonName")
    def reset_common_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommonName", []))

    @builtins.property
    @jsii.member(jsii_name="commonNameInput")
    def common_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commonNameInput"))

    @builtins.property
    @jsii.member(jsii_name="thumbprintInput")
    def thumbprint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thumbprintInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="commonName")
    def common_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commonName"))

    @common_name.setter
    def common_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterAuthenticationCertificateOutputReference, "common_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commonName", value)

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @thumbprint.setter
    def thumbprint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterAuthenticationCertificateOutputReference, "thumbprint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thumbprint", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterAuthenticationCertificateOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceFabricManagedClusterAuthenticationCertificate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceFabricManagedClusterAuthenticationCertificate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceFabricManagedClusterAuthenticationCertificate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterAuthenticationCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricManagedClusterAuthenticationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterAuthenticationOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterAuthenticationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putActiveDirectory")
    def put_active_directory(
        self,
        *,
        client_application_id: builtins.str,
        cluster_application_id: builtins.str,
        tenant_id: builtins.str,
    ) -> None:
        '''
        :param client_application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#client_application_id ServiceFabricManagedCluster#client_application_id}.
        :param cluster_application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#cluster_application_id ServiceFabricManagedCluster#cluster_application_id}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#tenant_id ServiceFabricManagedCluster#tenant_id}.
        '''
        value = ServiceFabricManagedClusterAuthenticationActiveDirectory(
            client_application_id=client_application_id,
            cluster_application_id=cluster_application_id,
            tenant_id=tenant_id,
        )

        return typing.cast(None, jsii.invoke(self, "putActiveDirectory", [value]))

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ServiceFabricManagedClusterAuthenticationCertificate, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterAuthenticationOutputReference.put_certificate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @jsii.member(jsii_name="resetActiveDirectory")
    def reset_active_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActiveDirectory", []))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @builtins.property
    @jsii.member(jsii_name="activeDirectory")
    def active_directory(
        self,
    ) -> ServiceFabricManagedClusterAuthenticationActiveDirectoryOutputReference:
        return typing.cast(ServiceFabricManagedClusterAuthenticationActiveDirectoryOutputReference, jsii.get(self, "activeDirectory"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> ServiceFabricManagedClusterAuthenticationCertificateList:
        return typing.cast(ServiceFabricManagedClusterAuthenticationCertificateList, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryInput")
    def active_directory_input(
        self,
    ) -> typing.Optional[ServiceFabricManagedClusterAuthenticationActiveDirectory]:
        return typing.cast(typing.Optional[ServiceFabricManagedClusterAuthenticationActiveDirectory], jsii.get(self, "activeDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterAuthenticationCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterAuthenticationCertificate]]], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceFabricManagedClusterAuthentication]:
        return typing.cast(typing.Optional[ServiceFabricManagedClusterAuthentication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceFabricManagedClusterAuthentication],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterAuthenticationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "client_connection_port": "clientConnectionPort",
        "http_gateway_port": "httpGatewayPort",
        "lb_rule": "lbRule",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "authentication": "authentication",
        "backup_service_enabled": "backupServiceEnabled",
        "custom_fabric_setting": "customFabricSetting",
        "dns_name": "dnsName",
        "dns_service_enabled": "dnsServiceEnabled",
        "id": "id",
        "node_type": "nodeType",
        "password": "password",
        "sku": "sku",
        "tags": "tags",
        "timeouts": "timeouts",
        "upgrade_wave": "upgradeWave",
        "username": "username",
    },
)
class ServiceFabricManagedClusterConfig(cdktf.TerraformMetaArguments):
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
        client_connection_port: jsii.Number,
        http_gateway_port: jsii.Number,
        lb_rule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricManagedClusterLbRule", typing.Dict[str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        authentication: typing.Optional[typing.Union[ServiceFabricManagedClusterAuthentication, typing.Dict[str, typing.Any]]] = None,
        backup_service_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_fabric_setting: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricManagedClusterCustomFabricSetting", typing.Dict[str, typing.Any]]]]] = None,
        dns_name: typing.Optional[builtins.str] = None,
        dns_service_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        node_type: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricManagedClusterNodeType", typing.Dict[str, typing.Any]]]]] = None,
        password: typing.Optional[builtins.str] = None,
        sku: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ServiceFabricManagedClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        upgrade_wave: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param client_connection_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#client_connection_port ServiceFabricManagedCluster#client_connection_port}.
        :param http_gateway_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#http_gateway_port ServiceFabricManagedCluster#http_gateway_port}.
        :param lb_rule: lb_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#lb_rule ServiceFabricManagedCluster#lb_rule}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#location ServiceFabricManagedCluster#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#name ServiceFabricManagedCluster#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#resource_group_name ServiceFabricManagedCluster#resource_group_name}.
        :param authentication: authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#authentication ServiceFabricManagedCluster#authentication}
        :param backup_service_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#backup_service_enabled ServiceFabricManagedCluster#backup_service_enabled}.
        :param custom_fabric_setting: custom_fabric_setting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#custom_fabric_setting ServiceFabricManagedCluster#custom_fabric_setting}
        :param dns_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#dns_name ServiceFabricManagedCluster#dns_name}.
        :param dns_service_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#dns_service_enabled ServiceFabricManagedCluster#dns_service_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#id ServiceFabricManagedCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param node_type: node_type block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#node_type ServiceFabricManagedCluster#node_type}
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#password ServiceFabricManagedCluster#password}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#sku ServiceFabricManagedCluster#sku}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#tags ServiceFabricManagedCluster#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#timeouts ServiceFabricManagedCluster#timeouts}
        :param upgrade_wave: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#upgrade_wave ServiceFabricManagedCluster#upgrade_wave}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#username ServiceFabricManagedCluster#username}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(authentication, dict):
            authentication = ServiceFabricManagedClusterAuthentication(**authentication)
        if isinstance(timeouts, dict):
            timeouts = ServiceFabricManagedClusterTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument client_connection_port", value=client_connection_port, expected_type=type_hints["client_connection_port"])
            check_type(argname="argument http_gateway_port", value=http_gateway_port, expected_type=type_hints["http_gateway_port"])
            check_type(argname="argument lb_rule", value=lb_rule, expected_type=type_hints["lb_rule"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument authentication", value=authentication, expected_type=type_hints["authentication"])
            check_type(argname="argument backup_service_enabled", value=backup_service_enabled, expected_type=type_hints["backup_service_enabled"])
            check_type(argname="argument custom_fabric_setting", value=custom_fabric_setting, expected_type=type_hints["custom_fabric_setting"])
            check_type(argname="argument dns_name", value=dns_name, expected_type=type_hints["dns_name"])
            check_type(argname="argument dns_service_enabled", value=dns_service_enabled, expected_type=type_hints["dns_service_enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument node_type", value=node_type, expected_type=type_hints["node_type"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument upgrade_wave", value=upgrade_wave, expected_type=type_hints["upgrade_wave"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_connection_port": client_connection_port,
            "http_gateway_port": http_gateway_port,
            "lb_rule": lb_rule,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
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
        if authentication is not None:
            self._values["authentication"] = authentication
        if backup_service_enabled is not None:
            self._values["backup_service_enabled"] = backup_service_enabled
        if custom_fabric_setting is not None:
            self._values["custom_fabric_setting"] = custom_fabric_setting
        if dns_name is not None:
            self._values["dns_name"] = dns_name
        if dns_service_enabled is not None:
            self._values["dns_service_enabled"] = dns_service_enabled
        if id is not None:
            self._values["id"] = id
        if node_type is not None:
            self._values["node_type"] = node_type
        if password is not None:
            self._values["password"] = password
        if sku is not None:
            self._values["sku"] = sku
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if upgrade_wave is not None:
            self._values["upgrade_wave"] = upgrade_wave
        if username is not None:
            self._values["username"] = username

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
    def client_connection_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#client_connection_port ServiceFabricManagedCluster#client_connection_port}.'''
        result = self._values.get("client_connection_port")
        assert result is not None, "Required property 'client_connection_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def http_gateway_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#http_gateway_port ServiceFabricManagedCluster#http_gateway_port}.'''
        result = self._values.get("http_gateway_port")
        assert result is not None, "Required property 'http_gateway_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def lb_rule(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterLbRule"]]:
        '''lb_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#lb_rule ServiceFabricManagedCluster#lb_rule}
        '''
        result = self._values.get("lb_rule")
        assert result is not None, "Required property 'lb_rule' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterLbRule"]], result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#location ServiceFabricManagedCluster#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#name ServiceFabricManagedCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#resource_group_name ServiceFabricManagedCluster#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authentication(
        self,
    ) -> typing.Optional[ServiceFabricManagedClusterAuthentication]:
        '''authentication block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#authentication ServiceFabricManagedCluster#authentication}
        '''
        result = self._values.get("authentication")
        return typing.cast(typing.Optional[ServiceFabricManagedClusterAuthentication], result)

    @builtins.property
    def backup_service_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#backup_service_enabled ServiceFabricManagedCluster#backup_service_enabled}.'''
        result = self._values.get("backup_service_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def custom_fabric_setting(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterCustomFabricSetting"]]]:
        '''custom_fabric_setting block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#custom_fabric_setting ServiceFabricManagedCluster#custom_fabric_setting}
        '''
        result = self._values.get("custom_fabric_setting")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterCustomFabricSetting"]]], result)

    @builtins.property
    def dns_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#dns_name ServiceFabricManagedCluster#dns_name}.'''
        result = self._values.get("dns_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns_service_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#dns_service_enabled ServiceFabricManagedCluster#dns_service_enabled}.'''
        result = self._values.get("dns_service_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#id ServiceFabricManagedCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_type(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterNodeType"]]]:
        '''node_type block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#node_type ServiceFabricManagedCluster#node_type}
        '''
        result = self._values.get("node_type")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterNodeType"]]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#password ServiceFabricManagedCluster#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sku(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#sku ServiceFabricManagedCluster#sku}.'''
        result = self._values.get("sku")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#tags ServiceFabricManagedCluster#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ServiceFabricManagedClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#timeouts ServiceFabricManagedCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ServiceFabricManagedClusterTimeouts"], result)

    @builtins.property
    def upgrade_wave(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#upgrade_wave ServiceFabricManagedCluster#upgrade_wave}.'''
        result = self._values.get("upgrade_wave")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#username ServiceFabricManagedCluster#username}.'''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricManagedClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterCustomFabricSetting",
    jsii_struct_bases=[],
    name_mapping={"parameter": "parameter", "section": "section", "value": "value"},
)
class ServiceFabricManagedClusterCustomFabricSetting:
    def __init__(
        self,
        *,
        parameter: builtins.str,
        section: builtins.str,
        value: builtins.str,
    ) -> None:
        '''
        :param parameter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#parameter ServiceFabricManagedCluster#parameter}.
        :param section: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#section ServiceFabricManagedCluster#section}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#value ServiceFabricManagedCluster#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterCustomFabricSetting.__init__)
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
            check_type(argname="argument section", value=section, expected_type=type_hints["section"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "parameter": parameter,
            "section": section,
            "value": value,
        }

    @builtins.property
    def parameter(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#parameter ServiceFabricManagedCluster#parameter}.'''
        result = self._values.get("parameter")
        assert result is not None, "Required property 'parameter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def section(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#section ServiceFabricManagedCluster#section}.'''
        result = self._values.get("section")
        assert result is not None, "Required property 'section' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#value ServiceFabricManagedCluster#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricManagedClusterCustomFabricSetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricManagedClusterCustomFabricSettingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterCustomFabricSettingList",
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
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterCustomFabricSettingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceFabricManagedClusterCustomFabricSettingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterCustomFabricSettingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceFabricManagedClusterCustomFabricSettingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterCustomFabricSettingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterCustomFabricSettingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterCustomFabricSettingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterCustomFabricSetting]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterCustomFabricSetting]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterCustomFabricSetting]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterCustomFabricSettingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricManagedClusterCustomFabricSettingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterCustomFabricSettingOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterCustomFabricSettingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="sectionInput")
    def section_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sectionInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameter"))

    @parameter.setter
    def parameter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterCustomFabricSettingOutputReference, "parameter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameter", value)

    @builtins.property
    @jsii.member(jsii_name="section")
    def section(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "section"))

    @section.setter
    def section(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterCustomFabricSettingOutputReference, "section").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "section", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterCustomFabricSettingOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceFabricManagedClusterCustomFabricSetting, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceFabricManagedClusterCustomFabricSetting, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceFabricManagedClusterCustomFabricSetting, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterCustomFabricSettingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterLbRule",
    jsii_struct_bases=[],
    name_mapping={
        "backend_port": "backendPort",
        "frontend_port": "frontendPort",
        "probe_protocol": "probeProtocol",
        "protocol": "protocol",
        "probe_request_path": "probeRequestPath",
    },
)
class ServiceFabricManagedClusterLbRule:
    def __init__(
        self,
        *,
        backend_port: jsii.Number,
        frontend_port: jsii.Number,
        probe_protocol: builtins.str,
        protocol: builtins.str,
        probe_request_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param backend_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#backend_port ServiceFabricManagedCluster#backend_port}.
        :param frontend_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#frontend_port ServiceFabricManagedCluster#frontend_port}.
        :param probe_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#probe_protocol ServiceFabricManagedCluster#probe_protocol}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#protocol ServiceFabricManagedCluster#protocol}.
        :param probe_request_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#probe_request_path ServiceFabricManagedCluster#probe_request_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterLbRule.__init__)
            check_type(argname="argument backend_port", value=backend_port, expected_type=type_hints["backend_port"])
            check_type(argname="argument frontend_port", value=frontend_port, expected_type=type_hints["frontend_port"])
            check_type(argname="argument probe_protocol", value=probe_protocol, expected_type=type_hints["probe_protocol"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument probe_request_path", value=probe_request_path, expected_type=type_hints["probe_request_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend_port": backend_port,
            "frontend_port": frontend_port,
            "probe_protocol": probe_protocol,
            "protocol": protocol,
        }
        if probe_request_path is not None:
            self._values["probe_request_path"] = probe_request_path

    @builtins.property
    def backend_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#backend_port ServiceFabricManagedCluster#backend_port}.'''
        result = self._values.get("backend_port")
        assert result is not None, "Required property 'backend_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def frontend_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#frontend_port ServiceFabricManagedCluster#frontend_port}.'''
        result = self._values.get("frontend_port")
        assert result is not None, "Required property 'frontend_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def probe_protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#probe_protocol ServiceFabricManagedCluster#probe_protocol}.'''
        result = self._values.get("probe_protocol")
        assert result is not None, "Required property 'probe_protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#protocol ServiceFabricManagedCluster#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def probe_request_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#probe_request_path ServiceFabricManagedCluster#probe_request_path}.'''
        result = self._values.get("probe_request_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricManagedClusterLbRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricManagedClusterLbRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterLbRuleList",
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
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterLbRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceFabricManagedClusterLbRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterLbRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceFabricManagedClusterLbRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterLbRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterLbRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterLbRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterLbRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterLbRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterLbRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterLbRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricManagedClusterLbRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterLbRuleOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterLbRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetProbeRequestPath")
    def reset_probe_request_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProbeRequestPath", []))

    @builtins.property
    @jsii.member(jsii_name="backendPortInput")
    def backend_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backendPortInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendPortInput")
    def frontend_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "frontendPortInput"))

    @builtins.property
    @jsii.member(jsii_name="probeProtocolInput")
    def probe_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "probeProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="probeRequestPathInput")
    def probe_request_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "probeRequestPathInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="backendPort")
    def backend_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backendPort"))

    @backend_port.setter
    def backend_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterLbRuleOutputReference, "backend_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendPort", value)

    @builtins.property
    @jsii.member(jsii_name="frontendPort")
    def frontend_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "frontendPort"))

    @frontend_port.setter
    def frontend_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterLbRuleOutputReference, "frontend_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frontendPort", value)

    @builtins.property
    @jsii.member(jsii_name="probeProtocol")
    def probe_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "probeProtocol"))

    @probe_protocol.setter
    def probe_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterLbRuleOutputReference, "probe_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "probeProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="probeRequestPath")
    def probe_request_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "probeRequestPath"))

    @probe_request_path.setter
    def probe_request_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterLbRuleOutputReference, "probe_request_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "probeRequestPath", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterLbRuleOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceFabricManagedClusterLbRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceFabricManagedClusterLbRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceFabricManagedClusterLbRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterLbRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterNodeType",
    jsii_struct_bases=[],
    name_mapping={
        "application_port_range": "applicationPortRange",
        "data_disk_size_gb": "dataDiskSizeGb",
        "ephemeral_port_range": "ephemeralPortRange",
        "name": "name",
        "vm_image_offer": "vmImageOffer",
        "vm_image_publisher": "vmImagePublisher",
        "vm_image_sku": "vmImageSku",
        "vm_image_version": "vmImageVersion",
        "vm_instance_count": "vmInstanceCount",
        "vm_size": "vmSize",
        "capacities": "capacities",
        "data_disk_type": "dataDiskType",
        "multiple_placement_groups_enabled": "multiplePlacementGroupsEnabled",
        "placement_properties": "placementProperties",
        "primary": "primary",
        "stateless": "stateless",
        "vm_secrets": "vmSecrets",
    },
)
class ServiceFabricManagedClusterNodeType:
    def __init__(
        self,
        *,
        application_port_range: builtins.str,
        data_disk_size_gb: jsii.Number,
        ephemeral_port_range: builtins.str,
        name: builtins.str,
        vm_image_offer: builtins.str,
        vm_image_publisher: builtins.str,
        vm_image_sku: builtins.str,
        vm_image_version: builtins.str,
        vm_instance_count: jsii.Number,
        vm_size: builtins.str,
        capacities: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        data_disk_type: typing.Optional[builtins.str] = None,
        multiple_placement_groups_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        placement_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        primary: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        stateless: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        vm_secrets: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricManagedClusterNodeTypeVmSecrets", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param application_port_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#application_port_range ServiceFabricManagedCluster#application_port_range}.
        :param data_disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#data_disk_size_gb ServiceFabricManagedCluster#data_disk_size_gb}.
        :param ephemeral_port_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#ephemeral_port_range ServiceFabricManagedCluster#ephemeral_port_range}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#name ServiceFabricManagedCluster#name}.
        :param vm_image_offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#vm_image_offer ServiceFabricManagedCluster#vm_image_offer}.
        :param vm_image_publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#vm_image_publisher ServiceFabricManagedCluster#vm_image_publisher}.
        :param vm_image_sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#vm_image_sku ServiceFabricManagedCluster#vm_image_sku}.
        :param vm_image_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#vm_image_version ServiceFabricManagedCluster#vm_image_version}.
        :param vm_instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#vm_instance_count ServiceFabricManagedCluster#vm_instance_count}.
        :param vm_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#vm_size ServiceFabricManagedCluster#vm_size}.
        :param capacities: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#capacities ServiceFabricManagedCluster#capacities}.
        :param data_disk_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#data_disk_type ServiceFabricManagedCluster#data_disk_type}.
        :param multiple_placement_groups_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#multiple_placement_groups_enabled ServiceFabricManagedCluster#multiple_placement_groups_enabled}.
        :param placement_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#placement_properties ServiceFabricManagedCluster#placement_properties}.
        :param primary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#primary ServiceFabricManagedCluster#primary}.
        :param stateless: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#stateless ServiceFabricManagedCluster#stateless}.
        :param vm_secrets: vm_secrets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#vm_secrets ServiceFabricManagedCluster#vm_secrets}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterNodeType.__init__)
            check_type(argname="argument application_port_range", value=application_port_range, expected_type=type_hints["application_port_range"])
            check_type(argname="argument data_disk_size_gb", value=data_disk_size_gb, expected_type=type_hints["data_disk_size_gb"])
            check_type(argname="argument ephemeral_port_range", value=ephemeral_port_range, expected_type=type_hints["ephemeral_port_range"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument vm_image_offer", value=vm_image_offer, expected_type=type_hints["vm_image_offer"])
            check_type(argname="argument vm_image_publisher", value=vm_image_publisher, expected_type=type_hints["vm_image_publisher"])
            check_type(argname="argument vm_image_sku", value=vm_image_sku, expected_type=type_hints["vm_image_sku"])
            check_type(argname="argument vm_image_version", value=vm_image_version, expected_type=type_hints["vm_image_version"])
            check_type(argname="argument vm_instance_count", value=vm_instance_count, expected_type=type_hints["vm_instance_count"])
            check_type(argname="argument vm_size", value=vm_size, expected_type=type_hints["vm_size"])
            check_type(argname="argument capacities", value=capacities, expected_type=type_hints["capacities"])
            check_type(argname="argument data_disk_type", value=data_disk_type, expected_type=type_hints["data_disk_type"])
            check_type(argname="argument multiple_placement_groups_enabled", value=multiple_placement_groups_enabled, expected_type=type_hints["multiple_placement_groups_enabled"])
            check_type(argname="argument placement_properties", value=placement_properties, expected_type=type_hints["placement_properties"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
            check_type(argname="argument stateless", value=stateless, expected_type=type_hints["stateless"])
            check_type(argname="argument vm_secrets", value=vm_secrets, expected_type=type_hints["vm_secrets"])
        self._values: typing.Dict[str, typing.Any] = {
            "application_port_range": application_port_range,
            "data_disk_size_gb": data_disk_size_gb,
            "ephemeral_port_range": ephemeral_port_range,
            "name": name,
            "vm_image_offer": vm_image_offer,
            "vm_image_publisher": vm_image_publisher,
            "vm_image_sku": vm_image_sku,
            "vm_image_version": vm_image_version,
            "vm_instance_count": vm_instance_count,
            "vm_size": vm_size,
        }
        if capacities is not None:
            self._values["capacities"] = capacities
        if data_disk_type is not None:
            self._values["data_disk_type"] = data_disk_type
        if multiple_placement_groups_enabled is not None:
            self._values["multiple_placement_groups_enabled"] = multiple_placement_groups_enabled
        if placement_properties is not None:
            self._values["placement_properties"] = placement_properties
        if primary is not None:
            self._values["primary"] = primary
        if stateless is not None:
            self._values["stateless"] = stateless
        if vm_secrets is not None:
            self._values["vm_secrets"] = vm_secrets

    @builtins.property
    def application_port_range(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#application_port_range ServiceFabricManagedCluster#application_port_range}.'''
        result = self._values.get("application_port_range")
        assert result is not None, "Required property 'application_port_range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_disk_size_gb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#data_disk_size_gb ServiceFabricManagedCluster#data_disk_size_gb}.'''
        result = self._values.get("data_disk_size_gb")
        assert result is not None, "Required property 'data_disk_size_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def ephemeral_port_range(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#ephemeral_port_range ServiceFabricManagedCluster#ephemeral_port_range}.'''
        result = self._values.get("ephemeral_port_range")
        assert result is not None, "Required property 'ephemeral_port_range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#name ServiceFabricManagedCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vm_image_offer(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#vm_image_offer ServiceFabricManagedCluster#vm_image_offer}.'''
        result = self._values.get("vm_image_offer")
        assert result is not None, "Required property 'vm_image_offer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vm_image_publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#vm_image_publisher ServiceFabricManagedCluster#vm_image_publisher}.'''
        result = self._values.get("vm_image_publisher")
        assert result is not None, "Required property 'vm_image_publisher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vm_image_sku(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#vm_image_sku ServiceFabricManagedCluster#vm_image_sku}.'''
        result = self._values.get("vm_image_sku")
        assert result is not None, "Required property 'vm_image_sku' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vm_image_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#vm_image_version ServiceFabricManagedCluster#vm_image_version}.'''
        result = self._values.get("vm_image_version")
        assert result is not None, "Required property 'vm_image_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vm_instance_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#vm_instance_count ServiceFabricManagedCluster#vm_instance_count}.'''
        result = self._values.get("vm_instance_count")
        assert result is not None, "Required property 'vm_instance_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def vm_size(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#vm_size ServiceFabricManagedCluster#vm_size}.'''
        result = self._values.get("vm_size")
        assert result is not None, "Required property 'vm_size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacities(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#capacities ServiceFabricManagedCluster#capacities}.'''
        result = self._values.get("capacities")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def data_disk_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#data_disk_type ServiceFabricManagedCluster#data_disk_type}.'''
        result = self._values.get("data_disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def multiple_placement_groups_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#multiple_placement_groups_enabled ServiceFabricManagedCluster#multiple_placement_groups_enabled}.'''
        result = self._values.get("multiple_placement_groups_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def placement_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#placement_properties ServiceFabricManagedCluster#placement_properties}.'''
        result = self._values.get("placement_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def primary(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#primary ServiceFabricManagedCluster#primary}.'''
        result = self._values.get("primary")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def stateless(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#stateless ServiceFabricManagedCluster#stateless}.'''
        result = self._values.get("stateless")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def vm_secrets(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterNodeTypeVmSecrets"]]]:
        '''vm_secrets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#vm_secrets ServiceFabricManagedCluster#vm_secrets}
        '''
        result = self._values.get("vm_secrets")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterNodeTypeVmSecrets"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricManagedClusterNodeType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricManagedClusterNodeTypeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterNodeTypeList",
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
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterNodeTypeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceFabricManagedClusterNodeTypeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterNodeTypeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceFabricManagedClusterNodeTypeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterNodeType]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterNodeType]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterNodeType]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricManagedClusterNodeTypeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterNodeTypeOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterNodeTypeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putVmSecrets")
    def put_vm_secrets(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricManagedClusterNodeTypeVmSecrets", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterNodeTypeOutputReference.put_vm_secrets)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVmSecrets", [value]))

    @jsii.member(jsii_name="resetCapacities")
    def reset_capacities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacities", []))

    @jsii.member(jsii_name="resetDataDiskType")
    def reset_data_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataDiskType", []))

    @jsii.member(jsii_name="resetMultiplePlacementGroupsEnabled")
    def reset_multiple_placement_groups_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMultiplePlacementGroupsEnabled", []))

    @jsii.member(jsii_name="resetPlacementProperties")
    def reset_placement_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacementProperties", []))

    @jsii.member(jsii_name="resetPrimary")
    def reset_primary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimary", []))

    @jsii.member(jsii_name="resetStateless")
    def reset_stateless(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStateless", []))

    @jsii.member(jsii_name="resetVmSecrets")
    def reset_vm_secrets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVmSecrets", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="vmSecrets")
    def vm_secrets(self) -> "ServiceFabricManagedClusterNodeTypeVmSecretsList":
        return typing.cast("ServiceFabricManagedClusterNodeTypeVmSecretsList", jsii.get(self, "vmSecrets"))

    @builtins.property
    @jsii.member(jsii_name="applicationPortRangeInput")
    def application_port_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationPortRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="capacitiesInput")
    def capacities_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "capacitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="dataDiskSizeGbInput")
    def data_disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dataDiskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="dataDiskTypeInput")
    def data_disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataDiskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ephemeralPortRangeInput")
    def ephemeral_port_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ephemeralPortRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="multiplePlacementGroupsEnabledInput")
    def multiple_placement_groups_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "multiplePlacementGroupsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="placementPropertiesInput")
    def placement_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "placementPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryInput")
    def primary_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "primaryInput"))

    @builtins.property
    @jsii.member(jsii_name="statelessInput")
    def stateless_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "statelessInput"))

    @builtins.property
    @jsii.member(jsii_name="vmImageOfferInput")
    def vm_image_offer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmImageOfferInput"))

    @builtins.property
    @jsii.member(jsii_name="vmImagePublisherInput")
    def vm_image_publisher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmImagePublisherInput"))

    @builtins.property
    @jsii.member(jsii_name="vmImageSkuInput")
    def vm_image_sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmImageSkuInput"))

    @builtins.property
    @jsii.member(jsii_name="vmImageVersionInput")
    def vm_image_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmImageVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="vmInstanceCountInput")
    def vm_instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vmInstanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="vmSecretsInput")
    def vm_secrets_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterNodeTypeVmSecrets"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterNodeTypeVmSecrets"]]], jsii.get(self, "vmSecretsInput"))

    @builtins.property
    @jsii.member(jsii_name="vmSizeInput")
    def vm_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationPortRange")
    def application_port_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationPortRange"))

    @application_port_range.setter
    def application_port_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeOutputReference, "application_port_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationPortRange", value)

    @builtins.property
    @jsii.member(jsii_name="capacities")
    def capacities(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "capacities"))

    @capacities.setter
    def capacities(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeOutputReference, "capacities").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacities", value)

    @builtins.property
    @jsii.member(jsii_name="dataDiskSizeGb")
    def data_disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dataDiskSizeGb"))

    @data_disk_size_gb.setter
    def data_disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeOutputReference, "data_disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataDiskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="dataDiskType")
    def data_disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataDiskType"))

    @data_disk_type.setter
    def data_disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeOutputReference, "data_disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataDiskType", value)

    @builtins.property
    @jsii.member(jsii_name="ephemeralPortRange")
    def ephemeral_port_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ephemeralPortRange"))

    @ephemeral_port_range.setter
    def ephemeral_port_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeOutputReference, "ephemeral_port_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ephemeralPortRange", value)

    @builtins.property
    @jsii.member(jsii_name="multiplePlacementGroupsEnabled")
    def multiple_placement_groups_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "multiplePlacementGroupsEnabled"))

    @multiple_placement_groups_enabled.setter
    def multiple_placement_groups_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeOutputReference, "multiple_placement_groups_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multiplePlacementGroupsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="placementProperties")
    def placement_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "placementProperties"))

    @placement_properties.setter
    def placement_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeOutputReference, "placement_properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placementProperties", value)

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "primary"))

    @primary.setter
    def primary(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeOutputReference, "primary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="stateless")
    def stateless(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "stateless"))

    @stateless.setter
    def stateless(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeOutputReference, "stateless").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateless", value)

    @builtins.property
    @jsii.member(jsii_name="vmImageOffer")
    def vm_image_offer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmImageOffer"))

    @vm_image_offer.setter
    def vm_image_offer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeOutputReference, "vm_image_offer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmImageOffer", value)

    @builtins.property
    @jsii.member(jsii_name="vmImagePublisher")
    def vm_image_publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmImagePublisher"))

    @vm_image_publisher.setter
    def vm_image_publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeOutputReference, "vm_image_publisher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmImagePublisher", value)

    @builtins.property
    @jsii.member(jsii_name="vmImageSku")
    def vm_image_sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmImageSku"))

    @vm_image_sku.setter
    def vm_image_sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeOutputReference, "vm_image_sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmImageSku", value)

    @builtins.property
    @jsii.member(jsii_name="vmImageVersion")
    def vm_image_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmImageVersion"))

    @vm_image_version.setter
    def vm_image_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeOutputReference, "vm_image_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmImageVersion", value)

    @builtins.property
    @jsii.member(jsii_name="vmInstanceCount")
    def vm_instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vmInstanceCount"))

    @vm_instance_count.setter
    def vm_instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeOutputReference, "vm_instance_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmInstanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="vmSize")
    def vm_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmSize"))

    @vm_size.setter
    def vm_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeOutputReference, "vm_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmSize", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceFabricManagedClusterNodeType, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceFabricManagedClusterNodeType, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceFabricManagedClusterNodeType, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterNodeTypeVmSecrets",
    jsii_struct_bases=[],
    name_mapping={"certificates": "certificates", "vault_id": "vaultId"},
)
class ServiceFabricManagedClusterNodeTypeVmSecrets:
    def __init__(
        self,
        *,
        certificates: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricManagedClusterNodeTypeVmSecretsCertificates", typing.Dict[str, typing.Any]]]],
        vault_id: builtins.str,
    ) -> None:
        '''
        :param certificates: certificates block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#certificates ServiceFabricManagedCluster#certificates}
        :param vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#vault_id ServiceFabricManagedCluster#vault_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterNodeTypeVmSecrets.__init__)
            check_type(argname="argument certificates", value=certificates, expected_type=type_hints["certificates"])
            check_type(argname="argument vault_id", value=vault_id, expected_type=type_hints["vault_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificates": certificates,
            "vault_id": vault_id,
        }

    @builtins.property
    def certificates(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterNodeTypeVmSecretsCertificates"]]:
        '''certificates block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#certificates ServiceFabricManagedCluster#certificates}
        '''
        result = self._values.get("certificates")
        assert result is not None, "Required property 'certificates' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ServiceFabricManagedClusterNodeTypeVmSecretsCertificates"]], result)

    @builtins.property
    def vault_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#vault_id ServiceFabricManagedCluster#vault_id}.'''
        result = self._values.get("vault_id")
        assert result is not None, "Required property 'vault_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricManagedClusterNodeTypeVmSecrets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterNodeTypeVmSecretsCertificates",
    jsii_struct_bases=[],
    name_mapping={"store": "store", "url": "url"},
)
class ServiceFabricManagedClusterNodeTypeVmSecretsCertificates:
    def __init__(self, *, store: builtins.str, url: builtins.str) -> None:
        '''
        :param store: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#store ServiceFabricManagedCluster#store}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#url ServiceFabricManagedCluster#url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterNodeTypeVmSecretsCertificates.__init__)
            check_type(argname="argument store", value=store, expected_type=type_hints["store"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[str, typing.Any] = {
            "store": store,
            "url": url,
        }

    @builtins.property
    def store(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#store ServiceFabricManagedCluster#store}.'''
        result = self._values.get("store")
        assert result is not None, "Required property 'store' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#url ServiceFabricManagedCluster#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricManagedClusterNodeTypeVmSecretsCertificates(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesList",
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
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterNodeTypeVmSecretsCertificates]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterNodeTypeVmSecretsCertificates]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterNodeTypeVmSecretsCertificates]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="storeInput")
    def store_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storeInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="store")
    def store(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "store"))

    @store.setter
    def store(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesOutputReference, "store").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "store", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceFabricManagedClusterNodeTypeVmSecretsCertificates, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceFabricManagedClusterNodeTypeVmSecretsCertificates, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceFabricManagedClusterNodeTypeVmSecretsCertificates, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricManagedClusterNodeTypeVmSecretsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterNodeTypeVmSecretsList",
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
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterNodeTypeVmSecretsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceFabricManagedClusterNodeTypeVmSecretsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterNodeTypeVmSecretsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceFabricManagedClusterNodeTypeVmSecretsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeVmSecretsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeVmSecretsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeVmSecretsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterNodeTypeVmSecrets]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterNodeTypeVmSecrets]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterNodeTypeVmSecrets]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeVmSecretsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricManagedClusterNodeTypeVmSecretsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterNodeTypeVmSecretsOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterNodeTypeVmSecretsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCertificates")
    def put_certificates(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ServiceFabricManagedClusterNodeTypeVmSecretsCertificates, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterNodeTypeVmSecretsOutputReference.put_certificates)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCertificates", [value]))

    @builtins.property
    @jsii.member(jsii_name="certificates")
    def certificates(
        self,
    ) -> ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesList:
        return typing.cast(ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesList, jsii.get(self, "certificates"))

    @builtins.property
    @jsii.member(jsii_name="certificatesInput")
    def certificates_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterNodeTypeVmSecretsCertificates]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricManagedClusterNodeTypeVmSecretsCertificates]]], jsii.get(self, "certificatesInput"))

    @builtins.property
    @jsii.member(jsii_name="vaultIdInput")
    def vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vaultId")
    def vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vaultId"))

    @vault_id.setter
    def vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeVmSecretsOutputReference, "vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vaultId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceFabricManagedClusterNodeTypeVmSecrets, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceFabricManagedClusterNodeTypeVmSecrets, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceFabricManagedClusterNodeTypeVmSecrets, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterNodeTypeVmSecretsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ServiceFabricManagedClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#create ServiceFabricManagedCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#delete ServiceFabricManagedCluster#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#read ServiceFabricManagedCluster#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#update ServiceFabricManagedCluster#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#create ServiceFabricManagedCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#delete ServiceFabricManagedCluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#read ServiceFabricManagedCluster#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_managed_cluster#update ServiceFabricManagedCluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricManagedClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricManagedClusterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricManagedCluster.ServiceFabricManagedClusterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricManagedClusterTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceFabricManagedClusterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceFabricManagedClusterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceFabricManagedClusterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricManagedClusterTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ServiceFabricManagedCluster",
    "ServiceFabricManagedClusterAuthentication",
    "ServiceFabricManagedClusterAuthenticationActiveDirectory",
    "ServiceFabricManagedClusterAuthenticationActiveDirectoryOutputReference",
    "ServiceFabricManagedClusterAuthenticationCertificate",
    "ServiceFabricManagedClusterAuthenticationCertificateList",
    "ServiceFabricManagedClusterAuthenticationCertificateOutputReference",
    "ServiceFabricManagedClusterAuthenticationOutputReference",
    "ServiceFabricManagedClusterConfig",
    "ServiceFabricManagedClusterCustomFabricSetting",
    "ServiceFabricManagedClusterCustomFabricSettingList",
    "ServiceFabricManagedClusterCustomFabricSettingOutputReference",
    "ServiceFabricManagedClusterLbRule",
    "ServiceFabricManagedClusterLbRuleList",
    "ServiceFabricManagedClusterLbRuleOutputReference",
    "ServiceFabricManagedClusterNodeType",
    "ServiceFabricManagedClusterNodeTypeList",
    "ServiceFabricManagedClusterNodeTypeOutputReference",
    "ServiceFabricManagedClusterNodeTypeVmSecrets",
    "ServiceFabricManagedClusterNodeTypeVmSecretsCertificates",
    "ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesList",
    "ServiceFabricManagedClusterNodeTypeVmSecretsCertificatesOutputReference",
    "ServiceFabricManagedClusterNodeTypeVmSecretsList",
    "ServiceFabricManagedClusterNodeTypeVmSecretsOutputReference",
    "ServiceFabricManagedClusterTimeouts",
    "ServiceFabricManagedClusterTimeoutsOutputReference",
]

publication.publish()
