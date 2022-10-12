'''
# `azurerm_container_group`

Refer to the Terraform Registory for docs: [`azurerm_container_group`](https://www.terraform.io/docs/providers/azurerm/r/container_group).
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


class ContainerGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/container_group azurerm_container_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        container: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupContainer", typing.Dict[str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        os_type: builtins.str,
        resource_group_name: builtins.str,
        diagnostics: typing.Optional[typing.Union["ContainerGroupDiagnostics", typing.Dict[str, typing.Any]]] = None,
        dns_config: typing.Optional[typing.Union["ContainerGroupDnsConfig", typing.Dict[str, typing.Any]]] = None,
        dns_name_label: typing.Optional[builtins.str] = None,
        exposed_port: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupExposedPort", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["ContainerGroupIdentity", typing.Dict[str, typing.Any]]] = None,
        image_registry_credential: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupImageRegistryCredential", typing.Dict[str, typing.Any]]]]] = None,
        init_container: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupInitContainer", typing.Dict[str, typing.Any]]]]] = None,
        ip_address_type: typing.Optional[builtins.str] = None,
        key_vault_key_id: typing.Optional[builtins.str] = None,
        network_profile_id: typing.Optional[builtins.str] = None,
        restart_policy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ContainerGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/container_group azurerm_container_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param container: container block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#container ContainerGroup#container}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#location ContainerGroup#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#name ContainerGroup#name}.
        :param os_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#os_type ContainerGroup#os_type}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#resource_group_name ContainerGroup#resource_group_name}.
        :param diagnostics: diagnostics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#diagnostics ContainerGroup#diagnostics}
        :param dns_config: dns_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#dns_config ContainerGroup#dns_config}
        :param dns_name_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#dns_name_label ContainerGroup#dns_name_label}.
        :param exposed_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#exposed_port ContainerGroup#exposed_port}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#id ContainerGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#identity ContainerGroup#identity}
        :param image_registry_credential: image_registry_credential block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#image_registry_credential ContainerGroup#image_registry_credential}
        :param init_container: init_container block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#init_container ContainerGroup#init_container}
        :param ip_address_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#ip_address_type ContainerGroup#ip_address_type}.
        :param key_vault_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#key_vault_key_id ContainerGroup#key_vault_key_id}.
        :param network_profile_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#network_profile_id ContainerGroup#network_profile_id}.
        :param restart_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#restart_policy ContainerGroup#restart_policy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#tags ContainerGroup#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#timeouts ContainerGroup#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ContainerGroupConfig(
            container=container,
            location=location,
            name=name,
            os_type=os_type,
            resource_group_name=resource_group_name,
            diagnostics=diagnostics,
            dns_config=dns_config,
            dns_name_label=dns_name_label,
            exposed_port=exposed_port,
            id=id,
            identity=identity,
            image_registry_credential=image_registry_credential,
            init_container=init_container,
            ip_address_type=ip_address_type,
            key_vault_key_id=key_vault_key_id,
            network_profile_id=network_profile_id,
            restart_policy=restart_policy,
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

    @jsii.member(jsii_name="putContainer")
    def put_container(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupContainer", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroup.put_container)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putContainer", [value]))

    @jsii.member(jsii_name="putDiagnostics")
    def put_diagnostics(
        self,
        *,
        log_analytics: typing.Union["ContainerGroupDiagnosticsLogAnalytics", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param log_analytics: log_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#log_analytics ContainerGroup#log_analytics}
        '''
        value = ContainerGroupDiagnostics(log_analytics=log_analytics)

        return typing.cast(None, jsii.invoke(self, "putDiagnostics", [value]))

    @jsii.member(jsii_name="putDnsConfig")
    def put_dns_config(
        self,
        *,
        nameservers: typing.Sequence[builtins.str],
        options: typing.Optional[typing.Sequence[builtins.str]] = None,
        search_domains: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param nameservers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#nameservers ContainerGroup#nameservers}.
        :param options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#options ContainerGroup#options}.
        :param search_domains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#search_domains ContainerGroup#search_domains}.
        '''
        value = ContainerGroupDnsConfig(
            nameservers=nameservers, options=options, search_domains=search_domains
        )

        return typing.cast(None, jsii.invoke(self, "putDnsConfig", [value]))

    @jsii.member(jsii_name="putExposedPort")
    def put_exposed_port(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupExposedPort", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroup.put_exposed_port)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExposedPort", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#type ContainerGroup#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#identity_ids ContainerGroup#identity_ids}.
        '''
        value = ContainerGroupIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putImageRegistryCredential")
    def put_image_registry_credential(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupImageRegistryCredential", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroup.put_image_registry_credential)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putImageRegistryCredential", [value]))

    @jsii.member(jsii_name="putInitContainer")
    def put_init_container(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupInitContainer", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroup.put_init_container)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInitContainer", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#create ContainerGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#delete ContainerGroup#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#read ContainerGroup#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#update ContainerGroup#update}.
        '''
        value = ContainerGroupTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDiagnostics")
    def reset_diagnostics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiagnostics", []))

    @jsii.member(jsii_name="resetDnsConfig")
    def reset_dns_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsConfig", []))

    @jsii.member(jsii_name="resetDnsNameLabel")
    def reset_dns_name_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsNameLabel", []))

    @jsii.member(jsii_name="resetExposedPort")
    def reset_exposed_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExposedPort", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetImageRegistryCredential")
    def reset_image_registry_credential(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageRegistryCredential", []))

    @jsii.member(jsii_name="resetInitContainer")
    def reset_init_container(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitContainer", []))

    @jsii.member(jsii_name="resetIpAddressType")
    def reset_ip_address_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddressType", []))

    @jsii.member(jsii_name="resetKeyVaultKeyId")
    def reset_key_vault_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultKeyId", []))

    @jsii.member(jsii_name="resetNetworkProfileId")
    def reset_network_profile_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkProfileId", []))

    @jsii.member(jsii_name="resetRestartPolicy")
    def reset_restart_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestartPolicy", []))

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
    @jsii.member(jsii_name="container")
    def container(self) -> "ContainerGroupContainerList":
        return typing.cast("ContainerGroupContainerList", jsii.get(self, "container"))

    @builtins.property
    @jsii.member(jsii_name="diagnostics")
    def diagnostics(self) -> "ContainerGroupDiagnosticsOutputReference":
        return typing.cast("ContainerGroupDiagnosticsOutputReference", jsii.get(self, "diagnostics"))

    @builtins.property
    @jsii.member(jsii_name="dnsConfig")
    def dns_config(self) -> "ContainerGroupDnsConfigOutputReference":
        return typing.cast("ContainerGroupDnsConfigOutputReference", jsii.get(self, "dnsConfig"))

    @builtins.property
    @jsii.member(jsii_name="exposedPort")
    def exposed_port(self) -> "ContainerGroupExposedPortList":
        return typing.cast("ContainerGroupExposedPortList", jsii.get(self, "exposedPort"))

    @builtins.property
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fqdn"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "ContainerGroupIdentityOutputReference":
        return typing.cast("ContainerGroupIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="imageRegistryCredential")
    def image_registry_credential(self) -> "ContainerGroupImageRegistryCredentialList":
        return typing.cast("ContainerGroupImageRegistryCredentialList", jsii.get(self, "imageRegistryCredential"))

    @builtins.property
    @jsii.member(jsii_name="initContainer")
    def init_container(self) -> "ContainerGroupInitContainerList":
        return typing.cast("ContainerGroupInitContainerList", jsii.get(self, "initContainer"))

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ContainerGroupTimeoutsOutputReference":
        return typing.cast("ContainerGroupTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="containerInput")
    def container_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupContainer"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupContainer"]]], jsii.get(self, "containerInput"))

    @builtins.property
    @jsii.member(jsii_name="diagnosticsInput")
    def diagnostics_input(self) -> typing.Optional["ContainerGroupDiagnostics"]:
        return typing.cast(typing.Optional["ContainerGroupDiagnostics"], jsii.get(self, "diagnosticsInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsConfigInput")
    def dns_config_input(self) -> typing.Optional["ContainerGroupDnsConfig"]:
        return typing.cast(typing.Optional["ContainerGroupDnsConfig"], jsii.get(self, "dnsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsNameLabelInput")
    def dns_name_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsNameLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="exposedPortInput")
    def exposed_port_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupExposedPort"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupExposedPort"]]], jsii.get(self, "exposedPortInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["ContainerGroupIdentity"]:
        return typing.cast(typing.Optional["ContainerGroupIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="imageRegistryCredentialInput")
    def image_registry_credential_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupImageRegistryCredential"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupImageRegistryCredential"]]], jsii.get(self, "imageRegistryCredentialInput"))

    @builtins.property
    @jsii.member(jsii_name="initContainerInput")
    def init_container_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupInitContainer"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupInitContainer"]]], jsii.get(self, "initContainerInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressTypeInput")
    def ip_address_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultKeyIdInput")
    def key_vault_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkProfileIdInput")
    def network_profile_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkProfileIdInput"))

    @builtins.property
    @jsii.member(jsii_name="osTypeInput")
    def os_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="restartPolicyInput")
    def restart_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restartPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ContainerGroupTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ContainerGroupTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsNameLabel")
    def dns_name_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsNameLabel"))

    @dns_name_label.setter
    def dns_name_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroup, "dns_name_label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsNameLabel", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddressType")
    def ip_address_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddressType"))

    @ip_address_type.setter
    def ip_address_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroup, "ip_address_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddressType", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultKeyId")
    def key_vault_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultKeyId"))

    @key_vault_key_id.setter
    def key_vault_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroup, "key_vault_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroup, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroup, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkProfileId")
    def network_profile_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkProfileId"))

    @network_profile_id.setter
    def network_profile_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroup, "network_profile_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkProfileId", value)

    @builtins.property
    @jsii.member(jsii_name="osType")
    def os_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "osType"))

    @os_type.setter
    def os_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroup, "os_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroup, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="restartPolicy")
    def restart_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restartPolicy"))

    @restart_policy.setter
    def restart_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroup, "restart_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restartPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroup, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "container": "container",
        "location": "location",
        "name": "name",
        "os_type": "osType",
        "resource_group_name": "resourceGroupName",
        "diagnostics": "diagnostics",
        "dns_config": "dnsConfig",
        "dns_name_label": "dnsNameLabel",
        "exposed_port": "exposedPort",
        "id": "id",
        "identity": "identity",
        "image_registry_credential": "imageRegistryCredential",
        "init_container": "initContainer",
        "ip_address_type": "ipAddressType",
        "key_vault_key_id": "keyVaultKeyId",
        "network_profile_id": "networkProfileId",
        "restart_policy": "restartPolicy",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class ContainerGroupConfig(cdktf.TerraformMetaArguments):
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
        container: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupContainer", typing.Dict[str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        os_type: builtins.str,
        resource_group_name: builtins.str,
        diagnostics: typing.Optional[typing.Union["ContainerGroupDiagnostics", typing.Dict[str, typing.Any]]] = None,
        dns_config: typing.Optional[typing.Union["ContainerGroupDnsConfig", typing.Dict[str, typing.Any]]] = None,
        dns_name_label: typing.Optional[builtins.str] = None,
        exposed_port: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupExposedPort", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["ContainerGroupIdentity", typing.Dict[str, typing.Any]]] = None,
        image_registry_credential: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupImageRegistryCredential", typing.Dict[str, typing.Any]]]]] = None,
        init_container: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupInitContainer", typing.Dict[str, typing.Any]]]]] = None,
        ip_address_type: typing.Optional[builtins.str] = None,
        key_vault_key_id: typing.Optional[builtins.str] = None,
        network_profile_id: typing.Optional[builtins.str] = None,
        restart_policy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ContainerGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param container: container block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#container ContainerGroup#container}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#location ContainerGroup#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#name ContainerGroup#name}.
        :param os_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#os_type ContainerGroup#os_type}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#resource_group_name ContainerGroup#resource_group_name}.
        :param diagnostics: diagnostics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#diagnostics ContainerGroup#diagnostics}
        :param dns_config: dns_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#dns_config ContainerGroup#dns_config}
        :param dns_name_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#dns_name_label ContainerGroup#dns_name_label}.
        :param exposed_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#exposed_port ContainerGroup#exposed_port}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#id ContainerGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#identity ContainerGroup#identity}
        :param image_registry_credential: image_registry_credential block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#image_registry_credential ContainerGroup#image_registry_credential}
        :param init_container: init_container block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#init_container ContainerGroup#init_container}
        :param ip_address_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#ip_address_type ContainerGroup#ip_address_type}.
        :param key_vault_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#key_vault_key_id ContainerGroup#key_vault_key_id}.
        :param network_profile_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#network_profile_id ContainerGroup#network_profile_id}.
        :param restart_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#restart_policy ContainerGroup#restart_policy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#tags ContainerGroup#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#timeouts ContainerGroup#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(diagnostics, dict):
            diagnostics = ContainerGroupDiagnostics(**diagnostics)
        if isinstance(dns_config, dict):
            dns_config = ContainerGroupDnsConfig(**dns_config)
        if isinstance(identity, dict):
            identity = ContainerGroupIdentity(**identity)
        if isinstance(timeouts, dict):
            timeouts = ContainerGroupTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument os_type", value=os_type, expected_type=type_hints["os_type"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument diagnostics", value=diagnostics, expected_type=type_hints["diagnostics"])
            check_type(argname="argument dns_config", value=dns_config, expected_type=type_hints["dns_config"])
            check_type(argname="argument dns_name_label", value=dns_name_label, expected_type=type_hints["dns_name_label"])
            check_type(argname="argument exposed_port", value=exposed_port, expected_type=type_hints["exposed_port"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument image_registry_credential", value=image_registry_credential, expected_type=type_hints["image_registry_credential"])
            check_type(argname="argument init_container", value=init_container, expected_type=type_hints["init_container"])
            check_type(argname="argument ip_address_type", value=ip_address_type, expected_type=type_hints["ip_address_type"])
            check_type(argname="argument key_vault_key_id", value=key_vault_key_id, expected_type=type_hints["key_vault_key_id"])
            check_type(argname="argument network_profile_id", value=network_profile_id, expected_type=type_hints["network_profile_id"])
            check_type(argname="argument restart_policy", value=restart_policy, expected_type=type_hints["restart_policy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "container": container,
            "location": location,
            "name": name,
            "os_type": os_type,
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
        if diagnostics is not None:
            self._values["diagnostics"] = diagnostics
        if dns_config is not None:
            self._values["dns_config"] = dns_config
        if dns_name_label is not None:
            self._values["dns_name_label"] = dns_name_label
        if exposed_port is not None:
            self._values["exposed_port"] = exposed_port
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if image_registry_credential is not None:
            self._values["image_registry_credential"] = image_registry_credential
        if init_container is not None:
            self._values["init_container"] = init_container
        if ip_address_type is not None:
            self._values["ip_address_type"] = ip_address_type
        if key_vault_key_id is not None:
            self._values["key_vault_key_id"] = key_vault_key_id
        if network_profile_id is not None:
            self._values["network_profile_id"] = network_profile_id
        if restart_policy is not None:
            self._values["restart_policy"] = restart_policy
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
    def container(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ContainerGroupContainer"]]:
        '''container block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#container ContainerGroup#container}
        '''
        result = self._values.get("container")
        assert result is not None, "Required property 'container' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ContainerGroupContainer"]], result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#location ContainerGroup#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#name ContainerGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def os_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#os_type ContainerGroup#os_type}.'''
        result = self._values.get("os_type")
        assert result is not None, "Required property 'os_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#resource_group_name ContainerGroup#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def diagnostics(self) -> typing.Optional["ContainerGroupDiagnostics"]:
        '''diagnostics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#diagnostics ContainerGroup#diagnostics}
        '''
        result = self._values.get("diagnostics")
        return typing.cast(typing.Optional["ContainerGroupDiagnostics"], result)

    @builtins.property
    def dns_config(self) -> typing.Optional["ContainerGroupDnsConfig"]:
        '''dns_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#dns_config ContainerGroup#dns_config}
        '''
        result = self._values.get("dns_config")
        return typing.cast(typing.Optional["ContainerGroupDnsConfig"], result)

    @builtins.property
    def dns_name_label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#dns_name_label ContainerGroup#dns_name_label}.'''
        result = self._values.get("dns_name_label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exposed_port(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupExposedPort"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#exposed_port ContainerGroup#exposed_port}.'''
        result = self._values.get("exposed_port")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupExposedPort"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#id ContainerGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["ContainerGroupIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#identity ContainerGroup#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["ContainerGroupIdentity"], result)

    @builtins.property
    def image_registry_credential(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupImageRegistryCredential"]]]:
        '''image_registry_credential block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#image_registry_credential ContainerGroup#image_registry_credential}
        '''
        result = self._values.get("image_registry_credential")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupImageRegistryCredential"]]], result)

    @builtins.property
    def init_container(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupInitContainer"]]]:
        '''init_container block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#init_container ContainerGroup#init_container}
        '''
        result = self._values.get("init_container")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupInitContainer"]]], result)

    @builtins.property
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#ip_address_type ContainerGroup#ip_address_type}.'''
        result = self._values.get("ip_address_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_vault_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#key_vault_key_id ContainerGroup#key_vault_key_id}.'''
        result = self._values.get("key_vault_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_profile_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#network_profile_id ContainerGroup#network_profile_id}.'''
        result = self._values.get("network_profile_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restart_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#restart_policy ContainerGroup#restart_policy}.'''
        result = self._values.get("restart_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#tags ContainerGroup#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ContainerGroupTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#timeouts ContainerGroup#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ContainerGroupTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainer",
    jsii_struct_bases=[],
    name_mapping={
        "cpu": "cpu",
        "image": "image",
        "memory": "memory",
        "name": "name",
        "commands": "commands",
        "cpu_limit": "cpuLimit",
        "environment_variables": "environmentVariables",
        "gpu": "gpu",
        "gpu_limit": "gpuLimit",
        "liveness_probe": "livenessProbe",
        "memory_limit": "memoryLimit",
        "ports": "ports",
        "readiness_probe": "readinessProbe",
        "secure_environment_variables": "secureEnvironmentVariables",
        "volume": "volume",
    },
)
class ContainerGroupContainer:
    def __init__(
        self,
        *,
        cpu: jsii.Number,
        image: builtins.str,
        memory: jsii.Number,
        name: builtins.str,
        commands: typing.Optional[typing.Sequence[builtins.str]] = None,
        cpu_limit: typing.Optional[jsii.Number] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        gpu: typing.Optional[typing.Union["ContainerGroupContainerGpu", typing.Dict[str, typing.Any]]] = None,
        gpu_limit: typing.Optional[typing.Union["ContainerGroupContainerGpuLimit", typing.Dict[str, typing.Any]]] = None,
        liveness_probe: typing.Optional[typing.Union["ContainerGroupContainerLivenessProbe", typing.Dict[str, typing.Any]]] = None,
        memory_limit: typing.Optional[jsii.Number] = None,
        ports: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupContainerPorts", typing.Dict[str, typing.Any]]]]] = None,
        readiness_probe: typing.Optional[typing.Union["ContainerGroupContainerReadinessProbe", typing.Dict[str, typing.Any]]] = None,
        secure_environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        volume: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupContainerVolume", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#cpu ContainerGroup#cpu}.
        :param image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#image ContainerGroup#image}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#memory ContainerGroup#memory}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#name ContainerGroup#name}.
        :param commands: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#commands ContainerGroup#commands}.
        :param cpu_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#cpu_limit ContainerGroup#cpu_limit}.
        :param environment_variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#environment_variables ContainerGroup#environment_variables}.
        :param gpu: gpu block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#gpu ContainerGroup#gpu}
        :param gpu_limit: gpu_limit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#gpu_limit ContainerGroup#gpu_limit}
        :param liveness_probe: liveness_probe block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#liveness_probe ContainerGroup#liveness_probe}
        :param memory_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#memory_limit ContainerGroup#memory_limit}.
        :param ports: ports block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#ports ContainerGroup#ports}
        :param readiness_probe: readiness_probe block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#readiness_probe ContainerGroup#readiness_probe}
        :param secure_environment_variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#secure_environment_variables ContainerGroup#secure_environment_variables}.
        :param volume: volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#volume ContainerGroup#volume}
        '''
        if isinstance(gpu, dict):
            gpu = ContainerGroupContainerGpu(**gpu)
        if isinstance(gpu_limit, dict):
            gpu_limit = ContainerGroupContainerGpuLimit(**gpu_limit)
        if isinstance(liveness_probe, dict):
            liveness_probe = ContainerGroupContainerLivenessProbe(**liveness_probe)
        if isinstance(readiness_probe, dict):
            readiness_probe = ContainerGroupContainerReadinessProbe(**readiness_probe)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainer.__init__)
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument commands", value=commands, expected_type=type_hints["commands"])
            check_type(argname="argument cpu_limit", value=cpu_limit, expected_type=type_hints["cpu_limit"])
            check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
            check_type(argname="argument gpu", value=gpu, expected_type=type_hints["gpu"])
            check_type(argname="argument gpu_limit", value=gpu_limit, expected_type=type_hints["gpu_limit"])
            check_type(argname="argument liveness_probe", value=liveness_probe, expected_type=type_hints["liveness_probe"])
            check_type(argname="argument memory_limit", value=memory_limit, expected_type=type_hints["memory_limit"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
            check_type(argname="argument readiness_probe", value=readiness_probe, expected_type=type_hints["readiness_probe"])
            check_type(argname="argument secure_environment_variables", value=secure_environment_variables, expected_type=type_hints["secure_environment_variables"])
            check_type(argname="argument volume", value=volume, expected_type=type_hints["volume"])
        self._values: typing.Dict[str, typing.Any] = {
            "cpu": cpu,
            "image": image,
            "memory": memory,
            "name": name,
        }
        if commands is not None:
            self._values["commands"] = commands
        if cpu_limit is not None:
            self._values["cpu_limit"] = cpu_limit
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if gpu is not None:
            self._values["gpu"] = gpu
        if gpu_limit is not None:
            self._values["gpu_limit"] = gpu_limit
        if liveness_probe is not None:
            self._values["liveness_probe"] = liveness_probe
        if memory_limit is not None:
            self._values["memory_limit"] = memory_limit
        if ports is not None:
            self._values["ports"] = ports
        if readiness_probe is not None:
            self._values["readiness_probe"] = readiness_probe
        if secure_environment_variables is not None:
            self._values["secure_environment_variables"] = secure_environment_variables
        if volume is not None:
            self._values["volume"] = volume

    @builtins.property
    def cpu(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#cpu ContainerGroup#cpu}.'''
        result = self._values.get("cpu")
        assert result is not None, "Required property 'cpu' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def image(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#image ContainerGroup#image}.'''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def memory(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#memory ContainerGroup#memory}.'''
        result = self._values.get("memory")
        assert result is not None, "Required property 'memory' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#name ContainerGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def commands(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#commands ContainerGroup#commands}.'''
        result = self._values.get("commands")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cpu_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#cpu_limit ContainerGroup#cpu_limit}.'''
        result = self._values.get("cpu_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#environment_variables ContainerGroup#environment_variables}.'''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def gpu(self) -> typing.Optional["ContainerGroupContainerGpu"]:
        '''gpu block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#gpu ContainerGroup#gpu}
        '''
        result = self._values.get("gpu")
        return typing.cast(typing.Optional["ContainerGroupContainerGpu"], result)

    @builtins.property
    def gpu_limit(self) -> typing.Optional["ContainerGroupContainerGpuLimit"]:
        '''gpu_limit block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#gpu_limit ContainerGroup#gpu_limit}
        '''
        result = self._values.get("gpu_limit")
        return typing.cast(typing.Optional["ContainerGroupContainerGpuLimit"], result)

    @builtins.property
    def liveness_probe(self) -> typing.Optional["ContainerGroupContainerLivenessProbe"]:
        '''liveness_probe block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#liveness_probe ContainerGroup#liveness_probe}
        '''
        result = self._values.get("liveness_probe")
        return typing.cast(typing.Optional["ContainerGroupContainerLivenessProbe"], result)

    @builtins.property
    def memory_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#memory_limit ContainerGroup#memory_limit}.'''
        result = self._values.get("memory_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ports(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupContainerPorts"]]]:
        '''ports block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#ports ContainerGroup#ports}
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupContainerPorts"]]], result)

    @builtins.property
    def readiness_probe(
        self,
    ) -> typing.Optional["ContainerGroupContainerReadinessProbe"]:
        '''readiness_probe block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#readiness_probe ContainerGroup#readiness_probe}
        '''
        result = self._values.get("readiness_probe")
        return typing.cast(typing.Optional["ContainerGroupContainerReadinessProbe"], result)

    @builtins.property
    def secure_environment_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#secure_environment_variables ContainerGroup#secure_environment_variables}.'''
        result = self._values.get("secure_environment_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def volume(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupContainerVolume"]]]:
        '''volume block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#volume ContainerGroup#volume}
        '''
        result = self._values.get("volume")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupContainerVolume"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupContainer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerGpu",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "sku": "sku"},
)
class ContainerGroupContainerGpu:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        sku: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#count ContainerGroup#count}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#sku ContainerGroup#sku}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainerGpu.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if sku is not None:
            self._values["sku"] = sku

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#count ContainerGroup#count}.'''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sku(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#sku ContainerGroup#sku}.'''
        result = self._values.get("sku")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupContainerGpu(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerGpuLimit",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "sku": "sku"},
)
class ContainerGroupContainerGpuLimit:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        sku: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#count ContainerGroup#count}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#sku ContainerGroup#sku}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainerGpuLimit.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if sku is not None:
            self._values["sku"] = sku

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#count ContainerGroup#count}.'''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sku(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#sku ContainerGroup#sku}.'''
        result = self._values.get("sku")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupContainerGpuLimit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerGroupContainerGpuLimitOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerGpuLimitOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupContainerGpuLimitOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetSku")
    def reset_sku(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSku", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerGpuLimitOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerGpuLimitOutputReference, "sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerGroupContainerGpuLimit]:
        return typing.cast(typing.Optional[ContainerGroupContainerGpuLimit], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerGroupContainerGpuLimit],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerGpuLimitOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerGroupContainerGpuOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerGpuOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupContainerGpuOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetSku")
    def reset_sku(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSku", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerGpuOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerGpuOutputReference, "sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerGroupContainerGpu]:
        return typing.cast(typing.Optional[ContainerGroupContainerGpu], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerGroupContainerGpu],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerGpuOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerGroupContainerList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerList",
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
            type_hints = typing.get_type_hints(ContainerGroupContainerList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerGroupContainerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainerList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerGroupContainerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainer]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainer]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainer]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerLivenessProbe",
    jsii_struct_bases=[],
    name_mapping={
        "exec": "exec",
        "failure_threshold": "failureThreshold",
        "http_get": "httpGet",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "success_threshold": "successThreshold",
        "timeout_seconds": "timeoutSeconds",
    },
)
class ContainerGroupContainerLivenessProbe:
    def __init__(
        self,
        *,
        exec: typing.Optional[typing.Sequence[builtins.str]] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        http_get: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupContainerLivenessProbeHttpGet", typing.Dict[str, typing.Any]]]]] = None,
        initial_delay_seconds: typing.Optional[jsii.Number] = None,
        period_seconds: typing.Optional[jsii.Number] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param exec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#exec ContainerGroup#exec}.
        :param failure_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#failure_threshold ContainerGroup#failure_threshold}.
        :param http_get: http_get block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#http_get ContainerGroup#http_get}
        :param initial_delay_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#initial_delay_seconds ContainerGroup#initial_delay_seconds}.
        :param period_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#period_seconds ContainerGroup#period_seconds}.
        :param success_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#success_threshold ContainerGroup#success_threshold}.
        :param timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#timeout_seconds ContainerGroup#timeout_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainerLivenessProbe.__init__)
            check_type(argname="argument exec", value=exec, expected_type=type_hints["exec"])
            check_type(argname="argument failure_threshold", value=failure_threshold, expected_type=type_hints["failure_threshold"])
            check_type(argname="argument http_get", value=http_get, expected_type=type_hints["http_get"])
            check_type(argname="argument initial_delay_seconds", value=initial_delay_seconds, expected_type=type_hints["initial_delay_seconds"])
            check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
            check_type(argname="argument success_threshold", value=success_threshold, expected_type=type_hints["success_threshold"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if exec is not None:
            self._values["exec"] = exec
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if http_get is not None:
            self._values["http_get"] = http_get
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def exec(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#exec ContainerGroup#exec}.'''
        result = self._values.get("exec")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#failure_threshold ContainerGroup#failure_threshold}.'''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def http_get(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupContainerLivenessProbeHttpGet"]]]:
        '''http_get block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#http_get ContainerGroup#http_get}
        '''
        result = self._values.get("http_get")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupContainerLivenessProbeHttpGet"]]], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#initial_delay_seconds ContainerGroup#initial_delay_seconds}.'''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#period_seconds ContainerGroup#period_seconds}.'''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#success_threshold ContainerGroup#success_threshold}.'''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#timeout_seconds ContainerGroup#timeout_seconds}.'''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupContainerLivenessProbe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerLivenessProbeHttpGet",
    jsii_struct_bases=[],
    name_mapping={
        "http_headers": "httpHeaders",
        "path": "path",
        "port": "port",
        "scheme": "scheme",
    },
)
class ContainerGroupContainerLivenessProbeHttpGet:
    def __init__(
        self,
        *,
        http_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        scheme: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#http_headers ContainerGroup#http_headers}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#path ContainerGroup#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#port ContainerGroup#port}.
        :param scheme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#scheme ContainerGroup#scheme}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainerLivenessProbeHttpGet.__init__)
            check_type(argname="argument http_headers", value=http_headers, expected_type=type_hints["http_headers"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument scheme", value=scheme, expected_type=type_hints["scheme"])
        self._values: typing.Dict[str, typing.Any] = {}
        if http_headers is not None:
            self._values["http_headers"] = http_headers
        if path is not None:
            self._values["path"] = path
        if port is not None:
            self._values["port"] = port
        if scheme is not None:
            self._values["scheme"] = scheme

    @builtins.property
    def http_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#http_headers ContainerGroup#http_headers}.'''
        result = self._values.get("http_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#path ContainerGroup#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#port ContainerGroup#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scheme(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#scheme ContainerGroup#scheme}.'''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupContainerLivenessProbeHttpGet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerGroupContainerLivenessProbeHttpGetList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerLivenessProbeHttpGetList",
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
            type_hints = typing.get_type_hints(ContainerGroupContainerLivenessProbeHttpGetList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ContainerGroupContainerLivenessProbeHttpGetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainerLivenessProbeHttpGetList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerGroupContainerLivenessProbeHttpGetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerLivenessProbeHttpGetList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerLivenessProbeHttpGetList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerLivenessProbeHttpGetList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainerLivenessProbeHttpGet]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainerLivenessProbeHttpGet]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainerLivenessProbeHttpGet]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerLivenessProbeHttpGetList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerGroupContainerLivenessProbeHttpGetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerLivenessProbeHttpGetOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupContainerLivenessProbeHttpGetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetHttpHeaders")
    def reset_http_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpHeaders", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetScheme")
    def reset_scheme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheme", []))

    @builtins.property
    @jsii.member(jsii_name="httpHeadersInput")
    def http_headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "httpHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="schemeInput")
    def scheme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemeInput"))

    @builtins.property
    @jsii.member(jsii_name="httpHeaders")
    def http_headers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "httpHeaders"))

    @http_headers.setter
    def http_headers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerLivenessProbeHttpGetOutputReference, "http_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerLivenessProbeHttpGetOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerLivenessProbeHttpGetOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="scheme")
    def scheme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheme"))

    @scheme.setter
    def scheme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerLivenessProbeHttpGetOutputReference, "scheme").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheme", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerGroupContainerLivenessProbeHttpGet, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerGroupContainerLivenessProbeHttpGet, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerGroupContainerLivenessProbeHttpGet, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerLivenessProbeHttpGetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerGroupContainerLivenessProbeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerLivenessProbeOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupContainerLivenessProbeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHttpGet")
    def put_http_get(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ContainerGroupContainerLivenessProbeHttpGet, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainerLivenessProbeOutputReference.put_http_get)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHttpGet", [value]))

    @jsii.member(jsii_name="resetExec")
    def reset_exec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExec", []))

    @jsii.member(jsii_name="resetFailureThreshold")
    def reset_failure_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailureThreshold", []))

    @jsii.member(jsii_name="resetHttpGet")
    def reset_http_get(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpGet", []))

    @jsii.member(jsii_name="resetInitialDelaySeconds")
    def reset_initial_delay_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialDelaySeconds", []))

    @jsii.member(jsii_name="resetPeriodSeconds")
    def reset_period_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriodSeconds", []))

    @jsii.member(jsii_name="resetSuccessThreshold")
    def reset_success_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuccessThreshold", []))

    @jsii.member(jsii_name="resetTimeoutSeconds")
    def reset_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="httpGet")
    def http_get(self) -> ContainerGroupContainerLivenessProbeHttpGetList:
        return typing.cast(ContainerGroupContainerLivenessProbeHttpGetList, jsii.get(self, "httpGet"))

    @builtins.property
    @jsii.member(jsii_name="execInput")
    def exec_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "execInput"))

    @builtins.property
    @jsii.member(jsii_name="failureThresholdInput")
    def failure_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "failureThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="httpGetInput")
    def http_get_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainerLivenessProbeHttpGet]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainerLivenessProbeHttpGet]]], jsii.get(self, "httpGetInput"))

    @builtins.property
    @jsii.member(jsii_name="initialDelaySecondsInput")
    def initial_delay_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "initialDelaySecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="periodSecondsInput")
    def period_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "periodSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="successThresholdInput")
    def success_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "successThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutSecondsInput")
    def timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="exec")
    def exec(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exec"))

    @exec.setter
    def exec(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerLivenessProbeOutputReference, "exec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exec", value)

    @builtins.property
    @jsii.member(jsii_name="failureThreshold")
    def failure_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "failureThreshold"))

    @failure_threshold.setter
    def failure_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerLivenessProbeOutputReference, "failure_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failureThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="initialDelaySeconds")
    def initial_delay_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialDelaySeconds"))

    @initial_delay_seconds.setter
    def initial_delay_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerLivenessProbeOutputReference, "initial_delay_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialDelaySeconds", value)

    @builtins.property
    @jsii.member(jsii_name="periodSeconds")
    def period_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "periodSeconds"))

    @period_seconds.setter
    def period_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerLivenessProbeOutputReference, "period_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "periodSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="successThreshold")
    def success_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "successThreshold"))

    @success_threshold.setter
    def success_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerLivenessProbeOutputReference, "success_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "successThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutSeconds")
    def timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutSeconds"))

    @timeout_seconds.setter
    def timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerLivenessProbeOutputReference, "timeout_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerGroupContainerLivenessProbe]:
        return typing.cast(typing.Optional[ContainerGroupContainerLivenessProbe], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerGroupContainerLivenessProbe],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerLivenessProbeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerGroupContainerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupContainerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putGpu")
    def put_gpu(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        sku: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#count ContainerGroup#count}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#sku ContainerGroup#sku}.
        '''
        value = ContainerGroupContainerGpu(count=count, sku=sku)

        return typing.cast(None, jsii.invoke(self, "putGpu", [value]))

    @jsii.member(jsii_name="putGpuLimit")
    def put_gpu_limit(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        sku: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#count ContainerGroup#count}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#sku ContainerGroup#sku}.
        '''
        value = ContainerGroupContainerGpuLimit(count=count, sku=sku)

        return typing.cast(None, jsii.invoke(self, "putGpuLimit", [value]))

    @jsii.member(jsii_name="putLivenessProbe")
    def put_liveness_probe(
        self,
        *,
        exec: typing.Optional[typing.Sequence[builtins.str]] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        http_get: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ContainerGroupContainerLivenessProbeHttpGet, typing.Dict[str, typing.Any]]]]] = None,
        initial_delay_seconds: typing.Optional[jsii.Number] = None,
        period_seconds: typing.Optional[jsii.Number] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param exec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#exec ContainerGroup#exec}.
        :param failure_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#failure_threshold ContainerGroup#failure_threshold}.
        :param http_get: http_get block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#http_get ContainerGroup#http_get}
        :param initial_delay_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#initial_delay_seconds ContainerGroup#initial_delay_seconds}.
        :param period_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#period_seconds ContainerGroup#period_seconds}.
        :param success_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#success_threshold ContainerGroup#success_threshold}.
        :param timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#timeout_seconds ContainerGroup#timeout_seconds}.
        '''
        value = ContainerGroupContainerLivenessProbe(
            exec=exec,
            failure_threshold=failure_threshold,
            http_get=http_get,
            initial_delay_seconds=initial_delay_seconds,
            period_seconds=period_seconds,
            success_threshold=success_threshold,
            timeout_seconds=timeout_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putLivenessProbe", [value]))

    @jsii.member(jsii_name="putPorts")
    def put_ports(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupContainerPorts", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainerOutputReference.put_ports)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPorts", [value]))

    @jsii.member(jsii_name="putReadinessProbe")
    def put_readiness_probe(
        self,
        *,
        exec: typing.Optional[typing.Sequence[builtins.str]] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        http_get: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupContainerReadinessProbeHttpGet", typing.Dict[str, typing.Any]]]]] = None,
        initial_delay_seconds: typing.Optional[jsii.Number] = None,
        period_seconds: typing.Optional[jsii.Number] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param exec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#exec ContainerGroup#exec}.
        :param failure_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#failure_threshold ContainerGroup#failure_threshold}.
        :param http_get: http_get block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#http_get ContainerGroup#http_get}
        :param initial_delay_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#initial_delay_seconds ContainerGroup#initial_delay_seconds}.
        :param period_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#period_seconds ContainerGroup#period_seconds}.
        :param success_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#success_threshold ContainerGroup#success_threshold}.
        :param timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#timeout_seconds ContainerGroup#timeout_seconds}.
        '''
        value = ContainerGroupContainerReadinessProbe(
            exec=exec,
            failure_threshold=failure_threshold,
            http_get=http_get,
            initial_delay_seconds=initial_delay_seconds,
            period_seconds=period_seconds,
            success_threshold=success_threshold,
            timeout_seconds=timeout_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putReadinessProbe", [value]))

    @jsii.member(jsii_name="putVolume")
    def put_volume(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupContainerVolume", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainerOutputReference.put_volume)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVolume", [value]))

    @jsii.member(jsii_name="resetCommands")
    def reset_commands(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommands", []))

    @jsii.member(jsii_name="resetCpuLimit")
    def reset_cpu_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuLimit", []))

    @jsii.member(jsii_name="resetEnvironmentVariables")
    def reset_environment_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentVariables", []))

    @jsii.member(jsii_name="resetGpu")
    def reset_gpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGpu", []))

    @jsii.member(jsii_name="resetGpuLimit")
    def reset_gpu_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGpuLimit", []))

    @jsii.member(jsii_name="resetLivenessProbe")
    def reset_liveness_probe(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLivenessProbe", []))

    @jsii.member(jsii_name="resetMemoryLimit")
    def reset_memory_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryLimit", []))

    @jsii.member(jsii_name="resetPorts")
    def reset_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPorts", []))

    @jsii.member(jsii_name="resetReadinessProbe")
    def reset_readiness_probe(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadinessProbe", []))

    @jsii.member(jsii_name="resetSecureEnvironmentVariables")
    def reset_secure_environment_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecureEnvironmentVariables", []))

    @jsii.member(jsii_name="resetVolume")
    def reset_volume(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolume", []))

    @builtins.property
    @jsii.member(jsii_name="gpu")
    def gpu(self) -> ContainerGroupContainerGpuOutputReference:
        return typing.cast(ContainerGroupContainerGpuOutputReference, jsii.get(self, "gpu"))

    @builtins.property
    @jsii.member(jsii_name="gpuLimit")
    def gpu_limit(self) -> ContainerGroupContainerGpuLimitOutputReference:
        return typing.cast(ContainerGroupContainerGpuLimitOutputReference, jsii.get(self, "gpuLimit"))

    @builtins.property
    @jsii.member(jsii_name="livenessProbe")
    def liveness_probe(self) -> ContainerGroupContainerLivenessProbeOutputReference:
        return typing.cast(ContainerGroupContainerLivenessProbeOutputReference, jsii.get(self, "livenessProbe"))

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> "ContainerGroupContainerPortsList":
        return typing.cast("ContainerGroupContainerPortsList", jsii.get(self, "ports"))

    @builtins.property
    @jsii.member(jsii_name="readinessProbe")
    def readiness_probe(self) -> "ContainerGroupContainerReadinessProbeOutputReference":
        return typing.cast("ContainerGroupContainerReadinessProbeOutputReference", jsii.get(self, "readinessProbe"))

    @builtins.property
    @jsii.member(jsii_name="volume")
    def volume(self) -> "ContainerGroupContainerVolumeList":
        return typing.cast("ContainerGroupContainerVolumeList", jsii.get(self, "volume"))

    @builtins.property
    @jsii.member(jsii_name="commandsInput")
    def commands_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "commandsInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuInput")
    def cpu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuLimitInput")
    def cpu_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentVariablesInput")
    def environment_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "environmentVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="gpuInput")
    def gpu_input(self) -> typing.Optional[ContainerGroupContainerGpu]:
        return typing.cast(typing.Optional[ContainerGroupContainerGpu], jsii.get(self, "gpuInput"))

    @builtins.property
    @jsii.member(jsii_name="gpuLimitInput")
    def gpu_limit_input(self) -> typing.Optional[ContainerGroupContainerGpuLimit]:
        return typing.cast(typing.Optional[ContainerGroupContainerGpuLimit], jsii.get(self, "gpuLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="livenessProbeInput")
    def liveness_probe_input(
        self,
    ) -> typing.Optional[ContainerGroupContainerLivenessProbe]:
        return typing.cast(typing.Optional[ContainerGroupContainerLivenessProbe], jsii.get(self, "livenessProbeInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryInput")
    def memory_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryLimitInput")
    def memory_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="portsInput")
    def ports_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupContainerPorts"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupContainerPorts"]]], jsii.get(self, "portsInput"))

    @builtins.property
    @jsii.member(jsii_name="readinessProbeInput")
    def readiness_probe_input(
        self,
    ) -> typing.Optional["ContainerGroupContainerReadinessProbe"]:
        return typing.cast(typing.Optional["ContainerGroupContainerReadinessProbe"], jsii.get(self, "readinessProbeInput"))

    @builtins.property
    @jsii.member(jsii_name="secureEnvironmentVariablesInput")
    def secure_environment_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "secureEnvironmentVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeInput")
    def volume_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupContainerVolume"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupContainerVolume"]]], jsii.get(self, "volumeInput"))

    @builtins.property
    @jsii.member(jsii_name="commands")
    def commands(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "commands"))

    @commands.setter
    def commands(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerOutputReference, "commands").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commands", value)

    @builtins.property
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpu"))

    @cpu.setter
    def cpu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerOutputReference, "cpu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpu", value)

    @builtins.property
    @jsii.member(jsii_name="cpuLimit")
    def cpu_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuLimit"))

    @cpu_limit.setter
    def cpu_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerOutputReference, "cpu_limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuLimit", value)

    @builtins.property
    @jsii.member(jsii_name="environmentVariables")
    def environment_variables(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "environmentVariables"))

    @environment_variables.setter
    def environment_variables(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerOutputReference, "environment_variables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentVariables", value)

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @image.setter
    def image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerOutputReference, "image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "image", value)

    @builtins.property
    @jsii.member(jsii_name="memory")
    def memory(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memory"))

    @memory.setter
    def memory(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerOutputReference, "memory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memory", value)

    @builtins.property
    @jsii.member(jsii_name="memoryLimit")
    def memory_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryLimit"))

    @memory_limit.setter
    def memory_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerOutputReference, "memory_limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryLimit", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="secureEnvironmentVariables")
    def secure_environment_variables(
        self,
    ) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "secureEnvironmentVariables"))

    @secure_environment_variables.setter
    def secure_environment_variables(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerOutputReference, "secure_environment_variables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secureEnvironmentVariables", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerGroupContainer, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerGroupContainer, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerGroupContainer, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerPorts",
    jsii_struct_bases=[],
    name_mapping={"port": "port", "protocol": "protocol"},
)
class ContainerGroupContainerPorts:
    def __init__(
        self,
        *,
        port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#port ContainerGroup#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#protocol ContainerGroup#protocol}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainerPorts.__init__)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
        self._values: typing.Dict[str, typing.Any] = {}
        if port is not None:
            self._values["port"] = port
        if protocol is not None:
            self._values["protocol"] = protocol

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#port ContainerGroup#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#protocol ContainerGroup#protocol}.'''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupContainerPorts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerGroupContainerPortsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerPortsList",
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
            type_hints = typing.get_type_hints(ContainerGroupContainerPortsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerGroupContainerPortsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainerPortsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerGroupContainerPortsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerPortsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerPortsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerPortsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainerPorts]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainerPorts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainerPorts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerPortsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerGroupContainerPortsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerPortsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupContainerPortsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerPortsOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerPortsOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerGroupContainerPorts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerGroupContainerPorts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerGroupContainerPorts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerPortsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerReadinessProbe",
    jsii_struct_bases=[],
    name_mapping={
        "exec": "exec",
        "failure_threshold": "failureThreshold",
        "http_get": "httpGet",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "success_threshold": "successThreshold",
        "timeout_seconds": "timeoutSeconds",
    },
)
class ContainerGroupContainerReadinessProbe:
    def __init__(
        self,
        *,
        exec: typing.Optional[typing.Sequence[builtins.str]] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        http_get: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupContainerReadinessProbeHttpGet", typing.Dict[str, typing.Any]]]]] = None,
        initial_delay_seconds: typing.Optional[jsii.Number] = None,
        period_seconds: typing.Optional[jsii.Number] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param exec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#exec ContainerGroup#exec}.
        :param failure_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#failure_threshold ContainerGroup#failure_threshold}.
        :param http_get: http_get block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#http_get ContainerGroup#http_get}
        :param initial_delay_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#initial_delay_seconds ContainerGroup#initial_delay_seconds}.
        :param period_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#period_seconds ContainerGroup#period_seconds}.
        :param success_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#success_threshold ContainerGroup#success_threshold}.
        :param timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#timeout_seconds ContainerGroup#timeout_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainerReadinessProbe.__init__)
            check_type(argname="argument exec", value=exec, expected_type=type_hints["exec"])
            check_type(argname="argument failure_threshold", value=failure_threshold, expected_type=type_hints["failure_threshold"])
            check_type(argname="argument http_get", value=http_get, expected_type=type_hints["http_get"])
            check_type(argname="argument initial_delay_seconds", value=initial_delay_seconds, expected_type=type_hints["initial_delay_seconds"])
            check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
            check_type(argname="argument success_threshold", value=success_threshold, expected_type=type_hints["success_threshold"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if exec is not None:
            self._values["exec"] = exec
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if http_get is not None:
            self._values["http_get"] = http_get
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def exec(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#exec ContainerGroup#exec}.'''
        result = self._values.get("exec")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#failure_threshold ContainerGroup#failure_threshold}.'''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def http_get(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupContainerReadinessProbeHttpGet"]]]:
        '''http_get block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#http_get ContainerGroup#http_get}
        '''
        result = self._values.get("http_get")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupContainerReadinessProbeHttpGet"]]], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#initial_delay_seconds ContainerGroup#initial_delay_seconds}.'''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#period_seconds ContainerGroup#period_seconds}.'''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#success_threshold ContainerGroup#success_threshold}.'''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#timeout_seconds ContainerGroup#timeout_seconds}.'''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupContainerReadinessProbe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerReadinessProbeHttpGet",
    jsii_struct_bases=[],
    name_mapping={
        "http_headers": "httpHeaders",
        "path": "path",
        "port": "port",
        "scheme": "scheme",
    },
)
class ContainerGroupContainerReadinessProbeHttpGet:
    def __init__(
        self,
        *,
        http_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        scheme: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#http_headers ContainerGroup#http_headers}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#path ContainerGroup#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#port ContainerGroup#port}.
        :param scheme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#scheme ContainerGroup#scheme}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainerReadinessProbeHttpGet.__init__)
            check_type(argname="argument http_headers", value=http_headers, expected_type=type_hints["http_headers"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument scheme", value=scheme, expected_type=type_hints["scheme"])
        self._values: typing.Dict[str, typing.Any] = {}
        if http_headers is not None:
            self._values["http_headers"] = http_headers
        if path is not None:
            self._values["path"] = path
        if port is not None:
            self._values["port"] = port
        if scheme is not None:
            self._values["scheme"] = scheme

    @builtins.property
    def http_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#http_headers ContainerGroup#http_headers}.'''
        result = self._values.get("http_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#path ContainerGroup#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#port ContainerGroup#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scheme(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#scheme ContainerGroup#scheme}.'''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupContainerReadinessProbeHttpGet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerGroupContainerReadinessProbeHttpGetList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerReadinessProbeHttpGetList",
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
            type_hints = typing.get_type_hints(ContainerGroupContainerReadinessProbeHttpGetList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ContainerGroupContainerReadinessProbeHttpGetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainerReadinessProbeHttpGetList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerGroupContainerReadinessProbeHttpGetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerReadinessProbeHttpGetList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerReadinessProbeHttpGetList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerReadinessProbeHttpGetList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainerReadinessProbeHttpGet]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainerReadinessProbeHttpGet]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainerReadinessProbeHttpGet]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerReadinessProbeHttpGetList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerGroupContainerReadinessProbeHttpGetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerReadinessProbeHttpGetOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupContainerReadinessProbeHttpGetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetHttpHeaders")
    def reset_http_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpHeaders", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetScheme")
    def reset_scheme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheme", []))

    @builtins.property
    @jsii.member(jsii_name="httpHeadersInput")
    def http_headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "httpHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="schemeInput")
    def scheme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemeInput"))

    @builtins.property
    @jsii.member(jsii_name="httpHeaders")
    def http_headers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "httpHeaders"))

    @http_headers.setter
    def http_headers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerReadinessProbeHttpGetOutputReference, "http_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerReadinessProbeHttpGetOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerReadinessProbeHttpGetOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="scheme")
    def scheme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheme"))

    @scheme.setter
    def scheme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerReadinessProbeHttpGetOutputReference, "scheme").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheme", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerGroupContainerReadinessProbeHttpGet, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerGroupContainerReadinessProbeHttpGet, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerGroupContainerReadinessProbeHttpGet, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerReadinessProbeHttpGetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerGroupContainerReadinessProbeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerReadinessProbeOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupContainerReadinessProbeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHttpGet")
    def put_http_get(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ContainerGroupContainerReadinessProbeHttpGet, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainerReadinessProbeOutputReference.put_http_get)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHttpGet", [value]))

    @jsii.member(jsii_name="resetExec")
    def reset_exec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExec", []))

    @jsii.member(jsii_name="resetFailureThreshold")
    def reset_failure_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailureThreshold", []))

    @jsii.member(jsii_name="resetHttpGet")
    def reset_http_get(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpGet", []))

    @jsii.member(jsii_name="resetInitialDelaySeconds")
    def reset_initial_delay_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialDelaySeconds", []))

    @jsii.member(jsii_name="resetPeriodSeconds")
    def reset_period_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriodSeconds", []))

    @jsii.member(jsii_name="resetSuccessThreshold")
    def reset_success_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuccessThreshold", []))

    @jsii.member(jsii_name="resetTimeoutSeconds")
    def reset_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="httpGet")
    def http_get(self) -> ContainerGroupContainerReadinessProbeHttpGetList:
        return typing.cast(ContainerGroupContainerReadinessProbeHttpGetList, jsii.get(self, "httpGet"))

    @builtins.property
    @jsii.member(jsii_name="execInput")
    def exec_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "execInput"))

    @builtins.property
    @jsii.member(jsii_name="failureThresholdInput")
    def failure_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "failureThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="httpGetInput")
    def http_get_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainerReadinessProbeHttpGet]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainerReadinessProbeHttpGet]]], jsii.get(self, "httpGetInput"))

    @builtins.property
    @jsii.member(jsii_name="initialDelaySecondsInput")
    def initial_delay_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "initialDelaySecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="periodSecondsInput")
    def period_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "periodSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="successThresholdInput")
    def success_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "successThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutSecondsInput")
    def timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="exec")
    def exec(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exec"))

    @exec.setter
    def exec(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerReadinessProbeOutputReference, "exec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exec", value)

    @builtins.property
    @jsii.member(jsii_name="failureThreshold")
    def failure_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "failureThreshold"))

    @failure_threshold.setter
    def failure_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerReadinessProbeOutputReference, "failure_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failureThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="initialDelaySeconds")
    def initial_delay_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialDelaySeconds"))

    @initial_delay_seconds.setter
    def initial_delay_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerReadinessProbeOutputReference, "initial_delay_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialDelaySeconds", value)

    @builtins.property
    @jsii.member(jsii_name="periodSeconds")
    def period_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "periodSeconds"))

    @period_seconds.setter
    def period_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerReadinessProbeOutputReference, "period_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "periodSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="successThreshold")
    def success_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "successThreshold"))

    @success_threshold.setter
    def success_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerReadinessProbeOutputReference, "success_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "successThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutSeconds")
    def timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutSeconds"))

    @timeout_seconds.setter
    def timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerReadinessProbeOutputReference, "timeout_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerGroupContainerReadinessProbe]:
        return typing.cast(typing.Optional[ContainerGroupContainerReadinessProbe], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerGroupContainerReadinessProbe],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerReadinessProbeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerVolume",
    jsii_struct_bases=[],
    name_mapping={
        "mount_path": "mountPath",
        "name": "name",
        "empty_dir": "emptyDir",
        "git_repo": "gitRepo",
        "read_only": "readOnly",
        "secret": "secret",
        "share_name": "shareName",
        "storage_account_key": "storageAccountKey",
        "storage_account_name": "storageAccountName",
    },
)
class ContainerGroupContainerVolume:
    def __init__(
        self,
        *,
        mount_path: builtins.str,
        name: builtins.str,
        empty_dir: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        git_repo: typing.Optional[typing.Union["ContainerGroupContainerVolumeGitRepo", typing.Dict[str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        secret: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        share_name: typing.Optional[builtins.str] = None,
        storage_account_key: typing.Optional[builtins.str] = None,
        storage_account_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param mount_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#mount_path ContainerGroup#mount_path}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#name ContainerGroup#name}.
        :param empty_dir: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#empty_dir ContainerGroup#empty_dir}.
        :param git_repo: git_repo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#git_repo ContainerGroup#git_repo}
        :param read_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#read_only ContainerGroup#read_only}.
        :param secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#secret ContainerGroup#secret}.
        :param share_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#share_name ContainerGroup#share_name}.
        :param storage_account_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#storage_account_key ContainerGroup#storage_account_key}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#storage_account_name ContainerGroup#storage_account_name}.
        '''
        if isinstance(git_repo, dict):
            git_repo = ContainerGroupContainerVolumeGitRepo(**git_repo)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainerVolume.__init__)
            check_type(argname="argument mount_path", value=mount_path, expected_type=type_hints["mount_path"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument empty_dir", value=empty_dir, expected_type=type_hints["empty_dir"])
            check_type(argname="argument git_repo", value=git_repo, expected_type=type_hints["git_repo"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
            check_type(argname="argument share_name", value=share_name, expected_type=type_hints["share_name"])
            check_type(argname="argument storage_account_key", value=storage_account_key, expected_type=type_hints["storage_account_key"])
            check_type(argname="argument storage_account_name", value=storage_account_name, expected_type=type_hints["storage_account_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "mount_path": mount_path,
            "name": name,
        }
        if empty_dir is not None:
            self._values["empty_dir"] = empty_dir
        if git_repo is not None:
            self._values["git_repo"] = git_repo
        if read_only is not None:
            self._values["read_only"] = read_only
        if secret is not None:
            self._values["secret"] = secret
        if share_name is not None:
            self._values["share_name"] = share_name
        if storage_account_key is not None:
            self._values["storage_account_key"] = storage_account_key
        if storage_account_name is not None:
            self._values["storage_account_name"] = storage_account_name

    @builtins.property
    def mount_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#mount_path ContainerGroup#mount_path}.'''
        result = self._values.get("mount_path")
        assert result is not None, "Required property 'mount_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#name ContainerGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def empty_dir(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#empty_dir ContainerGroup#empty_dir}.'''
        result = self._values.get("empty_dir")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def git_repo(self) -> typing.Optional["ContainerGroupContainerVolumeGitRepo"]:
        '''git_repo block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#git_repo ContainerGroup#git_repo}
        '''
        result = self._values.get("git_repo")
        return typing.cast(typing.Optional["ContainerGroupContainerVolumeGitRepo"], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#read_only ContainerGroup#read_only}.'''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def secret(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#secret ContainerGroup#secret}.'''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def share_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#share_name ContainerGroup#share_name}.'''
        result = self._values.get("share_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#storage_account_key ContainerGroup#storage_account_key}.'''
        result = self._values.get("storage_account_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#storage_account_name ContainerGroup#storage_account_name}.'''
        result = self._values.get("storage_account_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupContainerVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerVolumeGitRepo",
    jsii_struct_bases=[],
    name_mapping={"url": "url", "directory": "directory", "revision": "revision"},
)
class ContainerGroupContainerVolumeGitRepo:
    def __init__(
        self,
        *,
        url: builtins.str,
        directory: typing.Optional[builtins.str] = None,
        revision: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#url ContainerGroup#url}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#directory ContainerGroup#directory}.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#revision ContainerGroup#revision}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainerVolumeGitRepo.__init__)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
            check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
        self._values: typing.Dict[str, typing.Any] = {
            "url": url,
        }
        if directory is not None:
            self._values["directory"] = directory
        if revision is not None:
            self._values["revision"] = revision

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#url ContainerGroup#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def directory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#directory ContainerGroup#directory}.'''
        result = self._values.get("directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def revision(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#revision ContainerGroup#revision}.'''
        result = self._values.get("revision")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupContainerVolumeGitRepo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerGroupContainerVolumeGitRepoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerVolumeGitRepoOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupContainerVolumeGitRepoOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDirectory")
    def reset_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectory", []))

    @jsii.member(jsii_name="resetRevision")
    def reset_revision(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRevision", []))

    @builtins.property
    @jsii.member(jsii_name="directoryInput")
    def directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryInput"))

    @builtins.property
    @jsii.member(jsii_name="revisionInput")
    def revision_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "revisionInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="directory")
    def directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directory"))

    @directory.setter
    def directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerVolumeGitRepoOutputReference, "directory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directory", value)

    @builtins.property
    @jsii.member(jsii_name="revision")
    def revision(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "revision"))

    @revision.setter
    def revision(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerVolumeGitRepoOutputReference, "revision").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revision", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerVolumeGitRepoOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerGroupContainerVolumeGitRepo]:
        return typing.cast(typing.Optional[ContainerGroupContainerVolumeGitRepo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerGroupContainerVolumeGitRepo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerVolumeGitRepoOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerGroupContainerVolumeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerVolumeList",
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
            type_hints = typing.get_type_hints(ContainerGroupContainerVolumeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerGroupContainerVolumeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupContainerVolumeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerGroupContainerVolumeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerVolumeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerVolumeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerVolumeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainerVolume]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainerVolume]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupContainerVolume]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerVolumeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerGroupContainerVolumeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupContainerVolumeOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupContainerVolumeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putGitRepo")
    def put_git_repo(
        self,
        *,
        url: builtins.str,
        directory: typing.Optional[builtins.str] = None,
        revision: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#url ContainerGroup#url}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#directory ContainerGroup#directory}.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#revision ContainerGroup#revision}.
        '''
        value = ContainerGroupContainerVolumeGitRepo(
            url=url, directory=directory, revision=revision
        )

        return typing.cast(None, jsii.invoke(self, "putGitRepo", [value]))

    @jsii.member(jsii_name="resetEmptyDir")
    def reset_empty_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmptyDir", []))

    @jsii.member(jsii_name="resetGitRepo")
    def reset_git_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitRepo", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecret")
    def reset_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecret", []))

    @jsii.member(jsii_name="resetShareName")
    def reset_share_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShareName", []))

    @jsii.member(jsii_name="resetStorageAccountKey")
    def reset_storage_account_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountKey", []))

    @jsii.member(jsii_name="resetStorageAccountName")
    def reset_storage_account_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountName", []))

    @builtins.property
    @jsii.member(jsii_name="gitRepo")
    def git_repo(self) -> ContainerGroupContainerVolumeGitRepoOutputReference:
        return typing.cast(ContainerGroupContainerVolumeGitRepoOutputReference, jsii.get(self, "gitRepo"))

    @builtins.property
    @jsii.member(jsii_name="emptyDirInput")
    def empty_dir_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "emptyDirInput"))

    @builtins.property
    @jsii.member(jsii_name="gitRepoInput")
    def git_repo_input(self) -> typing.Optional[ContainerGroupContainerVolumeGitRepo]:
        return typing.cast(typing.Optional[ContainerGroupContainerVolumeGitRepo], jsii.get(self, "gitRepoInput"))

    @builtins.property
    @jsii.member(jsii_name="mountPathInput")
    def mount_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountPathInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretInput")
    def secret_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "secretInput"))

    @builtins.property
    @jsii.member(jsii_name="shareNameInput")
    def share_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shareNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountKeyInput")
    def storage_account_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountNameInput")
    def storage_account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="emptyDir")
    def empty_dir(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "emptyDir"))

    @empty_dir.setter
    def empty_dir(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerVolumeOutputReference, "empty_dir").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emptyDir", value)

    @builtins.property
    @jsii.member(jsii_name="mountPath")
    def mount_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountPath"))

    @mount_path.setter
    def mount_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerVolumeOutputReference, "mount_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountPath", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerVolumeOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerVolumeOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "secret"))

    @secret.setter
    def secret(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerVolumeOutputReference, "secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secret", value)

    @builtins.property
    @jsii.member(jsii_name="shareName")
    def share_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shareName"))

    @share_name.setter
    def share_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerVolumeOutputReference, "share_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shareName", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountKey")
    def storage_account_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountKey"))

    @storage_account_key.setter
    def storage_account_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerVolumeOutputReference, "storage_account_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountKey", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountName")
    def storage_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountName"))

    @storage_account_name.setter
    def storage_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerVolumeOutputReference, "storage_account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerGroupContainerVolume, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerGroupContainerVolume, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerGroupContainerVolume, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupContainerVolumeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupDiagnostics",
    jsii_struct_bases=[],
    name_mapping={"log_analytics": "logAnalytics"},
)
class ContainerGroupDiagnostics:
    def __init__(
        self,
        *,
        log_analytics: typing.Union["ContainerGroupDiagnosticsLogAnalytics", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param log_analytics: log_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#log_analytics ContainerGroup#log_analytics}
        '''
        if isinstance(log_analytics, dict):
            log_analytics = ContainerGroupDiagnosticsLogAnalytics(**log_analytics)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupDiagnostics.__init__)
            check_type(argname="argument log_analytics", value=log_analytics, expected_type=type_hints["log_analytics"])
        self._values: typing.Dict[str, typing.Any] = {
            "log_analytics": log_analytics,
        }

    @builtins.property
    def log_analytics(self) -> "ContainerGroupDiagnosticsLogAnalytics":
        '''log_analytics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#log_analytics ContainerGroup#log_analytics}
        '''
        result = self._values.get("log_analytics")
        assert result is not None, "Required property 'log_analytics' is missing"
        return typing.cast("ContainerGroupDiagnosticsLogAnalytics", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupDiagnostics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupDiagnosticsLogAnalytics",
    jsii_struct_bases=[],
    name_mapping={
        "workspace_id": "workspaceId",
        "workspace_key": "workspaceKey",
        "log_type": "logType",
        "metadata": "metadata",
    },
)
class ContainerGroupDiagnosticsLogAnalytics:
    def __init__(
        self,
        *,
        workspace_id: builtins.str,
        workspace_key: builtins.str,
        log_type: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#workspace_id ContainerGroup#workspace_id}.
        :param workspace_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#workspace_key ContainerGroup#workspace_key}.
        :param log_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#log_type ContainerGroup#log_type}.
        :param metadata: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#metadata ContainerGroup#metadata}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupDiagnosticsLogAnalytics.__init__)
            check_type(argname="argument workspace_id", value=workspace_id, expected_type=type_hints["workspace_id"])
            check_type(argname="argument workspace_key", value=workspace_key, expected_type=type_hints["workspace_key"])
            check_type(argname="argument log_type", value=log_type, expected_type=type_hints["log_type"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[str, typing.Any] = {
            "workspace_id": workspace_id,
            "workspace_key": workspace_key,
        }
        if log_type is not None:
            self._values["log_type"] = log_type
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def workspace_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#workspace_id ContainerGroup#workspace_id}.'''
        result = self._values.get("workspace_id")
        assert result is not None, "Required property 'workspace_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#workspace_key ContainerGroup#workspace_key}.'''
        result = self._values.get("workspace_key")
        assert result is not None, "Required property 'workspace_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#log_type ContainerGroup#log_type}.'''
        result = self._values.get("log_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#metadata ContainerGroup#metadata}.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupDiagnosticsLogAnalytics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerGroupDiagnosticsLogAnalyticsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupDiagnosticsLogAnalyticsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupDiagnosticsLogAnalyticsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLogType")
    def reset_log_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogType", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @builtins.property
    @jsii.member(jsii_name="logTypeInput")
    def log_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceIdInput")
    def workspace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceKeyInput")
    def workspace_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workspaceKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="logType")
    def log_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logType"))

    @log_type.setter
    def log_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupDiagnosticsLogAnalyticsOutputReference, "log_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logType", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupDiagnosticsLogAnalyticsOutputReference, "metadata").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceId")
    def workspace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceId"))

    @workspace_id.setter
    def workspace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupDiagnosticsLogAnalyticsOutputReference, "workspace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceId", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceKey")
    def workspace_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceKey"))

    @workspace_key.setter
    def workspace_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupDiagnosticsLogAnalyticsOutputReference, "workspace_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerGroupDiagnosticsLogAnalytics]:
        return typing.cast(typing.Optional[ContainerGroupDiagnosticsLogAnalytics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerGroupDiagnosticsLogAnalytics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupDiagnosticsLogAnalyticsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerGroupDiagnosticsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupDiagnosticsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupDiagnosticsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLogAnalytics")
    def put_log_analytics(
        self,
        *,
        workspace_id: builtins.str,
        workspace_key: builtins.str,
        log_type: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#workspace_id ContainerGroup#workspace_id}.
        :param workspace_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#workspace_key ContainerGroup#workspace_key}.
        :param log_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#log_type ContainerGroup#log_type}.
        :param metadata: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#metadata ContainerGroup#metadata}.
        '''
        value = ContainerGroupDiagnosticsLogAnalytics(
            workspace_id=workspace_id,
            workspace_key=workspace_key,
            log_type=log_type,
            metadata=metadata,
        )

        return typing.cast(None, jsii.invoke(self, "putLogAnalytics", [value]))

    @builtins.property
    @jsii.member(jsii_name="logAnalytics")
    def log_analytics(self) -> ContainerGroupDiagnosticsLogAnalyticsOutputReference:
        return typing.cast(ContainerGroupDiagnosticsLogAnalyticsOutputReference, jsii.get(self, "logAnalytics"))

    @builtins.property
    @jsii.member(jsii_name="logAnalyticsInput")
    def log_analytics_input(
        self,
    ) -> typing.Optional[ContainerGroupDiagnosticsLogAnalytics]:
        return typing.cast(typing.Optional[ContainerGroupDiagnosticsLogAnalytics], jsii.get(self, "logAnalyticsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerGroupDiagnostics]:
        return typing.cast(typing.Optional[ContainerGroupDiagnostics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ContainerGroupDiagnostics]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupDiagnosticsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupDnsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "nameservers": "nameservers",
        "options": "options",
        "search_domains": "searchDomains",
    },
)
class ContainerGroupDnsConfig:
    def __init__(
        self,
        *,
        nameservers: typing.Sequence[builtins.str],
        options: typing.Optional[typing.Sequence[builtins.str]] = None,
        search_domains: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param nameservers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#nameservers ContainerGroup#nameservers}.
        :param options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#options ContainerGroup#options}.
        :param search_domains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#search_domains ContainerGroup#search_domains}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupDnsConfig.__init__)
            check_type(argname="argument nameservers", value=nameservers, expected_type=type_hints["nameservers"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument search_domains", value=search_domains, expected_type=type_hints["search_domains"])
        self._values: typing.Dict[str, typing.Any] = {
            "nameservers": nameservers,
        }
        if options is not None:
            self._values["options"] = options
        if search_domains is not None:
            self._values["search_domains"] = search_domains

    @builtins.property
    def nameservers(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#nameservers ContainerGroup#nameservers}.'''
        result = self._values.get("nameservers")
        assert result is not None, "Required property 'nameservers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#options ContainerGroup#options}.'''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def search_domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#search_domains ContainerGroup#search_domains}.'''
        result = self._values.get("search_domains")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupDnsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerGroupDnsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupDnsConfigOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupDnsConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @jsii.member(jsii_name="resetSearchDomains")
    def reset_search_domains(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearchDomains", []))

    @builtins.property
    @jsii.member(jsii_name="nameserversInput")
    def nameservers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nameserversInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="searchDomainsInput")
    def search_domains_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "searchDomainsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameservers")
    def nameservers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nameservers"))

    @nameservers.setter
    def nameservers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupDnsConfigOutputReference, "nameservers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameservers", value)

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupDnsConfigOutputReference, "options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)

    @builtins.property
    @jsii.member(jsii_name="searchDomains")
    def search_domains(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "searchDomains"))

    @search_domains.setter
    def search_domains(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupDnsConfigOutputReference, "search_domains").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "searchDomains", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerGroupDnsConfig]:
        return typing.cast(typing.Optional[ContainerGroupDnsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ContainerGroupDnsConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupDnsConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupExposedPort",
    jsii_struct_bases=[],
    name_mapping={"port": "port", "protocol": "protocol"},
)
class ContainerGroupExposedPort:
    def __init__(
        self,
        *,
        port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#port ContainerGroup#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#protocol ContainerGroup#protocol}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupExposedPort.__init__)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
        self._values: typing.Dict[str, typing.Any] = {}
        if port is not None:
            self._values["port"] = port
        if protocol is not None:
            self._values["protocol"] = protocol

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#port ContainerGroup#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#protocol ContainerGroup#protocol}.'''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupExposedPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerGroupExposedPortList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupExposedPortList",
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
            type_hints = typing.get_type_hints(ContainerGroupExposedPortList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerGroupExposedPortOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupExposedPortList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerGroupExposedPortOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupExposedPortList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupExposedPortList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupExposedPortList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupExposedPort]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupExposedPort]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupExposedPort]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupExposedPortList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerGroupExposedPortOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupExposedPortOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupExposedPortOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupExposedPortOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupExposedPortOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerGroupExposedPort, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerGroupExposedPort, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerGroupExposedPort, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupExposedPortOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class ContainerGroupIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#type ContainerGroup#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#identity_ids ContainerGroup#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#type ContainerGroup#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#identity_ids ContainerGroup#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerGroupIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupIdentityOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdentityIds")
    def reset_identity_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityIds", []))

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

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
            type_hints = typing.get_type_hints(getattr(ContainerGroupIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerGroupIdentity]:
        return typing.cast(typing.Optional[ContainerGroupIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ContainerGroupIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupImageRegistryCredential",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "server": "server", "username": "username"},
)
class ContainerGroupImageRegistryCredential:
    def __init__(
        self,
        *,
        password: builtins.str,
        server: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#password ContainerGroup#password}.
        :param server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#server ContainerGroup#server}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#username ContainerGroup#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupImageRegistryCredential.__init__)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument server", value=server, expected_type=type_hints["server"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "server": server,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#password ContainerGroup#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#server ContainerGroup#server}.'''
        result = self._values.get("server")
        assert result is not None, "Required property 'server' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#username ContainerGroup#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupImageRegistryCredential(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerGroupImageRegistryCredentialList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupImageRegistryCredentialList",
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
            type_hints = typing.get_type_hints(ContainerGroupImageRegistryCredentialList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ContainerGroupImageRegistryCredentialOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupImageRegistryCredentialList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerGroupImageRegistryCredentialOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupImageRegistryCredentialList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupImageRegistryCredentialList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupImageRegistryCredentialList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupImageRegistryCredential]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupImageRegistryCredential]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupImageRegistryCredential]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupImageRegistryCredentialList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerGroupImageRegistryCredentialOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupImageRegistryCredentialOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupImageRegistryCredentialOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="serverInput")
    def server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverInput"))

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
            type_hints = typing.get_type_hints(getattr(ContainerGroupImageRegistryCredentialOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="server")
    def server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "server"))

    @server.setter
    def server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupImageRegistryCredentialOutputReference, "server").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "server", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupImageRegistryCredentialOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerGroupImageRegistryCredential, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerGroupImageRegistryCredential, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerGroupImageRegistryCredential, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupImageRegistryCredentialOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupInitContainer",
    jsii_struct_bases=[],
    name_mapping={
        "image": "image",
        "name": "name",
        "commands": "commands",
        "environment_variables": "environmentVariables",
        "secure_environment_variables": "secureEnvironmentVariables",
        "volume": "volume",
    },
)
class ContainerGroupInitContainer:
    def __init__(
        self,
        *,
        image: builtins.str,
        name: builtins.str,
        commands: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        secure_environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        volume: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupInitContainerVolume", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#image ContainerGroup#image}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#name ContainerGroup#name}.
        :param commands: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#commands ContainerGroup#commands}.
        :param environment_variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#environment_variables ContainerGroup#environment_variables}.
        :param secure_environment_variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#secure_environment_variables ContainerGroup#secure_environment_variables}.
        :param volume: volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#volume ContainerGroup#volume}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupInitContainer.__init__)
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument commands", value=commands, expected_type=type_hints["commands"])
            check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
            check_type(argname="argument secure_environment_variables", value=secure_environment_variables, expected_type=type_hints["secure_environment_variables"])
            check_type(argname="argument volume", value=volume, expected_type=type_hints["volume"])
        self._values: typing.Dict[str, typing.Any] = {
            "image": image,
            "name": name,
        }
        if commands is not None:
            self._values["commands"] = commands
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if secure_environment_variables is not None:
            self._values["secure_environment_variables"] = secure_environment_variables
        if volume is not None:
            self._values["volume"] = volume

    @builtins.property
    def image(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#image ContainerGroup#image}.'''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#name ContainerGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def commands(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#commands ContainerGroup#commands}.'''
        result = self._values.get("commands")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#environment_variables ContainerGroup#environment_variables}.'''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def secure_environment_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#secure_environment_variables ContainerGroup#secure_environment_variables}.'''
        result = self._values.get("secure_environment_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def volume(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupInitContainerVolume"]]]:
        '''volume block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#volume ContainerGroup#volume}
        '''
        result = self._values.get("volume")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupInitContainerVolume"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupInitContainer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerGroupInitContainerList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupInitContainerList",
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
            type_hints = typing.get_type_hints(ContainerGroupInitContainerList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerGroupInitContainerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupInitContainerList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerGroupInitContainerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupInitContainer]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupInitContainer]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupInitContainer]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerGroupInitContainerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupInitContainerOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupInitContainerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putVolume")
    def put_volume(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerGroupInitContainerVolume", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupInitContainerOutputReference.put_volume)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVolume", [value]))

    @jsii.member(jsii_name="resetCommands")
    def reset_commands(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommands", []))

    @jsii.member(jsii_name="resetEnvironmentVariables")
    def reset_environment_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentVariables", []))

    @jsii.member(jsii_name="resetSecureEnvironmentVariables")
    def reset_secure_environment_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecureEnvironmentVariables", []))

    @jsii.member(jsii_name="resetVolume")
    def reset_volume(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolume", []))

    @builtins.property
    @jsii.member(jsii_name="volume")
    def volume(self) -> "ContainerGroupInitContainerVolumeList":
        return typing.cast("ContainerGroupInitContainerVolumeList", jsii.get(self, "volume"))

    @builtins.property
    @jsii.member(jsii_name="commandsInput")
    def commands_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "commandsInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentVariablesInput")
    def environment_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "environmentVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="secureEnvironmentVariablesInput")
    def secure_environment_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "secureEnvironmentVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeInput")
    def volume_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupInitContainerVolume"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerGroupInitContainerVolume"]]], jsii.get(self, "volumeInput"))

    @builtins.property
    @jsii.member(jsii_name="commands")
    def commands(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "commands"))

    @commands.setter
    def commands(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerOutputReference, "commands").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commands", value)

    @builtins.property
    @jsii.member(jsii_name="environmentVariables")
    def environment_variables(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "environmentVariables"))

    @environment_variables.setter
    def environment_variables(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerOutputReference, "environment_variables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentVariables", value)

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @image.setter
    def image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerOutputReference, "image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "image", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="secureEnvironmentVariables")
    def secure_environment_variables(
        self,
    ) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "secureEnvironmentVariables"))

    @secure_environment_variables.setter
    def secure_environment_variables(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerOutputReference, "secure_environment_variables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secureEnvironmentVariables", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerGroupInitContainer, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerGroupInitContainer, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerGroupInitContainer, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupInitContainerVolume",
    jsii_struct_bases=[],
    name_mapping={
        "mount_path": "mountPath",
        "name": "name",
        "empty_dir": "emptyDir",
        "git_repo": "gitRepo",
        "read_only": "readOnly",
        "secret": "secret",
        "share_name": "shareName",
        "storage_account_key": "storageAccountKey",
        "storage_account_name": "storageAccountName",
    },
)
class ContainerGroupInitContainerVolume:
    def __init__(
        self,
        *,
        mount_path: builtins.str,
        name: builtins.str,
        empty_dir: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        git_repo: typing.Optional[typing.Union["ContainerGroupInitContainerVolumeGitRepo", typing.Dict[str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        secret: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        share_name: typing.Optional[builtins.str] = None,
        storage_account_key: typing.Optional[builtins.str] = None,
        storage_account_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param mount_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#mount_path ContainerGroup#mount_path}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#name ContainerGroup#name}.
        :param empty_dir: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#empty_dir ContainerGroup#empty_dir}.
        :param git_repo: git_repo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#git_repo ContainerGroup#git_repo}
        :param read_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#read_only ContainerGroup#read_only}.
        :param secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#secret ContainerGroup#secret}.
        :param share_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#share_name ContainerGroup#share_name}.
        :param storage_account_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#storage_account_key ContainerGroup#storage_account_key}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#storage_account_name ContainerGroup#storage_account_name}.
        '''
        if isinstance(git_repo, dict):
            git_repo = ContainerGroupInitContainerVolumeGitRepo(**git_repo)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupInitContainerVolume.__init__)
            check_type(argname="argument mount_path", value=mount_path, expected_type=type_hints["mount_path"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument empty_dir", value=empty_dir, expected_type=type_hints["empty_dir"])
            check_type(argname="argument git_repo", value=git_repo, expected_type=type_hints["git_repo"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
            check_type(argname="argument share_name", value=share_name, expected_type=type_hints["share_name"])
            check_type(argname="argument storage_account_key", value=storage_account_key, expected_type=type_hints["storage_account_key"])
            check_type(argname="argument storage_account_name", value=storage_account_name, expected_type=type_hints["storage_account_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "mount_path": mount_path,
            "name": name,
        }
        if empty_dir is not None:
            self._values["empty_dir"] = empty_dir
        if git_repo is not None:
            self._values["git_repo"] = git_repo
        if read_only is not None:
            self._values["read_only"] = read_only
        if secret is not None:
            self._values["secret"] = secret
        if share_name is not None:
            self._values["share_name"] = share_name
        if storage_account_key is not None:
            self._values["storage_account_key"] = storage_account_key
        if storage_account_name is not None:
            self._values["storage_account_name"] = storage_account_name

    @builtins.property
    def mount_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#mount_path ContainerGroup#mount_path}.'''
        result = self._values.get("mount_path")
        assert result is not None, "Required property 'mount_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#name ContainerGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def empty_dir(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#empty_dir ContainerGroup#empty_dir}.'''
        result = self._values.get("empty_dir")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def git_repo(self) -> typing.Optional["ContainerGroupInitContainerVolumeGitRepo"]:
        '''git_repo block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#git_repo ContainerGroup#git_repo}
        '''
        result = self._values.get("git_repo")
        return typing.cast(typing.Optional["ContainerGroupInitContainerVolumeGitRepo"], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#read_only ContainerGroup#read_only}.'''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def secret(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#secret ContainerGroup#secret}.'''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def share_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#share_name ContainerGroup#share_name}.'''
        result = self._values.get("share_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#storage_account_key ContainerGroup#storage_account_key}.'''
        result = self._values.get("storage_account_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#storage_account_name ContainerGroup#storage_account_name}.'''
        result = self._values.get("storage_account_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupInitContainerVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupInitContainerVolumeGitRepo",
    jsii_struct_bases=[],
    name_mapping={"url": "url", "directory": "directory", "revision": "revision"},
)
class ContainerGroupInitContainerVolumeGitRepo:
    def __init__(
        self,
        *,
        url: builtins.str,
        directory: typing.Optional[builtins.str] = None,
        revision: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#url ContainerGroup#url}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#directory ContainerGroup#directory}.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#revision ContainerGroup#revision}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupInitContainerVolumeGitRepo.__init__)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
            check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
        self._values: typing.Dict[str, typing.Any] = {
            "url": url,
        }
        if directory is not None:
            self._values["directory"] = directory
        if revision is not None:
            self._values["revision"] = revision

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#url ContainerGroup#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def directory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#directory ContainerGroup#directory}.'''
        result = self._values.get("directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def revision(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#revision ContainerGroup#revision}.'''
        result = self._values.get("revision")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupInitContainerVolumeGitRepo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerGroupInitContainerVolumeGitRepoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupInitContainerVolumeGitRepoOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupInitContainerVolumeGitRepoOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDirectory")
    def reset_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectory", []))

    @jsii.member(jsii_name="resetRevision")
    def reset_revision(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRevision", []))

    @builtins.property
    @jsii.member(jsii_name="directoryInput")
    def directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryInput"))

    @builtins.property
    @jsii.member(jsii_name="revisionInput")
    def revision_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "revisionInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="directory")
    def directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directory"))

    @directory.setter
    def directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerVolumeGitRepoOutputReference, "directory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directory", value)

    @builtins.property
    @jsii.member(jsii_name="revision")
    def revision(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "revision"))

    @revision.setter
    def revision(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerVolumeGitRepoOutputReference, "revision").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revision", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerVolumeGitRepoOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerGroupInitContainerVolumeGitRepo]:
        return typing.cast(typing.Optional[ContainerGroupInitContainerVolumeGitRepo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerGroupInitContainerVolumeGitRepo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerVolumeGitRepoOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerGroupInitContainerVolumeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupInitContainerVolumeList",
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
            type_hints = typing.get_type_hints(ContainerGroupInitContainerVolumeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ContainerGroupInitContainerVolumeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupInitContainerVolumeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerGroupInitContainerVolumeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerVolumeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerVolumeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerVolumeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupInitContainerVolume]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupInitContainerVolume]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerGroupInitContainerVolume]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerVolumeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerGroupInitContainerVolumeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupInitContainerVolumeOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupInitContainerVolumeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putGitRepo")
    def put_git_repo(
        self,
        *,
        url: builtins.str,
        directory: typing.Optional[builtins.str] = None,
        revision: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#url ContainerGroup#url}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#directory ContainerGroup#directory}.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#revision ContainerGroup#revision}.
        '''
        value = ContainerGroupInitContainerVolumeGitRepo(
            url=url, directory=directory, revision=revision
        )

        return typing.cast(None, jsii.invoke(self, "putGitRepo", [value]))

    @jsii.member(jsii_name="resetEmptyDir")
    def reset_empty_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmptyDir", []))

    @jsii.member(jsii_name="resetGitRepo")
    def reset_git_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitRepo", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecret")
    def reset_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecret", []))

    @jsii.member(jsii_name="resetShareName")
    def reset_share_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShareName", []))

    @jsii.member(jsii_name="resetStorageAccountKey")
    def reset_storage_account_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountKey", []))

    @jsii.member(jsii_name="resetStorageAccountName")
    def reset_storage_account_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountName", []))

    @builtins.property
    @jsii.member(jsii_name="gitRepo")
    def git_repo(self) -> ContainerGroupInitContainerVolumeGitRepoOutputReference:
        return typing.cast(ContainerGroupInitContainerVolumeGitRepoOutputReference, jsii.get(self, "gitRepo"))

    @builtins.property
    @jsii.member(jsii_name="emptyDirInput")
    def empty_dir_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "emptyDirInput"))

    @builtins.property
    @jsii.member(jsii_name="gitRepoInput")
    def git_repo_input(
        self,
    ) -> typing.Optional[ContainerGroupInitContainerVolumeGitRepo]:
        return typing.cast(typing.Optional[ContainerGroupInitContainerVolumeGitRepo], jsii.get(self, "gitRepoInput"))

    @builtins.property
    @jsii.member(jsii_name="mountPathInput")
    def mount_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountPathInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretInput")
    def secret_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "secretInput"))

    @builtins.property
    @jsii.member(jsii_name="shareNameInput")
    def share_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shareNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountKeyInput")
    def storage_account_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountNameInput")
    def storage_account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="emptyDir")
    def empty_dir(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "emptyDir"))

    @empty_dir.setter
    def empty_dir(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerVolumeOutputReference, "empty_dir").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emptyDir", value)

    @builtins.property
    @jsii.member(jsii_name="mountPath")
    def mount_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountPath"))

    @mount_path.setter
    def mount_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerVolumeOutputReference, "mount_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountPath", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerVolumeOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerVolumeOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "secret"))

    @secret.setter
    def secret(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerVolumeOutputReference, "secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secret", value)

    @builtins.property
    @jsii.member(jsii_name="shareName")
    def share_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shareName"))

    @share_name.setter
    def share_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerVolumeOutputReference, "share_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shareName", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountKey")
    def storage_account_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountKey"))

    @storage_account_key.setter
    def storage_account_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerVolumeOutputReference, "storage_account_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountKey", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountName")
    def storage_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountName"))

    @storage_account_name.setter
    def storage_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerVolumeOutputReference, "storage_account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerGroupInitContainerVolume, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerGroupInitContainerVolume, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerGroupInitContainerVolume, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupInitContainerVolumeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ContainerGroupTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#create ContainerGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#delete ContainerGroup#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#read ContainerGroup#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#update ContainerGroup#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerGroupTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#create ContainerGroup#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#delete ContainerGroup#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#read ContainerGroup#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_group#update ContainerGroup#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerGroupTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerGroup.ContainerGroupTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerGroupTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ContainerGroupTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerGroupTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerGroupTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerGroupTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerGroupTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ContainerGroup",
    "ContainerGroupConfig",
    "ContainerGroupContainer",
    "ContainerGroupContainerGpu",
    "ContainerGroupContainerGpuLimit",
    "ContainerGroupContainerGpuLimitOutputReference",
    "ContainerGroupContainerGpuOutputReference",
    "ContainerGroupContainerList",
    "ContainerGroupContainerLivenessProbe",
    "ContainerGroupContainerLivenessProbeHttpGet",
    "ContainerGroupContainerLivenessProbeHttpGetList",
    "ContainerGroupContainerLivenessProbeHttpGetOutputReference",
    "ContainerGroupContainerLivenessProbeOutputReference",
    "ContainerGroupContainerOutputReference",
    "ContainerGroupContainerPorts",
    "ContainerGroupContainerPortsList",
    "ContainerGroupContainerPortsOutputReference",
    "ContainerGroupContainerReadinessProbe",
    "ContainerGroupContainerReadinessProbeHttpGet",
    "ContainerGroupContainerReadinessProbeHttpGetList",
    "ContainerGroupContainerReadinessProbeHttpGetOutputReference",
    "ContainerGroupContainerReadinessProbeOutputReference",
    "ContainerGroupContainerVolume",
    "ContainerGroupContainerVolumeGitRepo",
    "ContainerGroupContainerVolumeGitRepoOutputReference",
    "ContainerGroupContainerVolumeList",
    "ContainerGroupContainerVolumeOutputReference",
    "ContainerGroupDiagnostics",
    "ContainerGroupDiagnosticsLogAnalytics",
    "ContainerGroupDiagnosticsLogAnalyticsOutputReference",
    "ContainerGroupDiagnosticsOutputReference",
    "ContainerGroupDnsConfig",
    "ContainerGroupDnsConfigOutputReference",
    "ContainerGroupExposedPort",
    "ContainerGroupExposedPortList",
    "ContainerGroupExposedPortOutputReference",
    "ContainerGroupIdentity",
    "ContainerGroupIdentityOutputReference",
    "ContainerGroupImageRegistryCredential",
    "ContainerGroupImageRegistryCredentialList",
    "ContainerGroupImageRegistryCredentialOutputReference",
    "ContainerGroupInitContainer",
    "ContainerGroupInitContainerList",
    "ContainerGroupInitContainerOutputReference",
    "ContainerGroupInitContainerVolume",
    "ContainerGroupInitContainerVolumeGitRepo",
    "ContainerGroupInitContainerVolumeGitRepoOutputReference",
    "ContainerGroupInitContainerVolumeList",
    "ContainerGroupInitContainerVolumeOutputReference",
    "ContainerGroupTimeouts",
    "ContainerGroupTimeoutsOutputReference",
]

publication.publish()
