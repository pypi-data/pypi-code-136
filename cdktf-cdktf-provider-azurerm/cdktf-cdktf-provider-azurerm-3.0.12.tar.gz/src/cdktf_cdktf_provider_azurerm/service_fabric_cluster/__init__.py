'''
# `azurerm_service_fabric_cluster`

Refer to the Terraform Registory for docs: [`azurerm_service_fabric_cluster`](https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster).
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


class ServiceFabricCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster azurerm_service_fabric_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        management_endpoint: builtins.str,
        name: builtins.str,
        node_type: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricClusterNodeType", typing.Dict[str, typing.Any]]]],
        reliability_level: builtins.str,
        resource_group_name: builtins.str,
        upgrade_mode: builtins.str,
        vm_image: builtins.str,
        add_on_features: typing.Optional[typing.Sequence[builtins.str]] = None,
        azure_active_directory: typing.Optional[typing.Union["ServiceFabricClusterAzureActiveDirectory", typing.Dict[str, typing.Any]]] = None,
        certificate: typing.Optional[typing.Union["ServiceFabricClusterCertificate", typing.Dict[str, typing.Any]]] = None,
        certificate_common_names: typing.Optional[typing.Union["ServiceFabricClusterCertificateCommonNames", typing.Dict[str, typing.Any]]] = None,
        client_certificate_common_name: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricClusterClientCertificateCommonName", typing.Dict[str, typing.Any]]]]] = None,
        client_certificate_thumbprint: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricClusterClientCertificateThumbprint", typing.Dict[str, typing.Any]]]]] = None,
        cluster_code_version: typing.Optional[builtins.str] = None,
        diagnostics_config: typing.Optional[typing.Union["ServiceFabricClusterDiagnosticsConfig", typing.Dict[str, typing.Any]]] = None,
        fabric_settings: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricClusterFabricSettings", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        reverse_proxy_certificate: typing.Optional[typing.Union["ServiceFabricClusterReverseProxyCertificate", typing.Dict[str, typing.Any]]] = None,
        reverse_proxy_certificate_common_names: typing.Optional[typing.Union["ServiceFabricClusterReverseProxyCertificateCommonNames", typing.Dict[str, typing.Any]]] = None,
        service_fabric_zonal_upgrade_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ServiceFabricClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        upgrade_policy: typing.Optional[typing.Union["ServiceFabricClusterUpgradePolicy", typing.Dict[str, typing.Any]]] = None,
        vmss_zonal_upgrade_mode: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster azurerm_service_fabric_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#location ServiceFabricCluster#location}.
        :param management_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#management_endpoint ServiceFabricCluster#management_endpoint}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#name ServiceFabricCluster#name}.
        :param node_type: node_type block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#node_type ServiceFabricCluster#node_type}
        :param reliability_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#reliability_level ServiceFabricCluster#reliability_level}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#resource_group_name ServiceFabricCluster#resource_group_name}.
        :param upgrade_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#upgrade_mode ServiceFabricCluster#upgrade_mode}.
        :param vm_image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#vm_image ServiceFabricCluster#vm_image}.
        :param add_on_features: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#add_on_features ServiceFabricCluster#add_on_features}.
        :param azure_active_directory: azure_active_directory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#azure_active_directory ServiceFabricCluster#azure_active_directory}
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#certificate ServiceFabricCluster#certificate}
        :param certificate_common_names: certificate_common_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#certificate_common_names ServiceFabricCluster#certificate_common_names}
        :param client_certificate_common_name: client_certificate_common_name block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#client_certificate_common_name ServiceFabricCluster#client_certificate_common_name}
        :param client_certificate_thumbprint: client_certificate_thumbprint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#client_certificate_thumbprint ServiceFabricCluster#client_certificate_thumbprint}
        :param cluster_code_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#cluster_code_version ServiceFabricCluster#cluster_code_version}.
        :param diagnostics_config: diagnostics_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#diagnostics_config ServiceFabricCluster#diagnostics_config}
        :param fabric_settings: fabric_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#fabric_settings ServiceFabricCluster#fabric_settings}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#id ServiceFabricCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param reverse_proxy_certificate: reverse_proxy_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#reverse_proxy_certificate ServiceFabricCluster#reverse_proxy_certificate}
        :param reverse_proxy_certificate_common_names: reverse_proxy_certificate_common_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#reverse_proxy_certificate_common_names ServiceFabricCluster#reverse_proxy_certificate_common_names}
        :param service_fabric_zonal_upgrade_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#service_fabric_zonal_upgrade_mode ServiceFabricCluster#service_fabric_zonal_upgrade_mode}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#tags ServiceFabricCluster#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#timeouts ServiceFabricCluster#timeouts}
        :param upgrade_policy: upgrade_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#upgrade_policy ServiceFabricCluster#upgrade_policy}
        :param vmss_zonal_upgrade_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#vmss_zonal_upgrade_mode ServiceFabricCluster#vmss_zonal_upgrade_mode}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ServiceFabricClusterConfig(
            location=location,
            management_endpoint=management_endpoint,
            name=name,
            node_type=node_type,
            reliability_level=reliability_level,
            resource_group_name=resource_group_name,
            upgrade_mode=upgrade_mode,
            vm_image=vm_image,
            add_on_features=add_on_features,
            azure_active_directory=azure_active_directory,
            certificate=certificate,
            certificate_common_names=certificate_common_names,
            client_certificate_common_name=client_certificate_common_name,
            client_certificate_thumbprint=client_certificate_thumbprint,
            cluster_code_version=cluster_code_version,
            diagnostics_config=diagnostics_config,
            fabric_settings=fabric_settings,
            id=id,
            reverse_proxy_certificate=reverse_proxy_certificate,
            reverse_proxy_certificate_common_names=reverse_proxy_certificate_common_names,
            service_fabric_zonal_upgrade_mode=service_fabric_zonal_upgrade_mode,
            tags=tags,
            timeouts=timeouts,
            upgrade_policy=upgrade_policy,
            vmss_zonal_upgrade_mode=vmss_zonal_upgrade_mode,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAzureActiveDirectory")
    def put_azure_active_directory(
        self,
        *,
        client_application_id: builtins.str,
        cluster_application_id: builtins.str,
        tenant_id: builtins.str,
    ) -> None:
        '''
        :param client_application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#client_application_id ServiceFabricCluster#client_application_id}.
        :param cluster_application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#cluster_application_id ServiceFabricCluster#cluster_application_id}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#tenant_id ServiceFabricCluster#tenant_id}.
        '''
        value = ServiceFabricClusterAzureActiveDirectory(
            client_application_id=client_application_id,
            cluster_application_id=cluster_application_id,
            tenant_id=tenant_id,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureActiveDirectory", [value]))

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        *,
        thumbprint: builtins.str,
        x509_store_name: builtins.str,
        thumbprint_secondary: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param thumbprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#thumbprint ServiceFabricCluster#thumbprint}.
        :param x509_store_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#x509_store_name ServiceFabricCluster#x509_store_name}.
        :param thumbprint_secondary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#thumbprint_secondary ServiceFabricCluster#thumbprint_secondary}.
        '''
        value = ServiceFabricClusterCertificate(
            thumbprint=thumbprint,
            x509_store_name=x509_store_name,
            thumbprint_secondary=thumbprint_secondary,
        )

        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @jsii.member(jsii_name="putCertificateCommonNames")
    def put_certificate_common_names(
        self,
        *,
        common_names: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricClusterCertificateCommonNamesCommonNames", typing.Dict[str, typing.Any]]]],
        x509_store_name: builtins.str,
    ) -> None:
        '''
        :param common_names: common_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#common_names ServiceFabricCluster#common_names}
        :param x509_store_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#x509_store_name ServiceFabricCluster#x509_store_name}.
        '''
        value = ServiceFabricClusterCertificateCommonNames(
            common_names=common_names, x509_store_name=x509_store_name
        )

        return typing.cast(None, jsii.invoke(self, "putCertificateCommonNames", [value]))

    @jsii.member(jsii_name="putClientCertificateCommonName")
    def put_client_certificate_common_name(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricClusterClientCertificateCommonName", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricCluster.put_client_certificate_common_name)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putClientCertificateCommonName", [value]))

    @jsii.member(jsii_name="putClientCertificateThumbprint")
    def put_client_certificate_thumbprint(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricClusterClientCertificateThumbprint", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricCluster.put_client_certificate_thumbprint)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putClientCertificateThumbprint", [value]))

    @jsii.member(jsii_name="putDiagnosticsConfig")
    def put_diagnostics_config(
        self,
        *,
        blob_endpoint: builtins.str,
        protected_account_key_name: builtins.str,
        queue_endpoint: builtins.str,
        storage_account_name: builtins.str,
        table_endpoint: builtins.str,
    ) -> None:
        '''
        :param blob_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#blob_endpoint ServiceFabricCluster#blob_endpoint}.
        :param protected_account_key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#protected_account_key_name ServiceFabricCluster#protected_account_key_name}.
        :param queue_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#queue_endpoint ServiceFabricCluster#queue_endpoint}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#storage_account_name ServiceFabricCluster#storage_account_name}.
        :param table_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#table_endpoint ServiceFabricCluster#table_endpoint}.
        '''
        value = ServiceFabricClusterDiagnosticsConfig(
            blob_endpoint=blob_endpoint,
            protected_account_key_name=protected_account_key_name,
            queue_endpoint=queue_endpoint,
            storage_account_name=storage_account_name,
            table_endpoint=table_endpoint,
        )

        return typing.cast(None, jsii.invoke(self, "putDiagnosticsConfig", [value]))

    @jsii.member(jsii_name="putFabricSettings")
    def put_fabric_settings(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricClusterFabricSettings", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricCluster.put_fabric_settings)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFabricSettings", [value]))

    @jsii.member(jsii_name="putNodeType")
    def put_node_type(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricClusterNodeType", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricCluster.put_node_type)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNodeType", [value]))

    @jsii.member(jsii_name="putReverseProxyCertificate")
    def put_reverse_proxy_certificate(
        self,
        *,
        thumbprint: builtins.str,
        x509_store_name: builtins.str,
        thumbprint_secondary: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param thumbprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#thumbprint ServiceFabricCluster#thumbprint}.
        :param x509_store_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#x509_store_name ServiceFabricCluster#x509_store_name}.
        :param thumbprint_secondary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#thumbprint_secondary ServiceFabricCluster#thumbprint_secondary}.
        '''
        value = ServiceFabricClusterReverseProxyCertificate(
            thumbprint=thumbprint,
            x509_store_name=x509_store_name,
            thumbprint_secondary=thumbprint_secondary,
        )

        return typing.cast(None, jsii.invoke(self, "putReverseProxyCertificate", [value]))

    @jsii.member(jsii_name="putReverseProxyCertificateCommonNames")
    def put_reverse_proxy_certificate_common_names(
        self,
        *,
        common_names: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNames", typing.Dict[str, typing.Any]]]],
        x509_store_name: builtins.str,
    ) -> None:
        '''
        :param common_names: common_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#common_names ServiceFabricCluster#common_names}
        :param x509_store_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#x509_store_name ServiceFabricCluster#x509_store_name}.
        '''
        value = ServiceFabricClusterReverseProxyCertificateCommonNames(
            common_names=common_names, x509_store_name=x509_store_name
        )

        return typing.cast(None, jsii.invoke(self, "putReverseProxyCertificateCommonNames", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#create ServiceFabricCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#delete ServiceFabricCluster#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#read ServiceFabricCluster#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#update ServiceFabricCluster#update}.
        '''
        value = ServiceFabricClusterTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putUpgradePolicy")
    def put_upgrade_policy(
        self,
        *,
        delta_health_policy: typing.Optional[typing.Union["ServiceFabricClusterUpgradePolicyDeltaHealthPolicy", typing.Dict[str, typing.Any]]] = None,
        force_restart_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_check_retry_timeout: typing.Optional[builtins.str] = None,
        health_check_stable_duration: typing.Optional[builtins.str] = None,
        health_check_wait_duration: typing.Optional[builtins.str] = None,
        health_policy: typing.Optional[typing.Union["ServiceFabricClusterUpgradePolicyHealthPolicy", typing.Dict[str, typing.Any]]] = None,
        upgrade_domain_timeout: typing.Optional[builtins.str] = None,
        upgrade_replica_set_check_timeout: typing.Optional[builtins.str] = None,
        upgrade_timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delta_health_policy: delta_health_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#delta_health_policy ServiceFabricCluster#delta_health_policy}
        :param force_restart_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#force_restart_enabled ServiceFabricCluster#force_restart_enabled}.
        :param health_check_retry_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#health_check_retry_timeout ServiceFabricCluster#health_check_retry_timeout}.
        :param health_check_stable_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#health_check_stable_duration ServiceFabricCluster#health_check_stable_duration}.
        :param health_check_wait_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#health_check_wait_duration ServiceFabricCluster#health_check_wait_duration}.
        :param health_policy: health_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#health_policy ServiceFabricCluster#health_policy}
        :param upgrade_domain_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#upgrade_domain_timeout ServiceFabricCluster#upgrade_domain_timeout}.
        :param upgrade_replica_set_check_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#upgrade_replica_set_check_timeout ServiceFabricCluster#upgrade_replica_set_check_timeout}.
        :param upgrade_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#upgrade_timeout ServiceFabricCluster#upgrade_timeout}.
        '''
        value = ServiceFabricClusterUpgradePolicy(
            delta_health_policy=delta_health_policy,
            force_restart_enabled=force_restart_enabled,
            health_check_retry_timeout=health_check_retry_timeout,
            health_check_stable_duration=health_check_stable_duration,
            health_check_wait_duration=health_check_wait_duration,
            health_policy=health_policy,
            upgrade_domain_timeout=upgrade_domain_timeout,
            upgrade_replica_set_check_timeout=upgrade_replica_set_check_timeout,
            upgrade_timeout=upgrade_timeout,
        )

        return typing.cast(None, jsii.invoke(self, "putUpgradePolicy", [value]))

    @jsii.member(jsii_name="resetAddOnFeatures")
    def reset_add_on_features(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddOnFeatures", []))

    @jsii.member(jsii_name="resetAzureActiveDirectory")
    def reset_azure_active_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureActiveDirectory", []))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetCertificateCommonNames")
    def reset_certificate_common_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateCommonNames", []))

    @jsii.member(jsii_name="resetClientCertificateCommonName")
    def reset_client_certificate_common_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificateCommonName", []))

    @jsii.member(jsii_name="resetClientCertificateThumbprint")
    def reset_client_certificate_thumbprint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificateThumbprint", []))

    @jsii.member(jsii_name="resetClusterCodeVersion")
    def reset_cluster_code_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterCodeVersion", []))

    @jsii.member(jsii_name="resetDiagnosticsConfig")
    def reset_diagnostics_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiagnosticsConfig", []))

    @jsii.member(jsii_name="resetFabricSettings")
    def reset_fabric_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFabricSettings", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetReverseProxyCertificate")
    def reset_reverse_proxy_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReverseProxyCertificate", []))

    @jsii.member(jsii_name="resetReverseProxyCertificateCommonNames")
    def reset_reverse_proxy_certificate_common_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReverseProxyCertificateCommonNames", []))

    @jsii.member(jsii_name="resetServiceFabricZonalUpgradeMode")
    def reset_service_fabric_zonal_upgrade_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceFabricZonalUpgradeMode", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUpgradePolicy")
    def reset_upgrade_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpgradePolicy", []))

    @jsii.member(jsii_name="resetVmssZonalUpgradeMode")
    def reset_vmss_zonal_upgrade_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVmssZonalUpgradeMode", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="azureActiveDirectory")
    def azure_active_directory(
        self,
    ) -> "ServiceFabricClusterAzureActiveDirectoryOutputReference":
        return typing.cast("ServiceFabricClusterAzureActiveDirectoryOutputReference", jsii.get(self, "azureActiveDirectory"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> "ServiceFabricClusterCertificateOutputReference":
        return typing.cast("ServiceFabricClusterCertificateOutputReference", jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="certificateCommonNames")
    def certificate_common_names(
        self,
    ) -> "ServiceFabricClusterCertificateCommonNamesOutputReference":
        return typing.cast("ServiceFabricClusterCertificateCommonNamesOutputReference", jsii.get(self, "certificateCommonNames"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateCommonName")
    def client_certificate_common_name(
        self,
    ) -> "ServiceFabricClusterClientCertificateCommonNameList":
        return typing.cast("ServiceFabricClusterClientCertificateCommonNameList", jsii.get(self, "clientCertificateCommonName"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateThumbprint")
    def client_certificate_thumbprint(
        self,
    ) -> "ServiceFabricClusterClientCertificateThumbprintList":
        return typing.cast("ServiceFabricClusterClientCertificateThumbprintList", jsii.get(self, "clientCertificateThumbprint"))

    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="diagnosticsConfig")
    def diagnostics_config(
        self,
    ) -> "ServiceFabricClusterDiagnosticsConfigOutputReference":
        return typing.cast("ServiceFabricClusterDiagnosticsConfigOutputReference", jsii.get(self, "diagnosticsConfig"))

    @builtins.property
    @jsii.member(jsii_name="fabricSettings")
    def fabric_settings(self) -> "ServiceFabricClusterFabricSettingsList":
        return typing.cast("ServiceFabricClusterFabricSettingsList", jsii.get(self, "fabricSettings"))

    @builtins.property
    @jsii.member(jsii_name="nodeType")
    def node_type(self) -> "ServiceFabricClusterNodeTypeList":
        return typing.cast("ServiceFabricClusterNodeTypeList", jsii.get(self, "nodeType"))

    @builtins.property
    @jsii.member(jsii_name="reverseProxyCertificate")
    def reverse_proxy_certificate(
        self,
    ) -> "ServiceFabricClusterReverseProxyCertificateOutputReference":
        return typing.cast("ServiceFabricClusterReverseProxyCertificateOutputReference", jsii.get(self, "reverseProxyCertificate"))

    @builtins.property
    @jsii.member(jsii_name="reverseProxyCertificateCommonNames")
    def reverse_proxy_certificate_common_names(
        self,
    ) -> "ServiceFabricClusterReverseProxyCertificateCommonNamesOutputReference":
        return typing.cast("ServiceFabricClusterReverseProxyCertificateCommonNamesOutputReference", jsii.get(self, "reverseProxyCertificateCommonNames"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ServiceFabricClusterTimeoutsOutputReference":
        return typing.cast("ServiceFabricClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="upgradePolicy")
    def upgrade_policy(self) -> "ServiceFabricClusterUpgradePolicyOutputReference":
        return typing.cast("ServiceFabricClusterUpgradePolicyOutputReference", jsii.get(self, "upgradePolicy"))

    @builtins.property
    @jsii.member(jsii_name="addOnFeaturesInput")
    def add_on_features_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "addOnFeaturesInput"))

    @builtins.property
    @jsii.member(jsii_name="azureActiveDirectoryInput")
    def azure_active_directory_input(
        self,
    ) -> typing.Optional["ServiceFabricClusterAzureActiveDirectory"]:
        return typing.cast(typing.Optional["ServiceFabricClusterAzureActiveDirectory"], jsii.get(self, "azureActiveDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateCommonNamesInput")
    def certificate_common_names_input(
        self,
    ) -> typing.Optional["ServiceFabricClusterCertificateCommonNames"]:
        return typing.cast(typing.Optional["ServiceFabricClusterCertificateCommonNames"], jsii.get(self, "certificateCommonNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional["ServiceFabricClusterCertificate"]:
        return typing.cast(typing.Optional["ServiceFabricClusterCertificate"], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateCommonNameInput")
    def client_certificate_common_name_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricClusterClientCertificateCommonName"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricClusterClientCertificateCommonName"]]], jsii.get(self, "clientCertificateCommonNameInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateThumbprintInput")
    def client_certificate_thumbprint_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricClusterClientCertificateThumbprint"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricClusterClientCertificateThumbprint"]]], jsii.get(self, "clientCertificateThumbprintInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterCodeVersionInput")
    def cluster_code_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterCodeVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="diagnosticsConfigInput")
    def diagnostics_config_input(
        self,
    ) -> typing.Optional["ServiceFabricClusterDiagnosticsConfig"]:
        return typing.cast(typing.Optional["ServiceFabricClusterDiagnosticsConfig"], jsii.get(self, "diagnosticsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="fabricSettingsInput")
    def fabric_settings_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricClusterFabricSettings"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricClusterFabricSettings"]]], jsii.get(self, "fabricSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="managementEndpointInput")
    def management_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managementEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeTypeInput")
    def node_type_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricClusterNodeType"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricClusterNodeType"]]], jsii.get(self, "nodeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="reliabilityLevelInput")
    def reliability_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "reliabilityLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="reverseProxyCertificateCommonNamesInput")
    def reverse_proxy_certificate_common_names_input(
        self,
    ) -> typing.Optional["ServiceFabricClusterReverseProxyCertificateCommonNames"]:
        return typing.cast(typing.Optional["ServiceFabricClusterReverseProxyCertificateCommonNames"], jsii.get(self, "reverseProxyCertificateCommonNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="reverseProxyCertificateInput")
    def reverse_proxy_certificate_input(
        self,
    ) -> typing.Optional["ServiceFabricClusterReverseProxyCertificate"]:
        return typing.cast(typing.Optional["ServiceFabricClusterReverseProxyCertificate"], jsii.get(self, "reverseProxyCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceFabricZonalUpgradeModeInput")
    def service_fabric_zonal_upgrade_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceFabricZonalUpgradeModeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ServiceFabricClusterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ServiceFabricClusterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="upgradeModeInput")
    def upgrade_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "upgradeModeInput"))

    @builtins.property
    @jsii.member(jsii_name="upgradePolicyInput")
    def upgrade_policy_input(
        self,
    ) -> typing.Optional["ServiceFabricClusterUpgradePolicy"]:
        return typing.cast(typing.Optional["ServiceFabricClusterUpgradePolicy"], jsii.get(self, "upgradePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="vmImageInput")
    def vm_image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmImageInput"))

    @builtins.property
    @jsii.member(jsii_name="vmssZonalUpgradeModeInput")
    def vmss_zonal_upgrade_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmssZonalUpgradeModeInput"))

    @builtins.property
    @jsii.member(jsii_name="addOnFeatures")
    def add_on_features(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "addOnFeatures"))

    @add_on_features.setter
    def add_on_features(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricCluster, "add_on_features").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addOnFeatures", value)

    @builtins.property
    @jsii.member(jsii_name="clusterCodeVersion")
    def cluster_code_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterCodeVersion"))

    @cluster_code_version.setter
    def cluster_code_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricCluster, "cluster_code_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterCodeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricCluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricCluster, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="managementEndpoint")
    def management_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managementEndpoint"))

    @management_endpoint.setter
    def management_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricCluster, "management_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managementEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricCluster, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="reliabilityLevel")
    def reliability_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reliabilityLevel"))

    @reliability_level.setter
    def reliability_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricCluster, "reliability_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reliabilityLevel", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricCluster, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceFabricZonalUpgradeMode")
    def service_fabric_zonal_upgrade_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceFabricZonalUpgradeMode"))

    @service_fabric_zonal_upgrade_mode.setter
    def service_fabric_zonal_upgrade_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricCluster, "service_fabric_zonal_upgrade_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceFabricZonalUpgradeMode", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricCluster, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="upgradeMode")
    def upgrade_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "upgradeMode"))

    @upgrade_mode.setter
    def upgrade_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricCluster, "upgrade_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upgradeMode", value)

    @builtins.property
    @jsii.member(jsii_name="vmImage")
    def vm_image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmImage"))

    @vm_image.setter
    def vm_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricCluster, "vm_image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmImage", value)

    @builtins.property
    @jsii.member(jsii_name="vmssZonalUpgradeMode")
    def vmss_zonal_upgrade_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmssZonalUpgradeMode"))

    @vmss_zonal_upgrade_mode.setter
    def vmss_zonal_upgrade_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricCluster, "vmss_zonal_upgrade_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmssZonalUpgradeMode", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterAzureActiveDirectory",
    jsii_struct_bases=[],
    name_mapping={
        "client_application_id": "clientApplicationId",
        "cluster_application_id": "clusterApplicationId",
        "tenant_id": "tenantId",
    },
)
class ServiceFabricClusterAzureActiveDirectory:
    def __init__(
        self,
        *,
        client_application_id: builtins.str,
        cluster_application_id: builtins.str,
        tenant_id: builtins.str,
    ) -> None:
        '''
        :param client_application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#client_application_id ServiceFabricCluster#client_application_id}.
        :param cluster_application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#cluster_application_id ServiceFabricCluster#cluster_application_id}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#tenant_id ServiceFabricCluster#tenant_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterAzureActiveDirectory.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#client_application_id ServiceFabricCluster#client_application_id}.'''
        result = self._values.get("client_application_id")
        assert result is not None, "Required property 'client_application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_application_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#cluster_application_id ServiceFabricCluster#cluster_application_id}.'''
        result = self._values.get("cluster_application_id")
        assert result is not None, "Required property 'cluster_application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tenant_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#tenant_id ServiceFabricCluster#tenant_id}.'''
        result = self._values.get("tenant_id")
        assert result is not None, "Required property 'tenant_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterAzureActiveDirectory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricClusterAzureActiveDirectoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterAzureActiveDirectoryOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterAzureActiveDirectoryOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterAzureActiveDirectoryOutputReference, "client_application_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientApplicationId", value)

    @builtins.property
    @jsii.member(jsii_name="clusterApplicationId")
    def cluster_application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterApplicationId"))

    @cluster_application_id.setter
    def cluster_application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterAzureActiveDirectoryOutputReference, "cluster_application_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterApplicationId", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterAzureActiveDirectoryOutputReference, "tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceFabricClusterAzureActiveDirectory]:
        return typing.cast(typing.Optional[ServiceFabricClusterAzureActiveDirectory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceFabricClusterAzureActiveDirectory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterAzureActiveDirectoryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterCertificate",
    jsii_struct_bases=[],
    name_mapping={
        "thumbprint": "thumbprint",
        "x509_store_name": "x509StoreName",
        "thumbprint_secondary": "thumbprintSecondary",
    },
)
class ServiceFabricClusterCertificate:
    def __init__(
        self,
        *,
        thumbprint: builtins.str,
        x509_store_name: builtins.str,
        thumbprint_secondary: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param thumbprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#thumbprint ServiceFabricCluster#thumbprint}.
        :param x509_store_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#x509_store_name ServiceFabricCluster#x509_store_name}.
        :param thumbprint_secondary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#thumbprint_secondary ServiceFabricCluster#thumbprint_secondary}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterCertificate.__init__)
            check_type(argname="argument thumbprint", value=thumbprint, expected_type=type_hints["thumbprint"])
            check_type(argname="argument x509_store_name", value=x509_store_name, expected_type=type_hints["x509_store_name"])
            check_type(argname="argument thumbprint_secondary", value=thumbprint_secondary, expected_type=type_hints["thumbprint_secondary"])
        self._values: typing.Dict[str, typing.Any] = {
            "thumbprint": thumbprint,
            "x509_store_name": x509_store_name,
        }
        if thumbprint_secondary is not None:
            self._values["thumbprint_secondary"] = thumbprint_secondary

    @builtins.property
    def thumbprint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#thumbprint ServiceFabricCluster#thumbprint}.'''
        result = self._values.get("thumbprint")
        assert result is not None, "Required property 'thumbprint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def x509_store_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#x509_store_name ServiceFabricCluster#x509_store_name}.'''
        result = self._values.get("x509_store_name")
        assert result is not None, "Required property 'x509_store_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def thumbprint_secondary(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#thumbprint_secondary ServiceFabricCluster#thumbprint_secondary}.'''
        result = self._values.get("thumbprint_secondary")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterCertificateCommonNames",
    jsii_struct_bases=[],
    name_mapping={"common_names": "commonNames", "x509_store_name": "x509StoreName"},
)
class ServiceFabricClusterCertificateCommonNames:
    def __init__(
        self,
        *,
        common_names: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricClusterCertificateCommonNamesCommonNames", typing.Dict[str, typing.Any]]]],
        x509_store_name: builtins.str,
    ) -> None:
        '''
        :param common_names: common_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#common_names ServiceFabricCluster#common_names}
        :param x509_store_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#x509_store_name ServiceFabricCluster#x509_store_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterCertificateCommonNames.__init__)
            check_type(argname="argument common_names", value=common_names, expected_type=type_hints["common_names"])
            check_type(argname="argument x509_store_name", value=x509_store_name, expected_type=type_hints["x509_store_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "common_names": common_names,
            "x509_store_name": x509_store_name,
        }

    @builtins.property
    def common_names(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ServiceFabricClusterCertificateCommonNamesCommonNames"]]:
        '''common_names block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#common_names ServiceFabricCluster#common_names}
        '''
        result = self._values.get("common_names")
        assert result is not None, "Required property 'common_names' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ServiceFabricClusterCertificateCommonNamesCommonNames"]], result)

    @builtins.property
    def x509_store_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#x509_store_name ServiceFabricCluster#x509_store_name}.'''
        result = self._values.get("x509_store_name")
        assert result is not None, "Required property 'x509_store_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterCertificateCommonNames(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterCertificateCommonNamesCommonNames",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_common_name": "certificateCommonName",
        "certificate_issuer_thumbprint": "certificateIssuerThumbprint",
    },
)
class ServiceFabricClusterCertificateCommonNamesCommonNames:
    def __init__(
        self,
        *,
        certificate_common_name: builtins.str,
        certificate_issuer_thumbprint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param certificate_common_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#certificate_common_name ServiceFabricCluster#certificate_common_name}.
        :param certificate_issuer_thumbprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#certificate_issuer_thumbprint ServiceFabricCluster#certificate_issuer_thumbprint}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterCertificateCommonNamesCommonNames.__init__)
            check_type(argname="argument certificate_common_name", value=certificate_common_name, expected_type=type_hints["certificate_common_name"])
            check_type(argname="argument certificate_issuer_thumbprint", value=certificate_issuer_thumbprint, expected_type=type_hints["certificate_issuer_thumbprint"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate_common_name": certificate_common_name,
        }
        if certificate_issuer_thumbprint is not None:
            self._values["certificate_issuer_thumbprint"] = certificate_issuer_thumbprint

    @builtins.property
    def certificate_common_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#certificate_common_name ServiceFabricCluster#certificate_common_name}.'''
        result = self._values.get("certificate_common_name")
        assert result is not None, "Required property 'certificate_common_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_issuer_thumbprint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#certificate_issuer_thumbprint ServiceFabricCluster#certificate_issuer_thumbprint}.'''
        result = self._values.get("certificate_issuer_thumbprint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterCertificateCommonNamesCommonNames(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricClusterCertificateCommonNamesCommonNamesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterCertificateCommonNamesCommonNamesList",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterCertificateCommonNamesCommonNamesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceFabricClusterCertificateCommonNamesCommonNamesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterCertificateCommonNamesCommonNamesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceFabricClusterCertificateCommonNamesCommonNamesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterCertificateCommonNamesCommonNamesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterCertificateCommonNamesCommonNamesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterCertificateCommonNamesCommonNamesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterCertificateCommonNamesCommonNames]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterCertificateCommonNamesCommonNames]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterCertificateCommonNamesCommonNames]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterCertificateCommonNamesCommonNamesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricClusterCertificateCommonNamesCommonNamesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterCertificateCommonNamesCommonNamesOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterCertificateCommonNamesCommonNamesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCertificateIssuerThumbprint")
    def reset_certificate_issuer_thumbprint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateIssuerThumbprint", []))

    @builtins.property
    @jsii.member(jsii_name="certificateCommonNameInput")
    def certificate_common_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateCommonNameInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateIssuerThumbprintInput")
    def certificate_issuer_thumbprint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateIssuerThumbprintInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateCommonName")
    def certificate_common_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateCommonName"))

    @certificate_common_name.setter
    def certificate_common_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterCertificateCommonNamesCommonNamesOutputReference, "certificate_common_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateCommonName", value)

    @builtins.property
    @jsii.member(jsii_name="certificateIssuerThumbprint")
    def certificate_issuer_thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateIssuerThumbprint"))

    @certificate_issuer_thumbprint.setter
    def certificate_issuer_thumbprint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterCertificateCommonNamesCommonNamesOutputReference, "certificate_issuer_thumbprint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateIssuerThumbprint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceFabricClusterCertificateCommonNamesCommonNames, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceFabricClusterCertificateCommonNamesCommonNames, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceFabricClusterCertificateCommonNamesCommonNames, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterCertificateCommonNamesCommonNamesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricClusterCertificateCommonNamesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterCertificateCommonNamesOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterCertificateCommonNamesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCommonNames")
    def put_common_names(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ServiceFabricClusterCertificateCommonNamesCommonNames, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterCertificateCommonNamesOutputReference.put_common_names)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCommonNames", [value]))

    @builtins.property
    @jsii.member(jsii_name="commonNames")
    def common_names(self) -> ServiceFabricClusterCertificateCommonNamesCommonNamesList:
        return typing.cast(ServiceFabricClusterCertificateCommonNamesCommonNamesList, jsii.get(self, "commonNames"))

    @builtins.property
    @jsii.member(jsii_name="commonNamesInput")
    def common_names_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterCertificateCommonNamesCommonNames]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterCertificateCommonNamesCommonNames]]], jsii.get(self, "commonNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="x509StoreNameInput")
    def x509_store_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "x509StoreNameInput"))

    @builtins.property
    @jsii.member(jsii_name="x509StoreName")
    def x509_store_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "x509StoreName"))

    @x509_store_name.setter
    def x509_store_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterCertificateCommonNamesOutputReference, "x509_store_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "x509StoreName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceFabricClusterCertificateCommonNames]:
        return typing.cast(typing.Optional[ServiceFabricClusterCertificateCommonNames], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceFabricClusterCertificateCommonNames],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterCertificateCommonNamesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricClusterCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterCertificateOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetThumbprintSecondary")
    def reset_thumbprint_secondary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThumbprintSecondary", []))

    @builtins.property
    @jsii.member(jsii_name="thumbprintInput")
    def thumbprint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thumbprintInput"))

    @builtins.property
    @jsii.member(jsii_name="thumbprintSecondaryInput")
    def thumbprint_secondary_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thumbprintSecondaryInput"))

    @builtins.property
    @jsii.member(jsii_name="x509StoreNameInput")
    def x509_store_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "x509StoreNameInput"))

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @thumbprint.setter
    def thumbprint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterCertificateOutputReference, "thumbprint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thumbprint", value)

    @builtins.property
    @jsii.member(jsii_name="thumbprintSecondary")
    def thumbprint_secondary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprintSecondary"))

    @thumbprint_secondary.setter
    def thumbprint_secondary(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterCertificateOutputReference, "thumbprint_secondary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thumbprintSecondary", value)

    @builtins.property
    @jsii.member(jsii_name="x509StoreName")
    def x509_store_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "x509StoreName"))

    @x509_store_name.setter
    def x509_store_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterCertificateOutputReference, "x509_store_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "x509StoreName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceFabricClusterCertificate]:
        return typing.cast(typing.Optional[ServiceFabricClusterCertificate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceFabricClusterCertificate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterClientCertificateCommonName",
    jsii_struct_bases=[],
    name_mapping={
        "common_name": "commonName",
        "is_admin": "isAdmin",
        "issuer_thumbprint": "issuerThumbprint",
    },
)
class ServiceFabricClusterClientCertificateCommonName:
    def __init__(
        self,
        *,
        common_name: builtins.str,
        is_admin: typing.Union[builtins.bool, cdktf.IResolvable],
        issuer_thumbprint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param common_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#common_name ServiceFabricCluster#common_name}.
        :param is_admin: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#is_admin ServiceFabricCluster#is_admin}.
        :param issuer_thumbprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#issuer_thumbprint ServiceFabricCluster#issuer_thumbprint}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterClientCertificateCommonName.__init__)
            check_type(argname="argument common_name", value=common_name, expected_type=type_hints["common_name"])
            check_type(argname="argument is_admin", value=is_admin, expected_type=type_hints["is_admin"])
            check_type(argname="argument issuer_thumbprint", value=issuer_thumbprint, expected_type=type_hints["issuer_thumbprint"])
        self._values: typing.Dict[str, typing.Any] = {
            "common_name": common_name,
            "is_admin": is_admin,
        }
        if issuer_thumbprint is not None:
            self._values["issuer_thumbprint"] = issuer_thumbprint

    @builtins.property
    def common_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#common_name ServiceFabricCluster#common_name}.'''
        result = self._values.get("common_name")
        assert result is not None, "Required property 'common_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_admin(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#is_admin ServiceFabricCluster#is_admin}.'''
        result = self._values.get("is_admin")
        assert result is not None, "Required property 'is_admin' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def issuer_thumbprint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#issuer_thumbprint ServiceFabricCluster#issuer_thumbprint}.'''
        result = self._values.get("issuer_thumbprint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterClientCertificateCommonName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricClusterClientCertificateCommonNameList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterClientCertificateCommonNameList",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterClientCertificateCommonNameList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceFabricClusterClientCertificateCommonNameOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterClientCertificateCommonNameList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceFabricClusterClientCertificateCommonNameOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterClientCertificateCommonNameList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterClientCertificateCommonNameList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterClientCertificateCommonNameList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterClientCertificateCommonName]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterClientCertificateCommonName]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterClientCertificateCommonName]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterClientCertificateCommonNameList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricClusterClientCertificateCommonNameOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterClientCertificateCommonNameOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterClientCertificateCommonNameOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIssuerThumbprint")
    def reset_issuer_thumbprint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuerThumbprint", []))

    @builtins.property
    @jsii.member(jsii_name="commonNameInput")
    def common_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commonNameInput"))

    @builtins.property
    @jsii.member(jsii_name="isAdminInput")
    def is_admin_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isAdminInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerThumbprintInput")
    def issuer_thumbprint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerThumbprintInput"))

    @builtins.property
    @jsii.member(jsii_name="commonName")
    def common_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commonName"))

    @common_name.setter
    def common_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterClientCertificateCommonNameOutputReference, "common_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commonName", value)

    @builtins.property
    @jsii.member(jsii_name="isAdmin")
    def is_admin(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isAdmin"))

    @is_admin.setter
    def is_admin(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterClientCertificateCommonNameOutputReference, "is_admin").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isAdmin", value)

    @builtins.property
    @jsii.member(jsii_name="issuerThumbprint")
    def issuer_thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuerThumbprint"))

    @issuer_thumbprint.setter
    def issuer_thumbprint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterClientCertificateCommonNameOutputReference, "issuer_thumbprint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuerThumbprint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceFabricClusterClientCertificateCommonName, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceFabricClusterClientCertificateCommonName, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceFabricClusterClientCertificateCommonName, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterClientCertificateCommonNameOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterClientCertificateThumbprint",
    jsii_struct_bases=[],
    name_mapping={"is_admin": "isAdmin", "thumbprint": "thumbprint"},
)
class ServiceFabricClusterClientCertificateThumbprint:
    def __init__(
        self,
        *,
        is_admin: typing.Union[builtins.bool, cdktf.IResolvable],
        thumbprint: builtins.str,
    ) -> None:
        '''
        :param is_admin: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#is_admin ServiceFabricCluster#is_admin}.
        :param thumbprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#thumbprint ServiceFabricCluster#thumbprint}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterClientCertificateThumbprint.__init__)
            check_type(argname="argument is_admin", value=is_admin, expected_type=type_hints["is_admin"])
            check_type(argname="argument thumbprint", value=thumbprint, expected_type=type_hints["thumbprint"])
        self._values: typing.Dict[str, typing.Any] = {
            "is_admin": is_admin,
            "thumbprint": thumbprint,
        }

    @builtins.property
    def is_admin(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#is_admin ServiceFabricCluster#is_admin}.'''
        result = self._values.get("is_admin")
        assert result is not None, "Required property 'is_admin' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def thumbprint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#thumbprint ServiceFabricCluster#thumbprint}.'''
        result = self._values.get("thumbprint")
        assert result is not None, "Required property 'thumbprint' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterClientCertificateThumbprint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricClusterClientCertificateThumbprintList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterClientCertificateThumbprintList",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterClientCertificateThumbprintList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceFabricClusterClientCertificateThumbprintOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterClientCertificateThumbprintList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceFabricClusterClientCertificateThumbprintOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterClientCertificateThumbprintList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterClientCertificateThumbprintList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterClientCertificateThumbprintList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterClientCertificateThumbprint]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterClientCertificateThumbprint]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterClientCertificateThumbprint]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterClientCertificateThumbprintList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricClusterClientCertificateThumbprintOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterClientCertificateThumbprintOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterClientCertificateThumbprintOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="isAdminInput")
    def is_admin_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isAdminInput"))

    @builtins.property
    @jsii.member(jsii_name="thumbprintInput")
    def thumbprint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thumbprintInput"))

    @builtins.property
    @jsii.member(jsii_name="isAdmin")
    def is_admin(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isAdmin"))

    @is_admin.setter
    def is_admin(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterClientCertificateThumbprintOutputReference, "is_admin").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isAdmin", value)

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @thumbprint.setter
    def thumbprint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterClientCertificateThumbprintOutputReference, "thumbprint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thumbprint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceFabricClusterClientCertificateThumbprint, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceFabricClusterClientCertificateThumbprint, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceFabricClusterClientCertificateThumbprint, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterClientCertificateThumbprintOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterConfig",
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
        "management_endpoint": "managementEndpoint",
        "name": "name",
        "node_type": "nodeType",
        "reliability_level": "reliabilityLevel",
        "resource_group_name": "resourceGroupName",
        "upgrade_mode": "upgradeMode",
        "vm_image": "vmImage",
        "add_on_features": "addOnFeatures",
        "azure_active_directory": "azureActiveDirectory",
        "certificate": "certificate",
        "certificate_common_names": "certificateCommonNames",
        "client_certificate_common_name": "clientCertificateCommonName",
        "client_certificate_thumbprint": "clientCertificateThumbprint",
        "cluster_code_version": "clusterCodeVersion",
        "diagnostics_config": "diagnosticsConfig",
        "fabric_settings": "fabricSettings",
        "id": "id",
        "reverse_proxy_certificate": "reverseProxyCertificate",
        "reverse_proxy_certificate_common_names": "reverseProxyCertificateCommonNames",
        "service_fabric_zonal_upgrade_mode": "serviceFabricZonalUpgradeMode",
        "tags": "tags",
        "timeouts": "timeouts",
        "upgrade_policy": "upgradePolicy",
        "vmss_zonal_upgrade_mode": "vmssZonalUpgradeMode",
    },
)
class ServiceFabricClusterConfig(cdktf.TerraformMetaArguments):
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
        management_endpoint: builtins.str,
        name: builtins.str,
        node_type: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricClusterNodeType", typing.Dict[str, typing.Any]]]],
        reliability_level: builtins.str,
        resource_group_name: builtins.str,
        upgrade_mode: builtins.str,
        vm_image: builtins.str,
        add_on_features: typing.Optional[typing.Sequence[builtins.str]] = None,
        azure_active_directory: typing.Optional[typing.Union[ServiceFabricClusterAzureActiveDirectory, typing.Dict[str, typing.Any]]] = None,
        certificate: typing.Optional[typing.Union[ServiceFabricClusterCertificate, typing.Dict[str, typing.Any]]] = None,
        certificate_common_names: typing.Optional[typing.Union[ServiceFabricClusterCertificateCommonNames, typing.Dict[str, typing.Any]]] = None,
        client_certificate_common_name: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ServiceFabricClusterClientCertificateCommonName, typing.Dict[str, typing.Any]]]]] = None,
        client_certificate_thumbprint: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ServiceFabricClusterClientCertificateThumbprint, typing.Dict[str, typing.Any]]]]] = None,
        cluster_code_version: typing.Optional[builtins.str] = None,
        diagnostics_config: typing.Optional[typing.Union["ServiceFabricClusterDiagnosticsConfig", typing.Dict[str, typing.Any]]] = None,
        fabric_settings: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricClusterFabricSettings", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        reverse_proxy_certificate: typing.Optional[typing.Union["ServiceFabricClusterReverseProxyCertificate", typing.Dict[str, typing.Any]]] = None,
        reverse_proxy_certificate_common_names: typing.Optional[typing.Union["ServiceFabricClusterReverseProxyCertificateCommonNames", typing.Dict[str, typing.Any]]] = None,
        service_fabric_zonal_upgrade_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ServiceFabricClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        upgrade_policy: typing.Optional[typing.Union["ServiceFabricClusterUpgradePolicy", typing.Dict[str, typing.Any]]] = None,
        vmss_zonal_upgrade_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#location ServiceFabricCluster#location}.
        :param management_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#management_endpoint ServiceFabricCluster#management_endpoint}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#name ServiceFabricCluster#name}.
        :param node_type: node_type block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#node_type ServiceFabricCluster#node_type}
        :param reliability_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#reliability_level ServiceFabricCluster#reliability_level}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#resource_group_name ServiceFabricCluster#resource_group_name}.
        :param upgrade_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#upgrade_mode ServiceFabricCluster#upgrade_mode}.
        :param vm_image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#vm_image ServiceFabricCluster#vm_image}.
        :param add_on_features: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#add_on_features ServiceFabricCluster#add_on_features}.
        :param azure_active_directory: azure_active_directory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#azure_active_directory ServiceFabricCluster#azure_active_directory}
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#certificate ServiceFabricCluster#certificate}
        :param certificate_common_names: certificate_common_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#certificate_common_names ServiceFabricCluster#certificate_common_names}
        :param client_certificate_common_name: client_certificate_common_name block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#client_certificate_common_name ServiceFabricCluster#client_certificate_common_name}
        :param client_certificate_thumbprint: client_certificate_thumbprint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#client_certificate_thumbprint ServiceFabricCluster#client_certificate_thumbprint}
        :param cluster_code_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#cluster_code_version ServiceFabricCluster#cluster_code_version}.
        :param diagnostics_config: diagnostics_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#diagnostics_config ServiceFabricCluster#diagnostics_config}
        :param fabric_settings: fabric_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#fabric_settings ServiceFabricCluster#fabric_settings}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#id ServiceFabricCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param reverse_proxy_certificate: reverse_proxy_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#reverse_proxy_certificate ServiceFabricCluster#reverse_proxy_certificate}
        :param reverse_proxy_certificate_common_names: reverse_proxy_certificate_common_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#reverse_proxy_certificate_common_names ServiceFabricCluster#reverse_proxy_certificate_common_names}
        :param service_fabric_zonal_upgrade_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#service_fabric_zonal_upgrade_mode ServiceFabricCluster#service_fabric_zonal_upgrade_mode}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#tags ServiceFabricCluster#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#timeouts ServiceFabricCluster#timeouts}
        :param upgrade_policy: upgrade_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#upgrade_policy ServiceFabricCluster#upgrade_policy}
        :param vmss_zonal_upgrade_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#vmss_zonal_upgrade_mode ServiceFabricCluster#vmss_zonal_upgrade_mode}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(azure_active_directory, dict):
            azure_active_directory = ServiceFabricClusterAzureActiveDirectory(**azure_active_directory)
        if isinstance(certificate, dict):
            certificate = ServiceFabricClusterCertificate(**certificate)
        if isinstance(certificate_common_names, dict):
            certificate_common_names = ServiceFabricClusterCertificateCommonNames(**certificate_common_names)
        if isinstance(diagnostics_config, dict):
            diagnostics_config = ServiceFabricClusterDiagnosticsConfig(**diagnostics_config)
        if isinstance(reverse_proxy_certificate, dict):
            reverse_proxy_certificate = ServiceFabricClusterReverseProxyCertificate(**reverse_proxy_certificate)
        if isinstance(reverse_proxy_certificate_common_names, dict):
            reverse_proxy_certificate_common_names = ServiceFabricClusterReverseProxyCertificateCommonNames(**reverse_proxy_certificate_common_names)
        if isinstance(timeouts, dict):
            timeouts = ServiceFabricClusterTimeouts(**timeouts)
        if isinstance(upgrade_policy, dict):
            upgrade_policy = ServiceFabricClusterUpgradePolicy(**upgrade_policy)
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument management_endpoint", value=management_endpoint, expected_type=type_hints["management_endpoint"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument node_type", value=node_type, expected_type=type_hints["node_type"])
            check_type(argname="argument reliability_level", value=reliability_level, expected_type=type_hints["reliability_level"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument upgrade_mode", value=upgrade_mode, expected_type=type_hints["upgrade_mode"])
            check_type(argname="argument vm_image", value=vm_image, expected_type=type_hints["vm_image"])
            check_type(argname="argument add_on_features", value=add_on_features, expected_type=type_hints["add_on_features"])
            check_type(argname="argument azure_active_directory", value=azure_active_directory, expected_type=type_hints["azure_active_directory"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument certificate_common_names", value=certificate_common_names, expected_type=type_hints["certificate_common_names"])
            check_type(argname="argument client_certificate_common_name", value=client_certificate_common_name, expected_type=type_hints["client_certificate_common_name"])
            check_type(argname="argument client_certificate_thumbprint", value=client_certificate_thumbprint, expected_type=type_hints["client_certificate_thumbprint"])
            check_type(argname="argument cluster_code_version", value=cluster_code_version, expected_type=type_hints["cluster_code_version"])
            check_type(argname="argument diagnostics_config", value=diagnostics_config, expected_type=type_hints["diagnostics_config"])
            check_type(argname="argument fabric_settings", value=fabric_settings, expected_type=type_hints["fabric_settings"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument reverse_proxy_certificate", value=reverse_proxy_certificate, expected_type=type_hints["reverse_proxy_certificate"])
            check_type(argname="argument reverse_proxy_certificate_common_names", value=reverse_proxy_certificate_common_names, expected_type=type_hints["reverse_proxy_certificate_common_names"])
            check_type(argname="argument service_fabric_zonal_upgrade_mode", value=service_fabric_zonal_upgrade_mode, expected_type=type_hints["service_fabric_zonal_upgrade_mode"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument upgrade_policy", value=upgrade_policy, expected_type=type_hints["upgrade_policy"])
            check_type(argname="argument vmss_zonal_upgrade_mode", value=vmss_zonal_upgrade_mode, expected_type=type_hints["vmss_zonal_upgrade_mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "management_endpoint": management_endpoint,
            "name": name,
            "node_type": node_type,
            "reliability_level": reliability_level,
            "resource_group_name": resource_group_name,
            "upgrade_mode": upgrade_mode,
            "vm_image": vm_image,
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
        if add_on_features is not None:
            self._values["add_on_features"] = add_on_features
        if azure_active_directory is not None:
            self._values["azure_active_directory"] = azure_active_directory
        if certificate is not None:
            self._values["certificate"] = certificate
        if certificate_common_names is not None:
            self._values["certificate_common_names"] = certificate_common_names
        if client_certificate_common_name is not None:
            self._values["client_certificate_common_name"] = client_certificate_common_name
        if client_certificate_thumbprint is not None:
            self._values["client_certificate_thumbprint"] = client_certificate_thumbprint
        if cluster_code_version is not None:
            self._values["cluster_code_version"] = cluster_code_version
        if diagnostics_config is not None:
            self._values["diagnostics_config"] = diagnostics_config
        if fabric_settings is not None:
            self._values["fabric_settings"] = fabric_settings
        if id is not None:
            self._values["id"] = id
        if reverse_proxy_certificate is not None:
            self._values["reverse_proxy_certificate"] = reverse_proxy_certificate
        if reverse_proxy_certificate_common_names is not None:
            self._values["reverse_proxy_certificate_common_names"] = reverse_proxy_certificate_common_names
        if service_fabric_zonal_upgrade_mode is not None:
            self._values["service_fabric_zonal_upgrade_mode"] = service_fabric_zonal_upgrade_mode
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if upgrade_policy is not None:
            self._values["upgrade_policy"] = upgrade_policy
        if vmss_zonal_upgrade_mode is not None:
            self._values["vmss_zonal_upgrade_mode"] = vmss_zonal_upgrade_mode

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#location ServiceFabricCluster#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def management_endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#management_endpoint ServiceFabricCluster#management_endpoint}.'''
        result = self._values.get("management_endpoint")
        assert result is not None, "Required property 'management_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#name ServiceFabricCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def node_type(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ServiceFabricClusterNodeType"]]:
        '''node_type block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#node_type ServiceFabricCluster#node_type}
        '''
        result = self._values.get("node_type")
        assert result is not None, "Required property 'node_type' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ServiceFabricClusterNodeType"]], result)

    @builtins.property
    def reliability_level(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#reliability_level ServiceFabricCluster#reliability_level}.'''
        result = self._values.get("reliability_level")
        assert result is not None, "Required property 'reliability_level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#resource_group_name ServiceFabricCluster#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def upgrade_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#upgrade_mode ServiceFabricCluster#upgrade_mode}.'''
        result = self._values.get("upgrade_mode")
        assert result is not None, "Required property 'upgrade_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vm_image(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#vm_image ServiceFabricCluster#vm_image}.'''
        result = self._values.get("vm_image")
        assert result is not None, "Required property 'vm_image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def add_on_features(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#add_on_features ServiceFabricCluster#add_on_features}.'''
        result = self._values.get("add_on_features")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def azure_active_directory(
        self,
    ) -> typing.Optional[ServiceFabricClusterAzureActiveDirectory]:
        '''azure_active_directory block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#azure_active_directory ServiceFabricCluster#azure_active_directory}
        '''
        result = self._values.get("azure_active_directory")
        return typing.cast(typing.Optional[ServiceFabricClusterAzureActiveDirectory], result)

    @builtins.property
    def certificate(self) -> typing.Optional[ServiceFabricClusterCertificate]:
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#certificate ServiceFabricCluster#certificate}
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[ServiceFabricClusterCertificate], result)

    @builtins.property
    def certificate_common_names(
        self,
    ) -> typing.Optional[ServiceFabricClusterCertificateCommonNames]:
        '''certificate_common_names block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#certificate_common_names ServiceFabricCluster#certificate_common_names}
        '''
        result = self._values.get("certificate_common_names")
        return typing.cast(typing.Optional[ServiceFabricClusterCertificateCommonNames], result)

    @builtins.property
    def client_certificate_common_name(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterClientCertificateCommonName]]]:
        '''client_certificate_common_name block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#client_certificate_common_name ServiceFabricCluster#client_certificate_common_name}
        '''
        result = self._values.get("client_certificate_common_name")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterClientCertificateCommonName]]], result)

    @builtins.property
    def client_certificate_thumbprint(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterClientCertificateThumbprint]]]:
        '''client_certificate_thumbprint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#client_certificate_thumbprint ServiceFabricCluster#client_certificate_thumbprint}
        '''
        result = self._values.get("client_certificate_thumbprint")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterClientCertificateThumbprint]]], result)

    @builtins.property
    def cluster_code_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#cluster_code_version ServiceFabricCluster#cluster_code_version}.'''
        result = self._values.get("cluster_code_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def diagnostics_config(
        self,
    ) -> typing.Optional["ServiceFabricClusterDiagnosticsConfig"]:
        '''diagnostics_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#diagnostics_config ServiceFabricCluster#diagnostics_config}
        '''
        result = self._values.get("diagnostics_config")
        return typing.cast(typing.Optional["ServiceFabricClusterDiagnosticsConfig"], result)

    @builtins.property
    def fabric_settings(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricClusterFabricSettings"]]]:
        '''fabric_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#fabric_settings ServiceFabricCluster#fabric_settings}
        '''
        result = self._values.get("fabric_settings")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceFabricClusterFabricSettings"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#id ServiceFabricCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reverse_proxy_certificate(
        self,
    ) -> typing.Optional["ServiceFabricClusterReverseProxyCertificate"]:
        '''reverse_proxy_certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#reverse_proxy_certificate ServiceFabricCluster#reverse_proxy_certificate}
        '''
        result = self._values.get("reverse_proxy_certificate")
        return typing.cast(typing.Optional["ServiceFabricClusterReverseProxyCertificate"], result)

    @builtins.property
    def reverse_proxy_certificate_common_names(
        self,
    ) -> typing.Optional["ServiceFabricClusterReverseProxyCertificateCommonNames"]:
        '''reverse_proxy_certificate_common_names block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#reverse_proxy_certificate_common_names ServiceFabricCluster#reverse_proxy_certificate_common_names}
        '''
        result = self._values.get("reverse_proxy_certificate_common_names")
        return typing.cast(typing.Optional["ServiceFabricClusterReverseProxyCertificateCommonNames"], result)

    @builtins.property
    def service_fabric_zonal_upgrade_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#service_fabric_zonal_upgrade_mode ServiceFabricCluster#service_fabric_zonal_upgrade_mode}.'''
        result = self._values.get("service_fabric_zonal_upgrade_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#tags ServiceFabricCluster#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ServiceFabricClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#timeouts ServiceFabricCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ServiceFabricClusterTimeouts"], result)

    @builtins.property
    def upgrade_policy(self) -> typing.Optional["ServiceFabricClusterUpgradePolicy"]:
        '''upgrade_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#upgrade_policy ServiceFabricCluster#upgrade_policy}
        '''
        result = self._values.get("upgrade_policy")
        return typing.cast(typing.Optional["ServiceFabricClusterUpgradePolicy"], result)

    @builtins.property
    def vmss_zonal_upgrade_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#vmss_zonal_upgrade_mode ServiceFabricCluster#vmss_zonal_upgrade_mode}.'''
        result = self._values.get("vmss_zonal_upgrade_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterDiagnosticsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "blob_endpoint": "blobEndpoint",
        "protected_account_key_name": "protectedAccountKeyName",
        "queue_endpoint": "queueEndpoint",
        "storage_account_name": "storageAccountName",
        "table_endpoint": "tableEndpoint",
    },
)
class ServiceFabricClusterDiagnosticsConfig:
    def __init__(
        self,
        *,
        blob_endpoint: builtins.str,
        protected_account_key_name: builtins.str,
        queue_endpoint: builtins.str,
        storage_account_name: builtins.str,
        table_endpoint: builtins.str,
    ) -> None:
        '''
        :param blob_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#blob_endpoint ServiceFabricCluster#blob_endpoint}.
        :param protected_account_key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#protected_account_key_name ServiceFabricCluster#protected_account_key_name}.
        :param queue_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#queue_endpoint ServiceFabricCluster#queue_endpoint}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#storage_account_name ServiceFabricCluster#storage_account_name}.
        :param table_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#table_endpoint ServiceFabricCluster#table_endpoint}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterDiagnosticsConfig.__init__)
            check_type(argname="argument blob_endpoint", value=blob_endpoint, expected_type=type_hints["blob_endpoint"])
            check_type(argname="argument protected_account_key_name", value=protected_account_key_name, expected_type=type_hints["protected_account_key_name"])
            check_type(argname="argument queue_endpoint", value=queue_endpoint, expected_type=type_hints["queue_endpoint"])
            check_type(argname="argument storage_account_name", value=storage_account_name, expected_type=type_hints["storage_account_name"])
            check_type(argname="argument table_endpoint", value=table_endpoint, expected_type=type_hints["table_endpoint"])
        self._values: typing.Dict[str, typing.Any] = {
            "blob_endpoint": blob_endpoint,
            "protected_account_key_name": protected_account_key_name,
            "queue_endpoint": queue_endpoint,
            "storage_account_name": storage_account_name,
            "table_endpoint": table_endpoint,
        }

    @builtins.property
    def blob_endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#blob_endpoint ServiceFabricCluster#blob_endpoint}.'''
        result = self._values.get("blob_endpoint")
        assert result is not None, "Required property 'blob_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protected_account_key_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#protected_account_key_name ServiceFabricCluster#protected_account_key_name}.'''
        result = self._values.get("protected_account_key_name")
        assert result is not None, "Required property 'protected_account_key_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def queue_endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#queue_endpoint ServiceFabricCluster#queue_endpoint}.'''
        result = self._values.get("queue_endpoint")
        assert result is not None, "Required property 'queue_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#storage_account_name ServiceFabricCluster#storage_account_name}.'''
        result = self._values.get("storage_account_name")
        assert result is not None, "Required property 'storage_account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#table_endpoint ServiceFabricCluster#table_endpoint}.'''
        result = self._values.get("table_endpoint")
        assert result is not None, "Required property 'table_endpoint' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterDiagnosticsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricClusterDiagnosticsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterDiagnosticsConfigOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterDiagnosticsConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="blobEndpointInput")
    def blob_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blobEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="protectedAccountKeyNameInput")
    def protected_account_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protectedAccountKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="queueEndpointInput")
    def queue_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queueEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountNameInput")
    def storage_account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tableEndpointInput")
    def table_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="blobEndpoint")
    def blob_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "blobEndpoint"))

    @blob_endpoint.setter
    def blob_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterDiagnosticsConfigOutputReference, "blob_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blobEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="protectedAccountKeyName")
    def protected_account_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protectedAccountKeyName"))

    @protected_account_key_name.setter
    def protected_account_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterDiagnosticsConfigOutputReference, "protected_account_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectedAccountKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="queueEndpoint")
    def queue_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queueEndpoint"))

    @queue_endpoint.setter
    def queue_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterDiagnosticsConfigOutputReference, "queue_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queueEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountName")
    def storage_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountName"))

    @storage_account_name.setter
    def storage_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterDiagnosticsConfigOutputReference, "storage_account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="tableEndpoint")
    def table_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableEndpoint"))

    @table_endpoint.setter
    def table_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterDiagnosticsConfigOutputReference, "table_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceFabricClusterDiagnosticsConfig]:
        return typing.cast(typing.Optional[ServiceFabricClusterDiagnosticsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceFabricClusterDiagnosticsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterDiagnosticsConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterFabricSettings",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "parameters": "parameters"},
)
class ServiceFabricClusterFabricSettings:
    def __init__(
        self,
        *,
        name: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#name ServiceFabricCluster#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#parameters ServiceFabricCluster#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterFabricSettings.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#name ServiceFabricCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#parameters ServiceFabricCluster#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterFabricSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricClusterFabricSettingsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterFabricSettingsList",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterFabricSettingsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceFabricClusterFabricSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterFabricSettingsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceFabricClusterFabricSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterFabricSettingsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterFabricSettingsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterFabricSettingsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterFabricSettings]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterFabricSettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterFabricSettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterFabricSettingsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricClusterFabricSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterFabricSettingsOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterFabricSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterFabricSettingsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterFabricSettingsOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceFabricClusterFabricSettings, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceFabricClusterFabricSettings, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceFabricClusterFabricSettings, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterFabricSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterNodeType",
    jsii_struct_bases=[],
    name_mapping={
        "client_endpoint_port": "clientEndpointPort",
        "http_endpoint_port": "httpEndpointPort",
        "instance_count": "instanceCount",
        "is_primary": "isPrimary",
        "name": "name",
        "application_ports": "applicationPorts",
        "capacities": "capacities",
        "durability_level": "durabilityLevel",
        "ephemeral_ports": "ephemeralPorts",
        "is_stateless": "isStateless",
        "multiple_availability_zones": "multipleAvailabilityZones",
        "placement_properties": "placementProperties",
        "reverse_proxy_endpoint_port": "reverseProxyEndpointPort",
    },
)
class ServiceFabricClusterNodeType:
    def __init__(
        self,
        *,
        client_endpoint_port: jsii.Number,
        http_endpoint_port: jsii.Number,
        instance_count: jsii.Number,
        is_primary: typing.Union[builtins.bool, cdktf.IResolvable],
        name: builtins.str,
        application_ports: typing.Optional[typing.Union["ServiceFabricClusterNodeTypeApplicationPorts", typing.Dict[str, typing.Any]]] = None,
        capacities: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        durability_level: typing.Optional[builtins.str] = None,
        ephemeral_ports: typing.Optional[typing.Union["ServiceFabricClusterNodeTypeEphemeralPorts", typing.Dict[str, typing.Any]]] = None,
        is_stateless: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        multiple_availability_zones: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        placement_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        reverse_proxy_endpoint_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param client_endpoint_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#client_endpoint_port ServiceFabricCluster#client_endpoint_port}.
        :param http_endpoint_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#http_endpoint_port ServiceFabricCluster#http_endpoint_port}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#instance_count ServiceFabricCluster#instance_count}.
        :param is_primary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#is_primary ServiceFabricCluster#is_primary}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#name ServiceFabricCluster#name}.
        :param application_ports: application_ports block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#application_ports ServiceFabricCluster#application_ports}
        :param capacities: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#capacities ServiceFabricCluster#capacities}.
        :param durability_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#durability_level ServiceFabricCluster#durability_level}.
        :param ephemeral_ports: ephemeral_ports block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#ephemeral_ports ServiceFabricCluster#ephemeral_ports}
        :param is_stateless: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#is_stateless ServiceFabricCluster#is_stateless}.
        :param multiple_availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#multiple_availability_zones ServiceFabricCluster#multiple_availability_zones}.
        :param placement_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#placement_properties ServiceFabricCluster#placement_properties}.
        :param reverse_proxy_endpoint_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#reverse_proxy_endpoint_port ServiceFabricCluster#reverse_proxy_endpoint_port}.
        '''
        if isinstance(application_ports, dict):
            application_ports = ServiceFabricClusterNodeTypeApplicationPorts(**application_ports)
        if isinstance(ephemeral_ports, dict):
            ephemeral_ports = ServiceFabricClusterNodeTypeEphemeralPorts(**ephemeral_ports)
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterNodeType.__init__)
            check_type(argname="argument client_endpoint_port", value=client_endpoint_port, expected_type=type_hints["client_endpoint_port"])
            check_type(argname="argument http_endpoint_port", value=http_endpoint_port, expected_type=type_hints["http_endpoint_port"])
            check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
            check_type(argname="argument is_primary", value=is_primary, expected_type=type_hints["is_primary"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument application_ports", value=application_ports, expected_type=type_hints["application_ports"])
            check_type(argname="argument capacities", value=capacities, expected_type=type_hints["capacities"])
            check_type(argname="argument durability_level", value=durability_level, expected_type=type_hints["durability_level"])
            check_type(argname="argument ephemeral_ports", value=ephemeral_ports, expected_type=type_hints["ephemeral_ports"])
            check_type(argname="argument is_stateless", value=is_stateless, expected_type=type_hints["is_stateless"])
            check_type(argname="argument multiple_availability_zones", value=multiple_availability_zones, expected_type=type_hints["multiple_availability_zones"])
            check_type(argname="argument placement_properties", value=placement_properties, expected_type=type_hints["placement_properties"])
            check_type(argname="argument reverse_proxy_endpoint_port", value=reverse_proxy_endpoint_port, expected_type=type_hints["reverse_proxy_endpoint_port"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_endpoint_port": client_endpoint_port,
            "http_endpoint_port": http_endpoint_port,
            "instance_count": instance_count,
            "is_primary": is_primary,
            "name": name,
        }
        if application_ports is not None:
            self._values["application_ports"] = application_ports
        if capacities is not None:
            self._values["capacities"] = capacities
        if durability_level is not None:
            self._values["durability_level"] = durability_level
        if ephemeral_ports is not None:
            self._values["ephemeral_ports"] = ephemeral_ports
        if is_stateless is not None:
            self._values["is_stateless"] = is_stateless
        if multiple_availability_zones is not None:
            self._values["multiple_availability_zones"] = multiple_availability_zones
        if placement_properties is not None:
            self._values["placement_properties"] = placement_properties
        if reverse_proxy_endpoint_port is not None:
            self._values["reverse_proxy_endpoint_port"] = reverse_proxy_endpoint_port

    @builtins.property
    def client_endpoint_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#client_endpoint_port ServiceFabricCluster#client_endpoint_port}.'''
        result = self._values.get("client_endpoint_port")
        assert result is not None, "Required property 'client_endpoint_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def http_endpoint_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#http_endpoint_port ServiceFabricCluster#http_endpoint_port}.'''
        result = self._values.get("http_endpoint_port")
        assert result is not None, "Required property 'http_endpoint_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def instance_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#instance_count ServiceFabricCluster#instance_count}.'''
        result = self._values.get("instance_count")
        assert result is not None, "Required property 'instance_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def is_primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#is_primary ServiceFabricCluster#is_primary}.'''
        result = self._values.get("is_primary")
        assert result is not None, "Required property 'is_primary' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#name ServiceFabricCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_ports(
        self,
    ) -> typing.Optional["ServiceFabricClusterNodeTypeApplicationPorts"]:
        '''application_ports block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#application_ports ServiceFabricCluster#application_ports}
        '''
        result = self._values.get("application_ports")
        return typing.cast(typing.Optional["ServiceFabricClusterNodeTypeApplicationPorts"], result)

    @builtins.property
    def capacities(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#capacities ServiceFabricCluster#capacities}.'''
        result = self._values.get("capacities")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def durability_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#durability_level ServiceFabricCluster#durability_level}.'''
        result = self._values.get("durability_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ephemeral_ports(
        self,
    ) -> typing.Optional["ServiceFabricClusterNodeTypeEphemeralPorts"]:
        '''ephemeral_ports block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#ephemeral_ports ServiceFabricCluster#ephemeral_ports}
        '''
        result = self._values.get("ephemeral_ports")
        return typing.cast(typing.Optional["ServiceFabricClusterNodeTypeEphemeralPorts"], result)

    @builtins.property
    def is_stateless(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#is_stateless ServiceFabricCluster#is_stateless}.'''
        result = self._values.get("is_stateless")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def multiple_availability_zones(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#multiple_availability_zones ServiceFabricCluster#multiple_availability_zones}.'''
        result = self._values.get("multiple_availability_zones")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def placement_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#placement_properties ServiceFabricCluster#placement_properties}.'''
        result = self._values.get("placement_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def reverse_proxy_endpoint_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#reverse_proxy_endpoint_port ServiceFabricCluster#reverse_proxy_endpoint_port}.'''
        result = self._values.get("reverse_proxy_endpoint_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterNodeType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterNodeTypeApplicationPorts",
    jsii_struct_bases=[],
    name_mapping={"end_port": "endPort", "start_port": "startPort"},
)
class ServiceFabricClusterNodeTypeApplicationPorts:
    def __init__(self, *, end_port: jsii.Number, start_port: jsii.Number) -> None:
        '''
        :param end_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#end_port ServiceFabricCluster#end_port}.
        :param start_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#start_port ServiceFabricCluster#start_port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterNodeTypeApplicationPorts.__init__)
            check_type(argname="argument end_port", value=end_port, expected_type=type_hints["end_port"])
            check_type(argname="argument start_port", value=start_port, expected_type=type_hints["start_port"])
        self._values: typing.Dict[str, typing.Any] = {
            "end_port": end_port,
            "start_port": start_port,
        }

    @builtins.property
    def end_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#end_port ServiceFabricCluster#end_port}.'''
        result = self._values.get("end_port")
        assert result is not None, "Required property 'end_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def start_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#start_port ServiceFabricCluster#start_port}.'''
        result = self._values.get("start_port")
        assert result is not None, "Required property 'start_port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterNodeTypeApplicationPorts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricClusterNodeTypeApplicationPortsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterNodeTypeApplicationPortsOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterNodeTypeApplicationPortsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endPortInput")
    def end_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "endPortInput"))

    @builtins.property
    @jsii.member(jsii_name="startPortInput")
    def start_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startPortInput"))

    @builtins.property
    @jsii.member(jsii_name="endPort")
    def end_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "endPort"))

    @end_port.setter
    def end_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeApplicationPortsOutputReference, "end_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endPort", value)

    @builtins.property
    @jsii.member(jsii_name="startPort")
    def start_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startPort"))

    @start_port.setter
    def start_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeApplicationPortsOutputReference, "start_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startPort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceFabricClusterNodeTypeApplicationPorts]:
        return typing.cast(typing.Optional[ServiceFabricClusterNodeTypeApplicationPorts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceFabricClusterNodeTypeApplicationPorts],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeApplicationPortsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterNodeTypeEphemeralPorts",
    jsii_struct_bases=[],
    name_mapping={"end_port": "endPort", "start_port": "startPort"},
)
class ServiceFabricClusterNodeTypeEphemeralPorts:
    def __init__(self, *, end_port: jsii.Number, start_port: jsii.Number) -> None:
        '''
        :param end_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#end_port ServiceFabricCluster#end_port}.
        :param start_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#start_port ServiceFabricCluster#start_port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterNodeTypeEphemeralPorts.__init__)
            check_type(argname="argument end_port", value=end_port, expected_type=type_hints["end_port"])
            check_type(argname="argument start_port", value=start_port, expected_type=type_hints["start_port"])
        self._values: typing.Dict[str, typing.Any] = {
            "end_port": end_port,
            "start_port": start_port,
        }

    @builtins.property
    def end_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#end_port ServiceFabricCluster#end_port}.'''
        result = self._values.get("end_port")
        assert result is not None, "Required property 'end_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def start_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#start_port ServiceFabricCluster#start_port}.'''
        result = self._values.get("start_port")
        assert result is not None, "Required property 'start_port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterNodeTypeEphemeralPorts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricClusterNodeTypeEphemeralPortsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterNodeTypeEphemeralPortsOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterNodeTypeEphemeralPortsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endPortInput")
    def end_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "endPortInput"))

    @builtins.property
    @jsii.member(jsii_name="startPortInput")
    def start_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startPortInput"))

    @builtins.property
    @jsii.member(jsii_name="endPort")
    def end_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "endPort"))

    @end_port.setter
    def end_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeEphemeralPortsOutputReference, "end_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endPort", value)

    @builtins.property
    @jsii.member(jsii_name="startPort")
    def start_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startPort"))

    @start_port.setter
    def start_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeEphemeralPortsOutputReference, "start_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startPort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceFabricClusterNodeTypeEphemeralPorts]:
        return typing.cast(typing.Optional[ServiceFabricClusterNodeTypeEphemeralPorts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceFabricClusterNodeTypeEphemeralPorts],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeEphemeralPortsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricClusterNodeTypeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterNodeTypeList",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterNodeTypeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ServiceFabricClusterNodeTypeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterNodeTypeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceFabricClusterNodeTypeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterNodeType]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterNodeType]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterNodeType]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricClusterNodeTypeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterNodeTypeOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterNodeTypeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putApplicationPorts")
    def put_application_ports(
        self,
        *,
        end_port: jsii.Number,
        start_port: jsii.Number,
    ) -> None:
        '''
        :param end_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#end_port ServiceFabricCluster#end_port}.
        :param start_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#start_port ServiceFabricCluster#start_port}.
        '''
        value = ServiceFabricClusterNodeTypeApplicationPorts(
            end_port=end_port, start_port=start_port
        )

        return typing.cast(None, jsii.invoke(self, "putApplicationPorts", [value]))

    @jsii.member(jsii_name="putEphemeralPorts")
    def put_ephemeral_ports(
        self,
        *,
        end_port: jsii.Number,
        start_port: jsii.Number,
    ) -> None:
        '''
        :param end_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#end_port ServiceFabricCluster#end_port}.
        :param start_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#start_port ServiceFabricCluster#start_port}.
        '''
        value = ServiceFabricClusterNodeTypeEphemeralPorts(
            end_port=end_port, start_port=start_port
        )

        return typing.cast(None, jsii.invoke(self, "putEphemeralPorts", [value]))

    @jsii.member(jsii_name="resetApplicationPorts")
    def reset_application_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationPorts", []))

    @jsii.member(jsii_name="resetCapacities")
    def reset_capacities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacities", []))

    @jsii.member(jsii_name="resetDurabilityLevel")
    def reset_durability_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDurabilityLevel", []))

    @jsii.member(jsii_name="resetEphemeralPorts")
    def reset_ephemeral_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEphemeralPorts", []))

    @jsii.member(jsii_name="resetIsStateless")
    def reset_is_stateless(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsStateless", []))

    @jsii.member(jsii_name="resetMultipleAvailabilityZones")
    def reset_multiple_availability_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMultipleAvailabilityZones", []))

    @jsii.member(jsii_name="resetPlacementProperties")
    def reset_placement_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacementProperties", []))

    @jsii.member(jsii_name="resetReverseProxyEndpointPort")
    def reset_reverse_proxy_endpoint_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReverseProxyEndpointPort", []))

    @builtins.property
    @jsii.member(jsii_name="applicationPorts")
    def application_ports(
        self,
    ) -> ServiceFabricClusterNodeTypeApplicationPortsOutputReference:
        return typing.cast(ServiceFabricClusterNodeTypeApplicationPortsOutputReference, jsii.get(self, "applicationPorts"))

    @builtins.property
    @jsii.member(jsii_name="ephemeralPorts")
    def ephemeral_ports(
        self,
    ) -> ServiceFabricClusterNodeTypeEphemeralPortsOutputReference:
        return typing.cast(ServiceFabricClusterNodeTypeEphemeralPortsOutputReference, jsii.get(self, "ephemeralPorts"))

    @builtins.property
    @jsii.member(jsii_name="applicationPortsInput")
    def application_ports_input(
        self,
    ) -> typing.Optional[ServiceFabricClusterNodeTypeApplicationPorts]:
        return typing.cast(typing.Optional[ServiceFabricClusterNodeTypeApplicationPorts], jsii.get(self, "applicationPortsInput"))

    @builtins.property
    @jsii.member(jsii_name="capacitiesInput")
    def capacities_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "capacitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="clientEndpointPortInput")
    def client_endpoint_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "clientEndpointPortInput"))

    @builtins.property
    @jsii.member(jsii_name="durabilityLevelInput")
    def durability_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "durabilityLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="ephemeralPortsInput")
    def ephemeral_ports_input(
        self,
    ) -> typing.Optional[ServiceFabricClusterNodeTypeEphemeralPorts]:
        return typing.cast(typing.Optional[ServiceFabricClusterNodeTypeEphemeralPorts], jsii.get(self, "ephemeralPortsInput"))

    @builtins.property
    @jsii.member(jsii_name="httpEndpointPortInput")
    def http_endpoint_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpEndpointPortInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceCountInput")
    def instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="isPrimaryInput")
    def is_primary_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isPrimaryInput"))

    @builtins.property
    @jsii.member(jsii_name="isStatelessInput")
    def is_stateless_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isStatelessInput"))

    @builtins.property
    @jsii.member(jsii_name="multipleAvailabilityZonesInput")
    def multiple_availability_zones_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "multipleAvailabilityZonesInput"))

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
    @jsii.member(jsii_name="reverseProxyEndpointPortInput")
    def reverse_proxy_endpoint_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "reverseProxyEndpointPortInput"))

    @builtins.property
    @jsii.member(jsii_name="capacities")
    def capacities(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "capacities"))

    @capacities.setter
    def capacities(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeOutputReference, "capacities").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacities", value)

    @builtins.property
    @jsii.member(jsii_name="clientEndpointPort")
    def client_endpoint_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "clientEndpointPort"))

    @client_endpoint_port.setter
    def client_endpoint_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeOutputReference, "client_endpoint_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientEndpointPort", value)

    @builtins.property
    @jsii.member(jsii_name="durabilityLevel")
    def durability_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "durabilityLevel"))

    @durability_level.setter
    def durability_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeOutputReference, "durability_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "durabilityLevel", value)

    @builtins.property
    @jsii.member(jsii_name="httpEndpointPort")
    def http_endpoint_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpEndpointPort"))

    @http_endpoint_port.setter
    def http_endpoint_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeOutputReference, "http_endpoint_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpEndpointPort", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeOutputReference, "instance_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="isPrimary")
    def is_primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isPrimary"))

    @is_primary.setter
    def is_primary(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeOutputReference, "is_primary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isPrimary", value)

    @builtins.property
    @jsii.member(jsii_name="isStateless")
    def is_stateless(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isStateless"))

    @is_stateless.setter
    def is_stateless(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeOutputReference, "is_stateless").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isStateless", value)

    @builtins.property
    @jsii.member(jsii_name="multipleAvailabilityZones")
    def multiple_availability_zones(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "multipleAvailabilityZones"))

    @multiple_availability_zones.setter
    def multiple_availability_zones(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeOutputReference, "multiple_availability_zones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multipleAvailabilityZones", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeOutputReference, "name").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeOutputReference, "placement_properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placementProperties", value)

    @builtins.property
    @jsii.member(jsii_name="reverseProxyEndpointPort")
    def reverse_proxy_endpoint_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "reverseProxyEndpointPort"))

    @reverse_proxy_endpoint_port.setter
    def reverse_proxy_endpoint_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeOutputReference, "reverse_proxy_endpoint_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reverseProxyEndpointPort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceFabricClusterNodeType, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceFabricClusterNodeType, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceFabricClusterNodeType, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterNodeTypeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterReverseProxyCertificate",
    jsii_struct_bases=[],
    name_mapping={
        "thumbprint": "thumbprint",
        "x509_store_name": "x509StoreName",
        "thumbprint_secondary": "thumbprintSecondary",
    },
)
class ServiceFabricClusterReverseProxyCertificate:
    def __init__(
        self,
        *,
        thumbprint: builtins.str,
        x509_store_name: builtins.str,
        thumbprint_secondary: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param thumbprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#thumbprint ServiceFabricCluster#thumbprint}.
        :param x509_store_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#x509_store_name ServiceFabricCluster#x509_store_name}.
        :param thumbprint_secondary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#thumbprint_secondary ServiceFabricCluster#thumbprint_secondary}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterReverseProxyCertificate.__init__)
            check_type(argname="argument thumbprint", value=thumbprint, expected_type=type_hints["thumbprint"])
            check_type(argname="argument x509_store_name", value=x509_store_name, expected_type=type_hints["x509_store_name"])
            check_type(argname="argument thumbprint_secondary", value=thumbprint_secondary, expected_type=type_hints["thumbprint_secondary"])
        self._values: typing.Dict[str, typing.Any] = {
            "thumbprint": thumbprint,
            "x509_store_name": x509_store_name,
        }
        if thumbprint_secondary is not None:
            self._values["thumbprint_secondary"] = thumbprint_secondary

    @builtins.property
    def thumbprint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#thumbprint ServiceFabricCluster#thumbprint}.'''
        result = self._values.get("thumbprint")
        assert result is not None, "Required property 'thumbprint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def x509_store_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#x509_store_name ServiceFabricCluster#x509_store_name}.'''
        result = self._values.get("x509_store_name")
        assert result is not None, "Required property 'x509_store_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def thumbprint_secondary(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#thumbprint_secondary ServiceFabricCluster#thumbprint_secondary}.'''
        result = self._values.get("thumbprint_secondary")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterReverseProxyCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterReverseProxyCertificateCommonNames",
    jsii_struct_bases=[],
    name_mapping={"common_names": "commonNames", "x509_store_name": "x509StoreName"},
)
class ServiceFabricClusterReverseProxyCertificateCommonNames:
    def __init__(
        self,
        *,
        common_names: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNames", typing.Dict[str, typing.Any]]]],
        x509_store_name: builtins.str,
    ) -> None:
        '''
        :param common_names: common_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#common_names ServiceFabricCluster#common_names}
        :param x509_store_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#x509_store_name ServiceFabricCluster#x509_store_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterReverseProxyCertificateCommonNames.__init__)
            check_type(argname="argument common_names", value=common_names, expected_type=type_hints["common_names"])
            check_type(argname="argument x509_store_name", value=x509_store_name, expected_type=type_hints["x509_store_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "common_names": common_names,
            "x509_store_name": x509_store_name,
        }

    @builtins.property
    def common_names(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNames"]]:
        '''common_names block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#common_names ServiceFabricCluster#common_names}
        '''
        result = self._values.get("common_names")
        assert result is not None, "Required property 'common_names' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNames"]], result)

    @builtins.property
    def x509_store_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#x509_store_name ServiceFabricCluster#x509_store_name}.'''
        result = self._values.get("x509_store_name")
        assert result is not None, "Required property 'x509_store_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterReverseProxyCertificateCommonNames(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNames",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_common_name": "certificateCommonName",
        "certificate_issuer_thumbprint": "certificateIssuerThumbprint",
    },
)
class ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNames:
    def __init__(
        self,
        *,
        certificate_common_name: builtins.str,
        certificate_issuer_thumbprint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param certificate_common_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#certificate_common_name ServiceFabricCluster#certificate_common_name}.
        :param certificate_issuer_thumbprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#certificate_issuer_thumbprint ServiceFabricCluster#certificate_issuer_thumbprint}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNames.__init__)
            check_type(argname="argument certificate_common_name", value=certificate_common_name, expected_type=type_hints["certificate_common_name"])
            check_type(argname="argument certificate_issuer_thumbprint", value=certificate_issuer_thumbprint, expected_type=type_hints["certificate_issuer_thumbprint"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate_common_name": certificate_common_name,
        }
        if certificate_issuer_thumbprint is not None:
            self._values["certificate_issuer_thumbprint"] = certificate_issuer_thumbprint

    @builtins.property
    def certificate_common_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#certificate_common_name ServiceFabricCluster#certificate_common_name}.'''
        result = self._values.get("certificate_common_name")
        assert result is not None, "Required property 'certificate_common_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_issuer_thumbprint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#certificate_issuer_thumbprint ServiceFabricCluster#certificate_issuer_thumbprint}.'''
        result = self._values.get("certificate_issuer_thumbprint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNames(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesList",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNames]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNames]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNames]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCertificateIssuerThumbprint")
    def reset_certificate_issuer_thumbprint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateIssuerThumbprint", []))

    @builtins.property
    @jsii.member(jsii_name="certificateCommonNameInput")
    def certificate_common_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateCommonNameInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateIssuerThumbprintInput")
    def certificate_issuer_thumbprint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateIssuerThumbprintInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateCommonName")
    def certificate_common_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateCommonName"))

    @certificate_common_name.setter
    def certificate_common_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesOutputReference, "certificate_common_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateCommonName", value)

    @builtins.property
    @jsii.member(jsii_name="certificateIssuerThumbprint")
    def certificate_issuer_thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateIssuerThumbprint"))

    @certificate_issuer_thumbprint.setter
    def certificate_issuer_thumbprint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesOutputReference, "certificate_issuer_thumbprint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateIssuerThumbprint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNames, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNames, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNames, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricClusterReverseProxyCertificateCommonNamesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterReverseProxyCertificateCommonNamesOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterReverseProxyCertificateCommonNamesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCommonNames")
    def put_common_names(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNames, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterReverseProxyCertificateCommonNamesOutputReference.put_common_names)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCommonNames", [value]))

    @builtins.property
    @jsii.member(jsii_name="commonNames")
    def common_names(
        self,
    ) -> ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesList:
        return typing.cast(ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesList, jsii.get(self, "commonNames"))

    @builtins.property
    @jsii.member(jsii_name="commonNamesInput")
    def common_names_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNames]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNames]]], jsii.get(self, "commonNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="x509StoreNameInput")
    def x509_store_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "x509StoreNameInput"))

    @builtins.property
    @jsii.member(jsii_name="x509StoreName")
    def x509_store_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "x509StoreName"))

    @x509_store_name.setter
    def x509_store_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterReverseProxyCertificateCommonNamesOutputReference, "x509_store_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "x509StoreName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceFabricClusterReverseProxyCertificateCommonNames]:
        return typing.cast(typing.Optional[ServiceFabricClusterReverseProxyCertificateCommonNames], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceFabricClusterReverseProxyCertificateCommonNames],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterReverseProxyCertificateCommonNamesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricClusterReverseProxyCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterReverseProxyCertificateOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterReverseProxyCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetThumbprintSecondary")
    def reset_thumbprint_secondary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThumbprintSecondary", []))

    @builtins.property
    @jsii.member(jsii_name="thumbprintInput")
    def thumbprint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thumbprintInput"))

    @builtins.property
    @jsii.member(jsii_name="thumbprintSecondaryInput")
    def thumbprint_secondary_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thumbprintSecondaryInput"))

    @builtins.property
    @jsii.member(jsii_name="x509StoreNameInput")
    def x509_store_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "x509StoreNameInput"))

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @thumbprint.setter
    def thumbprint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterReverseProxyCertificateOutputReference, "thumbprint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thumbprint", value)

    @builtins.property
    @jsii.member(jsii_name="thumbprintSecondary")
    def thumbprint_secondary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprintSecondary"))

    @thumbprint_secondary.setter
    def thumbprint_secondary(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterReverseProxyCertificateOutputReference, "thumbprint_secondary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thumbprintSecondary", value)

    @builtins.property
    @jsii.member(jsii_name="x509StoreName")
    def x509_store_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "x509StoreName"))

    @x509_store_name.setter
    def x509_store_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterReverseProxyCertificateOutputReference, "x509_store_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "x509StoreName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceFabricClusterReverseProxyCertificate]:
        return typing.cast(typing.Optional[ServiceFabricClusterReverseProxyCertificate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceFabricClusterReverseProxyCertificate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterReverseProxyCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ServiceFabricClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#create ServiceFabricCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#delete ServiceFabricCluster#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#read ServiceFabricCluster#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#update ServiceFabricCluster#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#create ServiceFabricCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#delete ServiceFabricCluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#read ServiceFabricCluster#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#update ServiceFabricCluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricClusterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceFabricClusterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceFabricClusterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceFabricClusterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterUpgradePolicy",
    jsii_struct_bases=[],
    name_mapping={
        "delta_health_policy": "deltaHealthPolicy",
        "force_restart_enabled": "forceRestartEnabled",
        "health_check_retry_timeout": "healthCheckRetryTimeout",
        "health_check_stable_duration": "healthCheckStableDuration",
        "health_check_wait_duration": "healthCheckWaitDuration",
        "health_policy": "healthPolicy",
        "upgrade_domain_timeout": "upgradeDomainTimeout",
        "upgrade_replica_set_check_timeout": "upgradeReplicaSetCheckTimeout",
        "upgrade_timeout": "upgradeTimeout",
    },
)
class ServiceFabricClusterUpgradePolicy:
    def __init__(
        self,
        *,
        delta_health_policy: typing.Optional[typing.Union["ServiceFabricClusterUpgradePolicyDeltaHealthPolicy", typing.Dict[str, typing.Any]]] = None,
        force_restart_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_check_retry_timeout: typing.Optional[builtins.str] = None,
        health_check_stable_duration: typing.Optional[builtins.str] = None,
        health_check_wait_duration: typing.Optional[builtins.str] = None,
        health_policy: typing.Optional[typing.Union["ServiceFabricClusterUpgradePolicyHealthPolicy", typing.Dict[str, typing.Any]]] = None,
        upgrade_domain_timeout: typing.Optional[builtins.str] = None,
        upgrade_replica_set_check_timeout: typing.Optional[builtins.str] = None,
        upgrade_timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delta_health_policy: delta_health_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#delta_health_policy ServiceFabricCluster#delta_health_policy}
        :param force_restart_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#force_restart_enabled ServiceFabricCluster#force_restart_enabled}.
        :param health_check_retry_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#health_check_retry_timeout ServiceFabricCluster#health_check_retry_timeout}.
        :param health_check_stable_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#health_check_stable_duration ServiceFabricCluster#health_check_stable_duration}.
        :param health_check_wait_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#health_check_wait_duration ServiceFabricCluster#health_check_wait_duration}.
        :param health_policy: health_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#health_policy ServiceFabricCluster#health_policy}
        :param upgrade_domain_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#upgrade_domain_timeout ServiceFabricCluster#upgrade_domain_timeout}.
        :param upgrade_replica_set_check_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#upgrade_replica_set_check_timeout ServiceFabricCluster#upgrade_replica_set_check_timeout}.
        :param upgrade_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#upgrade_timeout ServiceFabricCluster#upgrade_timeout}.
        '''
        if isinstance(delta_health_policy, dict):
            delta_health_policy = ServiceFabricClusterUpgradePolicyDeltaHealthPolicy(**delta_health_policy)
        if isinstance(health_policy, dict):
            health_policy = ServiceFabricClusterUpgradePolicyHealthPolicy(**health_policy)
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterUpgradePolicy.__init__)
            check_type(argname="argument delta_health_policy", value=delta_health_policy, expected_type=type_hints["delta_health_policy"])
            check_type(argname="argument force_restart_enabled", value=force_restart_enabled, expected_type=type_hints["force_restart_enabled"])
            check_type(argname="argument health_check_retry_timeout", value=health_check_retry_timeout, expected_type=type_hints["health_check_retry_timeout"])
            check_type(argname="argument health_check_stable_duration", value=health_check_stable_duration, expected_type=type_hints["health_check_stable_duration"])
            check_type(argname="argument health_check_wait_duration", value=health_check_wait_duration, expected_type=type_hints["health_check_wait_duration"])
            check_type(argname="argument health_policy", value=health_policy, expected_type=type_hints["health_policy"])
            check_type(argname="argument upgrade_domain_timeout", value=upgrade_domain_timeout, expected_type=type_hints["upgrade_domain_timeout"])
            check_type(argname="argument upgrade_replica_set_check_timeout", value=upgrade_replica_set_check_timeout, expected_type=type_hints["upgrade_replica_set_check_timeout"])
            check_type(argname="argument upgrade_timeout", value=upgrade_timeout, expected_type=type_hints["upgrade_timeout"])
        self._values: typing.Dict[str, typing.Any] = {}
        if delta_health_policy is not None:
            self._values["delta_health_policy"] = delta_health_policy
        if force_restart_enabled is not None:
            self._values["force_restart_enabled"] = force_restart_enabled
        if health_check_retry_timeout is not None:
            self._values["health_check_retry_timeout"] = health_check_retry_timeout
        if health_check_stable_duration is not None:
            self._values["health_check_stable_duration"] = health_check_stable_duration
        if health_check_wait_duration is not None:
            self._values["health_check_wait_duration"] = health_check_wait_duration
        if health_policy is not None:
            self._values["health_policy"] = health_policy
        if upgrade_domain_timeout is not None:
            self._values["upgrade_domain_timeout"] = upgrade_domain_timeout
        if upgrade_replica_set_check_timeout is not None:
            self._values["upgrade_replica_set_check_timeout"] = upgrade_replica_set_check_timeout
        if upgrade_timeout is not None:
            self._values["upgrade_timeout"] = upgrade_timeout

    @builtins.property
    def delta_health_policy(
        self,
    ) -> typing.Optional["ServiceFabricClusterUpgradePolicyDeltaHealthPolicy"]:
        '''delta_health_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#delta_health_policy ServiceFabricCluster#delta_health_policy}
        '''
        result = self._values.get("delta_health_policy")
        return typing.cast(typing.Optional["ServiceFabricClusterUpgradePolicyDeltaHealthPolicy"], result)

    @builtins.property
    def force_restart_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#force_restart_enabled ServiceFabricCluster#force_restart_enabled}.'''
        result = self._values.get("force_restart_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def health_check_retry_timeout(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#health_check_retry_timeout ServiceFabricCluster#health_check_retry_timeout}.'''
        result = self._values.get("health_check_retry_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_stable_duration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#health_check_stable_duration ServiceFabricCluster#health_check_stable_duration}.'''
        result = self._values.get("health_check_stable_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_wait_duration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#health_check_wait_duration ServiceFabricCluster#health_check_wait_duration}.'''
        result = self._values.get("health_check_wait_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_policy(
        self,
    ) -> typing.Optional["ServiceFabricClusterUpgradePolicyHealthPolicy"]:
        '''health_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#health_policy ServiceFabricCluster#health_policy}
        '''
        result = self._values.get("health_policy")
        return typing.cast(typing.Optional["ServiceFabricClusterUpgradePolicyHealthPolicy"], result)

    @builtins.property
    def upgrade_domain_timeout(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#upgrade_domain_timeout ServiceFabricCluster#upgrade_domain_timeout}.'''
        result = self._values.get("upgrade_domain_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def upgrade_replica_set_check_timeout(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#upgrade_replica_set_check_timeout ServiceFabricCluster#upgrade_replica_set_check_timeout}.'''
        result = self._values.get("upgrade_replica_set_check_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def upgrade_timeout(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#upgrade_timeout ServiceFabricCluster#upgrade_timeout}.'''
        result = self._values.get("upgrade_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterUpgradePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterUpgradePolicyDeltaHealthPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "max_delta_unhealthy_applications_percent": "maxDeltaUnhealthyApplicationsPercent",
        "max_delta_unhealthy_nodes_percent": "maxDeltaUnhealthyNodesPercent",
        "max_upgrade_domain_delta_unhealthy_nodes_percent": "maxUpgradeDomainDeltaUnhealthyNodesPercent",
    },
)
class ServiceFabricClusterUpgradePolicyDeltaHealthPolicy:
    def __init__(
        self,
        *,
        max_delta_unhealthy_applications_percent: typing.Optional[jsii.Number] = None,
        max_delta_unhealthy_nodes_percent: typing.Optional[jsii.Number] = None,
        max_upgrade_domain_delta_unhealthy_nodes_percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_delta_unhealthy_applications_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#max_delta_unhealthy_applications_percent ServiceFabricCluster#max_delta_unhealthy_applications_percent}.
        :param max_delta_unhealthy_nodes_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#max_delta_unhealthy_nodes_percent ServiceFabricCluster#max_delta_unhealthy_nodes_percent}.
        :param max_upgrade_domain_delta_unhealthy_nodes_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#max_upgrade_domain_delta_unhealthy_nodes_percent ServiceFabricCluster#max_upgrade_domain_delta_unhealthy_nodes_percent}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterUpgradePolicyDeltaHealthPolicy.__init__)
            check_type(argname="argument max_delta_unhealthy_applications_percent", value=max_delta_unhealthy_applications_percent, expected_type=type_hints["max_delta_unhealthy_applications_percent"])
            check_type(argname="argument max_delta_unhealthy_nodes_percent", value=max_delta_unhealthy_nodes_percent, expected_type=type_hints["max_delta_unhealthy_nodes_percent"])
            check_type(argname="argument max_upgrade_domain_delta_unhealthy_nodes_percent", value=max_upgrade_domain_delta_unhealthy_nodes_percent, expected_type=type_hints["max_upgrade_domain_delta_unhealthy_nodes_percent"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_delta_unhealthy_applications_percent is not None:
            self._values["max_delta_unhealthy_applications_percent"] = max_delta_unhealthy_applications_percent
        if max_delta_unhealthy_nodes_percent is not None:
            self._values["max_delta_unhealthy_nodes_percent"] = max_delta_unhealthy_nodes_percent
        if max_upgrade_domain_delta_unhealthy_nodes_percent is not None:
            self._values["max_upgrade_domain_delta_unhealthy_nodes_percent"] = max_upgrade_domain_delta_unhealthy_nodes_percent

    @builtins.property
    def max_delta_unhealthy_applications_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#max_delta_unhealthy_applications_percent ServiceFabricCluster#max_delta_unhealthy_applications_percent}.'''
        result = self._values.get("max_delta_unhealthy_applications_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_delta_unhealthy_nodes_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#max_delta_unhealthy_nodes_percent ServiceFabricCluster#max_delta_unhealthy_nodes_percent}.'''
        result = self._values.get("max_delta_unhealthy_nodes_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_upgrade_domain_delta_unhealthy_nodes_percent(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#max_upgrade_domain_delta_unhealthy_nodes_percent ServiceFabricCluster#max_upgrade_domain_delta_unhealthy_nodes_percent}.'''
        result = self._values.get("max_upgrade_domain_delta_unhealthy_nodes_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterUpgradePolicyDeltaHealthPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricClusterUpgradePolicyDeltaHealthPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterUpgradePolicyDeltaHealthPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterUpgradePolicyDeltaHealthPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxDeltaUnhealthyApplicationsPercent")
    def reset_max_delta_unhealthy_applications_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxDeltaUnhealthyApplicationsPercent", []))

    @jsii.member(jsii_name="resetMaxDeltaUnhealthyNodesPercent")
    def reset_max_delta_unhealthy_nodes_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxDeltaUnhealthyNodesPercent", []))

    @jsii.member(jsii_name="resetMaxUpgradeDomainDeltaUnhealthyNodesPercent")
    def reset_max_upgrade_domain_delta_unhealthy_nodes_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxUpgradeDomainDeltaUnhealthyNodesPercent", []))

    @builtins.property
    @jsii.member(jsii_name="maxDeltaUnhealthyApplicationsPercentInput")
    def max_delta_unhealthy_applications_percent_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxDeltaUnhealthyApplicationsPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="maxDeltaUnhealthyNodesPercentInput")
    def max_delta_unhealthy_nodes_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxDeltaUnhealthyNodesPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="maxUpgradeDomainDeltaUnhealthyNodesPercentInput")
    def max_upgrade_domain_delta_unhealthy_nodes_percent_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxUpgradeDomainDeltaUnhealthyNodesPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="maxDeltaUnhealthyApplicationsPercent")
    def max_delta_unhealthy_applications_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxDeltaUnhealthyApplicationsPercent"))

    @max_delta_unhealthy_applications_percent.setter
    def max_delta_unhealthy_applications_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterUpgradePolicyDeltaHealthPolicyOutputReference, "max_delta_unhealthy_applications_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxDeltaUnhealthyApplicationsPercent", value)

    @builtins.property
    @jsii.member(jsii_name="maxDeltaUnhealthyNodesPercent")
    def max_delta_unhealthy_nodes_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxDeltaUnhealthyNodesPercent"))

    @max_delta_unhealthy_nodes_percent.setter
    def max_delta_unhealthy_nodes_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterUpgradePolicyDeltaHealthPolicyOutputReference, "max_delta_unhealthy_nodes_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxDeltaUnhealthyNodesPercent", value)

    @builtins.property
    @jsii.member(jsii_name="maxUpgradeDomainDeltaUnhealthyNodesPercent")
    def max_upgrade_domain_delta_unhealthy_nodes_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUpgradeDomainDeltaUnhealthyNodesPercent"))

    @max_upgrade_domain_delta_unhealthy_nodes_percent.setter
    def max_upgrade_domain_delta_unhealthy_nodes_percent(
        self,
        value: jsii.Number,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterUpgradePolicyDeltaHealthPolicyOutputReference, "max_upgrade_domain_delta_unhealthy_nodes_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUpgradeDomainDeltaUnhealthyNodesPercent", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceFabricClusterUpgradePolicyDeltaHealthPolicy]:
        return typing.cast(typing.Optional[ServiceFabricClusterUpgradePolicyDeltaHealthPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceFabricClusterUpgradePolicyDeltaHealthPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterUpgradePolicyDeltaHealthPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterUpgradePolicyHealthPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "max_unhealthy_applications_percent": "maxUnhealthyApplicationsPercent",
        "max_unhealthy_nodes_percent": "maxUnhealthyNodesPercent",
    },
)
class ServiceFabricClusterUpgradePolicyHealthPolicy:
    def __init__(
        self,
        *,
        max_unhealthy_applications_percent: typing.Optional[jsii.Number] = None,
        max_unhealthy_nodes_percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_unhealthy_applications_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#max_unhealthy_applications_percent ServiceFabricCluster#max_unhealthy_applications_percent}.
        :param max_unhealthy_nodes_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#max_unhealthy_nodes_percent ServiceFabricCluster#max_unhealthy_nodes_percent}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceFabricClusterUpgradePolicyHealthPolicy.__init__)
            check_type(argname="argument max_unhealthy_applications_percent", value=max_unhealthy_applications_percent, expected_type=type_hints["max_unhealthy_applications_percent"])
            check_type(argname="argument max_unhealthy_nodes_percent", value=max_unhealthy_nodes_percent, expected_type=type_hints["max_unhealthy_nodes_percent"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_unhealthy_applications_percent is not None:
            self._values["max_unhealthy_applications_percent"] = max_unhealthy_applications_percent
        if max_unhealthy_nodes_percent is not None:
            self._values["max_unhealthy_nodes_percent"] = max_unhealthy_nodes_percent

    @builtins.property
    def max_unhealthy_applications_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#max_unhealthy_applications_percent ServiceFabricCluster#max_unhealthy_applications_percent}.'''
        result = self._values.get("max_unhealthy_applications_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_unhealthy_nodes_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#max_unhealthy_nodes_percent ServiceFabricCluster#max_unhealthy_nodes_percent}.'''
        result = self._values.get("max_unhealthy_nodes_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceFabricClusterUpgradePolicyHealthPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceFabricClusterUpgradePolicyHealthPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterUpgradePolicyHealthPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterUpgradePolicyHealthPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxUnhealthyApplicationsPercent")
    def reset_max_unhealthy_applications_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxUnhealthyApplicationsPercent", []))

    @jsii.member(jsii_name="resetMaxUnhealthyNodesPercent")
    def reset_max_unhealthy_nodes_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxUnhealthyNodesPercent", []))

    @builtins.property
    @jsii.member(jsii_name="maxUnhealthyApplicationsPercentInput")
    def max_unhealthy_applications_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxUnhealthyApplicationsPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="maxUnhealthyNodesPercentInput")
    def max_unhealthy_nodes_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxUnhealthyNodesPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="maxUnhealthyApplicationsPercent")
    def max_unhealthy_applications_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUnhealthyApplicationsPercent"))

    @max_unhealthy_applications_percent.setter
    def max_unhealthy_applications_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterUpgradePolicyHealthPolicyOutputReference, "max_unhealthy_applications_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUnhealthyApplicationsPercent", value)

    @builtins.property
    @jsii.member(jsii_name="maxUnhealthyNodesPercent")
    def max_unhealthy_nodes_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUnhealthyNodesPercent"))

    @max_unhealthy_nodes_percent.setter
    def max_unhealthy_nodes_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterUpgradePolicyHealthPolicyOutputReference, "max_unhealthy_nodes_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUnhealthyNodesPercent", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceFabricClusterUpgradePolicyHealthPolicy]:
        return typing.cast(typing.Optional[ServiceFabricClusterUpgradePolicyHealthPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceFabricClusterUpgradePolicyHealthPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterUpgradePolicyHealthPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceFabricClusterUpgradePolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.serviceFabricCluster.ServiceFabricClusterUpgradePolicyOutputReference",
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
            type_hints = typing.get_type_hints(ServiceFabricClusterUpgradePolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDeltaHealthPolicy")
    def put_delta_health_policy(
        self,
        *,
        max_delta_unhealthy_applications_percent: typing.Optional[jsii.Number] = None,
        max_delta_unhealthy_nodes_percent: typing.Optional[jsii.Number] = None,
        max_upgrade_domain_delta_unhealthy_nodes_percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_delta_unhealthy_applications_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#max_delta_unhealthy_applications_percent ServiceFabricCluster#max_delta_unhealthy_applications_percent}.
        :param max_delta_unhealthy_nodes_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#max_delta_unhealthy_nodes_percent ServiceFabricCluster#max_delta_unhealthy_nodes_percent}.
        :param max_upgrade_domain_delta_unhealthy_nodes_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#max_upgrade_domain_delta_unhealthy_nodes_percent ServiceFabricCluster#max_upgrade_domain_delta_unhealthy_nodes_percent}.
        '''
        value = ServiceFabricClusterUpgradePolicyDeltaHealthPolicy(
            max_delta_unhealthy_applications_percent=max_delta_unhealthy_applications_percent,
            max_delta_unhealthy_nodes_percent=max_delta_unhealthy_nodes_percent,
            max_upgrade_domain_delta_unhealthy_nodes_percent=max_upgrade_domain_delta_unhealthy_nodes_percent,
        )

        return typing.cast(None, jsii.invoke(self, "putDeltaHealthPolicy", [value]))

    @jsii.member(jsii_name="putHealthPolicy")
    def put_health_policy(
        self,
        *,
        max_unhealthy_applications_percent: typing.Optional[jsii.Number] = None,
        max_unhealthy_nodes_percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_unhealthy_applications_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#max_unhealthy_applications_percent ServiceFabricCluster#max_unhealthy_applications_percent}.
        :param max_unhealthy_nodes_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster#max_unhealthy_nodes_percent ServiceFabricCluster#max_unhealthy_nodes_percent}.
        '''
        value = ServiceFabricClusterUpgradePolicyHealthPolicy(
            max_unhealthy_applications_percent=max_unhealthy_applications_percent,
            max_unhealthy_nodes_percent=max_unhealthy_nodes_percent,
        )

        return typing.cast(None, jsii.invoke(self, "putHealthPolicy", [value]))

    @jsii.member(jsii_name="resetDeltaHealthPolicy")
    def reset_delta_health_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeltaHealthPolicy", []))

    @jsii.member(jsii_name="resetForceRestartEnabled")
    def reset_force_restart_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceRestartEnabled", []))

    @jsii.member(jsii_name="resetHealthCheckRetryTimeout")
    def reset_health_check_retry_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckRetryTimeout", []))

    @jsii.member(jsii_name="resetHealthCheckStableDuration")
    def reset_health_check_stable_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckStableDuration", []))

    @jsii.member(jsii_name="resetHealthCheckWaitDuration")
    def reset_health_check_wait_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckWaitDuration", []))

    @jsii.member(jsii_name="resetHealthPolicy")
    def reset_health_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthPolicy", []))

    @jsii.member(jsii_name="resetUpgradeDomainTimeout")
    def reset_upgrade_domain_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpgradeDomainTimeout", []))

    @jsii.member(jsii_name="resetUpgradeReplicaSetCheckTimeout")
    def reset_upgrade_replica_set_check_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpgradeReplicaSetCheckTimeout", []))

    @jsii.member(jsii_name="resetUpgradeTimeout")
    def reset_upgrade_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpgradeTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="deltaHealthPolicy")
    def delta_health_policy(
        self,
    ) -> ServiceFabricClusterUpgradePolicyDeltaHealthPolicyOutputReference:
        return typing.cast(ServiceFabricClusterUpgradePolicyDeltaHealthPolicyOutputReference, jsii.get(self, "deltaHealthPolicy"))

    @builtins.property
    @jsii.member(jsii_name="healthPolicy")
    def health_policy(
        self,
    ) -> ServiceFabricClusterUpgradePolicyHealthPolicyOutputReference:
        return typing.cast(ServiceFabricClusterUpgradePolicyHealthPolicyOutputReference, jsii.get(self, "healthPolicy"))

    @builtins.property
    @jsii.member(jsii_name="deltaHealthPolicyInput")
    def delta_health_policy_input(
        self,
    ) -> typing.Optional[ServiceFabricClusterUpgradePolicyDeltaHealthPolicy]:
        return typing.cast(typing.Optional[ServiceFabricClusterUpgradePolicyDeltaHealthPolicy], jsii.get(self, "deltaHealthPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="forceRestartEnabledInput")
    def force_restart_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceRestartEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckRetryTimeoutInput")
    def health_check_retry_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckRetryTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckStableDurationInput")
    def health_check_stable_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckStableDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckWaitDurationInput")
    def health_check_wait_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckWaitDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="healthPolicyInput")
    def health_policy_input(
        self,
    ) -> typing.Optional[ServiceFabricClusterUpgradePolicyHealthPolicy]:
        return typing.cast(typing.Optional[ServiceFabricClusterUpgradePolicyHealthPolicy], jsii.get(self, "healthPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="upgradeDomainTimeoutInput")
    def upgrade_domain_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "upgradeDomainTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="upgradeReplicaSetCheckTimeoutInput")
    def upgrade_replica_set_check_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "upgradeReplicaSetCheckTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="upgradeTimeoutInput")
    def upgrade_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "upgradeTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="forceRestartEnabled")
    def force_restart_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forceRestartEnabled"))

    @force_restart_enabled.setter
    def force_restart_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterUpgradePolicyOutputReference, "force_restart_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceRestartEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckRetryTimeout")
    def health_check_retry_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckRetryTimeout"))

    @health_check_retry_timeout.setter
    def health_check_retry_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterUpgradePolicyOutputReference, "health_check_retry_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckRetryTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckStableDuration")
    def health_check_stable_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckStableDuration"))

    @health_check_stable_duration.setter
    def health_check_stable_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterUpgradePolicyOutputReference, "health_check_stable_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckStableDuration", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckWaitDuration")
    def health_check_wait_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckWaitDuration"))

    @health_check_wait_duration.setter
    def health_check_wait_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterUpgradePolicyOutputReference, "health_check_wait_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckWaitDuration", value)

    @builtins.property
    @jsii.member(jsii_name="upgradeDomainTimeout")
    def upgrade_domain_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "upgradeDomainTimeout"))

    @upgrade_domain_timeout.setter
    def upgrade_domain_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterUpgradePolicyOutputReference, "upgrade_domain_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upgradeDomainTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="upgradeReplicaSetCheckTimeout")
    def upgrade_replica_set_check_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "upgradeReplicaSetCheckTimeout"))

    @upgrade_replica_set_check_timeout.setter
    def upgrade_replica_set_check_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterUpgradePolicyOutputReference, "upgrade_replica_set_check_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upgradeReplicaSetCheckTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="upgradeTimeout")
    def upgrade_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "upgradeTimeout"))

    @upgrade_timeout.setter
    def upgrade_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterUpgradePolicyOutputReference, "upgrade_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upgradeTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceFabricClusterUpgradePolicy]:
        return typing.cast(typing.Optional[ServiceFabricClusterUpgradePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceFabricClusterUpgradePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceFabricClusterUpgradePolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ServiceFabricCluster",
    "ServiceFabricClusterAzureActiveDirectory",
    "ServiceFabricClusterAzureActiveDirectoryOutputReference",
    "ServiceFabricClusterCertificate",
    "ServiceFabricClusterCertificateCommonNames",
    "ServiceFabricClusterCertificateCommonNamesCommonNames",
    "ServiceFabricClusterCertificateCommonNamesCommonNamesList",
    "ServiceFabricClusterCertificateCommonNamesCommonNamesOutputReference",
    "ServiceFabricClusterCertificateCommonNamesOutputReference",
    "ServiceFabricClusterCertificateOutputReference",
    "ServiceFabricClusterClientCertificateCommonName",
    "ServiceFabricClusterClientCertificateCommonNameList",
    "ServiceFabricClusterClientCertificateCommonNameOutputReference",
    "ServiceFabricClusterClientCertificateThumbprint",
    "ServiceFabricClusterClientCertificateThumbprintList",
    "ServiceFabricClusterClientCertificateThumbprintOutputReference",
    "ServiceFabricClusterConfig",
    "ServiceFabricClusterDiagnosticsConfig",
    "ServiceFabricClusterDiagnosticsConfigOutputReference",
    "ServiceFabricClusterFabricSettings",
    "ServiceFabricClusterFabricSettingsList",
    "ServiceFabricClusterFabricSettingsOutputReference",
    "ServiceFabricClusterNodeType",
    "ServiceFabricClusterNodeTypeApplicationPorts",
    "ServiceFabricClusterNodeTypeApplicationPortsOutputReference",
    "ServiceFabricClusterNodeTypeEphemeralPorts",
    "ServiceFabricClusterNodeTypeEphemeralPortsOutputReference",
    "ServiceFabricClusterNodeTypeList",
    "ServiceFabricClusterNodeTypeOutputReference",
    "ServiceFabricClusterReverseProxyCertificate",
    "ServiceFabricClusterReverseProxyCertificateCommonNames",
    "ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNames",
    "ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesList",
    "ServiceFabricClusterReverseProxyCertificateCommonNamesCommonNamesOutputReference",
    "ServiceFabricClusterReverseProxyCertificateCommonNamesOutputReference",
    "ServiceFabricClusterReverseProxyCertificateOutputReference",
    "ServiceFabricClusterTimeouts",
    "ServiceFabricClusterTimeoutsOutputReference",
    "ServiceFabricClusterUpgradePolicy",
    "ServiceFabricClusterUpgradePolicyDeltaHealthPolicy",
    "ServiceFabricClusterUpgradePolicyDeltaHealthPolicyOutputReference",
    "ServiceFabricClusterUpgradePolicyHealthPolicy",
    "ServiceFabricClusterUpgradePolicyHealthPolicyOutputReference",
    "ServiceFabricClusterUpgradePolicyOutputReference",
]

publication.publish()
