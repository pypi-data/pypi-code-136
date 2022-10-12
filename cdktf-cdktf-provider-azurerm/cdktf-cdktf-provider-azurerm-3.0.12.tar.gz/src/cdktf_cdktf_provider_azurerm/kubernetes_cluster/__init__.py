'''
# `azurerm_kubernetes_cluster`

Refer to the Terraform Registory for docs: [`azurerm_kubernetes_cluster`](https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster).
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


class KubernetesCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster azurerm_kubernetes_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        default_node_pool: typing.Union["KubernetesClusterDefaultNodePool", typing.Dict[str, typing.Any]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        aci_connector_linux: typing.Optional[typing.Union["KubernetesClusterAciConnectorLinux", typing.Dict[str, typing.Any]]] = None,
        api_server_authorized_ip_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        automatic_channel_upgrade: typing.Optional[builtins.str] = None,
        auto_scaler_profile: typing.Optional[typing.Union["KubernetesClusterAutoScalerProfile", typing.Dict[str, typing.Any]]] = None,
        azure_active_directory_role_based_access_control: typing.Optional[typing.Union["KubernetesClusterAzureActiveDirectoryRoleBasedAccessControl", typing.Dict[str, typing.Any]]] = None,
        azure_policy_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disk_encryption_set_id: typing.Optional[builtins.str] = None,
        dns_prefix: typing.Optional[builtins.str] = None,
        dns_prefix_private_cluster: typing.Optional[builtins.str] = None,
        edge_zone: typing.Optional[builtins.str] = None,
        enable_pod_security_policy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        http_application_routing_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        http_proxy_config: typing.Optional[typing.Union["KubernetesClusterHttpProxyConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["KubernetesClusterIdentity", typing.Dict[str, typing.Any]]] = None,
        ingress_application_gateway: typing.Optional[typing.Union["KubernetesClusterIngressApplicationGateway", typing.Dict[str, typing.Any]]] = None,
        key_vault_secrets_provider: typing.Optional[typing.Union["KubernetesClusterKeyVaultSecretsProvider", typing.Dict[str, typing.Any]]] = None,
        kubelet_identity: typing.Optional[typing.Union["KubernetesClusterKubeletIdentity", typing.Dict[str, typing.Any]]] = None,
        kubernetes_version: typing.Optional[builtins.str] = None,
        linux_profile: typing.Optional[typing.Union["KubernetesClusterLinuxProfile", typing.Dict[str, typing.Any]]] = None,
        local_account_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        maintenance_window: typing.Optional[typing.Union["KubernetesClusterMaintenanceWindow", typing.Dict[str, typing.Any]]] = None,
        microsoft_defender: typing.Optional[typing.Union["KubernetesClusterMicrosoftDefender", typing.Dict[str, typing.Any]]] = None,
        network_profile: typing.Optional[typing.Union["KubernetesClusterNetworkProfile", typing.Dict[str, typing.Any]]] = None,
        node_resource_group: typing.Optional[builtins.str] = None,
        oidc_issuer_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        oms_agent: typing.Optional[typing.Union["KubernetesClusterOmsAgent", typing.Dict[str, typing.Any]]] = None,
        open_service_mesh_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        private_cluster_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        private_cluster_public_fqdn_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        private_dns_zone_id: typing.Optional[builtins.str] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        role_based_access_control_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        run_command_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        service_principal: typing.Optional[typing.Union["KubernetesClusterServicePrincipal", typing.Dict[str, typing.Any]]] = None,
        sku_tier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KubernetesClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        windows_profile: typing.Optional[typing.Union["KubernetesClusterWindowsProfile", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster azurerm_kubernetes_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param default_node_pool: default_node_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#default_node_pool KubernetesCluster#default_node_pool}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#location KubernetesCluster#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#name KubernetesCluster#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#resource_group_name KubernetesCluster#resource_group_name}.
        :param aci_connector_linux: aci_connector_linux block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#aci_connector_linux KubernetesCluster#aci_connector_linux}
        :param api_server_authorized_ip_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#api_server_authorized_ip_ranges KubernetesCluster#api_server_authorized_ip_ranges}.
        :param automatic_channel_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#automatic_channel_upgrade KubernetesCluster#automatic_channel_upgrade}.
        :param auto_scaler_profile: auto_scaler_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#auto_scaler_profile KubernetesCluster#auto_scaler_profile}
        :param azure_active_directory_role_based_access_control: azure_active_directory_role_based_access_control block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#azure_active_directory_role_based_access_control KubernetesCluster#azure_active_directory_role_based_access_control}
        :param azure_policy_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#azure_policy_enabled KubernetesCluster#azure_policy_enabled}.
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#disk_encryption_set_id KubernetesCluster#disk_encryption_set_id}.
        :param dns_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#dns_prefix KubernetesCluster#dns_prefix}.
        :param dns_prefix_private_cluster: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#dns_prefix_private_cluster KubernetesCluster#dns_prefix_private_cluster}.
        :param edge_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#edge_zone KubernetesCluster#edge_zone}.
        :param enable_pod_security_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#enable_pod_security_policy KubernetesCluster#enable_pod_security_policy}.
        :param http_application_routing_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#http_application_routing_enabled KubernetesCluster#http_application_routing_enabled}.
        :param http_proxy_config: http_proxy_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#http_proxy_config KubernetesCluster#http_proxy_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#id KubernetesCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#identity KubernetesCluster#identity}
        :param ingress_application_gateway: ingress_application_gateway block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#ingress_application_gateway KubernetesCluster#ingress_application_gateway}
        :param key_vault_secrets_provider: key_vault_secrets_provider block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#key_vault_secrets_provider KubernetesCluster#key_vault_secrets_provider}
        :param kubelet_identity: kubelet_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#kubelet_identity KubernetesCluster#kubelet_identity}
        :param kubernetes_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#kubernetes_version KubernetesCluster#kubernetes_version}.
        :param linux_profile: linux_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#linux_profile KubernetesCluster#linux_profile}
        :param local_account_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#local_account_disabled KubernetesCluster#local_account_disabled}.
        :param maintenance_window: maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#maintenance_window KubernetesCluster#maintenance_window}
        :param microsoft_defender: microsoft_defender block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#microsoft_defender KubernetesCluster#microsoft_defender}
        :param network_profile: network_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#network_profile KubernetesCluster#network_profile}
        :param node_resource_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#node_resource_group KubernetesCluster#node_resource_group}.
        :param oidc_issuer_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#oidc_issuer_enabled KubernetesCluster#oidc_issuer_enabled}.
        :param oms_agent: oms_agent block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#oms_agent KubernetesCluster#oms_agent}
        :param open_service_mesh_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#open_service_mesh_enabled KubernetesCluster#open_service_mesh_enabled}.
        :param private_cluster_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#private_cluster_enabled KubernetesCluster#private_cluster_enabled}.
        :param private_cluster_public_fqdn_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#private_cluster_public_fqdn_enabled KubernetesCluster#private_cluster_public_fqdn_enabled}.
        :param private_dns_zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#private_dns_zone_id KubernetesCluster#private_dns_zone_id}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#public_network_access_enabled KubernetesCluster#public_network_access_enabled}.
        :param role_based_access_control_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#role_based_access_control_enabled KubernetesCluster#role_based_access_control_enabled}.
        :param run_command_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#run_command_enabled KubernetesCluster#run_command_enabled}.
        :param service_principal: service_principal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#service_principal KubernetesCluster#service_principal}
        :param sku_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#sku_tier KubernetesCluster#sku_tier}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#tags KubernetesCluster#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#timeouts KubernetesCluster#timeouts}
        :param windows_profile: windows_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#windows_profile KubernetesCluster#windows_profile}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = KubernetesClusterConfig(
            default_node_pool=default_node_pool,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            aci_connector_linux=aci_connector_linux,
            api_server_authorized_ip_ranges=api_server_authorized_ip_ranges,
            automatic_channel_upgrade=automatic_channel_upgrade,
            auto_scaler_profile=auto_scaler_profile,
            azure_active_directory_role_based_access_control=azure_active_directory_role_based_access_control,
            azure_policy_enabled=azure_policy_enabled,
            disk_encryption_set_id=disk_encryption_set_id,
            dns_prefix=dns_prefix,
            dns_prefix_private_cluster=dns_prefix_private_cluster,
            edge_zone=edge_zone,
            enable_pod_security_policy=enable_pod_security_policy,
            http_application_routing_enabled=http_application_routing_enabled,
            http_proxy_config=http_proxy_config,
            id=id,
            identity=identity,
            ingress_application_gateway=ingress_application_gateway,
            key_vault_secrets_provider=key_vault_secrets_provider,
            kubelet_identity=kubelet_identity,
            kubernetes_version=kubernetes_version,
            linux_profile=linux_profile,
            local_account_disabled=local_account_disabled,
            maintenance_window=maintenance_window,
            microsoft_defender=microsoft_defender,
            network_profile=network_profile,
            node_resource_group=node_resource_group,
            oidc_issuer_enabled=oidc_issuer_enabled,
            oms_agent=oms_agent,
            open_service_mesh_enabled=open_service_mesh_enabled,
            private_cluster_enabled=private_cluster_enabled,
            private_cluster_public_fqdn_enabled=private_cluster_public_fqdn_enabled,
            private_dns_zone_id=private_dns_zone_id,
            public_network_access_enabled=public_network_access_enabled,
            role_based_access_control_enabled=role_based_access_control_enabled,
            run_command_enabled=run_command_enabled,
            service_principal=service_principal,
            sku_tier=sku_tier,
            tags=tags,
            timeouts=timeouts,
            windows_profile=windows_profile,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAciConnectorLinux")
    def put_aci_connector_linux(self, *, subnet_name: builtins.str) -> None:
        '''
        :param subnet_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#subnet_name KubernetesCluster#subnet_name}.
        '''
        value = KubernetesClusterAciConnectorLinux(subnet_name=subnet_name)

        return typing.cast(None, jsii.invoke(self, "putAciConnectorLinux", [value]))

    @jsii.member(jsii_name="putAutoScalerProfile")
    def put_auto_scaler_profile(
        self,
        *,
        balance_similar_node_groups: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        empty_bulk_delete_max: typing.Optional[builtins.str] = None,
        expander: typing.Optional[builtins.str] = None,
        max_graceful_termination_sec: typing.Optional[builtins.str] = None,
        max_node_provisioning_time: typing.Optional[builtins.str] = None,
        max_unready_nodes: typing.Optional[jsii.Number] = None,
        max_unready_percentage: typing.Optional[jsii.Number] = None,
        new_pod_scale_up_delay: typing.Optional[builtins.str] = None,
        scale_down_delay_after_add: typing.Optional[builtins.str] = None,
        scale_down_delay_after_delete: typing.Optional[builtins.str] = None,
        scale_down_delay_after_failure: typing.Optional[builtins.str] = None,
        scale_down_unneeded: typing.Optional[builtins.str] = None,
        scale_down_unready: typing.Optional[builtins.str] = None,
        scale_down_utilization_threshold: typing.Optional[builtins.str] = None,
        scan_interval: typing.Optional[builtins.str] = None,
        skip_nodes_with_local_storage: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        skip_nodes_with_system_pods: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param balance_similar_node_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#balance_similar_node_groups KubernetesCluster#balance_similar_node_groups}.
        :param empty_bulk_delete_max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#empty_bulk_delete_max KubernetesCluster#empty_bulk_delete_max}.
        :param expander: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#expander KubernetesCluster#expander}.
        :param max_graceful_termination_sec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_graceful_termination_sec KubernetesCluster#max_graceful_termination_sec}.
        :param max_node_provisioning_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_node_provisioning_time KubernetesCluster#max_node_provisioning_time}.
        :param max_unready_nodes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_unready_nodes KubernetesCluster#max_unready_nodes}.
        :param max_unready_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_unready_percentage KubernetesCluster#max_unready_percentage}.
        :param new_pod_scale_up_delay: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#new_pod_scale_up_delay KubernetesCluster#new_pod_scale_up_delay}.
        :param scale_down_delay_after_add: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_delay_after_add KubernetesCluster#scale_down_delay_after_add}.
        :param scale_down_delay_after_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_delay_after_delete KubernetesCluster#scale_down_delay_after_delete}.
        :param scale_down_delay_after_failure: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_delay_after_failure KubernetesCluster#scale_down_delay_after_failure}.
        :param scale_down_unneeded: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_unneeded KubernetesCluster#scale_down_unneeded}.
        :param scale_down_unready: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_unready KubernetesCluster#scale_down_unready}.
        :param scale_down_utilization_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_utilization_threshold KubernetesCluster#scale_down_utilization_threshold}.
        :param scan_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scan_interval KubernetesCluster#scan_interval}.
        :param skip_nodes_with_local_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#skip_nodes_with_local_storage KubernetesCluster#skip_nodes_with_local_storage}.
        :param skip_nodes_with_system_pods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#skip_nodes_with_system_pods KubernetesCluster#skip_nodes_with_system_pods}.
        '''
        value = KubernetesClusterAutoScalerProfile(
            balance_similar_node_groups=balance_similar_node_groups,
            empty_bulk_delete_max=empty_bulk_delete_max,
            expander=expander,
            max_graceful_termination_sec=max_graceful_termination_sec,
            max_node_provisioning_time=max_node_provisioning_time,
            max_unready_nodes=max_unready_nodes,
            max_unready_percentage=max_unready_percentage,
            new_pod_scale_up_delay=new_pod_scale_up_delay,
            scale_down_delay_after_add=scale_down_delay_after_add,
            scale_down_delay_after_delete=scale_down_delay_after_delete,
            scale_down_delay_after_failure=scale_down_delay_after_failure,
            scale_down_unneeded=scale_down_unneeded,
            scale_down_unready=scale_down_unready,
            scale_down_utilization_threshold=scale_down_utilization_threshold,
            scan_interval=scan_interval,
            skip_nodes_with_local_storage=skip_nodes_with_local_storage,
            skip_nodes_with_system_pods=skip_nodes_with_system_pods,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoScalerProfile", [value]))

    @jsii.member(jsii_name="putAzureActiveDirectoryRoleBasedAccessControl")
    def put_azure_active_directory_role_based_access_control(
        self,
        *,
        admin_group_object_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        azure_rbac_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        client_app_id: typing.Optional[builtins.str] = None,
        managed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        server_app_id: typing.Optional[builtins.str] = None,
        server_app_secret: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_group_object_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#admin_group_object_ids KubernetesCluster#admin_group_object_ids}.
        :param azure_rbac_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#azure_rbac_enabled KubernetesCluster#azure_rbac_enabled}.
        :param client_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#client_app_id KubernetesCluster#client_app_id}.
        :param managed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#managed KubernetesCluster#managed}.
        :param server_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#server_app_id KubernetesCluster#server_app_id}.
        :param server_app_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#server_app_secret KubernetesCluster#server_app_secret}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#tenant_id KubernetesCluster#tenant_id}.
        '''
        value = KubernetesClusterAzureActiveDirectoryRoleBasedAccessControl(
            admin_group_object_ids=admin_group_object_ids,
            azure_rbac_enabled=azure_rbac_enabled,
            client_app_id=client_app_id,
            managed=managed,
            server_app_id=server_app_id,
            server_app_secret=server_app_secret,
            tenant_id=tenant_id,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureActiveDirectoryRoleBasedAccessControl", [value]))

    @jsii.member(jsii_name="putDefaultNodePool")
    def put_default_node_pool(
        self,
        *,
        name: builtins.str,
        vm_size: builtins.str,
        capacity_reservation_group_id: typing.Optional[builtins.str] = None,
        enable_auto_scaling: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_host_encryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_node_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fips_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        host_group_id: typing.Optional[builtins.str] = None,
        kubelet_config: typing.Optional[typing.Union["KubernetesClusterDefaultNodePoolKubeletConfig", typing.Dict[str, typing.Any]]] = None,
        kubelet_disk_type: typing.Optional[builtins.str] = None,
        linux_os_config: typing.Optional[typing.Union["KubernetesClusterDefaultNodePoolLinuxOsConfig", typing.Dict[str, typing.Any]]] = None,
        max_count: typing.Optional[jsii.Number] = None,
        max_pods: typing.Optional[jsii.Number] = None,
        message_of_the_day: typing.Optional[builtins.str] = None,
        min_count: typing.Optional[jsii.Number] = None,
        node_count: typing.Optional[jsii.Number] = None,
        node_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        node_public_ip_prefix_id: typing.Optional[builtins.str] = None,
        node_taints: typing.Optional[typing.Sequence[builtins.str]] = None,
        only_critical_addons_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        orchestrator_version: typing.Optional[builtins.str] = None,
        os_disk_size_gb: typing.Optional[jsii.Number] = None,
        os_disk_type: typing.Optional[builtins.str] = None,
        os_sku: typing.Optional[builtins.str] = None,
        pod_subnet_id: typing.Optional[builtins.str] = None,
        proximity_placement_group_id: typing.Optional[builtins.str] = None,
        scale_down_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
        ultra_ssd_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        upgrade_settings: typing.Optional[typing.Union["KubernetesClusterDefaultNodePoolUpgradeSettings", typing.Dict[str, typing.Any]]] = None,
        vnet_subnet_id: typing.Optional[builtins.str] = None,
        workload_runtime: typing.Optional[builtins.str] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#name KubernetesCluster#name}.
        :param vm_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#vm_size KubernetesCluster#vm_size}.
        :param capacity_reservation_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#capacity_reservation_group_id KubernetesCluster#capacity_reservation_group_id}.
        :param enable_auto_scaling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#enable_auto_scaling KubernetesCluster#enable_auto_scaling}.
        :param enable_host_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#enable_host_encryption KubernetesCluster#enable_host_encryption}.
        :param enable_node_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#enable_node_public_ip KubernetesCluster#enable_node_public_ip}.
        :param fips_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#fips_enabled KubernetesCluster#fips_enabled}.
        :param host_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#host_group_id KubernetesCluster#host_group_id}.
        :param kubelet_config: kubelet_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#kubelet_config KubernetesCluster#kubelet_config}
        :param kubelet_disk_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#kubelet_disk_type KubernetesCluster#kubelet_disk_type}.
        :param linux_os_config: linux_os_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#linux_os_config KubernetesCluster#linux_os_config}
        :param max_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_count KubernetesCluster#max_count}.
        :param max_pods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_pods KubernetesCluster#max_pods}.
        :param message_of_the_day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#message_of_the_day KubernetesCluster#message_of_the_day}.
        :param min_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#min_count KubernetesCluster#min_count}.
        :param node_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#node_count KubernetesCluster#node_count}.
        :param node_labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#node_labels KubernetesCluster#node_labels}.
        :param node_public_ip_prefix_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#node_public_ip_prefix_id KubernetesCluster#node_public_ip_prefix_id}.
        :param node_taints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#node_taints KubernetesCluster#node_taints}.
        :param only_critical_addons_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#only_critical_addons_enabled KubernetesCluster#only_critical_addons_enabled}.
        :param orchestrator_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#orchestrator_version KubernetesCluster#orchestrator_version}.
        :param os_disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#os_disk_size_gb KubernetesCluster#os_disk_size_gb}.
        :param os_disk_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#os_disk_type KubernetesCluster#os_disk_type}.
        :param os_sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#os_sku KubernetesCluster#os_sku}.
        :param pod_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#pod_subnet_id KubernetesCluster#pod_subnet_id}.
        :param proximity_placement_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#proximity_placement_group_id KubernetesCluster#proximity_placement_group_id}.
        :param scale_down_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_mode KubernetesCluster#scale_down_mode}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#tags KubernetesCluster#tags}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#type KubernetesCluster#type}.
        :param ultra_ssd_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#ultra_ssd_enabled KubernetesCluster#ultra_ssd_enabled}.
        :param upgrade_settings: upgrade_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#upgrade_settings KubernetesCluster#upgrade_settings}
        :param vnet_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#vnet_subnet_id KubernetesCluster#vnet_subnet_id}.
        :param workload_runtime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#workload_runtime KubernetesCluster#workload_runtime}.
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#zones KubernetesCluster#zones}.
        '''
        value = KubernetesClusterDefaultNodePool(
            name=name,
            vm_size=vm_size,
            capacity_reservation_group_id=capacity_reservation_group_id,
            enable_auto_scaling=enable_auto_scaling,
            enable_host_encryption=enable_host_encryption,
            enable_node_public_ip=enable_node_public_ip,
            fips_enabled=fips_enabled,
            host_group_id=host_group_id,
            kubelet_config=kubelet_config,
            kubelet_disk_type=kubelet_disk_type,
            linux_os_config=linux_os_config,
            max_count=max_count,
            max_pods=max_pods,
            message_of_the_day=message_of_the_day,
            min_count=min_count,
            node_count=node_count,
            node_labels=node_labels,
            node_public_ip_prefix_id=node_public_ip_prefix_id,
            node_taints=node_taints,
            only_critical_addons_enabled=only_critical_addons_enabled,
            orchestrator_version=orchestrator_version,
            os_disk_size_gb=os_disk_size_gb,
            os_disk_type=os_disk_type,
            os_sku=os_sku,
            pod_subnet_id=pod_subnet_id,
            proximity_placement_group_id=proximity_placement_group_id,
            scale_down_mode=scale_down_mode,
            tags=tags,
            type=type,
            ultra_ssd_enabled=ultra_ssd_enabled,
            upgrade_settings=upgrade_settings,
            vnet_subnet_id=vnet_subnet_id,
            workload_runtime=workload_runtime,
            zones=zones,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultNodePool", [value]))

    @jsii.member(jsii_name="putHttpProxyConfig")
    def put_http_proxy_config(
        self,
        *,
        http_proxy: typing.Optional[builtins.str] = None,
        https_proxy: typing.Optional[builtins.str] = None,
        no_proxy: typing.Optional[typing.Sequence[builtins.str]] = None,
        trusted_ca: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_proxy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#http_proxy KubernetesCluster#http_proxy}.
        :param https_proxy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#https_proxy KubernetesCluster#https_proxy}.
        :param no_proxy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#no_proxy KubernetesCluster#no_proxy}.
        :param trusted_ca: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#trusted_ca KubernetesCluster#trusted_ca}.
        '''
        value = KubernetesClusterHttpProxyConfig(
            http_proxy=http_proxy,
            https_proxy=https_proxy,
            no_proxy=no_proxy,
            trusted_ca=trusted_ca,
        )

        return typing.cast(None, jsii.invoke(self, "putHttpProxyConfig", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#type KubernetesCluster#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#identity_ids KubernetesCluster#identity_ids}.
        '''
        value = KubernetesClusterIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putIngressApplicationGateway")
    def put_ingress_application_gateway(
        self,
        *,
        gateway_id: typing.Optional[builtins.str] = None,
        gateway_name: typing.Optional[builtins.str] = None,
        subnet_cidr: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#gateway_id KubernetesCluster#gateway_id}.
        :param gateway_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#gateway_name KubernetesCluster#gateway_name}.
        :param subnet_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#subnet_cidr KubernetesCluster#subnet_cidr}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#subnet_id KubernetesCluster#subnet_id}.
        '''
        value = KubernetesClusterIngressApplicationGateway(
            gateway_id=gateway_id,
            gateway_name=gateway_name,
            subnet_cidr=subnet_cidr,
            subnet_id=subnet_id,
        )

        return typing.cast(None, jsii.invoke(self, "putIngressApplicationGateway", [value]))

    @jsii.member(jsii_name="putKeyVaultSecretsProvider")
    def put_key_vault_secrets_provider(
        self,
        *,
        secret_rotation_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        secret_rotation_interval: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param secret_rotation_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#secret_rotation_enabled KubernetesCluster#secret_rotation_enabled}.
        :param secret_rotation_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#secret_rotation_interval KubernetesCluster#secret_rotation_interval}.
        '''
        value = KubernetesClusterKeyVaultSecretsProvider(
            secret_rotation_enabled=secret_rotation_enabled,
            secret_rotation_interval=secret_rotation_interval,
        )

        return typing.cast(None, jsii.invoke(self, "putKeyVaultSecretsProvider", [value]))

    @jsii.member(jsii_name="putKubeletIdentity")
    def put_kubelet_identity(
        self,
        *,
        client_id: typing.Optional[builtins.str] = None,
        object_id: typing.Optional[builtins.str] = None,
        user_assigned_identity_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#client_id KubernetesCluster#client_id}.
        :param object_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#object_id KubernetesCluster#object_id}.
        :param user_assigned_identity_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#user_assigned_identity_id KubernetesCluster#user_assigned_identity_id}.
        '''
        value = KubernetesClusterKubeletIdentity(
            client_id=client_id,
            object_id=object_id,
            user_assigned_identity_id=user_assigned_identity_id,
        )

        return typing.cast(None, jsii.invoke(self, "putKubeletIdentity", [value]))

    @jsii.member(jsii_name="putLinuxProfile")
    def put_linux_profile(
        self,
        *,
        admin_username: builtins.str,
        ssh_key: typing.Union["KubernetesClusterLinuxProfileSshKey", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#admin_username KubernetesCluster#admin_username}.
        :param ssh_key: ssh_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#ssh_key KubernetesCluster#ssh_key}
        '''
        value = KubernetesClusterLinuxProfile(
            admin_username=admin_username, ssh_key=ssh_key
        )

        return typing.cast(None, jsii.invoke(self, "putLinuxProfile", [value]))

    @jsii.member(jsii_name="putMaintenanceWindow")
    def put_maintenance_window(
        self,
        *,
        allowed: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KubernetesClusterMaintenanceWindowAllowed", typing.Dict[str, typing.Any]]]]] = None,
        not_allowed: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KubernetesClusterMaintenanceWindowNotAllowed", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param allowed: allowed block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#allowed KubernetesCluster#allowed}
        :param not_allowed: not_allowed block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#not_allowed KubernetesCluster#not_allowed}
        '''
        value = KubernetesClusterMaintenanceWindow(
            allowed=allowed, not_allowed=not_allowed
        )

        return typing.cast(None, jsii.invoke(self, "putMaintenanceWindow", [value]))

    @jsii.member(jsii_name="putMicrosoftDefender")
    def put_microsoft_defender(
        self,
        *,
        log_analytics_workspace_id: builtins.str,
    ) -> None:
        '''
        :param log_analytics_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#log_analytics_workspace_id KubernetesCluster#log_analytics_workspace_id}.
        '''
        value = KubernetesClusterMicrosoftDefender(
            log_analytics_workspace_id=log_analytics_workspace_id
        )

        return typing.cast(None, jsii.invoke(self, "putMicrosoftDefender", [value]))

    @jsii.member(jsii_name="putNetworkProfile")
    def put_network_profile(
        self,
        *,
        network_plugin: builtins.str,
        dns_service_ip: typing.Optional[builtins.str] = None,
        docker_bridge_cidr: typing.Optional[builtins.str] = None,
        ip_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        load_balancer_profile: typing.Optional[typing.Union["KubernetesClusterNetworkProfileLoadBalancerProfile", typing.Dict[str, typing.Any]]] = None,
        load_balancer_sku: typing.Optional[builtins.str] = None,
        nat_gateway_profile: typing.Optional[typing.Union["KubernetesClusterNetworkProfileNatGatewayProfile", typing.Dict[str, typing.Any]]] = None,
        network_mode: typing.Optional[builtins.str] = None,
        network_policy: typing.Optional[builtins.str] = None,
        outbound_type: typing.Optional[builtins.str] = None,
        pod_cidr: typing.Optional[builtins.str] = None,
        pod_cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_cidr: typing.Optional[builtins.str] = None,
        service_cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param network_plugin: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#network_plugin KubernetesCluster#network_plugin}.
        :param dns_service_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#dns_service_ip KubernetesCluster#dns_service_ip}.
        :param docker_bridge_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#docker_bridge_cidr KubernetesCluster#docker_bridge_cidr}.
        :param ip_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#ip_versions KubernetesCluster#ip_versions}.
        :param load_balancer_profile: load_balancer_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#load_balancer_profile KubernetesCluster#load_balancer_profile}
        :param load_balancer_sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#load_balancer_sku KubernetesCluster#load_balancer_sku}.
        :param nat_gateway_profile: nat_gateway_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#nat_gateway_profile KubernetesCluster#nat_gateway_profile}
        :param network_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#network_mode KubernetesCluster#network_mode}.
        :param network_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#network_policy KubernetesCluster#network_policy}.
        :param outbound_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#outbound_type KubernetesCluster#outbound_type}.
        :param pod_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#pod_cidr KubernetesCluster#pod_cidr}.
        :param pod_cidrs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#pod_cidrs KubernetesCluster#pod_cidrs}.
        :param service_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#service_cidr KubernetesCluster#service_cidr}.
        :param service_cidrs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#service_cidrs KubernetesCluster#service_cidrs}.
        '''
        value = KubernetesClusterNetworkProfile(
            network_plugin=network_plugin,
            dns_service_ip=dns_service_ip,
            docker_bridge_cidr=docker_bridge_cidr,
            ip_versions=ip_versions,
            load_balancer_profile=load_balancer_profile,
            load_balancer_sku=load_balancer_sku,
            nat_gateway_profile=nat_gateway_profile,
            network_mode=network_mode,
            network_policy=network_policy,
            outbound_type=outbound_type,
            pod_cidr=pod_cidr,
            pod_cidrs=pod_cidrs,
            service_cidr=service_cidr,
            service_cidrs=service_cidrs,
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkProfile", [value]))

    @jsii.member(jsii_name="putOmsAgent")
    def put_oms_agent(self, *, log_analytics_workspace_id: builtins.str) -> None:
        '''
        :param log_analytics_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#log_analytics_workspace_id KubernetesCluster#log_analytics_workspace_id}.
        '''
        value = KubernetesClusterOmsAgent(
            log_analytics_workspace_id=log_analytics_workspace_id
        )

        return typing.cast(None, jsii.invoke(self, "putOmsAgent", [value]))

    @jsii.member(jsii_name="putServicePrincipal")
    def put_service_principal(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#client_id KubernetesCluster#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#client_secret KubernetesCluster#client_secret}.
        '''
        value = KubernetesClusterServicePrincipal(
            client_id=client_id, client_secret=client_secret
        )

        return typing.cast(None, jsii.invoke(self, "putServicePrincipal", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#create KubernetesCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#delete KubernetesCluster#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#read KubernetesCluster#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#update KubernetesCluster#update}.
        '''
        value = KubernetesClusterTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWindowsProfile")
    def put_windows_profile(
        self,
        *,
        admin_username: builtins.str,
        admin_password: typing.Optional[builtins.str] = None,
        gmsa: typing.Optional[typing.Union["KubernetesClusterWindowsProfileGmsa", typing.Dict[str, typing.Any]]] = None,
        license: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#admin_username KubernetesCluster#admin_username}.
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#admin_password KubernetesCluster#admin_password}.
        :param gmsa: gmsa block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#gmsa KubernetesCluster#gmsa}
        :param license: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#license KubernetesCluster#license}.
        '''
        value = KubernetesClusterWindowsProfile(
            admin_username=admin_username,
            admin_password=admin_password,
            gmsa=gmsa,
            license=license,
        )

        return typing.cast(None, jsii.invoke(self, "putWindowsProfile", [value]))

    @jsii.member(jsii_name="resetAciConnectorLinux")
    def reset_aci_connector_linux(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAciConnectorLinux", []))

    @jsii.member(jsii_name="resetApiServerAuthorizedIpRanges")
    def reset_api_server_authorized_ip_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiServerAuthorizedIpRanges", []))

    @jsii.member(jsii_name="resetAutomaticChannelUpgrade")
    def reset_automatic_channel_upgrade(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticChannelUpgrade", []))

    @jsii.member(jsii_name="resetAutoScalerProfile")
    def reset_auto_scaler_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoScalerProfile", []))

    @jsii.member(jsii_name="resetAzureActiveDirectoryRoleBasedAccessControl")
    def reset_azure_active_directory_role_based_access_control(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureActiveDirectoryRoleBasedAccessControl", []))

    @jsii.member(jsii_name="resetAzurePolicyEnabled")
    def reset_azure_policy_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzurePolicyEnabled", []))

    @jsii.member(jsii_name="resetDiskEncryptionSetId")
    def reset_disk_encryption_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskEncryptionSetId", []))

    @jsii.member(jsii_name="resetDnsPrefix")
    def reset_dns_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsPrefix", []))

    @jsii.member(jsii_name="resetDnsPrefixPrivateCluster")
    def reset_dns_prefix_private_cluster(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsPrefixPrivateCluster", []))

    @jsii.member(jsii_name="resetEdgeZone")
    def reset_edge_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEdgeZone", []))

    @jsii.member(jsii_name="resetEnablePodSecurityPolicy")
    def reset_enable_pod_security_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablePodSecurityPolicy", []))

    @jsii.member(jsii_name="resetHttpApplicationRoutingEnabled")
    def reset_http_application_routing_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpApplicationRoutingEnabled", []))

    @jsii.member(jsii_name="resetHttpProxyConfig")
    def reset_http_proxy_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpProxyConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetIngressApplicationGateway")
    def reset_ingress_application_gateway(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressApplicationGateway", []))

    @jsii.member(jsii_name="resetKeyVaultSecretsProvider")
    def reset_key_vault_secrets_provider(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultSecretsProvider", []))

    @jsii.member(jsii_name="resetKubeletIdentity")
    def reset_kubelet_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKubeletIdentity", []))

    @jsii.member(jsii_name="resetKubernetesVersion")
    def reset_kubernetes_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKubernetesVersion", []))

    @jsii.member(jsii_name="resetLinuxProfile")
    def reset_linux_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinuxProfile", []))

    @jsii.member(jsii_name="resetLocalAccountDisabled")
    def reset_local_account_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalAccountDisabled", []))

    @jsii.member(jsii_name="resetMaintenanceWindow")
    def reset_maintenance_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceWindow", []))

    @jsii.member(jsii_name="resetMicrosoftDefender")
    def reset_microsoft_defender(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMicrosoftDefender", []))

    @jsii.member(jsii_name="resetNetworkProfile")
    def reset_network_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkProfile", []))

    @jsii.member(jsii_name="resetNodeResourceGroup")
    def reset_node_resource_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeResourceGroup", []))

    @jsii.member(jsii_name="resetOidcIssuerEnabled")
    def reset_oidc_issuer_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOidcIssuerEnabled", []))

    @jsii.member(jsii_name="resetOmsAgent")
    def reset_oms_agent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOmsAgent", []))

    @jsii.member(jsii_name="resetOpenServiceMeshEnabled")
    def reset_open_service_mesh_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpenServiceMeshEnabled", []))

    @jsii.member(jsii_name="resetPrivateClusterEnabled")
    def reset_private_cluster_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateClusterEnabled", []))

    @jsii.member(jsii_name="resetPrivateClusterPublicFqdnEnabled")
    def reset_private_cluster_public_fqdn_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateClusterPublicFqdnEnabled", []))

    @jsii.member(jsii_name="resetPrivateDnsZoneId")
    def reset_private_dns_zone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateDnsZoneId", []))

    @jsii.member(jsii_name="resetPublicNetworkAccessEnabled")
    def reset_public_network_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicNetworkAccessEnabled", []))

    @jsii.member(jsii_name="resetRoleBasedAccessControlEnabled")
    def reset_role_based_access_control_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleBasedAccessControlEnabled", []))

    @jsii.member(jsii_name="resetRunCommandEnabled")
    def reset_run_command_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunCommandEnabled", []))

    @jsii.member(jsii_name="resetServicePrincipal")
    def reset_service_principal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServicePrincipal", []))

    @jsii.member(jsii_name="resetSkuTier")
    def reset_sku_tier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkuTier", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWindowsProfile")
    def reset_windows_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWindowsProfile", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aciConnectorLinux")
    def aci_connector_linux(
        self,
    ) -> "KubernetesClusterAciConnectorLinuxOutputReference":
        return typing.cast("KubernetesClusterAciConnectorLinuxOutputReference", jsii.get(self, "aciConnectorLinux"))

    @builtins.property
    @jsii.member(jsii_name="autoScalerProfile")
    def auto_scaler_profile(
        self,
    ) -> "KubernetesClusterAutoScalerProfileOutputReference":
        return typing.cast("KubernetesClusterAutoScalerProfileOutputReference", jsii.get(self, "autoScalerProfile"))

    @builtins.property
    @jsii.member(jsii_name="azureActiveDirectoryRoleBasedAccessControl")
    def azure_active_directory_role_based_access_control(
        self,
    ) -> "KubernetesClusterAzureActiveDirectoryRoleBasedAccessControlOutputReference":
        return typing.cast("KubernetesClusterAzureActiveDirectoryRoleBasedAccessControlOutputReference", jsii.get(self, "azureActiveDirectoryRoleBasedAccessControl"))

    @builtins.property
    @jsii.member(jsii_name="defaultNodePool")
    def default_node_pool(self) -> "KubernetesClusterDefaultNodePoolOutputReference":
        return typing.cast("KubernetesClusterDefaultNodePoolOutputReference", jsii.get(self, "defaultNodePool"))

    @builtins.property
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fqdn"))

    @builtins.property
    @jsii.member(jsii_name="httpApplicationRoutingZoneName")
    def http_application_routing_zone_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpApplicationRoutingZoneName"))

    @builtins.property
    @jsii.member(jsii_name="httpProxyConfig")
    def http_proxy_config(self) -> "KubernetesClusterHttpProxyConfigOutputReference":
        return typing.cast("KubernetesClusterHttpProxyConfigOutputReference", jsii.get(self, "httpProxyConfig"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "KubernetesClusterIdentityOutputReference":
        return typing.cast("KubernetesClusterIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="ingressApplicationGateway")
    def ingress_application_gateway(
        self,
    ) -> "KubernetesClusterIngressApplicationGatewayOutputReference":
        return typing.cast("KubernetesClusterIngressApplicationGatewayOutputReference", jsii.get(self, "ingressApplicationGateway"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultSecretsProvider")
    def key_vault_secrets_provider(
        self,
    ) -> "KubernetesClusterKeyVaultSecretsProviderOutputReference":
        return typing.cast("KubernetesClusterKeyVaultSecretsProviderOutputReference", jsii.get(self, "keyVaultSecretsProvider"))

    @builtins.property
    @jsii.member(jsii_name="kubeAdminConfig")
    def kube_admin_config(self) -> "KubernetesClusterKubeAdminConfigList":
        return typing.cast("KubernetesClusterKubeAdminConfigList", jsii.get(self, "kubeAdminConfig"))

    @builtins.property
    @jsii.member(jsii_name="kubeAdminConfigRaw")
    def kube_admin_config_raw(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kubeAdminConfigRaw"))

    @builtins.property
    @jsii.member(jsii_name="kubeConfig")
    def kube_config(self) -> "KubernetesClusterKubeConfigList":
        return typing.cast("KubernetesClusterKubeConfigList", jsii.get(self, "kubeConfig"))

    @builtins.property
    @jsii.member(jsii_name="kubeConfigRaw")
    def kube_config_raw(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kubeConfigRaw"))

    @builtins.property
    @jsii.member(jsii_name="kubeletIdentity")
    def kubelet_identity(self) -> "KubernetesClusterKubeletIdentityOutputReference":
        return typing.cast("KubernetesClusterKubeletIdentityOutputReference", jsii.get(self, "kubeletIdentity"))

    @builtins.property
    @jsii.member(jsii_name="linuxProfile")
    def linux_profile(self) -> "KubernetesClusterLinuxProfileOutputReference":
        return typing.cast("KubernetesClusterLinuxProfileOutputReference", jsii.get(self, "linuxProfile"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindow")
    def maintenance_window(self) -> "KubernetesClusterMaintenanceWindowOutputReference":
        return typing.cast("KubernetesClusterMaintenanceWindowOutputReference", jsii.get(self, "maintenanceWindow"))

    @builtins.property
    @jsii.member(jsii_name="microsoftDefender")
    def microsoft_defender(self) -> "KubernetesClusterMicrosoftDefenderOutputReference":
        return typing.cast("KubernetesClusterMicrosoftDefenderOutputReference", jsii.get(self, "microsoftDefender"))

    @builtins.property
    @jsii.member(jsii_name="networkProfile")
    def network_profile(self) -> "KubernetesClusterNetworkProfileOutputReference":
        return typing.cast("KubernetesClusterNetworkProfileOutputReference", jsii.get(self, "networkProfile"))

    @builtins.property
    @jsii.member(jsii_name="oidcIssuerUrl")
    def oidc_issuer_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oidcIssuerUrl"))

    @builtins.property
    @jsii.member(jsii_name="omsAgent")
    def oms_agent(self) -> "KubernetesClusterOmsAgentOutputReference":
        return typing.cast("KubernetesClusterOmsAgentOutputReference", jsii.get(self, "omsAgent"))

    @builtins.property
    @jsii.member(jsii_name="portalFqdn")
    def portal_fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portalFqdn"))

    @builtins.property
    @jsii.member(jsii_name="privateFqdn")
    def private_fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateFqdn"))

    @builtins.property
    @jsii.member(jsii_name="servicePrincipal")
    def service_principal(self) -> "KubernetesClusterServicePrincipalOutputReference":
        return typing.cast("KubernetesClusterServicePrincipalOutputReference", jsii.get(self, "servicePrincipal"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "KubernetesClusterTimeoutsOutputReference":
        return typing.cast("KubernetesClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="windowsProfile")
    def windows_profile(self) -> "KubernetesClusterWindowsProfileOutputReference":
        return typing.cast("KubernetesClusterWindowsProfileOutputReference", jsii.get(self, "windowsProfile"))

    @builtins.property
    @jsii.member(jsii_name="aciConnectorLinuxInput")
    def aci_connector_linux_input(
        self,
    ) -> typing.Optional["KubernetesClusterAciConnectorLinux"]:
        return typing.cast(typing.Optional["KubernetesClusterAciConnectorLinux"], jsii.get(self, "aciConnectorLinuxInput"))

    @builtins.property
    @jsii.member(jsii_name="apiServerAuthorizedIpRangesInput")
    def api_server_authorized_ip_ranges_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "apiServerAuthorizedIpRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticChannelUpgradeInput")
    def automatic_channel_upgrade_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "automaticChannelUpgradeInput"))

    @builtins.property
    @jsii.member(jsii_name="autoScalerProfileInput")
    def auto_scaler_profile_input(
        self,
    ) -> typing.Optional["KubernetesClusterAutoScalerProfile"]:
        return typing.cast(typing.Optional["KubernetesClusterAutoScalerProfile"], jsii.get(self, "autoScalerProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="azureActiveDirectoryRoleBasedAccessControlInput")
    def azure_active_directory_role_based_access_control_input(
        self,
    ) -> typing.Optional["KubernetesClusterAzureActiveDirectoryRoleBasedAccessControl"]:
        return typing.cast(typing.Optional["KubernetesClusterAzureActiveDirectoryRoleBasedAccessControl"], jsii.get(self, "azureActiveDirectoryRoleBasedAccessControlInput"))

    @builtins.property
    @jsii.member(jsii_name="azurePolicyEnabledInput")
    def azure_policy_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "azurePolicyEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultNodePoolInput")
    def default_node_pool_input(
        self,
    ) -> typing.Optional["KubernetesClusterDefaultNodePool"]:
        return typing.cast(typing.Optional["KubernetesClusterDefaultNodePool"], jsii.get(self, "defaultNodePoolInput"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionSetIdInput")
    def disk_encryption_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskEncryptionSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsPrefixInput")
    def dns_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsPrefixPrivateClusterInput")
    def dns_prefix_private_cluster_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsPrefixPrivateClusterInput"))

    @builtins.property
    @jsii.member(jsii_name="edgeZoneInput")
    def edge_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "edgeZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="enablePodSecurityPolicyInput")
    def enable_pod_security_policy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enablePodSecurityPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="httpApplicationRoutingEnabledInput")
    def http_application_routing_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpApplicationRoutingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="httpProxyConfigInput")
    def http_proxy_config_input(
        self,
    ) -> typing.Optional["KubernetesClusterHttpProxyConfig"]:
        return typing.cast(typing.Optional["KubernetesClusterHttpProxyConfig"], jsii.get(self, "httpProxyConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["KubernetesClusterIdentity"]:
        return typing.cast(typing.Optional["KubernetesClusterIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressApplicationGatewayInput")
    def ingress_application_gateway_input(
        self,
    ) -> typing.Optional["KubernetesClusterIngressApplicationGateway"]:
        return typing.cast(typing.Optional["KubernetesClusterIngressApplicationGateway"], jsii.get(self, "ingressApplicationGatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultSecretsProviderInput")
    def key_vault_secrets_provider_input(
        self,
    ) -> typing.Optional["KubernetesClusterKeyVaultSecretsProvider"]:
        return typing.cast(typing.Optional["KubernetesClusterKeyVaultSecretsProvider"], jsii.get(self, "keyVaultSecretsProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="kubeletIdentityInput")
    def kubelet_identity_input(
        self,
    ) -> typing.Optional["KubernetesClusterKubeletIdentity"]:
        return typing.cast(typing.Optional["KubernetesClusterKubeletIdentity"], jsii.get(self, "kubeletIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesVersionInput")
    def kubernetes_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kubernetesVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="linuxProfileInput")
    def linux_profile_input(self) -> typing.Optional["KubernetesClusterLinuxProfile"]:
        return typing.cast(typing.Optional["KubernetesClusterLinuxProfile"], jsii.get(self, "linuxProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="localAccountDisabledInput")
    def local_account_disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "localAccountDisabledInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowInput")
    def maintenance_window_input(
        self,
    ) -> typing.Optional["KubernetesClusterMaintenanceWindow"]:
        return typing.cast(typing.Optional["KubernetesClusterMaintenanceWindow"], jsii.get(self, "maintenanceWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="microsoftDefenderInput")
    def microsoft_defender_input(
        self,
    ) -> typing.Optional["KubernetesClusterMicrosoftDefender"]:
        return typing.cast(typing.Optional["KubernetesClusterMicrosoftDefender"], jsii.get(self, "microsoftDefenderInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkProfileInput")
    def network_profile_input(
        self,
    ) -> typing.Optional["KubernetesClusterNetworkProfile"]:
        return typing.cast(typing.Optional["KubernetesClusterNetworkProfile"], jsii.get(self, "networkProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeResourceGroupInput")
    def node_resource_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeResourceGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="oidcIssuerEnabledInput")
    def oidc_issuer_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "oidcIssuerEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="omsAgentInput")
    def oms_agent_input(self) -> typing.Optional["KubernetesClusterOmsAgent"]:
        return typing.cast(typing.Optional["KubernetesClusterOmsAgent"], jsii.get(self, "omsAgentInput"))

    @builtins.property
    @jsii.member(jsii_name="openServiceMeshEnabledInput")
    def open_service_mesh_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "openServiceMeshEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="privateClusterEnabledInput")
    def private_cluster_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "privateClusterEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="privateClusterPublicFqdnEnabledInput")
    def private_cluster_public_fqdn_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "privateClusterPublicFqdnEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="privateDnsZoneIdInput")
    def private_dns_zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateDnsZoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabledInput")
    def public_network_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicNetworkAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleBasedAccessControlEnabledInput")
    def role_based_access_control_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "roleBasedAccessControlEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="runCommandEnabledInput")
    def run_command_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "runCommandEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="servicePrincipalInput")
    def service_principal_input(
        self,
    ) -> typing.Optional["KubernetesClusterServicePrincipal"]:
        return typing.cast(typing.Optional["KubernetesClusterServicePrincipal"], jsii.get(self, "servicePrincipalInput"))

    @builtins.property
    @jsii.member(jsii_name="skuTierInput")
    def sku_tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuTierInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["KubernetesClusterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["KubernetesClusterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="windowsProfileInput")
    def windows_profile_input(
        self,
    ) -> typing.Optional["KubernetesClusterWindowsProfile"]:
        return typing.cast(typing.Optional["KubernetesClusterWindowsProfile"], jsii.get(self, "windowsProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="apiServerAuthorizedIpRanges")
    def api_server_authorized_ip_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "apiServerAuthorizedIpRanges"))

    @api_server_authorized_ip_ranges.setter
    def api_server_authorized_ip_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "api_server_authorized_ip_ranges").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiServerAuthorizedIpRanges", value)

    @builtins.property
    @jsii.member(jsii_name="automaticChannelUpgrade")
    def automatic_channel_upgrade(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "automaticChannelUpgrade"))

    @automatic_channel_upgrade.setter
    def automatic_channel_upgrade(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "automatic_channel_upgrade").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticChannelUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="azurePolicyEnabled")
    def azure_policy_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "azurePolicyEnabled"))

    @azure_policy_enabled.setter
    def azure_policy_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "azure_policy_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azurePolicyEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskEncryptionSetId"))

    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "disk_encryption_set_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskEncryptionSetId", value)

    @builtins.property
    @jsii.member(jsii_name="dnsPrefix")
    def dns_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsPrefix"))

    @dns_prefix.setter
    def dns_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "dns_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="dnsPrefixPrivateCluster")
    def dns_prefix_private_cluster(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsPrefixPrivateCluster"))

    @dns_prefix_private_cluster.setter
    def dns_prefix_private_cluster(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "dns_prefix_private_cluster").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsPrefixPrivateCluster", value)

    @builtins.property
    @jsii.member(jsii_name="edgeZone")
    def edge_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "edgeZone"))

    @edge_zone.setter
    def edge_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "edge_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edgeZone", value)

    @builtins.property
    @jsii.member(jsii_name="enablePodSecurityPolicy")
    def enable_pod_security_policy(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enablePodSecurityPolicy"))

    @enable_pod_security_policy.setter
    def enable_pod_security_policy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "enable_pod_security_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePodSecurityPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="httpApplicationRoutingEnabled")
    def http_application_routing_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "httpApplicationRoutingEnabled"))

    @http_application_routing_enabled.setter
    def http_application_routing_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "http_application_routing_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpApplicationRoutingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kubernetesVersion")
    def kubernetes_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kubernetesVersion"))

    @kubernetes_version.setter
    def kubernetes_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "kubernetes_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kubernetesVersion", value)

    @builtins.property
    @jsii.member(jsii_name="localAccountDisabled")
    def local_account_disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "localAccountDisabled"))

    @local_account_disabled.setter
    def local_account_disabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "local_account_disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localAccountDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nodeResourceGroup")
    def node_resource_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeResourceGroup"))

    @node_resource_group.setter
    def node_resource_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "node_resource_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeResourceGroup", value)

    @builtins.property
    @jsii.member(jsii_name="oidcIssuerEnabled")
    def oidc_issuer_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "oidcIssuerEnabled"))

    @oidc_issuer_enabled.setter
    def oidc_issuer_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "oidc_issuer_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oidcIssuerEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="openServiceMeshEnabled")
    def open_service_mesh_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "openServiceMeshEnabled"))

    @open_service_mesh_enabled.setter
    def open_service_mesh_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "open_service_mesh_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openServiceMeshEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="privateClusterEnabled")
    def private_cluster_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "privateClusterEnabled"))

    @private_cluster_enabled.setter
    def private_cluster_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "private_cluster_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateClusterEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="privateClusterPublicFqdnEnabled")
    def private_cluster_public_fqdn_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "privateClusterPublicFqdnEnabled"))

    @private_cluster_public_fqdn_enabled.setter
    def private_cluster_public_fqdn_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "private_cluster_public_fqdn_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateClusterPublicFqdnEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="privateDnsZoneId")
    def private_dns_zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateDnsZoneId"))

    @private_dns_zone_id.setter
    def private_dns_zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "private_dns_zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateDnsZoneId", value)

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabled")
    def public_network_access_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publicNetworkAccessEnabled"))

    @public_network_access_enabled.setter
    def public_network_access_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "public_network_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicNetworkAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="roleBasedAccessControlEnabled")
    def role_based_access_control_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "roleBasedAccessControlEnabled"))

    @role_based_access_control_enabled.setter
    def role_based_access_control_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "role_based_access_control_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleBasedAccessControlEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="runCommandEnabled")
    def run_command_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "runCommandEnabled"))

    @run_command_enabled.setter
    def run_command_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "run_command_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runCommandEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="skuTier")
    def sku_tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skuTier"))

    @sku_tier.setter
    def sku_tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "sku_tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skuTier", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesCluster, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterAciConnectorLinux",
    jsii_struct_bases=[],
    name_mapping={"subnet_name": "subnetName"},
)
class KubernetesClusterAciConnectorLinux:
    def __init__(self, *, subnet_name: builtins.str) -> None:
        '''
        :param subnet_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#subnet_name KubernetesCluster#subnet_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterAciConnectorLinux.__init__)
            check_type(argname="argument subnet_name", value=subnet_name, expected_type=type_hints["subnet_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "subnet_name": subnet_name,
        }

    @builtins.property
    def subnet_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#subnet_name KubernetesCluster#subnet_name}.'''
        result = self._values.get("subnet_name")
        assert result is not None, "Required property 'subnet_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterAciConnectorLinux(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterAciConnectorLinuxOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterAciConnectorLinuxOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterAciConnectorLinuxOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="subnetNameInput")
    def subnet_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetName")
    def subnet_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetName"))

    @subnet_name.setter
    def subnet_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAciConnectorLinuxOutputReference, "subnet_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterAciConnectorLinux]:
        return typing.cast(typing.Optional[KubernetesClusterAciConnectorLinux], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterAciConnectorLinux],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAciConnectorLinuxOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterAutoScalerProfile",
    jsii_struct_bases=[],
    name_mapping={
        "balance_similar_node_groups": "balanceSimilarNodeGroups",
        "empty_bulk_delete_max": "emptyBulkDeleteMax",
        "expander": "expander",
        "max_graceful_termination_sec": "maxGracefulTerminationSec",
        "max_node_provisioning_time": "maxNodeProvisioningTime",
        "max_unready_nodes": "maxUnreadyNodes",
        "max_unready_percentage": "maxUnreadyPercentage",
        "new_pod_scale_up_delay": "newPodScaleUpDelay",
        "scale_down_delay_after_add": "scaleDownDelayAfterAdd",
        "scale_down_delay_after_delete": "scaleDownDelayAfterDelete",
        "scale_down_delay_after_failure": "scaleDownDelayAfterFailure",
        "scale_down_unneeded": "scaleDownUnneeded",
        "scale_down_unready": "scaleDownUnready",
        "scale_down_utilization_threshold": "scaleDownUtilizationThreshold",
        "scan_interval": "scanInterval",
        "skip_nodes_with_local_storage": "skipNodesWithLocalStorage",
        "skip_nodes_with_system_pods": "skipNodesWithSystemPods",
    },
)
class KubernetesClusterAutoScalerProfile:
    def __init__(
        self,
        *,
        balance_similar_node_groups: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        empty_bulk_delete_max: typing.Optional[builtins.str] = None,
        expander: typing.Optional[builtins.str] = None,
        max_graceful_termination_sec: typing.Optional[builtins.str] = None,
        max_node_provisioning_time: typing.Optional[builtins.str] = None,
        max_unready_nodes: typing.Optional[jsii.Number] = None,
        max_unready_percentage: typing.Optional[jsii.Number] = None,
        new_pod_scale_up_delay: typing.Optional[builtins.str] = None,
        scale_down_delay_after_add: typing.Optional[builtins.str] = None,
        scale_down_delay_after_delete: typing.Optional[builtins.str] = None,
        scale_down_delay_after_failure: typing.Optional[builtins.str] = None,
        scale_down_unneeded: typing.Optional[builtins.str] = None,
        scale_down_unready: typing.Optional[builtins.str] = None,
        scale_down_utilization_threshold: typing.Optional[builtins.str] = None,
        scan_interval: typing.Optional[builtins.str] = None,
        skip_nodes_with_local_storage: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        skip_nodes_with_system_pods: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param balance_similar_node_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#balance_similar_node_groups KubernetesCluster#balance_similar_node_groups}.
        :param empty_bulk_delete_max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#empty_bulk_delete_max KubernetesCluster#empty_bulk_delete_max}.
        :param expander: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#expander KubernetesCluster#expander}.
        :param max_graceful_termination_sec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_graceful_termination_sec KubernetesCluster#max_graceful_termination_sec}.
        :param max_node_provisioning_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_node_provisioning_time KubernetesCluster#max_node_provisioning_time}.
        :param max_unready_nodes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_unready_nodes KubernetesCluster#max_unready_nodes}.
        :param max_unready_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_unready_percentage KubernetesCluster#max_unready_percentage}.
        :param new_pod_scale_up_delay: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#new_pod_scale_up_delay KubernetesCluster#new_pod_scale_up_delay}.
        :param scale_down_delay_after_add: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_delay_after_add KubernetesCluster#scale_down_delay_after_add}.
        :param scale_down_delay_after_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_delay_after_delete KubernetesCluster#scale_down_delay_after_delete}.
        :param scale_down_delay_after_failure: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_delay_after_failure KubernetesCluster#scale_down_delay_after_failure}.
        :param scale_down_unneeded: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_unneeded KubernetesCluster#scale_down_unneeded}.
        :param scale_down_unready: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_unready KubernetesCluster#scale_down_unready}.
        :param scale_down_utilization_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_utilization_threshold KubernetesCluster#scale_down_utilization_threshold}.
        :param scan_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scan_interval KubernetesCluster#scan_interval}.
        :param skip_nodes_with_local_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#skip_nodes_with_local_storage KubernetesCluster#skip_nodes_with_local_storage}.
        :param skip_nodes_with_system_pods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#skip_nodes_with_system_pods KubernetesCluster#skip_nodes_with_system_pods}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterAutoScalerProfile.__init__)
            check_type(argname="argument balance_similar_node_groups", value=balance_similar_node_groups, expected_type=type_hints["balance_similar_node_groups"])
            check_type(argname="argument empty_bulk_delete_max", value=empty_bulk_delete_max, expected_type=type_hints["empty_bulk_delete_max"])
            check_type(argname="argument expander", value=expander, expected_type=type_hints["expander"])
            check_type(argname="argument max_graceful_termination_sec", value=max_graceful_termination_sec, expected_type=type_hints["max_graceful_termination_sec"])
            check_type(argname="argument max_node_provisioning_time", value=max_node_provisioning_time, expected_type=type_hints["max_node_provisioning_time"])
            check_type(argname="argument max_unready_nodes", value=max_unready_nodes, expected_type=type_hints["max_unready_nodes"])
            check_type(argname="argument max_unready_percentage", value=max_unready_percentage, expected_type=type_hints["max_unready_percentage"])
            check_type(argname="argument new_pod_scale_up_delay", value=new_pod_scale_up_delay, expected_type=type_hints["new_pod_scale_up_delay"])
            check_type(argname="argument scale_down_delay_after_add", value=scale_down_delay_after_add, expected_type=type_hints["scale_down_delay_after_add"])
            check_type(argname="argument scale_down_delay_after_delete", value=scale_down_delay_after_delete, expected_type=type_hints["scale_down_delay_after_delete"])
            check_type(argname="argument scale_down_delay_after_failure", value=scale_down_delay_after_failure, expected_type=type_hints["scale_down_delay_after_failure"])
            check_type(argname="argument scale_down_unneeded", value=scale_down_unneeded, expected_type=type_hints["scale_down_unneeded"])
            check_type(argname="argument scale_down_unready", value=scale_down_unready, expected_type=type_hints["scale_down_unready"])
            check_type(argname="argument scale_down_utilization_threshold", value=scale_down_utilization_threshold, expected_type=type_hints["scale_down_utilization_threshold"])
            check_type(argname="argument scan_interval", value=scan_interval, expected_type=type_hints["scan_interval"])
            check_type(argname="argument skip_nodes_with_local_storage", value=skip_nodes_with_local_storage, expected_type=type_hints["skip_nodes_with_local_storage"])
            check_type(argname="argument skip_nodes_with_system_pods", value=skip_nodes_with_system_pods, expected_type=type_hints["skip_nodes_with_system_pods"])
        self._values: typing.Dict[str, typing.Any] = {}
        if balance_similar_node_groups is not None:
            self._values["balance_similar_node_groups"] = balance_similar_node_groups
        if empty_bulk_delete_max is not None:
            self._values["empty_bulk_delete_max"] = empty_bulk_delete_max
        if expander is not None:
            self._values["expander"] = expander
        if max_graceful_termination_sec is not None:
            self._values["max_graceful_termination_sec"] = max_graceful_termination_sec
        if max_node_provisioning_time is not None:
            self._values["max_node_provisioning_time"] = max_node_provisioning_time
        if max_unready_nodes is not None:
            self._values["max_unready_nodes"] = max_unready_nodes
        if max_unready_percentage is not None:
            self._values["max_unready_percentage"] = max_unready_percentage
        if new_pod_scale_up_delay is not None:
            self._values["new_pod_scale_up_delay"] = new_pod_scale_up_delay
        if scale_down_delay_after_add is not None:
            self._values["scale_down_delay_after_add"] = scale_down_delay_after_add
        if scale_down_delay_after_delete is not None:
            self._values["scale_down_delay_after_delete"] = scale_down_delay_after_delete
        if scale_down_delay_after_failure is not None:
            self._values["scale_down_delay_after_failure"] = scale_down_delay_after_failure
        if scale_down_unneeded is not None:
            self._values["scale_down_unneeded"] = scale_down_unneeded
        if scale_down_unready is not None:
            self._values["scale_down_unready"] = scale_down_unready
        if scale_down_utilization_threshold is not None:
            self._values["scale_down_utilization_threshold"] = scale_down_utilization_threshold
        if scan_interval is not None:
            self._values["scan_interval"] = scan_interval
        if skip_nodes_with_local_storage is not None:
            self._values["skip_nodes_with_local_storage"] = skip_nodes_with_local_storage
        if skip_nodes_with_system_pods is not None:
            self._values["skip_nodes_with_system_pods"] = skip_nodes_with_system_pods

    @builtins.property
    def balance_similar_node_groups(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#balance_similar_node_groups KubernetesCluster#balance_similar_node_groups}.'''
        result = self._values.get("balance_similar_node_groups")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def empty_bulk_delete_max(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#empty_bulk_delete_max KubernetesCluster#empty_bulk_delete_max}.'''
        result = self._values.get("empty_bulk_delete_max")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expander(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#expander KubernetesCluster#expander}.'''
        result = self._values.get("expander")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_graceful_termination_sec(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_graceful_termination_sec KubernetesCluster#max_graceful_termination_sec}.'''
        result = self._values.get("max_graceful_termination_sec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_node_provisioning_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_node_provisioning_time KubernetesCluster#max_node_provisioning_time}.'''
        result = self._values.get("max_node_provisioning_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_unready_nodes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_unready_nodes KubernetesCluster#max_unready_nodes}.'''
        result = self._values.get("max_unready_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_unready_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_unready_percentage KubernetesCluster#max_unready_percentage}.'''
        result = self._values.get("max_unready_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def new_pod_scale_up_delay(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#new_pod_scale_up_delay KubernetesCluster#new_pod_scale_up_delay}.'''
        result = self._values.get("new_pod_scale_up_delay")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_down_delay_after_add(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_delay_after_add KubernetesCluster#scale_down_delay_after_add}.'''
        result = self._values.get("scale_down_delay_after_add")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_down_delay_after_delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_delay_after_delete KubernetesCluster#scale_down_delay_after_delete}.'''
        result = self._values.get("scale_down_delay_after_delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_down_delay_after_failure(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_delay_after_failure KubernetesCluster#scale_down_delay_after_failure}.'''
        result = self._values.get("scale_down_delay_after_failure")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_down_unneeded(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_unneeded KubernetesCluster#scale_down_unneeded}.'''
        result = self._values.get("scale_down_unneeded")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_down_unready(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_unready KubernetesCluster#scale_down_unready}.'''
        result = self._values.get("scale_down_unready")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_down_utilization_threshold(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_utilization_threshold KubernetesCluster#scale_down_utilization_threshold}.'''
        result = self._values.get("scale_down_utilization_threshold")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scan_interval(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scan_interval KubernetesCluster#scan_interval}.'''
        result = self._values.get("scan_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_nodes_with_local_storage(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#skip_nodes_with_local_storage KubernetesCluster#skip_nodes_with_local_storage}.'''
        result = self._values.get("skip_nodes_with_local_storage")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def skip_nodes_with_system_pods(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#skip_nodes_with_system_pods KubernetesCluster#skip_nodes_with_system_pods}.'''
        result = self._values.get("skip_nodes_with_system_pods")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterAutoScalerProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterAutoScalerProfileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterAutoScalerProfileOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterAutoScalerProfileOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBalanceSimilarNodeGroups")
    def reset_balance_similar_node_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBalanceSimilarNodeGroups", []))

    @jsii.member(jsii_name="resetEmptyBulkDeleteMax")
    def reset_empty_bulk_delete_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmptyBulkDeleteMax", []))

    @jsii.member(jsii_name="resetExpander")
    def reset_expander(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpander", []))

    @jsii.member(jsii_name="resetMaxGracefulTerminationSec")
    def reset_max_graceful_termination_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxGracefulTerminationSec", []))

    @jsii.member(jsii_name="resetMaxNodeProvisioningTime")
    def reset_max_node_provisioning_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxNodeProvisioningTime", []))

    @jsii.member(jsii_name="resetMaxUnreadyNodes")
    def reset_max_unready_nodes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxUnreadyNodes", []))

    @jsii.member(jsii_name="resetMaxUnreadyPercentage")
    def reset_max_unready_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxUnreadyPercentage", []))

    @jsii.member(jsii_name="resetNewPodScaleUpDelay")
    def reset_new_pod_scale_up_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNewPodScaleUpDelay", []))

    @jsii.member(jsii_name="resetScaleDownDelayAfterAdd")
    def reset_scale_down_delay_after_add(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleDownDelayAfterAdd", []))

    @jsii.member(jsii_name="resetScaleDownDelayAfterDelete")
    def reset_scale_down_delay_after_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleDownDelayAfterDelete", []))

    @jsii.member(jsii_name="resetScaleDownDelayAfterFailure")
    def reset_scale_down_delay_after_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleDownDelayAfterFailure", []))

    @jsii.member(jsii_name="resetScaleDownUnneeded")
    def reset_scale_down_unneeded(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleDownUnneeded", []))

    @jsii.member(jsii_name="resetScaleDownUnready")
    def reset_scale_down_unready(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleDownUnready", []))

    @jsii.member(jsii_name="resetScaleDownUtilizationThreshold")
    def reset_scale_down_utilization_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleDownUtilizationThreshold", []))

    @jsii.member(jsii_name="resetScanInterval")
    def reset_scan_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScanInterval", []))

    @jsii.member(jsii_name="resetSkipNodesWithLocalStorage")
    def reset_skip_nodes_with_local_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipNodesWithLocalStorage", []))

    @jsii.member(jsii_name="resetSkipNodesWithSystemPods")
    def reset_skip_nodes_with_system_pods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipNodesWithSystemPods", []))

    @builtins.property
    @jsii.member(jsii_name="balanceSimilarNodeGroupsInput")
    def balance_similar_node_groups_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "balanceSimilarNodeGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="emptyBulkDeleteMaxInput")
    def empty_bulk_delete_max_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emptyBulkDeleteMaxInput"))

    @builtins.property
    @jsii.member(jsii_name="expanderInput")
    def expander_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expanderInput"))

    @builtins.property
    @jsii.member(jsii_name="maxGracefulTerminationSecInput")
    def max_graceful_termination_sec_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxGracefulTerminationSecInput"))

    @builtins.property
    @jsii.member(jsii_name="maxNodeProvisioningTimeInput")
    def max_node_provisioning_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxNodeProvisioningTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxUnreadyNodesInput")
    def max_unready_nodes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxUnreadyNodesInput"))

    @builtins.property
    @jsii.member(jsii_name="maxUnreadyPercentageInput")
    def max_unready_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxUnreadyPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="newPodScaleUpDelayInput")
    def new_pod_scale_up_delay_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "newPodScaleUpDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleDownDelayAfterAddInput")
    def scale_down_delay_after_add_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scaleDownDelayAfterAddInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleDownDelayAfterDeleteInput")
    def scale_down_delay_after_delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scaleDownDelayAfterDeleteInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleDownDelayAfterFailureInput")
    def scale_down_delay_after_failure_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scaleDownDelayAfterFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleDownUnneededInput")
    def scale_down_unneeded_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scaleDownUnneededInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleDownUnreadyInput")
    def scale_down_unready_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scaleDownUnreadyInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleDownUtilizationThresholdInput")
    def scale_down_utilization_threshold_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scaleDownUtilizationThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="scanIntervalInput")
    def scan_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scanIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="skipNodesWithLocalStorageInput")
    def skip_nodes_with_local_storage_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipNodesWithLocalStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="skipNodesWithSystemPodsInput")
    def skip_nodes_with_system_pods_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipNodesWithSystemPodsInput"))

    @builtins.property
    @jsii.member(jsii_name="balanceSimilarNodeGroups")
    def balance_similar_node_groups(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "balanceSimilarNodeGroups"))

    @balance_similar_node_groups.setter
    def balance_similar_node_groups(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAutoScalerProfileOutputReference, "balance_similar_node_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "balanceSimilarNodeGroups", value)

    @builtins.property
    @jsii.member(jsii_name="emptyBulkDeleteMax")
    def empty_bulk_delete_max(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emptyBulkDeleteMax"))

    @empty_bulk_delete_max.setter
    def empty_bulk_delete_max(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAutoScalerProfileOutputReference, "empty_bulk_delete_max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emptyBulkDeleteMax", value)

    @builtins.property
    @jsii.member(jsii_name="expander")
    def expander(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expander"))

    @expander.setter
    def expander(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAutoScalerProfileOutputReference, "expander").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expander", value)

    @builtins.property
    @jsii.member(jsii_name="maxGracefulTerminationSec")
    def max_graceful_termination_sec(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxGracefulTerminationSec"))

    @max_graceful_termination_sec.setter
    def max_graceful_termination_sec(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAutoScalerProfileOutputReference, "max_graceful_termination_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxGracefulTerminationSec", value)

    @builtins.property
    @jsii.member(jsii_name="maxNodeProvisioningTime")
    def max_node_provisioning_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxNodeProvisioningTime"))

    @max_node_provisioning_time.setter
    def max_node_provisioning_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAutoScalerProfileOutputReference, "max_node_provisioning_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxNodeProvisioningTime", value)

    @builtins.property
    @jsii.member(jsii_name="maxUnreadyNodes")
    def max_unready_nodes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUnreadyNodes"))

    @max_unready_nodes.setter
    def max_unready_nodes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAutoScalerProfileOutputReference, "max_unready_nodes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUnreadyNodes", value)

    @builtins.property
    @jsii.member(jsii_name="maxUnreadyPercentage")
    def max_unready_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUnreadyPercentage"))

    @max_unready_percentage.setter
    def max_unready_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAutoScalerProfileOutputReference, "max_unready_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUnreadyPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="newPodScaleUpDelay")
    def new_pod_scale_up_delay(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "newPodScaleUpDelay"))

    @new_pod_scale_up_delay.setter
    def new_pod_scale_up_delay(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAutoScalerProfileOutputReference, "new_pod_scale_up_delay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "newPodScaleUpDelay", value)

    @builtins.property
    @jsii.member(jsii_name="scaleDownDelayAfterAdd")
    def scale_down_delay_after_add(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleDownDelayAfterAdd"))

    @scale_down_delay_after_add.setter
    def scale_down_delay_after_add(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAutoScalerProfileOutputReference, "scale_down_delay_after_add").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleDownDelayAfterAdd", value)

    @builtins.property
    @jsii.member(jsii_name="scaleDownDelayAfterDelete")
    def scale_down_delay_after_delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleDownDelayAfterDelete"))

    @scale_down_delay_after_delete.setter
    def scale_down_delay_after_delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAutoScalerProfileOutputReference, "scale_down_delay_after_delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleDownDelayAfterDelete", value)

    @builtins.property
    @jsii.member(jsii_name="scaleDownDelayAfterFailure")
    def scale_down_delay_after_failure(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleDownDelayAfterFailure"))

    @scale_down_delay_after_failure.setter
    def scale_down_delay_after_failure(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAutoScalerProfileOutputReference, "scale_down_delay_after_failure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleDownDelayAfterFailure", value)

    @builtins.property
    @jsii.member(jsii_name="scaleDownUnneeded")
    def scale_down_unneeded(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleDownUnneeded"))

    @scale_down_unneeded.setter
    def scale_down_unneeded(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAutoScalerProfileOutputReference, "scale_down_unneeded").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleDownUnneeded", value)

    @builtins.property
    @jsii.member(jsii_name="scaleDownUnready")
    def scale_down_unready(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleDownUnready"))

    @scale_down_unready.setter
    def scale_down_unready(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAutoScalerProfileOutputReference, "scale_down_unready").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleDownUnready", value)

    @builtins.property
    @jsii.member(jsii_name="scaleDownUtilizationThreshold")
    def scale_down_utilization_threshold(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleDownUtilizationThreshold"))

    @scale_down_utilization_threshold.setter
    def scale_down_utilization_threshold(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAutoScalerProfileOutputReference, "scale_down_utilization_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleDownUtilizationThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="scanInterval")
    def scan_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scanInterval"))

    @scan_interval.setter
    def scan_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAutoScalerProfileOutputReference, "scan_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scanInterval", value)

    @builtins.property
    @jsii.member(jsii_name="skipNodesWithLocalStorage")
    def skip_nodes_with_local_storage(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "skipNodesWithLocalStorage"))

    @skip_nodes_with_local_storage.setter
    def skip_nodes_with_local_storage(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAutoScalerProfileOutputReference, "skip_nodes_with_local_storage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipNodesWithLocalStorage", value)

    @builtins.property
    @jsii.member(jsii_name="skipNodesWithSystemPods")
    def skip_nodes_with_system_pods(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "skipNodesWithSystemPods"))

    @skip_nodes_with_system_pods.setter
    def skip_nodes_with_system_pods(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAutoScalerProfileOutputReference, "skip_nodes_with_system_pods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipNodesWithSystemPods", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterAutoScalerProfile]:
        return typing.cast(typing.Optional[KubernetesClusterAutoScalerProfile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterAutoScalerProfile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAutoScalerProfileOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterAzureActiveDirectoryRoleBasedAccessControl",
    jsii_struct_bases=[],
    name_mapping={
        "admin_group_object_ids": "adminGroupObjectIds",
        "azure_rbac_enabled": "azureRbacEnabled",
        "client_app_id": "clientAppId",
        "managed": "managed",
        "server_app_id": "serverAppId",
        "server_app_secret": "serverAppSecret",
        "tenant_id": "tenantId",
    },
)
class KubernetesClusterAzureActiveDirectoryRoleBasedAccessControl:
    def __init__(
        self,
        *,
        admin_group_object_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        azure_rbac_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        client_app_id: typing.Optional[builtins.str] = None,
        managed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        server_app_id: typing.Optional[builtins.str] = None,
        server_app_secret: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_group_object_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#admin_group_object_ids KubernetesCluster#admin_group_object_ids}.
        :param azure_rbac_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#azure_rbac_enabled KubernetesCluster#azure_rbac_enabled}.
        :param client_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#client_app_id KubernetesCluster#client_app_id}.
        :param managed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#managed KubernetesCluster#managed}.
        :param server_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#server_app_id KubernetesCluster#server_app_id}.
        :param server_app_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#server_app_secret KubernetesCluster#server_app_secret}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#tenant_id KubernetesCluster#tenant_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterAzureActiveDirectoryRoleBasedAccessControl.__init__)
            check_type(argname="argument admin_group_object_ids", value=admin_group_object_ids, expected_type=type_hints["admin_group_object_ids"])
            check_type(argname="argument azure_rbac_enabled", value=azure_rbac_enabled, expected_type=type_hints["azure_rbac_enabled"])
            check_type(argname="argument client_app_id", value=client_app_id, expected_type=type_hints["client_app_id"])
            check_type(argname="argument managed", value=managed, expected_type=type_hints["managed"])
            check_type(argname="argument server_app_id", value=server_app_id, expected_type=type_hints["server_app_id"])
            check_type(argname="argument server_app_secret", value=server_app_secret, expected_type=type_hints["server_app_secret"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if admin_group_object_ids is not None:
            self._values["admin_group_object_ids"] = admin_group_object_ids
        if azure_rbac_enabled is not None:
            self._values["azure_rbac_enabled"] = azure_rbac_enabled
        if client_app_id is not None:
            self._values["client_app_id"] = client_app_id
        if managed is not None:
            self._values["managed"] = managed
        if server_app_id is not None:
            self._values["server_app_id"] = server_app_id
        if server_app_secret is not None:
            self._values["server_app_secret"] = server_app_secret
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id

    @builtins.property
    def admin_group_object_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#admin_group_object_ids KubernetesCluster#admin_group_object_ids}.'''
        result = self._values.get("admin_group_object_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def azure_rbac_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#azure_rbac_enabled KubernetesCluster#azure_rbac_enabled}.'''
        result = self._values.get("azure_rbac_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def client_app_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#client_app_id KubernetesCluster#client_app_id}.'''
        result = self._values.get("client_app_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#managed KubernetesCluster#managed}.'''
        result = self._values.get("managed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def server_app_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#server_app_id KubernetesCluster#server_app_id}.'''
        result = self._values.get("server_app_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_app_secret(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#server_app_secret KubernetesCluster#server_app_secret}.'''
        result = self._values.get("server_app_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#tenant_id KubernetesCluster#tenant_id}.'''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterAzureActiveDirectoryRoleBasedAccessControl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterAzureActiveDirectoryRoleBasedAccessControlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterAzureActiveDirectoryRoleBasedAccessControlOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterAzureActiveDirectoryRoleBasedAccessControlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAdminGroupObjectIds")
    def reset_admin_group_object_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminGroupObjectIds", []))

    @jsii.member(jsii_name="resetAzureRbacEnabled")
    def reset_azure_rbac_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureRbacEnabled", []))

    @jsii.member(jsii_name="resetClientAppId")
    def reset_client_app_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientAppId", []))

    @jsii.member(jsii_name="resetManaged")
    def reset_managed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManaged", []))

    @jsii.member(jsii_name="resetServerAppId")
    def reset_server_app_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerAppId", []))

    @jsii.member(jsii_name="resetServerAppSecret")
    def reset_server_app_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerAppSecret", []))

    @jsii.member(jsii_name="resetTenantId")
    def reset_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenantId", []))

    @builtins.property
    @jsii.member(jsii_name="adminGroupObjectIdsInput")
    def admin_group_object_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "adminGroupObjectIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="azureRbacEnabledInput")
    def azure_rbac_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "azureRbacEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="clientAppIdInput")
    def client_app_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientAppIdInput"))

    @builtins.property
    @jsii.member(jsii_name="managedInput")
    def managed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "managedInput"))

    @builtins.property
    @jsii.member(jsii_name="serverAppIdInput")
    def server_app_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverAppIdInput"))

    @builtins.property
    @jsii.member(jsii_name="serverAppSecretInput")
    def server_app_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverAppSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="adminGroupObjectIds")
    def admin_group_object_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "adminGroupObjectIds"))

    @admin_group_object_ids.setter
    def admin_group_object_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAzureActiveDirectoryRoleBasedAccessControlOutputReference, "admin_group_object_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminGroupObjectIds", value)

    @builtins.property
    @jsii.member(jsii_name="azureRbacEnabled")
    def azure_rbac_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "azureRbacEnabled"))

    @azure_rbac_enabled.setter
    def azure_rbac_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAzureActiveDirectoryRoleBasedAccessControlOutputReference, "azure_rbac_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureRbacEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="clientAppId")
    def client_app_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientAppId"))

    @client_app_id.setter
    def client_app_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAzureActiveDirectoryRoleBasedAccessControlOutputReference, "client_app_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientAppId", value)

    @builtins.property
    @jsii.member(jsii_name="managed")
    def managed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "managed"))

    @managed.setter
    def managed(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAzureActiveDirectoryRoleBasedAccessControlOutputReference, "managed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managed", value)

    @builtins.property
    @jsii.member(jsii_name="serverAppId")
    def server_app_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverAppId"))

    @server_app_id.setter
    def server_app_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAzureActiveDirectoryRoleBasedAccessControlOutputReference, "server_app_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverAppId", value)

    @builtins.property
    @jsii.member(jsii_name="serverAppSecret")
    def server_app_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverAppSecret"))

    @server_app_secret.setter
    def server_app_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAzureActiveDirectoryRoleBasedAccessControlOutputReference, "server_app_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverAppSecret", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAzureActiveDirectoryRoleBasedAccessControlOutputReference, "tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KubernetesClusterAzureActiveDirectoryRoleBasedAccessControl]:
        return typing.cast(typing.Optional[KubernetesClusterAzureActiveDirectoryRoleBasedAccessControl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterAzureActiveDirectoryRoleBasedAccessControl],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterAzureActiveDirectoryRoleBasedAccessControlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "default_node_pool": "defaultNodePool",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "aci_connector_linux": "aciConnectorLinux",
        "api_server_authorized_ip_ranges": "apiServerAuthorizedIpRanges",
        "automatic_channel_upgrade": "automaticChannelUpgrade",
        "auto_scaler_profile": "autoScalerProfile",
        "azure_active_directory_role_based_access_control": "azureActiveDirectoryRoleBasedAccessControl",
        "azure_policy_enabled": "azurePolicyEnabled",
        "disk_encryption_set_id": "diskEncryptionSetId",
        "dns_prefix": "dnsPrefix",
        "dns_prefix_private_cluster": "dnsPrefixPrivateCluster",
        "edge_zone": "edgeZone",
        "enable_pod_security_policy": "enablePodSecurityPolicy",
        "http_application_routing_enabled": "httpApplicationRoutingEnabled",
        "http_proxy_config": "httpProxyConfig",
        "id": "id",
        "identity": "identity",
        "ingress_application_gateway": "ingressApplicationGateway",
        "key_vault_secrets_provider": "keyVaultSecretsProvider",
        "kubelet_identity": "kubeletIdentity",
        "kubernetes_version": "kubernetesVersion",
        "linux_profile": "linuxProfile",
        "local_account_disabled": "localAccountDisabled",
        "maintenance_window": "maintenanceWindow",
        "microsoft_defender": "microsoftDefender",
        "network_profile": "networkProfile",
        "node_resource_group": "nodeResourceGroup",
        "oidc_issuer_enabled": "oidcIssuerEnabled",
        "oms_agent": "omsAgent",
        "open_service_mesh_enabled": "openServiceMeshEnabled",
        "private_cluster_enabled": "privateClusterEnabled",
        "private_cluster_public_fqdn_enabled": "privateClusterPublicFqdnEnabled",
        "private_dns_zone_id": "privateDnsZoneId",
        "public_network_access_enabled": "publicNetworkAccessEnabled",
        "role_based_access_control_enabled": "roleBasedAccessControlEnabled",
        "run_command_enabled": "runCommandEnabled",
        "service_principal": "servicePrincipal",
        "sku_tier": "skuTier",
        "tags": "tags",
        "timeouts": "timeouts",
        "windows_profile": "windowsProfile",
    },
)
class KubernetesClusterConfig(cdktf.TerraformMetaArguments):
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
        default_node_pool: typing.Union["KubernetesClusterDefaultNodePool", typing.Dict[str, typing.Any]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        aci_connector_linux: typing.Optional[typing.Union[KubernetesClusterAciConnectorLinux, typing.Dict[str, typing.Any]]] = None,
        api_server_authorized_ip_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        automatic_channel_upgrade: typing.Optional[builtins.str] = None,
        auto_scaler_profile: typing.Optional[typing.Union[KubernetesClusterAutoScalerProfile, typing.Dict[str, typing.Any]]] = None,
        azure_active_directory_role_based_access_control: typing.Optional[typing.Union[KubernetesClusterAzureActiveDirectoryRoleBasedAccessControl, typing.Dict[str, typing.Any]]] = None,
        azure_policy_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disk_encryption_set_id: typing.Optional[builtins.str] = None,
        dns_prefix: typing.Optional[builtins.str] = None,
        dns_prefix_private_cluster: typing.Optional[builtins.str] = None,
        edge_zone: typing.Optional[builtins.str] = None,
        enable_pod_security_policy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        http_application_routing_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        http_proxy_config: typing.Optional[typing.Union["KubernetesClusterHttpProxyConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["KubernetesClusterIdentity", typing.Dict[str, typing.Any]]] = None,
        ingress_application_gateway: typing.Optional[typing.Union["KubernetesClusterIngressApplicationGateway", typing.Dict[str, typing.Any]]] = None,
        key_vault_secrets_provider: typing.Optional[typing.Union["KubernetesClusterKeyVaultSecretsProvider", typing.Dict[str, typing.Any]]] = None,
        kubelet_identity: typing.Optional[typing.Union["KubernetesClusterKubeletIdentity", typing.Dict[str, typing.Any]]] = None,
        kubernetes_version: typing.Optional[builtins.str] = None,
        linux_profile: typing.Optional[typing.Union["KubernetesClusterLinuxProfile", typing.Dict[str, typing.Any]]] = None,
        local_account_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        maintenance_window: typing.Optional[typing.Union["KubernetesClusterMaintenanceWindow", typing.Dict[str, typing.Any]]] = None,
        microsoft_defender: typing.Optional[typing.Union["KubernetesClusterMicrosoftDefender", typing.Dict[str, typing.Any]]] = None,
        network_profile: typing.Optional[typing.Union["KubernetesClusterNetworkProfile", typing.Dict[str, typing.Any]]] = None,
        node_resource_group: typing.Optional[builtins.str] = None,
        oidc_issuer_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        oms_agent: typing.Optional[typing.Union["KubernetesClusterOmsAgent", typing.Dict[str, typing.Any]]] = None,
        open_service_mesh_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        private_cluster_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        private_cluster_public_fqdn_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        private_dns_zone_id: typing.Optional[builtins.str] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        role_based_access_control_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        run_command_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        service_principal: typing.Optional[typing.Union["KubernetesClusterServicePrincipal", typing.Dict[str, typing.Any]]] = None,
        sku_tier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KubernetesClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        windows_profile: typing.Optional[typing.Union["KubernetesClusterWindowsProfile", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param default_node_pool: default_node_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#default_node_pool KubernetesCluster#default_node_pool}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#location KubernetesCluster#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#name KubernetesCluster#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#resource_group_name KubernetesCluster#resource_group_name}.
        :param aci_connector_linux: aci_connector_linux block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#aci_connector_linux KubernetesCluster#aci_connector_linux}
        :param api_server_authorized_ip_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#api_server_authorized_ip_ranges KubernetesCluster#api_server_authorized_ip_ranges}.
        :param automatic_channel_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#automatic_channel_upgrade KubernetesCluster#automatic_channel_upgrade}.
        :param auto_scaler_profile: auto_scaler_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#auto_scaler_profile KubernetesCluster#auto_scaler_profile}
        :param azure_active_directory_role_based_access_control: azure_active_directory_role_based_access_control block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#azure_active_directory_role_based_access_control KubernetesCluster#azure_active_directory_role_based_access_control}
        :param azure_policy_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#azure_policy_enabled KubernetesCluster#azure_policy_enabled}.
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#disk_encryption_set_id KubernetesCluster#disk_encryption_set_id}.
        :param dns_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#dns_prefix KubernetesCluster#dns_prefix}.
        :param dns_prefix_private_cluster: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#dns_prefix_private_cluster KubernetesCluster#dns_prefix_private_cluster}.
        :param edge_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#edge_zone KubernetesCluster#edge_zone}.
        :param enable_pod_security_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#enable_pod_security_policy KubernetesCluster#enable_pod_security_policy}.
        :param http_application_routing_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#http_application_routing_enabled KubernetesCluster#http_application_routing_enabled}.
        :param http_proxy_config: http_proxy_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#http_proxy_config KubernetesCluster#http_proxy_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#id KubernetesCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#identity KubernetesCluster#identity}
        :param ingress_application_gateway: ingress_application_gateway block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#ingress_application_gateway KubernetesCluster#ingress_application_gateway}
        :param key_vault_secrets_provider: key_vault_secrets_provider block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#key_vault_secrets_provider KubernetesCluster#key_vault_secrets_provider}
        :param kubelet_identity: kubelet_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#kubelet_identity KubernetesCluster#kubelet_identity}
        :param kubernetes_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#kubernetes_version KubernetesCluster#kubernetes_version}.
        :param linux_profile: linux_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#linux_profile KubernetesCluster#linux_profile}
        :param local_account_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#local_account_disabled KubernetesCluster#local_account_disabled}.
        :param maintenance_window: maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#maintenance_window KubernetesCluster#maintenance_window}
        :param microsoft_defender: microsoft_defender block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#microsoft_defender KubernetesCluster#microsoft_defender}
        :param network_profile: network_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#network_profile KubernetesCluster#network_profile}
        :param node_resource_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#node_resource_group KubernetesCluster#node_resource_group}.
        :param oidc_issuer_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#oidc_issuer_enabled KubernetesCluster#oidc_issuer_enabled}.
        :param oms_agent: oms_agent block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#oms_agent KubernetesCluster#oms_agent}
        :param open_service_mesh_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#open_service_mesh_enabled KubernetesCluster#open_service_mesh_enabled}.
        :param private_cluster_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#private_cluster_enabled KubernetesCluster#private_cluster_enabled}.
        :param private_cluster_public_fqdn_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#private_cluster_public_fqdn_enabled KubernetesCluster#private_cluster_public_fqdn_enabled}.
        :param private_dns_zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#private_dns_zone_id KubernetesCluster#private_dns_zone_id}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#public_network_access_enabled KubernetesCluster#public_network_access_enabled}.
        :param role_based_access_control_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#role_based_access_control_enabled KubernetesCluster#role_based_access_control_enabled}.
        :param run_command_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#run_command_enabled KubernetesCluster#run_command_enabled}.
        :param service_principal: service_principal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#service_principal KubernetesCluster#service_principal}
        :param sku_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#sku_tier KubernetesCluster#sku_tier}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#tags KubernetesCluster#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#timeouts KubernetesCluster#timeouts}
        :param windows_profile: windows_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#windows_profile KubernetesCluster#windows_profile}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(default_node_pool, dict):
            default_node_pool = KubernetesClusterDefaultNodePool(**default_node_pool)
        if isinstance(aci_connector_linux, dict):
            aci_connector_linux = KubernetesClusterAciConnectorLinux(**aci_connector_linux)
        if isinstance(auto_scaler_profile, dict):
            auto_scaler_profile = KubernetesClusterAutoScalerProfile(**auto_scaler_profile)
        if isinstance(azure_active_directory_role_based_access_control, dict):
            azure_active_directory_role_based_access_control = KubernetesClusterAzureActiveDirectoryRoleBasedAccessControl(**azure_active_directory_role_based_access_control)
        if isinstance(http_proxy_config, dict):
            http_proxy_config = KubernetesClusterHttpProxyConfig(**http_proxy_config)
        if isinstance(identity, dict):
            identity = KubernetesClusterIdentity(**identity)
        if isinstance(ingress_application_gateway, dict):
            ingress_application_gateway = KubernetesClusterIngressApplicationGateway(**ingress_application_gateway)
        if isinstance(key_vault_secrets_provider, dict):
            key_vault_secrets_provider = KubernetesClusterKeyVaultSecretsProvider(**key_vault_secrets_provider)
        if isinstance(kubelet_identity, dict):
            kubelet_identity = KubernetesClusterKubeletIdentity(**kubelet_identity)
        if isinstance(linux_profile, dict):
            linux_profile = KubernetesClusterLinuxProfile(**linux_profile)
        if isinstance(maintenance_window, dict):
            maintenance_window = KubernetesClusterMaintenanceWindow(**maintenance_window)
        if isinstance(microsoft_defender, dict):
            microsoft_defender = KubernetesClusterMicrosoftDefender(**microsoft_defender)
        if isinstance(network_profile, dict):
            network_profile = KubernetesClusterNetworkProfile(**network_profile)
        if isinstance(oms_agent, dict):
            oms_agent = KubernetesClusterOmsAgent(**oms_agent)
        if isinstance(service_principal, dict):
            service_principal = KubernetesClusterServicePrincipal(**service_principal)
        if isinstance(timeouts, dict):
            timeouts = KubernetesClusterTimeouts(**timeouts)
        if isinstance(windows_profile, dict):
            windows_profile = KubernetesClusterWindowsProfile(**windows_profile)
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument default_node_pool", value=default_node_pool, expected_type=type_hints["default_node_pool"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument aci_connector_linux", value=aci_connector_linux, expected_type=type_hints["aci_connector_linux"])
            check_type(argname="argument api_server_authorized_ip_ranges", value=api_server_authorized_ip_ranges, expected_type=type_hints["api_server_authorized_ip_ranges"])
            check_type(argname="argument automatic_channel_upgrade", value=automatic_channel_upgrade, expected_type=type_hints["automatic_channel_upgrade"])
            check_type(argname="argument auto_scaler_profile", value=auto_scaler_profile, expected_type=type_hints["auto_scaler_profile"])
            check_type(argname="argument azure_active_directory_role_based_access_control", value=azure_active_directory_role_based_access_control, expected_type=type_hints["azure_active_directory_role_based_access_control"])
            check_type(argname="argument azure_policy_enabled", value=azure_policy_enabled, expected_type=type_hints["azure_policy_enabled"])
            check_type(argname="argument disk_encryption_set_id", value=disk_encryption_set_id, expected_type=type_hints["disk_encryption_set_id"])
            check_type(argname="argument dns_prefix", value=dns_prefix, expected_type=type_hints["dns_prefix"])
            check_type(argname="argument dns_prefix_private_cluster", value=dns_prefix_private_cluster, expected_type=type_hints["dns_prefix_private_cluster"])
            check_type(argname="argument edge_zone", value=edge_zone, expected_type=type_hints["edge_zone"])
            check_type(argname="argument enable_pod_security_policy", value=enable_pod_security_policy, expected_type=type_hints["enable_pod_security_policy"])
            check_type(argname="argument http_application_routing_enabled", value=http_application_routing_enabled, expected_type=type_hints["http_application_routing_enabled"])
            check_type(argname="argument http_proxy_config", value=http_proxy_config, expected_type=type_hints["http_proxy_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument ingress_application_gateway", value=ingress_application_gateway, expected_type=type_hints["ingress_application_gateway"])
            check_type(argname="argument key_vault_secrets_provider", value=key_vault_secrets_provider, expected_type=type_hints["key_vault_secrets_provider"])
            check_type(argname="argument kubelet_identity", value=kubelet_identity, expected_type=type_hints["kubelet_identity"])
            check_type(argname="argument kubernetes_version", value=kubernetes_version, expected_type=type_hints["kubernetes_version"])
            check_type(argname="argument linux_profile", value=linux_profile, expected_type=type_hints["linux_profile"])
            check_type(argname="argument local_account_disabled", value=local_account_disabled, expected_type=type_hints["local_account_disabled"])
            check_type(argname="argument maintenance_window", value=maintenance_window, expected_type=type_hints["maintenance_window"])
            check_type(argname="argument microsoft_defender", value=microsoft_defender, expected_type=type_hints["microsoft_defender"])
            check_type(argname="argument network_profile", value=network_profile, expected_type=type_hints["network_profile"])
            check_type(argname="argument node_resource_group", value=node_resource_group, expected_type=type_hints["node_resource_group"])
            check_type(argname="argument oidc_issuer_enabled", value=oidc_issuer_enabled, expected_type=type_hints["oidc_issuer_enabled"])
            check_type(argname="argument oms_agent", value=oms_agent, expected_type=type_hints["oms_agent"])
            check_type(argname="argument open_service_mesh_enabled", value=open_service_mesh_enabled, expected_type=type_hints["open_service_mesh_enabled"])
            check_type(argname="argument private_cluster_enabled", value=private_cluster_enabled, expected_type=type_hints["private_cluster_enabled"])
            check_type(argname="argument private_cluster_public_fqdn_enabled", value=private_cluster_public_fqdn_enabled, expected_type=type_hints["private_cluster_public_fqdn_enabled"])
            check_type(argname="argument private_dns_zone_id", value=private_dns_zone_id, expected_type=type_hints["private_dns_zone_id"])
            check_type(argname="argument public_network_access_enabled", value=public_network_access_enabled, expected_type=type_hints["public_network_access_enabled"])
            check_type(argname="argument role_based_access_control_enabled", value=role_based_access_control_enabled, expected_type=type_hints["role_based_access_control_enabled"])
            check_type(argname="argument run_command_enabled", value=run_command_enabled, expected_type=type_hints["run_command_enabled"])
            check_type(argname="argument service_principal", value=service_principal, expected_type=type_hints["service_principal"])
            check_type(argname="argument sku_tier", value=sku_tier, expected_type=type_hints["sku_tier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument windows_profile", value=windows_profile, expected_type=type_hints["windows_profile"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_node_pool": default_node_pool,
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
        if aci_connector_linux is not None:
            self._values["aci_connector_linux"] = aci_connector_linux
        if api_server_authorized_ip_ranges is not None:
            self._values["api_server_authorized_ip_ranges"] = api_server_authorized_ip_ranges
        if automatic_channel_upgrade is not None:
            self._values["automatic_channel_upgrade"] = automatic_channel_upgrade
        if auto_scaler_profile is not None:
            self._values["auto_scaler_profile"] = auto_scaler_profile
        if azure_active_directory_role_based_access_control is not None:
            self._values["azure_active_directory_role_based_access_control"] = azure_active_directory_role_based_access_control
        if azure_policy_enabled is not None:
            self._values["azure_policy_enabled"] = azure_policy_enabled
        if disk_encryption_set_id is not None:
            self._values["disk_encryption_set_id"] = disk_encryption_set_id
        if dns_prefix is not None:
            self._values["dns_prefix"] = dns_prefix
        if dns_prefix_private_cluster is not None:
            self._values["dns_prefix_private_cluster"] = dns_prefix_private_cluster
        if edge_zone is not None:
            self._values["edge_zone"] = edge_zone
        if enable_pod_security_policy is not None:
            self._values["enable_pod_security_policy"] = enable_pod_security_policy
        if http_application_routing_enabled is not None:
            self._values["http_application_routing_enabled"] = http_application_routing_enabled
        if http_proxy_config is not None:
            self._values["http_proxy_config"] = http_proxy_config
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if ingress_application_gateway is not None:
            self._values["ingress_application_gateway"] = ingress_application_gateway
        if key_vault_secrets_provider is not None:
            self._values["key_vault_secrets_provider"] = key_vault_secrets_provider
        if kubelet_identity is not None:
            self._values["kubelet_identity"] = kubelet_identity
        if kubernetes_version is not None:
            self._values["kubernetes_version"] = kubernetes_version
        if linux_profile is not None:
            self._values["linux_profile"] = linux_profile
        if local_account_disabled is not None:
            self._values["local_account_disabled"] = local_account_disabled
        if maintenance_window is not None:
            self._values["maintenance_window"] = maintenance_window
        if microsoft_defender is not None:
            self._values["microsoft_defender"] = microsoft_defender
        if network_profile is not None:
            self._values["network_profile"] = network_profile
        if node_resource_group is not None:
            self._values["node_resource_group"] = node_resource_group
        if oidc_issuer_enabled is not None:
            self._values["oidc_issuer_enabled"] = oidc_issuer_enabled
        if oms_agent is not None:
            self._values["oms_agent"] = oms_agent
        if open_service_mesh_enabled is not None:
            self._values["open_service_mesh_enabled"] = open_service_mesh_enabled
        if private_cluster_enabled is not None:
            self._values["private_cluster_enabled"] = private_cluster_enabled
        if private_cluster_public_fqdn_enabled is not None:
            self._values["private_cluster_public_fqdn_enabled"] = private_cluster_public_fqdn_enabled
        if private_dns_zone_id is not None:
            self._values["private_dns_zone_id"] = private_dns_zone_id
        if public_network_access_enabled is not None:
            self._values["public_network_access_enabled"] = public_network_access_enabled
        if role_based_access_control_enabled is not None:
            self._values["role_based_access_control_enabled"] = role_based_access_control_enabled
        if run_command_enabled is not None:
            self._values["run_command_enabled"] = run_command_enabled
        if service_principal is not None:
            self._values["service_principal"] = service_principal
        if sku_tier is not None:
            self._values["sku_tier"] = sku_tier
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if windows_profile is not None:
            self._values["windows_profile"] = windows_profile

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
    def default_node_pool(self) -> "KubernetesClusterDefaultNodePool":
        '''default_node_pool block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#default_node_pool KubernetesCluster#default_node_pool}
        '''
        result = self._values.get("default_node_pool")
        assert result is not None, "Required property 'default_node_pool' is missing"
        return typing.cast("KubernetesClusterDefaultNodePool", result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#location KubernetesCluster#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#name KubernetesCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#resource_group_name KubernetesCluster#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aci_connector_linux(
        self,
    ) -> typing.Optional[KubernetesClusterAciConnectorLinux]:
        '''aci_connector_linux block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#aci_connector_linux KubernetesCluster#aci_connector_linux}
        '''
        result = self._values.get("aci_connector_linux")
        return typing.cast(typing.Optional[KubernetesClusterAciConnectorLinux], result)

    @builtins.property
    def api_server_authorized_ip_ranges(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#api_server_authorized_ip_ranges KubernetesCluster#api_server_authorized_ip_ranges}.'''
        result = self._values.get("api_server_authorized_ip_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def automatic_channel_upgrade(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#automatic_channel_upgrade KubernetesCluster#automatic_channel_upgrade}.'''
        result = self._values.get("automatic_channel_upgrade")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_scaler_profile(
        self,
    ) -> typing.Optional[KubernetesClusterAutoScalerProfile]:
        '''auto_scaler_profile block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#auto_scaler_profile KubernetesCluster#auto_scaler_profile}
        '''
        result = self._values.get("auto_scaler_profile")
        return typing.cast(typing.Optional[KubernetesClusterAutoScalerProfile], result)

    @builtins.property
    def azure_active_directory_role_based_access_control(
        self,
    ) -> typing.Optional[KubernetesClusterAzureActiveDirectoryRoleBasedAccessControl]:
        '''azure_active_directory_role_based_access_control block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#azure_active_directory_role_based_access_control KubernetesCluster#azure_active_directory_role_based_access_control}
        '''
        result = self._values.get("azure_active_directory_role_based_access_control")
        return typing.cast(typing.Optional[KubernetesClusterAzureActiveDirectoryRoleBasedAccessControl], result)

    @builtins.property
    def azure_policy_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#azure_policy_enabled KubernetesCluster#azure_policy_enabled}.'''
        result = self._values.get("azure_policy_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def disk_encryption_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#disk_encryption_set_id KubernetesCluster#disk_encryption_set_id}.'''
        result = self._values.get("disk_encryption_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#dns_prefix KubernetesCluster#dns_prefix}.'''
        result = self._values.get("dns_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns_prefix_private_cluster(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#dns_prefix_private_cluster KubernetesCluster#dns_prefix_private_cluster}.'''
        result = self._values.get("dns_prefix_private_cluster")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def edge_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#edge_zone KubernetesCluster#edge_zone}.'''
        result = self._values.get("edge_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_pod_security_policy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#enable_pod_security_policy KubernetesCluster#enable_pod_security_policy}.'''
        result = self._values.get("enable_pod_security_policy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def http_application_routing_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#http_application_routing_enabled KubernetesCluster#http_application_routing_enabled}.'''
        result = self._values.get("http_application_routing_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def http_proxy_config(self) -> typing.Optional["KubernetesClusterHttpProxyConfig"]:
        '''http_proxy_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#http_proxy_config KubernetesCluster#http_proxy_config}
        '''
        result = self._values.get("http_proxy_config")
        return typing.cast(typing.Optional["KubernetesClusterHttpProxyConfig"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#id KubernetesCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["KubernetesClusterIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#identity KubernetesCluster#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["KubernetesClusterIdentity"], result)

    @builtins.property
    def ingress_application_gateway(
        self,
    ) -> typing.Optional["KubernetesClusterIngressApplicationGateway"]:
        '''ingress_application_gateway block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#ingress_application_gateway KubernetesCluster#ingress_application_gateway}
        '''
        result = self._values.get("ingress_application_gateway")
        return typing.cast(typing.Optional["KubernetesClusterIngressApplicationGateway"], result)

    @builtins.property
    def key_vault_secrets_provider(
        self,
    ) -> typing.Optional["KubernetesClusterKeyVaultSecretsProvider"]:
        '''key_vault_secrets_provider block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#key_vault_secrets_provider KubernetesCluster#key_vault_secrets_provider}
        '''
        result = self._values.get("key_vault_secrets_provider")
        return typing.cast(typing.Optional["KubernetesClusterKeyVaultSecretsProvider"], result)

    @builtins.property
    def kubelet_identity(self) -> typing.Optional["KubernetesClusterKubeletIdentity"]:
        '''kubelet_identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#kubelet_identity KubernetesCluster#kubelet_identity}
        '''
        result = self._values.get("kubelet_identity")
        return typing.cast(typing.Optional["KubernetesClusterKubeletIdentity"], result)

    @builtins.property
    def kubernetes_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#kubernetes_version KubernetesCluster#kubernetes_version}.'''
        result = self._values.get("kubernetes_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def linux_profile(self) -> typing.Optional["KubernetesClusterLinuxProfile"]:
        '''linux_profile block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#linux_profile KubernetesCluster#linux_profile}
        '''
        result = self._values.get("linux_profile")
        return typing.cast(typing.Optional["KubernetesClusterLinuxProfile"], result)

    @builtins.property
    def local_account_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#local_account_disabled KubernetesCluster#local_account_disabled}.'''
        result = self._values.get("local_account_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def maintenance_window(
        self,
    ) -> typing.Optional["KubernetesClusterMaintenanceWindow"]:
        '''maintenance_window block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#maintenance_window KubernetesCluster#maintenance_window}
        '''
        result = self._values.get("maintenance_window")
        return typing.cast(typing.Optional["KubernetesClusterMaintenanceWindow"], result)

    @builtins.property
    def microsoft_defender(
        self,
    ) -> typing.Optional["KubernetesClusterMicrosoftDefender"]:
        '''microsoft_defender block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#microsoft_defender KubernetesCluster#microsoft_defender}
        '''
        result = self._values.get("microsoft_defender")
        return typing.cast(typing.Optional["KubernetesClusterMicrosoftDefender"], result)

    @builtins.property
    def network_profile(self) -> typing.Optional["KubernetesClusterNetworkProfile"]:
        '''network_profile block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#network_profile KubernetesCluster#network_profile}
        '''
        result = self._values.get("network_profile")
        return typing.cast(typing.Optional["KubernetesClusterNetworkProfile"], result)

    @builtins.property
    def node_resource_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#node_resource_group KubernetesCluster#node_resource_group}.'''
        result = self._values.get("node_resource_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oidc_issuer_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#oidc_issuer_enabled KubernetesCluster#oidc_issuer_enabled}.'''
        result = self._values.get("oidc_issuer_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def oms_agent(self) -> typing.Optional["KubernetesClusterOmsAgent"]:
        '''oms_agent block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#oms_agent KubernetesCluster#oms_agent}
        '''
        result = self._values.get("oms_agent")
        return typing.cast(typing.Optional["KubernetesClusterOmsAgent"], result)

    @builtins.property
    def open_service_mesh_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#open_service_mesh_enabled KubernetesCluster#open_service_mesh_enabled}.'''
        result = self._values.get("open_service_mesh_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def private_cluster_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#private_cluster_enabled KubernetesCluster#private_cluster_enabled}.'''
        result = self._values.get("private_cluster_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def private_cluster_public_fqdn_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#private_cluster_public_fqdn_enabled KubernetesCluster#private_cluster_public_fqdn_enabled}.'''
        result = self._values.get("private_cluster_public_fqdn_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def private_dns_zone_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#private_dns_zone_id KubernetesCluster#private_dns_zone_id}.'''
        result = self._values.get("private_dns_zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_network_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#public_network_access_enabled KubernetesCluster#public_network_access_enabled}.'''
        result = self._values.get("public_network_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def role_based_access_control_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#role_based_access_control_enabled KubernetesCluster#role_based_access_control_enabled}.'''
        result = self._values.get("role_based_access_control_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def run_command_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#run_command_enabled KubernetesCluster#run_command_enabled}.'''
        result = self._values.get("run_command_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def service_principal(self) -> typing.Optional["KubernetesClusterServicePrincipal"]:
        '''service_principal block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#service_principal KubernetesCluster#service_principal}
        '''
        result = self._values.get("service_principal")
        return typing.cast(typing.Optional["KubernetesClusterServicePrincipal"], result)

    @builtins.property
    def sku_tier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#sku_tier KubernetesCluster#sku_tier}.'''
        result = self._values.get("sku_tier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#tags KubernetesCluster#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["KubernetesClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#timeouts KubernetesCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["KubernetesClusterTimeouts"], result)

    @builtins.property
    def windows_profile(self) -> typing.Optional["KubernetesClusterWindowsProfile"]:
        '''windows_profile block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#windows_profile KubernetesCluster#windows_profile}
        '''
        result = self._values.get("windows_profile")
        return typing.cast(typing.Optional["KubernetesClusterWindowsProfile"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterDefaultNodePool",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "vm_size": "vmSize",
        "capacity_reservation_group_id": "capacityReservationGroupId",
        "enable_auto_scaling": "enableAutoScaling",
        "enable_host_encryption": "enableHostEncryption",
        "enable_node_public_ip": "enableNodePublicIp",
        "fips_enabled": "fipsEnabled",
        "host_group_id": "hostGroupId",
        "kubelet_config": "kubeletConfig",
        "kubelet_disk_type": "kubeletDiskType",
        "linux_os_config": "linuxOsConfig",
        "max_count": "maxCount",
        "max_pods": "maxPods",
        "message_of_the_day": "messageOfTheDay",
        "min_count": "minCount",
        "node_count": "nodeCount",
        "node_labels": "nodeLabels",
        "node_public_ip_prefix_id": "nodePublicIpPrefixId",
        "node_taints": "nodeTaints",
        "only_critical_addons_enabled": "onlyCriticalAddonsEnabled",
        "orchestrator_version": "orchestratorVersion",
        "os_disk_size_gb": "osDiskSizeGb",
        "os_disk_type": "osDiskType",
        "os_sku": "osSku",
        "pod_subnet_id": "podSubnetId",
        "proximity_placement_group_id": "proximityPlacementGroupId",
        "scale_down_mode": "scaleDownMode",
        "tags": "tags",
        "type": "type",
        "ultra_ssd_enabled": "ultraSsdEnabled",
        "upgrade_settings": "upgradeSettings",
        "vnet_subnet_id": "vnetSubnetId",
        "workload_runtime": "workloadRuntime",
        "zones": "zones",
    },
)
class KubernetesClusterDefaultNodePool:
    def __init__(
        self,
        *,
        name: builtins.str,
        vm_size: builtins.str,
        capacity_reservation_group_id: typing.Optional[builtins.str] = None,
        enable_auto_scaling: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_host_encryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_node_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fips_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        host_group_id: typing.Optional[builtins.str] = None,
        kubelet_config: typing.Optional[typing.Union["KubernetesClusterDefaultNodePoolKubeletConfig", typing.Dict[str, typing.Any]]] = None,
        kubelet_disk_type: typing.Optional[builtins.str] = None,
        linux_os_config: typing.Optional[typing.Union["KubernetesClusterDefaultNodePoolLinuxOsConfig", typing.Dict[str, typing.Any]]] = None,
        max_count: typing.Optional[jsii.Number] = None,
        max_pods: typing.Optional[jsii.Number] = None,
        message_of_the_day: typing.Optional[builtins.str] = None,
        min_count: typing.Optional[jsii.Number] = None,
        node_count: typing.Optional[jsii.Number] = None,
        node_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        node_public_ip_prefix_id: typing.Optional[builtins.str] = None,
        node_taints: typing.Optional[typing.Sequence[builtins.str]] = None,
        only_critical_addons_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        orchestrator_version: typing.Optional[builtins.str] = None,
        os_disk_size_gb: typing.Optional[jsii.Number] = None,
        os_disk_type: typing.Optional[builtins.str] = None,
        os_sku: typing.Optional[builtins.str] = None,
        pod_subnet_id: typing.Optional[builtins.str] = None,
        proximity_placement_group_id: typing.Optional[builtins.str] = None,
        scale_down_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
        ultra_ssd_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        upgrade_settings: typing.Optional[typing.Union["KubernetesClusterDefaultNodePoolUpgradeSettings", typing.Dict[str, typing.Any]]] = None,
        vnet_subnet_id: typing.Optional[builtins.str] = None,
        workload_runtime: typing.Optional[builtins.str] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#name KubernetesCluster#name}.
        :param vm_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#vm_size KubernetesCluster#vm_size}.
        :param capacity_reservation_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#capacity_reservation_group_id KubernetesCluster#capacity_reservation_group_id}.
        :param enable_auto_scaling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#enable_auto_scaling KubernetesCluster#enable_auto_scaling}.
        :param enable_host_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#enable_host_encryption KubernetesCluster#enable_host_encryption}.
        :param enable_node_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#enable_node_public_ip KubernetesCluster#enable_node_public_ip}.
        :param fips_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#fips_enabled KubernetesCluster#fips_enabled}.
        :param host_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#host_group_id KubernetesCluster#host_group_id}.
        :param kubelet_config: kubelet_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#kubelet_config KubernetesCluster#kubelet_config}
        :param kubelet_disk_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#kubelet_disk_type KubernetesCluster#kubelet_disk_type}.
        :param linux_os_config: linux_os_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#linux_os_config KubernetesCluster#linux_os_config}
        :param max_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_count KubernetesCluster#max_count}.
        :param max_pods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_pods KubernetesCluster#max_pods}.
        :param message_of_the_day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#message_of_the_day KubernetesCluster#message_of_the_day}.
        :param min_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#min_count KubernetesCluster#min_count}.
        :param node_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#node_count KubernetesCluster#node_count}.
        :param node_labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#node_labels KubernetesCluster#node_labels}.
        :param node_public_ip_prefix_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#node_public_ip_prefix_id KubernetesCluster#node_public_ip_prefix_id}.
        :param node_taints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#node_taints KubernetesCluster#node_taints}.
        :param only_critical_addons_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#only_critical_addons_enabled KubernetesCluster#only_critical_addons_enabled}.
        :param orchestrator_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#orchestrator_version KubernetesCluster#orchestrator_version}.
        :param os_disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#os_disk_size_gb KubernetesCluster#os_disk_size_gb}.
        :param os_disk_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#os_disk_type KubernetesCluster#os_disk_type}.
        :param os_sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#os_sku KubernetesCluster#os_sku}.
        :param pod_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#pod_subnet_id KubernetesCluster#pod_subnet_id}.
        :param proximity_placement_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#proximity_placement_group_id KubernetesCluster#proximity_placement_group_id}.
        :param scale_down_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_mode KubernetesCluster#scale_down_mode}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#tags KubernetesCluster#tags}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#type KubernetesCluster#type}.
        :param ultra_ssd_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#ultra_ssd_enabled KubernetesCluster#ultra_ssd_enabled}.
        :param upgrade_settings: upgrade_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#upgrade_settings KubernetesCluster#upgrade_settings}
        :param vnet_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#vnet_subnet_id KubernetesCluster#vnet_subnet_id}.
        :param workload_runtime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#workload_runtime KubernetesCluster#workload_runtime}.
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#zones KubernetesCluster#zones}.
        '''
        if isinstance(kubelet_config, dict):
            kubelet_config = KubernetesClusterDefaultNodePoolKubeletConfig(**kubelet_config)
        if isinstance(linux_os_config, dict):
            linux_os_config = KubernetesClusterDefaultNodePoolLinuxOsConfig(**linux_os_config)
        if isinstance(upgrade_settings, dict):
            upgrade_settings = KubernetesClusterDefaultNodePoolUpgradeSettings(**upgrade_settings)
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterDefaultNodePool.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument vm_size", value=vm_size, expected_type=type_hints["vm_size"])
            check_type(argname="argument capacity_reservation_group_id", value=capacity_reservation_group_id, expected_type=type_hints["capacity_reservation_group_id"])
            check_type(argname="argument enable_auto_scaling", value=enable_auto_scaling, expected_type=type_hints["enable_auto_scaling"])
            check_type(argname="argument enable_host_encryption", value=enable_host_encryption, expected_type=type_hints["enable_host_encryption"])
            check_type(argname="argument enable_node_public_ip", value=enable_node_public_ip, expected_type=type_hints["enable_node_public_ip"])
            check_type(argname="argument fips_enabled", value=fips_enabled, expected_type=type_hints["fips_enabled"])
            check_type(argname="argument host_group_id", value=host_group_id, expected_type=type_hints["host_group_id"])
            check_type(argname="argument kubelet_config", value=kubelet_config, expected_type=type_hints["kubelet_config"])
            check_type(argname="argument kubelet_disk_type", value=kubelet_disk_type, expected_type=type_hints["kubelet_disk_type"])
            check_type(argname="argument linux_os_config", value=linux_os_config, expected_type=type_hints["linux_os_config"])
            check_type(argname="argument max_count", value=max_count, expected_type=type_hints["max_count"])
            check_type(argname="argument max_pods", value=max_pods, expected_type=type_hints["max_pods"])
            check_type(argname="argument message_of_the_day", value=message_of_the_day, expected_type=type_hints["message_of_the_day"])
            check_type(argname="argument min_count", value=min_count, expected_type=type_hints["min_count"])
            check_type(argname="argument node_count", value=node_count, expected_type=type_hints["node_count"])
            check_type(argname="argument node_labels", value=node_labels, expected_type=type_hints["node_labels"])
            check_type(argname="argument node_public_ip_prefix_id", value=node_public_ip_prefix_id, expected_type=type_hints["node_public_ip_prefix_id"])
            check_type(argname="argument node_taints", value=node_taints, expected_type=type_hints["node_taints"])
            check_type(argname="argument only_critical_addons_enabled", value=only_critical_addons_enabled, expected_type=type_hints["only_critical_addons_enabled"])
            check_type(argname="argument orchestrator_version", value=orchestrator_version, expected_type=type_hints["orchestrator_version"])
            check_type(argname="argument os_disk_size_gb", value=os_disk_size_gb, expected_type=type_hints["os_disk_size_gb"])
            check_type(argname="argument os_disk_type", value=os_disk_type, expected_type=type_hints["os_disk_type"])
            check_type(argname="argument os_sku", value=os_sku, expected_type=type_hints["os_sku"])
            check_type(argname="argument pod_subnet_id", value=pod_subnet_id, expected_type=type_hints["pod_subnet_id"])
            check_type(argname="argument proximity_placement_group_id", value=proximity_placement_group_id, expected_type=type_hints["proximity_placement_group_id"])
            check_type(argname="argument scale_down_mode", value=scale_down_mode, expected_type=type_hints["scale_down_mode"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument ultra_ssd_enabled", value=ultra_ssd_enabled, expected_type=type_hints["ultra_ssd_enabled"])
            check_type(argname="argument upgrade_settings", value=upgrade_settings, expected_type=type_hints["upgrade_settings"])
            check_type(argname="argument vnet_subnet_id", value=vnet_subnet_id, expected_type=type_hints["vnet_subnet_id"])
            check_type(argname="argument workload_runtime", value=workload_runtime, expected_type=type_hints["workload_runtime"])
            check_type(argname="argument zones", value=zones, expected_type=type_hints["zones"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "vm_size": vm_size,
        }
        if capacity_reservation_group_id is not None:
            self._values["capacity_reservation_group_id"] = capacity_reservation_group_id
        if enable_auto_scaling is not None:
            self._values["enable_auto_scaling"] = enable_auto_scaling
        if enable_host_encryption is not None:
            self._values["enable_host_encryption"] = enable_host_encryption
        if enable_node_public_ip is not None:
            self._values["enable_node_public_ip"] = enable_node_public_ip
        if fips_enabled is not None:
            self._values["fips_enabled"] = fips_enabled
        if host_group_id is not None:
            self._values["host_group_id"] = host_group_id
        if kubelet_config is not None:
            self._values["kubelet_config"] = kubelet_config
        if kubelet_disk_type is not None:
            self._values["kubelet_disk_type"] = kubelet_disk_type
        if linux_os_config is not None:
            self._values["linux_os_config"] = linux_os_config
        if max_count is not None:
            self._values["max_count"] = max_count
        if max_pods is not None:
            self._values["max_pods"] = max_pods
        if message_of_the_day is not None:
            self._values["message_of_the_day"] = message_of_the_day
        if min_count is not None:
            self._values["min_count"] = min_count
        if node_count is not None:
            self._values["node_count"] = node_count
        if node_labels is not None:
            self._values["node_labels"] = node_labels
        if node_public_ip_prefix_id is not None:
            self._values["node_public_ip_prefix_id"] = node_public_ip_prefix_id
        if node_taints is not None:
            self._values["node_taints"] = node_taints
        if only_critical_addons_enabled is not None:
            self._values["only_critical_addons_enabled"] = only_critical_addons_enabled
        if orchestrator_version is not None:
            self._values["orchestrator_version"] = orchestrator_version
        if os_disk_size_gb is not None:
            self._values["os_disk_size_gb"] = os_disk_size_gb
        if os_disk_type is not None:
            self._values["os_disk_type"] = os_disk_type
        if os_sku is not None:
            self._values["os_sku"] = os_sku
        if pod_subnet_id is not None:
            self._values["pod_subnet_id"] = pod_subnet_id
        if proximity_placement_group_id is not None:
            self._values["proximity_placement_group_id"] = proximity_placement_group_id
        if scale_down_mode is not None:
            self._values["scale_down_mode"] = scale_down_mode
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type
        if ultra_ssd_enabled is not None:
            self._values["ultra_ssd_enabled"] = ultra_ssd_enabled
        if upgrade_settings is not None:
            self._values["upgrade_settings"] = upgrade_settings
        if vnet_subnet_id is not None:
            self._values["vnet_subnet_id"] = vnet_subnet_id
        if workload_runtime is not None:
            self._values["workload_runtime"] = workload_runtime
        if zones is not None:
            self._values["zones"] = zones

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#name KubernetesCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vm_size(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#vm_size KubernetesCluster#vm_size}.'''
        result = self._values.get("vm_size")
        assert result is not None, "Required property 'vm_size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity_reservation_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#capacity_reservation_group_id KubernetesCluster#capacity_reservation_group_id}.'''
        result = self._values.get("capacity_reservation_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_auto_scaling(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#enable_auto_scaling KubernetesCluster#enable_auto_scaling}.'''
        result = self._values.get("enable_auto_scaling")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_host_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#enable_host_encryption KubernetesCluster#enable_host_encryption}.'''
        result = self._values.get("enable_host_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_node_public_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#enable_node_public_ip KubernetesCluster#enable_node_public_ip}.'''
        result = self._values.get("enable_node_public_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def fips_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#fips_enabled KubernetesCluster#fips_enabled}.'''
        result = self._values.get("fips_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def host_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#host_group_id KubernetesCluster#host_group_id}.'''
        result = self._values.get("host_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kubelet_config(
        self,
    ) -> typing.Optional["KubernetesClusterDefaultNodePoolKubeletConfig"]:
        '''kubelet_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#kubelet_config KubernetesCluster#kubelet_config}
        '''
        result = self._values.get("kubelet_config")
        return typing.cast(typing.Optional["KubernetesClusterDefaultNodePoolKubeletConfig"], result)

    @builtins.property
    def kubelet_disk_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#kubelet_disk_type KubernetesCluster#kubelet_disk_type}.'''
        result = self._values.get("kubelet_disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def linux_os_config(
        self,
    ) -> typing.Optional["KubernetesClusterDefaultNodePoolLinuxOsConfig"]:
        '''linux_os_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#linux_os_config KubernetesCluster#linux_os_config}
        '''
        result = self._values.get("linux_os_config")
        return typing.cast(typing.Optional["KubernetesClusterDefaultNodePoolLinuxOsConfig"], result)

    @builtins.property
    def max_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_count KubernetesCluster#max_count}.'''
        result = self._values.get("max_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_pods(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_pods KubernetesCluster#max_pods}.'''
        result = self._values.get("max_pods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def message_of_the_day(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#message_of_the_day KubernetesCluster#message_of_the_day}.'''
        result = self._values.get("message_of_the_day")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#min_count KubernetesCluster#min_count}.'''
        result = self._values.get("min_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def node_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#node_count KubernetesCluster#node_count}.'''
        result = self._values.get("node_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def node_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#node_labels KubernetesCluster#node_labels}.'''
        result = self._values.get("node_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def node_public_ip_prefix_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#node_public_ip_prefix_id KubernetesCluster#node_public_ip_prefix_id}.'''
        result = self._values.get("node_public_ip_prefix_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_taints(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#node_taints KubernetesCluster#node_taints}.'''
        result = self._values.get("node_taints")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def only_critical_addons_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#only_critical_addons_enabled KubernetesCluster#only_critical_addons_enabled}.'''
        result = self._values.get("only_critical_addons_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def orchestrator_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#orchestrator_version KubernetesCluster#orchestrator_version}.'''
        result = self._values.get("orchestrator_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def os_disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#os_disk_size_gb KubernetesCluster#os_disk_size_gb}.'''
        result = self._values.get("os_disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def os_disk_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#os_disk_type KubernetesCluster#os_disk_type}.'''
        result = self._values.get("os_disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def os_sku(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#os_sku KubernetesCluster#os_sku}.'''
        result = self._values.get("os_sku")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pod_subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#pod_subnet_id KubernetesCluster#pod_subnet_id}.'''
        result = self._values.get("pod_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proximity_placement_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#proximity_placement_group_id KubernetesCluster#proximity_placement_group_id}.'''
        result = self._values.get("proximity_placement_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_down_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#scale_down_mode KubernetesCluster#scale_down_mode}.'''
        result = self._values.get("scale_down_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#tags KubernetesCluster#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#type KubernetesCluster#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ultra_ssd_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#ultra_ssd_enabled KubernetesCluster#ultra_ssd_enabled}.'''
        result = self._values.get("ultra_ssd_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def upgrade_settings(
        self,
    ) -> typing.Optional["KubernetesClusterDefaultNodePoolUpgradeSettings"]:
        '''upgrade_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#upgrade_settings KubernetesCluster#upgrade_settings}
        '''
        result = self._values.get("upgrade_settings")
        return typing.cast(typing.Optional["KubernetesClusterDefaultNodePoolUpgradeSettings"], result)

    @builtins.property
    def vnet_subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#vnet_subnet_id KubernetesCluster#vnet_subnet_id}.'''
        result = self._values.get("vnet_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workload_runtime(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#workload_runtime KubernetesCluster#workload_runtime}.'''
        result = self._values.get("workload_runtime")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#zones KubernetesCluster#zones}.'''
        result = self._values.get("zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterDefaultNodePool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterDefaultNodePoolKubeletConfig",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_unsafe_sysctls": "allowedUnsafeSysctls",
        "container_log_max_line": "containerLogMaxLine",
        "container_log_max_size_mb": "containerLogMaxSizeMb",
        "cpu_cfs_quota_enabled": "cpuCfsQuotaEnabled",
        "cpu_cfs_quota_period": "cpuCfsQuotaPeriod",
        "cpu_manager_policy": "cpuManagerPolicy",
        "image_gc_high_threshold": "imageGcHighThreshold",
        "image_gc_low_threshold": "imageGcLowThreshold",
        "pod_max_pid": "podMaxPid",
        "topology_manager_policy": "topologyManagerPolicy",
    },
)
class KubernetesClusterDefaultNodePoolKubeletConfig:
    def __init__(
        self,
        *,
        allowed_unsafe_sysctls: typing.Optional[typing.Sequence[builtins.str]] = None,
        container_log_max_line: typing.Optional[jsii.Number] = None,
        container_log_max_size_mb: typing.Optional[jsii.Number] = None,
        cpu_cfs_quota_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cpu_cfs_quota_period: typing.Optional[builtins.str] = None,
        cpu_manager_policy: typing.Optional[builtins.str] = None,
        image_gc_high_threshold: typing.Optional[jsii.Number] = None,
        image_gc_low_threshold: typing.Optional[jsii.Number] = None,
        pod_max_pid: typing.Optional[jsii.Number] = None,
        topology_manager_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_unsafe_sysctls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#allowed_unsafe_sysctls KubernetesCluster#allowed_unsafe_sysctls}.
        :param container_log_max_line: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#container_log_max_line KubernetesCluster#container_log_max_line}.
        :param container_log_max_size_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#container_log_max_size_mb KubernetesCluster#container_log_max_size_mb}.
        :param cpu_cfs_quota_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#cpu_cfs_quota_enabled KubernetesCluster#cpu_cfs_quota_enabled}.
        :param cpu_cfs_quota_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#cpu_cfs_quota_period KubernetesCluster#cpu_cfs_quota_period}.
        :param cpu_manager_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#cpu_manager_policy KubernetesCluster#cpu_manager_policy}.
        :param image_gc_high_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#image_gc_high_threshold KubernetesCluster#image_gc_high_threshold}.
        :param image_gc_low_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#image_gc_low_threshold KubernetesCluster#image_gc_low_threshold}.
        :param pod_max_pid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#pod_max_pid KubernetesCluster#pod_max_pid}.
        :param topology_manager_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#topology_manager_policy KubernetesCluster#topology_manager_policy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterDefaultNodePoolKubeletConfig.__init__)
            check_type(argname="argument allowed_unsafe_sysctls", value=allowed_unsafe_sysctls, expected_type=type_hints["allowed_unsafe_sysctls"])
            check_type(argname="argument container_log_max_line", value=container_log_max_line, expected_type=type_hints["container_log_max_line"])
            check_type(argname="argument container_log_max_size_mb", value=container_log_max_size_mb, expected_type=type_hints["container_log_max_size_mb"])
            check_type(argname="argument cpu_cfs_quota_enabled", value=cpu_cfs_quota_enabled, expected_type=type_hints["cpu_cfs_quota_enabled"])
            check_type(argname="argument cpu_cfs_quota_period", value=cpu_cfs_quota_period, expected_type=type_hints["cpu_cfs_quota_period"])
            check_type(argname="argument cpu_manager_policy", value=cpu_manager_policy, expected_type=type_hints["cpu_manager_policy"])
            check_type(argname="argument image_gc_high_threshold", value=image_gc_high_threshold, expected_type=type_hints["image_gc_high_threshold"])
            check_type(argname="argument image_gc_low_threshold", value=image_gc_low_threshold, expected_type=type_hints["image_gc_low_threshold"])
            check_type(argname="argument pod_max_pid", value=pod_max_pid, expected_type=type_hints["pod_max_pid"])
            check_type(argname="argument topology_manager_policy", value=topology_manager_policy, expected_type=type_hints["topology_manager_policy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_unsafe_sysctls is not None:
            self._values["allowed_unsafe_sysctls"] = allowed_unsafe_sysctls
        if container_log_max_line is not None:
            self._values["container_log_max_line"] = container_log_max_line
        if container_log_max_size_mb is not None:
            self._values["container_log_max_size_mb"] = container_log_max_size_mb
        if cpu_cfs_quota_enabled is not None:
            self._values["cpu_cfs_quota_enabled"] = cpu_cfs_quota_enabled
        if cpu_cfs_quota_period is not None:
            self._values["cpu_cfs_quota_period"] = cpu_cfs_quota_period
        if cpu_manager_policy is not None:
            self._values["cpu_manager_policy"] = cpu_manager_policy
        if image_gc_high_threshold is not None:
            self._values["image_gc_high_threshold"] = image_gc_high_threshold
        if image_gc_low_threshold is not None:
            self._values["image_gc_low_threshold"] = image_gc_low_threshold
        if pod_max_pid is not None:
            self._values["pod_max_pid"] = pod_max_pid
        if topology_manager_policy is not None:
            self._values["topology_manager_policy"] = topology_manager_policy

    @builtins.property
    def allowed_unsafe_sysctls(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#allowed_unsafe_sysctls KubernetesCluster#allowed_unsafe_sysctls}.'''
        result = self._values.get("allowed_unsafe_sysctls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def container_log_max_line(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#container_log_max_line KubernetesCluster#container_log_max_line}.'''
        result = self._values.get("container_log_max_line")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def container_log_max_size_mb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#container_log_max_size_mb KubernetesCluster#container_log_max_size_mb}.'''
        result = self._values.get("container_log_max_size_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cpu_cfs_quota_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#cpu_cfs_quota_enabled KubernetesCluster#cpu_cfs_quota_enabled}.'''
        result = self._values.get("cpu_cfs_quota_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cpu_cfs_quota_period(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#cpu_cfs_quota_period KubernetesCluster#cpu_cfs_quota_period}.'''
        result = self._values.get("cpu_cfs_quota_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cpu_manager_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#cpu_manager_policy KubernetesCluster#cpu_manager_policy}.'''
        result = self._values.get("cpu_manager_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_gc_high_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#image_gc_high_threshold KubernetesCluster#image_gc_high_threshold}.'''
        result = self._values.get("image_gc_high_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def image_gc_low_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#image_gc_low_threshold KubernetesCluster#image_gc_low_threshold}.'''
        result = self._values.get("image_gc_low_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pod_max_pid(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#pod_max_pid KubernetesCluster#pod_max_pid}.'''
        result = self._values.get("pod_max_pid")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def topology_manager_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#topology_manager_policy KubernetesCluster#topology_manager_policy}.'''
        result = self._values.get("topology_manager_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterDefaultNodePoolKubeletConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterDefaultNodePoolKubeletConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterDefaultNodePoolKubeletConfigOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterDefaultNodePoolKubeletConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedUnsafeSysctls")
    def reset_allowed_unsafe_sysctls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedUnsafeSysctls", []))

    @jsii.member(jsii_name="resetContainerLogMaxLine")
    def reset_container_log_max_line(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerLogMaxLine", []))

    @jsii.member(jsii_name="resetContainerLogMaxSizeMb")
    def reset_container_log_max_size_mb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerLogMaxSizeMb", []))

    @jsii.member(jsii_name="resetCpuCfsQuotaEnabled")
    def reset_cpu_cfs_quota_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuCfsQuotaEnabled", []))

    @jsii.member(jsii_name="resetCpuCfsQuotaPeriod")
    def reset_cpu_cfs_quota_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuCfsQuotaPeriod", []))

    @jsii.member(jsii_name="resetCpuManagerPolicy")
    def reset_cpu_manager_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuManagerPolicy", []))

    @jsii.member(jsii_name="resetImageGcHighThreshold")
    def reset_image_gc_high_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageGcHighThreshold", []))

    @jsii.member(jsii_name="resetImageGcLowThreshold")
    def reset_image_gc_low_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageGcLowThreshold", []))

    @jsii.member(jsii_name="resetPodMaxPid")
    def reset_pod_max_pid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPodMaxPid", []))

    @jsii.member(jsii_name="resetTopologyManagerPolicy")
    def reset_topology_manager_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTopologyManagerPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="allowedUnsafeSysctlsInput")
    def allowed_unsafe_sysctls_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedUnsafeSysctlsInput"))

    @builtins.property
    @jsii.member(jsii_name="containerLogMaxLineInput")
    def container_log_max_line_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "containerLogMaxLineInput"))

    @builtins.property
    @jsii.member(jsii_name="containerLogMaxSizeMbInput")
    def container_log_max_size_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "containerLogMaxSizeMbInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuCfsQuotaEnabledInput")
    def cpu_cfs_quota_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cpuCfsQuotaEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuCfsQuotaPeriodInput")
    def cpu_cfs_quota_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuCfsQuotaPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuManagerPolicyInput")
    def cpu_manager_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuManagerPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="imageGcHighThresholdInput")
    def image_gc_high_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "imageGcHighThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="imageGcLowThresholdInput")
    def image_gc_low_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "imageGcLowThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="podMaxPidInput")
    def pod_max_pid_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "podMaxPidInput"))

    @builtins.property
    @jsii.member(jsii_name="topologyManagerPolicyInput")
    def topology_manager_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topologyManagerPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedUnsafeSysctls")
    def allowed_unsafe_sysctls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedUnsafeSysctls"))

    @allowed_unsafe_sysctls.setter
    def allowed_unsafe_sysctls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolKubeletConfigOutputReference, "allowed_unsafe_sysctls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedUnsafeSysctls", value)

    @builtins.property
    @jsii.member(jsii_name="containerLogMaxLine")
    def container_log_max_line(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerLogMaxLine"))

    @container_log_max_line.setter
    def container_log_max_line(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolKubeletConfigOutputReference, "container_log_max_line").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerLogMaxLine", value)

    @builtins.property
    @jsii.member(jsii_name="containerLogMaxSizeMb")
    def container_log_max_size_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerLogMaxSizeMb"))

    @container_log_max_size_mb.setter
    def container_log_max_size_mb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolKubeletConfigOutputReference, "container_log_max_size_mb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerLogMaxSizeMb", value)

    @builtins.property
    @jsii.member(jsii_name="cpuCfsQuotaEnabled")
    def cpu_cfs_quota_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cpuCfsQuotaEnabled"))

    @cpu_cfs_quota_enabled.setter
    def cpu_cfs_quota_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolKubeletConfigOutputReference, "cpu_cfs_quota_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuCfsQuotaEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="cpuCfsQuotaPeriod")
    def cpu_cfs_quota_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpuCfsQuotaPeriod"))

    @cpu_cfs_quota_period.setter
    def cpu_cfs_quota_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolKubeletConfigOutputReference, "cpu_cfs_quota_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuCfsQuotaPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="cpuManagerPolicy")
    def cpu_manager_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpuManagerPolicy"))

    @cpu_manager_policy.setter
    def cpu_manager_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolKubeletConfigOutputReference, "cpu_manager_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuManagerPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="imageGcHighThreshold")
    def image_gc_high_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "imageGcHighThreshold"))

    @image_gc_high_threshold.setter
    def image_gc_high_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolKubeletConfigOutputReference, "image_gc_high_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageGcHighThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="imageGcLowThreshold")
    def image_gc_low_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "imageGcLowThreshold"))

    @image_gc_low_threshold.setter
    def image_gc_low_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolKubeletConfigOutputReference, "image_gc_low_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageGcLowThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="podMaxPid")
    def pod_max_pid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "podMaxPid"))

    @pod_max_pid.setter
    def pod_max_pid(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolKubeletConfigOutputReference, "pod_max_pid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "podMaxPid", value)

    @builtins.property
    @jsii.member(jsii_name="topologyManagerPolicy")
    def topology_manager_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topologyManagerPolicy"))

    @topology_manager_policy.setter
    def topology_manager_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolKubeletConfigOutputReference, "topology_manager_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topologyManagerPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KubernetesClusterDefaultNodePoolKubeletConfig]:
        return typing.cast(typing.Optional[KubernetesClusterDefaultNodePoolKubeletConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterDefaultNodePoolKubeletConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolKubeletConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterDefaultNodePoolLinuxOsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "swap_file_size_mb": "swapFileSizeMb",
        "sysctl_config": "sysctlConfig",
        "transparent_huge_page_defrag": "transparentHugePageDefrag",
        "transparent_huge_page_enabled": "transparentHugePageEnabled",
    },
)
class KubernetesClusterDefaultNodePoolLinuxOsConfig:
    def __init__(
        self,
        *,
        swap_file_size_mb: typing.Optional[jsii.Number] = None,
        sysctl_config: typing.Optional[typing.Union["KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfig", typing.Dict[str, typing.Any]]] = None,
        transparent_huge_page_defrag: typing.Optional[builtins.str] = None,
        transparent_huge_page_enabled: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param swap_file_size_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#swap_file_size_mb KubernetesCluster#swap_file_size_mb}.
        :param sysctl_config: sysctl_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#sysctl_config KubernetesCluster#sysctl_config}
        :param transparent_huge_page_defrag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#transparent_huge_page_defrag KubernetesCluster#transparent_huge_page_defrag}.
        :param transparent_huge_page_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#transparent_huge_page_enabled KubernetesCluster#transparent_huge_page_enabled}.
        '''
        if isinstance(sysctl_config, dict):
            sysctl_config = KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfig(**sysctl_config)
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterDefaultNodePoolLinuxOsConfig.__init__)
            check_type(argname="argument swap_file_size_mb", value=swap_file_size_mb, expected_type=type_hints["swap_file_size_mb"])
            check_type(argname="argument sysctl_config", value=sysctl_config, expected_type=type_hints["sysctl_config"])
            check_type(argname="argument transparent_huge_page_defrag", value=transparent_huge_page_defrag, expected_type=type_hints["transparent_huge_page_defrag"])
            check_type(argname="argument transparent_huge_page_enabled", value=transparent_huge_page_enabled, expected_type=type_hints["transparent_huge_page_enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if swap_file_size_mb is not None:
            self._values["swap_file_size_mb"] = swap_file_size_mb
        if sysctl_config is not None:
            self._values["sysctl_config"] = sysctl_config
        if transparent_huge_page_defrag is not None:
            self._values["transparent_huge_page_defrag"] = transparent_huge_page_defrag
        if transparent_huge_page_enabled is not None:
            self._values["transparent_huge_page_enabled"] = transparent_huge_page_enabled

    @builtins.property
    def swap_file_size_mb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#swap_file_size_mb KubernetesCluster#swap_file_size_mb}.'''
        result = self._values.get("swap_file_size_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sysctl_config(
        self,
    ) -> typing.Optional["KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfig"]:
        '''sysctl_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#sysctl_config KubernetesCluster#sysctl_config}
        '''
        result = self._values.get("sysctl_config")
        return typing.cast(typing.Optional["KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfig"], result)

    @builtins.property
    def transparent_huge_page_defrag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#transparent_huge_page_defrag KubernetesCluster#transparent_huge_page_defrag}.'''
        result = self._values.get("transparent_huge_page_defrag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transparent_huge_page_enabled(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#transparent_huge_page_enabled KubernetesCluster#transparent_huge_page_enabled}.'''
        result = self._values.get("transparent_huge_page_enabled")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterDefaultNodePoolLinuxOsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterDefaultNodePoolLinuxOsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterDefaultNodePoolLinuxOsConfigOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterDefaultNodePoolLinuxOsConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSysctlConfig")
    def put_sysctl_config(
        self,
        *,
        fs_aio_max_nr: typing.Optional[jsii.Number] = None,
        fs_file_max: typing.Optional[jsii.Number] = None,
        fs_inotify_max_user_watches: typing.Optional[jsii.Number] = None,
        fs_nr_open: typing.Optional[jsii.Number] = None,
        kernel_threads_max: typing.Optional[jsii.Number] = None,
        net_core_netdev_max_backlog: typing.Optional[jsii.Number] = None,
        net_core_optmem_max: typing.Optional[jsii.Number] = None,
        net_core_rmem_default: typing.Optional[jsii.Number] = None,
        net_core_rmem_max: typing.Optional[jsii.Number] = None,
        net_core_somaxconn: typing.Optional[jsii.Number] = None,
        net_core_wmem_default: typing.Optional[jsii.Number] = None,
        net_core_wmem_max: typing.Optional[jsii.Number] = None,
        net_ipv4_ip_local_port_range_max: typing.Optional[jsii.Number] = None,
        net_ipv4_ip_local_port_range_min: typing.Optional[jsii.Number] = None,
        net_ipv4_neigh_default_gc_thresh1: typing.Optional[jsii.Number] = None,
        net_ipv4_neigh_default_gc_thresh2: typing.Optional[jsii.Number] = None,
        net_ipv4_neigh_default_gc_thresh3: typing.Optional[jsii.Number] = None,
        net_ipv4_tcp_fin_timeout: typing.Optional[jsii.Number] = None,
        net_ipv4_tcp_keepalive_intvl: typing.Optional[jsii.Number] = None,
        net_ipv4_tcp_keepalive_probes: typing.Optional[jsii.Number] = None,
        net_ipv4_tcp_keepalive_time: typing.Optional[jsii.Number] = None,
        net_ipv4_tcp_max_syn_backlog: typing.Optional[jsii.Number] = None,
        net_ipv4_tcp_max_tw_buckets: typing.Optional[jsii.Number] = None,
        net_ipv4_tcp_tw_reuse: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        net_netfilter_nf_conntrack_buckets: typing.Optional[jsii.Number] = None,
        net_netfilter_nf_conntrack_max: typing.Optional[jsii.Number] = None,
        vm_max_map_count: typing.Optional[jsii.Number] = None,
        vm_swappiness: typing.Optional[jsii.Number] = None,
        vm_vfs_cache_pressure: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fs_aio_max_nr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#fs_aio_max_nr KubernetesCluster#fs_aio_max_nr}.
        :param fs_file_max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#fs_file_max KubernetesCluster#fs_file_max}.
        :param fs_inotify_max_user_watches: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#fs_inotify_max_user_watches KubernetesCluster#fs_inotify_max_user_watches}.
        :param fs_nr_open: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#fs_nr_open KubernetesCluster#fs_nr_open}.
        :param kernel_threads_max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#kernel_threads_max KubernetesCluster#kernel_threads_max}.
        :param net_core_netdev_max_backlog: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_netdev_max_backlog KubernetesCluster#net_core_netdev_max_backlog}.
        :param net_core_optmem_max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_optmem_max KubernetesCluster#net_core_optmem_max}.
        :param net_core_rmem_default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_rmem_default KubernetesCluster#net_core_rmem_default}.
        :param net_core_rmem_max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_rmem_max KubernetesCluster#net_core_rmem_max}.
        :param net_core_somaxconn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_somaxconn KubernetesCluster#net_core_somaxconn}.
        :param net_core_wmem_default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_wmem_default KubernetesCluster#net_core_wmem_default}.
        :param net_core_wmem_max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_wmem_max KubernetesCluster#net_core_wmem_max}.
        :param net_ipv4_ip_local_port_range_max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_ip_local_port_range_max KubernetesCluster#net_ipv4_ip_local_port_range_max}.
        :param net_ipv4_ip_local_port_range_min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_ip_local_port_range_min KubernetesCluster#net_ipv4_ip_local_port_range_min}.
        :param net_ipv4_neigh_default_gc_thresh1: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_neigh_default_gc_thresh1 KubernetesCluster#net_ipv4_neigh_default_gc_thresh1}.
        :param net_ipv4_neigh_default_gc_thresh2: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_neigh_default_gc_thresh2 KubernetesCluster#net_ipv4_neigh_default_gc_thresh2}.
        :param net_ipv4_neigh_default_gc_thresh3: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_neigh_default_gc_thresh3 KubernetesCluster#net_ipv4_neigh_default_gc_thresh3}.
        :param net_ipv4_tcp_fin_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_fin_timeout KubernetesCluster#net_ipv4_tcp_fin_timeout}.
        :param net_ipv4_tcp_keepalive_intvl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_keepalive_intvl KubernetesCluster#net_ipv4_tcp_keepalive_intvl}.
        :param net_ipv4_tcp_keepalive_probes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_keepalive_probes KubernetesCluster#net_ipv4_tcp_keepalive_probes}.
        :param net_ipv4_tcp_keepalive_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_keepalive_time KubernetesCluster#net_ipv4_tcp_keepalive_time}.
        :param net_ipv4_tcp_max_syn_backlog: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_max_syn_backlog KubernetesCluster#net_ipv4_tcp_max_syn_backlog}.
        :param net_ipv4_tcp_max_tw_buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_max_tw_buckets KubernetesCluster#net_ipv4_tcp_max_tw_buckets}.
        :param net_ipv4_tcp_tw_reuse: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_tw_reuse KubernetesCluster#net_ipv4_tcp_tw_reuse}.
        :param net_netfilter_nf_conntrack_buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_netfilter_nf_conntrack_buckets KubernetesCluster#net_netfilter_nf_conntrack_buckets}.
        :param net_netfilter_nf_conntrack_max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_netfilter_nf_conntrack_max KubernetesCluster#net_netfilter_nf_conntrack_max}.
        :param vm_max_map_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#vm_max_map_count KubernetesCluster#vm_max_map_count}.
        :param vm_swappiness: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#vm_swappiness KubernetesCluster#vm_swappiness}.
        :param vm_vfs_cache_pressure: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#vm_vfs_cache_pressure KubernetesCluster#vm_vfs_cache_pressure}.
        '''
        value = KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfig(
            fs_aio_max_nr=fs_aio_max_nr,
            fs_file_max=fs_file_max,
            fs_inotify_max_user_watches=fs_inotify_max_user_watches,
            fs_nr_open=fs_nr_open,
            kernel_threads_max=kernel_threads_max,
            net_core_netdev_max_backlog=net_core_netdev_max_backlog,
            net_core_optmem_max=net_core_optmem_max,
            net_core_rmem_default=net_core_rmem_default,
            net_core_rmem_max=net_core_rmem_max,
            net_core_somaxconn=net_core_somaxconn,
            net_core_wmem_default=net_core_wmem_default,
            net_core_wmem_max=net_core_wmem_max,
            net_ipv4_ip_local_port_range_max=net_ipv4_ip_local_port_range_max,
            net_ipv4_ip_local_port_range_min=net_ipv4_ip_local_port_range_min,
            net_ipv4_neigh_default_gc_thresh1=net_ipv4_neigh_default_gc_thresh1,
            net_ipv4_neigh_default_gc_thresh2=net_ipv4_neigh_default_gc_thresh2,
            net_ipv4_neigh_default_gc_thresh3=net_ipv4_neigh_default_gc_thresh3,
            net_ipv4_tcp_fin_timeout=net_ipv4_tcp_fin_timeout,
            net_ipv4_tcp_keepalive_intvl=net_ipv4_tcp_keepalive_intvl,
            net_ipv4_tcp_keepalive_probes=net_ipv4_tcp_keepalive_probes,
            net_ipv4_tcp_keepalive_time=net_ipv4_tcp_keepalive_time,
            net_ipv4_tcp_max_syn_backlog=net_ipv4_tcp_max_syn_backlog,
            net_ipv4_tcp_max_tw_buckets=net_ipv4_tcp_max_tw_buckets,
            net_ipv4_tcp_tw_reuse=net_ipv4_tcp_tw_reuse,
            net_netfilter_nf_conntrack_buckets=net_netfilter_nf_conntrack_buckets,
            net_netfilter_nf_conntrack_max=net_netfilter_nf_conntrack_max,
            vm_max_map_count=vm_max_map_count,
            vm_swappiness=vm_swappiness,
            vm_vfs_cache_pressure=vm_vfs_cache_pressure,
        )

        return typing.cast(None, jsii.invoke(self, "putSysctlConfig", [value]))

    @jsii.member(jsii_name="resetSwapFileSizeMb")
    def reset_swap_file_size_mb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSwapFileSizeMb", []))

    @jsii.member(jsii_name="resetSysctlConfig")
    def reset_sysctl_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSysctlConfig", []))

    @jsii.member(jsii_name="resetTransparentHugePageDefrag")
    def reset_transparent_huge_page_defrag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransparentHugePageDefrag", []))

    @jsii.member(jsii_name="resetTransparentHugePageEnabled")
    def reset_transparent_huge_page_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransparentHugePageEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="sysctlConfig")
    def sysctl_config(
        self,
    ) -> "KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference":
        return typing.cast("KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference", jsii.get(self, "sysctlConfig"))

    @builtins.property
    @jsii.member(jsii_name="swapFileSizeMbInput")
    def swap_file_size_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "swapFileSizeMbInput"))

    @builtins.property
    @jsii.member(jsii_name="sysctlConfigInput")
    def sysctl_config_input(
        self,
    ) -> typing.Optional["KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfig"]:
        return typing.cast(typing.Optional["KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfig"], jsii.get(self, "sysctlConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="transparentHugePageDefragInput")
    def transparent_huge_page_defrag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transparentHugePageDefragInput"))

    @builtins.property
    @jsii.member(jsii_name="transparentHugePageEnabledInput")
    def transparent_huge_page_enabled_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transparentHugePageEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="swapFileSizeMb")
    def swap_file_size_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "swapFileSizeMb"))

    @swap_file_size_mb.setter
    def swap_file_size_mb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigOutputReference, "swap_file_size_mb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "swapFileSizeMb", value)

    @builtins.property
    @jsii.member(jsii_name="transparentHugePageDefrag")
    def transparent_huge_page_defrag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transparentHugePageDefrag"))

    @transparent_huge_page_defrag.setter
    def transparent_huge_page_defrag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigOutputReference, "transparent_huge_page_defrag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transparentHugePageDefrag", value)

    @builtins.property
    @jsii.member(jsii_name="transparentHugePageEnabled")
    def transparent_huge_page_enabled(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transparentHugePageEnabled"))

    @transparent_huge_page_enabled.setter
    def transparent_huge_page_enabled(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigOutputReference, "transparent_huge_page_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transparentHugePageEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KubernetesClusterDefaultNodePoolLinuxOsConfig]:
        return typing.cast(typing.Optional[KubernetesClusterDefaultNodePoolLinuxOsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterDefaultNodePoolLinuxOsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfig",
    jsii_struct_bases=[],
    name_mapping={
        "fs_aio_max_nr": "fsAioMaxNr",
        "fs_file_max": "fsFileMax",
        "fs_inotify_max_user_watches": "fsInotifyMaxUserWatches",
        "fs_nr_open": "fsNrOpen",
        "kernel_threads_max": "kernelThreadsMax",
        "net_core_netdev_max_backlog": "netCoreNetdevMaxBacklog",
        "net_core_optmem_max": "netCoreOptmemMax",
        "net_core_rmem_default": "netCoreRmemDefault",
        "net_core_rmem_max": "netCoreRmemMax",
        "net_core_somaxconn": "netCoreSomaxconn",
        "net_core_wmem_default": "netCoreWmemDefault",
        "net_core_wmem_max": "netCoreWmemMax",
        "net_ipv4_ip_local_port_range_max": "netIpv4IpLocalPortRangeMax",
        "net_ipv4_ip_local_port_range_min": "netIpv4IpLocalPortRangeMin",
        "net_ipv4_neigh_default_gc_thresh1": "netIpv4NeighDefaultGcThresh1",
        "net_ipv4_neigh_default_gc_thresh2": "netIpv4NeighDefaultGcThresh2",
        "net_ipv4_neigh_default_gc_thresh3": "netIpv4NeighDefaultGcThresh3",
        "net_ipv4_tcp_fin_timeout": "netIpv4TcpFinTimeout",
        "net_ipv4_tcp_keepalive_intvl": "netIpv4TcpKeepaliveIntvl",
        "net_ipv4_tcp_keepalive_probes": "netIpv4TcpKeepaliveProbes",
        "net_ipv4_tcp_keepalive_time": "netIpv4TcpKeepaliveTime",
        "net_ipv4_tcp_max_syn_backlog": "netIpv4TcpMaxSynBacklog",
        "net_ipv4_tcp_max_tw_buckets": "netIpv4TcpMaxTwBuckets",
        "net_ipv4_tcp_tw_reuse": "netIpv4TcpTwReuse",
        "net_netfilter_nf_conntrack_buckets": "netNetfilterNfConntrackBuckets",
        "net_netfilter_nf_conntrack_max": "netNetfilterNfConntrackMax",
        "vm_max_map_count": "vmMaxMapCount",
        "vm_swappiness": "vmSwappiness",
        "vm_vfs_cache_pressure": "vmVfsCachePressure",
    },
)
class KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfig:
    def __init__(
        self,
        *,
        fs_aio_max_nr: typing.Optional[jsii.Number] = None,
        fs_file_max: typing.Optional[jsii.Number] = None,
        fs_inotify_max_user_watches: typing.Optional[jsii.Number] = None,
        fs_nr_open: typing.Optional[jsii.Number] = None,
        kernel_threads_max: typing.Optional[jsii.Number] = None,
        net_core_netdev_max_backlog: typing.Optional[jsii.Number] = None,
        net_core_optmem_max: typing.Optional[jsii.Number] = None,
        net_core_rmem_default: typing.Optional[jsii.Number] = None,
        net_core_rmem_max: typing.Optional[jsii.Number] = None,
        net_core_somaxconn: typing.Optional[jsii.Number] = None,
        net_core_wmem_default: typing.Optional[jsii.Number] = None,
        net_core_wmem_max: typing.Optional[jsii.Number] = None,
        net_ipv4_ip_local_port_range_max: typing.Optional[jsii.Number] = None,
        net_ipv4_ip_local_port_range_min: typing.Optional[jsii.Number] = None,
        net_ipv4_neigh_default_gc_thresh1: typing.Optional[jsii.Number] = None,
        net_ipv4_neigh_default_gc_thresh2: typing.Optional[jsii.Number] = None,
        net_ipv4_neigh_default_gc_thresh3: typing.Optional[jsii.Number] = None,
        net_ipv4_tcp_fin_timeout: typing.Optional[jsii.Number] = None,
        net_ipv4_tcp_keepalive_intvl: typing.Optional[jsii.Number] = None,
        net_ipv4_tcp_keepalive_probes: typing.Optional[jsii.Number] = None,
        net_ipv4_tcp_keepalive_time: typing.Optional[jsii.Number] = None,
        net_ipv4_tcp_max_syn_backlog: typing.Optional[jsii.Number] = None,
        net_ipv4_tcp_max_tw_buckets: typing.Optional[jsii.Number] = None,
        net_ipv4_tcp_tw_reuse: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        net_netfilter_nf_conntrack_buckets: typing.Optional[jsii.Number] = None,
        net_netfilter_nf_conntrack_max: typing.Optional[jsii.Number] = None,
        vm_max_map_count: typing.Optional[jsii.Number] = None,
        vm_swappiness: typing.Optional[jsii.Number] = None,
        vm_vfs_cache_pressure: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fs_aio_max_nr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#fs_aio_max_nr KubernetesCluster#fs_aio_max_nr}.
        :param fs_file_max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#fs_file_max KubernetesCluster#fs_file_max}.
        :param fs_inotify_max_user_watches: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#fs_inotify_max_user_watches KubernetesCluster#fs_inotify_max_user_watches}.
        :param fs_nr_open: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#fs_nr_open KubernetesCluster#fs_nr_open}.
        :param kernel_threads_max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#kernel_threads_max KubernetesCluster#kernel_threads_max}.
        :param net_core_netdev_max_backlog: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_netdev_max_backlog KubernetesCluster#net_core_netdev_max_backlog}.
        :param net_core_optmem_max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_optmem_max KubernetesCluster#net_core_optmem_max}.
        :param net_core_rmem_default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_rmem_default KubernetesCluster#net_core_rmem_default}.
        :param net_core_rmem_max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_rmem_max KubernetesCluster#net_core_rmem_max}.
        :param net_core_somaxconn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_somaxconn KubernetesCluster#net_core_somaxconn}.
        :param net_core_wmem_default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_wmem_default KubernetesCluster#net_core_wmem_default}.
        :param net_core_wmem_max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_wmem_max KubernetesCluster#net_core_wmem_max}.
        :param net_ipv4_ip_local_port_range_max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_ip_local_port_range_max KubernetesCluster#net_ipv4_ip_local_port_range_max}.
        :param net_ipv4_ip_local_port_range_min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_ip_local_port_range_min KubernetesCluster#net_ipv4_ip_local_port_range_min}.
        :param net_ipv4_neigh_default_gc_thresh1: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_neigh_default_gc_thresh1 KubernetesCluster#net_ipv4_neigh_default_gc_thresh1}.
        :param net_ipv4_neigh_default_gc_thresh2: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_neigh_default_gc_thresh2 KubernetesCluster#net_ipv4_neigh_default_gc_thresh2}.
        :param net_ipv4_neigh_default_gc_thresh3: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_neigh_default_gc_thresh3 KubernetesCluster#net_ipv4_neigh_default_gc_thresh3}.
        :param net_ipv4_tcp_fin_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_fin_timeout KubernetesCluster#net_ipv4_tcp_fin_timeout}.
        :param net_ipv4_tcp_keepalive_intvl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_keepalive_intvl KubernetesCluster#net_ipv4_tcp_keepalive_intvl}.
        :param net_ipv4_tcp_keepalive_probes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_keepalive_probes KubernetesCluster#net_ipv4_tcp_keepalive_probes}.
        :param net_ipv4_tcp_keepalive_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_keepalive_time KubernetesCluster#net_ipv4_tcp_keepalive_time}.
        :param net_ipv4_tcp_max_syn_backlog: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_max_syn_backlog KubernetesCluster#net_ipv4_tcp_max_syn_backlog}.
        :param net_ipv4_tcp_max_tw_buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_max_tw_buckets KubernetesCluster#net_ipv4_tcp_max_tw_buckets}.
        :param net_ipv4_tcp_tw_reuse: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_tw_reuse KubernetesCluster#net_ipv4_tcp_tw_reuse}.
        :param net_netfilter_nf_conntrack_buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_netfilter_nf_conntrack_buckets KubernetesCluster#net_netfilter_nf_conntrack_buckets}.
        :param net_netfilter_nf_conntrack_max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_netfilter_nf_conntrack_max KubernetesCluster#net_netfilter_nf_conntrack_max}.
        :param vm_max_map_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#vm_max_map_count KubernetesCluster#vm_max_map_count}.
        :param vm_swappiness: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#vm_swappiness KubernetesCluster#vm_swappiness}.
        :param vm_vfs_cache_pressure: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#vm_vfs_cache_pressure KubernetesCluster#vm_vfs_cache_pressure}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfig.__init__)
            check_type(argname="argument fs_aio_max_nr", value=fs_aio_max_nr, expected_type=type_hints["fs_aio_max_nr"])
            check_type(argname="argument fs_file_max", value=fs_file_max, expected_type=type_hints["fs_file_max"])
            check_type(argname="argument fs_inotify_max_user_watches", value=fs_inotify_max_user_watches, expected_type=type_hints["fs_inotify_max_user_watches"])
            check_type(argname="argument fs_nr_open", value=fs_nr_open, expected_type=type_hints["fs_nr_open"])
            check_type(argname="argument kernel_threads_max", value=kernel_threads_max, expected_type=type_hints["kernel_threads_max"])
            check_type(argname="argument net_core_netdev_max_backlog", value=net_core_netdev_max_backlog, expected_type=type_hints["net_core_netdev_max_backlog"])
            check_type(argname="argument net_core_optmem_max", value=net_core_optmem_max, expected_type=type_hints["net_core_optmem_max"])
            check_type(argname="argument net_core_rmem_default", value=net_core_rmem_default, expected_type=type_hints["net_core_rmem_default"])
            check_type(argname="argument net_core_rmem_max", value=net_core_rmem_max, expected_type=type_hints["net_core_rmem_max"])
            check_type(argname="argument net_core_somaxconn", value=net_core_somaxconn, expected_type=type_hints["net_core_somaxconn"])
            check_type(argname="argument net_core_wmem_default", value=net_core_wmem_default, expected_type=type_hints["net_core_wmem_default"])
            check_type(argname="argument net_core_wmem_max", value=net_core_wmem_max, expected_type=type_hints["net_core_wmem_max"])
            check_type(argname="argument net_ipv4_ip_local_port_range_max", value=net_ipv4_ip_local_port_range_max, expected_type=type_hints["net_ipv4_ip_local_port_range_max"])
            check_type(argname="argument net_ipv4_ip_local_port_range_min", value=net_ipv4_ip_local_port_range_min, expected_type=type_hints["net_ipv4_ip_local_port_range_min"])
            check_type(argname="argument net_ipv4_neigh_default_gc_thresh1", value=net_ipv4_neigh_default_gc_thresh1, expected_type=type_hints["net_ipv4_neigh_default_gc_thresh1"])
            check_type(argname="argument net_ipv4_neigh_default_gc_thresh2", value=net_ipv4_neigh_default_gc_thresh2, expected_type=type_hints["net_ipv4_neigh_default_gc_thresh2"])
            check_type(argname="argument net_ipv4_neigh_default_gc_thresh3", value=net_ipv4_neigh_default_gc_thresh3, expected_type=type_hints["net_ipv4_neigh_default_gc_thresh3"])
            check_type(argname="argument net_ipv4_tcp_fin_timeout", value=net_ipv4_tcp_fin_timeout, expected_type=type_hints["net_ipv4_tcp_fin_timeout"])
            check_type(argname="argument net_ipv4_tcp_keepalive_intvl", value=net_ipv4_tcp_keepalive_intvl, expected_type=type_hints["net_ipv4_tcp_keepalive_intvl"])
            check_type(argname="argument net_ipv4_tcp_keepalive_probes", value=net_ipv4_tcp_keepalive_probes, expected_type=type_hints["net_ipv4_tcp_keepalive_probes"])
            check_type(argname="argument net_ipv4_tcp_keepalive_time", value=net_ipv4_tcp_keepalive_time, expected_type=type_hints["net_ipv4_tcp_keepalive_time"])
            check_type(argname="argument net_ipv4_tcp_max_syn_backlog", value=net_ipv4_tcp_max_syn_backlog, expected_type=type_hints["net_ipv4_tcp_max_syn_backlog"])
            check_type(argname="argument net_ipv4_tcp_max_tw_buckets", value=net_ipv4_tcp_max_tw_buckets, expected_type=type_hints["net_ipv4_tcp_max_tw_buckets"])
            check_type(argname="argument net_ipv4_tcp_tw_reuse", value=net_ipv4_tcp_tw_reuse, expected_type=type_hints["net_ipv4_tcp_tw_reuse"])
            check_type(argname="argument net_netfilter_nf_conntrack_buckets", value=net_netfilter_nf_conntrack_buckets, expected_type=type_hints["net_netfilter_nf_conntrack_buckets"])
            check_type(argname="argument net_netfilter_nf_conntrack_max", value=net_netfilter_nf_conntrack_max, expected_type=type_hints["net_netfilter_nf_conntrack_max"])
            check_type(argname="argument vm_max_map_count", value=vm_max_map_count, expected_type=type_hints["vm_max_map_count"])
            check_type(argname="argument vm_swappiness", value=vm_swappiness, expected_type=type_hints["vm_swappiness"])
            check_type(argname="argument vm_vfs_cache_pressure", value=vm_vfs_cache_pressure, expected_type=type_hints["vm_vfs_cache_pressure"])
        self._values: typing.Dict[str, typing.Any] = {}
        if fs_aio_max_nr is not None:
            self._values["fs_aio_max_nr"] = fs_aio_max_nr
        if fs_file_max is not None:
            self._values["fs_file_max"] = fs_file_max
        if fs_inotify_max_user_watches is not None:
            self._values["fs_inotify_max_user_watches"] = fs_inotify_max_user_watches
        if fs_nr_open is not None:
            self._values["fs_nr_open"] = fs_nr_open
        if kernel_threads_max is not None:
            self._values["kernel_threads_max"] = kernel_threads_max
        if net_core_netdev_max_backlog is not None:
            self._values["net_core_netdev_max_backlog"] = net_core_netdev_max_backlog
        if net_core_optmem_max is not None:
            self._values["net_core_optmem_max"] = net_core_optmem_max
        if net_core_rmem_default is not None:
            self._values["net_core_rmem_default"] = net_core_rmem_default
        if net_core_rmem_max is not None:
            self._values["net_core_rmem_max"] = net_core_rmem_max
        if net_core_somaxconn is not None:
            self._values["net_core_somaxconn"] = net_core_somaxconn
        if net_core_wmem_default is not None:
            self._values["net_core_wmem_default"] = net_core_wmem_default
        if net_core_wmem_max is not None:
            self._values["net_core_wmem_max"] = net_core_wmem_max
        if net_ipv4_ip_local_port_range_max is not None:
            self._values["net_ipv4_ip_local_port_range_max"] = net_ipv4_ip_local_port_range_max
        if net_ipv4_ip_local_port_range_min is not None:
            self._values["net_ipv4_ip_local_port_range_min"] = net_ipv4_ip_local_port_range_min
        if net_ipv4_neigh_default_gc_thresh1 is not None:
            self._values["net_ipv4_neigh_default_gc_thresh1"] = net_ipv4_neigh_default_gc_thresh1
        if net_ipv4_neigh_default_gc_thresh2 is not None:
            self._values["net_ipv4_neigh_default_gc_thresh2"] = net_ipv4_neigh_default_gc_thresh2
        if net_ipv4_neigh_default_gc_thresh3 is not None:
            self._values["net_ipv4_neigh_default_gc_thresh3"] = net_ipv4_neigh_default_gc_thresh3
        if net_ipv4_tcp_fin_timeout is not None:
            self._values["net_ipv4_tcp_fin_timeout"] = net_ipv4_tcp_fin_timeout
        if net_ipv4_tcp_keepalive_intvl is not None:
            self._values["net_ipv4_tcp_keepalive_intvl"] = net_ipv4_tcp_keepalive_intvl
        if net_ipv4_tcp_keepalive_probes is not None:
            self._values["net_ipv4_tcp_keepalive_probes"] = net_ipv4_tcp_keepalive_probes
        if net_ipv4_tcp_keepalive_time is not None:
            self._values["net_ipv4_tcp_keepalive_time"] = net_ipv4_tcp_keepalive_time
        if net_ipv4_tcp_max_syn_backlog is not None:
            self._values["net_ipv4_tcp_max_syn_backlog"] = net_ipv4_tcp_max_syn_backlog
        if net_ipv4_tcp_max_tw_buckets is not None:
            self._values["net_ipv4_tcp_max_tw_buckets"] = net_ipv4_tcp_max_tw_buckets
        if net_ipv4_tcp_tw_reuse is not None:
            self._values["net_ipv4_tcp_tw_reuse"] = net_ipv4_tcp_tw_reuse
        if net_netfilter_nf_conntrack_buckets is not None:
            self._values["net_netfilter_nf_conntrack_buckets"] = net_netfilter_nf_conntrack_buckets
        if net_netfilter_nf_conntrack_max is not None:
            self._values["net_netfilter_nf_conntrack_max"] = net_netfilter_nf_conntrack_max
        if vm_max_map_count is not None:
            self._values["vm_max_map_count"] = vm_max_map_count
        if vm_swappiness is not None:
            self._values["vm_swappiness"] = vm_swappiness
        if vm_vfs_cache_pressure is not None:
            self._values["vm_vfs_cache_pressure"] = vm_vfs_cache_pressure

    @builtins.property
    def fs_aio_max_nr(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#fs_aio_max_nr KubernetesCluster#fs_aio_max_nr}.'''
        result = self._values.get("fs_aio_max_nr")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def fs_file_max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#fs_file_max KubernetesCluster#fs_file_max}.'''
        result = self._values.get("fs_file_max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def fs_inotify_max_user_watches(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#fs_inotify_max_user_watches KubernetesCluster#fs_inotify_max_user_watches}.'''
        result = self._values.get("fs_inotify_max_user_watches")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def fs_nr_open(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#fs_nr_open KubernetesCluster#fs_nr_open}.'''
        result = self._values.get("fs_nr_open")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kernel_threads_max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#kernel_threads_max KubernetesCluster#kernel_threads_max}.'''
        result = self._values.get("kernel_threads_max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_core_netdev_max_backlog(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_netdev_max_backlog KubernetesCluster#net_core_netdev_max_backlog}.'''
        result = self._values.get("net_core_netdev_max_backlog")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_core_optmem_max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_optmem_max KubernetesCluster#net_core_optmem_max}.'''
        result = self._values.get("net_core_optmem_max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_core_rmem_default(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_rmem_default KubernetesCluster#net_core_rmem_default}.'''
        result = self._values.get("net_core_rmem_default")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_core_rmem_max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_rmem_max KubernetesCluster#net_core_rmem_max}.'''
        result = self._values.get("net_core_rmem_max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_core_somaxconn(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_somaxconn KubernetesCluster#net_core_somaxconn}.'''
        result = self._values.get("net_core_somaxconn")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_core_wmem_default(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_wmem_default KubernetesCluster#net_core_wmem_default}.'''
        result = self._values.get("net_core_wmem_default")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_core_wmem_max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_core_wmem_max KubernetesCluster#net_core_wmem_max}.'''
        result = self._values.get("net_core_wmem_max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_ipv4_ip_local_port_range_max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_ip_local_port_range_max KubernetesCluster#net_ipv4_ip_local_port_range_max}.'''
        result = self._values.get("net_ipv4_ip_local_port_range_max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_ipv4_ip_local_port_range_min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_ip_local_port_range_min KubernetesCluster#net_ipv4_ip_local_port_range_min}.'''
        result = self._values.get("net_ipv4_ip_local_port_range_min")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_ipv4_neigh_default_gc_thresh1(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_neigh_default_gc_thresh1 KubernetesCluster#net_ipv4_neigh_default_gc_thresh1}.'''
        result = self._values.get("net_ipv4_neigh_default_gc_thresh1")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_ipv4_neigh_default_gc_thresh2(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_neigh_default_gc_thresh2 KubernetesCluster#net_ipv4_neigh_default_gc_thresh2}.'''
        result = self._values.get("net_ipv4_neigh_default_gc_thresh2")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_ipv4_neigh_default_gc_thresh3(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_neigh_default_gc_thresh3 KubernetesCluster#net_ipv4_neigh_default_gc_thresh3}.'''
        result = self._values.get("net_ipv4_neigh_default_gc_thresh3")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_ipv4_tcp_fin_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_fin_timeout KubernetesCluster#net_ipv4_tcp_fin_timeout}.'''
        result = self._values.get("net_ipv4_tcp_fin_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_ipv4_tcp_keepalive_intvl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_keepalive_intvl KubernetesCluster#net_ipv4_tcp_keepalive_intvl}.'''
        result = self._values.get("net_ipv4_tcp_keepalive_intvl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_ipv4_tcp_keepalive_probes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_keepalive_probes KubernetesCluster#net_ipv4_tcp_keepalive_probes}.'''
        result = self._values.get("net_ipv4_tcp_keepalive_probes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_ipv4_tcp_keepalive_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_keepalive_time KubernetesCluster#net_ipv4_tcp_keepalive_time}.'''
        result = self._values.get("net_ipv4_tcp_keepalive_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_ipv4_tcp_max_syn_backlog(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_max_syn_backlog KubernetesCluster#net_ipv4_tcp_max_syn_backlog}.'''
        result = self._values.get("net_ipv4_tcp_max_syn_backlog")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_ipv4_tcp_max_tw_buckets(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_max_tw_buckets KubernetesCluster#net_ipv4_tcp_max_tw_buckets}.'''
        result = self._values.get("net_ipv4_tcp_max_tw_buckets")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_ipv4_tcp_tw_reuse(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_ipv4_tcp_tw_reuse KubernetesCluster#net_ipv4_tcp_tw_reuse}.'''
        result = self._values.get("net_ipv4_tcp_tw_reuse")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def net_netfilter_nf_conntrack_buckets(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_netfilter_nf_conntrack_buckets KubernetesCluster#net_netfilter_nf_conntrack_buckets}.'''
        result = self._values.get("net_netfilter_nf_conntrack_buckets")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def net_netfilter_nf_conntrack_max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#net_netfilter_nf_conntrack_max KubernetesCluster#net_netfilter_nf_conntrack_max}.'''
        result = self._values.get("net_netfilter_nf_conntrack_max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vm_max_map_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#vm_max_map_count KubernetesCluster#vm_max_map_count}.'''
        result = self._values.get("vm_max_map_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vm_swappiness(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#vm_swappiness KubernetesCluster#vm_swappiness}.'''
        result = self._values.get("vm_swappiness")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vm_vfs_cache_pressure(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#vm_vfs_cache_pressure KubernetesCluster#vm_vfs_cache_pressure}.'''
        result = self._values.get("vm_vfs_cache_pressure")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsAioMaxNr")
    def reset_fs_aio_max_nr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsAioMaxNr", []))

    @jsii.member(jsii_name="resetFsFileMax")
    def reset_fs_file_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsFileMax", []))

    @jsii.member(jsii_name="resetFsInotifyMaxUserWatches")
    def reset_fs_inotify_max_user_watches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsInotifyMaxUserWatches", []))

    @jsii.member(jsii_name="resetFsNrOpen")
    def reset_fs_nr_open(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsNrOpen", []))

    @jsii.member(jsii_name="resetKernelThreadsMax")
    def reset_kernel_threads_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKernelThreadsMax", []))

    @jsii.member(jsii_name="resetNetCoreNetdevMaxBacklog")
    def reset_net_core_netdev_max_backlog(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetCoreNetdevMaxBacklog", []))

    @jsii.member(jsii_name="resetNetCoreOptmemMax")
    def reset_net_core_optmem_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetCoreOptmemMax", []))

    @jsii.member(jsii_name="resetNetCoreRmemDefault")
    def reset_net_core_rmem_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetCoreRmemDefault", []))

    @jsii.member(jsii_name="resetNetCoreRmemMax")
    def reset_net_core_rmem_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetCoreRmemMax", []))

    @jsii.member(jsii_name="resetNetCoreSomaxconn")
    def reset_net_core_somaxconn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetCoreSomaxconn", []))

    @jsii.member(jsii_name="resetNetCoreWmemDefault")
    def reset_net_core_wmem_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetCoreWmemDefault", []))

    @jsii.member(jsii_name="resetNetCoreWmemMax")
    def reset_net_core_wmem_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetCoreWmemMax", []))

    @jsii.member(jsii_name="resetNetIpv4IpLocalPortRangeMax")
    def reset_net_ipv4_ip_local_port_range_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetIpv4IpLocalPortRangeMax", []))

    @jsii.member(jsii_name="resetNetIpv4IpLocalPortRangeMin")
    def reset_net_ipv4_ip_local_port_range_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetIpv4IpLocalPortRangeMin", []))

    @jsii.member(jsii_name="resetNetIpv4NeighDefaultGcThresh1")
    def reset_net_ipv4_neigh_default_gc_thresh1(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetIpv4NeighDefaultGcThresh1", []))

    @jsii.member(jsii_name="resetNetIpv4NeighDefaultGcThresh2")
    def reset_net_ipv4_neigh_default_gc_thresh2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetIpv4NeighDefaultGcThresh2", []))

    @jsii.member(jsii_name="resetNetIpv4NeighDefaultGcThresh3")
    def reset_net_ipv4_neigh_default_gc_thresh3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetIpv4NeighDefaultGcThresh3", []))

    @jsii.member(jsii_name="resetNetIpv4TcpFinTimeout")
    def reset_net_ipv4_tcp_fin_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetIpv4TcpFinTimeout", []))

    @jsii.member(jsii_name="resetNetIpv4TcpKeepaliveIntvl")
    def reset_net_ipv4_tcp_keepalive_intvl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetIpv4TcpKeepaliveIntvl", []))

    @jsii.member(jsii_name="resetNetIpv4TcpKeepaliveProbes")
    def reset_net_ipv4_tcp_keepalive_probes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetIpv4TcpKeepaliveProbes", []))

    @jsii.member(jsii_name="resetNetIpv4TcpKeepaliveTime")
    def reset_net_ipv4_tcp_keepalive_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetIpv4TcpKeepaliveTime", []))

    @jsii.member(jsii_name="resetNetIpv4TcpMaxSynBacklog")
    def reset_net_ipv4_tcp_max_syn_backlog(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetIpv4TcpMaxSynBacklog", []))

    @jsii.member(jsii_name="resetNetIpv4TcpMaxTwBuckets")
    def reset_net_ipv4_tcp_max_tw_buckets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetIpv4TcpMaxTwBuckets", []))

    @jsii.member(jsii_name="resetNetIpv4TcpTwReuse")
    def reset_net_ipv4_tcp_tw_reuse(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetIpv4TcpTwReuse", []))

    @jsii.member(jsii_name="resetNetNetfilterNfConntrackBuckets")
    def reset_net_netfilter_nf_conntrack_buckets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetNetfilterNfConntrackBuckets", []))

    @jsii.member(jsii_name="resetNetNetfilterNfConntrackMax")
    def reset_net_netfilter_nf_conntrack_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetNetfilterNfConntrackMax", []))

    @jsii.member(jsii_name="resetVmMaxMapCount")
    def reset_vm_max_map_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVmMaxMapCount", []))

    @jsii.member(jsii_name="resetVmSwappiness")
    def reset_vm_swappiness(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVmSwappiness", []))

    @jsii.member(jsii_name="resetVmVfsCachePressure")
    def reset_vm_vfs_cache_pressure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVmVfsCachePressure", []))

    @builtins.property
    @jsii.member(jsii_name="fsAioMaxNrInput")
    def fs_aio_max_nr_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fsAioMaxNrInput"))

    @builtins.property
    @jsii.member(jsii_name="fsFileMaxInput")
    def fs_file_max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fsFileMaxInput"))

    @builtins.property
    @jsii.member(jsii_name="fsInotifyMaxUserWatchesInput")
    def fs_inotify_max_user_watches_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fsInotifyMaxUserWatchesInput"))

    @builtins.property
    @jsii.member(jsii_name="fsNrOpenInput")
    def fs_nr_open_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fsNrOpenInput"))

    @builtins.property
    @jsii.member(jsii_name="kernelThreadsMaxInput")
    def kernel_threads_max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "kernelThreadsMaxInput"))

    @builtins.property
    @jsii.member(jsii_name="netCoreNetdevMaxBacklogInput")
    def net_core_netdev_max_backlog_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netCoreNetdevMaxBacklogInput"))

    @builtins.property
    @jsii.member(jsii_name="netCoreOptmemMaxInput")
    def net_core_optmem_max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netCoreOptmemMaxInput"))

    @builtins.property
    @jsii.member(jsii_name="netCoreRmemDefaultInput")
    def net_core_rmem_default_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netCoreRmemDefaultInput"))

    @builtins.property
    @jsii.member(jsii_name="netCoreRmemMaxInput")
    def net_core_rmem_max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netCoreRmemMaxInput"))

    @builtins.property
    @jsii.member(jsii_name="netCoreSomaxconnInput")
    def net_core_somaxconn_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netCoreSomaxconnInput"))

    @builtins.property
    @jsii.member(jsii_name="netCoreWmemDefaultInput")
    def net_core_wmem_default_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netCoreWmemDefaultInput"))

    @builtins.property
    @jsii.member(jsii_name="netCoreWmemMaxInput")
    def net_core_wmem_max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netCoreWmemMaxInput"))

    @builtins.property
    @jsii.member(jsii_name="netIpv4IpLocalPortRangeMaxInput")
    def net_ipv4_ip_local_port_range_max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netIpv4IpLocalPortRangeMaxInput"))

    @builtins.property
    @jsii.member(jsii_name="netIpv4IpLocalPortRangeMinInput")
    def net_ipv4_ip_local_port_range_min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netIpv4IpLocalPortRangeMinInput"))

    @builtins.property
    @jsii.member(jsii_name="netIpv4NeighDefaultGcThresh1Input")
    def net_ipv4_neigh_default_gc_thresh1_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netIpv4NeighDefaultGcThresh1Input"))

    @builtins.property
    @jsii.member(jsii_name="netIpv4NeighDefaultGcThresh2Input")
    def net_ipv4_neigh_default_gc_thresh2_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netIpv4NeighDefaultGcThresh2Input"))

    @builtins.property
    @jsii.member(jsii_name="netIpv4NeighDefaultGcThresh3Input")
    def net_ipv4_neigh_default_gc_thresh3_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netIpv4NeighDefaultGcThresh3Input"))

    @builtins.property
    @jsii.member(jsii_name="netIpv4TcpFinTimeoutInput")
    def net_ipv4_tcp_fin_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netIpv4TcpFinTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="netIpv4TcpKeepaliveIntvlInput")
    def net_ipv4_tcp_keepalive_intvl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netIpv4TcpKeepaliveIntvlInput"))

    @builtins.property
    @jsii.member(jsii_name="netIpv4TcpKeepaliveProbesInput")
    def net_ipv4_tcp_keepalive_probes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netIpv4TcpKeepaliveProbesInput"))

    @builtins.property
    @jsii.member(jsii_name="netIpv4TcpKeepaliveTimeInput")
    def net_ipv4_tcp_keepalive_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netIpv4TcpKeepaliveTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="netIpv4TcpMaxSynBacklogInput")
    def net_ipv4_tcp_max_syn_backlog_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netIpv4TcpMaxSynBacklogInput"))

    @builtins.property
    @jsii.member(jsii_name="netIpv4TcpMaxTwBucketsInput")
    def net_ipv4_tcp_max_tw_buckets_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netIpv4TcpMaxTwBucketsInput"))

    @builtins.property
    @jsii.member(jsii_name="netIpv4TcpTwReuseInput")
    def net_ipv4_tcp_tw_reuse_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "netIpv4TcpTwReuseInput"))

    @builtins.property
    @jsii.member(jsii_name="netNetfilterNfConntrackBucketsInput")
    def net_netfilter_nf_conntrack_buckets_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netNetfilterNfConntrackBucketsInput"))

    @builtins.property
    @jsii.member(jsii_name="netNetfilterNfConntrackMaxInput")
    def net_netfilter_nf_conntrack_max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "netNetfilterNfConntrackMaxInput"))

    @builtins.property
    @jsii.member(jsii_name="vmMaxMapCountInput")
    def vm_max_map_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vmMaxMapCountInput"))

    @builtins.property
    @jsii.member(jsii_name="vmSwappinessInput")
    def vm_swappiness_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vmSwappinessInput"))

    @builtins.property
    @jsii.member(jsii_name="vmVfsCachePressureInput")
    def vm_vfs_cache_pressure_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vmVfsCachePressureInput"))

    @builtins.property
    @jsii.member(jsii_name="fsAioMaxNr")
    def fs_aio_max_nr(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fsAioMaxNr"))

    @fs_aio_max_nr.setter
    def fs_aio_max_nr(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "fs_aio_max_nr").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsAioMaxNr", value)

    @builtins.property
    @jsii.member(jsii_name="fsFileMax")
    def fs_file_max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fsFileMax"))

    @fs_file_max.setter
    def fs_file_max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "fs_file_max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsFileMax", value)

    @builtins.property
    @jsii.member(jsii_name="fsInotifyMaxUserWatches")
    def fs_inotify_max_user_watches(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fsInotifyMaxUserWatches"))

    @fs_inotify_max_user_watches.setter
    def fs_inotify_max_user_watches(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "fs_inotify_max_user_watches").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsInotifyMaxUserWatches", value)

    @builtins.property
    @jsii.member(jsii_name="fsNrOpen")
    def fs_nr_open(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fsNrOpen"))

    @fs_nr_open.setter
    def fs_nr_open(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "fs_nr_open").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsNrOpen", value)

    @builtins.property
    @jsii.member(jsii_name="kernelThreadsMax")
    def kernel_threads_max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "kernelThreadsMax"))

    @kernel_threads_max.setter
    def kernel_threads_max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "kernel_threads_max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kernelThreadsMax", value)

    @builtins.property
    @jsii.member(jsii_name="netCoreNetdevMaxBacklog")
    def net_core_netdev_max_backlog(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netCoreNetdevMaxBacklog"))

    @net_core_netdev_max_backlog.setter
    def net_core_netdev_max_backlog(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_core_netdev_max_backlog").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netCoreNetdevMaxBacklog", value)

    @builtins.property
    @jsii.member(jsii_name="netCoreOptmemMax")
    def net_core_optmem_max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netCoreOptmemMax"))

    @net_core_optmem_max.setter
    def net_core_optmem_max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_core_optmem_max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netCoreOptmemMax", value)

    @builtins.property
    @jsii.member(jsii_name="netCoreRmemDefault")
    def net_core_rmem_default(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netCoreRmemDefault"))

    @net_core_rmem_default.setter
    def net_core_rmem_default(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_core_rmem_default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netCoreRmemDefault", value)

    @builtins.property
    @jsii.member(jsii_name="netCoreRmemMax")
    def net_core_rmem_max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netCoreRmemMax"))

    @net_core_rmem_max.setter
    def net_core_rmem_max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_core_rmem_max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netCoreRmemMax", value)

    @builtins.property
    @jsii.member(jsii_name="netCoreSomaxconn")
    def net_core_somaxconn(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netCoreSomaxconn"))

    @net_core_somaxconn.setter
    def net_core_somaxconn(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_core_somaxconn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netCoreSomaxconn", value)

    @builtins.property
    @jsii.member(jsii_name="netCoreWmemDefault")
    def net_core_wmem_default(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netCoreWmemDefault"))

    @net_core_wmem_default.setter
    def net_core_wmem_default(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_core_wmem_default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netCoreWmemDefault", value)

    @builtins.property
    @jsii.member(jsii_name="netCoreWmemMax")
    def net_core_wmem_max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netCoreWmemMax"))

    @net_core_wmem_max.setter
    def net_core_wmem_max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_core_wmem_max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netCoreWmemMax", value)

    @builtins.property
    @jsii.member(jsii_name="netIpv4IpLocalPortRangeMax")
    def net_ipv4_ip_local_port_range_max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netIpv4IpLocalPortRangeMax"))

    @net_ipv4_ip_local_port_range_max.setter
    def net_ipv4_ip_local_port_range_max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_ipv4_ip_local_port_range_max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netIpv4IpLocalPortRangeMax", value)

    @builtins.property
    @jsii.member(jsii_name="netIpv4IpLocalPortRangeMin")
    def net_ipv4_ip_local_port_range_min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netIpv4IpLocalPortRangeMin"))

    @net_ipv4_ip_local_port_range_min.setter
    def net_ipv4_ip_local_port_range_min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_ipv4_ip_local_port_range_min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netIpv4IpLocalPortRangeMin", value)

    @builtins.property
    @jsii.member(jsii_name="netIpv4NeighDefaultGcThresh1")
    def net_ipv4_neigh_default_gc_thresh1(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netIpv4NeighDefaultGcThresh1"))

    @net_ipv4_neigh_default_gc_thresh1.setter
    def net_ipv4_neigh_default_gc_thresh1(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_ipv4_neigh_default_gc_thresh1").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netIpv4NeighDefaultGcThresh1", value)

    @builtins.property
    @jsii.member(jsii_name="netIpv4NeighDefaultGcThresh2")
    def net_ipv4_neigh_default_gc_thresh2(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netIpv4NeighDefaultGcThresh2"))

    @net_ipv4_neigh_default_gc_thresh2.setter
    def net_ipv4_neigh_default_gc_thresh2(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_ipv4_neigh_default_gc_thresh2").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netIpv4NeighDefaultGcThresh2", value)

    @builtins.property
    @jsii.member(jsii_name="netIpv4NeighDefaultGcThresh3")
    def net_ipv4_neigh_default_gc_thresh3(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netIpv4NeighDefaultGcThresh3"))

    @net_ipv4_neigh_default_gc_thresh3.setter
    def net_ipv4_neigh_default_gc_thresh3(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_ipv4_neigh_default_gc_thresh3").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netIpv4NeighDefaultGcThresh3", value)

    @builtins.property
    @jsii.member(jsii_name="netIpv4TcpFinTimeout")
    def net_ipv4_tcp_fin_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netIpv4TcpFinTimeout"))

    @net_ipv4_tcp_fin_timeout.setter
    def net_ipv4_tcp_fin_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_ipv4_tcp_fin_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netIpv4TcpFinTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="netIpv4TcpKeepaliveIntvl")
    def net_ipv4_tcp_keepalive_intvl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netIpv4TcpKeepaliveIntvl"))

    @net_ipv4_tcp_keepalive_intvl.setter
    def net_ipv4_tcp_keepalive_intvl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_ipv4_tcp_keepalive_intvl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netIpv4TcpKeepaliveIntvl", value)

    @builtins.property
    @jsii.member(jsii_name="netIpv4TcpKeepaliveProbes")
    def net_ipv4_tcp_keepalive_probes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netIpv4TcpKeepaliveProbes"))

    @net_ipv4_tcp_keepalive_probes.setter
    def net_ipv4_tcp_keepalive_probes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_ipv4_tcp_keepalive_probes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netIpv4TcpKeepaliveProbes", value)

    @builtins.property
    @jsii.member(jsii_name="netIpv4TcpKeepaliveTime")
    def net_ipv4_tcp_keepalive_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netIpv4TcpKeepaliveTime"))

    @net_ipv4_tcp_keepalive_time.setter
    def net_ipv4_tcp_keepalive_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_ipv4_tcp_keepalive_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netIpv4TcpKeepaliveTime", value)

    @builtins.property
    @jsii.member(jsii_name="netIpv4TcpMaxSynBacklog")
    def net_ipv4_tcp_max_syn_backlog(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netIpv4TcpMaxSynBacklog"))

    @net_ipv4_tcp_max_syn_backlog.setter
    def net_ipv4_tcp_max_syn_backlog(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_ipv4_tcp_max_syn_backlog").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netIpv4TcpMaxSynBacklog", value)

    @builtins.property
    @jsii.member(jsii_name="netIpv4TcpMaxTwBuckets")
    def net_ipv4_tcp_max_tw_buckets(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netIpv4TcpMaxTwBuckets"))

    @net_ipv4_tcp_max_tw_buckets.setter
    def net_ipv4_tcp_max_tw_buckets(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_ipv4_tcp_max_tw_buckets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netIpv4TcpMaxTwBuckets", value)

    @builtins.property
    @jsii.member(jsii_name="netIpv4TcpTwReuse")
    def net_ipv4_tcp_tw_reuse(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "netIpv4TcpTwReuse"))

    @net_ipv4_tcp_tw_reuse.setter
    def net_ipv4_tcp_tw_reuse(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_ipv4_tcp_tw_reuse").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netIpv4TcpTwReuse", value)

    @builtins.property
    @jsii.member(jsii_name="netNetfilterNfConntrackBuckets")
    def net_netfilter_nf_conntrack_buckets(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netNetfilterNfConntrackBuckets"))

    @net_netfilter_nf_conntrack_buckets.setter
    def net_netfilter_nf_conntrack_buckets(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_netfilter_nf_conntrack_buckets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netNetfilterNfConntrackBuckets", value)

    @builtins.property
    @jsii.member(jsii_name="netNetfilterNfConntrackMax")
    def net_netfilter_nf_conntrack_max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "netNetfilterNfConntrackMax"))

    @net_netfilter_nf_conntrack_max.setter
    def net_netfilter_nf_conntrack_max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "net_netfilter_nf_conntrack_max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netNetfilterNfConntrackMax", value)

    @builtins.property
    @jsii.member(jsii_name="vmMaxMapCount")
    def vm_max_map_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vmMaxMapCount"))

    @vm_max_map_count.setter
    def vm_max_map_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "vm_max_map_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmMaxMapCount", value)

    @builtins.property
    @jsii.member(jsii_name="vmSwappiness")
    def vm_swappiness(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vmSwappiness"))

    @vm_swappiness.setter
    def vm_swappiness(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "vm_swappiness").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmSwappiness", value)

    @builtins.property
    @jsii.member(jsii_name="vmVfsCachePressure")
    def vm_vfs_cache_pressure(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vmVfsCachePressure"))

    @vm_vfs_cache_pressure.setter
    def vm_vfs_cache_pressure(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "vm_vfs_cache_pressure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmVfsCachePressure", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfig]:
        return typing.cast(typing.Optional[KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterDefaultNodePoolOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterDefaultNodePoolOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterDefaultNodePoolOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putKubeletConfig")
    def put_kubelet_config(
        self,
        *,
        allowed_unsafe_sysctls: typing.Optional[typing.Sequence[builtins.str]] = None,
        container_log_max_line: typing.Optional[jsii.Number] = None,
        container_log_max_size_mb: typing.Optional[jsii.Number] = None,
        cpu_cfs_quota_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cpu_cfs_quota_period: typing.Optional[builtins.str] = None,
        cpu_manager_policy: typing.Optional[builtins.str] = None,
        image_gc_high_threshold: typing.Optional[jsii.Number] = None,
        image_gc_low_threshold: typing.Optional[jsii.Number] = None,
        pod_max_pid: typing.Optional[jsii.Number] = None,
        topology_manager_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_unsafe_sysctls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#allowed_unsafe_sysctls KubernetesCluster#allowed_unsafe_sysctls}.
        :param container_log_max_line: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#container_log_max_line KubernetesCluster#container_log_max_line}.
        :param container_log_max_size_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#container_log_max_size_mb KubernetesCluster#container_log_max_size_mb}.
        :param cpu_cfs_quota_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#cpu_cfs_quota_enabled KubernetesCluster#cpu_cfs_quota_enabled}.
        :param cpu_cfs_quota_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#cpu_cfs_quota_period KubernetesCluster#cpu_cfs_quota_period}.
        :param cpu_manager_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#cpu_manager_policy KubernetesCluster#cpu_manager_policy}.
        :param image_gc_high_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#image_gc_high_threshold KubernetesCluster#image_gc_high_threshold}.
        :param image_gc_low_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#image_gc_low_threshold KubernetesCluster#image_gc_low_threshold}.
        :param pod_max_pid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#pod_max_pid KubernetesCluster#pod_max_pid}.
        :param topology_manager_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#topology_manager_policy KubernetesCluster#topology_manager_policy}.
        '''
        value = KubernetesClusterDefaultNodePoolKubeletConfig(
            allowed_unsafe_sysctls=allowed_unsafe_sysctls,
            container_log_max_line=container_log_max_line,
            container_log_max_size_mb=container_log_max_size_mb,
            cpu_cfs_quota_enabled=cpu_cfs_quota_enabled,
            cpu_cfs_quota_period=cpu_cfs_quota_period,
            cpu_manager_policy=cpu_manager_policy,
            image_gc_high_threshold=image_gc_high_threshold,
            image_gc_low_threshold=image_gc_low_threshold,
            pod_max_pid=pod_max_pid,
            topology_manager_policy=topology_manager_policy,
        )

        return typing.cast(None, jsii.invoke(self, "putKubeletConfig", [value]))

    @jsii.member(jsii_name="putLinuxOsConfig")
    def put_linux_os_config(
        self,
        *,
        swap_file_size_mb: typing.Optional[jsii.Number] = None,
        sysctl_config: typing.Optional[typing.Union[KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfig, typing.Dict[str, typing.Any]]] = None,
        transparent_huge_page_defrag: typing.Optional[builtins.str] = None,
        transparent_huge_page_enabled: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param swap_file_size_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#swap_file_size_mb KubernetesCluster#swap_file_size_mb}.
        :param sysctl_config: sysctl_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#sysctl_config KubernetesCluster#sysctl_config}
        :param transparent_huge_page_defrag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#transparent_huge_page_defrag KubernetesCluster#transparent_huge_page_defrag}.
        :param transparent_huge_page_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#transparent_huge_page_enabled KubernetesCluster#transparent_huge_page_enabled}.
        '''
        value = KubernetesClusterDefaultNodePoolLinuxOsConfig(
            swap_file_size_mb=swap_file_size_mb,
            sysctl_config=sysctl_config,
            transparent_huge_page_defrag=transparent_huge_page_defrag,
            transparent_huge_page_enabled=transparent_huge_page_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putLinuxOsConfig", [value]))

    @jsii.member(jsii_name="putUpgradeSettings")
    def put_upgrade_settings(self, *, max_surge: builtins.str) -> None:
        '''
        :param max_surge: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_surge KubernetesCluster#max_surge}.
        '''
        value = KubernetesClusterDefaultNodePoolUpgradeSettings(max_surge=max_surge)

        return typing.cast(None, jsii.invoke(self, "putUpgradeSettings", [value]))

    @jsii.member(jsii_name="resetCapacityReservationGroupId")
    def reset_capacity_reservation_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityReservationGroupId", []))

    @jsii.member(jsii_name="resetEnableAutoScaling")
    def reset_enable_auto_scaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAutoScaling", []))

    @jsii.member(jsii_name="resetEnableHostEncryption")
    def reset_enable_host_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableHostEncryption", []))

    @jsii.member(jsii_name="resetEnableNodePublicIp")
    def reset_enable_node_public_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableNodePublicIp", []))

    @jsii.member(jsii_name="resetFipsEnabled")
    def reset_fips_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFipsEnabled", []))

    @jsii.member(jsii_name="resetHostGroupId")
    def reset_host_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostGroupId", []))

    @jsii.member(jsii_name="resetKubeletConfig")
    def reset_kubelet_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKubeletConfig", []))

    @jsii.member(jsii_name="resetKubeletDiskType")
    def reset_kubelet_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKubeletDiskType", []))

    @jsii.member(jsii_name="resetLinuxOsConfig")
    def reset_linux_os_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinuxOsConfig", []))

    @jsii.member(jsii_name="resetMaxCount")
    def reset_max_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxCount", []))

    @jsii.member(jsii_name="resetMaxPods")
    def reset_max_pods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxPods", []))

    @jsii.member(jsii_name="resetMessageOfTheDay")
    def reset_message_of_the_day(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageOfTheDay", []))

    @jsii.member(jsii_name="resetMinCount")
    def reset_min_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCount", []))

    @jsii.member(jsii_name="resetNodeCount")
    def reset_node_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeCount", []))

    @jsii.member(jsii_name="resetNodeLabels")
    def reset_node_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeLabels", []))

    @jsii.member(jsii_name="resetNodePublicIpPrefixId")
    def reset_node_public_ip_prefix_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodePublicIpPrefixId", []))

    @jsii.member(jsii_name="resetNodeTaints")
    def reset_node_taints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeTaints", []))

    @jsii.member(jsii_name="resetOnlyCriticalAddonsEnabled")
    def reset_only_critical_addons_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnlyCriticalAddonsEnabled", []))

    @jsii.member(jsii_name="resetOrchestratorVersion")
    def reset_orchestrator_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrchestratorVersion", []))

    @jsii.member(jsii_name="resetOsDiskSizeGb")
    def reset_os_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsDiskSizeGb", []))

    @jsii.member(jsii_name="resetOsDiskType")
    def reset_os_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsDiskType", []))

    @jsii.member(jsii_name="resetOsSku")
    def reset_os_sku(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsSku", []))

    @jsii.member(jsii_name="resetPodSubnetId")
    def reset_pod_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPodSubnetId", []))

    @jsii.member(jsii_name="resetProximityPlacementGroupId")
    def reset_proximity_placement_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProximityPlacementGroupId", []))

    @jsii.member(jsii_name="resetScaleDownMode")
    def reset_scale_down_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleDownMode", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetUltraSsdEnabled")
    def reset_ultra_ssd_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUltraSsdEnabled", []))

    @jsii.member(jsii_name="resetUpgradeSettings")
    def reset_upgrade_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpgradeSettings", []))

    @jsii.member(jsii_name="resetVnetSubnetId")
    def reset_vnet_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVnetSubnetId", []))

    @jsii.member(jsii_name="resetWorkloadRuntime")
    def reset_workload_runtime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkloadRuntime", []))

    @jsii.member(jsii_name="resetZones")
    def reset_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZones", []))

    @builtins.property
    @jsii.member(jsii_name="kubeletConfig")
    def kubelet_config(
        self,
    ) -> KubernetesClusterDefaultNodePoolKubeletConfigOutputReference:
        return typing.cast(KubernetesClusterDefaultNodePoolKubeletConfigOutputReference, jsii.get(self, "kubeletConfig"))

    @builtins.property
    @jsii.member(jsii_name="linuxOsConfig")
    def linux_os_config(
        self,
    ) -> KubernetesClusterDefaultNodePoolLinuxOsConfigOutputReference:
        return typing.cast(KubernetesClusterDefaultNodePoolLinuxOsConfigOutputReference, jsii.get(self, "linuxOsConfig"))

    @builtins.property
    @jsii.member(jsii_name="upgradeSettings")
    def upgrade_settings(
        self,
    ) -> "KubernetesClusterDefaultNodePoolUpgradeSettingsOutputReference":
        return typing.cast("KubernetesClusterDefaultNodePoolUpgradeSettingsOutputReference", jsii.get(self, "upgradeSettings"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationGroupIdInput")
    def capacity_reservation_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "capacityReservationGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAutoScalingInput")
    def enable_auto_scaling_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableAutoScalingInput"))

    @builtins.property
    @jsii.member(jsii_name="enableHostEncryptionInput")
    def enable_host_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableHostEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enableNodePublicIpInput")
    def enable_node_public_ip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableNodePublicIpInput"))

    @builtins.property
    @jsii.member(jsii_name="fipsEnabledInput")
    def fips_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fipsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="hostGroupIdInput")
    def host_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="kubeletConfigInput")
    def kubelet_config_input(
        self,
    ) -> typing.Optional[KubernetesClusterDefaultNodePoolKubeletConfig]:
        return typing.cast(typing.Optional[KubernetesClusterDefaultNodePoolKubeletConfig], jsii.get(self, "kubeletConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="kubeletDiskTypeInput")
    def kubelet_disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kubeletDiskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="linuxOsConfigInput")
    def linux_os_config_input(
        self,
    ) -> typing.Optional[KubernetesClusterDefaultNodePoolLinuxOsConfig]:
        return typing.cast(typing.Optional[KubernetesClusterDefaultNodePoolLinuxOsConfig], jsii.get(self, "linuxOsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="maxCountInput")
    def max_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxCountInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPodsInput")
    def max_pods_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxPodsInput"))

    @builtins.property
    @jsii.member(jsii_name="messageOfTheDayInput")
    def message_of_the_day_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageOfTheDayInput"))

    @builtins.property
    @jsii.member(jsii_name="minCountInput")
    def min_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minCountInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeCountInput")
    def node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeLabelsInput")
    def node_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "nodeLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="nodePublicIpPrefixIdInput")
    def node_public_ip_prefix_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodePublicIpPrefixIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeTaintsInput")
    def node_taints_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nodeTaintsInput"))

    @builtins.property
    @jsii.member(jsii_name="onlyCriticalAddonsEnabledInput")
    def only_critical_addons_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "onlyCriticalAddonsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="orchestratorVersionInput")
    def orchestrator_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "orchestratorVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="osDiskSizeGbInput")
    def os_disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "osDiskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="osDiskTypeInput")
    def os_disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osDiskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="osSkuInput")
    def os_sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osSkuInput"))

    @builtins.property
    @jsii.member(jsii_name="podSubnetIdInput")
    def pod_subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "podSubnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="proximityPlacementGroupIdInput")
    def proximity_placement_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proximityPlacementGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleDownModeInput")
    def scale_down_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scaleDownModeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="ultraSsdEnabledInput")
    def ultra_ssd_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ultraSsdEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="upgradeSettingsInput")
    def upgrade_settings_input(
        self,
    ) -> typing.Optional["KubernetesClusterDefaultNodePoolUpgradeSettings"]:
        return typing.cast(typing.Optional["KubernetesClusterDefaultNodePoolUpgradeSettings"], jsii.get(self, "upgradeSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="vmSizeInput")
    def vm_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="vnetSubnetIdInput")
    def vnet_subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vnetSubnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="workloadRuntimeInput")
    def workload_runtime_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workloadRuntimeInput"))

    @builtins.property
    @jsii.member(jsii_name="zonesInput")
    def zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "zonesInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationGroupId")
    def capacity_reservation_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityReservationGroupId"))

    @capacity_reservation_group_id.setter
    def capacity_reservation_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "capacity_reservation_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityReservationGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="enableAutoScaling")
    def enable_auto_scaling(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableAutoScaling"))

    @enable_auto_scaling.setter
    def enable_auto_scaling(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "enable_auto_scaling").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutoScaling", value)

    @builtins.property
    @jsii.member(jsii_name="enableHostEncryption")
    def enable_host_encryption(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableHostEncryption"))

    @enable_host_encryption.setter
    def enable_host_encryption(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "enable_host_encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableHostEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="enableNodePublicIp")
    def enable_node_public_ip(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableNodePublicIp"))

    @enable_node_public_ip.setter
    def enable_node_public_ip(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "enable_node_public_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableNodePublicIp", value)

    @builtins.property
    @jsii.member(jsii_name="fipsEnabled")
    def fips_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fipsEnabled"))

    @fips_enabled.setter
    def fips_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "fips_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fipsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="hostGroupId")
    def host_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostGroupId"))

    @host_group_id.setter
    def host_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "host_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="kubeletDiskType")
    def kubelet_disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kubeletDiskType"))

    @kubelet_disk_type.setter
    def kubelet_disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "kubelet_disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kubeletDiskType", value)

    @builtins.property
    @jsii.member(jsii_name="maxCount")
    def max_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxCount"))

    @max_count.setter
    def max_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "max_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCount", value)

    @builtins.property
    @jsii.member(jsii_name="maxPods")
    def max_pods(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPods"))

    @max_pods.setter
    def max_pods(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "max_pods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPods", value)

    @builtins.property
    @jsii.member(jsii_name="messageOfTheDay")
    def message_of_the_day(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageOfTheDay"))

    @message_of_the_day.setter
    def message_of_the_day(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "message_of_the_day").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageOfTheDay", value)

    @builtins.property
    @jsii.member(jsii_name="minCount")
    def min_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minCount"))

    @min_count.setter
    def min_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "min_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCount", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nodeCount")
    def node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nodeCount"))

    @node_count.setter
    def node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "node_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="nodeLabels")
    def node_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "nodeLabels"))

    @node_labels.setter
    def node_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "node_labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeLabels", value)

    @builtins.property
    @jsii.member(jsii_name="nodePublicIpPrefixId")
    def node_public_ip_prefix_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodePublicIpPrefixId"))

    @node_public_ip_prefix_id.setter
    def node_public_ip_prefix_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "node_public_ip_prefix_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodePublicIpPrefixId", value)

    @builtins.property
    @jsii.member(jsii_name="nodeTaints")
    def node_taints(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nodeTaints"))

    @node_taints.setter
    def node_taints(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "node_taints").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeTaints", value)

    @builtins.property
    @jsii.member(jsii_name="onlyCriticalAddonsEnabled")
    def only_critical_addons_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "onlyCriticalAddonsEnabled"))

    @only_critical_addons_enabled.setter
    def only_critical_addons_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "only_critical_addons_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onlyCriticalAddonsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="orchestratorVersion")
    def orchestrator_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "orchestratorVersion"))

    @orchestrator_version.setter
    def orchestrator_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "orchestrator_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "orchestratorVersion", value)

    @builtins.property
    @jsii.member(jsii_name="osDiskSizeGb")
    def os_disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "osDiskSizeGb"))

    @os_disk_size_gb.setter
    def os_disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "os_disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osDiskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="osDiskType")
    def os_disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "osDiskType"))

    @os_disk_type.setter
    def os_disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "os_disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osDiskType", value)

    @builtins.property
    @jsii.member(jsii_name="osSku")
    def os_sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "osSku"))

    @os_sku.setter
    def os_sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "os_sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osSku", value)

    @builtins.property
    @jsii.member(jsii_name="podSubnetId")
    def pod_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "podSubnetId"))

    @pod_subnet_id.setter
    def pod_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "pod_subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "podSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="proximityPlacementGroupId")
    def proximity_placement_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "proximityPlacementGroupId"))

    @proximity_placement_group_id.setter
    def proximity_placement_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "proximity_placement_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proximityPlacementGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="scaleDownMode")
    def scale_down_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleDownMode"))

    @scale_down_mode.setter
    def scale_down_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "scale_down_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleDownMode", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="ultraSsdEnabled")
    def ultra_ssd_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ultraSsdEnabled"))

    @ultra_ssd_enabled.setter
    def ultra_ssd_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "ultra_ssd_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ultraSsdEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="vmSize")
    def vm_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmSize"))

    @vm_size.setter
    def vm_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "vm_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmSize", value)

    @builtins.property
    @jsii.member(jsii_name="vnetSubnetId")
    def vnet_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vnetSubnetId"))

    @vnet_subnet_id.setter
    def vnet_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "vnet_subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vnetSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="workloadRuntime")
    def workload_runtime(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workloadRuntime"))

    @workload_runtime.setter
    def workload_runtime(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "workload_runtime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workloadRuntime", value)

    @builtins.property
    @jsii.member(jsii_name="zones")
    def zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "zones"))

    @zones.setter
    def zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "zones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zones", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterDefaultNodePool]:
        return typing.cast(typing.Optional[KubernetesClusterDefaultNodePool], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterDefaultNodePool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterDefaultNodePoolUpgradeSettings",
    jsii_struct_bases=[],
    name_mapping={"max_surge": "maxSurge"},
)
class KubernetesClusterDefaultNodePoolUpgradeSettings:
    def __init__(self, *, max_surge: builtins.str) -> None:
        '''
        :param max_surge: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_surge KubernetesCluster#max_surge}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterDefaultNodePoolUpgradeSettings.__init__)
            check_type(argname="argument max_surge", value=max_surge, expected_type=type_hints["max_surge"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_surge": max_surge,
        }

    @builtins.property
    def max_surge(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#max_surge KubernetesCluster#max_surge}.'''
        result = self._values.get("max_surge")
        assert result is not None, "Required property 'max_surge' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterDefaultNodePoolUpgradeSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterDefaultNodePoolUpgradeSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterDefaultNodePoolUpgradeSettingsOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterDefaultNodePoolUpgradeSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maxSurgeInput")
    def max_surge_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxSurgeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSurge")
    def max_surge(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxSurge"))

    @max_surge.setter
    def max_surge(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolUpgradeSettingsOutputReference, "max_surge").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSurge", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KubernetesClusterDefaultNodePoolUpgradeSettings]:
        return typing.cast(typing.Optional[KubernetesClusterDefaultNodePoolUpgradeSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterDefaultNodePoolUpgradeSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterDefaultNodePoolUpgradeSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterHttpProxyConfig",
    jsii_struct_bases=[],
    name_mapping={
        "http_proxy": "httpProxy",
        "https_proxy": "httpsProxy",
        "no_proxy": "noProxy",
        "trusted_ca": "trustedCa",
    },
)
class KubernetesClusterHttpProxyConfig:
    def __init__(
        self,
        *,
        http_proxy: typing.Optional[builtins.str] = None,
        https_proxy: typing.Optional[builtins.str] = None,
        no_proxy: typing.Optional[typing.Sequence[builtins.str]] = None,
        trusted_ca: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_proxy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#http_proxy KubernetesCluster#http_proxy}.
        :param https_proxy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#https_proxy KubernetesCluster#https_proxy}.
        :param no_proxy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#no_proxy KubernetesCluster#no_proxy}.
        :param trusted_ca: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#trusted_ca KubernetesCluster#trusted_ca}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterHttpProxyConfig.__init__)
            check_type(argname="argument http_proxy", value=http_proxy, expected_type=type_hints["http_proxy"])
            check_type(argname="argument https_proxy", value=https_proxy, expected_type=type_hints["https_proxy"])
            check_type(argname="argument no_proxy", value=no_proxy, expected_type=type_hints["no_proxy"])
            check_type(argname="argument trusted_ca", value=trusted_ca, expected_type=type_hints["trusted_ca"])
        self._values: typing.Dict[str, typing.Any] = {}
        if http_proxy is not None:
            self._values["http_proxy"] = http_proxy
        if https_proxy is not None:
            self._values["https_proxy"] = https_proxy
        if no_proxy is not None:
            self._values["no_proxy"] = no_proxy
        if trusted_ca is not None:
            self._values["trusted_ca"] = trusted_ca

    @builtins.property
    def http_proxy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#http_proxy KubernetesCluster#http_proxy}.'''
        result = self._values.get("http_proxy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def https_proxy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#https_proxy KubernetesCluster#https_proxy}.'''
        result = self._values.get("https_proxy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def no_proxy(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#no_proxy KubernetesCluster#no_proxy}.'''
        result = self._values.get("no_proxy")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def trusted_ca(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#trusted_ca KubernetesCluster#trusted_ca}.'''
        result = self._values.get("trusted_ca")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterHttpProxyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterHttpProxyConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterHttpProxyConfigOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterHttpProxyConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHttpProxy")
    def reset_http_proxy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpProxy", []))

    @jsii.member(jsii_name="resetHttpsProxy")
    def reset_https_proxy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpsProxy", []))

    @jsii.member(jsii_name="resetNoProxy")
    def reset_no_proxy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoProxy", []))

    @jsii.member(jsii_name="resetTrustedCa")
    def reset_trusted_ca(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustedCa", []))

    @builtins.property
    @jsii.member(jsii_name="httpProxyInput")
    def http_proxy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpProxyInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsProxyInput")
    def https_proxy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpsProxyInput"))

    @builtins.property
    @jsii.member(jsii_name="noProxyInput")
    def no_proxy_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "noProxyInput"))

    @builtins.property
    @jsii.member(jsii_name="trustedCaInput")
    def trusted_ca_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trustedCaInput"))

    @builtins.property
    @jsii.member(jsii_name="httpProxy")
    def http_proxy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpProxy"))

    @http_proxy.setter
    def http_proxy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterHttpProxyConfigOutputReference, "http_proxy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpProxy", value)

    @builtins.property
    @jsii.member(jsii_name="httpsProxy")
    def https_proxy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpsProxy"))

    @https_proxy.setter
    def https_proxy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterHttpProxyConfigOutputReference, "https_proxy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsProxy", value)

    @builtins.property
    @jsii.member(jsii_name="noProxy")
    def no_proxy(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "noProxy"))

    @no_proxy.setter
    def no_proxy(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterHttpProxyConfigOutputReference, "no_proxy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noProxy", value)

    @builtins.property
    @jsii.member(jsii_name="trustedCa")
    def trusted_ca(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trustedCa"))

    @trusted_ca.setter
    def trusted_ca(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterHttpProxyConfigOutputReference, "trusted_ca").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustedCa", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterHttpProxyConfig]:
        return typing.cast(typing.Optional[KubernetesClusterHttpProxyConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterHttpProxyConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterHttpProxyConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class KubernetesClusterIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#type KubernetesCluster#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#identity_ids KubernetesCluster#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#type KubernetesCluster#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#identity_ids KubernetesCluster#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterIdentityOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterIdentityOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(KubernetesClusterIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterIdentity]:
        return typing.cast(typing.Optional[KubernetesClusterIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[KubernetesClusterIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterIngressApplicationGateway",
    jsii_struct_bases=[],
    name_mapping={
        "gateway_id": "gatewayId",
        "gateway_name": "gatewayName",
        "subnet_cidr": "subnetCidr",
        "subnet_id": "subnetId",
    },
)
class KubernetesClusterIngressApplicationGateway:
    def __init__(
        self,
        *,
        gateway_id: typing.Optional[builtins.str] = None,
        gateway_name: typing.Optional[builtins.str] = None,
        subnet_cidr: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#gateway_id KubernetesCluster#gateway_id}.
        :param gateway_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#gateway_name KubernetesCluster#gateway_name}.
        :param subnet_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#subnet_cidr KubernetesCluster#subnet_cidr}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#subnet_id KubernetesCluster#subnet_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterIngressApplicationGateway.__init__)
            check_type(argname="argument gateway_id", value=gateway_id, expected_type=type_hints["gateway_id"])
            check_type(argname="argument gateway_name", value=gateway_name, expected_type=type_hints["gateway_name"])
            check_type(argname="argument subnet_cidr", value=subnet_cidr, expected_type=type_hints["subnet_cidr"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if gateway_id is not None:
            self._values["gateway_id"] = gateway_id
        if gateway_name is not None:
            self._values["gateway_name"] = gateway_name
        if subnet_cidr is not None:
            self._values["subnet_cidr"] = subnet_cidr
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id

    @builtins.property
    def gateway_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#gateway_id KubernetesCluster#gateway_id}.'''
        result = self._values.get("gateway_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gateway_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#gateway_name KubernetesCluster#gateway_name}.'''
        result = self._values.get("gateway_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#subnet_cidr KubernetesCluster#subnet_cidr}.'''
        result = self._values.get("subnet_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#subnet_id KubernetesCluster#subnet_id}.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterIngressApplicationGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentity",
    jsii_struct_bases=[],
    name_mapping={},
)
class KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentity:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentityList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentityList",
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
            type_hints = typing.get_type_hints(KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentityList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentityList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentityList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentityList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentityList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentityOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectId"))

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentityId")
    def user_assigned_identity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userAssignedIdentityId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentity]:
        return typing.cast(typing.Optional[KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterIngressApplicationGatewayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterIngressApplicationGatewayOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterIngressApplicationGatewayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGatewayId")
    def reset_gateway_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGatewayId", []))

    @jsii.member(jsii_name="resetGatewayName")
    def reset_gateway_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGatewayName", []))

    @jsii.member(jsii_name="resetSubnetCidr")
    def reset_subnet_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetCidr", []))

    @jsii.member(jsii_name="resetSubnetId")
    def reset_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetId", []))

    @builtins.property
    @jsii.member(jsii_name="effectiveGatewayId")
    def effective_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "effectiveGatewayId"))

    @builtins.property
    @jsii.member(jsii_name="ingressApplicationGatewayIdentity")
    def ingress_application_gateway_identity(
        self,
    ) -> KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentityList:
        return typing.cast(KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentityList, jsii.get(self, "ingressApplicationGatewayIdentity"))

    @builtins.property
    @jsii.member(jsii_name="gatewayIdInput")
    def gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayNameInput")
    def gateway_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetCidrInput")
    def subnet_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayId")
    def gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayId"))

    @gateway_id.setter
    def gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterIngressApplicationGatewayOutputReference, "gateway_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayId", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayName")
    def gateway_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayName"))

    @gateway_name.setter
    def gateway_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterIngressApplicationGatewayOutputReference, "gateway_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayName", value)

    @builtins.property
    @jsii.member(jsii_name="subnetCidr")
    def subnet_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetCidr"))

    @subnet_cidr.setter
    def subnet_cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterIngressApplicationGatewayOutputReference, "subnet_cidr").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetCidr", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterIngressApplicationGatewayOutputReference, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KubernetesClusterIngressApplicationGateway]:
        return typing.cast(typing.Optional[KubernetesClusterIngressApplicationGateway], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterIngressApplicationGateway],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterIngressApplicationGatewayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterKeyVaultSecretsProvider",
    jsii_struct_bases=[],
    name_mapping={
        "secret_rotation_enabled": "secretRotationEnabled",
        "secret_rotation_interval": "secretRotationInterval",
    },
)
class KubernetesClusterKeyVaultSecretsProvider:
    def __init__(
        self,
        *,
        secret_rotation_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        secret_rotation_interval: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param secret_rotation_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#secret_rotation_enabled KubernetesCluster#secret_rotation_enabled}.
        :param secret_rotation_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#secret_rotation_interval KubernetesCluster#secret_rotation_interval}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterKeyVaultSecretsProvider.__init__)
            check_type(argname="argument secret_rotation_enabled", value=secret_rotation_enabled, expected_type=type_hints["secret_rotation_enabled"])
            check_type(argname="argument secret_rotation_interval", value=secret_rotation_interval, expected_type=type_hints["secret_rotation_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if secret_rotation_enabled is not None:
            self._values["secret_rotation_enabled"] = secret_rotation_enabled
        if secret_rotation_interval is not None:
            self._values["secret_rotation_interval"] = secret_rotation_interval

    @builtins.property
    def secret_rotation_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#secret_rotation_enabled KubernetesCluster#secret_rotation_enabled}.'''
        result = self._values.get("secret_rotation_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def secret_rotation_interval(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#secret_rotation_interval KubernetesCluster#secret_rotation_interval}.'''
        result = self._values.get("secret_rotation_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterKeyVaultSecretsProvider(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterKeyVaultSecretsProviderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterKeyVaultSecretsProviderOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterKeyVaultSecretsProviderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSecretRotationEnabled")
    def reset_secret_rotation_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretRotationEnabled", []))

    @jsii.member(jsii_name="resetSecretRotationInterval")
    def reset_secret_rotation_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretRotationInterval", []))

    @builtins.property
    @jsii.member(jsii_name="secretIdentity")
    def secret_identity(
        self,
    ) -> "KubernetesClusterKeyVaultSecretsProviderSecretIdentityList":
        return typing.cast("KubernetesClusterKeyVaultSecretsProviderSecretIdentityList", jsii.get(self, "secretIdentity"))

    @builtins.property
    @jsii.member(jsii_name="secretRotationEnabledInput")
    def secret_rotation_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "secretRotationEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="secretRotationIntervalInput")
    def secret_rotation_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretRotationIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="secretRotationEnabled")
    def secret_rotation_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "secretRotationEnabled"))

    @secret_rotation_enabled.setter
    def secret_rotation_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKeyVaultSecretsProviderOutputReference, "secret_rotation_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretRotationEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="secretRotationInterval")
    def secret_rotation_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretRotationInterval"))

    @secret_rotation_interval.setter
    def secret_rotation_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKeyVaultSecretsProviderOutputReference, "secret_rotation_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretRotationInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KubernetesClusterKeyVaultSecretsProvider]:
        return typing.cast(typing.Optional[KubernetesClusterKeyVaultSecretsProvider], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterKeyVaultSecretsProvider],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKeyVaultSecretsProviderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterKeyVaultSecretsProviderSecretIdentity",
    jsii_struct_bases=[],
    name_mapping={},
)
class KubernetesClusterKeyVaultSecretsProviderSecretIdentity:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterKeyVaultSecretsProviderSecretIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterKeyVaultSecretsProviderSecretIdentityList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterKeyVaultSecretsProviderSecretIdentityList",
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
            type_hints = typing.get_type_hints(KubernetesClusterKeyVaultSecretsProviderSecretIdentityList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KubernetesClusterKeyVaultSecretsProviderSecretIdentityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterKeyVaultSecretsProviderSecretIdentityList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesClusterKeyVaultSecretsProviderSecretIdentityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKeyVaultSecretsProviderSecretIdentityList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKeyVaultSecretsProviderSecretIdentityList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKeyVaultSecretsProviderSecretIdentityList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class KubernetesClusterKeyVaultSecretsProviderSecretIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterKeyVaultSecretsProviderSecretIdentityOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterKeyVaultSecretsProviderSecretIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectId"))

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentityId")
    def user_assigned_identity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userAssignedIdentityId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KubernetesClusterKeyVaultSecretsProviderSecretIdentity]:
        return typing.cast(typing.Optional[KubernetesClusterKeyVaultSecretsProviderSecretIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterKeyVaultSecretsProviderSecretIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKeyVaultSecretsProviderSecretIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterKubeAdminConfig",
    jsii_struct_bases=[],
    name_mapping={},
)
class KubernetesClusterKubeAdminConfig:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterKubeAdminConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterKubeAdminConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterKubeAdminConfigList",
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
            type_hints = typing.get_type_hints(KubernetesClusterKubeAdminConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KubernetesClusterKubeAdminConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterKubeAdminConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesClusterKubeAdminConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKubeAdminConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKubeAdminConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKubeAdminConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class KubernetesClusterKubeAdminConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterKubeAdminConfigOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterKubeAdminConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="clientCertificate")
    def client_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCertificate"))

    @builtins.property
    @jsii.member(jsii_name="clientKey")
    def client_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientKey"))

    @builtins.property
    @jsii.member(jsii_name="clusterCaCertificate")
    def cluster_ca_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterCaCertificate"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterKubeAdminConfig]:
        return typing.cast(typing.Optional[KubernetesClusterKubeAdminConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterKubeAdminConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKubeAdminConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterKubeConfig",
    jsii_struct_bases=[],
    name_mapping={},
)
class KubernetesClusterKubeConfig:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterKubeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterKubeConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterKubeConfigList",
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
            type_hints = typing.get_type_hints(KubernetesClusterKubeConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "KubernetesClusterKubeConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterKubeConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesClusterKubeConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKubeConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKubeConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKubeConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class KubernetesClusterKubeConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterKubeConfigOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterKubeConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="clientCertificate")
    def client_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCertificate"))

    @builtins.property
    @jsii.member(jsii_name="clientKey")
    def client_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientKey"))

    @builtins.property
    @jsii.member(jsii_name="clusterCaCertificate")
    def cluster_ca_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterCaCertificate"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterKubeConfig]:
        return typing.cast(typing.Optional[KubernetesClusterKubeConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterKubeConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKubeConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterKubeletIdentity",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "object_id": "objectId",
        "user_assigned_identity_id": "userAssignedIdentityId",
    },
)
class KubernetesClusterKubeletIdentity:
    def __init__(
        self,
        *,
        client_id: typing.Optional[builtins.str] = None,
        object_id: typing.Optional[builtins.str] = None,
        user_assigned_identity_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#client_id KubernetesCluster#client_id}.
        :param object_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#object_id KubernetesCluster#object_id}.
        :param user_assigned_identity_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#user_assigned_identity_id KubernetesCluster#user_assigned_identity_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterKubeletIdentity.__init__)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument object_id", value=object_id, expected_type=type_hints["object_id"])
            check_type(argname="argument user_assigned_identity_id", value=user_assigned_identity_id, expected_type=type_hints["user_assigned_identity_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if client_id is not None:
            self._values["client_id"] = client_id
        if object_id is not None:
            self._values["object_id"] = object_id
        if user_assigned_identity_id is not None:
            self._values["user_assigned_identity_id"] = user_assigned_identity_id

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#client_id KubernetesCluster#client_id}.'''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#object_id KubernetesCluster#object_id}.'''
        result = self._values.get("object_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_assigned_identity_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#user_assigned_identity_id KubernetesCluster#user_assigned_identity_id}.'''
        result = self._values.get("user_assigned_identity_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterKubeletIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterKubeletIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterKubeletIdentityOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterKubeletIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetObjectId")
    def reset_object_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectId", []))

    @jsii.member(jsii_name="resetUserAssignedIdentityId")
    def reset_user_assigned_identity_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserAssignedIdentityId", []))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="objectIdInput")
    def object_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentityIdInput")
    def user_assigned_identity_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userAssignedIdentityIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKubeletIdentityOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectId"))

    @object_id.setter
    def object_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKubeletIdentityOutputReference, "object_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectId", value)

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentityId")
    def user_assigned_identity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userAssignedIdentityId"))

    @user_assigned_identity_id.setter
    def user_assigned_identity_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKubeletIdentityOutputReference, "user_assigned_identity_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userAssignedIdentityId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterKubeletIdentity]:
        return typing.cast(typing.Optional[KubernetesClusterKubeletIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterKubeletIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterKubeletIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterLinuxProfile",
    jsii_struct_bases=[],
    name_mapping={"admin_username": "adminUsername", "ssh_key": "sshKey"},
)
class KubernetesClusterLinuxProfile:
    def __init__(
        self,
        *,
        admin_username: builtins.str,
        ssh_key: typing.Union["KubernetesClusterLinuxProfileSshKey", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#admin_username KubernetesCluster#admin_username}.
        :param ssh_key: ssh_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#ssh_key KubernetesCluster#ssh_key}
        '''
        if isinstance(ssh_key, dict):
            ssh_key = KubernetesClusterLinuxProfileSshKey(**ssh_key)
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterLinuxProfile.__init__)
            check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
            check_type(argname="argument ssh_key", value=ssh_key, expected_type=type_hints["ssh_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "admin_username": admin_username,
            "ssh_key": ssh_key,
        }

    @builtins.property
    def admin_username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#admin_username KubernetesCluster#admin_username}.'''
        result = self._values.get("admin_username")
        assert result is not None, "Required property 'admin_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ssh_key(self) -> "KubernetesClusterLinuxProfileSshKey":
        '''ssh_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#ssh_key KubernetesCluster#ssh_key}
        '''
        result = self._values.get("ssh_key")
        assert result is not None, "Required property 'ssh_key' is missing"
        return typing.cast("KubernetesClusterLinuxProfileSshKey", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterLinuxProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterLinuxProfileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterLinuxProfileOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterLinuxProfileOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSshKey")
    def put_ssh_key(self, *, key_data: builtins.str) -> None:
        '''
        :param key_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#key_data KubernetesCluster#key_data}.
        '''
        value = KubernetesClusterLinuxProfileSshKey(key_data=key_data)

        return typing.cast(None, jsii.invoke(self, "putSshKey", [value]))

    @builtins.property
    @jsii.member(jsii_name="sshKey")
    def ssh_key(self) -> "KubernetesClusterLinuxProfileSshKeyOutputReference":
        return typing.cast("KubernetesClusterLinuxProfileSshKeyOutputReference", jsii.get(self, "sshKey"))

    @builtins.property
    @jsii.member(jsii_name="adminUsernameInput")
    def admin_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="sshKeyInput")
    def ssh_key_input(self) -> typing.Optional["KubernetesClusterLinuxProfileSshKey"]:
        return typing.cast(typing.Optional["KubernetesClusterLinuxProfileSshKey"], jsii.get(self, "sshKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="adminUsername")
    def admin_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminUsername"))

    @admin_username.setter
    def admin_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterLinuxProfileOutputReference, "admin_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUsername", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterLinuxProfile]:
        return typing.cast(typing.Optional[KubernetesClusterLinuxProfile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterLinuxProfile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterLinuxProfileOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterLinuxProfileSshKey",
    jsii_struct_bases=[],
    name_mapping={"key_data": "keyData"},
)
class KubernetesClusterLinuxProfileSshKey:
    def __init__(self, *, key_data: builtins.str) -> None:
        '''
        :param key_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#key_data KubernetesCluster#key_data}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterLinuxProfileSshKey.__init__)
            check_type(argname="argument key_data", value=key_data, expected_type=type_hints["key_data"])
        self._values: typing.Dict[str, typing.Any] = {
            "key_data": key_data,
        }

    @builtins.property
    def key_data(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#key_data KubernetesCluster#key_data}.'''
        result = self._values.get("key_data")
        assert result is not None, "Required property 'key_data' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterLinuxProfileSshKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterLinuxProfileSshKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterLinuxProfileSshKeyOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterLinuxProfileSshKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="keyDataInput")
    def key_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyDataInput"))

    @builtins.property
    @jsii.member(jsii_name="keyData")
    def key_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyData"))

    @key_data.setter
    def key_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterLinuxProfileSshKeyOutputReference, "key_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyData", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterLinuxProfileSshKey]:
        return typing.cast(typing.Optional[KubernetesClusterLinuxProfileSshKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterLinuxProfileSshKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterLinuxProfileSshKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterMaintenanceWindow",
    jsii_struct_bases=[],
    name_mapping={"allowed": "allowed", "not_allowed": "notAllowed"},
)
class KubernetesClusterMaintenanceWindow:
    def __init__(
        self,
        *,
        allowed: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KubernetesClusterMaintenanceWindowAllowed", typing.Dict[str, typing.Any]]]]] = None,
        not_allowed: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KubernetesClusterMaintenanceWindowNotAllowed", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param allowed: allowed block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#allowed KubernetesCluster#allowed}
        :param not_allowed: not_allowed block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#not_allowed KubernetesCluster#not_allowed}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterMaintenanceWindow.__init__)
            check_type(argname="argument allowed", value=allowed, expected_type=type_hints["allowed"])
            check_type(argname="argument not_allowed", value=not_allowed, expected_type=type_hints["not_allowed"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed is not None:
            self._values["allowed"] = allowed
        if not_allowed is not None:
            self._values["not_allowed"] = not_allowed

    @builtins.property
    def allowed(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KubernetesClusterMaintenanceWindowAllowed"]]]:
        '''allowed block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#allowed KubernetesCluster#allowed}
        '''
        result = self._values.get("allowed")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KubernetesClusterMaintenanceWindowAllowed"]]], result)

    @builtins.property
    def not_allowed(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KubernetesClusterMaintenanceWindowNotAllowed"]]]:
        '''not_allowed block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#not_allowed KubernetesCluster#not_allowed}
        '''
        result = self._values.get("not_allowed")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KubernetesClusterMaintenanceWindowNotAllowed"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterMaintenanceWindow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterMaintenanceWindowAllowed",
    jsii_struct_bases=[],
    name_mapping={"day": "day", "hours": "hours"},
)
class KubernetesClusterMaintenanceWindowAllowed:
    def __init__(
        self,
        *,
        day: builtins.str,
        hours: typing.Sequence[jsii.Number],
    ) -> None:
        '''
        :param day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#day KubernetesCluster#day}.
        :param hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#hours KubernetesCluster#hours}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterMaintenanceWindowAllowed.__init__)
            check_type(argname="argument day", value=day, expected_type=type_hints["day"])
            check_type(argname="argument hours", value=hours, expected_type=type_hints["hours"])
        self._values: typing.Dict[str, typing.Any] = {
            "day": day,
            "hours": hours,
        }

    @builtins.property
    def day(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#day KubernetesCluster#day}.'''
        result = self._values.get("day")
        assert result is not None, "Required property 'day' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hours(self) -> typing.List[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#hours KubernetesCluster#hours}.'''
        result = self._values.get("hours")
        assert result is not None, "Required property 'hours' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterMaintenanceWindowAllowed(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterMaintenanceWindowAllowedList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterMaintenanceWindowAllowedList",
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
            type_hints = typing.get_type_hints(KubernetesClusterMaintenanceWindowAllowedList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KubernetesClusterMaintenanceWindowAllowedOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterMaintenanceWindowAllowedList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesClusterMaintenanceWindowAllowedOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterMaintenanceWindowAllowedList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(KubernetesClusterMaintenanceWindowAllowedList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(KubernetesClusterMaintenanceWindowAllowedList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KubernetesClusterMaintenanceWindowAllowed]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KubernetesClusterMaintenanceWindowAllowed]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KubernetesClusterMaintenanceWindowAllowed]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterMaintenanceWindowAllowedList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterMaintenanceWindowAllowedOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterMaintenanceWindowAllowedOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterMaintenanceWindowAllowedOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="dayInput")
    def day_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayInput"))

    @builtins.property
    @jsii.member(jsii_name="hoursInput")
    def hours_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "hoursInput"))

    @builtins.property
    @jsii.member(jsii_name="day")
    def day(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "day"))

    @day.setter
    def day(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterMaintenanceWindowAllowedOutputReference, "day").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "day", value)

    @builtins.property
    @jsii.member(jsii_name="hours")
    def hours(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "hours"))

    @hours.setter
    def hours(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterMaintenanceWindowAllowedOutputReference, "hours").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hours", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KubernetesClusterMaintenanceWindowAllowed, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KubernetesClusterMaintenanceWindowAllowed, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KubernetesClusterMaintenanceWindowAllowed, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterMaintenanceWindowAllowedOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterMaintenanceWindowNotAllowed",
    jsii_struct_bases=[],
    name_mapping={"end": "end", "start": "start"},
)
class KubernetesClusterMaintenanceWindowNotAllowed:
    def __init__(self, *, end: builtins.str, start: builtins.str) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#end KubernetesCluster#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#start KubernetesCluster#start}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterMaintenanceWindowNotAllowed.__init__)
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
        self._values: typing.Dict[str, typing.Any] = {
            "end": end,
            "start": start,
        }

    @builtins.property
    def end(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#end KubernetesCluster#end}.'''
        result = self._values.get("end")
        assert result is not None, "Required property 'end' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def start(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#start KubernetesCluster#start}.'''
        result = self._values.get("start")
        assert result is not None, "Required property 'start' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterMaintenanceWindowNotAllowed(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterMaintenanceWindowNotAllowedList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterMaintenanceWindowNotAllowedList",
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
            type_hints = typing.get_type_hints(KubernetesClusterMaintenanceWindowNotAllowedList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KubernetesClusterMaintenanceWindowNotAllowedOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterMaintenanceWindowNotAllowedList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesClusterMaintenanceWindowNotAllowedOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterMaintenanceWindowNotAllowedList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(KubernetesClusterMaintenanceWindowNotAllowedList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(KubernetesClusterMaintenanceWindowNotAllowedList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KubernetesClusterMaintenanceWindowNotAllowed]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KubernetesClusterMaintenanceWindowNotAllowed]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KubernetesClusterMaintenanceWindowNotAllowed]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterMaintenanceWindowNotAllowedList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterMaintenanceWindowNotAllowedOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterMaintenanceWindowNotAllowedOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterMaintenanceWindowNotAllowedOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="endInput")
    def end_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startInput"))

    @builtins.property
    @jsii.member(jsii_name="end")
    def end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "end"))

    @end.setter
    def end(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterMaintenanceWindowNotAllowedOutputReference, "end").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "end", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "start"))

    @start.setter
    def start(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterMaintenanceWindowNotAllowedOutputReference, "start").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KubernetesClusterMaintenanceWindowNotAllowed, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KubernetesClusterMaintenanceWindowNotAllowed, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KubernetesClusterMaintenanceWindowNotAllowed, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterMaintenanceWindowNotAllowedOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterMaintenanceWindowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterMaintenanceWindowOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterMaintenanceWindowOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAllowed")
    def put_allowed(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KubernetesClusterMaintenanceWindowAllowed, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterMaintenanceWindowOutputReference.put_allowed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAllowed", [value]))

    @jsii.member(jsii_name="putNotAllowed")
    def put_not_allowed(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KubernetesClusterMaintenanceWindowNotAllowed, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterMaintenanceWindowOutputReference.put_not_allowed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNotAllowed", [value]))

    @jsii.member(jsii_name="resetAllowed")
    def reset_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowed", []))

    @jsii.member(jsii_name="resetNotAllowed")
    def reset_not_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotAllowed", []))

    @builtins.property
    @jsii.member(jsii_name="allowed")
    def allowed(self) -> KubernetesClusterMaintenanceWindowAllowedList:
        return typing.cast(KubernetesClusterMaintenanceWindowAllowedList, jsii.get(self, "allowed"))

    @builtins.property
    @jsii.member(jsii_name="notAllowed")
    def not_allowed(self) -> KubernetesClusterMaintenanceWindowNotAllowedList:
        return typing.cast(KubernetesClusterMaintenanceWindowNotAllowedList, jsii.get(self, "notAllowed"))

    @builtins.property
    @jsii.member(jsii_name="allowedInput")
    def allowed_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KubernetesClusterMaintenanceWindowAllowed]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KubernetesClusterMaintenanceWindowAllowed]]], jsii.get(self, "allowedInput"))

    @builtins.property
    @jsii.member(jsii_name="notAllowedInput")
    def not_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KubernetesClusterMaintenanceWindowNotAllowed]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KubernetesClusterMaintenanceWindowNotAllowed]]], jsii.get(self, "notAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterMaintenanceWindow]:
        return typing.cast(typing.Optional[KubernetesClusterMaintenanceWindow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterMaintenanceWindow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterMaintenanceWindowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterMicrosoftDefender",
    jsii_struct_bases=[],
    name_mapping={"log_analytics_workspace_id": "logAnalyticsWorkspaceId"},
)
class KubernetesClusterMicrosoftDefender:
    def __init__(self, *, log_analytics_workspace_id: builtins.str) -> None:
        '''
        :param log_analytics_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#log_analytics_workspace_id KubernetesCluster#log_analytics_workspace_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterMicrosoftDefender.__init__)
            check_type(argname="argument log_analytics_workspace_id", value=log_analytics_workspace_id, expected_type=type_hints["log_analytics_workspace_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "log_analytics_workspace_id": log_analytics_workspace_id,
        }

    @builtins.property
    def log_analytics_workspace_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#log_analytics_workspace_id KubernetesCluster#log_analytics_workspace_id}.'''
        result = self._values.get("log_analytics_workspace_id")
        assert result is not None, "Required property 'log_analytics_workspace_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterMicrosoftDefender(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterMicrosoftDefenderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterMicrosoftDefenderOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterMicrosoftDefenderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="logAnalyticsWorkspaceIdInput")
    def log_analytics_workspace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logAnalyticsWorkspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logAnalyticsWorkspaceId"))

    @log_analytics_workspace_id.setter
    def log_analytics_workspace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterMicrosoftDefenderOutputReference, "log_analytics_workspace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logAnalyticsWorkspaceId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterMicrosoftDefender]:
        return typing.cast(typing.Optional[KubernetesClusterMicrosoftDefender], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterMicrosoftDefender],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterMicrosoftDefenderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterNetworkProfile",
    jsii_struct_bases=[],
    name_mapping={
        "network_plugin": "networkPlugin",
        "dns_service_ip": "dnsServiceIp",
        "docker_bridge_cidr": "dockerBridgeCidr",
        "ip_versions": "ipVersions",
        "load_balancer_profile": "loadBalancerProfile",
        "load_balancer_sku": "loadBalancerSku",
        "nat_gateway_profile": "natGatewayProfile",
        "network_mode": "networkMode",
        "network_policy": "networkPolicy",
        "outbound_type": "outboundType",
        "pod_cidr": "podCidr",
        "pod_cidrs": "podCidrs",
        "service_cidr": "serviceCidr",
        "service_cidrs": "serviceCidrs",
    },
)
class KubernetesClusterNetworkProfile:
    def __init__(
        self,
        *,
        network_plugin: builtins.str,
        dns_service_ip: typing.Optional[builtins.str] = None,
        docker_bridge_cidr: typing.Optional[builtins.str] = None,
        ip_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        load_balancer_profile: typing.Optional[typing.Union["KubernetesClusterNetworkProfileLoadBalancerProfile", typing.Dict[str, typing.Any]]] = None,
        load_balancer_sku: typing.Optional[builtins.str] = None,
        nat_gateway_profile: typing.Optional[typing.Union["KubernetesClusterNetworkProfileNatGatewayProfile", typing.Dict[str, typing.Any]]] = None,
        network_mode: typing.Optional[builtins.str] = None,
        network_policy: typing.Optional[builtins.str] = None,
        outbound_type: typing.Optional[builtins.str] = None,
        pod_cidr: typing.Optional[builtins.str] = None,
        pod_cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_cidr: typing.Optional[builtins.str] = None,
        service_cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param network_plugin: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#network_plugin KubernetesCluster#network_plugin}.
        :param dns_service_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#dns_service_ip KubernetesCluster#dns_service_ip}.
        :param docker_bridge_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#docker_bridge_cidr KubernetesCluster#docker_bridge_cidr}.
        :param ip_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#ip_versions KubernetesCluster#ip_versions}.
        :param load_balancer_profile: load_balancer_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#load_balancer_profile KubernetesCluster#load_balancer_profile}
        :param load_balancer_sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#load_balancer_sku KubernetesCluster#load_balancer_sku}.
        :param nat_gateway_profile: nat_gateway_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#nat_gateway_profile KubernetesCluster#nat_gateway_profile}
        :param network_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#network_mode KubernetesCluster#network_mode}.
        :param network_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#network_policy KubernetesCluster#network_policy}.
        :param outbound_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#outbound_type KubernetesCluster#outbound_type}.
        :param pod_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#pod_cidr KubernetesCluster#pod_cidr}.
        :param pod_cidrs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#pod_cidrs KubernetesCluster#pod_cidrs}.
        :param service_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#service_cidr KubernetesCluster#service_cidr}.
        :param service_cidrs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#service_cidrs KubernetesCluster#service_cidrs}.
        '''
        if isinstance(load_balancer_profile, dict):
            load_balancer_profile = KubernetesClusterNetworkProfileLoadBalancerProfile(**load_balancer_profile)
        if isinstance(nat_gateway_profile, dict):
            nat_gateway_profile = KubernetesClusterNetworkProfileNatGatewayProfile(**nat_gateway_profile)
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterNetworkProfile.__init__)
            check_type(argname="argument network_plugin", value=network_plugin, expected_type=type_hints["network_plugin"])
            check_type(argname="argument dns_service_ip", value=dns_service_ip, expected_type=type_hints["dns_service_ip"])
            check_type(argname="argument docker_bridge_cidr", value=docker_bridge_cidr, expected_type=type_hints["docker_bridge_cidr"])
            check_type(argname="argument ip_versions", value=ip_versions, expected_type=type_hints["ip_versions"])
            check_type(argname="argument load_balancer_profile", value=load_balancer_profile, expected_type=type_hints["load_balancer_profile"])
            check_type(argname="argument load_balancer_sku", value=load_balancer_sku, expected_type=type_hints["load_balancer_sku"])
            check_type(argname="argument nat_gateway_profile", value=nat_gateway_profile, expected_type=type_hints["nat_gateway_profile"])
            check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
            check_type(argname="argument network_policy", value=network_policy, expected_type=type_hints["network_policy"])
            check_type(argname="argument outbound_type", value=outbound_type, expected_type=type_hints["outbound_type"])
            check_type(argname="argument pod_cidr", value=pod_cidr, expected_type=type_hints["pod_cidr"])
            check_type(argname="argument pod_cidrs", value=pod_cidrs, expected_type=type_hints["pod_cidrs"])
            check_type(argname="argument service_cidr", value=service_cidr, expected_type=type_hints["service_cidr"])
            check_type(argname="argument service_cidrs", value=service_cidrs, expected_type=type_hints["service_cidrs"])
        self._values: typing.Dict[str, typing.Any] = {
            "network_plugin": network_plugin,
        }
        if dns_service_ip is not None:
            self._values["dns_service_ip"] = dns_service_ip
        if docker_bridge_cidr is not None:
            self._values["docker_bridge_cidr"] = docker_bridge_cidr
        if ip_versions is not None:
            self._values["ip_versions"] = ip_versions
        if load_balancer_profile is not None:
            self._values["load_balancer_profile"] = load_balancer_profile
        if load_balancer_sku is not None:
            self._values["load_balancer_sku"] = load_balancer_sku
        if nat_gateway_profile is not None:
            self._values["nat_gateway_profile"] = nat_gateway_profile
        if network_mode is not None:
            self._values["network_mode"] = network_mode
        if network_policy is not None:
            self._values["network_policy"] = network_policy
        if outbound_type is not None:
            self._values["outbound_type"] = outbound_type
        if pod_cidr is not None:
            self._values["pod_cidr"] = pod_cidr
        if pod_cidrs is not None:
            self._values["pod_cidrs"] = pod_cidrs
        if service_cidr is not None:
            self._values["service_cidr"] = service_cidr
        if service_cidrs is not None:
            self._values["service_cidrs"] = service_cidrs

    @builtins.property
    def network_plugin(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#network_plugin KubernetesCluster#network_plugin}.'''
        result = self._values.get("network_plugin")
        assert result is not None, "Required property 'network_plugin' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dns_service_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#dns_service_ip KubernetesCluster#dns_service_ip}.'''
        result = self._values.get("dns_service_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_bridge_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#docker_bridge_cidr KubernetesCluster#docker_bridge_cidr}.'''
        result = self._values.get("docker_bridge_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#ip_versions KubernetesCluster#ip_versions}.'''
        result = self._values.get("ip_versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def load_balancer_profile(
        self,
    ) -> typing.Optional["KubernetesClusterNetworkProfileLoadBalancerProfile"]:
        '''load_balancer_profile block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#load_balancer_profile KubernetesCluster#load_balancer_profile}
        '''
        result = self._values.get("load_balancer_profile")
        return typing.cast(typing.Optional["KubernetesClusterNetworkProfileLoadBalancerProfile"], result)

    @builtins.property
    def load_balancer_sku(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#load_balancer_sku KubernetesCluster#load_balancer_sku}.'''
        result = self._values.get("load_balancer_sku")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nat_gateway_profile(
        self,
    ) -> typing.Optional["KubernetesClusterNetworkProfileNatGatewayProfile"]:
        '''nat_gateway_profile block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#nat_gateway_profile KubernetesCluster#nat_gateway_profile}
        '''
        result = self._values.get("nat_gateway_profile")
        return typing.cast(typing.Optional["KubernetesClusterNetworkProfileNatGatewayProfile"], result)

    @builtins.property
    def network_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#network_mode KubernetesCluster#network_mode}.'''
        result = self._values.get("network_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#network_policy KubernetesCluster#network_policy}.'''
        result = self._values.get("network_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def outbound_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#outbound_type KubernetesCluster#outbound_type}.'''
        result = self._values.get("outbound_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pod_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#pod_cidr KubernetesCluster#pod_cidr}.'''
        result = self._values.get("pod_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pod_cidrs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#pod_cidrs KubernetesCluster#pod_cidrs}.'''
        result = self._values.get("pod_cidrs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def service_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#service_cidr KubernetesCluster#service_cidr}.'''
        result = self._values.get("service_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_cidrs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#service_cidrs KubernetesCluster#service_cidrs}.'''
        result = self._values.get("service_cidrs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterNetworkProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterNetworkProfileLoadBalancerProfile",
    jsii_struct_bases=[],
    name_mapping={
        "idle_timeout_in_minutes": "idleTimeoutInMinutes",
        "managed_outbound_ip_count": "managedOutboundIpCount",
        "managed_outbound_ipv6_count": "managedOutboundIpv6Count",
        "outbound_ip_address_ids": "outboundIpAddressIds",
        "outbound_ip_prefix_ids": "outboundIpPrefixIds",
        "outbound_ports_allocated": "outboundPortsAllocated",
    },
)
class KubernetesClusterNetworkProfileLoadBalancerProfile:
    def __init__(
        self,
        *,
        idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        managed_outbound_ip_count: typing.Optional[jsii.Number] = None,
        managed_outbound_ipv6_count: typing.Optional[jsii.Number] = None,
        outbound_ip_address_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        outbound_ip_prefix_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        outbound_ports_allocated: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#idle_timeout_in_minutes KubernetesCluster#idle_timeout_in_minutes}.
        :param managed_outbound_ip_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#managed_outbound_ip_count KubernetesCluster#managed_outbound_ip_count}.
        :param managed_outbound_ipv6_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#managed_outbound_ipv6_count KubernetesCluster#managed_outbound_ipv6_count}.
        :param outbound_ip_address_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#outbound_ip_address_ids KubernetesCluster#outbound_ip_address_ids}.
        :param outbound_ip_prefix_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#outbound_ip_prefix_ids KubernetesCluster#outbound_ip_prefix_ids}.
        :param outbound_ports_allocated: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#outbound_ports_allocated KubernetesCluster#outbound_ports_allocated}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterNetworkProfileLoadBalancerProfile.__init__)
            check_type(argname="argument idle_timeout_in_minutes", value=idle_timeout_in_minutes, expected_type=type_hints["idle_timeout_in_minutes"])
            check_type(argname="argument managed_outbound_ip_count", value=managed_outbound_ip_count, expected_type=type_hints["managed_outbound_ip_count"])
            check_type(argname="argument managed_outbound_ipv6_count", value=managed_outbound_ipv6_count, expected_type=type_hints["managed_outbound_ipv6_count"])
            check_type(argname="argument outbound_ip_address_ids", value=outbound_ip_address_ids, expected_type=type_hints["outbound_ip_address_ids"])
            check_type(argname="argument outbound_ip_prefix_ids", value=outbound_ip_prefix_ids, expected_type=type_hints["outbound_ip_prefix_ids"])
            check_type(argname="argument outbound_ports_allocated", value=outbound_ports_allocated, expected_type=type_hints["outbound_ports_allocated"])
        self._values: typing.Dict[str, typing.Any] = {}
        if idle_timeout_in_minutes is not None:
            self._values["idle_timeout_in_minutes"] = idle_timeout_in_minutes
        if managed_outbound_ip_count is not None:
            self._values["managed_outbound_ip_count"] = managed_outbound_ip_count
        if managed_outbound_ipv6_count is not None:
            self._values["managed_outbound_ipv6_count"] = managed_outbound_ipv6_count
        if outbound_ip_address_ids is not None:
            self._values["outbound_ip_address_ids"] = outbound_ip_address_ids
        if outbound_ip_prefix_ids is not None:
            self._values["outbound_ip_prefix_ids"] = outbound_ip_prefix_ids
        if outbound_ports_allocated is not None:
            self._values["outbound_ports_allocated"] = outbound_ports_allocated

    @builtins.property
    def idle_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#idle_timeout_in_minutes KubernetesCluster#idle_timeout_in_minutes}.'''
        result = self._values.get("idle_timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def managed_outbound_ip_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#managed_outbound_ip_count KubernetesCluster#managed_outbound_ip_count}.'''
        result = self._values.get("managed_outbound_ip_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def managed_outbound_ipv6_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#managed_outbound_ipv6_count KubernetesCluster#managed_outbound_ipv6_count}.'''
        result = self._values.get("managed_outbound_ipv6_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def outbound_ip_address_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#outbound_ip_address_ids KubernetesCluster#outbound_ip_address_ids}.'''
        result = self._values.get("outbound_ip_address_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def outbound_ip_prefix_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#outbound_ip_prefix_ids KubernetesCluster#outbound_ip_prefix_ids}.'''
        result = self._values.get("outbound_ip_prefix_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def outbound_ports_allocated(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#outbound_ports_allocated KubernetesCluster#outbound_ports_allocated}.'''
        result = self._values.get("outbound_ports_allocated")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterNetworkProfileLoadBalancerProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterNetworkProfileLoadBalancerProfileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterNetworkProfileLoadBalancerProfileOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterNetworkProfileLoadBalancerProfileOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdleTimeoutInMinutes")
    def reset_idle_timeout_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleTimeoutInMinutes", []))

    @jsii.member(jsii_name="resetManagedOutboundIpCount")
    def reset_managed_outbound_ip_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedOutboundIpCount", []))

    @jsii.member(jsii_name="resetManagedOutboundIpv6Count")
    def reset_managed_outbound_ipv6_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedOutboundIpv6Count", []))

    @jsii.member(jsii_name="resetOutboundIpAddressIds")
    def reset_outbound_ip_address_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutboundIpAddressIds", []))

    @jsii.member(jsii_name="resetOutboundIpPrefixIds")
    def reset_outbound_ip_prefix_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutboundIpPrefixIds", []))

    @jsii.member(jsii_name="resetOutboundPortsAllocated")
    def reset_outbound_ports_allocated(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutboundPortsAllocated", []))

    @builtins.property
    @jsii.member(jsii_name="effectiveOutboundIps")
    def effective_outbound_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "effectiveOutboundIps"))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInMinutesInput")
    def idle_timeout_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleTimeoutInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="managedOutboundIpCountInput")
    def managed_outbound_ip_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "managedOutboundIpCountInput"))

    @builtins.property
    @jsii.member(jsii_name="managedOutboundIpv6CountInput")
    def managed_outbound_ipv6_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "managedOutboundIpv6CountInput"))

    @builtins.property
    @jsii.member(jsii_name="outboundIpAddressIdsInput")
    def outbound_ip_address_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "outboundIpAddressIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="outboundIpPrefixIdsInput")
    def outbound_ip_prefix_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "outboundIpPrefixIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="outboundPortsAllocatedInput")
    def outbound_ports_allocated_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "outboundPortsAllocatedInput"))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleTimeoutInMinutes"))

    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileLoadBalancerProfileOutputReference, "idle_timeout_in_minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleTimeoutInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="managedOutboundIpCount")
    def managed_outbound_ip_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "managedOutboundIpCount"))

    @managed_outbound_ip_count.setter
    def managed_outbound_ip_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileLoadBalancerProfileOutputReference, "managed_outbound_ip_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedOutboundIpCount", value)

    @builtins.property
    @jsii.member(jsii_name="managedOutboundIpv6Count")
    def managed_outbound_ipv6_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "managedOutboundIpv6Count"))

    @managed_outbound_ipv6_count.setter
    def managed_outbound_ipv6_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileLoadBalancerProfileOutputReference, "managed_outbound_ipv6_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedOutboundIpv6Count", value)

    @builtins.property
    @jsii.member(jsii_name="outboundIpAddressIds")
    def outbound_ip_address_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "outboundIpAddressIds"))

    @outbound_ip_address_ids.setter
    def outbound_ip_address_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileLoadBalancerProfileOutputReference, "outbound_ip_address_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outboundIpAddressIds", value)

    @builtins.property
    @jsii.member(jsii_name="outboundIpPrefixIds")
    def outbound_ip_prefix_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "outboundIpPrefixIds"))

    @outbound_ip_prefix_ids.setter
    def outbound_ip_prefix_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileLoadBalancerProfileOutputReference, "outbound_ip_prefix_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outboundIpPrefixIds", value)

    @builtins.property
    @jsii.member(jsii_name="outboundPortsAllocated")
    def outbound_ports_allocated(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "outboundPortsAllocated"))

    @outbound_ports_allocated.setter
    def outbound_ports_allocated(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileLoadBalancerProfileOutputReference, "outbound_ports_allocated").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outboundPortsAllocated", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KubernetesClusterNetworkProfileLoadBalancerProfile]:
        return typing.cast(typing.Optional[KubernetesClusterNetworkProfileLoadBalancerProfile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterNetworkProfileLoadBalancerProfile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileLoadBalancerProfileOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterNetworkProfileNatGatewayProfile",
    jsii_struct_bases=[],
    name_mapping={
        "idle_timeout_in_minutes": "idleTimeoutInMinutes",
        "managed_outbound_ip_count": "managedOutboundIpCount",
    },
)
class KubernetesClusterNetworkProfileNatGatewayProfile:
    def __init__(
        self,
        *,
        idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        managed_outbound_ip_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#idle_timeout_in_minutes KubernetesCluster#idle_timeout_in_minutes}.
        :param managed_outbound_ip_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#managed_outbound_ip_count KubernetesCluster#managed_outbound_ip_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterNetworkProfileNatGatewayProfile.__init__)
            check_type(argname="argument idle_timeout_in_minutes", value=idle_timeout_in_minutes, expected_type=type_hints["idle_timeout_in_minutes"])
            check_type(argname="argument managed_outbound_ip_count", value=managed_outbound_ip_count, expected_type=type_hints["managed_outbound_ip_count"])
        self._values: typing.Dict[str, typing.Any] = {}
        if idle_timeout_in_minutes is not None:
            self._values["idle_timeout_in_minutes"] = idle_timeout_in_minutes
        if managed_outbound_ip_count is not None:
            self._values["managed_outbound_ip_count"] = managed_outbound_ip_count

    @builtins.property
    def idle_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#idle_timeout_in_minutes KubernetesCluster#idle_timeout_in_minutes}.'''
        result = self._values.get("idle_timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def managed_outbound_ip_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#managed_outbound_ip_count KubernetesCluster#managed_outbound_ip_count}.'''
        result = self._values.get("managed_outbound_ip_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterNetworkProfileNatGatewayProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterNetworkProfileNatGatewayProfileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterNetworkProfileNatGatewayProfileOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterNetworkProfileNatGatewayProfileOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdleTimeoutInMinutes")
    def reset_idle_timeout_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleTimeoutInMinutes", []))

    @jsii.member(jsii_name="resetManagedOutboundIpCount")
    def reset_managed_outbound_ip_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedOutboundIpCount", []))

    @builtins.property
    @jsii.member(jsii_name="effectiveOutboundIps")
    def effective_outbound_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "effectiveOutboundIps"))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInMinutesInput")
    def idle_timeout_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleTimeoutInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="managedOutboundIpCountInput")
    def managed_outbound_ip_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "managedOutboundIpCountInput"))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleTimeoutInMinutes"))

    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileNatGatewayProfileOutputReference, "idle_timeout_in_minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleTimeoutInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="managedOutboundIpCount")
    def managed_outbound_ip_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "managedOutboundIpCount"))

    @managed_outbound_ip_count.setter
    def managed_outbound_ip_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileNatGatewayProfileOutputReference, "managed_outbound_ip_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedOutboundIpCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KubernetesClusterNetworkProfileNatGatewayProfile]:
        return typing.cast(typing.Optional[KubernetesClusterNetworkProfileNatGatewayProfile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterNetworkProfileNatGatewayProfile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileNatGatewayProfileOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterNetworkProfileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterNetworkProfileOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterNetworkProfileOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLoadBalancerProfile")
    def put_load_balancer_profile(
        self,
        *,
        idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        managed_outbound_ip_count: typing.Optional[jsii.Number] = None,
        managed_outbound_ipv6_count: typing.Optional[jsii.Number] = None,
        outbound_ip_address_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        outbound_ip_prefix_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        outbound_ports_allocated: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#idle_timeout_in_minutes KubernetesCluster#idle_timeout_in_minutes}.
        :param managed_outbound_ip_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#managed_outbound_ip_count KubernetesCluster#managed_outbound_ip_count}.
        :param managed_outbound_ipv6_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#managed_outbound_ipv6_count KubernetesCluster#managed_outbound_ipv6_count}.
        :param outbound_ip_address_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#outbound_ip_address_ids KubernetesCluster#outbound_ip_address_ids}.
        :param outbound_ip_prefix_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#outbound_ip_prefix_ids KubernetesCluster#outbound_ip_prefix_ids}.
        :param outbound_ports_allocated: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#outbound_ports_allocated KubernetesCluster#outbound_ports_allocated}.
        '''
        value = KubernetesClusterNetworkProfileLoadBalancerProfile(
            idle_timeout_in_minutes=idle_timeout_in_minutes,
            managed_outbound_ip_count=managed_outbound_ip_count,
            managed_outbound_ipv6_count=managed_outbound_ipv6_count,
            outbound_ip_address_ids=outbound_ip_address_ids,
            outbound_ip_prefix_ids=outbound_ip_prefix_ids,
            outbound_ports_allocated=outbound_ports_allocated,
        )

        return typing.cast(None, jsii.invoke(self, "putLoadBalancerProfile", [value]))

    @jsii.member(jsii_name="putNatGatewayProfile")
    def put_nat_gateway_profile(
        self,
        *,
        idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        managed_outbound_ip_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#idle_timeout_in_minutes KubernetesCluster#idle_timeout_in_minutes}.
        :param managed_outbound_ip_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#managed_outbound_ip_count KubernetesCluster#managed_outbound_ip_count}.
        '''
        value = KubernetesClusterNetworkProfileNatGatewayProfile(
            idle_timeout_in_minutes=idle_timeout_in_minutes,
            managed_outbound_ip_count=managed_outbound_ip_count,
        )

        return typing.cast(None, jsii.invoke(self, "putNatGatewayProfile", [value]))

    @jsii.member(jsii_name="resetDnsServiceIp")
    def reset_dns_service_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsServiceIp", []))

    @jsii.member(jsii_name="resetDockerBridgeCidr")
    def reset_docker_bridge_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerBridgeCidr", []))

    @jsii.member(jsii_name="resetIpVersions")
    def reset_ip_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpVersions", []))

    @jsii.member(jsii_name="resetLoadBalancerProfile")
    def reset_load_balancer_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerProfile", []))

    @jsii.member(jsii_name="resetLoadBalancerSku")
    def reset_load_balancer_sku(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerSku", []))

    @jsii.member(jsii_name="resetNatGatewayProfile")
    def reset_nat_gateway_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNatGatewayProfile", []))

    @jsii.member(jsii_name="resetNetworkMode")
    def reset_network_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkMode", []))

    @jsii.member(jsii_name="resetNetworkPolicy")
    def reset_network_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkPolicy", []))

    @jsii.member(jsii_name="resetOutboundType")
    def reset_outbound_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutboundType", []))

    @jsii.member(jsii_name="resetPodCidr")
    def reset_pod_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPodCidr", []))

    @jsii.member(jsii_name="resetPodCidrs")
    def reset_pod_cidrs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPodCidrs", []))

    @jsii.member(jsii_name="resetServiceCidr")
    def reset_service_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceCidr", []))

    @jsii.member(jsii_name="resetServiceCidrs")
    def reset_service_cidrs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceCidrs", []))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerProfile")
    def load_balancer_profile(
        self,
    ) -> KubernetesClusterNetworkProfileLoadBalancerProfileOutputReference:
        return typing.cast(KubernetesClusterNetworkProfileLoadBalancerProfileOutputReference, jsii.get(self, "loadBalancerProfile"))

    @builtins.property
    @jsii.member(jsii_name="natGatewayProfile")
    def nat_gateway_profile(
        self,
    ) -> KubernetesClusterNetworkProfileNatGatewayProfileOutputReference:
        return typing.cast(KubernetesClusterNetworkProfileNatGatewayProfileOutputReference, jsii.get(self, "natGatewayProfile"))

    @builtins.property
    @jsii.member(jsii_name="dnsServiceIpInput")
    def dns_service_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsServiceIpInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerBridgeCidrInput")
    def docker_bridge_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerBridgeCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="ipVersionsInput")
    def ip_versions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerProfileInput")
    def load_balancer_profile_input(
        self,
    ) -> typing.Optional[KubernetesClusterNetworkProfileLoadBalancerProfile]:
        return typing.cast(typing.Optional[KubernetesClusterNetworkProfileLoadBalancerProfile], jsii.get(self, "loadBalancerProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerSkuInput")
    def load_balancer_sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancerSkuInput"))

    @builtins.property
    @jsii.member(jsii_name="natGatewayProfileInput")
    def nat_gateway_profile_input(
        self,
    ) -> typing.Optional[KubernetesClusterNetworkProfileNatGatewayProfile]:
        return typing.cast(typing.Optional[KubernetesClusterNetworkProfileNatGatewayProfile], jsii.get(self, "natGatewayProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="networkModeInput")
    def network_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkModeInput"))

    @builtins.property
    @jsii.member(jsii_name="networkPluginInput")
    def network_plugin_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkPluginInput"))

    @builtins.property
    @jsii.member(jsii_name="networkPolicyInput")
    def network_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="outboundTypeInput")
    def outbound_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outboundTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="podCidrInput")
    def pod_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "podCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="podCidrsInput")
    def pod_cidrs_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "podCidrsInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceCidrInput")
    def service_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceCidrsInput")
    def service_cidrs_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serviceCidrsInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsServiceIp")
    def dns_service_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsServiceIp"))

    @dns_service_ip.setter
    def dns_service_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileOutputReference, "dns_service_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsServiceIp", value)

    @builtins.property
    @jsii.member(jsii_name="dockerBridgeCidr")
    def docker_bridge_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerBridgeCidr"))

    @docker_bridge_cidr.setter
    def docker_bridge_cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileOutputReference, "docker_bridge_cidr").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerBridgeCidr", value)

    @builtins.property
    @jsii.member(jsii_name="ipVersions")
    def ip_versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipVersions"))

    @ip_versions.setter
    def ip_versions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileOutputReference, "ip_versions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipVersions", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerSku")
    def load_balancer_sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancerSku"))

    @load_balancer_sku.setter
    def load_balancer_sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileOutputReference, "load_balancer_sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerSku", value)

    @builtins.property
    @jsii.member(jsii_name="networkMode")
    def network_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkMode"))

    @network_mode.setter
    def network_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileOutputReference, "network_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkMode", value)

    @builtins.property
    @jsii.member(jsii_name="networkPlugin")
    def network_plugin(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkPlugin"))

    @network_plugin.setter
    def network_plugin(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileOutputReference, "network_plugin").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkPlugin", value)

    @builtins.property
    @jsii.member(jsii_name="networkPolicy")
    def network_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkPolicy"))

    @network_policy.setter
    def network_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileOutputReference, "network_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="outboundType")
    def outbound_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outboundType"))

    @outbound_type.setter
    def outbound_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileOutputReference, "outbound_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outboundType", value)

    @builtins.property
    @jsii.member(jsii_name="podCidr")
    def pod_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "podCidr"))

    @pod_cidr.setter
    def pod_cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileOutputReference, "pod_cidr").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "podCidr", value)

    @builtins.property
    @jsii.member(jsii_name="podCidrs")
    def pod_cidrs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "podCidrs"))

    @pod_cidrs.setter
    def pod_cidrs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileOutputReference, "pod_cidrs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "podCidrs", value)

    @builtins.property
    @jsii.member(jsii_name="serviceCidr")
    def service_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceCidr"))

    @service_cidr.setter
    def service_cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileOutputReference, "service_cidr").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceCidr", value)

    @builtins.property
    @jsii.member(jsii_name="serviceCidrs")
    def service_cidrs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "serviceCidrs"))

    @service_cidrs.setter
    def service_cidrs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileOutputReference, "service_cidrs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceCidrs", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterNetworkProfile]:
        return typing.cast(typing.Optional[KubernetesClusterNetworkProfile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterNetworkProfile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterNetworkProfileOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterOmsAgent",
    jsii_struct_bases=[],
    name_mapping={"log_analytics_workspace_id": "logAnalyticsWorkspaceId"},
)
class KubernetesClusterOmsAgent:
    def __init__(self, *, log_analytics_workspace_id: builtins.str) -> None:
        '''
        :param log_analytics_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#log_analytics_workspace_id KubernetesCluster#log_analytics_workspace_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterOmsAgent.__init__)
            check_type(argname="argument log_analytics_workspace_id", value=log_analytics_workspace_id, expected_type=type_hints["log_analytics_workspace_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "log_analytics_workspace_id": log_analytics_workspace_id,
        }

    @builtins.property
    def log_analytics_workspace_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#log_analytics_workspace_id KubernetesCluster#log_analytics_workspace_id}.'''
        result = self._values.get("log_analytics_workspace_id")
        assert result is not None, "Required property 'log_analytics_workspace_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterOmsAgent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterOmsAgentOmsAgentIdentity",
    jsii_struct_bases=[],
    name_mapping={},
)
class KubernetesClusterOmsAgentOmsAgentIdentity:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterOmsAgentOmsAgentIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterOmsAgentOmsAgentIdentityList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterOmsAgentOmsAgentIdentityList",
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
            type_hints = typing.get_type_hints(KubernetesClusterOmsAgentOmsAgentIdentityList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KubernetesClusterOmsAgentOmsAgentIdentityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterOmsAgentOmsAgentIdentityList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesClusterOmsAgentOmsAgentIdentityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterOmsAgentOmsAgentIdentityList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(KubernetesClusterOmsAgentOmsAgentIdentityList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(KubernetesClusterOmsAgentOmsAgentIdentityList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class KubernetesClusterOmsAgentOmsAgentIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterOmsAgentOmsAgentIdentityOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterOmsAgentOmsAgentIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectId"))

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentityId")
    def user_assigned_identity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userAssignedIdentityId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KubernetesClusterOmsAgentOmsAgentIdentity]:
        return typing.cast(typing.Optional[KubernetesClusterOmsAgentOmsAgentIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterOmsAgentOmsAgentIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterOmsAgentOmsAgentIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterOmsAgentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterOmsAgentOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterOmsAgentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="omsAgentIdentity")
    def oms_agent_identity(self) -> KubernetesClusterOmsAgentOmsAgentIdentityList:
        return typing.cast(KubernetesClusterOmsAgentOmsAgentIdentityList, jsii.get(self, "omsAgentIdentity"))

    @builtins.property
    @jsii.member(jsii_name="logAnalyticsWorkspaceIdInput")
    def log_analytics_workspace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logAnalyticsWorkspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logAnalyticsWorkspaceId"))

    @log_analytics_workspace_id.setter
    def log_analytics_workspace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterOmsAgentOutputReference, "log_analytics_workspace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logAnalyticsWorkspaceId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterOmsAgent]:
        return typing.cast(typing.Optional[KubernetesClusterOmsAgent], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[KubernetesClusterOmsAgent]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterOmsAgentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterServicePrincipal",
    jsii_struct_bases=[],
    name_mapping={"client_id": "clientId", "client_secret": "clientSecret"},
)
class KubernetesClusterServicePrincipal:
    def __init__(self, *, client_id: builtins.str, client_secret: builtins.str) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#client_id KubernetesCluster#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#client_secret KubernetesCluster#client_secret}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterServicePrincipal.__init__)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
        }

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#client_id KubernetesCluster#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#client_secret KubernetesCluster#client_secret}.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterServicePrincipal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterServicePrincipalOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterServicePrincipalOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterServicePrincipalOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterServicePrincipalOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterServicePrincipalOutputReference, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterServicePrincipal]:
        return typing.cast(typing.Optional[KubernetesClusterServicePrincipal], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterServicePrincipal],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterServicePrincipalOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class KubernetesClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#create KubernetesCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#delete KubernetesCluster#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#read KubernetesCluster#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#update KubernetesCluster#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#create KubernetesCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#delete KubernetesCluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#read KubernetesCluster#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#update KubernetesCluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(KubernetesClusterTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KubernetesClusterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KubernetesClusterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KubernetesClusterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterWindowsProfile",
    jsii_struct_bases=[],
    name_mapping={
        "admin_username": "adminUsername",
        "admin_password": "adminPassword",
        "gmsa": "gmsa",
        "license": "license",
    },
)
class KubernetesClusterWindowsProfile:
    def __init__(
        self,
        *,
        admin_username: builtins.str,
        admin_password: typing.Optional[builtins.str] = None,
        gmsa: typing.Optional[typing.Union["KubernetesClusterWindowsProfileGmsa", typing.Dict[str, typing.Any]]] = None,
        license: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#admin_username KubernetesCluster#admin_username}.
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#admin_password KubernetesCluster#admin_password}.
        :param gmsa: gmsa block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#gmsa KubernetesCluster#gmsa}
        :param license: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#license KubernetesCluster#license}.
        '''
        if isinstance(gmsa, dict):
            gmsa = KubernetesClusterWindowsProfileGmsa(**gmsa)
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterWindowsProfile.__init__)
            check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
            check_type(argname="argument admin_password", value=admin_password, expected_type=type_hints["admin_password"])
            check_type(argname="argument gmsa", value=gmsa, expected_type=type_hints["gmsa"])
            check_type(argname="argument license", value=license, expected_type=type_hints["license"])
        self._values: typing.Dict[str, typing.Any] = {
            "admin_username": admin_username,
        }
        if admin_password is not None:
            self._values["admin_password"] = admin_password
        if gmsa is not None:
            self._values["gmsa"] = gmsa
        if license is not None:
            self._values["license"] = license

    @builtins.property
    def admin_username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#admin_username KubernetesCluster#admin_username}.'''
        result = self._values.get("admin_username")
        assert result is not None, "Required property 'admin_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#admin_password KubernetesCluster#admin_password}.'''
        result = self._values.get("admin_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gmsa(self) -> typing.Optional["KubernetesClusterWindowsProfileGmsa"]:
        '''gmsa block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#gmsa KubernetesCluster#gmsa}
        '''
        result = self._values.get("gmsa")
        return typing.cast(typing.Optional["KubernetesClusterWindowsProfileGmsa"], result)

    @builtins.property
    def license(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#license KubernetesCluster#license}.'''
        result = self._values.get("license")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterWindowsProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterWindowsProfileGmsa",
    jsii_struct_bases=[],
    name_mapping={"dns_server": "dnsServer", "root_domain": "rootDomain"},
)
class KubernetesClusterWindowsProfileGmsa:
    def __init__(self, *, dns_server: builtins.str, root_domain: builtins.str) -> None:
        '''
        :param dns_server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#dns_server KubernetesCluster#dns_server}.
        :param root_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#root_domain KubernetesCluster#root_domain}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesClusterWindowsProfileGmsa.__init__)
            check_type(argname="argument dns_server", value=dns_server, expected_type=type_hints["dns_server"])
            check_type(argname="argument root_domain", value=root_domain, expected_type=type_hints["root_domain"])
        self._values: typing.Dict[str, typing.Any] = {
            "dns_server": dns_server,
            "root_domain": root_domain,
        }

    @builtins.property
    def dns_server(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#dns_server KubernetesCluster#dns_server}.'''
        result = self._values.get("dns_server")
        assert result is not None, "Required property 'dns_server' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def root_domain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#root_domain KubernetesCluster#root_domain}.'''
        result = self._values.get("root_domain")
        assert result is not None, "Required property 'root_domain' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterWindowsProfileGmsa(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterWindowsProfileGmsaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterWindowsProfileGmsaOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterWindowsProfileGmsaOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dnsServerInput")
    def dns_server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsServerInput"))

    @builtins.property
    @jsii.member(jsii_name="rootDomainInput")
    def root_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsServer")
    def dns_server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsServer"))

    @dns_server.setter
    def dns_server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterWindowsProfileGmsaOutputReference, "dns_server").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsServer", value)

    @builtins.property
    @jsii.member(jsii_name="rootDomain")
    def root_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootDomain"))

    @root_domain.setter
    def root_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterWindowsProfileGmsaOutputReference, "root_domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootDomain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterWindowsProfileGmsa]:
        return typing.cast(typing.Optional[KubernetesClusterWindowsProfileGmsa], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterWindowsProfileGmsa],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterWindowsProfileGmsaOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterWindowsProfileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kubernetesCluster.KubernetesClusterWindowsProfileOutputReference",
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
            type_hints = typing.get_type_hints(KubernetesClusterWindowsProfileOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGmsa")
    def put_gmsa(self, *, dns_server: builtins.str, root_domain: builtins.str) -> None:
        '''
        :param dns_server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#dns_server KubernetesCluster#dns_server}.
        :param root_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster#root_domain KubernetesCluster#root_domain}.
        '''
        value = KubernetesClusterWindowsProfileGmsa(
            dns_server=dns_server, root_domain=root_domain
        )

        return typing.cast(None, jsii.invoke(self, "putGmsa", [value]))

    @jsii.member(jsii_name="resetAdminPassword")
    def reset_admin_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminPassword", []))

    @jsii.member(jsii_name="resetGmsa")
    def reset_gmsa(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGmsa", []))

    @jsii.member(jsii_name="resetLicense")
    def reset_license(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLicense", []))

    @builtins.property
    @jsii.member(jsii_name="gmsa")
    def gmsa(self) -> KubernetesClusterWindowsProfileGmsaOutputReference:
        return typing.cast(KubernetesClusterWindowsProfileGmsaOutputReference, jsii.get(self, "gmsa"))

    @builtins.property
    @jsii.member(jsii_name="adminPasswordInput")
    def admin_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="adminUsernameInput")
    def admin_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="gmsaInput")
    def gmsa_input(self) -> typing.Optional[KubernetesClusterWindowsProfileGmsa]:
        return typing.cast(typing.Optional[KubernetesClusterWindowsProfileGmsa], jsii.get(self, "gmsaInput"))

    @builtins.property
    @jsii.member(jsii_name="licenseInput")
    def license_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenseInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPassword")
    def admin_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminPassword"))

    @admin_password.setter
    def admin_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterWindowsProfileOutputReference, "admin_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminPassword", value)

    @builtins.property
    @jsii.member(jsii_name="adminUsername")
    def admin_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminUsername"))

    @admin_username.setter
    def admin_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterWindowsProfileOutputReference, "admin_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUsername", value)

    @builtins.property
    @jsii.member(jsii_name="license")
    def license(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "license"))

    @license.setter
    def license(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterWindowsProfileOutputReference, "license").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "license", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KubernetesClusterWindowsProfile]:
        return typing.cast(typing.Optional[KubernetesClusterWindowsProfile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KubernetesClusterWindowsProfile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesClusterWindowsProfileOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KubernetesCluster",
    "KubernetesClusterAciConnectorLinux",
    "KubernetesClusterAciConnectorLinuxOutputReference",
    "KubernetesClusterAutoScalerProfile",
    "KubernetesClusterAutoScalerProfileOutputReference",
    "KubernetesClusterAzureActiveDirectoryRoleBasedAccessControl",
    "KubernetesClusterAzureActiveDirectoryRoleBasedAccessControlOutputReference",
    "KubernetesClusterConfig",
    "KubernetesClusterDefaultNodePool",
    "KubernetesClusterDefaultNodePoolKubeletConfig",
    "KubernetesClusterDefaultNodePoolKubeletConfigOutputReference",
    "KubernetesClusterDefaultNodePoolLinuxOsConfig",
    "KubernetesClusterDefaultNodePoolLinuxOsConfigOutputReference",
    "KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfig",
    "KubernetesClusterDefaultNodePoolLinuxOsConfigSysctlConfigOutputReference",
    "KubernetesClusterDefaultNodePoolOutputReference",
    "KubernetesClusterDefaultNodePoolUpgradeSettings",
    "KubernetesClusterDefaultNodePoolUpgradeSettingsOutputReference",
    "KubernetesClusterHttpProxyConfig",
    "KubernetesClusterHttpProxyConfigOutputReference",
    "KubernetesClusterIdentity",
    "KubernetesClusterIdentityOutputReference",
    "KubernetesClusterIngressApplicationGateway",
    "KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentity",
    "KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentityList",
    "KubernetesClusterIngressApplicationGatewayIngressApplicationGatewayIdentityOutputReference",
    "KubernetesClusterIngressApplicationGatewayOutputReference",
    "KubernetesClusterKeyVaultSecretsProvider",
    "KubernetesClusterKeyVaultSecretsProviderOutputReference",
    "KubernetesClusterKeyVaultSecretsProviderSecretIdentity",
    "KubernetesClusterKeyVaultSecretsProviderSecretIdentityList",
    "KubernetesClusterKeyVaultSecretsProviderSecretIdentityOutputReference",
    "KubernetesClusterKubeAdminConfig",
    "KubernetesClusterKubeAdminConfigList",
    "KubernetesClusterKubeAdminConfigOutputReference",
    "KubernetesClusterKubeConfig",
    "KubernetesClusterKubeConfigList",
    "KubernetesClusterKubeConfigOutputReference",
    "KubernetesClusterKubeletIdentity",
    "KubernetesClusterKubeletIdentityOutputReference",
    "KubernetesClusterLinuxProfile",
    "KubernetesClusterLinuxProfileOutputReference",
    "KubernetesClusterLinuxProfileSshKey",
    "KubernetesClusterLinuxProfileSshKeyOutputReference",
    "KubernetesClusterMaintenanceWindow",
    "KubernetesClusterMaintenanceWindowAllowed",
    "KubernetesClusterMaintenanceWindowAllowedList",
    "KubernetesClusterMaintenanceWindowAllowedOutputReference",
    "KubernetesClusterMaintenanceWindowNotAllowed",
    "KubernetesClusterMaintenanceWindowNotAllowedList",
    "KubernetesClusterMaintenanceWindowNotAllowedOutputReference",
    "KubernetesClusterMaintenanceWindowOutputReference",
    "KubernetesClusterMicrosoftDefender",
    "KubernetesClusterMicrosoftDefenderOutputReference",
    "KubernetesClusterNetworkProfile",
    "KubernetesClusterNetworkProfileLoadBalancerProfile",
    "KubernetesClusterNetworkProfileLoadBalancerProfileOutputReference",
    "KubernetesClusterNetworkProfileNatGatewayProfile",
    "KubernetesClusterNetworkProfileNatGatewayProfileOutputReference",
    "KubernetesClusterNetworkProfileOutputReference",
    "KubernetesClusterOmsAgent",
    "KubernetesClusterOmsAgentOmsAgentIdentity",
    "KubernetesClusterOmsAgentOmsAgentIdentityList",
    "KubernetesClusterOmsAgentOmsAgentIdentityOutputReference",
    "KubernetesClusterOmsAgentOutputReference",
    "KubernetesClusterServicePrincipal",
    "KubernetesClusterServicePrincipalOutputReference",
    "KubernetesClusterTimeouts",
    "KubernetesClusterTimeoutsOutputReference",
    "KubernetesClusterWindowsProfile",
    "KubernetesClusterWindowsProfileGmsa",
    "KubernetesClusterWindowsProfileGmsaOutputReference",
    "KubernetesClusterWindowsProfileOutputReference",
]

publication.publish()
