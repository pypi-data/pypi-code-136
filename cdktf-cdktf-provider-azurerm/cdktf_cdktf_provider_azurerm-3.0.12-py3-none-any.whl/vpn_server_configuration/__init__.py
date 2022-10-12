'''
# `azurerm_vpn_server_configuration`

Refer to the Terraform Registory for docs: [`azurerm_vpn_server_configuration`](https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration).
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


class VpnServerConfiguration(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration azurerm_vpn_server_configuration}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        vpn_authentication_types: typing.Sequence[builtins.str],
        azure_active_directory_authentication: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnServerConfigurationAzureActiveDirectoryAuthentication", typing.Dict[str, typing.Any]]]]] = None,
        client_revoked_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnServerConfigurationClientRevokedCertificate", typing.Dict[str, typing.Any]]]]] = None,
        client_root_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnServerConfigurationClientRootCertificate", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        ipsec_policy: typing.Optional[typing.Union["VpnServerConfigurationIpsecPolicy", typing.Dict[str, typing.Any]]] = None,
        radius: typing.Optional[typing.Union["VpnServerConfigurationRadius", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VpnServerConfigurationTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpn_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration azurerm_vpn_server_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#location VpnServerConfiguration#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#name VpnServerConfiguration#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#resource_group_name VpnServerConfiguration#resource_group_name}.
        :param vpn_authentication_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#vpn_authentication_types VpnServerConfiguration#vpn_authentication_types}.
        :param azure_active_directory_authentication: azure_active_directory_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#azure_active_directory_authentication VpnServerConfiguration#azure_active_directory_authentication}
        :param client_revoked_certificate: client_revoked_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#client_revoked_certificate VpnServerConfiguration#client_revoked_certificate}
        :param client_root_certificate: client_root_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#client_root_certificate VpnServerConfiguration#client_root_certificate}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#id VpnServerConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ipsec_policy: ipsec_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#ipsec_policy VpnServerConfiguration#ipsec_policy}
        :param radius: radius block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#radius VpnServerConfiguration#radius}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#tags VpnServerConfiguration#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#timeouts VpnServerConfiguration#timeouts}
        :param vpn_protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#vpn_protocols VpnServerConfiguration#vpn_protocols}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfiguration.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VpnServerConfigurationConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            vpn_authentication_types=vpn_authentication_types,
            azure_active_directory_authentication=azure_active_directory_authentication,
            client_revoked_certificate=client_revoked_certificate,
            client_root_certificate=client_root_certificate,
            id=id,
            ipsec_policy=ipsec_policy,
            radius=radius,
            tags=tags,
            timeouts=timeouts,
            vpn_protocols=vpn_protocols,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAzureActiveDirectoryAuthentication")
    def put_azure_active_directory_authentication(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnServerConfigurationAzureActiveDirectoryAuthentication", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfiguration.put_azure_active_directory_authentication)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAzureActiveDirectoryAuthentication", [value]))

    @jsii.member(jsii_name="putClientRevokedCertificate")
    def put_client_revoked_certificate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnServerConfigurationClientRevokedCertificate", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfiguration.put_client_revoked_certificate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putClientRevokedCertificate", [value]))

    @jsii.member(jsii_name="putClientRootCertificate")
    def put_client_root_certificate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnServerConfigurationClientRootCertificate", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfiguration.put_client_root_certificate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putClientRootCertificate", [value]))

    @jsii.member(jsii_name="putIpsecPolicy")
    def put_ipsec_policy(
        self,
        *,
        dh_group: builtins.str,
        ike_encryption: builtins.str,
        ike_integrity: builtins.str,
        ipsec_encryption: builtins.str,
        ipsec_integrity: builtins.str,
        pfs_group: builtins.str,
        sa_data_size_kilobytes: jsii.Number,
        sa_lifetime_seconds: jsii.Number,
    ) -> None:
        '''
        :param dh_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#dh_group VpnServerConfiguration#dh_group}.
        :param ike_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#ike_encryption VpnServerConfiguration#ike_encryption}.
        :param ike_integrity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#ike_integrity VpnServerConfiguration#ike_integrity}.
        :param ipsec_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#ipsec_encryption VpnServerConfiguration#ipsec_encryption}.
        :param ipsec_integrity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#ipsec_integrity VpnServerConfiguration#ipsec_integrity}.
        :param pfs_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#pfs_group VpnServerConfiguration#pfs_group}.
        :param sa_data_size_kilobytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#sa_data_size_kilobytes VpnServerConfiguration#sa_data_size_kilobytes}.
        :param sa_lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#sa_lifetime_seconds VpnServerConfiguration#sa_lifetime_seconds}.
        '''
        value = VpnServerConfigurationIpsecPolicy(
            dh_group=dh_group,
            ike_encryption=ike_encryption,
            ike_integrity=ike_integrity,
            ipsec_encryption=ipsec_encryption,
            ipsec_integrity=ipsec_integrity,
            pfs_group=pfs_group,
            sa_data_size_kilobytes=sa_data_size_kilobytes,
            sa_lifetime_seconds=sa_lifetime_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putIpsecPolicy", [value]))

    @jsii.member(jsii_name="putRadius")
    def put_radius(
        self,
        *,
        client_root_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnServerConfigurationRadiusClientRootCertificate", typing.Dict[str, typing.Any]]]]] = None,
        server: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnServerConfigurationRadiusServer", typing.Dict[str, typing.Any]]]]] = None,
        server_root_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnServerConfigurationRadiusServerRootCertificate", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param client_root_certificate: client_root_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#client_root_certificate VpnServerConfiguration#client_root_certificate}
        :param server: server block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#server VpnServerConfiguration#server}
        :param server_root_certificate: server_root_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#server_root_certificate VpnServerConfiguration#server_root_certificate}
        '''
        value = VpnServerConfigurationRadius(
            client_root_certificate=client_root_certificate,
            server=server,
            server_root_certificate=server_root_certificate,
        )

        return typing.cast(None, jsii.invoke(self, "putRadius", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#create VpnServerConfiguration#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#delete VpnServerConfiguration#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#read VpnServerConfiguration#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#update VpnServerConfiguration#update}.
        '''
        value = VpnServerConfigurationTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAzureActiveDirectoryAuthentication")
    def reset_azure_active_directory_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureActiveDirectoryAuthentication", []))

    @jsii.member(jsii_name="resetClientRevokedCertificate")
    def reset_client_revoked_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientRevokedCertificate", []))

    @jsii.member(jsii_name="resetClientRootCertificate")
    def reset_client_root_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientRootCertificate", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpsecPolicy")
    def reset_ipsec_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpsecPolicy", []))

    @jsii.member(jsii_name="resetRadius")
    def reset_radius(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRadius", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVpnProtocols")
    def reset_vpn_protocols(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpnProtocols", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="azureActiveDirectoryAuthentication")
    def azure_active_directory_authentication(
        self,
    ) -> "VpnServerConfigurationAzureActiveDirectoryAuthenticationList":
        return typing.cast("VpnServerConfigurationAzureActiveDirectoryAuthenticationList", jsii.get(self, "azureActiveDirectoryAuthentication"))

    @builtins.property
    @jsii.member(jsii_name="clientRevokedCertificate")
    def client_revoked_certificate(
        self,
    ) -> "VpnServerConfigurationClientRevokedCertificateList":
        return typing.cast("VpnServerConfigurationClientRevokedCertificateList", jsii.get(self, "clientRevokedCertificate"))

    @builtins.property
    @jsii.member(jsii_name="clientRootCertificate")
    def client_root_certificate(
        self,
    ) -> "VpnServerConfigurationClientRootCertificateList":
        return typing.cast("VpnServerConfigurationClientRootCertificateList", jsii.get(self, "clientRootCertificate"))

    @builtins.property
    @jsii.member(jsii_name="ipsecPolicy")
    def ipsec_policy(self) -> "VpnServerConfigurationIpsecPolicyOutputReference":
        return typing.cast("VpnServerConfigurationIpsecPolicyOutputReference", jsii.get(self, "ipsecPolicy"))

    @builtins.property
    @jsii.member(jsii_name="radius")
    def radius(self) -> "VpnServerConfigurationRadiusOutputReference":
        return typing.cast("VpnServerConfigurationRadiusOutputReference", jsii.get(self, "radius"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "VpnServerConfigurationTimeoutsOutputReference":
        return typing.cast("VpnServerConfigurationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="azureActiveDirectoryAuthenticationInput")
    def azure_active_directory_authentication_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnServerConfigurationAzureActiveDirectoryAuthentication"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnServerConfigurationAzureActiveDirectoryAuthentication"]]], jsii.get(self, "azureActiveDirectoryAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="clientRevokedCertificateInput")
    def client_revoked_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnServerConfigurationClientRevokedCertificate"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnServerConfigurationClientRevokedCertificate"]]], jsii.get(self, "clientRevokedCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="clientRootCertificateInput")
    def client_root_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnServerConfigurationClientRootCertificate"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnServerConfigurationClientRootCertificate"]]], jsii.get(self, "clientRootCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipsecPolicyInput")
    def ipsec_policy_input(
        self,
    ) -> typing.Optional["VpnServerConfigurationIpsecPolicy"]:
        return typing.cast(typing.Optional["VpnServerConfigurationIpsecPolicy"], jsii.get(self, "ipsecPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="radiusInput")
    def radius_input(self) -> typing.Optional["VpnServerConfigurationRadius"]:
        return typing.cast(typing.Optional["VpnServerConfigurationRadius"], jsii.get(self, "radiusInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["VpnServerConfigurationTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["VpnServerConfigurationTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnAuthenticationTypesInput")
    def vpn_authentication_types_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpnAuthenticationTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnProtocolsInput")
    def vpn_protocols_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpnProtocolsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfiguration, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfiguration, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfiguration, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfiguration, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfiguration, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="vpnAuthenticationTypes")
    def vpn_authentication_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vpnAuthenticationTypes"))

    @vpn_authentication_types.setter
    def vpn_authentication_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfiguration, "vpn_authentication_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnAuthenticationTypes", value)

    @builtins.property
    @jsii.member(jsii_name="vpnProtocols")
    def vpn_protocols(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vpnProtocols"))

    @vpn_protocols.setter
    def vpn_protocols(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfiguration, "vpn_protocols").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnProtocols", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationAzureActiveDirectoryAuthentication",
    jsii_struct_bases=[],
    name_mapping={"audience": "audience", "issuer": "issuer", "tenant": "tenant"},
)
class VpnServerConfigurationAzureActiveDirectoryAuthentication:
    def __init__(
        self,
        *,
        audience: builtins.str,
        issuer: builtins.str,
        tenant: builtins.str,
    ) -> None:
        '''
        :param audience: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#audience VpnServerConfiguration#audience}.
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#issuer VpnServerConfiguration#issuer}.
        :param tenant: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#tenant VpnServerConfiguration#tenant}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationAzureActiveDirectoryAuthentication.__init__)
            check_type(argname="argument audience", value=audience, expected_type=type_hints["audience"])
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            check_type(argname="argument tenant", value=tenant, expected_type=type_hints["tenant"])
        self._values: typing.Dict[str, typing.Any] = {
            "audience": audience,
            "issuer": issuer,
            "tenant": tenant,
        }

    @builtins.property
    def audience(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#audience VpnServerConfiguration#audience}.'''
        result = self._values.get("audience")
        assert result is not None, "Required property 'audience' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def issuer(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#issuer VpnServerConfiguration#issuer}.'''
        result = self._values.get("issuer")
        assert result is not None, "Required property 'issuer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tenant(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#tenant VpnServerConfiguration#tenant}.'''
        result = self._values.get("tenant")
        assert result is not None, "Required property 'tenant' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnServerConfigurationAzureActiveDirectoryAuthentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnServerConfigurationAzureActiveDirectoryAuthenticationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationAzureActiveDirectoryAuthenticationList",
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
            type_hints = typing.get_type_hints(VpnServerConfigurationAzureActiveDirectoryAuthenticationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VpnServerConfigurationAzureActiveDirectoryAuthenticationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationAzureActiveDirectoryAuthenticationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VpnServerConfigurationAzureActiveDirectoryAuthenticationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationAzureActiveDirectoryAuthenticationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationAzureActiveDirectoryAuthenticationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationAzureActiveDirectoryAuthenticationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationAzureActiveDirectoryAuthentication]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationAzureActiveDirectoryAuthentication]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationAzureActiveDirectoryAuthentication]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationAzureActiveDirectoryAuthenticationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VpnServerConfigurationAzureActiveDirectoryAuthenticationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationAzureActiveDirectoryAuthenticationOutputReference",
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
            type_hints = typing.get_type_hints(VpnServerConfigurationAzureActiveDirectoryAuthenticationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="audienceInput")
    def audience_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "audienceInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantInput")
    def tenant_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantInput"))

    @builtins.property
    @jsii.member(jsii_name="audience")
    def audience(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "audience"))

    @audience.setter
    def audience(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationAzureActiveDirectoryAuthenticationOutputReference, "audience").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audience", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationAzureActiveDirectoryAuthenticationOutputReference, "issuer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="tenant")
    def tenant(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenant"))

    @tenant.setter
    def tenant(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationAzureActiveDirectoryAuthenticationOutputReference, "tenant").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenant", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VpnServerConfigurationAzureActiveDirectoryAuthentication, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VpnServerConfigurationAzureActiveDirectoryAuthentication, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VpnServerConfigurationAzureActiveDirectoryAuthentication, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationAzureActiveDirectoryAuthenticationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationClientRevokedCertificate",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "thumbprint": "thumbprint"},
)
class VpnServerConfigurationClientRevokedCertificate:
    def __init__(self, *, name: builtins.str, thumbprint: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#name VpnServerConfiguration#name}.
        :param thumbprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#thumbprint VpnServerConfiguration#thumbprint}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationClientRevokedCertificate.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument thumbprint", value=thumbprint, expected_type=type_hints["thumbprint"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "thumbprint": thumbprint,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#name VpnServerConfiguration#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def thumbprint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#thumbprint VpnServerConfiguration#thumbprint}.'''
        result = self._values.get("thumbprint")
        assert result is not None, "Required property 'thumbprint' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnServerConfigurationClientRevokedCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnServerConfigurationClientRevokedCertificateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationClientRevokedCertificateList",
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
            type_hints = typing.get_type_hints(VpnServerConfigurationClientRevokedCertificateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VpnServerConfigurationClientRevokedCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationClientRevokedCertificateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VpnServerConfigurationClientRevokedCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationClientRevokedCertificateList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationClientRevokedCertificateList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationClientRevokedCertificateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationClientRevokedCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationClientRevokedCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationClientRevokedCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationClientRevokedCertificateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VpnServerConfigurationClientRevokedCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationClientRevokedCertificateOutputReference",
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
            type_hints = typing.get_type_hints(VpnServerConfigurationClientRevokedCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="thumbprintInput")
    def thumbprint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thumbprintInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationClientRevokedCertificateOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @thumbprint.setter
    def thumbprint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationClientRevokedCertificateOutputReference, "thumbprint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thumbprint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VpnServerConfigurationClientRevokedCertificate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VpnServerConfigurationClientRevokedCertificate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VpnServerConfigurationClientRevokedCertificate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationClientRevokedCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationClientRootCertificate",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "public_cert_data": "publicCertData"},
)
class VpnServerConfigurationClientRootCertificate:
    def __init__(self, *, name: builtins.str, public_cert_data: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#name VpnServerConfiguration#name}.
        :param public_cert_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#public_cert_data VpnServerConfiguration#public_cert_data}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationClientRootCertificate.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument public_cert_data", value=public_cert_data, expected_type=type_hints["public_cert_data"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "public_cert_data": public_cert_data,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#name VpnServerConfiguration#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def public_cert_data(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#public_cert_data VpnServerConfiguration#public_cert_data}.'''
        result = self._values.get("public_cert_data")
        assert result is not None, "Required property 'public_cert_data' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnServerConfigurationClientRootCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnServerConfigurationClientRootCertificateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationClientRootCertificateList",
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
            type_hints = typing.get_type_hints(VpnServerConfigurationClientRootCertificateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VpnServerConfigurationClientRootCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationClientRootCertificateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VpnServerConfigurationClientRootCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationClientRootCertificateList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationClientRootCertificateList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationClientRootCertificateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationClientRootCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationClientRootCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationClientRootCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationClientRootCertificateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VpnServerConfigurationClientRootCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationClientRootCertificateOutputReference",
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
            type_hints = typing.get_type_hints(VpnServerConfigurationClientRootCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicCertDataInput")
    def public_cert_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicCertDataInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationClientRootCertificateOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="publicCertData")
    def public_cert_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicCertData"))

    @public_cert_data.setter
    def public_cert_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationClientRootCertificateOutputReference, "public_cert_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicCertData", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VpnServerConfigurationClientRootCertificate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VpnServerConfigurationClientRootCertificate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VpnServerConfigurationClientRootCertificate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationClientRootCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "vpn_authentication_types": "vpnAuthenticationTypes",
        "azure_active_directory_authentication": "azureActiveDirectoryAuthentication",
        "client_revoked_certificate": "clientRevokedCertificate",
        "client_root_certificate": "clientRootCertificate",
        "id": "id",
        "ipsec_policy": "ipsecPolicy",
        "radius": "radius",
        "tags": "tags",
        "timeouts": "timeouts",
        "vpn_protocols": "vpnProtocols",
    },
)
class VpnServerConfigurationConfig(cdktf.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        vpn_authentication_types: typing.Sequence[builtins.str],
        azure_active_directory_authentication: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[VpnServerConfigurationAzureActiveDirectoryAuthentication, typing.Dict[str, typing.Any]]]]] = None,
        client_revoked_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[VpnServerConfigurationClientRevokedCertificate, typing.Dict[str, typing.Any]]]]] = None,
        client_root_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[VpnServerConfigurationClientRootCertificate, typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        ipsec_policy: typing.Optional[typing.Union["VpnServerConfigurationIpsecPolicy", typing.Dict[str, typing.Any]]] = None,
        radius: typing.Optional[typing.Union["VpnServerConfigurationRadius", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VpnServerConfigurationTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpn_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#location VpnServerConfiguration#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#name VpnServerConfiguration#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#resource_group_name VpnServerConfiguration#resource_group_name}.
        :param vpn_authentication_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#vpn_authentication_types VpnServerConfiguration#vpn_authentication_types}.
        :param azure_active_directory_authentication: azure_active_directory_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#azure_active_directory_authentication VpnServerConfiguration#azure_active_directory_authentication}
        :param client_revoked_certificate: client_revoked_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#client_revoked_certificate VpnServerConfiguration#client_revoked_certificate}
        :param client_root_certificate: client_root_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#client_root_certificate VpnServerConfiguration#client_root_certificate}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#id VpnServerConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ipsec_policy: ipsec_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#ipsec_policy VpnServerConfiguration#ipsec_policy}
        :param radius: radius block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#radius VpnServerConfiguration#radius}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#tags VpnServerConfiguration#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#timeouts VpnServerConfiguration#timeouts}
        :param vpn_protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#vpn_protocols VpnServerConfiguration#vpn_protocols}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(ipsec_policy, dict):
            ipsec_policy = VpnServerConfigurationIpsecPolicy(**ipsec_policy)
        if isinstance(radius, dict):
            radius = VpnServerConfigurationRadius(**radius)
        if isinstance(timeouts, dict):
            timeouts = VpnServerConfigurationTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument vpn_authentication_types", value=vpn_authentication_types, expected_type=type_hints["vpn_authentication_types"])
            check_type(argname="argument azure_active_directory_authentication", value=azure_active_directory_authentication, expected_type=type_hints["azure_active_directory_authentication"])
            check_type(argname="argument client_revoked_certificate", value=client_revoked_certificate, expected_type=type_hints["client_revoked_certificate"])
            check_type(argname="argument client_root_certificate", value=client_root_certificate, expected_type=type_hints["client_root_certificate"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ipsec_policy", value=ipsec_policy, expected_type=type_hints["ipsec_policy"])
            check_type(argname="argument radius", value=radius, expected_type=type_hints["radius"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vpn_protocols", value=vpn_protocols, expected_type=type_hints["vpn_protocols"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "vpn_authentication_types": vpn_authentication_types,
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
        if azure_active_directory_authentication is not None:
            self._values["azure_active_directory_authentication"] = azure_active_directory_authentication
        if client_revoked_certificate is not None:
            self._values["client_revoked_certificate"] = client_revoked_certificate
        if client_root_certificate is not None:
            self._values["client_root_certificate"] = client_root_certificate
        if id is not None:
            self._values["id"] = id
        if ipsec_policy is not None:
            self._values["ipsec_policy"] = ipsec_policy
        if radius is not None:
            self._values["radius"] = radius
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vpn_protocols is not None:
            self._values["vpn_protocols"] = vpn_protocols

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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#location VpnServerConfiguration#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#name VpnServerConfiguration#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#resource_group_name VpnServerConfiguration#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpn_authentication_types(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#vpn_authentication_types VpnServerConfiguration#vpn_authentication_types}.'''
        result = self._values.get("vpn_authentication_types")
        assert result is not None, "Required property 'vpn_authentication_types' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def azure_active_directory_authentication(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationAzureActiveDirectoryAuthentication]]]:
        '''azure_active_directory_authentication block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#azure_active_directory_authentication VpnServerConfiguration#azure_active_directory_authentication}
        '''
        result = self._values.get("azure_active_directory_authentication")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationAzureActiveDirectoryAuthentication]]], result)

    @builtins.property
    def client_revoked_certificate(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationClientRevokedCertificate]]]:
        '''client_revoked_certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#client_revoked_certificate VpnServerConfiguration#client_revoked_certificate}
        '''
        result = self._values.get("client_revoked_certificate")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationClientRevokedCertificate]]], result)

    @builtins.property
    def client_root_certificate(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationClientRootCertificate]]]:
        '''client_root_certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#client_root_certificate VpnServerConfiguration#client_root_certificate}
        '''
        result = self._values.get("client_root_certificate")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationClientRootCertificate]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#id VpnServerConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipsec_policy(self) -> typing.Optional["VpnServerConfigurationIpsecPolicy"]:
        '''ipsec_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#ipsec_policy VpnServerConfiguration#ipsec_policy}
        '''
        result = self._values.get("ipsec_policy")
        return typing.cast(typing.Optional["VpnServerConfigurationIpsecPolicy"], result)

    @builtins.property
    def radius(self) -> typing.Optional["VpnServerConfigurationRadius"]:
        '''radius block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#radius VpnServerConfiguration#radius}
        '''
        result = self._values.get("radius")
        return typing.cast(typing.Optional["VpnServerConfigurationRadius"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#tags VpnServerConfiguration#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["VpnServerConfigurationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#timeouts VpnServerConfiguration#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["VpnServerConfigurationTimeouts"], result)

    @builtins.property
    def vpn_protocols(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#vpn_protocols VpnServerConfiguration#vpn_protocols}.'''
        result = self._values.get("vpn_protocols")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnServerConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationIpsecPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "dh_group": "dhGroup",
        "ike_encryption": "ikeEncryption",
        "ike_integrity": "ikeIntegrity",
        "ipsec_encryption": "ipsecEncryption",
        "ipsec_integrity": "ipsecIntegrity",
        "pfs_group": "pfsGroup",
        "sa_data_size_kilobytes": "saDataSizeKilobytes",
        "sa_lifetime_seconds": "saLifetimeSeconds",
    },
)
class VpnServerConfigurationIpsecPolicy:
    def __init__(
        self,
        *,
        dh_group: builtins.str,
        ike_encryption: builtins.str,
        ike_integrity: builtins.str,
        ipsec_encryption: builtins.str,
        ipsec_integrity: builtins.str,
        pfs_group: builtins.str,
        sa_data_size_kilobytes: jsii.Number,
        sa_lifetime_seconds: jsii.Number,
    ) -> None:
        '''
        :param dh_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#dh_group VpnServerConfiguration#dh_group}.
        :param ike_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#ike_encryption VpnServerConfiguration#ike_encryption}.
        :param ike_integrity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#ike_integrity VpnServerConfiguration#ike_integrity}.
        :param ipsec_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#ipsec_encryption VpnServerConfiguration#ipsec_encryption}.
        :param ipsec_integrity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#ipsec_integrity VpnServerConfiguration#ipsec_integrity}.
        :param pfs_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#pfs_group VpnServerConfiguration#pfs_group}.
        :param sa_data_size_kilobytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#sa_data_size_kilobytes VpnServerConfiguration#sa_data_size_kilobytes}.
        :param sa_lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#sa_lifetime_seconds VpnServerConfiguration#sa_lifetime_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationIpsecPolicy.__init__)
            check_type(argname="argument dh_group", value=dh_group, expected_type=type_hints["dh_group"])
            check_type(argname="argument ike_encryption", value=ike_encryption, expected_type=type_hints["ike_encryption"])
            check_type(argname="argument ike_integrity", value=ike_integrity, expected_type=type_hints["ike_integrity"])
            check_type(argname="argument ipsec_encryption", value=ipsec_encryption, expected_type=type_hints["ipsec_encryption"])
            check_type(argname="argument ipsec_integrity", value=ipsec_integrity, expected_type=type_hints["ipsec_integrity"])
            check_type(argname="argument pfs_group", value=pfs_group, expected_type=type_hints["pfs_group"])
            check_type(argname="argument sa_data_size_kilobytes", value=sa_data_size_kilobytes, expected_type=type_hints["sa_data_size_kilobytes"])
            check_type(argname="argument sa_lifetime_seconds", value=sa_lifetime_seconds, expected_type=type_hints["sa_lifetime_seconds"])
        self._values: typing.Dict[str, typing.Any] = {
            "dh_group": dh_group,
            "ike_encryption": ike_encryption,
            "ike_integrity": ike_integrity,
            "ipsec_encryption": ipsec_encryption,
            "ipsec_integrity": ipsec_integrity,
            "pfs_group": pfs_group,
            "sa_data_size_kilobytes": sa_data_size_kilobytes,
            "sa_lifetime_seconds": sa_lifetime_seconds,
        }

    @builtins.property
    def dh_group(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#dh_group VpnServerConfiguration#dh_group}.'''
        result = self._values.get("dh_group")
        assert result is not None, "Required property 'dh_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ike_encryption(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#ike_encryption VpnServerConfiguration#ike_encryption}.'''
        result = self._values.get("ike_encryption")
        assert result is not None, "Required property 'ike_encryption' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ike_integrity(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#ike_integrity VpnServerConfiguration#ike_integrity}.'''
        result = self._values.get("ike_integrity")
        assert result is not None, "Required property 'ike_integrity' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ipsec_encryption(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#ipsec_encryption VpnServerConfiguration#ipsec_encryption}.'''
        result = self._values.get("ipsec_encryption")
        assert result is not None, "Required property 'ipsec_encryption' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ipsec_integrity(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#ipsec_integrity VpnServerConfiguration#ipsec_integrity}.'''
        result = self._values.get("ipsec_integrity")
        assert result is not None, "Required property 'ipsec_integrity' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pfs_group(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#pfs_group VpnServerConfiguration#pfs_group}.'''
        result = self._values.get("pfs_group")
        assert result is not None, "Required property 'pfs_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sa_data_size_kilobytes(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#sa_data_size_kilobytes VpnServerConfiguration#sa_data_size_kilobytes}.'''
        result = self._values.get("sa_data_size_kilobytes")
        assert result is not None, "Required property 'sa_data_size_kilobytes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def sa_lifetime_seconds(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#sa_lifetime_seconds VpnServerConfiguration#sa_lifetime_seconds}.'''
        result = self._values.get("sa_lifetime_seconds")
        assert result is not None, "Required property 'sa_lifetime_seconds' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnServerConfigurationIpsecPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnServerConfigurationIpsecPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationIpsecPolicyOutputReference",
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
            type_hints = typing.get_type_hints(VpnServerConfigurationIpsecPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dhGroupInput")
    def dh_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dhGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="ikeEncryptionInput")
    def ike_encryption_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ikeEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="ikeIntegrityInput")
    def ike_integrity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ikeIntegrityInput"))

    @builtins.property
    @jsii.member(jsii_name="ipsecEncryptionInput")
    def ipsec_encryption_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipsecEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="ipsecIntegrityInput")
    def ipsec_integrity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipsecIntegrityInput"))

    @builtins.property
    @jsii.member(jsii_name="pfsGroupInput")
    def pfs_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pfsGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="saDataSizeKilobytesInput")
    def sa_data_size_kilobytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "saDataSizeKilobytesInput"))

    @builtins.property
    @jsii.member(jsii_name="saLifetimeSecondsInput")
    def sa_lifetime_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "saLifetimeSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="dhGroup")
    def dh_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dhGroup"))

    @dh_group.setter
    def dh_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationIpsecPolicyOutputReference, "dh_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dhGroup", value)

    @builtins.property
    @jsii.member(jsii_name="ikeEncryption")
    def ike_encryption(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ikeEncryption"))

    @ike_encryption.setter
    def ike_encryption(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationIpsecPolicyOutputReference, "ike_encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ikeEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="ikeIntegrity")
    def ike_integrity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ikeIntegrity"))

    @ike_integrity.setter
    def ike_integrity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationIpsecPolicyOutputReference, "ike_integrity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ikeIntegrity", value)

    @builtins.property
    @jsii.member(jsii_name="ipsecEncryption")
    def ipsec_encryption(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipsecEncryption"))

    @ipsec_encryption.setter
    def ipsec_encryption(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationIpsecPolicyOutputReference, "ipsec_encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipsecEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="ipsecIntegrity")
    def ipsec_integrity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipsecIntegrity"))

    @ipsec_integrity.setter
    def ipsec_integrity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationIpsecPolicyOutputReference, "ipsec_integrity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipsecIntegrity", value)

    @builtins.property
    @jsii.member(jsii_name="pfsGroup")
    def pfs_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pfsGroup"))

    @pfs_group.setter
    def pfs_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationIpsecPolicyOutputReference, "pfs_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pfsGroup", value)

    @builtins.property
    @jsii.member(jsii_name="saDataSizeKilobytes")
    def sa_data_size_kilobytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "saDataSizeKilobytes"))

    @sa_data_size_kilobytes.setter
    def sa_data_size_kilobytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationIpsecPolicyOutputReference, "sa_data_size_kilobytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saDataSizeKilobytes", value)

    @builtins.property
    @jsii.member(jsii_name="saLifetimeSeconds")
    def sa_lifetime_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "saLifetimeSeconds"))

    @sa_lifetime_seconds.setter
    def sa_lifetime_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationIpsecPolicyOutputReference, "sa_lifetime_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saLifetimeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VpnServerConfigurationIpsecPolicy]:
        return typing.cast(typing.Optional[VpnServerConfigurationIpsecPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpnServerConfigurationIpsecPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationIpsecPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationRadius",
    jsii_struct_bases=[],
    name_mapping={
        "client_root_certificate": "clientRootCertificate",
        "server": "server",
        "server_root_certificate": "serverRootCertificate",
    },
)
class VpnServerConfigurationRadius:
    def __init__(
        self,
        *,
        client_root_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnServerConfigurationRadiusClientRootCertificate", typing.Dict[str, typing.Any]]]]] = None,
        server: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnServerConfigurationRadiusServer", typing.Dict[str, typing.Any]]]]] = None,
        server_root_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnServerConfigurationRadiusServerRootCertificate", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param client_root_certificate: client_root_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#client_root_certificate VpnServerConfiguration#client_root_certificate}
        :param server: server block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#server VpnServerConfiguration#server}
        :param server_root_certificate: server_root_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#server_root_certificate VpnServerConfiguration#server_root_certificate}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationRadius.__init__)
            check_type(argname="argument client_root_certificate", value=client_root_certificate, expected_type=type_hints["client_root_certificate"])
            check_type(argname="argument server", value=server, expected_type=type_hints["server"])
            check_type(argname="argument server_root_certificate", value=server_root_certificate, expected_type=type_hints["server_root_certificate"])
        self._values: typing.Dict[str, typing.Any] = {}
        if client_root_certificate is not None:
            self._values["client_root_certificate"] = client_root_certificate
        if server is not None:
            self._values["server"] = server
        if server_root_certificate is not None:
            self._values["server_root_certificate"] = server_root_certificate

    @builtins.property
    def client_root_certificate(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnServerConfigurationRadiusClientRootCertificate"]]]:
        '''client_root_certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#client_root_certificate VpnServerConfiguration#client_root_certificate}
        '''
        result = self._values.get("client_root_certificate")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnServerConfigurationRadiusClientRootCertificate"]]], result)

    @builtins.property
    def server(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnServerConfigurationRadiusServer"]]]:
        '''server block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#server VpnServerConfiguration#server}
        '''
        result = self._values.get("server")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnServerConfigurationRadiusServer"]]], result)

    @builtins.property
    def server_root_certificate(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnServerConfigurationRadiusServerRootCertificate"]]]:
        '''server_root_certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#server_root_certificate VpnServerConfiguration#server_root_certificate}
        '''
        result = self._values.get("server_root_certificate")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnServerConfigurationRadiusServerRootCertificate"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnServerConfigurationRadius(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationRadiusClientRootCertificate",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "thumbprint": "thumbprint"},
)
class VpnServerConfigurationRadiusClientRootCertificate:
    def __init__(self, *, name: builtins.str, thumbprint: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#name VpnServerConfiguration#name}.
        :param thumbprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#thumbprint VpnServerConfiguration#thumbprint}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationRadiusClientRootCertificate.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument thumbprint", value=thumbprint, expected_type=type_hints["thumbprint"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "thumbprint": thumbprint,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#name VpnServerConfiguration#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def thumbprint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#thumbprint VpnServerConfiguration#thumbprint}.'''
        result = self._values.get("thumbprint")
        assert result is not None, "Required property 'thumbprint' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnServerConfigurationRadiusClientRootCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnServerConfigurationRadiusClientRootCertificateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationRadiusClientRootCertificateList",
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
            type_hints = typing.get_type_hints(VpnServerConfigurationRadiusClientRootCertificateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VpnServerConfigurationRadiusClientRootCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationRadiusClientRootCertificateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VpnServerConfigurationRadiusClientRootCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusClientRootCertificateList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusClientRootCertificateList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusClientRootCertificateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationRadiusClientRootCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationRadiusClientRootCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationRadiusClientRootCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusClientRootCertificateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VpnServerConfigurationRadiusClientRootCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationRadiusClientRootCertificateOutputReference",
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
            type_hints = typing.get_type_hints(VpnServerConfigurationRadiusClientRootCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="thumbprintInput")
    def thumbprint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thumbprintInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusClientRootCertificateOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @thumbprint.setter
    def thumbprint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusClientRootCertificateOutputReference, "thumbprint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thumbprint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VpnServerConfigurationRadiusClientRootCertificate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VpnServerConfigurationRadiusClientRootCertificate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VpnServerConfigurationRadiusClientRootCertificate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusClientRootCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VpnServerConfigurationRadiusOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationRadiusOutputReference",
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
            type_hints = typing.get_type_hints(VpnServerConfigurationRadiusOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putClientRootCertificate")
    def put_client_root_certificate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[VpnServerConfigurationRadiusClientRootCertificate, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationRadiusOutputReference.put_client_root_certificate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putClientRootCertificate", [value]))

    @jsii.member(jsii_name="putServer")
    def put_server(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnServerConfigurationRadiusServer", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationRadiusOutputReference.put_server)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putServer", [value]))

    @jsii.member(jsii_name="putServerRootCertificate")
    def put_server_root_certificate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnServerConfigurationRadiusServerRootCertificate", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationRadiusOutputReference.put_server_root_certificate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putServerRootCertificate", [value]))

    @jsii.member(jsii_name="resetClientRootCertificate")
    def reset_client_root_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientRootCertificate", []))

    @jsii.member(jsii_name="resetServer")
    def reset_server(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServer", []))

    @jsii.member(jsii_name="resetServerRootCertificate")
    def reset_server_root_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerRootCertificate", []))

    @builtins.property
    @jsii.member(jsii_name="clientRootCertificate")
    def client_root_certificate(
        self,
    ) -> VpnServerConfigurationRadiusClientRootCertificateList:
        return typing.cast(VpnServerConfigurationRadiusClientRootCertificateList, jsii.get(self, "clientRootCertificate"))

    @builtins.property
    @jsii.member(jsii_name="server")
    def server(self) -> "VpnServerConfigurationRadiusServerList":
        return typing.cast("VpnServerConfigurationRadiusServerList", jsii.get(self, "server"))

    @builtins.property
    @jsii.member(jsii_name="serverRootCertificate")
    def server_root_certificate(
        self,
    ) -> "VpnServerConfigurationRadiusServerRootCertificateList":
        return typing.cast("VpnServerConfigurationRadiusServerRootCertificateList", jsii.get(self, "serverRootCertificate"))

    @builtins.property
    @jsii.member(jsii_name="clientRootCertificateInput")
    def client_root_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationRadiusClientRootCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationRadiusClientRootCertificate]]], jsii.get(self, "clientRootCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="serverInput")
    def server_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnServerConfigurationRadiusServer"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnServerConfigurationRadiusServer"]]], jsii.get(self, "serverInput"))

    @builtins.property
    @jsii.member(jsii_name="serverRootCertificateInput")
    def server_root_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnServerConfigurationRadiusServerRootCertificate"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnServerConfigurationRadiusServerRootCertificate"]]], jsii.get(self, "serverRootCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VpnServerConfigurationRadius]:
        return typing.cast(typing.Optional[VpnServerConfigurationRadius], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpnServerConfigurationRadius],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationRadiusServer",
    jsii_struct_bases=[],
    name_mapping={"address": "address", "score": "score", "secret": "secret"},
)
class VpnServerConfigurationRadiusServer:
    def __init__(
        self,
        *,
        address: builtins.str,
        score: jsii.Number,
        secret: builtins.str,
    ) -> None:
        '''
        :param address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#address VpnServerConfiguration#address}.
        :param score: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#score VpnServerConfiguration#score}.
        :param secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#secret VpnServerConfiguration#secret}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationRadiusServer.__init__)
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument score", value=score, expected_type=type_hints["score"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
        self._values: typing.Dict[str, typing.Any] = {
            "address": address,
            "score": score,
            "secret": secret,
        }

    @builtins.property
    def address(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#address VpnServerConfiguration#address}.'''
        result = self._values.get("address")
        assert result is not None, "Required property 'address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def score(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#score VpnServerConfiguration#score}.'''
        result = self._values.get("score")
        assert result is not None, "Required property 'score' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#secret VpnServerConfiguration#secret}.'''
        result = self._values.get("secret")
        assert result is not None, "Required property 'secret' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnServerConfigurationRadiusServer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnServerConfigurationRadiusServerList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationRadiusServerList",
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
            type_hints = typing.get_type_hints(VpnServerConfigurationRadiusServerList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VpnServerConfigurationRadiusServerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationRadiusServerList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VpnServerConfigurationRadiusServerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusServerList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusServerList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusServerList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationRadiusServer]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationRadiusServer]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationRadiusServer]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusServerList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VpnServerConfigurationRadiusServerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationRadiusServerOutputReference",
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
            type_hints = typing.get_type_hints(VpnServerConfigurationRadiusServerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="scoreInput")
    def score_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scoreInput"))

    @builtins.property
    @jsii.member(jsii_name="secretInput")
    def secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusServerOutputReference, "address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="score")
    def score(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "score"))

    @score.setter
    def score(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusServerOutputReference, "score").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "score", value)

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secret"))

    @secret.setter
    def secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusServerOutputReference, "secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secret", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VpnServerConfigurationRadiusServer, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VpnServerConfigurationRadiusServer, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VpnServerConfigurationRadiusServer, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusServerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationRadiusServerRootCertificate",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "public_cert_data": "publicCertData"},
)
class VpnServerConfigurationRadiusServerRootCertificate:
    def __init__(self, *, name: builtins.str, public_cert_data: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#name VpnServerConfiguration#name}.
        :param public_cert_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#public_cert_data VpnServerConfiguration#public_cert_data}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationRadiusServerRootCertificate.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument public_cert_data", value=public_cert_data, expected_type=type_hints["public_cert_data"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "public_cert_data": public_cert_data,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#name VpnServerConfiguration#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def public_cert_data(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#public_cert_data VpnServerConfiguration#public_cert_data}.'''
        result = self._values.get("public_cert_data")
        assert result is not None, "Required property 'public_cert_data' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnServerConfigurationRadiusServerRootCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnServerConfigurationRadiusServerRootCertificateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationRadiusServerRootCertificateList",
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
            type_hints = typing.get_type_hints(VpnServerConfigurationRadiusServerRootCertificateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VpnServerConfigurationRadiusServerRootCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationRadiusServerRootCertificateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VpnServerConfigurationRadiusServerRootCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusServerRootCertificateList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusServerRootCertificateList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusServerRootCertificateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationRadiusServerRootCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationRadiusServerRootCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnServerConfigurationRadiusServerRootCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusServerRootCertificateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VpnServerConfigurationRadiusServerRootCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationRadiusServerRootCertificateOutputReference",
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
            type_hints = typing.get_type_hints(VpnServerConfigurationRadiusServerRootCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicCertDataInput")
    def public_cert_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicCertDataInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusServerRootCertificateOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="publicCertData")
    def public_cert_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicCertData"))

    @public_cert_data.setter
    def public_cert_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusServerRootCertificateOutputReference, "public_cert_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicCertData", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VpnServerConfigurationRadiusServerRootCertificate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VpnServerConfigurationRadiusServerRootCertificate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VpnServerConfigurationRadiusServerRootCertificate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationRadiusServerRootCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class VpnServerConfigurationTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#create VpnServerConfiguration#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#delete VpnServerConfiguration#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#read VpnServerConfiguration#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#update VpnServerConfiguration#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnServerConfigurationTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#create VpnServerConfiguration#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#delete VpnServerConfiguration#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#read VpnServerConfiguration#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_server_configuration#update VpnServerConfiguration#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnServerConfigurationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnServerConfigurationTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnServerConfiguration.VpnServerConfigurationTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(VpnServerConfigurationTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VpnServerConfigurationTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VpnServerConfigurationTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VpnServerConfigurationTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnServerConfigurationTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VpnServerConfiguration",
    "VpnServerConfigurationAzureActiveDirectoryAuthentication",
    "VpnServerConfigurationAzureActiveDirectoryAuthenticationList",
    "VpnServerConfigurationAzureActiveDirectoryAuthenticationOutputReference",
    "VpnServerConfigurationClientRevokedCertificate",
    "VpnServerConfigurationClientRevokedCertificateList",
    "VpnServerConfigurationClientRevokedCertificateOutputReference",
    "VpnServerConfigurationClientRootCertificate",
    "VpnServerConfigurationClientRootCertificateList",
    "VpnServerConfigurationClientRootCertificateOutputReference",
    "VpnServerConfigurationConfig",
    "VpnServerConfigurationIpsecPolicy",
    "VpnServerConfigurationIpsecPolicyOutputReference",
    "VpnServerConfigurationRadius",
    "VpnServerConfigurationRadiusClientRootCertificate",
    "VpnServerConfigurationRadiusClientRootCertificateList",
    "VpnServerConfigurationRadiusClientRootCertificateOutputReference",
    "VpnServerConfigurationRadiusOutputReference",
    "VpnServerConfigurationRadiusServer",
    "VpnServerConfigurationRadiusServerList",
    "VpnServerConfigurationRadiusServerOutputReference",
    "VpnServerConfigurationRadiusServerRootCertificate",
    "VpnServerConfigurationRadiusServerRootCertificateList",
    "VpnServerConfigurationRadiusServerRootCertificateOutputReference",
    "VpnServerConfigurationTimeouts",
    "VpnServerConfigurationTimeoutsOutputReference",
]

publication.publish()
