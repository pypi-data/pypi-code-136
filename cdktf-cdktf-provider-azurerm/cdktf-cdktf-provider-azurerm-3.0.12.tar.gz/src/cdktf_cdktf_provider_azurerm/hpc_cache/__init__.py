'''
# `azurerm_hpc_cache`

Refer to the Terraform Registory for docs: [`azurerm_hpc_cache`](https://www.terraform.io/docs/providers/azurerm/r/hpc_cache).
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


class HpcCache(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCache",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache azurerm_hpc_cache}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cache_size_in_gb: jsii.Number,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        subnet_id: builtins.str,
        automatically_rotate_key_to_latest_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        default_access_policy: typing.Optional[typing.Union["HpcCacheDefaultAccessPolicy", typing.Dict[str, typing.Any]]] = None,
        directory_active_directory: typing.Optional[typing.Union["HpcCacheDirectoryActiveDirectory", typing.Dict[str, typing.Any]]] = None,
        directory_flat_file: typing.Optional[typing.Union["HpcCacheDirectoryFlatFile", typing.Dict[str, typing.Any]]] = None,
        directory_ldap: typing.Optional[typing.Union["HpcCacheDirectoryLdap", typing.Dict[str, typing.Any]]] = None,
        dns: typing.Optional[typing.Union["HpcCacheDns", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["HpcCacheIdentity", typing.Dict[str, typing.Any]]] = None,
        key_vault_key_id: typing.Optional[builtins.str] = None,
        mtu: typing.Optional[jsii.Number] = None,
        ntp_server: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["HpcCacheTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache azurerm_hpc_cache} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cache_size_in_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#cache_size_in_gb HpcCache#cache_size_in_gb}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#location HpcCache#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#name HpcCache#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#resource_group_name HpcCache#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#sku_name HpcCache#sku_name}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#subnet_id HpcCache#subnet_id}.
        :param automatically_rotate_key_to_latest_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#automatically_rotate_key_to_latest_enabled HpcCache#automatically_rotate_key_to_latest_enabled}.
        :param default_access_policy: default_access_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#default_access_policy HpcCache#default_access_policy}
        :param directory_active_directory: directory_active_directory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#directory_active_directory HpcCache#directory_active_directory}
        :param directory_flat_file: directory_flat_file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#directory_flat_file HpcCache#directory_flat_file}
        :param directory_ldap: directory_ldap block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#directory_ldap HpcCache#directory_ldap}
        :param dns: dns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#dns HpcCache#dns}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#id HpcCache#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#identity HpcCache#identity}
        :param key_vault_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#key_vault_key_id HpcCache#key_vault_key_id}.
        :param mtu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#mtu HpcCache#mtu}.
        :param ntp_server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#ntp_server HpcCache#ntp_server}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#tags HpcCache#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#timeouts HpcCache#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HpcCache.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = HpcCacheConfig(
            cache_size_in_gb=cache_size_in_gb,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            sku_name=sku_name,
            subnet_id=subnet_id,
            automatically_rotate_key_to_latest_enabled=automatically_rotate_key_to_latest_enabled,
            default_access_policy=default_access_policy,
            directory_active_directory=directory_active_directory,
            directory_flat_file=directory_flat_file,
            directory_ldap=directory_ldap,
            dns=dns,
            id=id,
            identity=identity,
            key_vault_key_id=key_vault_key_id,
            mtu=mtu,
            ntp_server=ntp_server,
            tags=tags,
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

    @jsii.member(jsii_name="putDefaultAccessPolicy")
    def put_default_access_policy(
        self,
        *,
        access_rule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HpcCacheDefaultAccessPolicyAccessRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param access_rule: access_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#access_rule HpcCache#access_rule}
        '''
        value = HpcCacheDefaultAccessPolicy(access_rule=access_rule)

        return typing.cast(None, jsii.invoke(self, "putDefaultAccessPolicy", [value]))

    @jsii.member(jsii_name="putDirectoryActiveDirectory")
    def put_directory_active_directory(
        self,
        *,
        cache_netbios_name: builtins.str,
        dns_primary_ip: builtins.str,
        domain_name: builtins.str,
        domain_netbios_name: builtins.str,
        password: builtins.str,
        username: builtins.str,
        dns_secondary_ip: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cache_netbios_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#cache_netbios_name HpcCache#cache_netbios_name}.
        :param dns_primary_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#dns_primary_ip HpcCache#dns_primary_ip}.
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#domain_name HpcCache#domain_name}.
        :param domain_netbios_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#domain_netbios_name HpcCache#domain_netbios_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#password HpcCache#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#username HpcCache#username}.
        :param dns_secondary_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#dns_secondary_ip HpcCache#dns_secondary_ip}.
        '''
        value = HpcCacheDirectoryActiveDirectory(
            cache_netbios_name=cache_netbios_name,
            dns_primary_ip=dns_primary_ip,
            domain_name=domain_name,
            domain_netbios_name=domain_netbios_name,
            password=password,
            username=username,
            dns_secondary_ip=dns_secondary_ip,
        )

        return typing.cast(None, jsii.invoke(self, "putDirectoryActiveDirectory", [value]))

    @jsii.member(jsii_name="putDirectoryFlatFile")
    def put_directory_flat_file(
        self,
        *,
        group_file_uri: builtins.str,
        password_file_uri: builtins.str,
    ) -> None:
        '''
        :param group_file_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#group_file_uri HpcCache#group_file_uri}.
        :param password_file_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#password_file_uri HpcCache#password_file_uri}.
        '''
        value = HpcCacheDirectoryFlatFile(
            group_file_uri=group_file_uri, password_file_uri=password_file_uri
        )

        return typing.cast(None, jsii.invoke(self, "putDirectoryFlatFile", [value]))

    @jsii.member(jsii_name="putDirectoryLdap")
    def put_directory_ldap(
        self,
        *,
        base_dn: builtins.str,
        server: builtins.str,
        bind: typing.Optional[typing.Union["HpcCacheDirectoryLdapBind", typing.Dict[str, typing.Any]]] = None,
        certificate_validation_uri: typing.Optional[builtins.str] = None,
        download_certificate_automatically: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param base_dn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#base_dn HpcCache#base_dn}.
        :param server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#server HpcCache#server}.
        :param bind: bind block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#bind HpcCache#bind}
        :param certificate_validation_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#certificate_validation_uri HpcCache#certificate_validation_uri}.
        :param download_certificate_automatically: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#download_certificate_automatically HpcCache#download_certificate_automatically}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#encrypted HpcCache#encrypted}.
        '''
        value = HpcCacheDirectoryLdap(
            base_dn=base_dn,
            server=server,
            bind=bind,
            certificate_validation_uri=certificate_validation_uri,
            download_certificate_automatically=download_certificate_automatically,
            encrypted=encrypted,
        )

        return typing.cast(None, jsii.invoke(self, "putDirectoryLdap", [value]))

    @jsii.member(jsii_name="putDns")
    def put_dns(
        self,
        *,
        servers: typing.Sequence[builtins.str],
        search_domain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#servers HpcCache#servers}.
        :param search_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#search_domain HpcCache#search_domain}.
        '''
        value = HpcCacheDns(servers=servers, search_domain=search_domain)

        return typing.cast(None, jsii.invoke(self, "putDns", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        identity_ids: typing.Sequence[builtins.str],
        type: builtins.str,
    ) -> None:
        '''
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#identity_ids HpcCache#identity_ids}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#type HpcCache#type}.
        '''
        value = HpcCacheIdentity(identity_ids=identity_ids, type=type)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#create HpcCache#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#delete HpcCache#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#read HpcCache#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#update HpcCache#update}.
        '''
        value = HpcCacheTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAutomaticallyRotateKeyToLatestEnabled")
    def reset_automatically_rotate_key_to_latest_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticallyRotateKeyToLatestEnabled", []))

    @jsii.member(jsii_name="resetDefaultAccessPolicy")
    def reset_default_access_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultAccessPolicy", []))

    @jsii.member(jsii_name="resetDirectoryActiveDirectory")
    def reset_directory_active_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectoryActiveDirectory", []))

    @jsii.member(jsii_name="resetDirectoryFlatFile")
    def reset_directory_flat_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectoryFlatFile", []))

    @jsii.member(jsii_name="resetDirectoryLdap")
    def reset_directory_ldap(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectoryLdap", []))

    @jsii.member(jsii_name="resetDns")
    def reset_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDns", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetKeyVaultKeyId")
    def reset_key_vault_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultKeyId", []))

    @jsii.member(jsii_name="resetMtu")
    def reset_mtu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMtu", []))

    @jsii.member(jsii_name="resetNtpServer")
    def reset_ntp_server(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNtpServer", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="defaultAccessPolicy")
    def default_access_policy(self) -> "HpcCacheDefaultAccessPolicyOutputReference":
        return typing.cast("HpcCacheDefaultAccessPolicyOutputReference", jsii.get(self, "defaultAccessPolicy"))

    @builtins.property
    @jsii.member(jsii_name="directoryActiveDirectory")
    def directory_active_directory(
        self,
    ) -> "HpcCacheDirectoryActiveDirectoryOutputReference":
        return typing.cast("HpcCacheDirectoryActiveDirectoryOutputReference", jsii.get(self, "directoryActiveDirectory"))

    @builtins.property
    @jsii.member(jsii_name="directoryFlatFile")
    def directory_flat_file(self) -> "HpcCacheDirectoryFlatFileOutputReference":
        return typing.cast("HpcCacheDirectoryFlatFileOutputReference", jsii.get(self, "directoryFlatFile"))

    @builtins.property
    @jsii.member(jsii_name="directoryLdap")
    def directory_ldap(self) -> "HpcCacheDirectoryLdapOutputReference":
        return typing.cast("HpcCacheDirectoryLdapOutputReference", jsii.get(self, "directoryLdap"))

    @builtins.property
    @jsii.member(jsii_name="dns")
    def dns(self) -> "HpcCacheDnsOutputReference":
        return typing.cast("HpcCacheDnsOutputReference", jsii.get(self, "dns"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "HpcCacheIdentityOutputReference":
        return typing.cast("HpcCacheIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="mountAddresses")
    def mount_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "mountAddresses"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "HpcCacheTimeoutsOutputReference":
        return typing.cast("HpcCacheTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="automaticallyRotateKeyToLatestEnabledInput")
    def automatically_rotate_key_to_latest_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "automaticallyRotateKeyToLatestEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheSizeInGbInput")
    def cache_size_in_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cacheSizeInGbInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultAccessPolicyInput")
    def default_access_policy_input(
        self,
    ) -> typing.Optional["HpcCacheDefaultAccessPolicy"]:
        return typing.cast(typing.Optional["HpcCacheDefaultAccessPolicy"], jsii.get(self, "defaultAccessPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryActiveDirectoryInput")
    def directory_active_directory_input(
        self,
    ) -> typing.Optional["HpcCacheDirectoryActiveDirectory"]:
        return typing.cast(typing.Optional["HpcCacheDirectoryActiveDirectory"], jsii.get(self, "directoryActiveDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryFlatFileInput")
    def directory_flat_file_input(self) -> typing.Optional["HpcCacheDirectoryFlatFile"]:
        return typing.cast(typing.Optional["HpcCacheDirectoryFlatFile"], jsii.get(self, "directoryFlatFileInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryLdapInput")
    def directory_ldap_input(self) -> typing.Optional["HpcCacheDirectoryLdap"]:
        return typing.cast(typing.Optional["HpcCacheDirectoryLdap"], jsii.get(self, "directoryLdapInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsInput")
    def dns_input(self) -> typing.Optional["HpcCacheDns"]:
        return typing.cast(typing.Optional["HpcCacheDns"], jsii.get(self, "dnsInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["HpcCacheIdentity"]:
        return typing.cast(typing.Optional["HpcCacheIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultKeyIdInput")
    def key_vault_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="mtuInput")
    def mtu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mtuInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="ntpServerInput")
    def ntp_server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ntpServerInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="skuNameInput")
    def sku_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuNameInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["HpcCacheTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["HpcCacheTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticallyRotateKeyToLatestEnabled")
    def automatically_rotate_key_to_latest_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "automaticallyRotateKeyToLatestEnabled"))

    @automatically_rotate_key_to_latest_enabled.setter
    def automatically_rotate_key_to_latest_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCache, "automatically_rotate_key_to_latest_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticallyRotateKeyToLatestEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="cacheSizeInGb")
    def cache_size_in_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cacheSizeInGb"))

    @cache_size_in_gb.setter
    def cache_size_in_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCache, "cache_size_in_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheSizeInGb", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCache, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultKeyId")
    def key_vault_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultKeyId"))

    @key_vault_key_id.setter
    def key_vault_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCache, "key_vault_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCache, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="mtu")
    def mtu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mtu"))

    @mtu.setter
    def mtu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCache, "mtu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mtu", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCache, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ntpServer")
    def ntp_server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ntpServer"))

    @ntp_server.setter
    def ntp_server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCache, "ntp_server").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ntpServer", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCache, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="skuName")
    def sku_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skuName"))

    @sku_name.setter
    def sku_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCache, "sku_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skuName", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCache, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCache, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cache_size_in_gb": "cacheSizeInGb",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "sku_name": "skuName",
        "subnet_id": "subnetId",
        "automatically_rotate_key_to_latest_enabled": "automaticallyRotateKeyToLatestEnabled",
        "default_access_policy": "defaultAccessPolicy",
        "directory_active_directory": "directoryActiveDirectory",
        "directory_flat_file": "directoryFlatFile",
        "directory_ldap": "directoryLdap",
        "dns": "dns",
        "id": "id",
        "identity": "identity",
        "key_vault_key_id": "keyVaultKeyId",
        "mtu": "mtu",
        "ntp_server": "ntpServer",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class HpcCacheConfig(cdktf.TerraformMetaArguments):
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
        cache_size_in_gb: jsii.Number,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        subnet_id: builtins.str,
        automatically_rotate_key_to_latest_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        default_access_policy: typing.Optional[typing.Union["HpcCacheDefaultAccessPolicy", typing.Dict[str, typing.Any]]] = None,
        directory_active_directory: typing.Optional[typing.Union["HpcCacheDirectoryActiveDirectory", typing.Dict[str, typing.Any]]] = None,
        directory_flat_file: typing.Optional[typing.Union["HpcCacheDirectoryFlatFile", typing.Dict[str, typing.Any]]] = None,
        directory_ldap: typing.Optional[typing.Union["HpcCacheDirectoryLdap", typing.Dict[str, typing.Any]]] = None,
        dns: typing.Optional[typing.Union["HpcCacheDns", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["HpcCacheIdentity", typing.Dict[str, typing.Any]]] = None,
        key_vault_key_id: typing.Optional[builtins.str] = None,
        mtu: typing.Optional[jsii.Number] = None,
        ntp_server: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["HpcCacheTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cache_size_in_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#cache_size_in_gb HpcCache#cache_size_in_gb}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#location HpcCache#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#name HpcCache#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#resource_group_name HpcCache#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#sku_name HpcCache#sku_name}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#subnet_id HpcCache#subnet_id}.
        :param automatically_rotate_key_to_latest_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#automatically_rotate_key_to_latest_enabled HpcCache#automatically_rotate_key_to_latest_enabled}.
        :param default_access_policy: default_access_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#default_access_policy HpcCache#default_access_policy}
        :param directory_active_directory: directory_active_directory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#directory_active_directory HpcCache#directory_active_directory}
        :param directory_flat_file: directory_flat_file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#directory_flat_file HpcCache#directory_flat_file}
        :param directory_ldap: directory_ldap block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#directory_ldap HpcCache#directory_ldap}
        :param dns: dns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#dns HpcCache#dns}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#id HpcCache#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#identity HpcCache#identity}
        :param key_vault_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#key_vault_key_id HpcCache#key_vault_key_id}.
        :param mtu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#mtu HpcCache#mtu}.
        :param ntp_server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#ntp_server HpcCache#ntp_server}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#tags HpcCache#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#timeouts HpcCache#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(default_access_policy, dict):
            default_access_policy = HpcCacheDefaultAccessPolicy(**default_access_policy)
        if isinstance(directory_active_directory, dict):
            directory_active_directory = HpcCacheDirectoryActiveDirectory(**directory_active_directory)
        if isinstance(directory_flat_file, dict):
            directory_flat_file = HpcCacheDirectoryFlatFile(**directory_flat_file)
        if isinstance(directory_ldap, dict):
            directory_ldap = HpcCacheDirectoryLdap(**directory_ldap)
        if isinstance(dns, dict):
            dns = HpcCacheDns(**dns)
        if isinstance(identity, dict):
            identity = HpcCacheIdentity(**identity)
        if isinstance(timeouts, dict):
            timeouts = HpcCacheTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(HpcCacheConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cache_size_in_gb", value=cache_size_in_gb, expected_type=type_hints["cache_size_in_gb"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument sku_name", value=sku_name, expected_type=type_hints["sku_name"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument automatically_rotate_key_to_latest_enabled", value=automatically_rotate_key_to_latest_enabled, expected_type=type_hints["automatically_rotate_key_to_latest_enabled"])
            check_type(argname="argument default_access_policy", value=default_access_policy, expected_type=type_hints["default_access_policy"])
            check_type(argname="argument directory_active_directory", value=directory_active_directory, expected_type=type_hints["directory_active_directory"])
            check_type(argname="argument directory_flat_file", value=directory_flat_file, expected_type=type_hints["directory_flat_file"])
            check_type(argname="argument directory_ldap", value=directory_ldap, expected_type=type_hints["directory_ldap"])
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument key_vault_key_id", value=key_vault_key_id, expected_type=type_hints["key_vault_key_id"])
            check_type(argname="argument mtu", value=mtu, expected_type=type_hints["mtu"])
            check_type(argname="argument ntp_server", value=ntp_server, expected_type=type_hints["ntp_server"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "cache_size_in_gb": cache_size_in_gb,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "sku_name": sku_name,
            "subnet_id": subnet_id,
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
        if automatically_rotate_key_to_latest_enabled is not None:
            self._values["automatically_rotate_key_to_latest_enabled"] = automatically_rotate_key_to_latest_enabled
        if default_access_policy is not None:
            self._values["default_access_policy"] = default_access_policy
        if directory_active_directory is not None:
            self._values["directory_active_directory"] = directory_active_directory
        if directory_flat_file is not None:
            self._values["directory_flat_file"] = directory_flat_file
        if directory_ldap is not None:
            self._values["directory_ldap"] = directory_ldap
        if dns is not None:
            self._values["dns"] = dns
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if key_vault_key_id is not None:
            self._values["key_vault_key_id"] = key_vault_key_id
        if mtu is not None:
            self._values["mtu"] = mtu
        if ntp_server is not None:
            self._values["ntp_server"] = ntp_server
        if tags is not None:
            self._values["tags"] = tags
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
    def cache_size_in_gb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#cache_size_in_gb HpcCache#cache_size_in_gb}.'''
        result = self._values.get("cache_size_in_gb")
        assert result is not None, "Required property 'cache_size_in_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#location HpcCache#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#name HpcCache#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#resource_group_name HpcCache#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#sku_name HpcCache#sku_name}.'''
        result = self._values.get("sku_name")
        assert result is not None, "Required property 'sku_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#subnet_id HpcCache#subnet_id}.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def automatically_rotate_key_to_latest_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#automatically_rotate_key_to_latest_enabled HpcCache#automatically_rotate_key_to_latest_enabled}.'''
        result = self._values.get("automatically_rotate_key_to_latest_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def default_access_policy(self) -> typing.Optional["HpcCacheDefaultAccessPolicy"]:
        '''default_access_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#default_access_policy HpcCache#default_access_policy}
        '''
        result = self._values.get("default_access_policy")
        return typing.cast(typing.Optional["HpcCacheDefaultAccessPolicy"], result)

    @builtins.property
    def directory_active_directory(
        self,
    ) -> typing.Optional["HpcCacheDirectoryActiveDirectory"]:
        '''directory_active_directory block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#directory_active_directory HpcCache#directory_active_directory}
        '''
        result = self._values.get("directory_active_directory")
        return typing.cast(typing.Optional["HpcCacheDirectoryActiveDirectory"], result)

    @builtins.property
    def directory_flat_file(self) -> typing.Optional["HpcCacheDirectoryFlatFile"]:
        '''directory_flat_file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#directory_flat_file HpcCache#directory_flat_file}
        '''
        result = self._values.get("directory_flat_file")
        return typing.cast(typing.Optional["HpcCacheDirectoryFlatFile"], result)

    @builtins.property
    def directory_ldap(self) -> typing.Optional["HpcCacheDirectoryLdap"]:
        '''directory_ldap block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#directory_ldap HpcCache#directory_ldap}
        '''
        result = self._values.get("directory_ldap")
        return typing.cast(typing.Optional["HpcCacheDirectoryLdap"], result)

    @builtins.property
    def dns(self) -> typing.Optional["HpcCacheDns"]:
        '''dns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#dns HpcCache#dns}
        '''
        result = self._values.get("dns")
        return typing.cast(typing.Optional["HpcCacheDns"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#id HpcCache#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["HpcCacheIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#identity HpcCache#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["HpcCacheIdentity"], result)

    @builtins.property
    def key_vault_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#key_vault_key_id HpcCache#key_vault_key_id}.'''
        result = self._values.get("key_vault_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mtu(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#mtu HpcCache#mtu}.'''
        result = self._values.get("mtu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ntp_server(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#ntp_server HpcCache#ntp_server}.'''
        result = self._values.get("ntp_server")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#tags HpcCache#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["HpcCacheTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#timeouts HpcCache#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["HpcCacheTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HpcCacheConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheDefaultAccessPolicy",
    jsii_struct_bases=[],
    name_mapping={"access_rule": "accessRule"},
)
class HpcCacheDefaultAccessPolicy:
    def __init__(
        self,
        *,
        access_rule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HpcCacheDefaultAccessPolicyAccessRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param access_rule: access_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#access_rule HpcCache#access_rule}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HpcCacheDefaultAccessPolicy.__init__)
            check_type(argname="argument access_rule", value=access_rule, expected_type=type_hints["access_rule"])
        self._values: typing.Dict[str, typing.Any] = {
            "access_rule": access_rule,
        }

    @builtins.property
    def access_rule(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["HpcCacheDefaultAccessPolicyAccessRule"]]:
        '''access_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#access_rule HpcCache#access_rule}
        '''
        result = self._values.get("access_rule")
        assert result is not None, "Required property 'access_rule' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["HpcCacheDefaultAccessPolicyAccessRule"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HpcCacheDefaultAccessPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheDefaultAccessPolicyAccessRule",
    jsii_struct_bases=[],
    name_mapping={
        "access": "access",
        "scope": "scope",
        "anonymous_gid": "anonymousGid",
        "anonymous_uid": "anonymousUid",
        "filter": "filter",
        "root_squash_enabled": "rootSquashEnabled",
        "submount_access_enabled": "submountAccessEnabled",
        "suid_enabled": "suidEnabled",
    },
)
class HpcCacheDefaultAccessPolicyAccessRule:
    def __init__(
        self,
        *,
        access: builtins.str,
        scope: builtins.str,
        anonymous_gid: typing.Optional[jsii.Number] = None,
        anonymous_uid: typing.Optional[jsii.Number] = None,
        filter: typing.Optional[builtins.str] = None,
        root_squash_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        submount_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        suid_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#access HpcCache#access}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#scope HpcCache#scope}.
        :param anonymous_gid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#anonymous_gid HpcCache#anonymous_gid}.
        :param anonymous_uid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#anonymous_uid HpcCache#anonymous_uid}.
        :param filter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#filter HpcCache#filter}.
        :param root_squash_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#root_squash_enabled HpcCache#root_squash_enabled}.
        :param submount_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#submount_access_enabled HpcCache#submount_access_enabled}.
        :param suid_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#suid_enabled HpcCache#suid_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HpcCacheDefaultAccessPolicyAccessRule.__init__)
            check_type(argname="argument access", value=access, expected_type=type_hints["access"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument anonymous_gid", value=anonymous_gid, expected_type=type_hints["anonymous_gid"])
            check_type(argname="argument anonymous_uid", value=anonymous_uid, expected_type=type_hints["anonymous_uid"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument root_squash_enabled", value=root_squash_enabled, expected_type=type_hints["root_squash_enabled"])
            check_type(argname="argument submount_access_enabled", value=submount_access_enabled, expected_type=type_hints["submount_access_enabled"])
            check_type(argname="argument suid_enabled", value=suid_enabled, expected_type=type_hints["suid_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "access": access,
            "scope": scope,
        }
        if anonymous_gid is not None:
            self._values["anonymous_gid"] = anonymous_gid
        if anonymous_uid is not None:
            self._values["anonymous_uid"] = anonymous_uid
        if filter is not None:
            self._values["filter"] = filter
        if root_squash_enabled is not None:
            self._values["root_squash_enabled"] = root_squash_enabled
        if submount_access_enabled is not None:
            self._values["submount_access_enabled"] = submount_access_enabled
        if suid_enabled is not None:
            self._values["suid_enabled"] = suid_enabled

    @builtins.property
    def access(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#access HpcCache#access}.'''
        result = self._values.get("access")
        assert result is not None, "Required property 'access' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#scope HpcCache#scope}.'''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def anonymous_gid(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#anonymous_gid HpcCache#anonymous_gid}.'''
        result = self._values.get("anonymous_gid")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def anonymous_uid(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#anonymous_uid HpcCache#anonymous_uid}.'''
        result = self._values.get("anonymous_uid")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def filter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#filter HpcCache#filter}.'''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_squash_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#root_squash_enabled HpcCache#root_squash_enabled}.'''
        result = self._values.get("root_squash_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def submount_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#submount_access_enabled HpcCache#submount_access_enabled}.'''
        result = self._values.get("submount_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def suid_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#suid_enabled HpcCache#suid_enabled}.'''
        result = self._values.get("suid_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HpcCacheDefaultAccessPolicyAccessRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HpcCacheDefaultAccessPolicyAccessRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheDefaultAccessPolicyAccessRuleList",
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
            type_hints = typing.get_type_hints(HpcCacheDefaultAccessPolicyAccessRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HpcCacheDefaultAccessPolicyAccessRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HpcCacheDefaultAccessPolicyAccessRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HpcCacheDefaultAccessPolicyAccessRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDefaultAccessPolicyAccessRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(HpcCacheDefaultAccessPolicyAccessRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(HpcCacheDefaultAccessPolicyAccessRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HpcCacheDefaultAccessPolicyAccessRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HpcCacheDefaultAccessPolicyAccessRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HpcCacheDefaultAccessPolicyAccessRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDefaultAccessPolicyAccessRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HpcCacheDefaultAccessPolicyAccessRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheDefaultAccessPolicyAccessRuleOutputReference",
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
            type_hints = typing.get_type_hints(HpcCacheDefaultAccessPolicyAccessRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAnonymousGid")
    def reset_anonymous_gid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnonymousGid", []))

    @jsii.member(jsii_name="resetAnonymousUid")
    def reset_anonymous_uid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnonymousUid", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetRootSquashEnabled")
    def reset_root_squash_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootSquashEnabled", []))

    @jsii.member(jsii_name="resetSubmountAccessEnabled")
    def reset_submount_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubmountAccessEnabled", []))

    @jsii.member(jsii_name="resetSuidEnabled")
    def reset_suid_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuidEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="accessInput")
    def access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessInput"))

    @builtins.property
    @jsii.member(jsii_name="anonymousGidInput")
    def anonymous_gid_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "anonymousGidInput"))

    @builtins.property
    @jsii.member(jsii_name="anonymousUidInput")
    def anonymous_uid_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "anonymousUidInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="rootSquashEnabledInput")
    def root_squash_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "rootSquashEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="submountAccessEnabledInput")
    def submount_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "submountAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="suidEnabledInput")
    def suid_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "suidEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="access")
    def access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "access"))

    @access.setter
    def access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDefaultAccessPolicyAccessRuleOutputReference, "access").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "access", value)

    @builtins.property
    @jsii.member(jsii_name="anonymousGid")
    def anonymous_gid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "anonymousGid"))

    @anonymous_gid.setter
    def anonymous_gid(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDefaultAccessPolicyAccessRuleOutputReference, "anonymous_gid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anonymousGid", value)

    @builtins.property
    @jsii.member(jsii_name="anonymousUid")
    def anonymous_uid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "anonymousUid"))

    @anonymous_uid.setter
    def anonymous_uid(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDefaultAccessPolicyAccessRuleOutputReference, "anonymous_uid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anonymousUid", value)

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filter"))

    @filter.setter
    def filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDefaultAccessPolicyAccessRuleOutputReference, "filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filter", value)

    @builtins.property
    @jsii.member(jsii_name="rootSquashEnabled")
    def root_squash_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "rootSquashEnabled"))

    @root_squash_enabled.setter
    def root_squash_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDefaultAccessPolicyAccessRuleOutputReference, "root_squash_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootSquashEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDefaultAccessPolicyAccessRuleOutputReference, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="submountAccessEnabled")
    def submount_access_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "submountAccessEnabled"))

    @submount_access_enabled.setter
    def submount_access_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDefaultAccessPolicyAccessRuleOutputReference, "submount_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "submountAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="suidEnabled")
    def suid_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "suidEnabled"))

    @suid_enabled.setter
    def suid_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDefaultAccessPolicyAccessRuleOutputReference, "suid_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suidEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HpcCacheDefaultAccessPolicyAccessRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HpcCacheDefaultAccessPolicyAccessRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HpcCacheDefaultAccessPolicyAccessRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDefaultAccessPolicyAccessRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HpcCacheDefaultAccessPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheDefaultAccessPolicyOutputReference",
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
            type_hints = typing.get_type_hints(HpcCacheDefaultAccessPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAccessRule")
    def put_access_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[HpcCacheDefaultAccessPolicyAccessRule, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HpcCacheDefaultAccessPolicyOutputReference.put_access_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccessRule", [value]))

    @builtins.property
    @jsii.member(jsii_name="accessRule")
    def access_rule(self) -> HpcCacheDefaultAccessPolicyAccessRuleList:
        return typing.cast(HpcCacheDefaultAccessPolicyAccessRuleList, jsii.get(self, "accessRule"))

    @builtins.property
    @jsii.member(jsii_name="accessRuleInput")
    def access_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HpcCacheDefaultAccessPolicyAccessRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HpcCacheDefaultAccessPolicyAccessRule]]], jsii.get(self, "accessRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HpcCacheDefaultAccessPolicy]:
        return typing.cast(typing.Optional[HpcCacheDefaultAccessPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HpcCacheDefaultAccessPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDefaultAccessPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheDirectoryActiveDirectory",
    jsii_struct_bases=[],
    name_mapping={
        "cache_netbios_name": "cacheNetbiosName",
        "dns_primary_ip": "dnsPrimaryIp",
        "domain_name": "domainName",
        "domain_netbios_name": "domainNetbiosName",
        "password": "password",
        "username": "username",
        "dns_secondary_ip": "dnsSecondaryIp",
    },
)
class HpcCacheDirectoryActiveDirectory:
    def __init__(
        self,
        *,
        cache_netbios_name: builtins.str,
        dns_primary_ip: builtins.str,
        domain_name: builtins.str,
        domain_netbios_name: builtins.str,
        password: builtins.str,
        username: builtins.str,
        dns_secondary_ip: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cache_netbios_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#cache_netbios_name HpcCache#cache_netbios_name}.
        :param dns_primary_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#dns_primary_ip HpcCache#dns_primary_ip}.
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#domain_name HpcCache#domain_name}.
        :param domain_netbios_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#domain_netbios_name HpcCache#domain_netbios_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#password HpcCache#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#username HpcCache#username}.
        :param dns_secondary_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#dns_secondary_ip HpcCache#dns_secondary_ip}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HpcCacheDirectoryActiveDirectory.__init__)
            check_type(argname="argument cache_netbios_name", value=cache_netbios_name, expected_type=type_hints["cache_netbios_name"])
            check_type(argname="argument dns_primary_ip", value=dns_primary_ip, expected_type=type_hints["dns_primary_ip"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument domain_netbios_name", value=domain_netbios_name, expected_type=type_hints["domain_netbios_name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument dns_secondary_ip", value=dns_secondary_ip, expected_type=type_hints["dns_secondary_ip"])
        self._values: typing.Dict[str, typing.Any] = {
            "cache_netbios_name": cache_netbios_name,
            "dns_primary_ip": dns_primary_ip,
            "domain_name": domain_name,
            "domain_netbios_name": domain_netbios_name,
            "password": password,
            "username": username,
        }
        if dns_secondary_ip is not None:
            self._values["dns_secondary_ip"] = dns_secondary_ip

    @builtins.property
    def cache_netbios_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#cache_netbios_name HpcCache#cache_netbios_name}.'''
        result = self._values.get("cache_netbios_name")
        assert result is not None, "Required property 'cache_netbios_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dns_primary_ip(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#dns_primary_ip HpcCache#dns_primary_ip}.'''
        result = self._values.get("dns_primary_ip")
        assert result is not None, "Required property 'dns_primary_ip' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#domain_name HpcCache#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_netbios_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#domain_netbios_name HpcCache#domain_netbios_name}.'''
        result = self._values.get("domain_netbios_name")
        assert result is not None, "Required property 'domain_netbios_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#password HpcCache#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#username HpcCache#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dns_secondary_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#dns_secondary_ip HpcCache#dns_secondary_ip}.'''
        result = self._values.get("dns_secondary_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HpcCacheDirectoryActiveDirectory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HpcCacheDirectoryActiveDirectoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheDirectoryActiveDirectoryOutputReference",
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
            type_hints = typing.get_type_hints(HpcCacheDirectoryActiveDirectoryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDnsSecondaryIp")
    def reset_dns_secondary_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsSecondaryIp", []))

    @builtins.property
    @jsii.member(jsii_name="cacheNetbiosNameInput")
    def cache_netbios_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheNetbiosNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsPrimaryIpInput")
    def dns_primary_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsPrimaryIpInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsSecondaryIpInput")
    def dns_secondary_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsSecondaryIpInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNetbiosNameInput")
    def domain_netbios_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNetbiosNameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheNetbiosName")
    def cache_netbios_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheNetbiosName"))

    @cache_netbios_name.setter
    def cache_netbios_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryActiveDirectoryOutputReference, "cache_netbios_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheNetbiosName", value)

    @builtins.property
    @jsii.member(jsii_name="dnsPrimaryIp")
    def dns_primary_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsPrimaryIp"))

    @dns_primary_ip.setter
    def dns_primary_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryActiveDirectoryOutputReference, "dns_primary_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsPrimaryIp", value)

    @builtins.property
    @jsii.member(jsii_name="dnsSecondaryIp")
    def dns_secondary_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsSecondaryIp"))

    @dns_secondary_ip.setter
    def dns_secondary_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryActiveDirectoryOutputReference, "dns_secondary_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsSecondaryIp", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryActiveDirectoryOutputReference, "domain_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="domainNetbiosName")
    def domain_netbios_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainNetbiosName"))

    @domain_netbios_name.setter
    def domain_netbios_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryActiveDirectoryOutputReference, "domain_netbios_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainNetbiosName", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryActiveDirectoryOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryActiveDirectoryOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HpcCacheDirectoryActiveDirectory]:
        return typing.cast(typing.Optional[HpcCacheDirectoryActiveDirectory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HpcCacheDirectoryActiveDirectory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryActiveDirectoryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheDirectoryFlatFile",
    jsii_struct_bases=[],
    name_mapping={
        "group_file_uri": "groupFileUri",
        "password_file_uri": "passwordFileUri",
    },
)
class HpcCacheDirectoryFlatFile:
    def __init__(
        self,
        *,
        group_file_uri: builtins.str,
        password_file_uri: builtins.str,
    ) -> None:
        '''
        :param group_file_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#group_file_uri HpcCache#group_file_uri}.
        :param password_file_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#password_file_uri HpcCache#password_file_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HpcCacheDirectoryFlatFile.__init__)
            check_type(argname="argument group_file_uri", value=group_file_uri, expected_type=type_hints["group_file_uri"])
            check_type(argname="argument password_file_uri", value=password_file_uri, expected_type=type_hints["password_file_uri"])
        self._values: typing.Dict[str, typing.Any] = {
            "group_file_uri": group_file_uri,
            "password_file_uri": password_file_uri,
        }

    @builtins.property
    def group_file_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#group_file_uri HpcCache#group_file_uri}.'''
        result = self._values.get("group_file_uri")
        assert result is not None, "Required property 'group_file_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password_file_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#password_file_uri HpcCache#password_file_uri}.'''
        result = self._values.get("password_file_uri")
        assert result is not None, "Required property 'password_file_uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HpcCacheDirectoryFlatFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HpcCacheDirectoryFlatFileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheDirectoryFlatFileOutputReference",
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
            type_hints = typing.get_type_hints(HpcCacheDirectoryFlatFileOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="groupFileUriInput")
    def group_file_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupFileUriInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordFileUriInput")
    def password_file_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordFileUriInput"))

    @builtins.property
    @jsii.member(jsii_name="groupFileUri")
    def group_file_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupFileUri"))

    @group_file_uri.setter
    def group_file_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryFlatFileOutputReference, "group_file_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupFileUri", value)

    @builtins.property
    @jsii.member(jsii_name="passwordFileUri")
    def password_file_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passwordFileUri"))

    @password_file_uri.setter
    def password_file_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryFlatFileOutputReference, "password_file_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordFileUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HpcCacheDirectoryFlatFile]:
        return typing.cast(typing.Optional[HpcCacheDirectoryFlatFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[HpcCacheDirectoryFlatFile]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryFlatFileOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheDirectoryLdap",
    jsii_struct_bases=[],
    name_mapping={
        "base_dn": "baseDn",
        "server": "server",
        "bind": "bind",
        "certificate_validation_uri": "certificateValidationUri",
        "download_certificate_automatically": "downloadCertificateAutomatically",
        "encrypted": "encrypted",
    },
)
class HpcCacheDirectoryLdap:
    def __init__(
        self,
        *,
        base_dn: builtins.str,
        server: builtins.str,
        bind: typing.Optional[typing.Union["HpcCacheDirectoryLdapBind", typing.Dict[str, typing.Any]]] = None,
        certificate_validation_uri: typing.Optional[builtins.str] = None,
        download_certificate_automatically: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param base_dn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#base_dn HpcCache#base_dn}.
        :param server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#server HpcCache#server}.
        :param bind: bind block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#bind HpcCache#bind}
        :param certificate_validation_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#certificate_validation_uri HpcCache#certificate_validation_uri}.
        :param download_certificate_automatically: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#download_certificate_automatically HpcCache#download_certificate_automatically}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#encrypted HpcCache#encrypted}.
        '''
        if isinstance(bind, dict):
            bind = HpcCacheDirectoryLdapBind(**bind)
        if __debug__:
            type_hints = typing.get_type_hints(HpcCacheDirectoryLdap.__init__)
            check_type(argname="argument base_dn", value=base_dn, expected_type=type_hints["base_dn"])
            check_type(argname="argument server", value=server, expected_type=type_hints["server"])
            check_type(argname="argument bind", value=bind, expected_type=type_hints["bind"])
            check_type(argname="argument certificate_validation_uri", value=certificate_validation_uri, expected_type=type_hints["certificate_validation_uri"])
            check_type(argname="argument download_certificate_automatically", value=download_certificate_automatically, expected_type=type_hints["download_certificate_automatically"])
            check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
        self._values: typing.Dict[str, typing.Any] = {
            "base_dn": base_dn,
            "server": server,
        }
        if bind is not None:
            self._values["bind"] = bind
        if certificate_validation_uri is not None:
            self._values["certificate_validation_uri"] = certificate_validation_uri
        if download_certificate_automatically is not None:
            self._values["download_certificate_automatically"] = download_certificate_automatically
        if encrypted is not None:
            self._values["encrypted"] = encrypted

    @builtins.property
    def base_dn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#base_dn HpcCache#base_dn}.'''
        result = self._values.get("base_dn")
        assert result is not None, "Required property 'base_dn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#server HpcCache#server}.'''
        result = self._values.get("server")
        assert result is not None, "Required property 'server' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bind(self) -> typing.Optional["HpcCacheDirectoryLdapBind"]:
        '''bind block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#bind HpcCache#bind}
        '''
        result = self._values.get("bind")
        return typing.cast(typing.Optional["HpcCacheDirectoryLdapBind"], result)

    @builtins.property
    def certificate_validation_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#certificate_validation_uri HpcCache#certificate_validation_uri}.'''
        result = self._values.get("certificate_validation_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def download_certificate_automatically(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#download_certificate_automatically HpcCache#download_certificate_automatically}.'''
        result = self._values.get("download_certificate_automatically")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#encrypted HpcCache#encrypted}.'''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HpcCacheDirectoryLdap(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheDirectoryLdapBind",
    jsii_struct_bases=[],
    name_mapping={"dn": "dn", "password": "password"},
)
class HpcCacheDirectoryLdapBind:
    def __init__(self, *, dn: builtins.str, password: builtins.str) -> None:
        '''
        :param dn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#dn HpcCache#dn}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#password HpcCache#password}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HpcCacheDirectoryLdapBind.__init__)
            check_type(argname="argument dn", value=dn, expected_type=type_hints["dn"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
        self._values: typing.Dict[str, typing.Any] = {
            "dn": dn,
            "password": password,
        }

    @builtins.property
    def dn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#dn HpcCache#dn}.'''
        result = self._values.get("dn")
        assert result is not None, "Required property 'dn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#password HpcCache#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HpcCacheDirectoryLdapBind(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HpcCacheDirectoryLdapBindOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheDirectoryLdapBindOutputReference",
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
            type_hints = typing.get_type_hints(HpcCacheDirectoryLdapBindOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dnInput")
    def dn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="dn")
    def dn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dn"))

    @dn.setter
    def dn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryLdapBindOutputReference, "dn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dn", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryLdapBindOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HpcCacheDirectoryLdapBind]:
        return typing.cast(typing.Optional[HpcCacheDirectoryLdapBind], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[HpcCacheDirectoryLdapBind]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryLdapBindOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HpcCacheDirectoryLdapOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheDirectoryLdapOutputReference",
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
            type_hints = typing.get_type_hints(HpcCacheDirectoryLdapOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBind")
    def put_bind(self, *, dn: builtins.str, password: builtins.str) -> None:
        '''
        :param dn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#dn HpcCache#dn}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#password HpcCache#password}.
        '''
        value = HpcCacheDirectoryLdapBind(dn=dn, password=password)

        return typing.cast(None, jsii.invoke(self, "putBind", [value]))

    @jsii.member(jsii_name="resetBind")
    def reset_bind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBind", []))

    @jsii.member(jsii_name="resetCertificateValidationUri")
    def reset_certificate_validation_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateValidationUri", []))

    @jsii.member(jsii_name="resetDownloadCertificateAutomatically")
    def reset_download_certificate_automatically(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDownloadCertificateAutomatically", []))

    @jsii.member(jsii_name="resetEncrypted")
    def reset_encrypted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncrypted", []))

    @builtins.property
    @jsii.member(jsii_name="bind")
    def bind(self) -> HpcCacheDirectoryLdapBindOutputReference:
        return typing.cast(HpcCacheDirectoryLdapBindOutputReference, jsii.get(self, "bind"))

    @builtins.property
    @jsii.member(jsii_name="baseDnInput")
    def base_dn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "baseDnInput"))

    @builtins.property
    @jsii.member(jsii_name="bindInput")
    def bind_input(self) -> typing.Optional[HpcCacheDirectoryLdapBind]:
        return typing.cast(typing.Optional[HpcCacheDirectoryLdapBind], jsii.get(self, "bindInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateValidationUriInput")
    def certificate_validation_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateValidationUriInput"))

    @builtins.property
    @jsii.member(jsii_name="downloadCertificateAutomaticallyInput")
    def download_certificate_automatically_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "downloadCertificateAutomaticallyInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptedInput")
    def encrypted_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "encryptedInput"))

    @builtins.property
    @jsii.member(jsii_name="serverInput")
    def server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverInput"))

    @builtins.property
    @jsii.member(jsii_name="baseDn")
    def base_dn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baseDn"))

    @base_dn.setter
    def base_dn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryLdapOutputReference, "base_dn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseDn", value)

    @builtins.property
    @jsii.member(jsii_name="certificateValidationUri")
    def certificate_validation_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateValidationUri"))

    @certificate_validation_uri.setter
    def certificate_validation_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryLdapOutputReference, "certificate_validation_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateValidationUri", value)

    @builtins.property
    @jsii.member(jsii_name="downloadCertificateAutomatically")
    def download_certificate_automatically(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "downloadCertificateAutomatically"))

    @download_certificate_automatically.setter
    def download_certificate_automatically(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryLdapOutputReference, "download_certificate_automatically").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "downloadCertificateAutomatically", value)

    @builtins.property
    @jsii.member(jsii_name="encrypted")
    def encrypted(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "encrypted"))

    @encrypted.setter
    def encrypted(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryLdapOutputReference, "encrypted").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="server")
    def server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "server"))

    @server.setter
    def server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryLdapOutputReference, "server").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "server", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HpcCacheDirectoryLdap]:
        return typing.cast(typing.Optional[HpcCacheDirectoryLdap], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[HpcCacheDirectoryLdap]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDirectoryLdapOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheDns",
    jsii_struct_bases=[],
    name_mapping={"servers": "servers", "search_domain": "searchDomain"},
)
class HpcCacheDns:
    def __init__(
        self,
        *,
        servers: typing.Sequence[builtins.str],
        search_domain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#servers HpcCache#servers}.
        :param search_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#search_domain HpcCache#search_domain}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HpcCacheDns.__init__)
            check_type(argname="argument servers", value=servers, expected_type=type_hints["servers"])
            check_type(argname="argument search_domain", value=search_domain, expected_type=type_hints["search_domain"])
        self._values: typing.Dict[str, typing.Any] = {
            "servers": servers,
        }
        if search_domain is not None:
            self._values["search_domain"] = search_domain

    @builtins.property
    def servers(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#servers HpcCache#servers}.'''
        result = self._values.get("servers")
        assert result is not None, "Required property 'servers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def search_domain(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#search_domain HpcCache#search_domain}.'''
        result = self._values.get("search_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HpcCacheDns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HpcCacheDnsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheDnsOutputReference",
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
            type_hints = typing.get_type_hints(HpcCacheDnsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSearchDomain")
    def reset_search_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearchDomain", []))

    @builtins.property
    @jsii.member(jsii_name="searchDomainInput")
    def search_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "searchDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="serversInput")
    def servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serversInput"))

    @builtins.property
    @jsii.member(jsii_name="searchDomain")
    def search_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "searchDomain"))

    @search_domain.setter
    def search_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDnsOutputReference, "search_domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "searchDomain", value)

    @builtins.property
    @jsii.member(jsii_name="servers")
    def servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "servers"))

    @servers.setter
    def servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDnsOutputReference, "servers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HpcCacheDns]:
        return typing.cast(typing.Optional[HpcCacheDns], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[HpcCacheDns]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheDnsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheIdentity",
    jsii_struct_bases=[],
    name_mapping={"identity_ids": "identityIds", "type": "type"},
)
class HpcCacheIdentity:
    def __init__(
        self,
        *,
        identity_ids: typing.Sequence[builtins.str],
        type: builtins.str,
    ) -> None:
        '''
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#identity_ids HpcCache#identity_ids}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#type HpcCache#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HpcCacheIdentity.__init__)
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "identity_ids": identity_ids,
            "type": type,
        }

    @builtins.property
    def identity_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#identity_ids HpcCache#identity_ids}.'''
        result = self._values.get("identity_ids")
        assert result is not None, "Required property 'identity_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#type HpcCache#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HpcCacheIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HpcCacheIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheIdentityOutputReference",
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
            type_hints = typing.get_type_hints(HpcCacheIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="identityIdsInput")
    def identity_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identityIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="identityIds")
    def identity_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identityIds"))

    @identity_ids.setter
    def identity_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HpcCacheIdentity]:
        return typing.cast(typing.Optional[HpcCacheIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[HpcCacheIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class HpcCacheTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#create HpcCache#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#delete HpcCache#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#read HpcCache#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#update HpcCache#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HpcCacheTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#create HpcCache#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#delete HpcCache#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#read HpcCache#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hpc_cache#update HpcCache#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HpcCacheTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HpcCacheTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hpcCache.HpcCacheTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(HpcCacheTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(HpcCacheTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HpcCacheTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HpcCacheTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HpcCacheTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HpcCacheTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "HpcCache",
    "HpcCacheConfig",
    "HpcCacheDefaultAccessPolicy",
    "HpcCacheDefaultAccessPolicyAccessRule",
    "HpcCacheDefaultAccessPolicyAccessRuleList",
    "HpcCacheDefaultAccessPolicyAccessRuleOutputReference",
    "HpcCacheDefaultAccessPolicyOutputReference",
    "HpcCacheDirectoryActiveDirectory",
    "HpcCacheDirectoryActiveDirectoryOutputReference",
    "HpcCacheDirectoryFlatFile",
    "HpcCacheDirectoryFlatFileOutputReference",
    "HpcCacheDirectoryLdap",
    "HpcCacheDirectoryLdapBind",
    "HpcCacheDirectoryLdapBindOutputReference",
    "HpcCacheDirectoryLdapOutputReference",
    "HpcCacheDns",
    "HpcCacheDnsOutputReference",
    "HpcCacheIdentity",
    "HpcCacheIdentityOutputReference",
    "HpcCacheTimeouts",
    "HpcCacheTimeoutsOutputReference",
]

publication.publish()
